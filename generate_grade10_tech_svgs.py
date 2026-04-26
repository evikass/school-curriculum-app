#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 10 Technology (Технология) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade10/tech"

# Color scheme
PRIMARY = "#37474F"
BG = "#ECEFF1"
ACCENT = "#546E7A"
ACCENT2 = "#78909C"
LIGHT = "#B0BEC5"
WHITE = "#FFFFFF"
DARK = "#263238"
HIGHLIGHT = "#00897B"
HIGHLIGHT2 = "#26A69A"
HIGHLIGHT_LIGHT = "#E0F2F1"
BLUE = "#1565C0"
BLUE_LIGHT = "#E3F2FD"
ORANGE = "#E65100"
ORANGE_LIGHT = "#FFF3E0"

LESSONS = [
    {
        "num": 1,
        "title": "Продвинутая робототехника",
        "content": "advanced_robotics"
    },
    {
        "num": 2,
        "title": "Программирование роботов",
        "content": "robot_programming"
    },
    {
        "num": 3,
        "title": "Мехатроника",
        "content": "mechatronics"
    },
    {
        "num": 4,
        "title": "Проект «Умный дом»",
        "content": "smart_home"
    },
    {
        "num": 5,
        "title": "CAD-системы",
        "content": "cad_systems"
    },
    {
        "num": 6,
        "title": "Сложные модели",
        "content": "complex_models"
    },
    {
        "num": 7,
        "title": "Подготовка к печати",
        "content": "print_preparation"
    },
    {
        "num": 8,
        "title": "Проект «Функциональная модель»",
        "content": "functional_model"
    },
    {
        "num": 9,
        "title": "Управление проектами",
        "content": "project_management"
    },
    {
        "num": 10,
        "title": "Командная работа",
        "content": "teamwork"
    },
    {
        "num": 11,
        "title": "Презентация проекта",
        "content": "project_presentation"
    },
    {
        "num": 12,
        "title": "Итоговый проект",
        "content": "final_project"
    },
]


def svg_header():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350" width="500" height="350">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap');
      text {{ font-family: 'Inter', 'Segoe UI', Arial, sans-serif; }}
    </style>
  </defs>
  <!-- Background -->
  <rect width="500" height="350" rx="12" ry="12" fill="{BG}" stroke="{PRIMARY}" stroke-width="2.5"/>
'''


def svg_footer(lesson_num):
    return f'''
  <!-- Footer -->
  <rect x="1" y="322" width="498" height="27" rx="0" ry="0" fill="{PRIMARY}"/>
  <rect x="1" y="322" width="498" height="27" rx="0" ry="0" fill="{PRIMARY}" opacity="0.9"/>
  <text x="250" y="340" text-anchor="middle" fill="{WHITE}" font-size="11" font-weight="500">Технология · 10 класс</text>
</svg>'''


def header_bar(lesson_num, title):
    return f'''
  <!-- Header bar -->
  <rect x="1" y="1" width="498" height="48" rx="12" ry="12" fill="{PRIMARY}"/>
  <rect x="1" y="25" width="498" height="24" fill="{PRIMARY}"/>
  <text x="250" y="20" text-anchor="middle" fill="{WHITE}" font-size="13" font-weight="600">{title}</text>
  <text x="250" y="40" text-anchor="middle" fill="{LIGHT}" font-size="10" font-weight="400">Технология — Урок {lesson_num}</text>
'''


def generate_lesson1(data):
    """Продвинутая робототехника — Advanced Robotics"""
    return svg_header() + header_bar(1, data["title"]) + f'''
  <!-- Robot body illustration -->
  <rect x="30" y="60" width="200" height="120" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="130" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Компоненты робота</text>

  <!-- Sensor box -->
  <rect x="40" y="88" width="85" height="36" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="82" y="103" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="600">Датчики</text>
  <text x="82" y="118" text-anchor="middle" fill="{ACCENT}" font-size="7">УЗ, ИК, LiDAR</text>

  <!-- Actuator box -->
  <rect x="135" y="88" width="85" height="36" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="177" y="103" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="600">Приводы</text>
  <text x="177" y="118" text-anchor="middle" fill="{ACCENT}" font-size="7">Серво, шаговые</text>

  <!-- Controller box -->
  <rect x="40" y="132" width="180" height="36" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="130" y="147" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="600">Контроллер (Arduino / Raspberry Pi)</text>
  <text x="130" y="162" text-anchor="middle" fill="{ACCENT}" font-size="7">Обработка данных и управление</text>

  <!-- Connecting lines -->
  <line x1="82" y1="124" x2="82" y2="132" stroke="{ACCENT}" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="177" y1="124" x2="177" y2="132" stroke="{ACCENT}" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- Right side: Robot types -->
  <rect x="250" y="60" width="220" height="120" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="360" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Типы роботов</text>

  <rect x="260" y="88" width="100" height="28" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="310" y="106" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="500">Манипуляторы</text>

  <rect x="370" y="88" width="90" height="28" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="415" y="106" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="500">Колёсные</text>

  <rect x="260" y="124" width="100" height="28" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="310" y="142" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="500">Гуманоидные</text>

  <rect x="370" y="124" width="90" height="28" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="415" y="142" text-anchor="middle" fill="{ACCENT}" font-size="9" font-weight="500">Дроны</text>

  <!-- Bottom: Kinematics -->
  <rect x="30" y="192" width="440" height="120" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="212" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Кинематика роботов: степени свободы (DOF)</text>

  <!-- DOF diagram -->
  <line x1="60" y1="245" x2="440" y2="245" stroke="{ACCENT}" stroke-width="1.5"/>
  <polygon points="440,245 434,241 434,249" fill="{ACCENT}"/>

  <!-- DOF markers -->
  <circle cx="100" cy="245" r="8" fill="{HIGHLIGHT}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="100" y="248" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="700">1</text>
  <text x="100" y="268" text-anchor="middle" fill="{PRIMARY}" font-size="8">Поступ.</text>

  <circle cx="190" cy="245" r="8" fill="{HIGHLIGHT}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="190" y="248" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="700">2</text>
  <text x="190" y="268" text-anchor="middle" fill="{PRIMARY}" font-size="8">Вращ.</text>

  <circle cx="280" cy="245" r="8" fill="{HIGHLIGHT}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="280" y="248" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="700">3</text>
  <text x="280" y="268" text-anchor="middle" fill="{PRIMARY}" font-size="8">Наклон</text>

  <circle cx="370" cy="245" r="8" fill="{HIGHLIGHT2}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="370" y="248" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="700">6</text>
  <text x="370" y="268" text-anchor="middle" fill="{PRIMARY}" font-size="8">Полная</text>

  <text x="250" y="295" text-anchor="middle" fill="{ACCENT}" font-size="8">6 DOF = полный контроль позиции и ориентации в 3D-пространстве</text>

  <!-- Joint illustration -->
  <rect x="60" y="224" width="50" height="12" rx="2" fill="{ACCENT2}" opacity="0.5"/>
  <rect x="150" y="224" width="50" height="12" rx="2" fill="{ACCENT2}" opacity="0.5"/>
  <rect x="240" y="224" width="50" height="12" rx="2" fill="{ACCENT2}" opacity="0.5"/>
  <rect x="330" y="224" width="50" height="12" rx="2" fill="{ACCENT2}" opacity="0.5"/>
  <text x="85" y="233" text-anchor="middle" fill="{WHITE}" font-size="7">Звено 1</text>
  <text x="175" y="233" text-anchor="middle" fill="{WHITE}" font-size="7">Звено 2</text>
  <text x="265" y="233" text-anchor="middle" fill="{WHITE}" font-size="7">Звено 3</text>
  <text x="355" y="233" text-anchor="middle" fill="{WHITE}" font-size="7">Звено N</text>
