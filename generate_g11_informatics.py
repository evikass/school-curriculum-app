#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 11 Informatics lessons."""

import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/informatics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme
PRIMARY = "#1565C0"
PRIMARY_LIGHT = "#1E88E5"
PRIMARY_DARK = "#0D47A1"
BG_LIGHT = "#E3F2FD"
BG_WHITE = "#FFFFFF"
ACCENT = "#42A5F5"
TEXT_DARK = "#0D47A1"
TEXT_MED = "#37474F"
TEXT_LIGHT = "#546E7A"
BORDER = "#1565C0"

LESSONS = [
    {
        "num": 1,
        "title": "Сложность алгоритмов",
        "icon_symbol": "O(f)",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Сложность алгоритма — функция",
                    "зависимости ресурсов от размера",
                    "входных данных n"
                ]
            },
            {
                "subtitle": "Виды сложности",
                "items": [
                    "O(1) — константная",
                    "O(log n) — логарифмическая",
                    "O(n) — линейная",
                    "O(n log n) — линеаритм.",
                    "O(n²) — квадратичная",
                    "O(2ⁿ) — экспоненциальная"
                ]
            },
            {
                "subtitle": "Пример",
                "items": [
                    "Линейный поиск: O(n)",
                    "Бинарный поиск: O(log n)",
                    "Пузырьковая сортировка: O(n²)"
                ]
            }
        ]
    },
    {
        "num": 2,
        "title": "Рекурсия",
        "icon_symbol": "f(n)",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Рекурсия — вызов функцией",
                    "самой себя с изменёнными",
                    "параметрами"
                ]
            },
            {
                "subtitle": "Ключевые понятия",
                "items": [
                    "Базовый случай — условие",
                    "  остановки рекурсии",
                    "Рекурсивный шаг — сведение",
                    "  задачи к меньшей",
                    "Стек вызовов — память для",
                    "  хранения параметров"
                ]
            },
            {
                "subtitle": "Примеры",
                "items": [
                    "Факториал: n! = n·(n−1)!",
                    "Фибоначчи: F(n)=F(n−1)+F(n−2)",
                    "Ханойские башни",
                    "Обход дерева"
                ]
            }
        ]
    },
    {
        "num": 3,
        "title": "Динамическое программирование",
        "icon_symbol": "DP",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "ДП — метод решения задач",
                    "путём разбиения на подзадачи",
                    "и запоминания результатов"
                ]
            },
            {
                "subtitle": "Принципы",
                "items": [
                    "Оптимальная подструктура",
                    "Пересекающиеся подзадачи",
                    "Восходящий подход (табличный)",
                    "Нисходящий подход (мемоизация)"
                ]
            },
            {
                "subtitle": "Примеры задач",
                "items": [
                    "Числа Фибоначчи — O(n)",
                    "Рюкзак (Knapsack) — O(n·W)",
                    "Наибольшая общая подпослед.",
                    "Расстояние Левенштейна"
                ]
            }
        ]
    },
    {
        "num": 4,
        "title": "Базы данных",
        "icon_symbol": "DB",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "БД — организованная совокуп-",
                    "ность данных, управляемая СУБД"
                ]
            },
            {
                "subtitle": "Ключевые понятия",
                "items": [
                    "Таблица (отношение)",
                    "Поле (атрибут) / Запись (кортеж)",
                    "Первичный ключ (PK)",
                    "Внешний ключ (FK)",
                    "Реляционная модель (SQL)",
                    "Нормализация (1НФ–3НФ)"
                ]
            },
            {
                "subtitle": "SQL-операции",
                "items": [
                    "SELECT ... FROM ... WHERE",
                    "INSERT INTO ... VALUES ...",
                    "UPDATE ... SET ... WHERE ...",
                    "DELETE FROM ... WHERE ..."
                ]
            }
        ]
    },
    {
        "num": 5,
        "title": "Компьютерные сети",
        "icon_symbol": "LAN",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Компьютерная сеть — система",
                    "соединённых узлов для обмена",
                    "данными и ресурсами"
                ]
            },
            {
                "subtitle": "Ключевые понятия",
                "items": [
                    "Модель OSI (7 уровней)",
                    "TCP/IP — стек протоколов",
                    "IP-адрес (IPv4, IPv6)",
                    "DNS — доменная система имён",
                    "Маршрутизатор, коммутатор",
                    "LAN / WAN / WLAN"
                ]
            },
            {
                "subtitle": "Протоколы",
                "items": [
                    "HTTP/HTTPS — веб",
                    "FTP — передача файлов",
                    "SMTP/POP3 — электронная почта",
                    "SSH — удалённый доступ"
                ]
            }
        ]
    },
    {
        "num": 6,
        "title": "Веб-технологии",
        "icon_symbol": "</>",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Веб-технологии — набор средств",
                    "для создания и функциониро-",
                    "вания веб-приложений"
                ]
            },
            {
                "subtitle": "Основы",
                "items": [
                    "HTML — структура страницы",
                    "CSS — оформление и стили",
                    "JavaScript — интерактивность",
                    "DOM — объектная модель документа",
                    "Клиент-серверная архитектура",
                    "HTTP-запросы (GET, POST)"
                ]
            },
            {
                "subtitle": "Пример",
                "items": [
                    "&lt;h1&gt;Заголовок&lt;/h1&gt;",
                    "&lt;p&gt;Текст абзаца&lt;/p&gt;",
                    "CSS: color: #1565C0;",
                    "JS: document.getElementById()"
                ]
            }
        ]
    },
    {
        "num": 7,
        "title": "Криптография",
        "icon_symbol": "🔑",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Криптография — наука о методах",
                    "обеспечения конфиденциаль-",
                    "ности и целостности данных"
                ]
            },
            {
                "subtitle": "Ключевые понятия",
                "items": [
                    "Шифр — алгоритм преобразования",
                    "Ключ — секретный параметр",
                    "Симметричное шифрование (AES)",
                    "Асимметричное (RSA, ECC)",
                    "Хеш-функции (SHA-256)",
                    "Цифровая подпись"
                ]
            },
            {
                "subtitle": "Примеры",
                "items": [
                    "Шифр Цезаря: сдвиг на k",
                    "XOR-шифрование",
                    "RSA: n = p · q, открытый ключ",
                    "SSL/TLS — защита соединений"
                ]
            }
        ]
    },
    {
        "num": 8,
        "title": "Защита информации",
        "icon_symbol": "🛡",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Защита информации — комплекс",
                    "мер по обеспечению конфиден-",
                    "циальности, целостности, доступ."
                ]
            },
            {
                "subtitle": "Угрозы",
                "items": [
                    "Вредоносные программы (вирусы)",
                    "Фишинг и социальная инженерия",
                    "DDoS-атаки",
                    "Утечка данных",
                    "Перехват трафика (MITM)"
                ]
            },
            {
                "subtitle": "Методы защиты",
                "items": [
                    "Антивирусное ПО и брандмауэр",
                    "Шифрование данных",
                    "Двухфакторная аутентификация",
                    "Резервное копирование"
                ]
            }
        ]
    },
    {
        "num": 9,
        "title": "Задания на системы счисления",
        "icon_symbol": "2↔10",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Система счисления — способ",
                    "записи чисел с помощью цифр",
                    "по определённым правилам"
                ]
            },
            {
                "subtitle": "Ключевые понятия",
                "items": [
                    "Двоичная (основание 2): 0,1",
                    "Восьмеричная (основание 8): 0–7",
                    "Десятичная (основание 10): 0–9",
                    "Шестнадцатеричная (осн. 16): 0–F",
                    "Перевод между системами",
                    "Арифметика в различных СС"
                ]
            },
            {
                "subtitle": "Примеры",
                "items": [
                    "1010₂ = 10₁₀",
                    "1A₁₆ = 26₁₀",
                    "12₈ = 10₁₀",
                    "10₁₀ = 1010₂ = 12₈ = A₁₆"
                ]
            }
        ]
    },
    {
        "num": 10,
        "title": "Задания на алгебру логики",
        "icon_symbol": "∧∨¬",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Алгебра логики — раздел мате-",
                    "матики, изучающий логические",
                    "операции и высказывания"
                ]
            },
            {
                "subtitle": "Операции",
                "items": [
                    "Конъюнкция (AND, ∧) — умнож.",
                    "Дизъюнкция (OR, ∨) — сложение",
                    "Инверсия (NOT, ¬) — отрицание",
                    "Импликация (→) — следование",
                    "Эквивалентность (≡) — равносил.",
                    "Законы де Моргана"
                ]
            },
            {
                "subtitle": "Примеры",
                "items": [
                    "Таблицы истинности",
                    "Упрощение: ¬(A∧B) = ¬A∨¬B",
                    "F = (A∧B)∨(¬A∧C)",
                    "Решение логических уравнений"
                ]
            }
        ]
    },
    {
        "num": 11,
        "title": "Программирование в ЕГЭ",
        "icon_symbol": "{};",
        "sections": [
            {
                "subtitle": "Определение",
                "items": [
                    "Разбор заданий ЕГЭ по инфор-",
                    "матике, требующих написания",
                    "программ на Python/Pascal/C++"
                ]
            },
            {
                "subtitle": "Типы заданий",
                "items": [
                    "Задание 17: обработка послед.",
                    "Задание 24: анализ строки",
                    "Задание 25: маски чисел",
                    "Задание 26: сортировка, жадн.",
                    "Задание 27: оптимизация"
                ]
            },
            {
                "subtitle": "Пример (задание 17)",
                "items": [
                    "Найти макс. пару элементов,",
                    "где один кратен 3, другой — нет",
                    "max1 = max2 = 0",
                    "for x in data: ..."
                ]
            }
        ]
    },
    {
        "num": 12,
        "title": "Итоговое повторение",
        "icon_symbol": "∑",
        "sections": [
            {
                "subtitle": "Структура ЕГЭ",
                "items": [
                    "27 заданий, 235 минут",
                    "Часть 1: задания 1–25",
                    "Часть 2: задания 26–27",
                    "Первичный балл: 30"
                ]
            },
            {
                "subtitle": "Ключевые темы",
                "items": [
                    "Системы счисления (зад. 1, 8)",
                    "Алгебра логики (зад. 2, 15)",
                    "Алгоритмы и программы (зад. 6)",
                    "Базы данных (зад. 3, 4)",
                    "Сети и кодирование (зад. 7, 9)",
                    "Программирование (зад. 17–27)"
                ]
            },
            {
                "subtitle": "Советы",
                "items": [
                    "Решать типовые варианты",
                    "Проверять ответы на ПК",
                    "Следить за временем",
                    "Начинать с простых заданий"
                ]
            }
        ]
    }
]


