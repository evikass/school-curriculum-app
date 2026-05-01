#!/usr/bin/env python3
"""Generate Grade 11 Physics and Algebra lesson SVG files."""

import os
import xml.etree.ElementTree as ET

# ── Paths ──────────────────────────────────────────────────────────────────
BASE = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11"
PHYSICS_DIR = os.path.join(BASE, "physics")
ALGEBRA_DIR = os.path.join(BASE, "algebra")

os.makedirs(PHYSICS_DIR, exist_ok=True)
os.makedirs(ALGEBRA_DIR, exist_ok=True)

# ── Physics lesson data ───────────────────────────────────────────────────
physics_lessons = [
    {
        "n": 1,
        "title": "Магнитное поле",
        "subject_header": "Физика — Урок 1",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <!-- Magnetic field lines illustration -->
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- Bar magnet -->
    <rect x="40" y="100" width="80" height="35" rx="3" fill="#E53935" stroke="#B71C1C" stroke-width="1"/>
    <rect x="120" y="100" width="80" height="35" rx="3" fill="#1E88E5" stroke="#0D47A1" stroke-width="1"/>
    <text x="70" y="123" font-family="Arial,sans-serif" font-size="16" fill="white" text-anchor="middle" font-weight="bold">N</text>
    <text x="150" y="123" font-family="Arial,sans-serif" font-size="16" fill="white" text-anchor="middle" font-weight="bold">S</text>
    <!-- Field lines from N to S (external) -->
    <path d="M80,100 Q80,70 150,70 Q220,70 220,100" fill="none" stroke="#1565C0" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
    <path d="M100,100 Q100,80 150,80 Q200,80 200,100" fill="none" stroke="#1565C0" stroke-width="1.5"/>
    <path d="M80,135 Q80,165 150,165 Q220,165 220,135" fill="none" stroke="#1565C0" stroke-width="1.5" marker-end="url(#arrowBlue)"/>
    <path d="M100,135 Q100,155 150,155 Q200,155 200,135" fill="none" stroke="#1565C0" stroke-width="1.5"/>
    <!-- Current-carrying conductor cross-section -->
    <circle cx="320" cy="115" r="15" fill="white" stroke="#1565C0" stroke-width="2"/>
    <circle cx="320" cy="115" r="3" fill="#1565C0"/>
    <text x="320" y="100" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1" text-anchor="middle">⊙ I</text>
    <!-- Circular B-field around conductor -->
    <circle cx="320" cy="115" r="28" fill="none" stroke="#1565C0" stroke-width="1" stroke-dasharray="4,3"/>
    <circle cx="320" cy="115" r="42" fill="none" stroke="#1565C0" stroke-width="1" stroke-dasharray="4,3"/>
    <text x="365" y="115" font-family="Arial,sans-serif" font-size="9" fill="#1565C0">B</text>
    <!-- Right-hand rule hint -->
    <text x="320" y="168" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1" text-anchor="middle">Правило буравчика</text>
    <!-- Formulas box -->
    <rect x="20" y="180" width="225" height="112" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="198" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Сила Ампера:</text>
    <text x="30" y="215" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">F = B·I·L·sin(α)</text>
    <text x="30" y="232" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Сила Лоренца:</text>
    <text x="30" y="249" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">F = q·v·B·sin(α)</text>
    <text x="30" y="266" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Магнитный поток:</text>
    <text x="30" y="283" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">Φ = B·S·cos(α)</text>
    <!-- Right box: properties -->
    <rect x="255" y="180" width="225" height="112" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="265" y="198" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Свойства магнитного поля:</text>
    <text x="265" y="215" font-family="Arial,sans-serif" font-size="10" fill="#444">• Порождается движущимися зарядами</text>
    <text x="265" y="230" font-family="Arial,sans-serif" font-size="10" fill="#444">• Действует на движущиеся заряды</text>
    <text x="265" y="245" font-family="Arial,sans-serif" font-size="10" fill="#444">• Замкнутые силовые линии</text>
    <text x="265" y="260" font-family="Arial,sans-serif" font-size="10" fill="#444">• В = μ₀μH (в веществе)</text>
    <text x="265" y="278" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" font-weight="bold">μ₀ = 4π·10⁻⁷ Тл·м/А</text>
    <text x="265" y="293" font-family="Arial,sans-serif" font-size="10" fill="#1565C0">[B] = Тл (тесла)</text>
    """,
    },
    {
        "n": 2,
        "title": "Электромагнитная индукция",
        "subject_header": "Физика — Урок 2",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- Coil with changing flux -->
    <rect x="30" y="95" width="130" height="90" rx="5" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="95" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Катушка в магнитном поле</text>
    <!-- Coil loops -->
    <ellipse cx="70" cy="155" rx="15" ry="20" fill="none" stroke="#1565C0" stroke-width="2"/>
    <ellipse cx="95" cy="155" rx="15" ry="20" fill="none" stroke="#1565C0" stroke-width="2"/>
    <ellipse cx="120" cy="155" rx="15" ry="20" fill="none" stroke="#1565C0" stroke-width="2"/>
    <!-- Arrow showing B -->
    <line x1="45" y1="130" x2="145" y2="130" stroke="#E53935" stroke-width="2" marker-end="url(#arrowRed)"/>
    <text x="100" y="128" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle">B →</text>
    <!-- Galvanometer -->
    <circle cx="250" cy="120" r="20" fill="white" stroke="#1565C0" stroke-width="2"/>
    <text x="250" y="118" font-family="Arial,sans-serif" font-size="7" fill="#0D47A1" text-anchor="middle">G</text>
    <line x1="250" y1="128" x2="255" y2="138" stroke="#E53935" stroke-width="2"/>
    <line x1="150" y1="155" x2="230" y2="130" stroke="#1565C0" stroke-width="1.5"/>
    <line x1="270" y1="120" x2="150" y2="165" stroke="#1565C0" stroke-width="1.5"/>
    <!-- EMF graph -->
    <rect x="300" y="95" width="170" height="90" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="385" y="108" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">ЭДС индукции</text>
    <line x1="315" y1="170" x2="455" y2="170" stroke="#0D47A1" stroke-width="1"/>
    <line x1="315" y1="170" x2="315" y2="115" stroke="#0D47A1" stroke-width="1"/>
    <path d="M320,155 Q340,115 360,155 Q380,195 400,155 Q420,115 440,155" fill="none" stroke="#E53935" stroke-width="2"/>
    <text x="460" y="173" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">t</text>
    <text x="310" y="113" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">ε</text>
    <!-- Formulas box -->
    <rect x="20" y="192" width="225" height="100" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="210" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Закон Фарадея:</text>
    <text x="30" y="228" font-family="Arial,sans-serif" font-size="13" fill="#1565C0">ε = −dΦ/dt</text>
    <text x="30" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Правило Ленца:</text>
    <text x="30" y="265" font-family="Arial,sans-serif" font-size="10" fill="#444">Индукционный ток препятствует</text>
    <text x="30" y="278" font-family="Arial,sans-serif" font-size="10" fill="#444">изменению магнитного потока</text>
    <!-- Right box -->
    <rect x="255" y="192" width="225" height="100" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="265" y="210" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">ЭДС движущегося проводника:</text>
    <text x="265" y="228" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">ε = B·L·v·sin(α)</text>
    <text x="265" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Самоиндукция:</text>
    <text x="265" y="265" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">ε = −L·dI/dt</text>
    <text x="265" y="283" font-family="Arial,sans-serif" font-size="10" fill="#1565C0">[L] = Гн (генри)</text>
    """,
    },
    {
        "n": 3,
        "title": "Гармонические колебания",
        "subject_header": "Физика — Урок 3",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- Pendulum illustration -->
    <rect x="25" y="95" width="150" height="115" rx="5" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="100" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Маятник</text>
    <line x1="100" y1="118" x2="65" y2="185" stroke="#555" stroke-width="2"/>
    <circle cx="65" cy="188" r="8" fill="#1565C0"/>
    <line x1="100" y1="118" x2="100" y2="118" stroke="#555" stroke-width="0.5" stroke-dasharray="3,3"/>
    <line x1="100" y1="118" x2="135" y2="185" stroke="#555" stroke-width="1.5" stroke-dasharray="4,3"/>
    <circle cx="135" cy="188" r="6" fill="#90CAF9" stroke="#1565C0" stroke-width="1"/>
    <!-- x(t) graph -->
    <rect x="190" y="95" width="145" height="115" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="262" y="108" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">x(t)</text>
    <line x1="200" y1="155" x2="325" y2="155" stroke="#0D47A1" stroke-width="1"/>
    <line x1="200" y1="195" x2="200" y2="115" stroke="#0D47A1" stroke-width="1"/>
    <path d="M205,155 Q215,115 230,155 Q245,195 255,155 Q265,115 280,155 Q295,195 305,155 Q315,115 320,145" fill="none" stroke="#E53935" stroke-width="2"/>
    <text x="327" y="158" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">t</text>
    <text x="193" y="112" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">x</text>
    <!-- Amplitude marker -->
    <line x1="195" y1="120" x2="205" y2="120" stroke="#4CAF50" stroke-width="1"/>
    <text x="200" y="117" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50" text-anchor="middle">A</text>
    <!-- Spring illustration -->
    <rect x="345" y="95" width="145" height="115" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="417" y="108" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Пружинный маятник</text>
    <rect x="350" y="140" width="15" height="35" fill="#888"/>
    <path d="M365,155 L375,140 L385,170 L395,140 L405,170 L415,140 L425,170 L435,155" fill="none" stroke="#1565C0" stroke-width="2"/>
    <rect x="435" y="143" width="20" height="24" rx="3" fill="#1565C0"/>
    <!-- Formulas box -->
    <rect x="20" y="218" width="225" height="76" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="236" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Уравнение колебания:</text>
    <text x="30" y="255" font-family="Arial,sans-serif" font-size="13" fill="#1565C0">x = A·cos(ωt + φ₀)</text>
    <text x="30" y="273" font-family="Arial,sans-serif" font-size="11" fill="#444">ω = 2π/T = 2πν</text>
    <text x="30" y="288" font-family="Arial,sans-serif" font-size="10" fill="#1565C0">T = 2π√(m/k) — пружинный</text>
    <!-- Right box -->
    <rect x="255" y="218" width="225" height="76" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="265" y="236" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Энергия:</text>
    <text x="265" y="255" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">E = ½kA² = ½mω²A²</text>
    <text x="265" y="273" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Период мат. маятника:</text>
    <text x="265" y="290" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">T = 2π√(L/g)</text>
    """,
    },
    {
        "n": 4,
        "title": "Электромагнитные колебания",
        "subject_header": "Физика — Урок 4",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- LC circuit -->
    <rect x="25" y="95" width="220" height="130" rx="5" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Колебательный контур (LC)</text>
    <!-- Capacitor -->
    <line x1="60" y1="135" x2="60" y2="175" stroke="#1565C0" stroke-width="3"/>
    <line x1="75" y1="135" x2="75" y2="175" stroke="#1565C0" stroke-width="3"/>
    <!-- Wires -->
    <line x1="45" y1="130" x2="60" y2="155" stroke="#0D47A1" stroke-width="1.5"/>
    <line x1="75" y1="155" x2="195" y2="155" stroke="#0D47A1" stroke-width="1.5"/>
    <!-- Inductor coil -->
    <path d="M195,155 Q200,135 210,155 Q220,135 230,155 Q240,135 250,155 Q260,135 270,155" fill="none" stroke="#1565C0" stroke-width="2"/>
    <line x1="270" y1="155" x2="45" y2="155" stroke="none"/>
    <line x1="270" y1="155" x2="230" y2="180" stroke="#0D47A1" stroke-width="1.5"/>
    <line x1="45" y1="155" x2="45" y2="130" stroke="#0D47A1" stroke-width="1.5"/>
    <line x1="45" y1="130" x2="60" y2="130" stroke="#0D47A1" stroke-width="1.5"/>
    <line x1="75" y1="130" x2="45" y2="130" stroke="none"/>
    <line x1="75" y1="130" x2="230" y2="130" stroke="#0D47A1" stroke-width="1.5"/>
    <line x1="230" y1="130" x2="230" y2="155" stroke="#0D47A1" stroke-width="1.5"/>
    <!-- Labels -->
    <text x="68" y="195" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle">C</text>
    <text x="230" y="170" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle">L</text>
    <!-- Energy exchange diagram -->
    <rect x="260" y="95" width="215" height="130" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Обмен энергией</text>
    <rect x="275" y="120" width="80" height="20" rx="5" fill="#1565C0" opacity="0.8"/>
    <text x="315" y="134" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">E_C = ½CU²</text>
    <rect x="375" y="120" width="80" height="20" rx="5" fill="#E53935" opacity="0.8"/>
    <text x="415" y="134" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">E_L = ½LI²</text>
    <path d="M355,130 L370,130" fill="none" stroke="#333" stroke-width="1.5" marker-end="url(#arrowDark)"/>
    <text x="362" y="125" font-family="Arial,sans-serif" font-size="8" fill="#333" text-anchor="middle">⇄</text>
    <text x="367" y="160" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" text-anchor="middle">E = E_C + E_L = const</text>
    <text x="367" y="178" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">E = ½CU²_max = ½LI²_max</text>
    <text x="367" y="200" font-family="Arial,sans-serif" font-size="9" fill="#666" text-anchor="middle">(закон сохранения энергии)</text>
    <!-- Formulas -->
    <rect x="20" y="230" width="460" height="66" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Формула Томсона:</text>
    <text x="30" y="268" font-family="Arial,sans-serif" font-size="14" fill="#1565C0">T = 2π√(LC)</text>
    <text x="200" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Циклическая частота:</text>
    <text x="200" y="268" font-family="Arial,sans-serif" font-size="14" fill="#1565C0">ω = 1/√(LC)</text>
    <text x="370" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Добротность:</text>
    <text x="370" y="268" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">Q = ωL/R</text>
    <text x="30" y="290" font-family="Arial,sans-serif" font-size="10" fill="#666">Уравнение: q = q₀·cos(ωt + φ₀);  I = q₀ω·sin(ωt + φ₀)</text>
    """,
    },
    {
        "n": 5,
        "title": "Геометрическая оптика",
        "subject_header": "Физика — Урок 5",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- Thin lens diagram -->
    <rect x="25" y="95" width="220" height="130" rx="5" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Тонкая линза</text>
    <!-- Lens -->
    <ellipse cx="135" cy="160" rx="5" ry="40" fill="#90CAF9" stroke="#1565C0" stroke-width="2" opacity="0.6"/>
    <!-- Optical axis -->
    <line x1="35" y1="160" x2="235" y2="160" stroke="#888" stroke-width="0.5" stroke-dasharray="4,3"/>
    <!-- Focal points -->
    <circle cx="85" cy="160" r="3" fill="#E53935"/>
    <circle cx="185" cy="160" r="3" fill="#E53935"/>
    <text x="85" y="175" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle">F</text>
    <text x="185" y="175" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle">F'</text>
    <!-- Incoming rays -->
    <line x1="40" y1="130" x2="135" y2="130" stroke="#FF9800" stroke-width="1.5"/>
    <line x1="40" y1="130" x2="135" y2="160" stroke="#FF9800" stroke-width="1.5"/>
    <line x1="40" y1="160" x2="135" y2="160" stroke="#FF9800" stroke-width="1.5"/>
    <!-- Outgoing rays (converging) -->
    <line x1="135" y1="130" x2="220" y2="185" stroke="#4CAF50" stroke-width="1.5"/>
    <line x1="135" y1="160" x2="220" y2="185" stroke="#4CAF50" stroke-width="1.5"/>
    <!-- Image point -->
    <circle cx="220" cy="185" r="3" fill="#4CAF50"/>
    <text x="220" y="198" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50" text-anchor="middle">Изобр.</text>
    <!-- 2F markers -->
    <circle cx="35" cy="160" r="2" fill="#0D47A1"/>
    <text x="55" y="155" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1">2F</text>
    <!-- Mirror diagram -->
    <rect x="260" y="95" width="215" height="130" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Зеркало</text>
    <!-- Mirror surface -->
    <path d="M300,125 Q300,160 300,195" fill="none" stroke="#1565C0" stroke-width="3"/>
    <line x1="270" y1="160" x2="460" y2="160" stroke="#888" stroke-width="0.5" stroke-dasharray="4,3"/>
    <!-- Incoming ray -->
    <line x1="420" y1="130" x2="300" y2="140" stroke="#FF9800" stroke-width="1.5"/>
    <!-- Reflected ray -->
    <line x1="300" y1="140" x2="420" y2="175" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="300" y="210" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">Угол падения = Угол отражения</text>
    <!-- Formulas -->
    <rect x="20" y="230" width="225" height="66" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Формула тонкой линзы:</text>
    <text x="30" y="268" font-family="Arial,sans-serif" font-size="14" fill="#1565C0">1/d + 1/f = 1/F = D</text>
    <text x="30" y="288" font-family="Arial,sans-serif" font-size="10" fill="#444">D — оптическая сила [дптр]</text>
    <!-- Right box -->
    <rect x="255" y="230" width="225" height="66" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="265" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Увеличение:</text>
    <text x="265" y="268" font-family="Arial,sans-serif" font-size="13" fill="#1565C0">Γ = f/d = H/h</text>
    <text x="265" y="288" font-family="Arial,sans-serif" font-size="10" fill="#444">Закон отражения: α = β</text>
    """,
    },
    {
        "n": 6,
        "title": "Волновая оптика",
        "subject_header": "Физика — Урок 6",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- Interference pattern -->
    <rect x="25" y="95" width="220" height="125" rx="5" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Интерференция</text>
    <!-- Two slits -->
    <rect x="40" y="130" width="5" height="65" fill="#555"/>
    <rect x="40" y="120" width="5" height="10" fill="#555"/>
    <rect x="40" y="195" width="5" height="5" fill="#555"/>
    <!-- Slit openings -->
    <rect x="40" y="140" width="5" height="5" fill="#E3F2FD"/>
    <rect x="40" y="170" width="5" height="5" fill="#E3F2FD"/>
    <!-- Wave fronts from slits -->
    <circle cx="45" cy="142" r="15" fill="none" stroke="#1565C0" stroke-width="0.7" opacity="0.6"/>
    <circle cx="45" cy="142" r="30" fill="none" stroke="#1565C0" stroke-width="0.7" opacity="0.5"/>
    <circle cx="45" cy="142" r="45" fill="none" stroke="#1565C0" stroke-width="0.7" opacity="0.4"/>
    <circle cx="45" cy="172" r="15" fill="none" stroke="#E53935" stroke-width="0.7" opacity="0.6"/>
    <circle cx="45" cy="172" r="30" fill="none" stroke="#E53935" stroke-width="0.7" opacity="0.5"/>
    <circle cx="45" cy="172" r="45" fill="none" stroke="#E53935" stroke-width="0.7" opacity="0.4"/>
    <!-- Screen with interference bands -->
    <rect x="210" y="120" width="5" height="80" fill="#333"/>
    <!-- Bright and dark bands on screen -->
    <rect x="216" y="122" width="12" height="4" fill="#1565C0" opacity="0.8"/>
    <rect x="216" y="128" width="12" height="4" fill="#1565C0" opacity="0.3"/>
    <rect x="216" y="134" width="12" height="4" fill="#1565C0" opacity="0.8"/>
    <rect x="216" y="140" width="12" height="4" fill="#1565C0" opacity="0.3"/>
    <rect x="216" y="146" width="12" height="4" fill="#1565C0" opacity="0.9"/>
    <rect x="216" y="152" width="12" height="4" fill="#1565C0" opacity="0.3"/>
    <rect x="216" y="158" width="12" height="4" fill="#1565C0" opacity="0.8"/>
    <rect x="216" y="164" width="12" height="4" fill="#1565C0" opacity="0.3"/>
    <rect x="216" y="170" width="12" height="4" fill="#1565C0" opacity="0.8"/>
    <!-- Diffraction -->
    <rect x="260" y="95" width="215" height="125" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Дифракционная решётка</text>
    <!-- Grating -->
    <rect x="280" y="125" width="8" height="75" fill="#555"/>
    <line x1="280" y1="130" x2="288" y2="130" stroke="#888" stroke-width="1"/>
    <line x1="280" y1="140" x2="288" y2="140" stroke="#888" stroke-width="1"/>
    <line x1="280" y1="150" x2="288" y2="150" stroke="#888" stroke-width="1"/>
    <line x1="280" y1="160" x2="288" y2="160" stroke="#888" stroke-width="1"/>
    <line x1="280" y1="170" x2="288" y2="170" stroke="#888" stroke-width="1"/>
    <line x1="280" y1="180" x2="288" y2="180" stroke="#888" stroke-width="1"/>
    <line x1="280" y1="190" x2="288" y2="190" stroke="#888" stroke-width="1"/>
    <!-- Diffraction pattern -->
    <rect x="430" y="120" width="5" height="80" fill="#333"/>
    <rect x="436" y="148" width="25" height="8" fill="#E53935" opacity="0.7"/>
    <rect x="436" y="140" width="15" height="5" fill="#FF9800" opacity="0.5"/>
    <rect x="436" y="158" width="15" height="5" fill="#FF9800" opacity="0.5"/>
    <rect x="436" y="133" width="8" height="4" fill="#4CAF50" opacity="0.4"/>
    <rect x="436" y="166" width="8" height="4" fill="#4CAF50" opacity="0.4"/>
    <text x="448" y="155" font-family="Arial,sans-serif" font-size="8" fill="#E53935">max</text>
    <text x="300" y="210" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">d·sin(φ) = kλ</text>
    <!-- Formulas -->
    <rect x="20" y="226" width="225" height="70" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="244" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Условие max интерференции:</text>
    <text x="30" y="262" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">Δd = kλ  (k = 0,1,2...)</text>
    <text x="30" y="280" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Условие min:</text>
    <text x="30" y="293" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">Δd = (2k+1)λ/2</text>
    <!-- Right box -->
    <rect x="255" y="226" width="225" height="70" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="265" y="244" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Дифракционная решётка:</text>
    <text x="265" y="262" font-family="Arial,sans-serif" font-size="12" fill="#1565C0">d·sin(φ) = kλ</text>
    <text x="265" y="280" font-family="Arial,sans-serif" font-size="10" fill="#444">d = 1/N — период решётки</text>
    <text x="265" y="293" font-family="Arial,sans-serif" font-size="10" fill="#444">N — число штрихов на 1 мм</text>
    """,
    },
    {
        "n": 7,
        "title": "Фотоэффект",
        "subject_header": "Физика — Урок 7",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- Photoelectric experiment -->
    <rect x="25" y="95" width="220" height="130" rx="5" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Фотоэффект</text>
    <!-- Vacuum tube -->
    <ellipse cx="135" cy="160" rx="60" ry="35" fill="none" stroke="#0D47A1" stroke-width="2"/>
    <!-- Cathode -->
    <rect x="80" y="148" width="8" height="25" fill="#1565C0"/>
    <text x="72" y="165" font-family="Arial,sans-serif" font-size="8" fill="#0D47A1">K</text>
    <!-- Anode -->
    <rect x="182" y="148" width="8" height="25" fill="#E53935"/>
    <text x="196" y="165" font-family="Arial,sans-serif" font-size="8" fill="#E53935">A</text>
    <!-- Incoming light (wavy arrows) -->
    <path d="M35,140 Q45,135 55,140 Q65,145 75,140" fill="none" stroke="#FF9800" stroke-width="2"/>
    <path d="M35,150 Q45,145 55,150 Q65,155 75,150" fill="none" stroke="#FF9800" stroke-width="2"/>
    <text x="55" y="135" font-family="Arial,sans-serif" font-size="9" fill="#FF9800">hν</text>
    <!-- Electrons flying -->
    <circle cx="100" cy="155" r="2" fill="#4CAF50"/>
    <line x1="102" y1="155" x2="115" y2="152" stroke="#4CAF50" stroke-width="1"/>
    <circle cx="115" cy="152" r="2" fill="#4CAF50"/>
    <line x1="117" y1="152" x2="130" y2="148" stroke="#4CAF50" stroke-width="1"/>
    <circle cx="130" cy="148" r="2" fill="#4CAF50"/>
    <text x="110" y="200" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50">e⁻</text>
    <!-- Graph: I vs U -->
    <rect x="260" y="95" width="215" height="130" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="367" y="108" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Вольт-амперная характеристика</text>
    <line x1="280" y1="200" x2="460" y2="200" stroke="#0D47A1" stroke-width="1"/>
    <line x1="280" y1="200" x2="280" y2="115" stroke="#0D47A1" stroke-width="1"/>
    <text x="465" y="203" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">U</text>
    <text x="274" y="113" font-family="Arial,sans-serif" font-size="9" fill="#0D47A1">I</text>
    <!-- Saturation curve -->
    <path d="M280,200 L295,175 L310,155 L330,142 L360,133 L400,128 L450,126" fill="none" stroke="#E53935" stroke-width="2"/>
    <text x="420" y="122" font-family="Arial,sans-serif" font-size="8" fill="#E53935">I_нас</text>
    <!-- Stopping voltage marker -->
    <line x1="270" y1="180" x2="280" y2="180" stroke="#4CAF50" stroke-width="1"/>
    <text x="255" y="183" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50">−U_з</text>
    <!-- Formulas -->
    <rect x="20" y="230" width="225" height="66" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Уравнение Эйнштейна:</text>
    <text x="30" y="268" font-family="Arial,sans-serif" font-size="14" fill="#1565C0">hν = A_вых + E_k</text>
    <text x="30" y="288" font-family="Arial,sans-serif" font-size="10" fill="#444">E_k = ½mv²_max = eU_з</text>
    <!-- Right box -->
    <rect x="255" y="230" width="225" height="66" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="265" y="248" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Красная граница:</text>
    <text x="265" y="268" font-family="Arial,sans-serif" font-size="13" fill="#1565C0">ν_min = A_вых/h</text>
    <text x="265" y="288" font-family="Arial,sans-serif" font-size="10" fill="#444">h = 6.63·10⁻³⁴ Дж·с</text>
    """,
    },
    {
        "n": 8,
        "title": "Строение атома",
        "subject_header": "Физика — Урок 8",
        "footer": "Физика · 11 класс",
        "primary": "#1565C0",
        "primary_dark": "#0D47A1",
        "bg": "#E3F2FD",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#E3F2FD" opacity="0.5"/>
    <!-- Bohr atom model -->
    <rect x="25" y="95" width="200" height="145" rx="5" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="125" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Модель Бора</text>
    <!-- Nucleus -->
    <circle cx="125" cy="165" r="10" fill="#E53935" opacity="0.8"/>
    <text x="125" y="168" font-family="Arial,sans-serif" font-size="7" fill="white" text-anchor="middle">Z+</text>
    <!-- Orbits -->
    <ellipse cx="125" cy="165" rx="35" ry="30" fill="none" stroke="#1565C0" stroke-width="1" stroke-dasharray="3,2"/>
    <ellipse cx="125" cy="165" rx="60" ry="50" fill="none" stroke="#4CAF50" stroke-width="1" stroke-dasharray="3,2"/>
    <ellipse cx="125" cy="165" rx="85" ry="65" fill="none" stroke="#FF9800" stroke-width="1" stroke-dasharray="3,2"/>
    <!-- Electrons on orbits -->
    <circle cx="160" cy="155" r="4" fill="#1565C0"/>
    <circle cx="65" cy="180" r="4" fill="#4CAF50"/>
    <circle cx="180" cy="140" r="4" fill="#FF9800"/>
    <!-- Energy levels -->
    <text x="60" y="135" font-family="Arial,sans-serif" font-size="8" fill="#FF9800">n=3</text>
    <text x="60" y="150" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50">n=2</text>
    <text x="85" y="160" font-family="Arial,sans-serif" font-size="8" fill="#1565C0">n=1</text>
    <!-- Transition arrows -->
    <line x1="155" y1="152" x2="125" y2="162" stroke="#E53935" stroke-width="1.5" marker-end="url(#arrowRed)"/>
    <text x="148" y="148" font-family="Arial,sans-serif" font-size="7" fill="#E53935">hν</text>
    <!-- Energy level diagram -->
    <rect x="240" y="95" width="240" height="145" rx="3" fill="white" opacity="0.7" stroke="#1565C0" stroke-width="1"/>
    <text x="360" y="110" font-family="Arial,sans-serif" font-size="10" fill="#0D47A1" text-anchor="middle" font-weight="bold">Энергетические уровни</text>
    <!-- Energy levels -->
    <line x1="280" y1="220" x2="380" y2="220" stroke="#1565C0" stroke-width="2"/>
    <text x="385" y="223" font-family="Arial,sans-serif" font-size="9" fill="#1565C0">n=1  E₁</text>
    <line x1="280" y1="185" x2="380" y2="185" stroke="#4CAF50" stroke-width="2"/>
    <text x="385" y="188" font-family="Arial,sans-serif" font-size="9" fill="#4CAF50">n=2  E₂</text>
    <line x1="280" y1="150" x2="380" y2="150" stroke="#FF9800" stroke-width="2"/>
    <text x="385" y="153" font-family="Arial,sans-serif" font-size="9" fill="#FF9800">n=3  E₃</text>
    <line x1="280" y1="120" x2="380" y2="120" stroke="#E53935" stroke-width="2"/>
    <text x="385" y="123" font-family="Arial,sans-serif" font-size="9" fill="#E53935">n=∞  E=0</text>
    <!-- Transition arrow -->
    <line x1="330" y1="185" x2="330" y2="220" stroke="#E53935" stroke-width="2" marker-end="url(#arrowRed)"/>
    <text x="335" y="205" font-family="Arial,sans-serif" font-size="8" fill="#E53935">hν₁₂</text>
    <line x1="340" y1="150" x2="340" y2="220" stroke="#4CAF50" stroke-width="1.5" marker-end="url(#arrowGreen)"/>
    <text x="345" y="195" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50">hν₁₃</text>
    <!-- Formulas -->
    <rect x="20" y="246" width="460" height="50" rx="5" fill="white" opacity="0.9" stroke="#1565C0" stroke-width="1"/>
    <text x="30" y="264" font-family="Arial,sans-serif" font-size="11" fill="#0D47A1" font-weight="bold">Постулаты Бора:</text>
    <text x="30" y="282" font-family="Arial,sans-serif" font-size="10" fill="#444">1) Стационарные орбиты: mvr = nħ;   2) Излучение при переходе: hν = E_n − E_k</text>
    <text x="30" y="293" font-family="Arial,sans-serif" font-size="10" fill="#1565C0">E_n = −13.6/n² эВ (водород)</text>
    """,
    },
]