''' + svg_footer(1)


def generate_lesson2(data):
    """Программирование роботов — Robot Programming"""
    return svg_header() + header_bar(2, data["title"]) + f'''
  <!-- Left: Programming flow -->
  <rect x="30" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Алгоритм управления</text>

  <!-- Flowchart -->
  <rect x="85" y="86" width="100" height="20" rx="10" fill="{HIGHLIGHT}" stroke="none"/>
  <text x="135" y="100" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="500">НАЧАЛО</text>

  <line x1="135" y1="106" x2="135" y2="114" stroke="{ACCENT}" stroke-width="1"/>
  <polygon points="135,118 131,112 139,112" fill="{ACCENT}"/>

  <rect x="70" y="118" width="130" height="20" rx="3" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="135" y="132" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="500">Считать датчики</text>

  <line x1="135" y1="138" x2="135" y2="146" stroke="{ACCENT}" stroke-width="1"/>
  <polygon points="135,150 131,144 139,144" fill="{ACCENT}"/>

  <polygon points="135,152 185,165 135,178 85,165" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="135" y="168" text-anchor="middle" fill="{ORANGE}" font-size="7" font-weight="600">Условие?</text>

  <line x1="85" y1="165" x2="55" y2="165" stroke="{ORANGE}" stroke-width="1"/>
  <text x="70" y="160" fill="{ORANGE}" font-size="7">Да</text>
  <rect x="38" y="158" width="30" height="16" rx="3" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="53" y="170" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7">Дейст.1</text>

  <line x1="185" y1="165" x2="215" y2="165" stroke="{ORANGE}" stroke-width="1"/>
  <text x="200" y="160" fill="{ORANGE}" font-size="7">Нет</text>
  <rect x="198" y="158" width="30" height="16" rx="3" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="213" y="170" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7">Дейст.2</text>

  <!-- Right: Languages -->
  <rect x="260" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Языки программирования</text>

  <rect x="270" y="88" width="95" height="32" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="317" y="102" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="600">C / C++</text>
  <text x="317" y="114" text-anchor="middle" fill="{ACCENT}" font-size="7">Arduino, ROS</text>

  <rect x="375" y="88" width="85" height="32" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="417" y="102" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="600">Python</text>
  <text x="417" y="114" text-anchor="middle" fill="{ACCENT}" font-size="7">Raspberry Pi</text>

  <rect x="270" y="128" width="95" height="32" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="317" y="142" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="600">Scratch</text>
  <text x="317" y="154" text-anchor="middle" fill="{ACCENT}" font-size="7">Визуальное прогр.</text>

  <rect x="375" y="128" width="85" height="32" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="417" y="142" text-anchor="middle" fill="{ACCENT}" font-size="9" font-weight="600">ROS2</text>
  <text x="417" y="154" text-anchor="middle" fill="{ACCENT}" font-size="7">Фреймворк</text>

  <!-- Bottom: PID Control -->
  <rect x="30" y="217" width="440" height="95" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="236" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">ПИД-регулятор (PID Controller)</text>

  <!-- PID diagram -->
  <rect x="50" y="250" width="60" height="24" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="80" y="266" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="500">Цель</text>

  <text x="122" y="266" text-anchor="middle" fill="{ORANGE}" font-size="12">→</text>

  <rect x="135" y="250" width="60" height="24" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="165" y="266" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="500">Ошибка</text>

  <text x="207" y="266" text-anchor="middle" fill="{HIGHLIGHT}" font-size="12">→</text>

  <rect x="220" y="245" width="110" height="34" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1.5"/>
  <text x="275" y="259" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="600">ПИД-регулятор</text>
  <text x="275" y="273" text-anchor="middle" fill="{ACCENT}" font-size="7">P + I + D</text>

  <text x="342" y="266" text-anchor="middle" fill="{HIGHLIGHT}" font-size="12">→</text>

  <rect x="355" y="250" width="60" height="24" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="385" y="266" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="500">Робот</text>

  <text x="250" y="300" text-anchor="middle" fill="{ACCENT}" font-size="8">P — пропорциональный · I — интегральный · D — дифференциальный</text>
''' + svg_footer(2)


def generate_lesson3(data):
    """Мехатроника — Mechatronics"""
    return svg_header() + header_bar(3, data["title"]) + f'''
  <!-- Central Venn-like diagram: Mechatronics = Mechanical + Electronics + Software -->
  <rect x="30" y="60" width="440" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Мехатроника = Механика + Электроника + ПО</text>

  <!-- Three overlapping circles conceptually -->
  <circle cx="160" cy="135" r="42" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1.5" opacity="0.7"/>
  <text x="145" y="128" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="600">Механика</text>
  <text x="145" y="142" text-anchor="middle" fill="{BLUE}" font-size="7">Шестерни</text>
  <text x="145" y="153" text-anchor="middle" fill="{BLUE}" font-size="7">Рычаги</text>

  <circle cx="250" cy="135" r="42" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1.5" opacity="0.7"/>
  <text x="250" y="125" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="700">Мехатроника</text>
  <text x="250" y="140" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7">Интеграция</text>
  <text x="250" y="152" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7">систем</text>

  <circle cx="340" cy="135" r="42" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1.5" opacity="0.7"/>
  <text x="355" y="128" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="600">Электроника</text>
  <text x="355" y="142" text-anchor="middle" fill="{ORANGE}" font-size="7">Микросхемы</text>
  <text x="355" y="153" text-anchor="middle" fill="{ORANGE}" font-size="7">Датчики</text>

  <!-- Software label -->
  <rect x="210" y="168" width="80" height="22" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="250" y="183" text-anchor="middle" fill="{ACCENT}" font-size="8" font-weight="600">+ ПО</text>

  <!-- Bottom: Key components -->
  <rect x="30" y="217" width="210" height="95" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="235" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Основные компоненты</text>

  <rect x="42" y="244" width="92" height="24" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="88" y="260" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="500">Микроконтроллер</text>

  <rect x="142" y="244" width="86" height="24" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="185" y="260" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="500">Актюаторы</text>

  <rect x="42" y="276" width="92" height="24" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="88" y="292" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="500">ШИМ-контроль</text>

  <rect x="142" y="276" width="86" height="24" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="185" y="292" text-anchor="middle" fill="{ACCENT}" font-size="8" font-weight="500">АЦП / ЦАП</text>

  <!-- Right bottom: Applications -->
  <rect x="260" y="217" width="210" height="95" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="235" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Применение мехатроники</text>

  <text x="275" y="254" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="288" y="254" fill="{ACCENT}" font-size="8">Промышленные роботы</text>
  <text x="275" y="268" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="288" y="268" fill="{ACCENT}" font-size="8">CNC-станки</text>
  <text x="275" y="282" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="288" y="282" fill="{ACCENT}" font-size="8">Автомобильные системы</text>
  <text x="275" y="296" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="288" y="296" fill="{ACCENT}" font-size="8">Медицинское оборудование</text>
