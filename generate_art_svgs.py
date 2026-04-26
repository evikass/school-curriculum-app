#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 10 Art (Искусство) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/art"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRIMARY = "#880E4F"
PRIMARY_LIGHT = "#EC407A"
ACCENT = "#C2185B"
BG_TOP = "#FCE4EC"
BG_BOT = "#FFFFFF"

lessons = [
    {
        "num": 1,
        "title": "Древнее искусство",
        "subtitle": "Искусство — Урок 1",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Cave painting illustration -->
    <rect x="25" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="95" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Наскальная живопись</text>
    <rect x="35" y="120" width="50" height="35" rx="3" fill="#FFF3E0" stroke="#880E4F" stroke-width="1"/>
    <ellipse cx="60" cy="135" rx="12" ry="8" fill="#880E4F" opacity="0.3"/>
    <path d="M50,140 L55,130 L60,138 L65,128 L70,140" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <rect x="95" y="120" width="55" height="35" rx="3" fill="#FFF3E0" stroke="#880E4F" stroke-width="1"/>
    <circle cx="122" cy="133" r="8" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <line x1="122" y1="141" x2="122" y2="152" stroke="#880E4F" stroke-width="1.5"/>
    <line x1="115" y1="146" x2="129" y2="146" stroke="#880E4F" stroke-width="1.5"/>
    <text x="95" y="170" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Ласко, Альтамира ~15000 до н.э.</text>

    <!-- Egyptian art -->
    <rect x="180" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="250" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Искусство Египта</text>
    <!-- Pyramid -->
    <polygon points="210,160 230,125 250,160" fill="#880E4F" opacity="0.2" stroke="#880E4F" stroke-width="1"/>
    <!-- Obelisk -->
    <polygon points="265,160 272,130 279,160" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="1"/>
    <!-- Eye of Horus -->
    <ellipse cx="300" cy="140" rx="10" ry="6" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <circle cx="300" cy="140" r="3" fill="#880E4F" opacity="0.5"/>
    <line x1="310" y1="140" x2="318" y2="137" stroke="#880E4F" stroke-width="1"/>
    <text x="250" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Пирамиды, сфинкс, иероглифы</text>

    <!-- Greek art -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Искусство Греции</text>
    <!-- Column -->
    <rect x="365" y="125" width="10" height="40" fill="#880E4F" opacity="0.25" stroke="#880E4F" stroke-width="1"/>
    <rect x="360" y="120" width="20" height="5" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="1"/>
    <rect x="358" y="165" width="24" height="5" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="1"/>
    <!-- Vase -->
    <ellipse cx="420" cy="145" rx="15" ry="20" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <rect x="415" y="125" width="10" height="5" fill="#880E4F" opacity="0.3"/>
    <line x1="415" y1="130" x2="410" y2="135" stroke="#880E4F" stroke-width="1"/>
    <line x1="425" y1="130" x2="430" y2="135" stroke="#880E4F" stroke-width="1"/>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Ордера, вазопись, скульптура</text>

    <!-- Key concepts row -->
    <rect x="25" y="190" width="220" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Ключевые понятия:</text>
    <text x="135" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Канон · Символизм · Ритуал</text>
    <text x="135" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Фреска · Рельеф · Монумент</text>

    <!-- Timeline -->
    <rect x="260" y="190" width="215" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Хронология:</text>
    <line x1="275" y1="218" x2="460" y2="218" stroke="#880E4F" stroke-width="1.5" opacity="0.5"/>
    <circle cx="290" cy="218" r="3" fill="#880E4F"/>
    <text x="290" y="228" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">30000</text>
    <circle cx="340" cy="218" r="3" fill="#880E4F"/>
    <text x="340" y="228" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">3000</text>
    <circle cx="400" cy="218" r="3" fill="#880E4F"/>
    <text x="400" y="228" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">500 до н.э.</text>
    <circle cx="450" cy="218" r="3" fill="#C2185B"/>
    <text x="450" y="228" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">I в.</text>

    <!-- Artists / Works -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Великие произведения:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Пирамиды Гизы · Парфенон · Ника Самофракийская · Росписи Помпей</text>"""
    },
    {
        "num": 2,
        "title": "Искусство Средневековья",
        "subtitle": "Искусство — Урок 2",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Byzantine art -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Византия</text>
    <!-- Dome/Church -->
    <rect x="55" y="135" width="40" height="30" fill="#880E4F" opacity="0.15" stroke="#880E4F" stroke-width="1"/>
    <ellipse cx="75" cy="135" rx="20" ry="12" fill="#880E4F" opacity="0.1" stroke="#880E4F" stroke-width="1"/>
    <line x1="75" y1="123" x2="75" y2="118" stroke="#880E4F" stroke-width="1.5"/>
    <line x1="70" y1="118" x2="80" y2="118" stroke="#880E4F" stroke-width="1.5"/>
    <!-- Cross -->
    <line x1="115" y1="125" x2="115" y2="158" stroke="#880E4F" stroke-width="2.5"/>
    <line x1="105" y1="138" x2="125" y2="138" stroke="#880E4F" stroke-width="2.5"/>
    <!-- Halo -->
    <circle cx="140" cy="130" r="10" fill="none" stroke="#C2185B" stroke-width="1.5" opacity="0.5"/>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Мозаика, иконы, храмы</text>

    <!-- Romanesque -->
    <rect x="180" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="250" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Романский стиль</text>
    <!-- Thick wall / arch -->
    <rect x="200" y="125" width="15" height="40" fill="#880E4F" opacity="0.2" stroke="#880E4F" stroke-width="1"/>
    <rect x="240" y="125" width="15" height="40" fill="#880E4F" opacity="0.2" stroke="#880E4F" stroke-width="1"/>
    <path d="M200,125 Q222,105 240,125" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <rect x="210" y="125" width="35" height="35" fill="#880E4F" opacity="0.08"/>
    <text x="250" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">X–XII вв. Массивность</text>

    <!-- Gothic -->
    <rect x="330" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="400" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Готика</text>
    <!-- Pointed arch -->
    <path d="M360,160 L380,120 L400,160" fill="none" stroke="#880E4F" stroke-width="2"/>
    <!-- Rose window -->
    <circle cx="435" cy="140" r="15" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <circle cx="435" cy="140" r="10" fill="none" stroke="#C2185B" stroke-width="1" opacity="0.5"/>
    <line x1="435" y1="125" x2="435" y2="155" stroke="#880E4F" stroke-width="0.5"/>
    <line x1="420" y1="140" x2="450" y2="140" stroke="#880E4F" stroke-width="0.5"/>
    <!-- Stained glass effect -->
    <circle cx="435" cy="140" r="5" fill="#880E4F" opacity="0.15"/>
    <text x="400" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Витражи, соборы, стрельчатые арки</text>

    <!-- Key concepts -->
    <rect x="25" y="190" width="220" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Ключевые понятия:</text>
    <text x="135" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Символизм · Аллегория · Догмат</text>
    <text x="135" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Иконопись · Миниатюра · Фреска</text>

    <!-- Period timeline -->
    <rect x="260" y="190" width="215" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Периоды:</text>
    <line x1="275" y1="220" x2="460" y2="220" stroke="#880E4F" stroke-width="1.5" opacity="0.5"/>
    <circle cx="290" cy="220" r="3" fill="#880E4F"/>
    <text x="290" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">V в.</text>
    <circle cx="340" cy="220" r="3" fill="#880E4F"/>
    <text x="340" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">X в.</text>
    <circle cx="400" cy="220" r="3" fill="#C2185B"/>
    <text x="400" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">XII в.</text>
    <circle cx="450" cy="220" r="3" fill="#EC407A"/>
    <text x="450" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">XV в.</text>

    <!-- Works -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Шедевры Средневековья:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Собор Нотр-Дам · Собор Св. Витта · Мозаики Равенны · Книги часов</text>"""
    },
    {
        "num": 3,
        "title": "Возрождение",
        "subtitle": "Искусство — Урок 3",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Renaissance Man -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Ренессанс</text>
    <!-- Vitruvian Man simplified -->
    <circle cx="97" cy="145" r="22" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <circle cx="97" cy="145" r="14" fill="none" stroke="#C2185B" stroke-width="1" opacity="0.5"/>
    <line x1="97" y1="135" x2="97" y2="160" stroke="#880E4F" stroke-width="1.5"/>
    <line x1="83" y1="145" x2="111" y2="145" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Антропоцентризм, гармония</text>

    <!-- Perspective diagram -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Перспектива</text>
    <!-- Vanishing point -->
    <circle cx="252" cy="140" r="3" fill="#880E4F"/>
    <text x="252" y="135" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">точка схода</text>
    <!-- Perspective lines -->
    <line x1="252" y1="140" x2="195" y2="170" stroke="#880E4F" stroke-width="1" opacity="0.6"/>
    <line x1="252" y1="140" x2="310" y2="170" stroke="#880E4F" stroke-width="1" opacity="0.6"/>
    <line x1="252" y1="140" x2="220" y2="170" stroke="#C2185B" stroke-width="1" opacity="0.4"/>
    <line x1="252" y1="140" x2="285" y2="170" stroke="#C2185B" stroke-width="1" opacity="0.4"/>
    <!-- Ground line -->
    <line x1="195" y1="170" x2="310" y2="170" stroke="#880E4F" stroke-width="1"/>
    <text x="252" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Линейная, воздушная</text>

    <!-- Great Masters -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Титаны</text>
    <!-- Three columns for 3 masters -->
    <text x="365" y="130" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="#880E4F" text-anchor="middle">Леонардо</text>
    <text x="365" y="142" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Мона Лиза</text>
    <text x="365" y="152" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Тайная вечеря</text>
    <text x="405" y="130" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="#880E4F" text-anchor="middle">Микеланджело</text>
    <text x="405" y="142" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Давид</text>
    <text x="405" y="152" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сикстинская</text>
    <text x="445" y="130" font-family="Arial,sans-serif" font-size="8" font-weight="bold" fill="#880E4F" text-anchor="middle">Рафаэль</text>
    <text x="445" y="142" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Сикстинская</text>
    <text x="445" y="152" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">мадонна</text>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">XIV–XVI вв.</text>

    <!-- Key concepts -->
    <rect x="25" y="190" width="220" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Ключевые понятия:</text>
    <text x="135" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Гуманизм · Сфумато · Пропорции</text>
    <text x="135" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Золотое сечение · Антропоцентризм</text>

    <!-- Techniques -->
    <rect x="260" y="190" width="215" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Техники:</text>
    <text x="367" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Сфумато · Кьяроскуро · Гризайль</text>
    <text x="367" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Масляная живопись · Фреска</text>

    <!-- Works -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Шедевры Возрождения:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Мона Лиза · Давид · Афинская школа · Рождение Венеры · Сикстинская капелла</text>"""
    },
    {
        "num": 4,
        "title": "Русское искусство",
        "subtitle": "Искусство — Урок 4",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Icon painting -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Иконопись</text>
    <!-- Icon frame -->
    <rect x="55" y="118" width="40" height="50" rx="2" fill="#FFF8E1" stroke="#880E4F" stroke-width="1.5"/>
    <!-- Halo -->
    <circle cx="75" cy="133" r="10" fill="none" stroke="#C2185B" stroke-width="1" opacity="0.6"/>
    <!-- Face -->
    <ellipse cx="75" cy="133" rx="6" ry="7" fill="none" stroke="#880E4F" stroke-width="1"/>
    <!-- Body -->
    <path d="M65,145 Q75,140 85,145 L82,160 L68,160 Z" fill="#880E4F" opacity="0.15" stroke="#880E4F" stroke-width="1"/>
    <!-- Text labels -->
    <text x="120" y="132" font-family="Arial,sans-serif" font-size="7" fill="#555">Андрей Рублёв</text>
    <text x="120" y="142" font-family="Arial,sans-serif" font-size="7" fill="#555">Феофан Грек</text>
    <text x="120" y="152" font-family="Arial,sans-serif" font-size="7" fill="#555">Дионисий</text>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Троица, XIV–XV вв.</text>

    <!-- Russian realism -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Реализм XIX в.</text>
    <!-- Palette -->
    <ellipse cx="235" cy="145" rx="18" ry="12" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <circle cx="228" cy="142" r="3" fill="#880E4F" opacity="0.4"/>
    <circle cx="237" cy="138" r="3" fill="#C2185B" opacity="0.4"/>
    <circle cx="246" cy="142" r="3" fill="#EC407A" opacity="0.4"/>
    <!-- Brush -->
    <line x1="253" y1="145" x2="270" y2="135" stroke="#880E4F" stroke-width="2"/>
    <text x="252" y="168" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Репин · Суриков</text>
    <text x="252" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Левитан · Шишкин</text>

    <!-- Avant-garde -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Авангард</text>
    <!-- Abstract shapes -->
    <rect x="360" y="120" width="25" height="25" fill="#880E4F" opacity="0.3" transform="rotate(15,372,132)"/>
    <circle cx="415" cy="135" r="12" fill="none" stroke="#C2185B" stroke-width="2"/>
    <polygon points="390,160 400,140 410,160" fill="#880E4F" opacity="0.2"/>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Кандинский · Малевич</text>

    <!-- Key concepts -->
    <rect x="25" y="190" width="220" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Ключевые понятия:</text>
    <text x="135" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Образ · Духовность · Православие</text>
    <text x="135" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Передвижники · Супрематизм</text>

    <!-- Timeline -->
    <rect x="260" y="190" width="215" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Эпохи русского искусства:</text>
    <line x1="275" y1="220" x2="460" y2="220" stroke="#880E4F" stroke-width="1.5" opacity="0.5"/>
    <circle cx="285" cy="220" r="3" fill="#880E4F"/>
    <text x="285" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">XI</text>
    <circle cx="330" cy="220" r="3" fill="#880E4F"/>
    <text x="330" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">XV</text>
    <circle cx="385" cy="220" r="3" fill="#C2185B"/>
    <text x="385" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">XIX</text>
    <circle cx="445" cy="220" r="3" fill="#EC407A"/>
    <text x="445" y="230" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">XX</text>

    <!-- Works -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Шедевры русского искусства:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Троица · Бурлаки на Волге · Чёрный квадрат · Утро в сосновом лесу</text>"""
    },
    {
        "num": 5,
        "title": "Модернизм",
        "subtitle": "Искусство — Урок 5",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Impressionism -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Импрессионизм</text>
    <!-- Dots/dashes for impressionist style -->
    <circle cx="60" cy="130" r="3" fill="#880E4F" opacity="0.5"/>
    <circle cx="70" cy="128" r="2" fill="#C2185B" opacity="0.6"/>
    <circle cx="80" cy="132" r="3" fill="#EC407A" opacity="0.4"/>
    <circle cx="65" cy="140" r="2" fill="#880E4F" opacity="0.6"/>
    <circle cx="75" cy="142" r="3" fill="#C2185B" opacity="0.5"/>
    <circle cx="85" cy="138" r="2" fill="#880E4F" opacity="0.4"/>
    <circle cx="90" cy="148" r="3" fill="#EC407A" opacity="0.5"/>
    <circle cx="100" cy="145" r="2" fill="#880E4F" opacity="0.6"/>
    <circle cx="110" cy="150" r="3" fill="#C2185B" opacity="0.4"/>
    <circle cx="95" cy="155" r="2" fill="#880E4F" opacity="0.5"/>
    <circle cx="120" cy="155" r="2" fill="#EC407A" opacity="0.6"/>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Моне · Ренуар · Дега</text>

    <!-- Cubism -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Кубизм</text>
    <!-- Geometric face -->
    <polygon points="235,125 270,125 280,145 265,160 240,160 225,145" fill="#880E4F" opacity="0.15" stroke="#880E4F" stroke-width="1"/>
    <line x1="252" y1="125" x2="250" y2="160" stroke="#880E4F" stroke-width="0.8" opacity="0.5"/>
    <line x1="225" y1="142" x2="280" y2="142" stroke="#880E4F" stroke-width="0.8" opacity="0.5"/>
    <polygon points="235,125 252,120 270,125" fill="#880E4F" opacity="0.2"/>
    <text x="252" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Пикассо · Брак</text>

    <!-- Surrealism -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Сюрреализм</text>
    <!-- Melting clock (Dalí inspired) -->
    <ellipse cx="395" cy="140" rx="18" ry="10" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <path d="M380,140 Q375,155 385,160" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <line x1="395" y1="130" x2="395" y2="140" stroke="#880E4F" stroke-width="1"/>
    <line x1="395" y1="140" x2="405" y2="135" stroke="#880E4F" stroke-width="1"/>
    <!-- Eye -->
    <ellipse cx="430" cy="150" rx="10" ry="6" fill="none" stroke="#C2185B" stroke-width="1.5"/>
    <circle cx="430" cy="150" r="3" fill="#C2185B" opacity="0.5"/>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Дали · Магритт · Эрнст</text>

    <!-- Movement comparison -->
    <rect x="25" y="190" width="450" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Направления модернизма:</text>
    <line x1="40" y1="218" x2="460" y2="218" stroke="#880E4F" stroke-width="1" opacity="0.3"/>
    <text x="72" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F">Импрессионизм</text>
    <text x="152" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F">Экспрессионизм</text>
    <text x="237" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F">Кубизм</text>
    <text x="287" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F">Футуризм</text>
    <text x="340" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F">Сюрреализм</text>
    <text x="410" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F">Абстракционизм</text>

    <!-- Concepts & Techniques -->
    <rect x="25" y="250" width="220" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Идеи:</text>
    <text x="135" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Деконструкция · Авангард · Бессознательное</text>

    <rect x="255" y="250" width="220" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="365" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Техники:</text>
    <text x="365" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Дивизионизм · Коллаж · Фроттаж</text>"""
    },
    {
        "num": 6,
        "title": "Современное искусство",
        "subtitle": "Искусство — Урок 6",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Pop Art -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Поп-арт</text>
    <!-- Warhol-style repeated image -->
    <rect x="42" y="120" width="22" height="22" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="1"/>
    <rect x="68" y="120" width="22" height="22" fill="#C2185B" opacity="0.3" stroke="#880E4F" stroke-width="1"/>
    <rect x="94" y="120" width="22" height="22" fill="#EC407A" opacity="0.3" stroke="#880E4F" stroke-width="1"/>
    <rect x="120" y="120" width="22" height="22" fill="#880E4F" opacity="0.5" stroke="#880E4F" stroke-width="1"/>
    <!-- Soup can shape -->
    <rect x="60" y="150" width="30" height="20" rx="3" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <ellipse cx="75" cy="150" rx="15" ry="4" fill="none" stroke="#880E4F" stroke-width="1"/>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Уорхол · Лихтенштейн</text>

    <!-- Installation -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Инсталляция</text>
    <!-- Room/box with objects -->
    <rect x="210" y="125" width="50" height="40" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <rect x="218" y="135" width="10" height="15" fill="#880E4F" opacity="0.3"/>
    <circle cx="242" cy="140" r="7" fill="none" stroke="#C2185B" stroke-width="1.5"/>
    <line x1="255" y1="140" x2="275" y2="130" stroke="#880E4F" stroke-width="1"/>
    <line x1="255" y1="140" x2="275" y2="150" stroke="#880E4F" stroke-width="1"/>
    <text x="252" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Бойс · Кабаков</text>

    <!-- Performance / Conceptual -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Концептуализм</text>
    <!-- Idea bubble -->
    <ellipse cx="405" cy="145" rx="25" ry="15" fill="none" stroke="#880E4F" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="405" y="148" font-family="Arial,sans-serif" font-size="10" fill="#880E4F" text-anchor="middle">идея</text>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Дюшан · Кошут</text>

    <!-- Key concepts -->
    <rect x="25" y="190" width="220" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Формы современного искусства:</text>
    <text x="135" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Перформанс · Хэппенинг · Видеоарт</text>
    <text x="135" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Лэнд-арт · Боди-арт · Реди-мейд</text>

    <!-- Features -->
    <rect x="260" y="190" width="215" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Особенности:</text>
    <text x="367" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Дематериализация объекта</text>
    <text x="367" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Контекст важнее формы</text>

    <!-- Works -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Знаковые работы:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Фонтан Дюшана · Банки Уорхола · Установка Кабакова · Баллоны Кусамы</text>"""
    },
    {
        "num": 7,
        "title": "Дизайн и искусство",
        "subtitle": "Искусство — Урок 7",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Bauhaus -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Баухаус</text>
    <!-- Bauhaus geometric composition -->
    <circle cx="60" cy="140" r="15" fill="#880E4F" opacity="0.25" stroke="#880E4F" stroke-width="1"/>
    <rect x="85" y="128" width="22" height="22" fill="#C2185B" opacity="0.25" stroke="#880E4F" stroke-width="1"/>
    <polygon points="120,150 130,130 140,150" fill="#880E4F" opacity="0.25" stroke="#880E4F" stroke-width="1"/>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Гропиус · Кандинский · Мохой-Надь</text>

    <!-- Typography -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Типографика</text>
    <!-- Font specimens -->
    <text x="195" y="135" font-family="serif" font-size="16" fill="#880E4F">Aa</text>
    <text x="220" y="135" font-family="Arial,sans-serif" font-size="16" fill="#C2185B">Aa</text>
    <text x="245" y="135" font-family="monospace" font-size="16" fill="#880E4F">Aa</text>
    <!-- Font metrics -->
    <line x1="195" y1="145" x2="300" y2="145" stroke="#880E4F" stroke-width="0.5" opacity="0.3"/>
    <text x="250" y="158" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Шрифт · Кегль · Интерлиньяж</text>
    <text x="252" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Антикова · Гротеск</text>

    <!-- Graphic design -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Графический дизайн</text>
    <!-- Grid system -->
    <rect x="355" y="120" width="50" height="45" fill="none" stroke="#880E4F" stroke-width="1"/>
    <line x1="370" y1="120" x2="370" y2="165" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <line x1="390" y1="120" x2="390" y2="165" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <line x1="355" y1="135" x2="405" y2="135" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <line x1="355" y1="150" x2="405" y2="150" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <!-- Color swatches -->
    <rect x="420" y="125" width="12" height="12" fill="#880E4F" opacity="0.8"/>
    <rect x="435" y="125" width="12" height="12" fill="#C2185B" opacity="0.8"/>
    <rect x="420" y="140" width="12" height="12" fill="#EC407A" opacity="0.8"/>
    <rect x="435" y="140" width="12" height="12" fill="#FCE4EC" stroke="#880E4F" stroke-width="0.5"/>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Модульная сетка · Палитра</text>

    <!-- Principles -->
    <rect x="25" y="190" width="450" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Принципы дизайна:</text>
    <text x="72" y="225" font-family="Arial,sans-serif" font-size="8" fill="#880E4F">Баланс</text>
    <text x="130" y="225" font-family="Arial,sans-serif" font-size="8" fill="#880E4F">Контраст</text>
    <text x="195" y="225" font-family="Arial,sans-serif" font-size="8" fill="#880E4F">Акцент</text>
    <text x="252" y="225" font-family="Arial,sans-serif" font-size="8" fill="#880E4F">Ритм</text>
    <text x="298" y="225" font-family="Arial,sans-serif" font-size="8" fill="#880E4F">Пропорция</text>
    <text x="368" y="225" font-family="Arial,sans-serif" font-size="8" fill="#880E4F">Единство</text>
    <text x="428" y="225" font-family="Arial,sans-serif" font-size="8" fill="#880E4F">Гармония</text>

    <!-- Design fields -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Виды дизайна:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Графический · Промышленный · Интерьерный · Web-дизайн · UX/UI</text>"""
    },
    {
        "num": 8,
        "title": "Искусство и технологии",
        "subtitle": "Искусство — Урок 8",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Digital art -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Цифровое искусство</text>
    <!-- Monitor/tablet -->
    <rect x="52" y="122" width="45" height="35" rx="3" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <rect x="58" y="127" width="33" height="22" fill="#880E4F" opacity="0.1"/>
    <!-- Pixel grid on screen -->
    <rect x="58" y="127" width="5" height="5" fill="#880E4F" opacity="0.3"/>
    <rect x="68" y="127" width="5" height="5" fill="#C2185B" opacity="0.3"/>
    <rect x="78" y="127" width="5" height="5" fill="#880E4F" opacity="0.2"/>
    <rect x="63" y="137" width="5" height="5" fill="#EC407A" opacity="0.3"/>
    <rect x="73" y="137" width="5" height="5" fill="#880E4F" opacity="0.3"/>
    <!-- Stylus -->
    <line x1="110" y1="140" x2="130" y2="130" stroke="#880E4F" stroke-width="2"/>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Планшет · 3D · NFT</text>

    <!-- AI Art -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">ИИ и искусство</text>
    <!-- Neural network nodes -->
    <circle cx="230" cy="130" r="5" fill="#880E4F" opacity="0.4"/>
    <circle cx="250" cy="125" r="5" fill="#C2185B" opacity="0.4"/>
    <circle cx="270" cy="130" r="5" fill="#880E4F" opacity="0.4"/>
    <circle cx="235" cy="150" r="5" fill="#EC407A" opacity="0.4"/>
    <circle cx="255" cy="150" r="5" fill="#880E4F" opacity="0.4"/>
    <circle cx="275" cy="150" r="5" fill="#C2185B" opacity="0.4"/>
    <!-- Connections -->
    <line x1="230" y1="130" x2="235" y2="150" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <line x1="230" y1="130" x2="255" y2="150" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <line x1="250" y1="125" x2="255" y2="150" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <line x1="250" y1="125" x2="275" y2="150" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <line x1="270" y1="130" x2="275" y2="150" stroke="#880E4F" stroke-width="0.5" opacity="0.4"/>
    <text x="252" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Генеративное · Нейросети</text>

    <!-- VR/AR -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">VR / AR</text>
    <!-- VR headset -->
    <rect x="375" y="130" width="40" height="25" rx="8" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <circle cx="388" cy="142" r="6" fill="#880E4F" opacity="0.15"/>
    <circle cx="402" cy="142" r="6" fill="#880E4F" opacity="0.15"/>
    <!-- Immersion waves -->
    <path d="M370,155 Q385,160 395,155 Q405,150 420,155" fill="none" stroke="#C2185B" stroke-width="1" opacity="0.5"/>
    <path d="M365,162 Q385,168 395,162 Q405,156 425,162" fill="none" stroke="#880E4F" stroke-width="1" opacity="0.3"/>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Иммерсия · Интерактив</text>

    <!-- Key concepts -->
    <rect x="25" y="190" width="220" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Технологии в искусстве:</text>
    <text x="135" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Проекция · Мэппинг · Робототехника</text>
    <text x="135" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Биотехнологии · Квантовое искусство</text>

    <!-- Questions -->
    <rect x="260" y="190" width="215" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Этические вопросы:</text>
    <text x="367" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Авторство ИИ-произведений</text>
    <text x="367" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Оригинальность · Доступность</text>

    <!-- Timeline -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Эволюция технологий в искусстве:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Фото (1839) · Кино (1895) · Видеоарт (1960-е) · CGI (1990-е) · AI (2020-е)</text>"""
    },
    {
        "num": 9,
        "title": "Анализ произведения",
        "subtitle": "Искусство — Урок 9",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Composition analysis -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Композиция</text>
    <!-- Rule of thirds grid -->
    <rect x="40" y="120" width="60" height="45" fill="#880E4F" opacity="0.05" stroke="#880E4F" stroke-width="1"/>
    <line x1="60" y1="120" x2="60" y2="165" stroke="#880E4F" stroke-width="0.5" stroke-dasharray="3,2" opacity="0.5"/>
    <line x1="80" y1="120" x2="80" y2="165" stroke="#880E4F" stroke-width="0.5" stroke-dasharray="3,2" opacity="0.5"/>
    <line x1="40" y1="135" x2="100" y2="135" stroke="#880E4F" stroke-width="0.5" stroke-dasharray="3,2" opacity="0.5"/>
    <line x1="40" y1="150" x2="100" y2="150" stroke="#880E4F" stroke-width="0.5" stroke-dasharray="3,2" opacity="0.5"/>
    <!-- Focus point -->
    <circle cx="60" cy="135" r="4" fill="#C2185B" opacity="0.5"/>
    <circle cx="80" cy="150" r="4" fill="#C2185B" opacity="0.5"/>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Правило третей · Золотое сечение</text>

    <!-- Color analysis -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Цвет</text>
    <!-- Color wheel simplified -->
    <circle cx="240" cy="145" r="20" fill="none" stroke="#880E4F" stroke-width="1"/>
    <circle cx="240" cy="128" r="6" fill="#E53935" opacity="0.7"/>
    <circle cx="257" cy="138" r="6" fill="#FFB300" opacity="0.7"/>
    <circle cx="257" cy="155" r="6" fill="#43A047" opacity="0.7"/>
    <circle cx="240" cy="162" r="6" fill="#1E88E5" opacity="0.7"/>
    <circle cx="223" cy="155" r="6" fill="#8E24AA" opacity="0.7"/>
    <circle cx="223" cy="138" r="6" fill="#E53935" opacity="0.5"/>
    <!-- Temperature arrow -->
    <line x1="275" y1="132" x2="290" y2="132" stroke="#C2185B" stroke-width="1"/>
    <text x="282" y="128" font-family="Arial,sans-serif" font-size="6" fill="#555">тёпл.</text>
    <line x1="275" y1="155" x2="290" y2="155" stroke="#1E88E5" stroke-width="1"/>
    <text x="282" y="163" font-family="Arial,sans-serif" font-size="6" fill="#555">холод.</text>
    <text x="252" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Контраст · Гармония · Нюанс</text>

    <!-- Form & Content -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Форма и содержание</text>
    <!-- Form box -->
    <rect x="350" y="120" width="45" height="45" rx="2" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <text x="372" y="138" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Ф</text>
    <text x="372" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">форма</text>
    <!-- Arrow -->
    <line x1="398" y1="142" x2="410" y2="142" stroke="#C2185B" stroke-width="1.5"/>
    <polygon points="410,139 416,142 410,145" fill="#C2185B"/>
    <!-- Content box -->
    <rect x="418" y="120" width="45" height="45" rx="2" fill="#880E4F" opacity="0.1" stroke="#880E4F" stroke-width="1.5"/>
    <text x="440" y="138" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">С</text>
    <text x="440" y="150" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">смысл</text>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Единство формы и идеи</text>

    <!-- Analysis steps -->
    <rect x="25" y="190" width="450" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Этапы анализа произведения:</text>
    <rect x="35" y="215" width="80" height="18" rx="9" fill="#880E4F" opacity="0.15"/>
    <text x="75" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">1. Описание</text>
    <rect x="125" y="215" width="80" height="18" rx="9" fill="#880E4F" opacity="0.2"/>
    <text x="165" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">2. Анализ формы</text>
    <rect x="215" y="215" width="80" height="18" rx="9" fill="#880E4F" opacity="0.25"/>
    <text x="255" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">3. Интерпретация</text>
    <rect x="305" y="215" width="80" height="18" rx="9" fill="#880E4F" opacity="0.3"/>
    <text x="345" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">4. Оценка</text>
    <rect x="395" y="215" width="70" height="18" rx="9" fill="#880E4F" opacity="0.35"/>
    <text x="430" y="228" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">5. Контекст</text>

    <!-- Key terms -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Инструменты анализа:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Линия · Пятно · Фактура · Ритм · Светотень · Колорит · Силуэт · Пропорции</text>"""
    },
    {
        "num": 10,
        "title": "Критика искусства",
        "subtitle": "Искусство — Урок 10",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Critical approaches -->
    <rect x="25" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Подходы</text>
    <!-- Formal approach -->
    <rect x="35" y="120" width="55" height="20" rx="4" fill="#880E4F" opacity="0.15"/>
    <text x="62" y="134" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">Формальный</text>
    <!-- Iconographic -->
    <rect x="35" y="145" width="55" height="20" rx="4" fill="#880E4F" opacity="0.2"/>
    <text x="62" y="159" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">Иконограф.</text>
    <!-- Sociological -->
    <rect x="100" y="120" width="55" height="20" rx="4" fill="#880E4F" opacity="0.25"/>
    <text x="127" y="134" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">Социолог.</text>
    <!-- Psychoanalytic -->
    <rect x="100" y="145" width="55" height="20" rx="4" fill="#880E4F" opacity="0.3"/>
    <text x="127" y="159" font-family="Arial,sans-serif" font-size="7" fill="#880E4F" text-anchor="middle">Психоанал.</text>
    <text x="97" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Вёльфлин · Панофский · Фрейд</text>

    <!-- Criteria -->
    <rect x="180" y="95" width="145" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Критерии оценки</text>
    <!-- Star rating for each criterion -->
    <text x="200" y="132" font-family="Arial,sans-serif" font-size="7" fill="#555">Оригинальность</text>
    <text x="280" y="132" font-family="Arial,sans-serif" font-size="9" fill="#880E4F">★★★★☆</text>
    <text x="200" y="145" font-family="Arial,sans-serif" font-size="7" fill="#555">Мастерство</text>
    <text x="280" y="145" font-family="Arial,sans-serif" font-size="9" fill="#880E4F">★★★★★</text>
    <text x="200" y="158" font-family="Arial,sans-serif" font-size="7" fill="#555">Выразительность</text>
    <text x="280" y="158" font-family="Arial,sans-serif" font-size="9" fill="#880E4F">★★★★☆</text>
    <text x="200" y="171" font-family="Arial,sans-serif" font-size="7" fill="#555">Влияние</text>
    <text x="280" y="171" font-family="Arial,sans-serif" font-size="9" fill="#880E4F">★★★☆☆</text>

    <!-- Critical writing -->
    <rect x="335" y="95" width="140" height="85" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Критический текст</text>
    <!-- Document lines -->
    <rect x="350" y="120" width="60" height="45" fill="white" stroke="#880E4F" stroke-width="1"/>
    <line x1="355" y1="130" x2="405" y2="130" stroke="#880E4F" stroke-width="0.5" opacity="0.3"/>
    <line x1="355" y1="136" x2="400" y2="136" stroke="#880E4F" stroke-width="0.5" opacity="0.3"/>
    <line x1="355" y1="142" x2="405" y2="142" stroke="#880E4F" stroke-width="0.5" opacity="0.3"/>
    <line x1="355" y1="148" x2="395" y2="148" stroke="#880E4F" stroke-width="0.5" opacity="0.3"/>
    <line x1="355" y1="154" x2="400" y2="154" stroke="#880E4F" stroke-width="0.5" opacity="0.3"/>
    <!-- Pen -->
    <line x1="420" y1="155" x2="445" y2="130" stroke="#880E4F" stroke-width="2"/>
    <polygon points="445,130 448,127 443,128" fill="#880E4F"/>
    <text x="405" y="175" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Эссе · Рецензия · Отзыв</text>

    <!-- Criticism types -->
    <rect x="25" y="190" width="220" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Виды критики:</text>
    <text x="135" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Описательная · Нормативная</text>
    <text x="135" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Интерпретативная · Теоретическая</text>

    <!-- Great critics -->
    <rect x="260" y="190" width="215" height="50" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="207" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Критики и теоретики:</text>
    <text x="367" y="220" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Дидро · Бодлер · Гринберг</text>
    <text x="367" y="232" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Стасов · Бенуа · Фёдоров-Давыдов</text>

    <!-- Key concepts -->
    <rect x="25" y="250" width="450" height="40" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="266" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="#880E4F" text-anchor="middle">Золотое правило критики:</text>
    <text x="250" y="280" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">«Смотри → Чувствуй → Думай → Говори» — объективность, аргументированность, уважение</text>"""
    },
    {
        "num": 11,
        "title": "Создание арт-проекта",
        "subtitle": "Искусство — Урок 11",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Project stages -->
    <rect x="25" y="95" width="450" height="50" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="250" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Этапы создания арт-проекта</text>
    <!-- Flowchart: Idea → Research → Sketch → Execute → Present -->
    <rect x="35" y="120" width="70" height="20" rx="10" fill="#880E4F" opacity="0.2"/>
    <text x="70" y="134" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Идея</text>
    <polygon points="108,130 114,126 114,134" fill="#880E4F" opacity="0.5"/>
    <rect x="118" y="120" width="70" height="20" rx="10" fill="#880E4F" opacity="0.25"/>
    <text x="153" y="134" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Исслед.</text>
    <polygon points="191,130 197,126 197,134" fill="#880E4F" opacity="0.5"/>
    <rect x="201" y="120" width="70" height="20" rx="10" fill="#880E4F" opacity="0.3"/>
    <text x="236" y="134" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Эскиз</text>
    <polygon points="274,130 280,126 280,134" fill="#880E4F" opacity="0.5"/>
    <rect x="284" y="120" width="70" height="20" rx="10" fill="#880E4F" opacity="0.35"/>
    <text x="319" y="134" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Создание</text>
    <polygon points="357,130 363,126 363,134" fill="#880E4F" opacity="0.5"/>
    <rect x="367" y="120" width="95" height="20" rx="10" fill="#880E4F" opacity="0.4"/>
    <text x="414" y="134" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Презентация</text>

    <!-- Idea generation -->
    <rect x="25" y="155" width="145" height="70" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="97" y="172" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Генерация идей</text>
    <!-- Lightbulb -->
    <circle cx="70" cy="198" r="10" fill="none" stroke="#880E4F" stroke-width="1.5"/>
    <line x1="65" y1="208" x2="75" y2="208" stroke="#880E4F" stroke-width="1"/>
    <line x1="66" y1="211" x2="74" y2="211" stroke="#880E4F" stroke-width="1"/>
    <!-- Rays -->
    <line x1="70" y1="184" x2="70" y2="180" stroke="#C2185B" stroke-width="1"/>
    <line x1="82" y1="190" x2="85" y2="187" stroke="#C2185B" stroke-width="1"/>
    <line x1="58" y1="190" x2="55" y2="187" stroke="#C2185B" stroke-width="1"/>
    <text x="115" y="193" font-family="Arial,sans-serif" font-size="7" fill="#555">Мозговой</text>
    <text x="115" y="203" font-family="Arial,sans-serif" font-size="7" fill="#555">штурм</text>
    <text x="115" y="216" font-family="Arial,sans-serif" font-size="7" fill="#555">Минд-мап</text>

    <!-- Materials & Techniques -->
    <rect x="180" y="155" width="145" height="70" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="252" y="172" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Материалы</text>
    <!-- Paint tube -->
    <rect x="200" y="185" width="30" height="10" rx="3" fill="none" stroke="#880E4F" stroke-width="1"/>
    <line x1="230" y1="190" x2="240" y2="188" stroke="#880E4F" stroke-width="1.5"/>
    <!-- Brush -->
    <line x1="250" y1="195" x2="270" y2="185" stroke="#880E4F" stroke-width="2"/>
    <rect x="246" y="195" width="8" height="15" rx="1" fill="#880E4F" opacity="0.3" stroke="#880E4F" stroke-width="0.5"/>
    <!-- Camera -->
    <rect x="280" y="185" width="20" height="15" rx="2" fill="none" stroke="#880E4F" stroke-width="1"/>
    <circle cx="290" cy="192" r="4" fill="none" stroke="#880E4F" stroke-width="1"/>
    <text x="252" y="218" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Краски · Кисти · Фото · Цифра</text>

    <!-- Presentation -->
    <rect x="335" y="155" width="140" height="70" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="405" y="172" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Презентация</text>
    <!-- Exhibition wall -->
    <rect x="355" y="180" width="50" height="30" fill="white" stroke="#880E4F" stroke-width="1"/>
    <!-- Frames on wall -->
    <rect x="360" y="184" width="12" height="10" fill="#880E4F" opacity="0.15" stroke="#880E4F" stroke-width="0.5"/>
    <rect x="376" y="182" width="15" height="14" fill="#C2185B" opacity="0.1" stroke="#C2185B" stroke-width="0.5"/>
    <rect x="395" y="185" width="8" height="8" fill="#880E4F" opacity="0.2" stroke="#880E4F" stroke-width="0.5"/>
    <!-- Person silhouette -->
    <circle cx="435" cy="188" r="5" fill="none" stroke="#880E4F" stroke-width="1"/>
    <line x1="435" y1="193" x2="435" y2="205" stroke="#880E4F" stroke-width="1"/>
    <text x="405" y="218" font-family="Arial,sans-serif" font-size="7" fill="#555" text-anchor="middle">Выставка · Портфолио</text>

    <!-- Project types -->
    <rect x="25" y="235" width="450" height="22" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="250" font-family="Arial,sans-serif" font-size="8" fill="#880E4F" text-anchor="middle">Типы проектов: Живопись · Скульптура · Фото · Видео · Инсталляция · Дизайн · Перформанс</text>

    <!-- Tips -->
    <rect x="25" y="265" width="450" height="25" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="282" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">Совет: документируйте каждый этап — эскизы, ошибки, озарения ведут к лучшему результату</text>"""
    },
    {
        "num": 12,
        "title": "Итоговая работа",
        "subtitle": "Искусство — Урок 12",
        "footer": "Искусство · 10 класс",
        "content": """    <!-- Summary of course -->
    <rect x="25" y="95" width="450" height="40" rx="6" fill="#FCE4EC" stroke="#880E4F" stroke-width="1.5"/>
    <text x="250" y="112" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Путь через историю искусства</text>
    <!-- Timeline arrow -->
    <line x1="40" y1="125" x2="460" y2="125" stroke="#880E4F" stroke-width="2" opacity="0.5"/>
    <polygon points="460,121 468,125 460,129" fill="#880E4F" opacity="0.5"/>
    <!-- Period markers -->
    <circle cx="60" cy="125" r="4" fill="#880E4F"/>
    <text x="60" y="118" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Древность</text>
    <circle cx="120" cy="125" r="4" fill="#880E4F"/>
    <text x="120" y="118" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Ср. века</text>
    <circle cx="180" cy="125" r="4" fill="#880E4F"/>
    <text x="180" y="118" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Возрожд.</text>
    <circle cx="240" cy="125" r="4" fill="#880E4F"/>
    <text x="240" y="118" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Русское</text>
    <circle cx="300" cy="125" r="4" fill="#880E4F"/>
    <text x="300" y="118" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Модерн.</text>
    <circle cx="360" cy="125" r="4" fill="#880E4F"/>
    <text x="360" y="118" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Современ.</text>
    <circle cx="420" cy="125" r="4" fill="#C2185B"/>
    <text x="420" y="118" font-family="Arial,sans-serif" font-size="6" fill="#555" text-anchor="middle">Технол.</text>

    <!-- Portfolio components -->
    <rect x="25" y="145" width="220" height="75" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="135" y="162" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Портфолио</text>
    <!-- Checklist -->
    <rect x="40" y="170" width="8" height="8" rx="1" fill="none" stroke="#880E4F" stroke-width="1"/>
    <line x1="42" y1="174" x2="45" y2="177" stroke="#880E4F" stroke-width="1"/>
    <line x1="45" y1="177" x2="48" y2="172" stroke="#880E4F" stroke-width="1"/>
    <text x="55" y="178" font-family="Arial,sans-serif" font-size="8" fill="#555">Выбор произведения</text>
    <rect x="40" y="182" width="8" height="8" rx="1" fill="none" stroke="#880E4F" stroke-width="1"/>
    <line x1="42" y1="186" x2="45" y2="189" stroke="#880E4F" stroke-width="1"/>
    <line x1="45" y1="189" x2="48" y2="184" stroke="#880E4F" stroke-width="1"/>
    <text x="55" y="190" font-family="Arial,sans-serif" font-size="8" fill="#555">Анализ и критика</text>
    <rect x="40" y="194" width="8" height="8" rx="1" fill="none" stroke="#880E4F" stroke-width="1"/>
    <text x="55" y="202" font-family="Arial,sans-serif" font-size="8" fill="#555">Собственная работа</text>
    <rect x="40" y="206" width="8" height="8" rx="1" fill="none" stroke="#880E4F" stroke-width="1"/>
    <text x="55" y="214" font-family="Arial,sans-serif" font-size="8" fill="#555">Рефлексия и выводы</text>

    <!-- Assessment criteria -->
    <rect x="260" y="145" width="215" height="75" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="367" y="162" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Критерии оценки</text>
    <!-- Progress bars -->
    <text x="275" y="178" font-family="Arial,sans-serif" font-size="7" fill="#555">Знание теории</text>
    <rect x="350" y="172" width="100" height="6" rx="3" fill="#FCE4EC"/>
    <rect x="350" y="172" width="85" height="6" rx="3" fill="#880E4F" opacity="0.4"/>
    <text x="275" y="192" font-family="Arial,sans-serif" font-size="7" fill="#555">Анализ произведений</text>
    <rect x="350" y="186" width="100" height="6" rx="3" fill="#FCE4EC"/>
    <rect x="350" y="186" width="75" height="6" rx="3" fill="#880E4F" opacity="0.5"/>
    <text x="275" y="206" font-family="Arial,sans-serif" font-size="7" fill="#555">Творческая работа</text>
    <rect x="350" y="200" width="100" height="6" rx="3" fill="#FCE4EC"/>
    <rect x="350" y="200" width="90" height="6" rx="3" fill="#880E4F" opacity="0.6"/>
    <text x="275" y="214" font-family="Arial,sans-serif" font-size="7" fill="#555">Обоснование позиции</text>
    <rect x="350" y="208" width="100" height="6" rx="3" fill="#FCE4EC"/>
    <rect x="350" y="208" width="65" height="6" rx="3" fill="#880E4F" opacity="0.7"/>

    <!-- Final message -->
    <rect x="25" y="230" width="450" height="60" rx="6" fill="white" stroke="#880E4F" stroke-width="1" opacity="0.9"/>
    <text x="250" y="250" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#880E4F" text-anchor="middle">Что мы изучили:</text>
    <text x="250" y="265" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">От наскальных рисунков до цифрового искусства — история человечества</text>
    <text x="250" y="278" font-family="Arial,sans-serif" font-size="8" fill="#555" text-anchor="middle">через призму творчества. Анализ, критика, создание собственных произведений.</text>"""
    },
]