# ── Algebra lesson data ───────────────────────────────────────────────────
algebra_lessons = [
    {
        "n": 1,
        "title": "Свойства тригонометрических функций",
        "subject_header": "Алгебра — Урок 1",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- Unit circle -->
    <rect x="25" y="95" width="170" height="170" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="110" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Тригонометрический круг</text>
    <circle cx="110" cy="185" r="55" fill="none" stroke="#6A1B9A" stroke-width="1.5"/>
    <line x1="45" y1="185" x2="175" y2="185" stroke="#888" stroke-width="0.5"/>
    <line x1="110" y1="120" x2="110" y2="250" stroke="#888" stroke-width="0.5"/>
    <!-- Angle arc -->
    <path d="M130,185 A20,20 0 0,0 125,168" fill="none" stroke="#E53935" stroke-width="1.5"/>
    <text x="133" y="172" font-family="Arial,sans-serif" font-size="9" fill="#E53935">α</text>
    <!-- Point on circle -->
    <circle cx="148" cy="155" r="3" fill="#E53935"/>
    <line x1="110" y1="185" x2="148" y2="155" stroke="#E53935" stroke-width="1.5"/>
    <!-- cos projection -->
    <line x1="148" y1="155" x2="148" y2="185" stroke="#4CAF50" stroke-width="1" stroke-dasharray="3,2"/>
    <line x1="110" y1="185" x2="148" y2="185" stroke="#4CAF50" stroke-width="2"/>
    <text x="130" y="198" font-family="Arial,sans-serif" font-size="9" fill="#4CAF50">cosα</text>
    <!-- sin projection -->
    <line x1="148" y1="155" x2="110" y2="155" stroke="#1565C0" stroke-width="2"/>
    <text x="95" y="158" font-family="Arial,sans-serif" font-size="9" fill="#1565C0">sinα</text>
    <!-- Properties box -->
    <rect x="210" y="95" width="270" height="105" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="220" y="113" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Основные свойства:</text>
    <text x="220" y="130" font-family="Arial,sans-serif" font-size="10" fill="#444">• sin²α + cos²α = 1</text>
    <text x="220" y="145" font-family="Arial,sans-serif" font-size="10" fill="#444">• tgα = sinα/cosα;  ctgα = cosα/sinα</text>
    <text x="220" y="160" font-family="Arial,sans-serif" font-size="10" fill="#444">• 1 + tg²α = 1/cos²α</text>
    <text x="220" y="175" font-family="Arial,sans-serif" font-size="10" fill="#444">• 1 + ctg²α = 1/sin²α</text>
    <text x="220" y="192" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">• Чётность: cos(−α)=cosα; sin(−α)=−sinα</text>
    <!-- Periodicity and signs -->
    <rect x="210" y="208" width="270" height="90" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="220" y="226" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Периодичность:</text>
    <text x="220" y="243" font-family="Arial,sans-serif" font-size="10" fill="#444">sin(x+2π) = sinx;  cos(x+2π) = cosx</text>
    <text x="220" y="258" font-family="Arial,sans-serif" font-size="10" fill="#444">tg(x+π) = tgx;  ctg(x+π) = ctgx</text>
    <text x="220" y="278" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Формулы приведения:</text>
    <text x="220" y="293" font-family="Arial,sans-serif" font-size="9" fill="#6A1B9A">Правило: « Horse rule » — знак и функция</text>
    <!-- Left bottom -->
    <rect x="25" y="272" width="170" height="26" rx="3" fill="white" opacity="0.8" stroke="#6A1B9A" stroke-width="1"/>
    <text x="110" y="289" font-family="Arial,sans-serif" font-size="9" fill="#4A148C" text-anchor="middle">Знаки по четвертям: + + / + − / − − / − +</text>
    """,
    },
    {
        "n": 2,
        "title": "Обратные тригонометрические функции",
        "subject_header": "Алгебра — Урок 2",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- arcsin graph -->
    <rect x="25" y="95" width="220" height="125" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">y = arcsin(x)</text>
    <line x1="50" y1="160" x2="220" y2="160" stroke="#888" stroke-width="0.5"/>
    <line x1="135" y1="210" x2="135" y2="115" stroke="#888" stroke-width="0.5"/>
    <!-- arcsin curve -->
    <path d="M55,195 Q80,180 100,170 Q120,160 135,150 Q150,140 170,128 Q190,118 215,118" fill="none" stroke="#6A1B9A" stroke-width="2"/>
    <!-- Domain/range markers -->
    <text x="55" y="208" font-family="Arial,sans-serif" font-size="8" fill="#E53935">−1</text>
    <text x="210" y="208" font-family="Arial,sans-serif" font-size="8" fill="#E53935">1</text>
    <text x="140" y="118" font-family="Arial,sans-serif" font-size="8" fill="#E53935">π/2</text>
    <text x="140" y="208" font-family="Arial,sans-serif" font-size="8" fill="#E53935">−π/2</text>
    <!-- arccos graph -->
    <rect x="260" y="95" width="215" height="125" rx="3" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">y = arccos(x)</text>
    <line x1="280" y1="160" x2="455" y2="160" stroke="#888" stroke-width="0.5"/>
    <line x1="367" y1="210" x2="367" y2="115" stroke="#888" stroke-width="0.5"/>
    <!-- arccos curve -->
    <path d="M285,125 Q310,130 330,140 Q350,150 367,160 Q385,170 405,180 Q425,190 450,200" fill="none" stroke="#E53935" stroke-width="2"/>
    <text x="280" y="208" font-family="Arial,sans-serif" font-size="8" fill="#4A148C">−1</text>
    <text x="445" y="208" font-family="Arial,sans-serif" font-size="8" fill="#4A148C">1</text>
    <!-- Formulas -->
    <rect x="20" y="226" width="225" height="70" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="30" y="244" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">arcsin:</text>
    <text x="30" y="261" font-family="Arial,sans-serif" font-size="10" fill="#444">D(arcsin) = [−1; 1]</text>
    <text x="30" y="276" font-family="Arial,sans-serif" font-size="10" fill="#444">E(arcsin) = [−π/2; π/2]</text>
    <text x="30" y="291" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">arcsin(−x) = −arcsin(x)</text>
    <!-- Right box -->
    <rect x="255" y="226" width="225" height="70" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="265" y="244" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">arccos / arctg / arcctg:</text>
    <text x="265" y="261" font-family="Arial,sans-serif" font-size="10" fill="#444">E(arccos) = [0; π]</text>
    <text x="265" y="276" font-family="Arial,sans-serif" font-size="10" fill="#444">E(arctg) = (−π/2; π/2)</text>
    <text x="265" y="291" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">arccos(−x) = π − arccos(x)</text>
    """,
    },
    {
        "n": 3,
        "title": "Первообразная и неопределённый интеграл",
        "subject_header": "Алгебра — Урок 3",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- Antiderivative illustration -->
    <rect x="25" y="95" width="220" height="130" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Первообразная F'(x) = f(x)</text>
    <!-- f(x) curve -->
    <line x1="35" y1="200" x2="235" y2="200" stroke="#888" stroke-width="0.5"/>
    <line x1="35" y1="200" x2="35" y2="115" stroke="#888" stroke-width="0.5"/>
    <path d="M40,180 Q70,140 100,155 Q130,170 160,135 Q190,100 225,130" fill="none" stroke="#6A1B9A" stroke-width="2"/>
    <text x="230" y="128" font-family="Arial,sans-serif" font-size="9" fill="#6A1B9A">f(x)</text>
    <!-- Tangent line at a point -->
    <line x1="90" y1="200" x2="130" y2="120" stroke="#E53935" stroke-width="1.5" stroke-dasharray="4,3"/>
    <circle cx="110" cy="150" r="3" fill="#E53935"/>
    <text x="132" y="118" font-family="Arial,sans-serif" font-size="8" fill="#E53935">F'(x₀)=f(x₀)</text>
    <!-- Table of basic integrals -->
    <rect x="260" y="95" width="215" height="130" rx="3" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Таблица интегралов</text>
    <text x="270" y="128" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ xⁿ dx = xⁿ⁺¹/(n+1) + C</text>
    <text x="270" y="143" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ 1/x dx = ln|x| + C</text>
    <text x="270" y="158" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ eˣ dx = eˣ + C</text>
    <text x="270" y="173" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ sin(x) dx = −cos(x) + C</text>
    <text x="270" y="188" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ cos(x) dx = sin(x) + C</text>
    <text x="270" y="203" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ 1/cos²x dx = tg(x) + C</text>
    <text x="270" y="218" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ aˣ dx = aˣ/ln(a) + C</text>
    <!-- Rules -->
    <rect x="20" y="230" width="460" height="66" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="30" y="248" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">Правила интегрирования:</text>
    <text x="30" y="266" font-family="Arial,sans-serif" font-size="10" fill="#444">∫ (f(x) ± g(x)) dx = ∫ f(x) dx ± ∫ g(x) dx</text>
    <text x="30" y="282" font-family="Arial,sans-serif" font-size="10" fill="#444">∫ k·f(x) dx = k·∫ f(x) dx</text>
    <text x="30" y="293" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">∫ f(kx+b) dx = 1/k · F(kx+b) + C</text>
    """,
    },
    {
        "n": 4,
        "title": "Определённый интеграл",
        "subject_header": "Алгебра — Урок 4",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- Area under curve -->
    <rect x="25" y="95" width="220" height="135" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Площадь криволинейной трапеции</text>
    <line x1="35" y1="205" x2="235" y2="205" stroke="#888" stroke-width="0.5"/>
    <line x1="35" y1="205" x2="35" y2="115" stroke="#888" stroke-width="0.5"/>
    <!-- f(x) curve -->
    <path d="M40,185 Q70,140 100,130 Q130,120 160,135 Q190,155 225,145" fill="none" stroke="#6A1B9A" stroke-width="2"/>
    <!-- Shaded area -->
    <path d="M70,205 L70,160 Q90,140 100,130 Q130,120 160,135 Q180,145 190,150 L190,205 Z" fill="#6A1B9A" opacity="0.2"/>
    <!-- a and b markers -->
    <line x1="70" y1="205" x2="70" y2="210" stroke="#E53935" stroke-width="1.5"/>
    <line x1="190" y1="205" x2="190" y2="210" stroke="#E53935" stroke-width="1.5"/>
    <text x="70" y="222" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle">a</text>
    <text x="190" y="222" font-family="Arial,sans-serif" font-size="10" fill="#E53935" text-anchor="middle">b</text>
    <text x="130" y="175" font-family="Arial,sans-serif" font-size="12" fill="#6A1B9A" text-anchor="middle">S</text>
    <!-- Newton-Leibniz -->
    <rect x="260" y="95" width="215" height="135" rx="3" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Формула Ньютона-Лейбница</text>
    <text x="367" y="140" font-family="Arial,sans-serif" font-size="16" fill="#6A1B9A" text-anchor="middle" font-weight="bold">∫ₐᵇ f(x)dx</text>
    <text x="367" y="160" font-family="Arial,sans-serif" font-size="14" fill="#E53935" text-anchor="middle">= F(b) − F(a)</text>
    <line x1="280" y1="170" x2="455" y2="170" stroke="#6A1B9A" stroke-width="0.5"/>
    <text x="367" y="188" font-family="Arial,sans-serif" font-size="9" fill="#4A148C" text-anchor="middle">Свойства:</text>
    <text x="270" y="203" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ₐᵇ f(x)dx = −∫ᵇₐ f(x)dx</text>
    <text x="270" y="218" font-family="Arial,sans-serif" font-size="9" fill="#444">∫ₐᵇ f(x)dx + ∫ᵇᶜ f(x)dx = ∫ₐᶜ f(x)dx</text>
    <!-- Applications -->
    <rect x="20" y="232" width="460" height="64" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="30" y="250" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">Применения:</text>
    <text x="30" y="267" font-family="Arial,sans-serif" font-size="10" fill="#444">Площадь: S = ∫ₐᵇ f(x)dx</text>
    <text x="220" y="267" font-family="Arial,sans-serif" font-size="10" fill="#444">Объём вращения: V = π∫ₐᵇ f²(x)dx</text>
    <text x="30" y="285" font-family="Arial,sans-serif" font-size="10" fill="#444">Путь: S = ∫₀ᵗ v(t)dt</text>
    <text x="220" y="285" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">Работа: A = ∫ₐᵇ F(x)dx</text>
    """,
    },
    {
        "n": 5,
        "title": "Иррациональные уравнения",
        "subject_header": "Алгебра — Урок 5",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- Root function graph -->
    <rect x="25" y="95" width="220" height="130" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">y = √(f(x))</text>
    <line x1="40" y1="195" x2="230" y2="195" stroke="#888" stroke-width="0.5"/>
    <line x1="40" y1="195" x2="40" y2="115" stroke="#888" stroke-width="0.5"/>
    <!-- sqrt curve -->
    <path d="M50,192 Q80,175 110,160 Q140,145 170,135 Q200,128 225,122" fill="none" stroke="#6A1B9A" stroke-width="2.5"/>
    <text x="228" y="118" font-family="Arial,sans-serif" font-size="9" fill="#6A1B9A">√x</text>
    <!-- Domain marker -->
    <line x1="40" y1="195" x2="50" y2="195" stroke="#E53935" stroke-width="2"/>
    <text x="40" y="208" font-family="Arial,sans-serif" font-size="8" fill="#E53935">0</text>
    <text x="35" y="112" font-family="Arial,sans-serif" font-size="9" fill="#4A148C">y</text>
    <text x="233" y="198" font-family="Arial,sans-serif" font-size="9" fill="#4A148C">x</text>
    <!-- Methods -->
    <rect x="260" y="95" width="215" height="130" rx="3" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Методы решения</text>
    <text x="270" y="130" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">1. Возведение в степень:</text>
    <text x="270" y="145" font-family="Arial,sans-serif" font-size="9" fill="#444">√(f(x)) = g(x) ⇒ f(x) = g²(x)</text>
    <text x="270" y="160" font-family="Arial,sans-serif" font-size="9" fill="#E53935">+ проверка! (ОДЗ: g(x) ≥ 0)</text>
    <text x="270" y="178" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">2. Замена переменной:</text>
    <text x="270" y="193" font-family="Arial,sans-serif" font-size="9" fill="#444">√x = t, t ≥ 0</text>
    <text x="270" y="211" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">3. Свойства корней:</text>
    <text x="270" y="226" font-family="Arial,sans-serif" font-size="9" fill="#444">√a·√b = √(ab); √a/√b = √(a/b)</text>
    <!-- Examples -->
    <rect x="20" y="230" width="460" height="66" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="30" y="248" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">Пример:</text>
    <text x="30" y="265" font-family="Arial,sans-serif" font-size="10" fill="#444">√(2x+1) = x − 1  ⇒  2x+1 = (x−1)²  ⇒  x²−4x = 0</text>
    <text x="30" y="280" font-family="Arial,sans-serif" font-size="10" fill="#444">x = 0 или x = 4. Проверка: x=0 → −1✗; x=4 → √9=3 ✓</text>
    <text x="30" y="293" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">Ответ: x = 4 (посторонний корень исключён)</text>
    """,
    },
    {
        "n": 6,
        "title": "Системы уравнений",
        "subject_header": "Алгебра — Урок 6",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- Graphical method -->
    <rect x="25" y="95" width="220" height="130" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Графический метод</text>
    <line x1="40" y1="200" x2="235" y2="200" stroke="#888" stroke-width="0.5"/>
    <line x1="40" y1="200" x2="40" y2="115" stroke="#888" stroke-width="0.5"/>
    <!-- Two curves -->
    <path d="M45,185 Q80,150 110,155 Q140,160 170,130 Q200,100 230,115" fill="none" stroke="#6A1B9A" stroke-width="2"/>
    <path d="M45,170 Q80,180 110,165 Q140,150 170,155 Q200,165 230,135" fill="none" stroke="#E53935" stroke-width="2"/>
    <!-- Intersection points -->
    <circle cx="80" cy="173" r="4" fill="#4CAF50" stroke="#4CAF50" stroke-width="1"/>
    <circle cx="155" cy="152" r="4" fill="#4CAF50" stroke="#4CAF50" stroke-width="1"/>
    <text x="82" y="168" font-family="Arial,sans-serif" font-size="8" fill="#4A148C">f(x)</text>
    <text x="82" y="185" font-family="Arial,sans-serif" font-size="8" fill="#E53935">g(x)</text>
    <text x="120" y="148" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50">решения</text>
    <!-- Methods -->
    <rect x="260" y="95" width="215" height="130" rx="3" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Методы решения</text>
    <text x="270" y="130" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">1. Подстановка:</text>
    <text x="270" y="145" font-family="Arial,sans-serif" font-size="9" fill="#444">y = f(x) → подставить в другое</text>
    <text x="270" y="162" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">2. Сложение:</text>
    <text x="270" y="177" font-family="Arial,sans-serif" font-size="9" fill="#444">Умножить и сложить уравнения</text>
    <text x="270" y="194" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">3. Замена:</text>
    <text x="270" y="209" font-family="Arial,sans-serif" font-size="9" fill="#444">Ввести новые переменные</text>
    <text x="270" y="226" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">4. Графический</text>
    <!-- Example -->
    <rect x="20" y="230" width="460" height="66" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="30" y="248" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">Пример (замена):</text>
    <text x="30" y="265" font-family="Arial,sans-serif" font-size="10" fill="#444">{ x+y = 5;  x²+y² = 13 }</text>
    <text x="30" y="280" font-family="Arial,sans-serif" font-size="10" fill="#444">y = 5−x → x²+(5−x)² = 13 → 2x²−10x+12 = 0 → x = 2 или x = 3</text>
    <text x="30" y="293" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">Ответ: (2;3), (3;2)</text>
    """,
    },
    {
        "n": 7,
        "title": "Неравенства с модулем",
        "subject_header": "Алгебра — Урок 7",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- Number line for |x| < a -->
    <rect x="25" y="95" width="220" height="80" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">|x| &lt; a  (a &gt; 0)</text>
    <line x1="40" y1="140" x2="230" y2="140" stroke="#4A148C" stroke-width="1.5"/>
    <!-- Interval -->
    <line x1="75" y1="140" x2="195" y2="140" stroke="#6A1B9A" stroke-width="4"/>
    <circle cx="75" cy="140" r="4" fill="white" stroke="#6A1B9A" stroke-width="2"/>
    <circle cx="195" cy="140" r="4" fill="white" stroke="#6A1B9A" stroke-width="2"/>
    <text x="75" y="158" font-family="Arial,sans-serif" font-size="9" fill="#4A148C" text-anchor="middle">−a</text>
    <text x="195" y="158" font-family="Arial,sans-serif" font-size="9" fill="#4A148C" text-anchor="middle">a</text>
    <text x="135" y="158" font-family="Arial,sans-serif" font-size="9" fill="#6A1B9A" text-anchor="middle">x ∈ (−a; a)</text>
    <!-- Number line for |x| > a -->
    <rect x="25" y="180" width="220" height="60" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="195" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">|x| &gt; a  (a &gt; 0)</text>
    <line x1="40" y1="215" x2="230" y2="215" stroke="#4A148C" stroke-width="1.5"/>
    <line x1="40" y1="215" x2="75" y2="215" stroke="#E53935" stroke-width="4"/>
    <line x1="195" y1="215" x2="230" y2="215" stroke="#E53935" stroke-width="4"/>
    <circle cx="75" cy="215" r="4" fill="#E53935" stroke="#E53935" stroke-width="2"/>
    <circle cx="195" cy="215" r="4" fill="#E53935" stroke="#E53935" stroke-width="2"/>
    <text x="75" y="230" font-family="Arial,sans-serif" font-size="9" fill="#4A148C" text-anchor="middle">−a</text>
    <text x="195" y="230" font-family="Arial,sans-serif" font-size="9" fill="#4A148C" text-anchor="middle">a</text>
    <text x="135" y="230" font-family="Arial,sans-serif" font-size="9" fill="#E53935" text-anchor="middle">x ∈ (−∞;−a)∪(a;+∞)</text>
    <!-- Rules -->
    <rect x="260" y="95" width="215" height="145" rx="3" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Свойства модуля</text>
    <text x="270" y="130" font-family="Arial,sans-serif" font-size="10" fill="#444">|a| ≥ 0</text>
    <text x="270" y="145" font-family="Arial,sans-serif" font-size="10" fill="#444">|a·b| = |a|·|b|</text>
    <text x="270" y="160" font-family="Arial,sans-serif" font-size="10" fill="#444">|a/b| = |a|/|b|</text>
    <text x="270" y="175" font-family="Arial,sans-serif" font-size="10" fill="#444">|a|² = a²</text>
    <text x="270" y="190" font-family="Arial,sans-serif" font-size="10" fill="#444">|a+b| ≤ |a|+|b|</text>
    <text x="270" y="208" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Методы:</text>
    <text x="270" y="223" font-family="Arial,sans-serif" font-size="9" fill="#444">1. По определению (2 случая)</text>
    <text x="270" y="236" font-family="Arial,sans-serif" font-size="9" fill="#444">2. Возведение в квадрат</text>
    <!-- Example -->
    <rect x="20" y="245" width="460" height="51" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="30" y="263" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">Пример: |2x−3| ≤ 5</text>
    <text x="30" y="279" font-family="Arial,sans-serif" font-size="10" fill="#444">−5 ≤ 2x−3 ≤ 5  →  −2 ≤ 2x ≤ 8  →  x ∈ [−1; 4]</text>
    <text x="30" y="292" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">Ответ: [−1; 4]</text>
    """,
    },
    {
        "n": 8,
        "title": "Комплексные числа и операции",
        "subject_header": "Алгебра — Урок 8",
        "footer": "Алгебра · 11 класс",
        "primary": "#6A1B9A",
        "primary_dark": "#4A148C",
        "bg": "#F3E5F5",
        "content": """
    <rect x="15" y="85" width="470" height="215" fill="#F3E5F5" opacity="0.5"/>
    <!-- Complex plane -->
    <rect x="25" y="95" width="220" height="145" rx="5" fill="white" opacity="0.7" stroke="#6A1B9A" stroke-width="1"/>
    <text x="135" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Комплексная плоскость</text>
    <line x1="35" y1="170" x2="235" y2="170" stroke="#888" stroke-width="0.5"/>
    <line x1="135" y1="230" x2="135" y2="115" stroke="#888" stroke-width="0.5"/>
    <text x="237" y="173" font-family="Arial,sans-serif" font-size="9" fill="#4A148C">Re</text>
    <text x="138" y="113" font-family="Arial,sans-serif" font-size="9" fill="#4A148C">Im</text>
    <!-- Point z = a + bi -->
    <circle cx="180" cy="135" r="4" fill="#6A1B9A"/>
    <line x1="135" y1="170" x2="180" y2="135" stroke="#6A1B9A" stroke-width="1.5"/>
    <!-- Projections -->
    <line x1="180" y1="135" x2="180" y2="170" stroke="#4A148C" stroke-width="1" stroke-dasharray="3,2"/>
    <line x1="180" y1="135" x2="135" y2="135" stroke="#4A148C" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="182" y="180" font-family="Arial,sans-serif" font-size="9" fill="#E53935">a</text>
    <text x="125" y="133" font-family="Arial,sans-serif" font-size="9" fill="#E53935">b</text>
    <!-- Angle -->
    <path d="M155,170 A20,20 0 0,0 152,158" fill="none" stroke="#4CAF50" stroke-width="1.5"/>
    <text x="148" y="162" font-family="Arial,sans-serif" font-size="8" fill="#4CAF50">φ</text>
    <text x="145" y="140" font-family="Arial,sans-serif" font-size="9" fill="#6A1B9A">|z|</text>
    <text x="183" y="132" font-family="Arial,sans-serif" font-size="9" fill="#6A1B9A">z=a+bi</text>
    <!-- Operations -->
    <rect x="260" y="95" width="215" height="145" rx="3" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="367" y="110" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" text-anchor="middle" font-weight="bold">Операции</text>
    <text x="270" y="130" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Сложение:</text>
    <text x="270" y="145" font-family="Arial,sans-serif" font-size="9" fill="#444">(a+bi) + (c+di) = (a+c)+(b+d)i</text>
    <text x="270" y="162" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Умножение:</text>
    <text x="270" y="177" font-family="Arial,sans-serif" font-size="9" fill="#444">(a+bi)(c+di) = (ac−bd)+(ad+bc)i</text>
    <text x="270" y="194" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Модуль:</text>
    <text x="270" y="209" font-family="Arial,sans-serif" font-size="9" fill="#444">|z| = √(a²+b²)</text>
    <text x="270" y="226" font-family="Arial,sans-serif" font-size="10" fill="#4A148C" font-weight="bold">Сопряжённое:</text>
    <text x="270" y="237" font-family="Arial,sans-serif" font-size="9" fill="#444">z̄ = a − bi</text>
    <!-- Forms -->
    <rect x="20" y="245" width="460" height="51" rx="5" fill="white" opacity="0.9" stroke="#6A1B9A" stroke-width="1"/>
    <text x="30" y="263" font-family="Arial,sans-serif" font-size="11" fill="#4A148C" font-weight="bold">Формы записи:</text>
    <text x="30" y="280" font-family="Arial,sans-serif" font-size="10" fill="#444">Алгебраическая: z = a+bi</text>
    <text x="200" y="280" font-family="Arial,sans-serif" font-size="10" fill="#444">Тригонометрическая: z = r(cosφ+i·sinφ)</text>
    <text x="30" y="293" font-family="Arial,sans-serif" font-size="10" fill="#6A1B9A">i² = −1;  Формула Муавра: zⁿ = rⁿ(cos(nφ)+i·sin(nφ))</text>
    """,
    },
]


# ── SVG builder ───────────────────────────────────────────────────────────

def escape_xml(text: str) -> str:
    """Replace XML-special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_svg(lesson: dict) -> str:
    n = lesson["n"]
    title = lesson["title"]
    hdr = lesson["subject_header"]
    footer = lesson["footer"]
    primary = lesson["primary"]
    primary_dark = lesson["primary_dark"]
    bg = lesson["bg"]
    content = lesson["content"]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{primary_dark}"/>
    </linearGradient>
    <marker id="arrowBlue" markerWidth="6" markerHeight="4" refX="6" refY="2" orient="auto">
      <polygon points="0,0 6,2 0,4" fill="{primary}"/>
    </marker>
    <marker id="arrowRed" markerWidth="6" markerHeight="4" refX="6" refY="2" orient="auto">
      <polygon points="0,0 6,2 0,4" fill="#E53935"/>
    </marker>
    <marker id="arrowGreen" markerWidth="6" markerHeight="4" refX="6" refY="2" orient="auto">
      <polygon points="0,0 6,2 0,4" fill="#4CAF50"/>
    </marker>
    <marker id="arrowDark" markerWidth="6" markerHeight="4" refX="6" refY="2" orient="auto">
      <polygon points="0,0 6,2 0,4" fill="#333"/>
    </marker>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{primary}" stroke-width="2.5"/>
  <text x="250" y="48" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="{primary}" text-anchor="middle">{escape_xml(title)}</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">{escape_xml(hdr)}</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="{primary}" stroke-width="2" opacity="0.25"/>
  <clipPath id="ill"><rect x="15" y="85" width="470" height="215" rx="6"/></clipPath>
  <g clip-path="url(#ill)">{content}
  </g>
  <rect x="12" y="305" width="476" height="32" rx="5" fill="url(#panel)"/>
  <text x="250" y="326" font-family="Arial,sans-serif" font-size="15" text-anchor="middle" fill="white" font-weight="bold">{escape_xml(footer)}</text>
</svg>'''
    return svg


# ── Generate ──────────────────────────────────────────────────────────────

errors = []
generated = []

for lesson in physics_lessons:
    svg = build_svg(lesson)
    path = os.path.join(PHYSICS_DIR, f"lesson{lesson['n']}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    # Validate as XML
    try:
        ET.fromstring(svg)
        generated.append(path)
    except ET.ParseError as e:
        errors.append(f"Physics lesson {lesson['n']}: {e}")

for lesson in algebra_lessons:
    svg = build_svg(lesson)
    path = os.path.join(ALGEBRA_DIR, f"lesson{lesson['n']}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    # Validate as XML
    try:
        ET.fromstring(svg)
        generated.append(path)
    except ET.ParseError as e:
        errors.append(f"Algebra lesson {lesson['n']}: {e}")

# ── Report ────────────────────────────────────────────────────────────────

print(f"Generated {len(generated)} SVG files.")
if errors:
    print("XML validation errors:")
    for e in errors:
        print(f"  ✗ {e}")
else:
    print("All SVGs passed XML validation ✓")

for p in generated:
    size = os.path.getsize(p)
    print(f"  {p}  ({size:,} bytes)")