''' + svg_footer(3)


def generate_lesson4(data):
    """Проект «Умный дом» — Smart Home Project"""
    return svg_header() + header_bar(4, data["title"]) + f'''
  <!-- House outline -->
  <rect x="30" y="60" width="220" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="140" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Архитектура умного дома</text>

  <!-- House shape -->
  <polygon points="140,88 70,130 210,130" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1.5"/>
  <rect x="85" y="130" width="110" height="60" fill="{BG}" stroke="{HIGHLIGHT}" stroke-width="1.5"/>

  <!-- Smart devices in house -->
  <rect x="95" y="138" width="40" height="18" rx="3" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="115" y="150" text-anchor="middle" fill="{BLUE}" font-size="6" font-weight="600">💡 Свет</text>

  <rect x="145" y="138" width="40" height="18" rx="3" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="165" y="150" text-anchor="middle" fill="{ORANGE}" font-size="6" font-weight="600">🌡 Терм</text>

  <rect x="95" y="164" width="40" height="18" rx="3" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="115" y="176" text-anchor="middle" fill="{HIGHLIGHT}" font-size="6" font-weight="600">🔒 Замок</text>

  <rect x="145" y="164" width="40" height="18" rx="3" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="165" y="176" text-anchor="middle" fill="{ACCENT}" font-size="6" font-weight="600">📹 Камера</text>

  <!-- Right: IoT Protocols -->
  <rect x="270" y="60" width="200" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="370" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">IoT протоколы</text>

  <rect x="280" y="88" width="85" height="28" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="322" y="102" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="600">Wi-Fi</text>
  <text x="322" y="112" text-anchor="middle" fill="{ACCENT}" font-size="7">802.11 b/g/n</text>

  <rect x="375" y="88" width="85" height="28" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="417" y="102" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="600">ZigBee</text>
  <text x="417" y="112" text-anchor="middle" fill="{ACCENT}" font-size="7">Mesh-сеть</text>

  <rect x="280" y="124" width="85" height="28" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="322" y="138" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="600">Bluetooth</text>
  <text x="322" y="148" text-anchor="middle" fill="{ACCENT}" font-size="7">BLE 5.0</text>

  <rect x="375" y="124" width="85" height="28" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="417" y="138" text-anchor="middle" fill="{ACCENT}" font-size="9" font-weight="600">MQTT</text>
  <text x="417" y="148" text-anchor="middle" fill="{ACCENT}" font-size="7">Pub/Sub</text>

  <!-- Hub -->
  <rect x="300" y="162" width="140" height="24" rx="4" fill="{PRIMARY}"/>
  <text x="370" y="178" text-anchor="middle" fill="{WHITE}" font-size="9" font-weight="600">Центральный хаб</text>

  <!-- Bottom: Automation rules -->
  <rect x="30" y="217" width="440" height="95" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="236" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Пример автоматизации: ЕСЛИ — ТО</text>

  <!-- Rule 1 -->
  <rect x="45" y="248" width="130" height="50" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="110" y="264" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="600">ЕСЛИ</text>
  <text x="110" y="278" text-anchor="middle" fill="{ACCENT}" font-size="7">Температура &gt; 25°C</text>
  <text x="110" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">Датчик движения = ВКЛ</text>

  <text x="186" y="276" text-anchor="middle" fill="{HIGHLIGHT}" font-size="14">→</text>

  <!-- Rule 2 -->
  <rect x="200" y="248" width="130" height="50" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="265" y="264" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="600">ТО</text>
  <text x="265" y="278" text-anchor="middle" fill="{ACCENT}" font-size="7">Включить кондиционер</text>
  <text x="265" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">Включить вентилятор</text>

  <!-- Security note -->
  <rect x="350" y="248" width="108" height="50" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="404" y="264" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="600">Безопасность</text>
  <text x="404" y="278" text-anchor="middle" fill="{ACCENT}" font-size="7">Шифрование TLS</text>
  <text x="404" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">Аутентификация</text>
''' + svg_footer(4)


def generate_lesson5(data):
    """CAD-системы — CAD Systems"""
    return svg_header() + header_bar(5, data["title"]) + f'''
  <!-- Left: CAD software comparison -->
  <rect x="30" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">CAD-системы</text>

  <rect x="42" y="88" width="92" height="28" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="88" y="102" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="600">FreeCAD</text>
  <text x="88" y="112" text-anchor="middle" fill="{ACCENT}" font-size="7">Open Source</text>

  <rect x="142" y="88" width="86" height="28" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="185" y="102" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="600">Tinkercad</text>
  <text x="185" y="112" text-anchor="middle" fill="{ACCENT}" font-size="7">Web-браузер</text>

  <rect x="42" y="124" width="92" height="28" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="88" y="138" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="600">Fusion 360</text>
  <text x="88" y="148" text-anchor="middle" fill="{ACCENT}" font-size="7">Облачный CAD</text>

  <rect x="142" y="124" width="86" height="28" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="185" y="138" text-anchor="middle" fill="{ACCENT}" font-size="9" font-weight="600">SolidWorks</text>
  <text x="185" y="148" text-anchor="middle" fill="{ACCENT}" font-size="7">Профессионал</text>

  <!-- Modeling types -->
  <rect x="42" y="160" width="186" height="30" rx="4" fill="{PRIMARY}" opacity="0.1" stroke="{PRIMARY}" stroke-width="1"/>
  <text x="135" y="175" text-anchor="middle" fill="{PRIMARY}" font-size="8" font-weight="500">Параметрическое моделирование</text>
  <text x="135" y="185" text-anchor="middle" fill="{ACCENT}" font-size="7">Размер → Форма → Изменение</text>

  <!-- Right: CAD workflow -->
  <rect x="260" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Рабочий процесс CAD</text>

  <!-- Step boxes -->
  <rect x="275" y="90" width="180" height="22" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="285" y="105" fill="{BLUE}" font-size="9" font-weight="600">1.</text>
  <text x="300" y="105" fill="{BLUE}" font-size="8">Эскиз (2D-контур)</text>

  <line x1="365" y1="112" x2="365" y2="118" stroke="{ACCENT}" stroke-width="1"/>
  <polygon points="365,122 361,116 369,116" fill="{ACCENT}"/>

  <rect x="275" y="122" width="180" height="22" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="285" y="137" fill="{ORANGE}" font-size="9" font-weight="600">2.</text>
  <text x="300" y="137" fill="{ORANGE}" font-size="8">Выдавливание / Вращение</text>

  <line x1="365" y1="144" x2="365" y2="150" stroke="{ACCENT}" stroke-width="1"/>
  <polygon points="365,154 361,148 369,148" fill="{ACCENT}"/>

  <rect x="275" y="154" width="180" height="22" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="285" y="169" fill="{HIGHLIGHT}" font-size="9" font-weight="600">3.</text>
  <text x="300" y="169" fill="{HIGHLIGHT}" font-size="8">Операции (фаски, скругления)</text>

  <line x1="365" y1="176" x2="365" y2="182" stroke="{ACCENT}" stroke-width="1"/>
  <polygon points="365,186 361,180 369,180" fill="{ACCENT}"/>

  <rect x="275" y="186" width="180" height="12" rx="3" fill="{PRIMARY}"/>
  <text x="365" y="195" text-anchor="middle" fill="{WHITE}" font-size="7">4. Экспорт STL / OBJ</text>

  <!-- Bottom: File formats -->
  <rect x="30" y="217" width="440" height="95" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="236" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Форматы файлов 3D-моделей</text>

  <rect x="45" y="248" width="80" height="50" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="85" y="266" text-anchor="middle" fill="{BLUE}" font-size="10" font-weight="700">.STL</text>
  <text x="85" y="280" text-anchor="middle" fill="{ACCENT}" font-size="7">Треугольная</text>
  <text x="85" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">сетка</text>

  <rect x="140" y="248" width="80" height="50" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="180" y="266" text-anchor="middle" fill="{ORANGE}" font-size="10" font-weight="700">.OBJ</text>
  <text x="180" y="280" text-anchor="middle" fill="{ACCENT}" font-size="7">Вершины +</text>
  <text x="180" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">текстуры</text>

  <rect x="235" y="248" width="80" height="50" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="275" y="266" text-anchor="middle" fill="{HIGHLIGHT}" font-size="10" font-weight="700">.STEP</text>
  <text x="275" y="280" text-anchor="middle" fill="{ACCENT}" font-size="7">Точные</text>
  <text x="275" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">поверхности</text>

  <rect x="330" y="248" width="80" height="50" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="370" y="266" text-anchor="middle" fill="{ACCENT}" font-size="10" font-weight="700">.3MF</text>
  <text x="370" y="280" text-anchor="middle" fill="{ACCENT}" font-size="7">Современный</text>
  <text x="370" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">формат</text>

  <text x="250" y="308" text-anchor="middle" fill="{ACCENT}" font-size="8">STL — стандарт для 3D-печати · STEP — для обмена между CAD</text>
