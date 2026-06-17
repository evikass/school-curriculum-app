#!/usr/bin/env python3
import os

SVG_DIR = 'public/images/lessons/grade2'

# ============================================================
# LITERATURE SVGs (10 lessons)
# ============================================================
literature_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes pageTurn{0%,100%{transform:rotateY(0)}50%{transform:rotateY(5deg)}}.book{animation:pageTurn 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FCE4EC"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#880E4F">Русские народные сказки</text>
  <!-- Book -->
  <g class="book" transform="translate(30,50)">
    <rect x="0" y="0" width="180" height="130" fill="#880E4F" rx="5"/>
    <rect x="5" y="5" width="170" height="120" fill="#FCE4EC" rx="3"/>
    <text x="90" y="35" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#880E4F">СКАЗКИ</text>
    <line x1="20" y1="45" x2="160" y2="45" stroke="#880E4F" stroke-width="1"/>
    <text x="90" y="65" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#880E4F">Колобок</text>
    <text x="90" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#880E4F">Теремок</text>
    <text x="90" y="99" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#880E4F">Репка</text>
    <text x="90" y="116" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#880E4F">Курочка Ряба</text>
  </g>
  <!-- Features -->
  <rect x="230" y="50" width="240" height="130" fill="white" rx="10" stroke="#F48FB1" stroke-width="2"/>
  <text x="350" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F">Особенности сказок</text>
  <text x="250" y="95" font-family="Arial,sans-serif" font-size="11" fill="#333">Зачин: «В некотором царстве...»</text>
  <text x="250" y="112" font-family="Arial,sans-serif" font-size="11" fill="#333">Волшебные события</text>
  <text x="250" y="129" font-family="Arial,sans-serif" font-size="11" fill="#333">Борьба добра и зла</text>
  <text x="250" y="146" font-family="Arial,sans-serif" font-size="11" fill="#333">Повторы: «За лесами, за горами...»</text>
  <text x="250" y="163" font-family="Arial,sans-serif" font-size="11" fill="#333">Концовка: «И стали жить-поживать...»</text>
  <!-- Types -->
  <rect x="30" y="200" width="440" height="140" fill="#FCE4EC" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F">Виды русских народных сказок</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="235" width="120" height="45" fill="white" rx="5" stroke="#F48FB1"/>
    <text x="110" y="255" text-anchor="middle" fill="#880E4F" font-weight="bold">Волшебные</text>
    <text x="110" y="272" text-anchor="middle" fill="#555">Гуси-лебеди</text>
    <rect x="190" y="235" width="120" height="45" fill="white" rx="5" stroke="#F48FB1"/>
    <text x="250" y="255" text-anchor="middle" fill="#880E4F" font-weight="bold">О животных</text>
    <text x="250" y="272" text-anchor="middle" fill="#555">Лиса и волк</text>
    <rect x="330" y="235" width="120" height="45" fill="white" rx="5" stroke="#F48FB1"/>
    <text x="390" y="255" text-anchor="middle" fill="#880E4F" font-weight="bold">Бытовые</text>
    <text x="390" y="272" text-anchor="middle" fill="#555">Каша из топора</text>
  </g>
  <text x="250" y="305" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#880E4F">Сказки передавались из уст в уста, от поколения к поколению</text>
  <text x="250" y="322" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">У каждой сказки есть мораль — добро побеждает зло</text>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes roll{0%{transform:translateX(0)}100%{transform:translateX(10px)}50%{transform:translateX(0)}}.rolling{animation:roll 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Сказка «Колобок»</text>
  <!-- Kolobok character -->
  <g class="rolling" transform="translate(50,60)">
    <circle cx="50" cy="50" r="45" fill="#FFB74D" stroke="#E65100" stroke-width="3"/>
    <circle cx="35" cy="40" r="6" fill="#333"/><circle cx="65" cy="40" r="6" fill="#333"/>
    <path d="M 30 60 Q 50 75 70 60" fill="none" stroke="#333" stroke-width="3"/>
    <circle cx="25" cy="55" r="7" fill="#FF8A65"/>
    <circle cx="75" cy="55" r="7" fill="#FF8A65"/>
  </g>
  <!-- Characters path -->
  <rect x="180" y="55" width="290" height="130" fill="white" rx="10" stroke="#FFB74D" stroke-width="2"/>
  <text x="325" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Кого встретил Колобок?</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="200" y="100">1. Зайца</text>
    <text x="200" y="118">2. Волка</text>
    <text x="200" y="136">3. Медведя</text>
    <text x="200" y="154">4. Лису (съела Колобка)</text>
  </g>
  <text x="325" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E65100">Каждому пел песенку: «Я Колобок, Колобок...»</text>
  <!-- Song -->
  <rect x="30" y="200" width="440" height="65" fill="#FFF3E0" rx="10"/>
  <text x="250" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#E65100">Песенка Колобка</text>
  <text x="250" y="240" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">«Я Колобок, Колобок! По амбару метён, по сусекам скребён,</text>
  <text x="250" y="255" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">на сметане мешён, в печку сажён, на окошке стужён!»</text>
  <!-- Moral -->
  <rect x="30" y="280" width="440" height="55" fill="white" rx="10" stroke="#FFB74D" stroke-width="2"/>
  <text x="250" y="302" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Чему учит сказка?</text>
  <text x="250" y="322" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Нельзя доверять незнакомцам и хвастаться</text>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes door{0%,100%{transform:scaleX(1)}50%{transform:scaleX(0.95)}}.house{animation:door 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#2E7D32">Сказка «Теремок»</text>
  <!-- Teremok house -->
  <g class="house" transform="translate(30,50)">
    <rect x="30" y="50" width="140" height="110" fill="#FFECB3" stroke="#795548" stroke-width="3" rx="3"/>
    <polygon points="100,10 10,50 190,50" fill="#C62828" stroke="#795548" stroke-width="2"/>
    <rect x="75" y="90" width="50" height="70" fill="#795548" rx="3"/>
    <circle cx="118" cy="125" r="4" fill="#FFD54F"/>
    <rect x="45" y="70" width="30" height="30" fill="#BBDEFB" stroke="#795548" stroke-width="1"/>
    <line x1="60" y1="70" x2="60" y2="100" stroke="#795548" stroke-width="1"/>
    <line x1="45" y1="85" x2="75" y2="85" stroke="#795548" stroke-width="1"/>
    <rect x="125" y="70" width="30" height="30" fill="#BBDEFB" stroke="#795548" stroke-width="1"/>
    <line x1="140" y1="70" x2="140" y2="100" stroke="#795548" stroke-width="1"/>
    <line x1="125" y1="85" x2="155" y2="85" stroke="#795548" stroke-width="1"/>
  </g>
  <!-- Animals -->
  <rect x="240" y="50" width="230" height="180" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="355" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#2E7D32">Кто жил в теремке?</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="260" y="95">1. Мышка-норушка</text>
    <text x="260" y="115">2. Лягушка-квакушка</text>
    <text x="260" y="135">3. Зайчик-побегайчик</text>
    <text x="260" y="155">4. Лисичка-сестричка</text>
    <text x="260" y="175">5. Волчок-серый бочок</text>
    <text x="260" y="195">6. Медведь (сломал теремок)</text>
  </g>
  <text x="355" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32">«Терем-теремок! Кто в тереме живёт?»</text>
  <!-- Moral -->
  <rect x="30" y="250" width="440" height="85" fill="#E8F5E9" rx="10"/>
  <text x="250" y="273" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#2E7D32">Чему учит сказка?</text>
  <text x="250" y="295" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Нужно жить дружно и приглашать гостей</text>
  <text x="250" y="315" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Но важно считаться с размером жилища</text>
  <text x="250" y="335" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#2E7D32">В конце звери построили новый теремок — вместе!</text>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes wisdom{0%,100%{opacity:1}50%{opacity:0.7}}.wise{animation:wisdom 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Пословицы и поговорки</text>
  <!-- Scroll -->
  <rect x="30" y="50" width="440" height="50" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#BF360C">Пословица — краткое мудрое изречение</text>
  <text x="250" y="92" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Поговорка — меткое образное выражение</text>
  <!-- Examples -->
  <g transform="translate(30,115)" font-family="Arial,sans-serif">
    <rect x="0" y="0" width="210" height="45" fill="#FFCCBC" rx="8" stroke="#BF360C"/>
    <text x="105" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#BF360C">Пословицы</text>
    <text x="105" y="38" text-anchor="middle" font-size="10" fill="#333">Без труда не выловишь и рыбку</text>
    <rect x="230" y="0" width="210" height="45" fill="#FFE0B2" rx="8" stroke="#E65100"/>
    <text x="335" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">Поговорки</text>
    <text x="335" y="38" text-anchor="middle" font-size="10" fill="#333">Как снег на голову</text>
  </g>
  <!-- More proverbs -->
  <rect x="30" y="175" width="440" height="120" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="195" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Известные пословицы</text>
  <g class="wise" font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="218">Терпенье и труд всё перетрут.</text>
    <text x="50" y="238">Семь раз отмерь, один раз отрежь.</text>
    <text x="50" y="258">Ученье — свет, а неученье — тьма.</text>
    <text x="50" y="278">Не имей сто рублей, а имей сто друзей.</text>
  </g>
  <!-- Topic -->
  <rect x="30" y="305" width="440" height="35" fill="#FFF3E0" rx="8"/>
  <text x="250" y="328" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#BF360C">Пословицы учат мудрости и помогают в жизни</text>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes feather{0%,100%{transform:rotate(-5deg)}50%{transform:rotate(5deg)}}.quill{animation:feather 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#EDE7F6"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#4527A0">А.С. Пушкин</text>
  <!-- Portrait area -->
  <rect x="30" y="50" width="160" height="150" fill="white" rx="10" stroke="#B39DDB" stroke-width="2"/>
  <text x="110" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#4527A0">1799-1837</text>
  <!-- Stylized quill -->
  <g class="quill" transform="translate(60,85)">
    <line x1="50" y1="0" x2="50" y2="80" stroke="#5D4037" stroke-width="3"/>
    <path d="M50 0 Q30 10 20 30 Q35 20 50 15 Q65 20 80 30 Q70 10 50 0Z" fill="#4527A0"/>
  </g>
  <text x="110" y="185" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#4527A0">Великий русский поэт</text>
  <!-- Works -->
  <rect x="210" y="50" width="260" height="150" fill="white" rx="10" stroke="#B39DDB" stroke-width="2"/>
  <text x="340" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#4527A0">Произведения для детей</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="225" y="95">Сказка о рыбаке и рыбке</text>
    <text x="225" y="112">Сказка о царе Салтане</text>
    <text x="225" y="129">Сказка о мёртвой царевне</text>
    <text x="225" y="146">Сказка о золотом петушке</text>
    <text x="225" y="163">У Лукоморья дуб зелёный...</text>
    <text x="225" y="180">Сказка о попе и работнике</text>
  </g>
  <!-- Quote -->
  <rect x="30" y="215" width="440" height="70" fill="#EDE7F6" rx="10"/>
  <text x="250" y="238" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#4527A0">«У Лукоморья дуб зелёный...»</text>
  <text x="250" y="258" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Златая цепь на дубе том,</text>
  <text x="250" y="273" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">И днём и ночью кот учёный всё ходит по цепи кругом...</text>
  <!-- Legacy -->
  <rect x="30" y="295" width="440" height="45" fill="white" rx="10" stroke="#B39DDB" stroke-width="1"/>
  <text x="250" y="315" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#4527A0">Пушкин — основатель современного русского языка</text>
  <text x="250" y="332" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Его сказки любят дети всего мира</text>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes hop{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}.jump{animation:hop 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">И.А. Крылов</text>
  <!-- Stylized animals -->
  <g transform="translate(30,50)">
    <rect x="0" y="0" width="160" height="130" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
    <text x="80" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1B5E20">1769-1844</text>
    <!-- Crow and Fox -->
    <g class="jump" transform="translate(20,35)">
      <circle cx="30" cy="40" r="15" fill="#333"/>
      <circle cx="35" cy="35" r="12" fill="#444"/>
      <polygon points="45,35 55,32 45,38" fill="#FF9800"/>
    </g>
    <g transform="translate(70,50)">
      <ellipse cx="30" cy="35" rx="25" ry="15" fill="#FF9800"/>
      <circle cx="15" cy="28" r="10" fill="#FFB74D"/>
      <polygon points="5,28 0,25 5,30" fill="#333"/>
    </g>
    <text x="80" y="120" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1B5E20">Великий баснописец</text>
  </g>
  <!-- Fables list -->
  <rect x="210" y="50" width="260" height="130" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="340" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Известные басни</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="225" y="95">Ворона и Лисица</text>
    <text x="225" y="112">Стрекоза и Муравей</text>
    <text x="225" y="129">Лебедь, Щука и Рак</text>
    <text x="225" y="146">Мартышка и Очки</text>
    <text x="225" y="163">Квартет</text>
  </g>
  <!-- Moral -->
  <rect x="30" y="200" width="440" height="140" fill="#E8F5E9" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Что такое басня?</text>
  <text x="250" y="243" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Короткий рассказ в стихах, где действуют животные</text>
  <text x="250" y="260" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Животные — это люди с их пороками</text>
  <text x="250" y="280" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1B5E20">Мораль — поучение в конце басни</text>
  <text x="250" y="300" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1B5E20">«У сильного всегда бессильный виноват»</text>
  <text x="250" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">«А вы, друзья, как ни садитесь, всё в музыканты не годитесь»</text>
</svg>''',

    7: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes write{0%,100%{transform:translateX(0)}50%{transform:translateX(3px)}}.pen{animation:write 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Л.Н. Толстой</text>
  <!-- Info card -->
  <rect x="30" y="50" width="160" height="130" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="110" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#BF360C">1828-1910</text>
  <g class="pen" transform="translate(60,85)">
    <rect x="30" y="0" width="40" height="60" fill="#795548" rx="3"/>
    <polygon points="30,60 50,80 70,60" fill="#5D4037"/>
    <rect x="35" y="5" width="30" height="8" fill="#FFB74D" rx="2"/>
  </g>
  <text x="110" y="185" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#BF360C">Великий русский писатель</text>
  <!-- Works -->
  <rect x="210" y="50" width="260" height="130" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="340" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Произведения для детей</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="225" y="95">Филипок</text>
    <text x="225" y="112">Котёнок</text>
    <text x="225" y="129">Лев и собачка</text>
    <text x="225" y="146">Два товарища</text>
    <text x="225" y="163">Акула</text>
  </g>
  <!-- School -->
  <rect x="30" y="200" width="440" height="140" fill="#FFF3E0" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Толстой и дети</text>
  <text x="250" y="245" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Открыл школу для крестьянских детей в Ясной Поляне</text>
  <text x="250" y="265" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Сам писал учебники и азбуки для обучения</text>
  <text x="250" y="290" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#BF360C">Рассказы Толстого учат доброте и честности</text>
  <text x="250" y="312" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">«Каждый сам своей судьбы хозяин»</text>
  <text x="250" y="332" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Главные ценности: добро, труд, справедливость</text>
</svg>''',

    8: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}.dream{animation:float 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">К.И. Чуковский</text>
  <!-- Muh-Tsokotuha scene -->
  <g class="dream" transform="translate(30,50)">
    <rect x="0" y="0" width="180" height="130" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
    <text x="90" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0D47A1">1882-1969</text>
    <!-- Sun -->
    <circle cx="40" cy="55" r="20" fill="#FFC107"/>
    <g stroke="#FFC107" stroke-width="2">
      <line x1="40" y1="30" x2="40" y2="22"/><line x1="40" y1="80" x2="40" y2="88"/>
      <line x1="15" y1="55" x2="7" y2="55"/><line x1="65" y1="55" x2="73" y2="55"/>
    </g>
    <!-- Book -->
    <rect x="80" y="45" width="70" height="50" fill="#BBDEFB" rx="3" stroke="#0D47A1" stroke-width="1"/>
    <line x1="115" y1="45" x2="115" y2="95" stroke="#0D47A1" stroke-width="1"/>
  </g>
  <!-- Works -->
  <rect x="230" y="50" width="240" height="130" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="350" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Стихи и сказки</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="245" y="95">Мойдодыр</text>
    <text x="245" y="112">Муха-Цокотуха</text>
    <text x="245" y="129">Тараканище</text>
    <text x="245" y="146">Айболит</text>
    <text x="245" y="163">Бармалей</text>
  </g>
  <!-- Quote -->
  <rect x="30" y="200" width="440" height="65" fill="#E3F2FD" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0D47A1">«Надо, надо умываться по утрам и вечерам!»</text>
  <text x="250" y="245" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Чуковский — любимый детский поэт, его стихи легко запоминаются</text>
  <!-- What he taught -->
  <rect x="30" y="278" width="440" height="60" fill="white" rx="10" stroke="#90CAF9" stroke-width="1"/>
  <text x="250" y="298" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0D47A1">Чему учат сказки Чуковского</text>
  <text x="250" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Быть чистоплотным (Мойдодыр), добрым (Айболит), смелым (Бармалей)</text>
</svg>''',

    9: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes twinkle{0%,100%{opacity:1}50%{opacity:0.5}}.star{animation:twinkle 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#EDE7F6"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#4527A0">Шарль Перро</text>
  <!-- Castle -->
  <g transform="translate(30,50)">
    <rect x="0" y="0" width="180" height="130" fill="white" rx="10" stroke="#B39DDB" stroke-width="2"/>
    <text x="90" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#4527A0">1628-1703</text>
    <!-- Castle silhouette -->
    <rect x="40" y="55" width="100" height="60" fill="#7B1FA2" rx="2"/>
    <rect x="30" y="40" width="25" height="75" fill="#9C27B0" rx="2"/>
    <rect x="125" y="40" width="25" height="75" fill="#9C27B0" rx="2"/>
    <polygon points="42,40 42,55 52,40" fill="#CE93D8"/>
    <polygon points="138,40 138,55 148,40" fill="#CE93D8"/>
    <rect x="70" y="80" width="30" height="35" fill="#FFD54F" rx="3"/>
    <g class="star">
      <circle cx="90" cy="48" r="3" fill="#FFD54F"/>
    </g>
  </g>
  <!-- Works -->
  <rect x="230" y="50" width="240" height="130" fill="white" rx="10" stroke="#B39DDB" stroke-width="2"/>
  <text x="350" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#4527A0">Сказки Шарля Перро</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="245" y="95">Золушка</text>
    <text x="245" y="112">Спящая красавица</text>
    <text x="245" y="129">Красная Шапочка</text>
    <text x="245" y="146">Кот в сапогах</text>
    <text x="245" y="163">Мальчик-с-пальчик</text>
  </g>
  <!-- French fairy tales -->
  <rect x="30" y="200" width="440" height="140" fill="#EDE7F6" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#4527A0">Особенности сказок Перро</text>
  <text x="250" y="245" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Французский сказочник, записывал народные сказки</text>
  <text x="250" y="265" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Волшебные превращения: тыква в карету, мыши в лошадей</text>
  <text x="250" y="290" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#4527A0">Каждая сказка учит добру и справедливости</text>
  <text x="250" y="312" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Золушка: доброта побеждает, Красная Шапочка: слушай родителей</text>
  <text x="250" y="332" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#4527A0">В конце сказок — мораль (поучение)</text>
</svg>''',

    10: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes snow{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}.flake{animation:snow 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Ганс Христиан Андерсен</text>
  <!-- Snowflake -->
  <g transform="translate(30,50)">
    <rect x="0" y="0" width="180" height="130" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
    <text x="90" y="22" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0D47A1">1805-1875</text>
    <g class="flake" transform="translate(60,45)">
      <line x1="30" y1="10" x2="30" y2="70" stroke="#90CAF9" stroke-width="2"/>
      <line x1="0" y1="40" x2="60" y2="40" stroke="#90CAF9" stroke-width="2"/>
      <line x1="10" y1="20" x2="50" y2="60" stroke="#90CAF9" stroke-width="2"/>
      <line x1="50" y1="20" x2="10" y2="60" stroke="#90CAF9" stroke-width="2"/>
      <circle cx="30" cy="40" r="5" fill="#BBDEFB"/>
    </g>
  </g>
  <!-- Works -->
  <rect x="230" y="50" width="240" height="130" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="350" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Сказки Андерсена</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="245" y="95">Снежная королева</text>
    <text x="245" y="112">Гадкий утёнок</text>
    <text x="245" y="129">Дюймовочка</text>
    <text x="245" y="146">Русалочка</text>
    <text x="245" y="163">Стойкий оловянный солдатик</text>
    <text x="245" y="180">Огниво</text>
  </g>
  <!-- Themes -->
  <rect x="30" y="200" width="440" height="140" fill="#E3F2FD" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Главные темы сказок Андерсена</text>
  <text x="250" y="245" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Доброта и сострадание побеждают зло</text>
  <text x="250" y="265" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Настоящая красота — внутри, а не снаружи</text>
  <text x="250" y="285" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#0D47A1">Гадкий утёнок стал прекрасным лебедем</text>
  <text x="250" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">Датский сказочник, его сказки переведены на 125 языков</text>
  <text x="250" y="330" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1">Сказки Андерсена — грустные и добрые одновременно</text>
</svg>'''
}

# ============================================================
# ENGLISH SVGs (8 lessons)
# ============================================================
english_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes wave{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}.hand{animation:wave 1s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Family Members</text>
  <!-- Family tree -->
  <rect x="30" y="50" width="440" height="140" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">My Family</text>
  <g font-family="Arial,sans-serif" font-size="12" text-anchor="middle">
    <rect x="170" y="82" width="160" height="28" fill="#BBDEFB" rx="5"/>
    <text x="250" y="101" fill="#0D47A1">grandfather / grandmother</text>
    <rect x="120" y="118" width="120" height="28" fill="#C8E6C9" rx="5"/>
    <text x="180" y="137" fill="#2E7D32">father (dad)</text>
    <rect x="260" y="118" width="120" height="28" fill="#F8BBD0" rx="5"/>
    <text x="320" y="137" fill="#C2185B">mother (mum)</text>
    <rect x="80" y="155" width="80" height="25" fill="#FFF9C4" rx="5"/>
    <text x="120" y="173" fill="#F57F17">brother</text>
    <rect x="170" y="155" width="70" height="25" fill="#FFCDD2" rx="5"/>
    <text x="205" y="173" fill="#C62828">sister</text>
    <rect x="250" y="155" width="80" height="25" fill="#E1BEE7" rx="5"/>
    <text x="290" y="173" fill="#6A1B9A">baby</text>
    <rect x="340" y="155" width="80" height="25" fill="#FFECB3" rx="5"/>
    <text x="380" y="173" fill="#E65100">me!</text>
  </g>
  <!-- Phrases -->
  <rect x="30" y="205" width="440" height="130" fill="#E3F2FD" rx="10"/>
  <text x="250" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Useful Phrases</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="252">This is my mother. - Это моя мама.</text>
    <text x="50" y="272">I have got a brother. - У меня есть брат.</text>
    <text x="50" y="292">My family is big/small. - Моя семья большая/маленькая.</text>
    <text x="50" y="312">I love my family! - Я люблю свою семью!</text>
  </g>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes heart{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}.love{animation:heart 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FCE4EC"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#880E4F">Describing Family</text>
  <!-- Description bubbles -->
  <rect x="30" y="50" width="440" height="120" fill="white" rx="10" stroke="#F48FB1" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F">How to describe your family</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="82" width="130" height="25" fill="#F8BBD0" rx="5"/>
    <text x="115" y="100" text-anchor="middle" fill="#880E4F">tall / short</text>
    <rect x="195" y="82" width="130" height="25" fill="#F8BBD0" rx="5"/>
    <text x="260" y="100" text-anchor="middle" fill="#880E4F">kind / strict</text>
    <rect x="340" y="82" width="110" height="25" fill="#F8BBD0" rx="5"/>
    <text x="395" y="100" text-anchor="middle" fill="#880E4F">young / old</text>
    <rect x="50" y="115" width="150" height="25" fill="#E1BEE7" rx="5"/>
    <text x="125" y="133" text-anchor="middle" fill="#6A1B9A">beautiful / handsome</text>
    <rect x="215" y="115" width="120" height="25" fill="#E1BEE7" rx="5"/>
    <text x="275" y="133" text-anchor="middle" fill="#6A1B9A">funny / serious</text>
  </g>
  <!-- Sentences -->
  <rect x="30" y="185" width="440" height="155" fill="#FCE4EC" rx="10"/>
  <text x="250" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#880E4F">Example Sentences</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <text x="50" y="232">My mother is kind and beautiful.</text>
    <text x="50" y="250">My father is tall and strong.</text>
    <text x="50" y="268">My sister is funny and clever.</text>
    <text x="50" y="286">My brother is young and active.</text>
    <text x="50" y="304">My grandmother is wise and caring.</text>
    <text x="50" y="322">My grandfather is old but kind.</text>
  </g>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes grow{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}.fruit{animation:grow 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#2E7D32">Fruits and Vegetables</text>
  <!-- Fruits -->
  <rect x="30" y="50" width="210" height="140" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="135" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#C62828">Fruits</text>
  <g class="fruit" font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="95">apple - яблоко</text>
    <text x="50" y="112">banana - банан</text>
    <text x="50" y="129">orange - апельсин</text>
    <text x="50" y="146">grape - виноград</text>
    <text x="50" y="163">pear - груша</text>
  </g>
  <!-- Vegetables -->
  <rect x="260" y="50" width="210" height="140" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="365" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#2E7D32">Vegetables</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="275" y="95">carrot - морковь</text>
    <text x="275" y="112">potato - картофель</text>
    <text x="275" y="129">tomato - помидор</text>
    <text x="275" y="146">cucumber - огурец</text>
    <text x="275" y="163">cabbage - капуста</text>
  </g>
  <!-- Phrases -->
  <rect x="30" y="205" width="440" height="130" fill="#E8F5E9" rx="10"/>
  <text x="250" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#2E7D32">Useful Phrases</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="252">I like apples. - Я люблю яблоки.</text>
    <text x="50" y="272">Do you like bananas? - Ты любишь бананы?</text>
    <text x="50" y="292">I don't like cabbage. - Я не люблю капусту.</text>
    <text x="50" y="312">An apple a day keeps the doctor away!</text>
  </g>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes pour{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.03)}}.drink{animation:pour 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Drinks and Food</text>
  <!-- Drinks -->
  <rect x="30" y="50" width="210" height="140" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="135" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1565C0">Drinks</text>
  <g class="drink" font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="95">water - вода</text>
    <text x="50" y="112">milk - молоко</text>
    <text x="50" y="129">juice - сок</text>
    <text x="50" y="146">tea - чай</text>
    <text x="50" y="163">lemonade - лимонад</text>
  </g>
  <!-- Food -->
  <rect x="260" y="50" width="210" height="140" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="365" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Food</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="275" y="95">bread - хлеб</text>
    <text x="275" y="112">cheese - сыр</text>
    <text x="275" y="129">soup - суп</text>
    <text x="275" y="146">sandwich - бутерброд</text>
    <text x="275" y="163">cake - торт</text>
  </g>
  <!-- Phrases -->
  <rect x="30" y="205" width="440" height="130" fill="#FFF3E0" rx="10"/>
  <text x="250" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Useful Phrases</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="252">I am hungry. - Я голоден.</text>
    <text x="50" y="272">I am thirsty. - Я хочу пить.</text>
    <text x="50" y="292">Can I have some water, please?</text>
    <text x="50" y="312">Would you like some tea? - Хочешь чаю?</text>
  </g>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes tail{0%,100%{transform:rotate(-5deg)}50%{transform:rotate(5deg)}}.wag{animation:tail 1s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Pets / Domestic Animals</text>
  <!-- Pets -->
  <rect x="30" y="50" width="440" height="120" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#E65100">Pets</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="82" width="100" height="25" fill="#FFF9C4" rx="5"/><text x="100" y="100" text-anchor="middle" fill="#E65100">cat - кошка</text>
    <rect x="165" y="82" width="100" height="25" fill="#FFECB3" rx="5"/><text x="215" y="100" text-anchor="middle" fill="#E65100">dog - собака</text>
    <rect x="280" y="82" width="100" height="25" fill="#FFF9C4" rx="5"/><text x="330" y="100" text-anchor="middle" fill="#E65100">fish - рыбка</text>
    <rect x="50" y="115" width="100" height="25" fill="#FFECB3" rx="5"/><text x="100" y="133" text-anchor="middle" fill="#E65100">bird - птица</text>
    <rect x="165" y="115" width="120" height="25" fill="#FFF9C4" rx="5"/><text x="225" y="133" text-anchor="middle" fill="#E65100">hamster - хомяк</text>
    <rect x="300" y="115" width="140" height="25" fill="#FFECB3" rx="5"/><text x="370" y="133" text-anchor="middle" fill="#E65100">guinea pig - морская свинка</text>
  </g>
  <!-- Phrases -->
  <rect x="30" y="185" width="440" height="150" fill="#FFF8E1" rx="10"/>
  <text x="250" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Talking about pets</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="232">I have got a cat. - У меня есть кошка.</text>
    <text x="50" y="252">My cat is fluffy. - Моя кошка пушистая.</text>
    <text x="50" y="272">It can run and jump. - Она умеет бегать и прыгать.</text>
    <text x="50" y="292">I feed my pet every day. - Я кормлю питомца каждый день.</text>
    <text x="50" y="312">Pets are our friends! - Питомцы — наши друзья!</text>
  </g>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes roam{0%,100%{transform:translateX(0)}50%{transform:translateX(5px)}}.wild{animation:roam 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Wild Animals</text>
  <!-- Animals grid -->
  <rect x="30" y="50" width="440" height="120" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <g class="wild" font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="60" width="100" height="25" fill="#C8E6C9" rx="5"/><text x="100" y="78" text-anchor="middle" fill="#1B5E20">bear - медведь</text>
    <rect x="165" y="60" width="100" height="25" fill="#E8F5E9" rx="5"/><text x="215" y="78" text-anchor="middle" fill="#1B5E20">wolf - волк</text>
    <rect x="280" y="60" width="100" height="25" fill="#C8E6C9" rx="5"/><text x="330" y="78" text-anchor="middle" fill="#1B5E20">fox - лиса</text>
    <rect x="50" y="95" width="100" height="25" fill="#E8F5E9" rx="5"/><text x="100" y="113" text-anchor="middle" fill="#1B5E20">deer - олень</text>
    <rect x="165" y="95" width="100" height="25" fill="#C8E6C9" rx="5"/><text x="215" y="113" text-anchor="middle" fill="#1B5E20">hare - заяц</text>
    <rect x="280" y="95" width="100" height="25" fill="#E8F5E9" rx="5"/><text x="330" y="113" text-anchor="middle" fill="#1B5E20">snake - змея</text>
    <rect x="390" y="60" width="70" height="60" fill="#DCEDC8" rx="5"/><text x="425" y="85" text-anchor="middle" fill="#1B5E20">lion</text><text x="425" y="100" text-anchor="middle" fill="#1B5E20">лев</text>
  </g>
  <!-- Phrases -->
  <rect x="30" y="185" width="440" height="150" fill="#E8F5E9" rx="10"/>
  <text x="250" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Talking about wild animals</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="232">Wild animals live in the forest. - Дикие животные живут в лесу.</text>
    <text x="50" y="252">The bear is big and strong. - Медведь большой и сильный.</text>
    <text x="50" y="272">The fox is clever. - Лиса хитрая.</text>
    <text x="50" y="292">Wild animals hunt for food. - Дикие животные добывают пищу.</text>
    <text x="50" y="312">We must protect wild animals! - Мы должны беречь диких животных!</text>
  </g>
</svg>''',

    7: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes rainbow{0%,100%{opacity:1}50%{opacity:0.8}}.colorful{animation:rainbow 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF8E1"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#E65100">Colours / Colors</text>
  <!-- Color palette -->
  <rect x="30" y="50" width="440" height="140" fill="white" rx="10" stroke="#FFE082" stroke-width="2"/>
  <g class="colorful">
    <rect x="50" y="65" width="60" height="40" fill="#F44336" rx="5"/><text x="80" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#C62828">red</text>
    <rect x="120" y="65" width="60" height="40" fill="#FF9800" rx="5"/><text x="150" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E65100">orange</text>
    <rect x="190" y="65" width="60" height="40" fill="#FFC107" rx="5"/><text x="220" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F57F17">yellow</text>
    <rect x="260" y="65" width="60" height="40" fill="#4CAF50" rx="5"/><text x="290" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32">green</text>
    <rect x="330" y="65" width="60" height="40" fill="#2196F3" rx="5"/><text x="360" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1565C0">blue</text>
    <rect x="400" y="65" width="60" height="40" fill="#9C27B0" rx="5"/><text x="430" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">purple</text>
    <rect x="50" y="130" width="60" height="40" fill="#E91E63" rx="5"/><text x="80" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#AD1457">pink</text>
    <rect x="120" y="130" width="60" height="40" fill="#795548" rx="5"/><text x="150" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#4E342E">brown</text>
    <rect x="190" y="130" width="60" height="40" fill="#212121" rx="5"/><text x="220" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#212121">black</text>
    <rect x="260" y="130" width="60" height="40" fill="#F5F5F5" rx="5" stroke="#E0E0E0"/><text x="290" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#616161">white</text>
    <rect x="330" y="130" width="60" height="40" fill="#9E9E9E" rx="5"/><text x="360" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#424242">grey</text>
  </g>
  <!-- Phrases -->
  <rect x="30" y="205" width="440" height="130" fill="#FFF8E1" rx="10"/>
  <text x="250" y="228" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#E65100">Describing colours</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="252">The apple is red. - Яблоко красное.</text>
    <text x="50" y="272">The sky is blue. - Небо голубое.</text>
    <text x="50" y="292">What colour is it? - Какого это цвета?</text>
    <text x="50" y="312">It is green. - Оно зелёное.</text>
  </g>
</svg>''',

    8: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes count{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}.number{animation:count 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8EAF6"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#283593">Numbers 1-20</text>
  <!-- Number grid -->
  <rect x="30" y="50" width="440" height="160" fill="white" rx="10" stroke="#9FA8DA" stroke-width="2"/>
  <g font-family="Arial,sans-serif" font-size="12" fill="#283593">
    <text x="60" y="75">1 - one</text><text x="160" y="75">2 - two</text><text x="260" y="75">3 - three</text><text x="370" y="75">4 - four</text>
    <text x="60" y="95">5 - five</text><text x="160" y="95">6 - six</text><text x="260" y="95">7 - seven</text><text x="370" y="95">8 - eight</text>
    <text x="60" y="115">9 - nine</text><text x="160" y="115">10 - ten</text><text x="260" y="115">11 - eleven</text><text x="370" y="115">12 - twelve</text>
    <text x="60" y="135">13 - thirteen</text><text x="190" y="135">14 - fourteen</text><text x="330" y="135">15 - fifteen</text>
    <text x="60" y="155">16 - sixteen</text><text x="190" y="155">17 - seventeen</text><text x="330" y="155">18 - eighteen</text>
    <text x="60" y="175">19 - nineteen</text><text x="190" y="175">20 - twenty</text>
  </g>
  <!-- Phrases -->
  <rect x="30" y="225" width="440" height="110" fill="#E8EAF6" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#283593">Using numbers</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="272">I am eight years old. - Мне 8 лет.</text>
    <text x="50" y="292">How old are you? - Сколько тебе лет?</text>
    <text x="50" y="312">I have got twelve pencils. - У меня 12 карандашей.</text>
  </g>
</svg>'''
}

# ============================================================
# WORLD SVGs (8 lessons)
# ============================================================
world_svgs = {
    1: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.03)}}.alive{animation:breathe 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Живая и неживая природа</text>
  <!-- Living -->
  <rect x="30" y="50" width="210" height="170" fill="white" rx="10" stroke="#66BB6A" stroke-width="2"/>
  <text x="135" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#2E7D32">Живая природа</text>
  <g class="alive" font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="95">Растёт</text>
    <text x="50" y="112">Питается</text>
    <text x="50" y="129">Дышит</text>
    <text x="50" y="146">Размножается</text>
    <text x="50" y="163">Умирает</text>
  </g>
  <text x="135" y="200" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#2E7D32">деревья, цветы, животные, грибы</text>
  <!-- Non-living -->
  <rect x="260" y="50" width="210" height="170" fill="white" rx="10" stroke="#90A4AE" stroke-width="2"/>
  <text x="365" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#546E7A">Неживая природа</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="280" y="95">Не растёт</text>
    <text x="280" y="112">Не питается</text>
    <text x="280" y="129">Не дышит</text>
    <text x="280" y="146">Не размножается</text>
    <text x="280" y="163">Может разрушаться</text>
  </g>
  <text x="365" y="200" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#546E7A">камни, вода, солнце, воздух</text>
  <!-- Venn -->
  <rect x="30" y="235" width="440" height="100" fill="#E8F5E9" rx="10"/>
  <text x="250" y="258" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Признаки живого</text>
  <text x="250" y="280" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Рост, питание, дыхание, размножение, развитие</text>
  <text x="250" y="300" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#555">Всё живое когда-нибудь умирает</text>
  <text x="250" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#1B5E20">Почва — связь живой и неживой природы</text>
</svg>''',

    2: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes rain{0%,100%{transform:translateY(0)}50%{transform:translateY(3px)}}.weather{animation:rain 1.5s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Явления природы</text>
  <!-- Phenomena grid -->
  <rect x="30" y="50" width="440" height="130" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="62" width="120" height="30" fill="#FFF9C4" rx="5"/><text x="110" y="82" text-anchor="middle" fill="#F57F17">Дождь</text>
    <rect x="185" y="62" width="120" height="30" fill="#E3F2FD" rx="5"/><text x="245" y="82" text-anchor="middle" fill="#1565C0">Снег</text>
    <rect x="320" y="62" width="130" height="30" fill="#BBDEFB" rx="5"/><text x="385" y="82" text-anchor="middle" fill="#0D47A1">Град</text>
    <rect x="50" y="100" width="120" height="30" fill="#FFECB3" rx="5"/><text x="110" y="120" text-anchor="middle" fill="#E65100">Ветер</text>
    <rect x="185" y="100" width="120" height="30" fill="#C8E6C9" rx="5"/><text x="245" y="120" text-anchor="middle" fill="#2E7D32">Туман</text>
    <rect x="320" y="100" width="130" height="30" fill="#F8BBD0" rx="5"/><text x="385" y="120" text-anchor="middle" fill="#C2185B">Радуга</text>
    <rect x="50" y="140" width="120" height="30" fill="#FFCDD2" rx="5"/><text x="110" y="160" text-anchor="middle" fill="#C62828">Гроза</text>
    <rect x="185" y="140" width="120" height="30" fill="#E1BEE7" rx="5"/><text x="245" y="160" text-anchor="middle" fill="#6A1B9A">Молния</text>
    <rect x="320" y="140" width="130" height="30" fill="#DCEDC8" rx="5"/><text x="385" y="160" text-anchor="middle" fill="#33691E">Роса</text>
  </g>
  <!-- Seasons -->
  <rect x="30" y="200" width="440" height="140" fill="#E3F2FD" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Явления по сезонам</text>
  <g font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="235" width="90" height="40" fill="#C8E6C9" rx="5"/><text x="95" y="252" text-anchor="middle" fill="#2E7D32">Весна</text><text x="95" y="268" text-anchor="middle" fill="#555">половодье</text>
    <rect x="155" y="235" width="90" height="40" fill="#FFF9C4" rx="5"/><text x="200" y="252" text-anchor="middle" fill="#F57F17">Лето</text><text x="200" y="268" text-anchor="middle" fill="#555">жара, гроза</text>
    <rect x="260" y="235" width="90" height="40" fill="#FFECB3" rx="5"/><text x="305" y="252" text-anchor="middle" fill="#E65100">Осень</text><text x="305" y="268" text-anchor="middle" fill="#555">листопад</text>
    <rect x="365" y="235" width="90" height="40" fill="#BBDEFB" rx="5"/><text x="410" y="252" text-anchor="middle" fill="#1565C0">Зима</text><text x="410" y="268" text-anchor="middle" fill="#555">метель</text>
  </g>
  <text x="250" y="305" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#0D47A1">Явления природы — это изменения, которые происходят в природе</text>
  <text x="250" y="325" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#555">За изменениями природы люди наблюдают с давних времён</text>
</svg>''',

    3: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes wave{0%,100%{transform:translateX(0)}50%{transform:translateX(3px)}}.water{animation:wave 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E3F2FD"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#0D47A1">Водоёмы</text>
  <!-- Types -->
  <rect x="30" y="50" width="440" height="160" fill="white" rx="10" stroke="#90CAF9" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#0D47A1">Виды водоёмов</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="82" width="190" height="30" fill="#BBDEFB" rx="5"/><text x="145" y="102" text-anchor="middle" fill="#0D47A1">Океан — самый большой</text>
    <rect x="260" y="82" width="190" height="30" fill="#90CAF9" rx="5"/><text x="355" y="102" text-anchor="middle" fill="#0D47A1">Море — часть океана</text>
    <rect x="50" y="120" width="190" height="30" fill="#64B5F6" rx="5"/><text x="145" y="140" text-anchor="middle" fill="#0D47A1">Озеро — замкнутый</text>
    <rect x="260" y="120" width="190" height="30" fill="#42A5F5" rx="5"/><text x="355" y="140" text-anchor="middle" fill="white">Река — течёт</text>
    <rect x="50" y="158" width="190" height="30" fill="#2196F3" rx="5"/><text x="145" y="178" text-anchor="middle" fill="white">Ручей — маленькая речка</text>
    <rect x="260" y="158" width="190" height="30" fill="#1976D2" rx="5"/><text x="355" y="178" text-anchor="middle" fill="white">Пруд — искусственный</text>
  </g>
  <!-- Water properties -->
  <rect x="30" y="225" width="440" height="110" fill="#E3F2FD" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#0D47A1">Свойства воды</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">Прозрачная, без цвета, без запаха, без вкуса</text>
    <text x="50" y="290">Текёт, принимает форму сосуда</text>
    <text x="50" y="310">Может быть твёрдой (лёд), жидкой, газом (пар)</text>
    <text x="50" y="330">Вода — самое важное вещество для жизни на Земле</text>
  </g>
</svg>''',

    4: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes shine{0%,100%{opacity:1}50%{opacity:0.7}}.mineral{animation:shine 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Полезные ископаемые</text>
  <!-- Types -->
  <rect x="30" y="50" width="440" height="130" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <g class="mineral" font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="62" width="120" height="28" fill="#FFCCBC" rx="5"/><text x="110" y="81" text-anchor="middle" fill="#BF360C">Нефть</text>
    <rect x="185" y="62" width="120" height="28" fill="#37474F" rx="5"/><text x="245" y="81" text-anchor="middle" fill="white">Уголь</text>
    <rect x="320" y="62" width="120" height="28" fill="#FFF9C4" rx="5"/><text x="380" y="81" text-anchor="middle" fill="#F57F17">Песок</text>
    <rect x="50" y="100" width="120" height="28" fill="#FFECB3" rx="5"/><text x="110" y="119" text-anchor="middle" fill="#E65100">Глина</text>
    <rect x="185" y="100" width="120" height="28" fill="#E0E0E0" rx="5"/><text x="245" y="119" text-anchor="middle" fill="#424242">Гранит</text>
    <rect x="320" y="100" width="120" height="28" fill="#D7CCC8" rx="5"/><text x="380" y="119" text-anchor="middle" fill="#5D4037">Известняк</text>
    <rect x="50" y="138" width="120" height="28" fill="#C8E6C9" rx="5"/><text x="110" y="157" text-anchor="middle" fill="#2E7D32">Торф</text>
    <rect x="185" y="138" width="120" height="28" fill="#BBDEFB" rx="5"/><text x="245" y="157" text-anchor="middle" fill="#1565C0">Железная руда</text>
  </g>
  <!-- Uses -->
  <rect x="30" y="200" width="440" height="140" fill="#FFF3E0" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Для чего используют</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="245">Нефть — бензин, пластмасса</text>
    <text x="50" y="265">Уголь — топливо, тепло</text>
    <text x="50" y="285">Глина — кирпичи, посуда</text>
    <text x="50" y="305">Песок — стекло, бетон</text>
    <text x="50" y="325">Железная руда — металлы</text>
  </g>
</svg>''',

    5: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes sway{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(2deg)}}.plant{animation:sway 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Растения и их разнообразие</text>
  <!-- Plant groups -->
  <rect x="30" y="50" width="440" height="130" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20">Группы растений</text>
  <g font-family="Arial,sans-serif" font-size="12">
    <rect x="50" y="82" width="100" height="40" fill="#C8E6C9" rx="5"/><text x="100" y="100" text-anchor="middle" fill="#1B5E20">Деревья</text><text x="100" y="115" text-anchor="middle" fill="#555" font-size="10">берёза, дуб</text>
    <rect x="165" y="82" width="100" height="40" fill="#DCEDC8" rx="5"/><text x="215" y="100" text-anchor="middle" fill="#33691E">Кустарники</text><text x="215" y="115" text-anchor="middle" fill="#555" font-size="10">шиповник, смородина</text>
    <rect x="280" y="82" width="100" height="40" fill="#F1F8E9" rx="5"/><text x="330" y="100" text-anchor="middle" fill="#1B5E20">Травы</text><text x="330" y="115" text-anchor="middle" fill="#555" font-size="10">одуванчик, клевер</text>
    <rect x="395" y="82" width="60" height="40" fill="#E8F5E9" rx="5"/><text x="425" y="100" text-anchor="middle" fill="#1B5E20">Мхи</text><text x="425" y="115" text-anchor="middle" fill="#555" font-size="10">кукушкин лён</text>
  </g>
  <!-- Parts of a plant -->
  <rect x="30" y="195" width="440" height="145" fill="#E8F5E9" rx="10"/>
  <text x="250" y="218" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Части растения</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="240">Корень — впитывает воду и питательные вещества</text>
    <text x="50" y="258">Стебель — переносит вещества</text>
    <text x="50" y="276">Лист — питает растение (фотосинтез)</text>
    <text x="50" y="294">Цветок — образует плод</text>
    <text x="50" y="312">Плод и семена — размножение</text>
    <text x="50" y="330" fill="#1B5E20">Растения — основа жизни на Земле</text>
  </g>
</svg>''',

    6: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes move{0%,100%{transform:translateX(0)}50%{transform:translateX(3px)}}.animal{animation:move 2s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFF3E0"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#BF360C">Животные и их группы</text>
  <!-- Animal groups -->
  <rect x="30" y="50" width="440" height="160" fill="white" rx="10" stroke="#FFAB91" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#BF360C">Группы животных</text>
  <g class="animal" font-family="Arial,sans-serif" font-size="11">
    <rect x="50" y="82" width="120" height="35" fill="#FFCCBC" rx="5"/><text x="110" y="97" text-anchor="middle" fill="#BF360C" font-weight="bold">Млекопитающие</text><text x="110" y="112" text-anchor="middle" fill="#555">кормят молоком</text>
    <rect x="185" y="82" width="120" height="35" fill="#FFE0B2" rx="5"/><text x="245" y="97" text-anchor="middle" fill="#E65100" font-weight="bold">Птицы</text><text x="245" y="112" text-anchor="middle" fill="#555">имеют перья</text>
    <rect x="320" y="82" width="120" height="35" fill="#FFF9C4" rx="5"/><text x="380" y="97" text-anchor="middle" fill="#F57F17" font-weight="bold">Рыбы</text><text x="380" y="112" text-anchor="middle" fill="#555">живут в воде</text>
    <rect x="50" y="128" width="120" height="35" fill="#C8E6C9" rx="5"/><text x="110" y="143" text-anchor="middle" fill="#2E7D32" font-weight="bold">Земноводные</text><text x="110" y="158" text-anchor="middle" fill="#555">лягушки, тритоны</text>
    <rect x="185" y="128" width="120" height="35" fill="#BBDEFB" rx="5"/><text x="245" y="143" text-anchor="middle" fill="#1565C0" font-weight="bold">Пресмыкающиеся</text><text x="245" y="158" text-anchor="middle" fill="#555">ящерицы, змеи</text>
    <rect x="320" y="128" width="120" height="35" fill="#E1BEE7" rx="5"/><text x="380" y="143" text-anchor="middle" fill="#6A1B9A" font-weight="bold">Насекомые</text><text x="380" y="158" text-anchor="middle" fill="#555">6 ног, жуки, бабочки</text>
  </g>
  <!-- Features -->
  <rect x="30" y="225" width="440" height="110" fill="#FFF3E0" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#BF360C">Чем различаются группы</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">Покров тела: шерсть, перья, чешуя, кожа</text>
    <text x="50" y="290">Количество ног: 0, 4, 6, 8</text>
    <text x="50" y="310">Где живут: вода, земля, воздух</text>
    <text x="50" y="330">Чем питаются: растения, другие животные</text>
  </g>
</svg>''',

    7: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes protect{0%,100%{transform:scale(1)}50%{transform:scale(1.02)}}.book{animation:protect 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#FFEBEE"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#B71C1C">Красная книга</text>
  <!-- Red book -->
  <g class="book" transform="translate(30,50)">
    <rect x="0" y="0" width="160" height="130" fill="#C62828" rx="5"/>
    <rect x="5" y="5" width="150" height="120" fill="#FFCDD2" rx="3"/>
    <text x="80" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="#B71C1C">КРАСНАЯ</text>
    <text x="80" y="60" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="#B71C1C">КНИГА</text>
    <line x1="20" y1="70" x2="140" y2="70" stroke="#B71C1C" stroke-width="1"/>
    <text x="80" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#B71C1C">Редкие и исчезающие</text>
    <text x="80" y="105" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#B71C1C">виды животных</text>
    <text x="80" y="120" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#B71C1C">и растений</text>
  </g>
  <!-- Categories -->
  <rect x="210" y="50" width="260" height="130" fill="white" rx="10" stroke="#EF9A9A" stroke-width="2"/>
  <text x="340" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#B71C1C">Категории</text>
  <g font-family="Arial,sans-serif" font-size="11" fill="#333">
    <rect x="225" y="80" width="100" height="22" fill="#FFCDD2" rx="3"/><text x="275" y="96" text-anchor="middle" fill="#C62828">Исчезающие</text>
    <rect x="335" y="80" width="120" height="22" fill="#FFECB3" rx="3"/><text x="395" y="96" text-anchor="middle" fill="#E65100">Сокращающиеся</text>
    <rect x="225" y="110" width="100" height="22" fill="#FFF9C4" rx="3"/><text x="275" y="126" text-anchor="middle" fill="#F57F17">Редкие</text>
    <rect x="335" y="110" width="120" height="22" fill="#C8E6C9" rx="3"/><text x="395" y="126" text-anchor="middle" fill="#2E7D32">Восстанавливаемые</text>
  </g>
  <text x="340" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#B71C1C">Амурский тигр, белый медведь, лотос</text>
  <text x="340" y="170" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#555">Зубр, снежный барс, журавль</text>
  <!-- How to help -->
  <rect x="30" y="200" width="440" height="135" fill="#FFEBEE" rx="10"/>
  <text x="250" y="222" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#B71C1C">Как мы можем помочь?</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="245">Не рвать редкие цветы</text>
    <text x="50" y="265">Не разорять гнёзда и муравейники</text>
    <text x="50" y="285">Не мусорить в лесу и у водоёмов</text>
    <text x="50" y="305">Беречь природу и животных</text>
    <text x="50" y="325" fill="#B71C1C" font-weight="bold">Красная книга — сигнал тревоги!</text>
  </g>
</svg>''',

    8: '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs><style>@keyframes leaf{0%,100%{transform:rotate(-5deg)}50%{transform:rotate(5deg)}}.nature{animation:leaf 3s ease-in-out infinite}</style></defs>
  <rect width="500" height="350" fill="#E8F5E9"/>
  <text x="250" y="32" text-anchor="middle" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#1B5E20">Охрана природы</text>
  <!-- Rules -->
  <rect x="30" y="50" width="440" height="160" fill="white" rx="10" stroke="#A5D6A7" stroke-width="2"/>
  <text x="250" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1B5E20">Правила охраны природы</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="95">1. Не мусорить в лесу, парке, у реки</text>
    <text x="50" y="115">2. Не разжигать костры без разрешения</text>
    <text x="50" y="135">3. Не ломать ветки и не рвать цветы</text>
    <text x="50" y="155">4. Не разорять птичьи гнёзда</text>
    <text x="50" y="175">5. Не ловить диких животных</text>
    <text x="50" y="195">6. Бережно относиться к воде</text>
  </g>
  <!-- Why protect -->
  <rect x="30" y="225" width="440" height="110" fill="#E8F5E9" rx="10"/>
  <text x="250" y="248" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1B5E20">Почему важно беречь природу?</text>
  <g font-family="Arial,sans-serif" font-size="12" fill="#333">
    <text x="50" y="270">Природа — наш дом</text>
    <text x="50" y="290">Загрязнение вредно для всех живых существ</text>
    <text x="50" y="310">Исчезновение одного вида нарушает равновесие</text>
    <text x="50" y="330" fill="#1B5E20" font-weight="bold">Природу нужно беречь для будущих поколений!</text>
  </g>
</svg>'''
}

# Save all
for i, svg in literature_svgs.items():
    path = os.path.join(SVG_DIR, 'literature', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

for i, svg in english_svgs.items():
    path = os.path.join(SVG_DIR, 'english', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

for i, svg in world_svgs.items():
    path = os.path.join(SVG_DIR, 'world', f'lesson{i}-unique.svg')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

print(f"Saved: literature ({len(literature_svgs)}) + english ({len(english_svgs)}) + world ({len(world_svgs)}) = {len(literature_svgs)+len(english_svgs)+len(world_svgs)} SVGs")