def escape_xml(text):
    """Escape special XML characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")


def build_svg(lesson):
    """Build SVG string for a lesson."""
    num = lesson["num"]
    title = lesson["title"]
    icon = lesson["icon_symbol"]
    sections = lesson["sections"]

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">')

    # Defs
    lines.append('  <defs>')
    lines.append(f'    <linearGradient id="bgGrad{num}" x1="0" y1="0" x2="0" y2="1">')
    lines.append(f'      <stop offset="0%" stop-color="#E3F2FD"/>')
    lines.append(f'      <stop offset="100%" stop-color="#BBDEFB"/>')
    lines.append(f'    </linearGradient>')
    lines.append(f'    <linearGradient id="headerGrad{num}" x1="0" y1="0" x2="1" y2="0">')
    lines.append(f'      <stop offset="0%" stop-color="#1565C0"/>')
    lines.append(f'      <stop offset="100%" stop-color="#0D47A1"/>')
    lines.append(f'    </linearGradient>')
    lines.append(f'    <linearGradient id="accentGrad{num}" x1="0" y1="0" x2="1" y2="1">')
    lines.append(f'      <stop offset="0%" stop-color="#42A5F5"/>')
    lines.append(f'      <stop offset="100%" stop-color="#1E88E5"/>')
    lines.append(f'    </linearGradient>')
    lines.append(f'    <filter id="shadow{num}" x="-2%" y="-2%" width="104%" height="104%">')
    lines.append(f'      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#1565C0" flood-opacity="0.15"/>')
    lines.append(f'    </filter>')
    lines.append('  </defs>')

    # Background
    lines.append(f'  <rect width="500" height="350" fill="url(#bgGrad{num})" rx="12"/>')

    # Border
    lines.append(f'  <rect x="1.25" y="1.25" width="497.5" height="347.5" rx="11" fill="none" stroke="{BORDER}" stroke-width="2.5"/>')

    # Inner subtle border
    lines.append(f'  <rect x="5" y="5" width="490" height="340" rx="9" fill="none" stroke="{BORDER}" stroke-width="0.5" opacity="0.2"/>')

    # Decorative corner triangles
    lines.append(f'  <polygon points="8,8 28,8 8,28" fill="{PRIMARY}" opacity="0.1"/>')
    lines.append(f'  <polygon points="492,8 472,8 492,28" fill="{PRIMARY_DARK}" opacity="0.1"/>')
    lines.append(f'  <polygon points="8,342 28,342 8,322" fill="{PRIMARY}" opacity="0.1"/>')
    lines.append(f'  <polygon points="492,342 472,342 492,322" fill="{PRIMARY_DARK}" opacity="0.1"/>')

    # Header background bar
    lines.append(f'  <rect x="10" y="10" width="480" height="52" fill="url(#headerGrad{num})" rx="8" opacity="0.95"/>')

    # Icon circle in header
    icon_x = 36
    icon_y = 36
    lines.append(f'  <circle cx="{icon_x}" cy="{icon_y}" r="16" fill="url(#accentGrad{num})" opacity="0.3"/>')
    lines.append(f'  <text x="{icon_x}" y="{icon_y + 5}" font-family="monospace,Arial" font-size="11" fill="#FFFFFF" text-anchor="middle" font-weight="bold">{escape_xml(icon)}</text>')

    # Title in header
    lines.append(f'  <text x="58" y="32" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#FFFFFF">{escape_xml(title)}</text>')
    lines.append(f'  <text x="58" y="48" font-family="Arial,sans-serif" font-size="11" fill="#BBDEFB">Информатика — Урок {num}</text>')

    # Separator line
    lines.append(f'  <line x1="20" y1="68" x2="480" y2="68" stroke="{ACCENT}" stroke-width="1.5" opacity="0.4"/>')
    lines.append(f'  <rect x="20" y="66" width="80" height="4" fill="{PRIMARY}" rx="2" opacity="0.25"/>')
    lines.append(f'  <rect x="400" y="66" width="80" height="4" fill="{PRIMARY_DARK}" rx="2" opacity="0.15"/>')

    # Content area - sections
    num_sections = len(sections)
    section_width = 148
    section_height = 205
    start_y = 78
    gap = 12
    total_width = num_sections * section_width + (num_sections - 1) * gap
    start_x = (500 - total_width) / 2

    for i, section in enumerate(sections):
        sx = start_x + i * (section_width + gap)
        sy = start_y

        # Section card background
        lines.append(f'  <rect x="{sx}" y="{sy}" width="{section_width}" height="{section_height}" fill="#FFFFFF" rx="7" filter="url(#shadow{num})" opacity="0.92"/>')

        # Section header strip
        lines.append(f'  <rect x="{sx}" y="{sy}" width="{section_width}" height="26" fill="url(#accentGrad{num})" rx="7"/>')
        lines.append(f'  <rect x="{sx}" y="{sy + 18}" width="{section_width}" height="8" fill="url(#accentGrad{num})"/>')

        # Section title
        lines.append(f'  <text x="{sx + section_width / 2}" y="{sy + 17}" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{escape_xml(section["subtitle"])}</text>')

        # Section items
        item_y = sy + 40
        for item in section["items"]:
            # Determine if it's an indented item
            is_indented = item.startswith("  ")
            display_text = item.strip()
            font_size = 9.5 if len(display_text) > 25 else 10
            text_x = sx + 10 if not is_indented else sx + 18
            fill_color = TEXT_DARK if not is_indented else TEXT_MED

            # Small bullet
            if not is_indented:
                lines.append(f'  <circle cx="{sx + 10}" cy="{item_y - 3}" r="1.8" fill="{PRIMARY}" opacity="0.5"/>')
                lines.append(f'  <text x="{sx + 16}" y="{item_y}" font-family="Arial,sans-serif" font-size="{font_size}" fill="{fill_color}">{escape_xml(display_text)}</text>')
            else:
                lines.append(f'  <text x="{sx + 18}" y="{item_y}" font-family="Arial,sans-serif" font-size="{font_size}" fill="{TEXT_LIGHT}">{escape_xml(display_text)}</text>')

            item_y += 14

    # Decorative dots pattern in content area (subtle)
    for dx in range(0, 500, 40):
        for dy in range(start_y + section_height + 5, 290, 15):
            lines.append(f'  <circle cx="{dx}" cy="{dy}" r="0.5" fill="{PRIMARY}" opacity="0.08"/>')

    # Footer bar
    footer_y = 310
    lines.append(f'  <rect x="10" y="{footer_y}" width="480" height="32" fill="url(#headerGrad{num})" rx="6" opacity="0.08"/>')
    lines.append(f'  <rect x="10" y="{footer_y}" width="480" height="1" fill="{ACCENT}" opacity="0.3"/>')
    lines.append(f'  <text x="250" y="{footer_y + 20}" font-family="Arial,sans-serif" font-size="11" fill="{PRIMARY}" text-anchor="middle" font-weight="bold">Информатика · 11 класс</text>')

    # Lesson number badge in footer
    badge_x = 460
    badge_y = footer_y + 16
    lines.append(f'  <circle cx="{badge_x}" cy="{badge_y}" r="10" fill="{PRIMARY}" opacity="0.15"/>')
    lines.append(f'  <text x="{badge_x}" y="{badge_y + 4}" font-family="Arial,sans-serif" font-size="9" fill="{PRIMARY}" text-anchor="middle" font-weight="bold">{num}</text>')

    lines.append('</svg>')
    return "\n".join(lines)


def validate_xml(svg_string):
    """Validate SVG as XML."""
    try:
        ET.fromstring(svg_string)
        return True, "Valid XML"
    except ET.ParseError as e:
        return False, str(e)


def main():
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 60)

    success_count = 0
    for lesson in LESSONS:
        num = lesson["num"]
        title = lesson["title"]
        filename = f"lesson{num}.svg"
        filepath = os.path.join(OUTPUT_DIR, filename)

        svg_content = build_svg(lesson)

        # Validate
        is_valid, msg = validate_xml(svg_content)
        if not is_valid:
            print(f"  ✗ Lesson {num} ({title}): XML INVALID - {msg}")
            continue

        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)

        file_size = os.path.getsize(filepath)
        print(f"  ✓ Lesson {num}: {title} → {filename} ({file_size} bytes) — {msg}")
        success_count += 1

    print("=" * 60)
    print(f"Generated {success_count}/12 SVG files successfully.")
    if success_count == 12:
        print("All files validated as XML. ✓")
    else:
        print(f"WARNING: {12 - success_count} files had issues!")


if __name__ == "__main__":
    main()