''' + svg_footer(5)


def generate_lesson6(data):
    """Сложные модели — Complex Models"""
    return svg_header() + header_bar(6, data["title"]) + f'''
  <!-- Left: Modeling techniques -->
  <rect x="30" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Методы моделирования</text>

  <rect x="42" y="88" width="92" height="36" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="88" y="103" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="600">Твердотельное</text>
  <text x="88" y="116" text-anchor="middle" fill="{ACCENT}" font-size="7">CSG-операции</text>

  <rect x="142" y="88" width="86" height="36" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="185" y="103" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="600">Поверхностное</text>
  <text x="185" y="116" text-anchor="middle" fill="{ACCENT}" font-size="7">NURBS-кривые</text>

  <rect x="42" y="132" width="92" height="36" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="88" y="147" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="600">Каркасное</text>
  <text x="88" y="160" text-anchor="middle" fill="{ACCENT}" font-size="7">Рёбра + вершины</text>

  <rect x="142" y="132" width="86" height="36" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="185" y="147" text-anchor="middle" fill="{ACCENT}" font-size="9" font-weight="600">Сборка</text>
  <text x="185" y="160" text-anchor="middle" fill="{ACCENT}" font-size="7">Компоненты</text>

  <!-- CSG Operations -->
  <rect x="42" y="176" width="186" height="20" rx="3" fill="{PRIMARY}" opacity="0.08"/>
  <text x="135" y="190" text-anchor="middle" fill="{PRIMARY}" font-size="8">CSG: ∪ объединение · ∩ пересечение · − разность</text>

  <!-- Right: Boolean operations illustration -->
  <rect x="260" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Булевы операции</text>

  <!-- Union -->
  <circle cx="295" cy="105" r="18" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1.5" opacity="0.7"/>
  <circle cx="315" cy="105" r="18" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1.5" opacity="0.5"/>
  <text x="305" y="135" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="600">∪ Объед.</text>

  <!-- Intersection -->
  <circle cx="380" cy="105" r="18" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1.5" opacity="0.5"/>
  <circle cx="400" cy="105" r="18" fill="{ORANGE}" stroke="{ORANGE}" stroke-width="1.5" opacity="0.5"/>
  <text x="390" y="135" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="600">∩ Пересеч.</text>

  <!-- Difference -->
  <circle cx="305" cy="170" r="18" fill="{HIGHLIGHT}" stroke="{HIGHLIGHT}" stroke-width="1.5" opacity="0.7"/>
  <circle cx="318" cy="170" r="14" fill="{WHITE}" stroke="{HIGHLIGHT}" stroke-width="1.5"/>
  <text x="305" y="198" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="600">− Разность</text>

  <!-- Bottom: Parametric design -->
  <rect x="30" y="217" width="440" height="95" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="236" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Параметрическое проектирование</text>

  <!-- Parametric chain -->
  <rect x="45" y="248" width="90" height="50" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="90" y="266" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="600">Параметры</text>
  <text x="90" y="280" text-anchor="middle" fill="{ACCENT}" font-size="7">Длина = 50</text>
  <text x="90" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">Ширина = 30</text>

  <text x="146" y="276" text-anchor="middle" fill="{HIGHLIGHT}" font-size="14">→</text>

  <rect x="160" y="248" width="90" height="50" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="205" y="266" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="600">Ограничения</text>
  <text x="205" y="280" text-anchor="middle" fill="{ACCENT}" font-size="7">Параллельность</text>
  <text x="205" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">Симметрия</text>

  <text x="261" y="276" text-anchor="middle" fill="{HIGHLIGHT}" font-size="14">→</text>

  <rect x="275" y="248" width="90" height="50" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="320" y="266" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="600">Операции</text>
  <text x="320" y="280" text-anchor="middle" fill="{ACCENT}" font-size="7">Выдавливание</text>
  <text x="320" y="290" text-anchor="middle" fill="{ACCENT}" font-size="7">Вращение</text>

  <text x="376" y="276" text-anchor="middle" fill="{HIGHLIGHT}" font-size="14">→</text>

  <rect x="390" y="248" width="68" height="50" rx="4" fill="{PRIMARY}"/>
  <text x="424" y="270" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="600">Модель</text>
  <text x="424" y="284" text-anchor="middle" fill="{LIGHT}" font-size="7">3D объект</text>