def generate_svg(lesson):
    """Generate an SVG string for a given lesson."""
    num = lesson["num"]
    title = lesson["title"]
    subtitle = lesson["subtitle"]
    footer = lesson["footer"]
    content = lesson["content"]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{BG_TOP}"/>
      <stop offset="100%" stop-color="{BG_BOT}"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{PRIMARY_LIGHT}"/>
      <stop offset="100%" stop-color="{ACCENT}"/>
    </linearGradient>
  </defs>
  <!-- Background -->
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <!-- Border -->
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{PRIMARY}" stroke-width="2.5"/>
  <!-- Inner decorative border -->
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="{PRIMARY}" stroke-width="1" opacity="0.3"/>
  <!-- Corner decorations -->
  <polygon points="10,10 30,10 10,30" fill="{PRIMARY}" opacity="0.12"/>
  <polygon points="490,10 470,10 490,30" fill="{ACCENT}" opacity="0.12"/>
  <polygon points="10,340 30,340 10,320" fill="{PRIMARY}" opacity="0.12"/>
  <polygon points="490,340 470,340 490,320" fill="{ACCENT}" opacity="0.12"/>
  <!-- Title -->
  <text x="250" y="42" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="{PRIMARY}" text-anchor="middle">{title}</text>
  <!-- Subtitle -->
  <text x="250" y="62" font-family="Arial,sans-serif" font-size="11" fill="#888" text-anchor="middle">{subtitle}</text>
  <!-- Divider line -->
  <line x1="30" y1="72" x2="470" y2="72" stroke="{PRIMARY}" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="69" width="60" height="5" fill="{PRIMARY}" opacity="0.18" rx="1"/>
  <rect x="410" y="69" width="60" height="5" fill="{ACCENT}" opacity="0.12" rx="1"/>
  <!-- Clip path for content area -->
  <clipPath id="ill"><rect x="15" y="80" width="470" height="220" rx="6"/></clipPath>
  <g clip-path="url(#ill)">
  <rect x="15" y="80" width="470" height="220" fill="{BG_TOP}" opacity="0.4"/>
{content}
  </g>
  <!-- Footer panel -->
  <rect x="12" y="305" width="476" height="35" rx="5" fill="url(#panel)"/>
  <line x1="20" y1="308" x2="20" y2="337" stroke="{PRIMARY}" stroke-width="1.5" opacity="0.6"/>
  <line x1="480" y1="308" x2="480" y2="337" stroke="{PRIMARY}" stroke-width="1.5" opacity="0.6"/>
  <text x="250" y="328" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">{footer}</text>
</svg>"""
    return svg


def validate_svg(svg_string, filepath):
    """Validate SVG as proper XML."""
    try:
        ET.fromstring(svg_string)
        return True, "Valid XML"
    except ET.ParseError as e:
        return False, str(e)


def main():
    generated = 0
    validated = 0
    errors = []

    for lesson in lessons:
        num = lesson["num"]
        filename = f"lesson{num}.svg"
        filepath = os.path.join(OUTPUT_DIR, filename)

        svg_content = generate_svg(lesson)

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        generated += 1
        print(f"  Generated: {filename}")

        # Validate
        is_valid, msg = validate_svg(svg_content, filepath)
        if is_valid:
            validated += 1
            print(f"  Validated: {filename} ✓")
        else:
            errors.append((filename, msg))
            print(f"  VALIDATION ERROR: {filename} — {msg}")

    print(f"\n{'='*50}")
    print(f"Generated: {generated} SVG files")
    print(f"Validated: {validated} SVG files")
    if errors:
        print(f"Errors: {len(errors)}")
        for fname, err in errors:
            print(f"  {fname}: {err}")
    else:
        print("All SVGs are valid XML! ✓")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