''' + svg_footer(6)


def generate_lesson7(data):
    """Подготовка к печати — Print Preparation"""
    return svg_header() + header_bar(7, data["title"]) + f'''
  <!-- Left: Slicer workflow -->
  <rect x="30" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Слайсер: STL → G-код</text>

  <!-- Step 1 -->
  <rect x="42" y="90" width="186" height="22" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="52" y="105" fill="{BLUE}" font-size="9" font-weight="600">1.</text>
  <text x="67" y="105" fill="{BLUE}" font-size="8">Импорт STL-файла</text>

  <line x1="135" y1="112" x2="135" y2="118" stroke="{ACCENT}" stroke-width="1"/>

  <!-- Step 2 -->
  <rect x="42" y="118" width="186" height="22" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="52" y="133" fill="{ORANGE}" font-size="9" font-weight="600">2.</text>
  <text x="67" y="133" fill="{ORANGE}" font-size="8">Настройка параметров печати</text>

  <line x1="135" y1="140" x2="135" y2="146" stroke="{ACCENT}" stroke-width="1"/>

  <!-- Step 3 -->
  <rect x="42" y="146" width="186" height="22" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="52" y="161" fill="{HIGHLIGHT}" font-size="9" font-weight="600">3.</text>
  <text x="67" y="161" fill="{HIGHLIGHT}" font-size="8">Нарезка на слои (срезы)</text>

  <line x1="135" y1="168" x2="135" y2="174" stroke="{ACCENT}" stroke-width="1"/>

  <!-- Step 4 -->
  <rect x="42" y="174" width="186" height="22" rx="4" fill="{PRIMARY}" opacity="0.12" stroke="{PRIMARY}" stroke-width="1"/>
  <text x="52" y="189" fill="{PRIMARY}" font-size="9" font-weight="600">4.</text>
  <text x="67" y="189" fill="{PRIMARY}" font-size="8">Генерация G-кода</text>

  <!-- Right: Print parameters -->
  <rect x="260" y="60" width="210" height="145" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Параметры печати</text>

  <text x="275" y="98" fill="{BLUE}" font-size="8" font-weight="600">Высота слоя:</text>
  <text x="455" y="98" text-anchor="end" fill="{ACCENT}" font-size="8">0.1 — 0.3 мм</text>

  <line x1="275" y1="105" x2="455" y2="105" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="118" fill="{ORANGE}" font-size="8" font-weight="600">Заполнение:</text>
  <text x="455" y="118" text-anchor="end" fill="{ACCENT}" font-size="8">15% — 100%</text>

  <line x1="275" y1="125" x2="455" y2="125" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="138" fill="{HIGHLIGHT}" font-size="8" font-weight="600">Температура:</text>
  <text x="455" y="138" text-anchor="end" fill="{ACCENT}" font-size="8">190 — 220 °C</text>

  <line x1="275" y1="145" x2="455" y2="145" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="158" fill="{PRIMARY}" font-size="8" font-weight="600">Скорость:</text>
  <text x="455" y="158" text-anchor="end" fill="{ACCENT}" font-size="8">40 — 80 мм/с</text>

  <line x1="275" y1="165" x2="455" y2="165" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="178" fill="{ACCENT2}" font-size="8" font-weight="600">Поддержки:</text>
  <text x="455" y="178" text-anchor="end" fill="{ACCENT}" font-size="8">Авто / Вручную</text>

  <line x1="275" y1="185" x2="455" y2="185" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="198" fill="{ACCENT2}" font-size="8" font-weight="600">Рафт / Брим:</text>
  <text x="455" y="198" text-anchor="end" fill="{ACCENT}" font-size="8">Адгезия к столу</text>

  <!-- Bottom: Infill patterns -->
  <rect x="30" y="217" width="440" height="95" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="236" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Типы заполнения (Infill)</text>

  <!-- Pattern boxes -->
  <rect x="45" y="248" width="78" height="52" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <!-- Grid pattern lines -->
  <line x1="55" y1="258" x2="113" y2="258" stroke="{BLUE}" stroke-width="0.7"/>
  <line x1="55" y1="268" x2="113" y2="268" stroke="{BLUE}" stroke-width="0.7"/>
  <line x1="55" y1="278" x2="113" y2="278" stroke="{BLUE}" stroke-width="0.7"/>
  <line x1="65" y1="253" x2="65" y2="290" stroke="{BLUE}" stroke-width="0.7"/>
  <line x1="80" y1="253" x2="80" y2="290" stroke="{BLUE}" stroke-width="0.7"/>
  <line x1="95" y1="253" x2="95" y2="290" stroke="{BLUE}" stroke-width="0.7"/>
  <text x="84" y="302" text-anchor="middle" fill="{BLUE}" font-size="7" font-weight="500">Сетка</text>

  <rect x="140" y="248" width="78" height="52" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <!-- Honeycomb pattern -->
  <line x1="155" y1="265" x2="165" y2="255" stroke="{ORANGE}" stroke-width="0.7"/>
  <line x1="165" y1="255" x2="185" y2="255" stroke="{ORANGE}" stroke-width="0.7"/>
  <line x1="185" y1="255" x2="195" y2="265" stroke="{ORANGE}" stroke-width="0.7"/>
  <line x1="195" y1="265" x2="185" y2="275" stroke="{ORANGE}" stroke-width="0.7"/>
  <line x1="185" y1="275" x2="165" y2="275" stroke="{ORANGE}" stroke-width="0.7"/>
  <line x1="165" y1="275" x2="155" y2="265" stroke="{ORANGE}" stroke-width="0.7"/>
  <text x="179" y="302" text-anchor="middle" fill="{ORANGE}" font-size="7" font-weight="500">Соты</text>

  <rect x="235" y="248" width="78" height="52" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <!-- Triangle pattern -->
  <polygon points="260,275 280,258 300,275" fill="none" stroke="{HIGHLIGHT}" stroke-width="0.7"/>
  <polygon points="270,285 290,268 300,280" fill="none" stroke="{HIGHLIGHT}" stroke-width="0.7"/>
  <text x="274" y="302" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7" font-weight="500">Треугольники</text>

  <rect x="330" y="248" width="78" height="52" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <!-- Gyroid lines -->
  <path d="M345,270 Q360,255 375,270 Q390,285 405,270" fill="none" stroke="{ACCENT}" stroke-width="1"/>
  <path d="M345,280 Q360,265 375,280 Q390,295 405,280" fill="none" stroke="{ACCENT}" stroke-width="0.7"/>
  <text x="369" y="302" text-anchor="middle" fill="{ACCENT}" font-size="7" font-weight="500">Гироид</text>
''' + svg_footer(7)


def generate_lesson8(data):
    """Проект «Функциональная модель» — Functional Model Project"""
    return svg_header() + header_bar(8, data["title"]) + f'''
  <!-- Top: Design Process -->
  <rect x="30" y="60" width="440" height="55" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Процесс создания функциональной модели</text>

  <rect x="42" y="88" width="80" height="20" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="82" y="102" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="500">Идея</text>

  <text x="130" y="102" fill="{ACCENT}" font-size="10">→</text>

  <rect x="140" y="88" width="80" height="20" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="180" y="102" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="500">Чертёж</text>

  <text x="228" y="102" fill="{ACCENT}" font-size="10">→</text>

  <rect x="238" y="88" width="80" height="20" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="278" y="102" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="500">3D-модель</text>

  <text x="326" y="102" fill="{ACCENT}" font-size="10">→</text>

  <rect x="336" y="88" width="80" height="20" rx="4" fill="{PRIMARY}" opacity="0.12" stroke="{PRIMARY}" stroke-width="1"/>
  <text x="376" y="102" text-anchor="middle" fill="{PRIMARY}" font-size="8" font-weight="500">Печать</text>

  <text x="424" y="102" fill="{ACCENT}" font-size="10">→</text>

  <rect x="434" y="88" width="26" height="20" rx="4" fill="{HIGHLIGHT}"/>
  <text x="447" y="102" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="700">✓</text>

  <!-- Left: Mechanical parts -->
  <rect x="30" y="127" width="210" height="105" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="145" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Механические детали</text>

  <rect x="42" y="154" width="92" height="30" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="88" y="168" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="500">Шестерни</text>
  <text x="88" y="179" text-anchor="middle" fill="{ACCENT}" font-size="7">Передача</text>

  <rect x="142" y="154" width="86" height="30" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="185" y="168" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="500">Оси / Валы</text>
  <text x="185" y="179" text-anchor="middle" fill="{ACCENT}" font-size="7">Вращение</text>

  <rect x="42" y="192" width="92" height="30" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="88" y="206" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="500">Корпус</text>
  <text x="88" y="217" text-anchor="middle" fill="{ACCENT}" font-size="7">Каркас</text>

  <rect x="142" y="192" width="86" height="30" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="185" y="206" text-anchor="middle" fill="{ACCENT}" font-size="8" font-weight="500">Крепёж</text>
  <text x="185" y="217" text-anchor="middle" fill="{ACCENT}" font-size="7">Болты, гайки</text>

  <!-- Right: Tolerances -->
  <rect x="260" y="127" width="210" height="105" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="145" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Допуски и посадки</text>

  <text x="275" y="164" fill="{BLUE}" font-size="8" font-weight="600">Зазор для оси:</text>
  <text x="455" y="164" text-anchor="end" fill="{ACCENT}" font-size="8">+0.2 мм</text>

  <line x1="275" y1="170" x2="455" y2="170" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="184" fill="{ORANGE}" font-size="8" font-weight="600">Усадка пластика:</text>
  <text x="455" y="184" text-anchor="end" fill="{ACCENT}" font-size="8">0.3 — 0.5%</text>

  <line x1="275" y1="190" x2="455" y2="190" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="204" fill="{HIGHLIGHT}" font-size="8" font-weight="600">Посадка с натягом:</text>
  <text x="455" y="204" text-anchor="end" fill="{ACCENT}" font-size="8">−0.1 мм</text>

  <line x1="275" y1="210" x2="455" y2="210" stroke="{LIGHT}" stroke-width="0.5"/>

  <text x="275" y="224" fill="{PRIMARY}" font-size="8" font-weight="600">Слой ступенька:</text>
  <text x="455" y="224" text-anchor="end" fill="{ACCENT}" font-size="8">Высота слоя</text>

  <!-- Bottom: Assembly -->
  <rect x="30" y="244" width="440" height="68" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="262" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Сборка и тестирование</text>

  <rect x="45" y="272" width="100" height="28" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="95" y="286" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="500">Подгонка деталей</text>
  <text x="95" y="296" text-anchor="middle" fill="{ACCENT}" font-size="7">Шлифовка</text>

  <text x="155" y="290" text-anchor="middle" fill="{HIGHLIGHT}" font-size="10">→</text>

  <rect x="168" y="272" width="100" height="28" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="218" y="286" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="500">Сборка узлов</text>
  <text x="218" y="296" text-anchor="middle" fill="{ACCENT}" font-size="7">Монтаж</text>

  <text x="278" y="290" text-anchor="middle" fill="{HIGHLIGHT}" font-size="10">→</text>

  <rect x="291" y="272" width="80" height="28" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="331" y="286" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="500">Тест</text>
  <text x="331" y="296" text-anchor="middle" fill="{ACCENT}" font-size="7">Проверка</text>

  <text x="381" y="290" text-anchor="middle" fill="{HIGHLIGHT}" font-size="10">→</text>

  <rect x="394" y="272" width="64" height="28" rx="4" fill="{HIGHLIGHT}"/>
  <text x="426" y="290" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="700">Готово!</text>
''' + svg_footer(8)


def generate_lesson9(data):
    """Управление проектами — Project Management"""
    return svg_header() + header_bar(9, data["title"]) + f'''
  <!-- Top: Project lifecycle -->
  <rect x="30" y="60" width="440" height="65" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Жизненный цикл проекта</text>

  <rect x="42" y="88" width="75" height="28" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="79" y="106" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="600">Инициация</text>

  <text x="124" y="106" fill="{ACCENT}" font-size="10">→</text>

  <rect x="134" y="88" width="75" height="28" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="171" y="106" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="600">Планирование</text>

  <text x="216" y="106" fill="{ACCENT}" font-size="10">→</text>

  <rect x="226" y="88" width="75" height="28" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="263" y="106" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="600">Реализация</text>

  <text x="308" y="106" fill="{ACCENT}" font-size="10">→</text>

  <rect x="318" y="88" width="70" height="28" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="353" y="106" text-anchor="middle" fill="{ACCENT}" font-size="8" font-weight="600">Мониторинг</text>

  <text x="396" y="106" fill="{ACCENT}" font-size="10">→</text>

  <rect x="406" y="88" width="52" height="28" rx="4" fill="{PRIMARY}"/>
  <text x="432" y="106" text-anchor="middle" fill="{WHITE}" font-size="8" font-weight="600">Закрытие</text>

  <!-- Left: Gantt chart -->
  <rect x="30" y="137" width="220" height="105" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="140" y="155" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Диаграмма Ганта</text>

  <!-- Gantt rows -->
  <text x="42" y="172" fill="{ACCENT}" font-size="7">Проектирование</text>
  <rect x="120" y="163" width="60" height="12" rx="3" fill="{BLUE}" opacity="0.7"/>
  <text x="150" y="172" text-anchor="middle" fill="{WHITE}" font-size="6">Нед 1-2</text>

  <text x="42" y="188" fill="{ACCENT}" font-size="7">Моделирование</text>
  <rect x="155" y="179" width="55" height="12" rx="3" fill="{ORANGE}" opacity="0.7"/>
  <text x="182" y="188" text-anchor="middle" fill="{WHITE}" font-size="6">Нед 2-3</text>

  <text x="42" y="204" fill="{ACCENT}" font-size="7">Печать</text>
  <rect x="180" y="195" width="40" height="12" rx="3" fill="{HIGHLIGHT}" opacity="0.7"/>
  <text x="200" y="204" text-anchor="middle" fill="{WHITE}" font-size="6">Нед 3</text>

  <text x="42" y="220" fill="{ACCENT}" font-size="7">Сборка</text>
  <rect x="195" y="211" width="45" height="12" rx="3" fill="{ACCENT2}" opacity="0.7"/>
  <text x="217" y="220" text-anchor="middle" fill="{WHITE}" font-size="6">Нед 4</text>

  <text x="42" y="236" fill="{ACCENT}" font-size="7">Тестирование</text>
  <rect x="215" y="227" width="30" height="12" rx="3" fill="{PRIMARY}" opacity="0.7"/>
  <text x="230" y="236" text-anchor="middle" fill="{WHITE}" font-size="6">Нед 5</text>

  <!-- Right: Key concepts -->
  <rect x="270" y="137" width="200" height="105" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="370" y="155" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Ключевые понятия</text>

  <text x="282" y="172" fill="{BLUE}" font-size="8" font-weight="600">WBS</text>
  <text x="315" y="172" fill="{ACCENT}" font-size="8">— иерархия работ</text>

  <text x="282" y="188" fill="{ORANGE}" font-size="8" font-weight="600">Крит. путь</text>
  <text x="340" y="188" fill="{ACCENT}" font-size="8">— самая длинная цепь</text>

  <text x="282" y="204" fill="{HIGHLIGHT}" font-size="8" font-weight="600">Milestone</text>
  <text x="340" y="204" fill="{ACCENT}" font-size="8">— контрольная точка</text>

  <text x="282" y="220" fill="{PRIMARY}" font-size="8" font-weight="600">Риски</text>
  <text x="315" y="220" fill="{ACCENT}" font-size="8">— вероятности и влияние</text>

  <text x="282" y="236" fill="{ACCENT2}" font-size="8" font-weight="600">Ресурсы</text>
  <text x="328" y="236" fill="{ACCENT}" font-size="8">— время, бюджет, люди</text>

  <!-- Bottom: Agile vs Waterfall -->
  <rect x="30" y="254" width="440" height="58" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="272" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Методологии: Agile ↔ Waterfall</text>

  <rect x="45" y="280" width="195" height="24" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="142" y="296" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="500">Agile: итерации, гибкость, Scrum</text>

  <rect x="260" y="280" width="195" height="24" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="357" y="296" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="500">Waterfall: каскад, фазы, план</text>
''' + svg_footer(9)


def generate_lesson10(data):
    """Командная работа — Teamwork"""
    return svg_header() + header_bar(10, data["title"]) + f'''
  <!-- Top: Team roles -->
  <rect x="30" y="60" width="440" height="90" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Роли в команде проекта</text>

  <!-- Central hub -->
  <circle cx="250" cy="118" r="18" fill="{HIGHLIGHT}" stroke="{WHITE}" stroke-width="2"/>
  <text x="250" y="122" text-anchor="middle" fill="{WHITE}" font-size="7" font-weight="700">ЦЕЛЬ</text>

  <!-- Role nodes around -->
  <circle cx="140" cy="100" r="16" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1.5"/>
  <text x="140" y="103" text-anchor="middle" fill="{BLUE}" font-size="6" font-weight="600">Руковод.</text>
  <line x1="156" y1="108" x2="232" y2="115" stroke="{BLUE}" stroke-width="1" stroke-dasharray="3,2"/>

  <circle cx="360" cy="100" r="16" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1.5"/>
  <text x="360" y="103" text-anchor="middle" fill="{ORANGE}" font-size="6" font-weight="600">Дизайнер</text>
  <line x1="344" y1="108" x2="268" y2="115" stroke="{ORANGE}" stroke-width="1" stroke-dasharray="3,2"/>

  <circle cx="120" cy="132" r="16" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1.5"/>
  <text x="120" y="135" text-anchor="middle" fill="{HIGHLIGHT}" font-size="6" font-weight="600">Инженер</text>
  <line x1="136" y1="126" x2="232" y2="120" stroke="{HIGHLIGHT}" stroke-width="1" stroke-dasharray="3,2"/>

  <circle cx="380" cy="132" r="16" fill="{BG}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="380" y="135" text-anchor="middle" fill="{ACCENT}" font-size="6" font-weight="600">Программ.</text>
  <line x1="364" y1="126" x2="268" y2="120" stroke="{ACCENT}" stroke-width="1" stroke-dasharray="3,2"/>

  <circle cx="180" cy="142" r="16" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1.5"/>
  <text x="180" y="145" text-anchor="middle" fill="{BLUE}" font-size="6" font-weight="600">Тестиров.</text>
  <line x1="196" y1="136" x2="234" y2="126" stroke="{BLUE}" stroke-width="1" stroke-dasharray="3,2"/>

  <circle cx="320" cy="142" r="16" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1.5"/>
  <text x="320" y="145" text-anchor="middle" fill="{ORANGE}" font-size="6" font-weight="600">Докумен.</text>
  <line x1="304" y1="136" x2="266" y2="126" stroke="{ORANGE}" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- Left: Communication -->
  <rect x="30" y="162" width="210" height="80" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="180" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Коммуникация</text>

  <text x="42" y="198" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="198" fill="{ACCENT}" font-size="8">Ежедневные стендапы (Daily)</text>

  <text x="42" y="212" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="212" fill="{ACCENT}" font-size="8">Канбан-доска задач</text>

  <text x="42" y="226" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="226" fill="{ACCENT}" font-size="8">Общие документы (Wiki)</text>

  <text x="42" y="240" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="240" fill="{ACCENT}" font-size="8">Ретроспектива спринта</text>

  <!-- Right: Conflict resolution -->
  <rect x="260" y="162" width="210" height="80" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="180" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Разрешение конфликтов</text>

  <rect x="275" y="190" width="90" height="20" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="320" y="204" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="500">Слушать</text>

  <rect x="375" y="190" width="80" height="20" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="415" y="204" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="500">Понимать</text>

  <rect x="275" y="218" width="90" height="20" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="320" y="232" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="500">Обсуждать</text>

  <rect x="375" y="218" width="80" height="20" rx="4" fill="{PRIMARY}" opacity="0.12" stroke="{PRIMARY}" stroke-width="1"/>
  <text x="415" y="232" text-anchor="middle" fill="{PRIMARY}" font-size="8" font-weight="500">Решать</text>

  <!-- Bottom: Rules -->
  <rect x="30" y="254" width="440" height="58" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="272" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Правила эффективной команды</text>

  <rect x="42" y="280" width="130" height="24" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="107" y="296" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8">Ответственность</text>

  <rect x="182" y="280" width="130" height="24" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="247" y="296" text-anchor="middle" fill="{BLUE}" font-size="8">Взаимопомощь</text>

  <rect x="322" y="280" width="138" height="24" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="391" y="296" text-anchor="middle" fill="{ORANGE}" font-size="8">Конструктивная критика</text>
''' + svg_footer(10)


def generate_lesson11(data):
    """Презентация проекта — Project Presentation"""
    return svg_header() + header_bar(11, data["title"]) + f'''
  <!-- Top: Presentation structure -->
  <rect x="30" y="60" width="440" height="90" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Структура презентации проекта</text>

  <!-- Slides structure -->
  <rect x="42" y="88" width="70" height="52" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="77" y="106" text-anchor="middle" fill="{BLUE}" font-size="8" font-weight="600">Слайд 1</text>
  <text x="77" y="120" text-anchor="middle" fill="{ACCENT}" font-size="7">Титульный</text>
  <text x="77" y="132" text-anchor="middle" fill="{ACCENT}" font-size="7">Название</text>

  <rect x="120" y="88" width="70" height="52" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="155" y="106" text-anchor="middle" fill="{ORANGE}" font-size="8" font-weight="600">Слайд 2</text>
  <text x="155" y="120" text-anchor="middle" fill="{ACCENT}" font-size="7">Проблема</text>
  <text x="155" y="132" text-anchor="middle" fill="{ACCENT}" font-size="7">и цель</text>

  <rect x="198" y="88" width="70" height="52" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="233" y="106" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8" font-weight="600">Слайд 3</text>
  <text x="233" y="120" text-anchor="middle" fill="{ACCENT}" font-size="7">Решение</text>
  <text x="233" y="132" text-anchor="middle" fill="{ACCENT}" font-size="7">и подход</text>

  <rect x="276" y="88" width="70" height="52" rx="4" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="311" y="106" text-anchor="middle" fill="{ACCENT}" font-size="8" font-weight="600">Слайд 4</text>
  <text x="311" y="120" text-anchor="middle" fill="{ACCENT}" font-size="7">Результат</text>
  <text x="311" y="132" text-anchor="middle" fill="{ACCENT}" font-size="7">Демо</text>

  <rect x="354" y="88" width="70" height="52" rx="4" fill="{PRIMARY}" opacity="0.12" stroke="{PRIMARY}" stroke-width="1"/>
  <text x="389" y="106" text-anchor="middle" fill="{PRIMARY}" font-size="8" font-weight="600">Слайд 5</text>
  <text x="389" y="120" text-anchor="middle" fill="{ACCENT}" font-size="7">Выводы</text>
  <text x="389" y="132" text-anchor="middle" fill="{ACCENT}" font-size="7">и планы</text>

  <rect x="432" y="88" width="28" height="52" rx="4" fill="{HIGHLIGHT}"/>
  <text x="446" y="118" text-anchor="middle" fill="{WHITE}" font-size="10" font-weight="700">Q&amp;A</text>

  <!-- Left: Visual tips -->
  <rect x="30" y="162" width="210" height="80" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="135" y="180" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Визуальные принципы</text>

  <text x="42" y="198" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="198" fill="{ACCENT}" font-size="8">Правило третей (композиция)</text>

  <text x="42" y="212" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="212" fill="{ACCENT}" font-size="8">Минимум текста, максимум графики</text>

  <text x="42" y="226" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="226" fill="{ACCENT}" font-size="8">Единый стиль и цветовая схема</text>

  <text x="42" y="240" fill="{HIGHLIGHT}" font-size="8">▸</text>
  <text x="54" y="240" fill="{ACCENT}" font-size="8">Крупный шрифт (≥ 24 pt)</text>

  <!-- Right: Speaking tips -->
  <rect x="260" y="162" width="210" height="80" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="365" y="180" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Навыки выступления</text>

  <text x="272" y="198" fill="{BLUE}" font-size="8">▸</text>
  <text x="284" y="198" fill="{ACCENT}" font-size="8">Зрительный контакт</text>

  <text x="272" y="212" fill="{BLUE}" font-size="8">▸</text>
  <text x="284" y="212" fill="{ACCENT}" font-size="8">Темп речи — 120 слов/мин</text>

  <text x="272" y="226" fill="{BLUE}" font-size="8">▸</text>
  <text x="284" y="226" fill="{ACCENT}" font-size="8">Жесты и мимика</text>

  <text x="272" y="240" fill="{BLUE}" font-size="8">▸</text>
  <text x="284" y="240" fill="{ACCENT}" font-size="8">Подготовка к вопросам</text>

  <!-- Bottom: Time management -->
  <rect x="30" y="254" width="440" height="58" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="272" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Тайминг презентации (5 минут)</text>

  <!-- Time bar -->
  <rect x="45" y="282" width="430" height="18" rx="4" fill="{BG}" stroke="{LIGHT}" stroke-width="0.5"/>
  <rect x="45" y="282" width="43" height="18" rx="4" fill="{BLUE}" opacity="0.8"/>
  <text x="66" y="295" text-anchor="middle" fill="{WHITE}" font-size="7" font-weight="600">0:30</text>

  <rect x="88" y="282" width="86" height="18" fill="{ORANGE}" opacity="0.8"/>
  <text x="131" y="295" text-anchor="middle" fill="{WHITE}" font-size="7" font-weight="600">1:00</text>

  <rect x="174" y="282" width="172" height="18" fill="{HIGHLIGHT}" opacity="0.8"/>
  <text x="260" y="295" text-anchor="middle" fill="{WHITE}" font-size="7" font-weight="600">2:00 — основная часть</text>

  <rect x="346" y="282" width="86" height="18" fill="{ACCENT2}" opacity="0.8"/>
  <text x="389" y="295" text-anchor="middle" fill="{WHITE}" font-size="7" font-weight="600">1:00 — выводы</text>

  <rect x="432" y="282" width="43" height="18" rx="4" fill="{PRIMARY}"/>
  <text x="453" y="295" text-anchor="middle" fill="{WHITE}" font-size="7" font-weight="600">0:30</text>
''' + svg_footer(11)


def generate_lesson12(data):
    """Итоговый проект — Final Project"""
    return svg_header() + header_bar(12, data["title"]) + f'''
  <!-- Top: Project requirements -->
  <rect x="30" y="60" width="440" height="85" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="78" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Требования к итоговому проекту</text>

  <!-- Requirement columns -->
  <rect x="42" y="88" width="105" height="48" rx="4" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="94" y="104" text-anchor="middle" fill="{BLUE}" font-size="9" font-weight="600">Техническая</text>
  <text x="94" y="118" text-anchor="middle" fill="{BLUE}" font-size="8">Чертежи, схемы,</text>
  <text x="94" y="130" text-anchor="middle" fill="{BLUE}" font-size="8">3D-модель</text>

  <rect x="155" y="88" width="105" height="48" rx="4" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="207" y="104" text-anchor="middle" fill="{ORANGE}" font-size="9" font-weight="600">Функциональная</text>
  <text x="207" y="118" text-anchor="middle" fill="{ORANGE}" font-size="8">Рабочий прототип,</text>
  <text x="207" y="130" text-anchor="middle" fill="{ORANGE}" font-size="8">тестирование</text>

  <rect x="268" y="88" width="105" height="48" rx="4" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="320" y="104" text-anchor="middle" fill="{HIGHLIGHT}" font-size="9" font-weight="600">Документация</text>
  <text x="320" y="118" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8">Отчёт, журнал,</text>
  <text x="320" y="130" text-anchor="middle" fill="{HIGHLIGHT}" font-size="8">инструкция</text>

  <rect x="381" y="88" width="78" height="48" rx="4" fill="{PRIMARY}" opacity="0.12" stroke="{PRIMARY}" stroke-width="1"/>
  <text x="420" y="104" text-anchor="middle" fill="{PRIMARY}" font-size="9" font-weight="600">Презентация</text>
  <text x="420" y="118" text-anchor="middle" fill="{PRIMARY}" font-size="8">Демонстрация,</text>
  <text x="420" y="130" text-anchor="middle" fill="{PRIMARY}" font-size="8">защита</text>

  <!-- Left: Evaluation criteria -->
  <rect x="30" y="157" width="220" height="75" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="140" y="175" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Критерии оценки</text>

  <text x="42" y="194" fill="{BLUE}" font-size="8" font-weight="500">▸ Оригинальность идеи</text>
  <text x="42" y="208" fill="{ORANGE}" font-size="8" font-weight="500">▸ Качество исполнения</text>
  <text x="42" y="222" fill="{HIGHLIGHT}" font-size="8" font-weight="500">▸ Функциональность</text>

  <text x="155" y="194" fill="{BLUE}" font-size="8" font-weight="500">▸ Сложность решения</text>
  <text x="155" y="208" fill="{ORANGE}" font-size="8" font-weight="500">▸ Документация</text>
  <text x="155" y="222" fill="{HIGHLIGHT}" font-size="8" font-weight="500">▸ Презентация</text>

  <!-- Right: Skills acquired -->
  <rect x="270" y="157" width="200" height="75" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="370" y="175" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">Приобретённые навыки</text>

  <rect x="280" y="184" width="88" height="18" rx="3" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="1"/>
  <text x="324" y="197" text-anchor="middle" fill="{BLUE}" font-size="7">CAD-моделир.</text>

  <rect x="374" y="184" width="86" height="18" rx="3" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="1"/>
  <text x="417" y="197" text-anchor="middle" fill="{ORANGE}" font-size="7">3D-печать</text>

  <rect x="280" y="208" width="88" height="18" rx="3" fill="{HIGHLIGHT_LIGHT}" stroke="{HIGHLIGHT}" stroke-width="1"/>
  <text x="324" y="221" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7">Программир.</text>

  <rect x="374" y="208" width="86" height="18" rx="3" fill="{BG}" stroke="{ACCENT}" stroke-width="1"/>
  <text x="417" y="221" text-anchor="middle" fill="{ACCENT}" font-size="7">Менеджмент</text>

  <!-- Bottom: Timeline -->
  <rect x="30" y="244" width="440" height="68" rx="6" fill="{WHITE}" stroke="{ACCENT}" stroke-width="1.5"/>
  <text x="250" y="262" text-anchor="middle" fill="{PRIMARY}" font-size="11" font-weight="600">График итогового проекта</text>

  <!-- Timeline -->
  <line x1="60" y1="280" x2="440" y2="280" stroke="{ACCENT}" stroke-width="2"/>
  <polygon points="440,280 434,276 434,284" fill="{ACCENT}"/>

  <!-- Milestones -->
  <circle cx="100" cy="280" r="7" fill="{BLUE}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="100" y="283" text-anchor="middle" fill="{WHITE}" font-size="6" font-weight="700">1</text>
  <text x="100" y="298" text-anchor="middle" fill="{BLUE}" font-size="7">Идея</text>

  <circle cx="170" cy="280" r="7" fill="{ORANGE}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="170" y="283" text-anchor="middle" fill="{WHITE}" font-size="6" font-weight="700">2</text>
  <text x="170" y="298" text-anchor="middle" fill="{ORANGE}" font-size="7">Проект</text>

  <circle cx="240" cy="280" r="7" fill="{HIGHLIGHT}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="240" y="283" text-anchor="middle" fill="{WHITE}" font-size="6" font-weight="700">3</text>
  <text x="240" y="298" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7">Модель</text>

  <circle cx="310" cy="280" r="7" fill="{ACCENT2}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="310" y="283" text-anchor="middle" fill="{WHITE}" font-size="6" font-weight="700">4</text>
  <text x="310" y="298" text-anchor="middle" fill="{ACCENT}" font-size="7">Печать</text>

  <circle cx="370" cy="280" r="7" fill="{PRIMARY}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="370" y="283" text-anchor="middle" fill="{WHITE}" font-size="6" font-weight="700">5</text>
  <text x="370" y="298" text-anchor="middle" fill="{PRIMARY}" font-size="7">Сборка</text>

  <circle cx="425" cy="280" r="7" fill="{HIGHLIGHT}" stroke="{WHITE}" stroke-width="1.5"/>
  <text x="425" y="283" text-anchor="middle" fill="{WHITE}" font-size="6" font-weight="700">6</text>
  <text x="425" y="298" text-anchor="middle" fill="{HIGHLIGHT}" font-size="7">Защита</text>
''' + svg_footer(12)


GENERATORS = {
    1: generate_lesson1,
    2: generate_lesson2,
    3: generate_lesson3,
    4: generate_lesson4,
    5: generate_lesson5,
    6: generate_lesson6,
    7: generate_lesson7,
    8: generate_lesson8,
    9: generate_lesson9,
    10: generate_lesson10,
    11: generate_lesson11,
    12: generate_lesson12,
}


def validate_svg(svg_content):
    """Validate SVG as proper XML."""
    try:
        ET.fromstring(svg_content)
        return True, None
    except ET.ParseError as e:
        return False, str(e)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generated = 0
    validated = 0
    errors = []

    for lesson in LESSONS:
        num = lesson["num"]
        generator = GENERATORS[num]
        svg_content = generator(lesson)

        # Validate
        is_valid, error = validate_svg(svg_content)
        if not is_valid:
            errors.append(f"Lesson {num}: XML validation FAILED - {error}")
            continue

        # Save
        filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        generated += 1
        validated += 1
        print(f"✓ lesson{num}.svg — {lesson['title']} (valid XML, {len(svg_content)} bytes)")

    print(f"\n{'='*60}")
    print(f"Generated: {generated}/12 SVGs")
    print(f"Validated: {validated}/12 as proper XML")
    if errors:
        print(f"\nErrors:")
        for e in errors:
            print(f"  ✗ {e}")
    else:
        print(f"\nAll SVGs passed XML validation!")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
