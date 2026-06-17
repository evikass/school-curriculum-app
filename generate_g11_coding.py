#!/usr/bin/env python3
"""Generate 32 detailed SVG files for Grade 11 Coding (Программирование) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/coding"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PRIMARY = "#0D47A1"
BG = "#E3F2FD"
WHITE = "#FFFFFF"
ACCENT = "#1565C0"
LIGHT_ACCENT = "#BBDEFB"
DARK_TEXT = "#0D47A1"
BODY_TEXT = "#1A237E"
SUBTLE = "#90CAF9"

NSMAP = "http://www.w3.org/2000/svg"

LESSONS = [
    (1, "Позиционные системы счисления", [
        ("Десятичная", "0–9, основание 10"),
        ("Двоичная", "0–1, основание 2"),
        ("Восьмеричная", "0–7, основание 8"),
        ("Шестнадцатеричная", "0–9, A–F, основание 16"),
    ], "Формула: A = aₙ·qⁿ + … + a₁·q + a₀"),
    (2, "Арифметика в разных системах", [
        ("Сложение", "1010₂ + 110₂ = 10000₂"),
        ("Вычитание", "1010₂ − 110₂ = 100₂"),
        ("Умножение", "101₂ × 11₂ = 1111₂"),
        ("Деление", "1100₂ ÷ 11₂ = 100₂"),
    ], "Правила переноса и заёма зависят от основания"),
    (3, "Представление чисел в компьютере", [
        ("Целые без знака", "0 … 2ⁿ−1"),
        ("Целые со знаком", "Прямой/обратный/дополнительный код"),
        ("Вещественные", "IEEE 754: мантисса + порядок"),
        ("Погрешности", "Конечная разрядность → ошибки"),
    ], "8 бит = 1 байт, 32 бит = int, 64 бит = long"),
    (4, "Кодирование текста и изображений", [
        ("ASCII", "7 бит, 128 символов"),
        ("Unicode", "UTF-8, UTF-16, >140 тыс. символов"),
        ("Растровое изображение", "Пиксели + глубина цвета"),
        ("Векторное изображение", "Примитивы + формулы"),
    ], "I = K × i (информация = кол-во × бит на символ)"),
    (5, "Логические операции", [
        ("Конъюнкция ∧", "И — истина только при обоих 1"),
        ("Дизъюнкция ∨", "ИЛИ — истина при хотя бы одной 1"),
        ("Инверсия ¬", "НЕ — отрицание значения"),
        ("Импликация →", "Ложь только 1→0"),
    ], "Эквиваленция ↔: истина при равных значениях"),
    (6, "Законы алгебры логики", [
        ("Коммутативность", "A∧B = B∧A, A∨B = B∨A"),
        ("Ассоциативность", "(A∧B)∧C = A∧(B∧C)"),
        ("Дистрибутивность", "A∧(B∨C) = (A∧B)∨(A∧C)"),
        ("Закон де Моргана", "¬(A∧B) = ¬A∨¬B"),
    ], "Закон поглощения: A∨(A∧B) = A"),
    (7, "Логические схемы", [
        ("Элемент И", "Два входа → конъюнкция"),
        ("Элемент ИЛИ", "Два входа → дизъюнкция"),
        ("Элемент НЕ", "Один вход → инверсия"),
        ("Сумматор", "Полусумматор и полный сумматор"),
    ], "Триггер — базовый элемент памяти"),
    (8, "Решение логических задач", [
        ("Таблица истинности", "Полный перебор всех комбинаций"),
        ("Упрощение выражений", "Законы алгебры логики"),
        ("Логические уравнения", "Подбор и анализ решений"),
        ("Метод резолюций", "Доказательство от противного"),
    ], "Кол-во решений = кол-во единиц в таблице"),
    (9, "Анализ алгоритмов", [
        ("Сложность O(n)", "Линейный поиск, подсчёт"),
        ("Сложность O(n²)", "Пузырьковая сортировка"),
        ("Сложность O(log n)", "Бинарный поиск"),
        ("Сложность O(1)", "Доступ по индексу"),
    ], "Временная и пространственная сложность"),
    (10, "Рекурсивные алгоритмы", [
        ("Базовый случай", "Условие остановки рекурсии"),
        ("Рекурсивный вызов", "Функция вызывает сама себя"),
        ("Факториал", "n! = n × (n−1)!; 0! = 1"),
        ("Числа Фибоначчи", "F(n) = F(n−1) + F(n−2)"),
    ], "Стек вызовов → риск переполнения"),
    (11, "Динамическое программирование", [
        ("Оптимальная подструктура", "Решение = оптимум подзадач"),
        ("Перекрывающиеся подзадачи", "Кэширование результатов"),
        ("Мемоизация", "Сверху вниз — запоминание"),
        ("Табличный метод", "Снизу вверх — заполнение таблицы"),
    ], "Задача о рюкзаке, наибольшая общая подстрока"),
    (12, "Графы и деревья", [
        ("Ориентированный граф", "Рёбра имеют направление"),
        ("Неориентированный", "Рёбра без направления"),
        ("Взвешенный граф", "Рёбра имеют вес/стоимость"),
        ("Дерево", "Связный граф без циклов"),
    ], "DFS — обход в глубину, BFS — в ширину"),
    (13, "Моделирование", [
        ("Модель", "Упрощённое представление объекта"),
        ("Адекватность", "Соответствие реальному объекту"),
        ("Верификация", "Проверка правильности модели"),
        ("Валидация", "Соответствие цели моделирования"),
    ], "Этапы: цель → модель → эксперимент → анализ"),
    (14, "Графические модели", [
        ("Граф", "Вершины + рёбра связей"),
        ("Дерево решений", "Иерархия выборов"),
        ("Блок-схема", "Алгоритм в графическом виде"),
        ("Диаграмма", "Визуализация данных и связей"),
    ], "Граф — универсальная модель структуры"),
    (15, "Табличные модели", [
        ("Двоичная матрица", "0/1 — наличие/отсутствие связи"),
        ("Весовая матрица", "Числа — веса рёбер графа"),
        ("Таблица «объект-свойство»", "Строки — объекты, столбцы — свойства"),
        ("Таблица «объект-объект»", "Ячейки — отношения пары объектов"),
    ], "Табличная модель удобна для систематизации"),
    (16, "Математические модели", [
        ("Формулы", "Аналитическое описание процессов"),
        ("Уравнения", "Связь переменных и параметров"),
        ("Функции", "Зависимость y = f(x)"),
        ("Системы уравнений", "Модели с несколькими переменными"),
    ], "Модель: абстракция → формализация → расчёт"),
    (17, "Модели сетей", [
        ("Топология «звезда»", "Центральный узел + клиенты"),
        ("Топология «кольцо»", "Замкнутый контур узлов"),
        ("Топология «шина»", "Общая среда передачи"),
        ("Топология «ячеистая»", "Каждый с каждым"),
    ], "Комбинированные топологии в реальных сетях"),
    (18, "IP-адресация", [
        ("IPv4", "4 октета: 192.168.0.1, 32 бита"),
        ("IPv6", "128 бит: 2001:0db8::1"),
        ("Маска подсети", "Определяет сеть и хост-часть"),
        ("Классы A/B/C", "Диапазоны адресов по умолчанию"),
    ], "Частные: 10.x, 172.16–31.x, 192.168.x"),
    (19, "Протоколы Интернета", [
        ("TCP", "Надёжная передача с подтверждением"),
        ("UDP", "Быстрая передача без гарантии"),
        ("HTTP/HTTPS", "Передача веб-страниц, порт 80/443"),
        ("DNS", "Преобразование имени → IP-адрес"),
    ], "Модель OSI: 7 уровней сетевых протоколов"),
    (20, "Сетевое оборудование", [
        ("Маршрутизатор", "Перенаправление пакетов между сетями"),
        ("Коммутатор", "Соединение устройств в LAN"),
        ("Концентратор", "Повторение сигнала на все порты"),
        ("Модем", "Преобразование сигнал ↔ данные"),
    ], "Firewall — фильтрация трафика по правилам"),
    (21, "Угрозы информационной безопасности", [
        ("Вредоносное ПО", "Вирусы, черви, трояны, ransomware"),
        ("Фишинг", "Поддельные сайты и письма"),
        ("Социальная инженерия", "Манипуляция людьми"),
        ("DDoS-атаки", "Перегрузка сервера запросами"),
    ], "Уязвимости нулевого дня — неизвестные разработчику"),
    (22, "Методы защиты", [
        ("Антивирус", "Сигнатуры + эвристика + sandbox"),
        ("Межсетевой экран", "Фильтрация входящего трафика"),
        ("Резервное копирование", "3-2-1 правило бэкапа"),
        ("Обновление ПО", "Патчи безопасности и исправления"),
    ], "Принцип наименьших привилегий"),
    (23, "Криптография", [
        ("Симметричное шифрование", "Один ключ для шифрования и дешифрования"),
        ("Асимметричное", "Пара ключей: открытый + закрытый"),
        ("Хеш-функции", "SHA-256: необратимое преобразование"),
        ("Цифровая подпись", "Аутентификация и целостность"),
    ], "RSA, AES — популярные алгоритмы шифрования"),
    (24, "Правовые аспекты", [
        ("Закон о персональных данных", "ФЗ-152: согласие и хранение"),
        ("Авторское право", "Программы — объект авторского права"),
        ("Лицензии ПО", "GPL, MIT, коммерческие лицензии"),
        ("Ответственность", "Ст. 272–274 УК РФ за киберпреступления"),
    ], "Электронная подпись = юридическая значимость"),
    (25, "Измерение информации", [
        ("Алфавитный подход", "I = K × log₂(N) — мощность алфавита"),
        ("Содержательный подход", "I = log₂(1/p) — вероятность события"),
        ("Единицы", "бит → байт → КБ → МБ → ГБ → ТБ"),
        ("Формула Хартли", "I = log₂(N) для равновероятных"),
    ], "1 байт = 8 бит, 1 КБ = 1024 байт"),
    (26, "Кодирование информации", [
        ("Равномерное кодирование", "Одинаковая длина для всех символов"),
        ("Неравномерное", "Разная длина (код Хаффмана)"),
        ("Условие Фано", "Ни один код не начало другого"),
        ("Префиксные коды", "Однозначное декодирование"),
    ], "Код Хаффмана: частые символы — короткие коды"),
    (27, "Передача информации", [
        ("Пропускная способность", "V = I / t (бит/с)"),
        ("Объём данных", "I = V × t"),
        ("Время передачи", "t = I / V"),
        ("Задержка (latency)", "Время прохождения сигнала"),
    ], "Сжатие данных уменьшает время передачи"),
    (28, "Хранение и обработка информации", [
        ("Базы данных", "Структурированное хранение"),
        ("Реляционные БД", "Таблицы + связи (SQL)"),
        ("СУБД", "MySQL, PostgreSQL, SQLite"),
        ("NoSQL", "Документные, ключ-значение, графовые"),
    ], "Нормализация БД — устранение избыточности"),
    (29, "Структура ЕГЭ по информатике", [
        ("Часть 1", "12 заданий с кратким ответом"),
        ("Часть 2", "6 заданий с развёрнутым ответом"),
        ("Время", "3 часа 55 минут на выполнение"),
        ("Первичный балл", "Максимум 30 баллов"),
    ], "Компьютерный формат с 2021 года"),
    (30, "Типовые задания", [
        ("Кодирование", "Определение объёма и декодирование"),
        ("Логика", "Таблицы истинности, уравнения"),
        ("Алгоритмы", "Анализ программ, рекурсия"),
        ("Графы/игры", "Поиск пути, дерево игры"),
    ], "Практика → разбор ошибок → повторение"),
    (31, "Программирование в ЕГЭ", [
        ("Задание 15", "Логические выражения: перебор"),
        ("Задание 16", "Рекурсивные функции: трассировка"),
        ("Задание 17", "Обработка массива/файла"),
        ("Задание 24–27", "Программирование: строки, файлы, алгоритмы"),
    ], "Python — рекомендуемый язык для ЕГЭ"),
    (32, "Стратегия подготовки", [
        ("Диагностика", "Пробный ЕГЭ → определение уровня"),
        ("План", "Темы по приоритету и сложности"),
        ("Практика", "Не менее 30 мин программирования/день"),
        ("Контроль", "Еженедельные пробники + анализ"),
    ], "Регулярность важнее интенсивности"),
]

def escape_xml(text):
    """Escape special XML characters."""
    return (text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;"))

def make_svg(num, title, items, formula):
    """Generate an SVG string for a lesson card."""
    W, H = 500, 350
    header_h = 70
    footer_h = 32
    content_y = header_h + 10
    content_h = H - header_h - footer_h - 20

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')

    # Defs: gradient + filters
    lines.append('  <defs>')
    lines.append(f'    <linearGradient id="hdr{num}" x1="0" y1="0" x2="1" y2="0">')
    lines.append(f'      <stop offset="0%" stop-color="{PRIMARY}"/>')
    lines.append(f'      <stop offset="100%" stop-color="{ACCENT}"/>')
    lines.append(f'    </linearGradient>')
    lines.append('    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">')
    lines.append('      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#00000022"/>')
    lines.append('    </filter>')
    lines.append('  </defs>')

    # Background rounded rect
    rx = 12
    lines.append(f'  <rect x="2" y="2" width="{W-4}" height="{H-4}" rx="{rx}" ry="{rx}" '
                 f'fill="{BG}" stroke="{PRIMARY}" stroke-width="2.5"/>')

    # Header band
    lines.append(f'  <rect x="2" y="2" width="{W-4}" height="{header_h}" rx="{rx}" ry="{rx}" '
                 f'fill="url(#hdr{num})"/>')
    # Cover bottom corners of header
    lines.append(f'  <rect x="2" y="{header_h - rx}" width="{W-4}" height="{rx}" fill="url(#hdr{num})"/>')

    # Lesson number badge
    badge_cx = 38
    badge_cy = header_h // 2 + 2
    badge_r = 22
    lines.append(f'  <circle cx="{badge_cx}" cy="{badge_cy}" r="{badge_r}" fill="{WHITE}" fill-opacity="0.2"/>')
    lines.append(f'  <text x="{badge_cx}" y="{badge_cy + 1}" text-anchor="middle" dominant-baseline="central" '
                 f'font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="{WHITE}">{num}</text>')

    # Title in header
    title_x = 68
    title_y = 28
    lines.append(f'  <text x="{title_x}" y="{title_y}" font-family="Arial, sans-serif" '
                 f'font-size="15" font-weight="bold" fill="{WHITE}">Программирование — Урок {num}</text>')
    # Main title
    title_y2 = 52
    # Truncate if too long
    display_title = title if len(title) <= 36 else title[:34] + "…"
    lines.append(f'  <text x="{title_x}" y="{title_y2}" font-family="Arial, sans-serif" '
                 f'font-size="17" font-weight="bold" fill="#E3F2FD">{escape_xml(display_title)}</text>')

    # Decorative line under header
    line_y = header_h + 2
    lines.append(f'  <line x1="20" y1="{line_y}" x2="{W-20}" y2="{line_y}" '
                 f'stroke="{SUBTLE}" stroke-width="1" stroke-dasharray="4,3"/>')

    # Content cards — 4 items in 2x2 grid
    card_w = 218
    card_h = 60
    margin_x = 18
    margin_y = 8
    gap_x = W - 2 * margin_x - 2 * card_w
    gap_y = 8
    start_y = content_y + 8

    for i, (label, desc) in enumerate(items):
        col = i % 2
        row = i // 2
        cx = margin_x + col * (card_w + gap_x)
        cy = start_y + row * (card_h + gap_y)

        # Card background
        lines.append(f'  <rect x="{cx}" y="{cy}" width="{card_w}" height="{card_h}" rx="6" ry="6" '
                     f'fill="{WHITE}" stroke="{SUBTLE}" stroke-width="1" filter="url(#shadow)"/>')

        # Left accent bar
        lines.append(f'  <rect x="{cx}" y="{cy}" width="4" height="{card_h}" rx="2" ry="2" fill="{PRIMARY}"/>')

        # Card number circle
        nc_x = cx + 18
        nc_y = cy + 18
        lines.append(f'  <circle cx="{nc_x}" cy="{nc_y}" r="10" fill="{LIGHT_ACCENT}"/>')
        lines.append(f'  <text x="{nc_x}" y="{nc_y + 1}" text-anchor="middle" dominant-baseline="central" '
                     f'font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{PRIMARY}">{i+1}</text>')

        # Card label
        lbl_x = cx + 32
        lbl_y = cy + 18
        disp_label = label if len(label) <= 22 else label[:20] + "…"
        lines.append(f'  <text x="{lbl_x}" y="{lbl_y}" font-family="Arial, sans-serif" '
                     f'font-size="12" font-weight="bold" fill="{DARK_TEXT}">{escape_xml(disp_label)}</text>')

        # Card description
        desc_x = cx + 32
        desc_y = cy + 38
        disp_desc = desc if len(desc) <= 28 else desc[:26] + "…"
        lines.append(f'  <text x="{desc_x}" y="{desc_y}" font-family="Arial, sans-serif" '
                     f'font-size="10" fill="{BODY_TEXT}" fill-opacity="0.8">{escape_xml(disp_desc)}</text>')

    # Formula / key info bar at bottom of content area
    formula_y = H - footer_h - 20
    lines.append(f'  <rect x="18" y="{formula_y}" width="{W-36}" height="24" rx="5" ry="5" '
                 f'fill="{LIGHT_ACCENT}" fill-opacity="0.6"/>')
    # Icon indicator
    ico_x = 30
    lines.append(f'  <text x="{ico_x}" y="{formula_y + 16}" font-family="Arial, sans-serif" '
                 f'font-size="13" fill="{PRIMARY}">★</text>')
    disp_formula = formula if len(formula) <= 56 else formula[:54] + "…"
    lines.append(f'  <text x="46" y="{formula_y + 16}" font-family="Arial, sans-serif" '
                 f'font-size="10.5" font-weight="600" fill="{DARK_TEXT}">{escape_xml(disp_formula)}</text>')

    # Footer
    footer_y = H - footer_h + 2
    lines.append(f'  <rect x="2" y="{footer_y - 8}" width="{W-4}" height="{footer_h + 6}" rx="0" ry="0" '
                 f'fill="{PRIMARY}" fill-opacity="0.08"/>')
    # Bottom corners
    lines.append(f'  <rect x="2" y="{H - rx - 2}" width="{W-4}" height="{rx}" rx="{rx}" ry="{rx}" '
                 f'fill="{BG}" stroke="{PRIMARY}" stroke-width="2.5"/>')
    lines.append(f'  <rect x="3" y="{H - rx - 2}" width="{W-6}" height="{rx - 2}" fill="{PRIMARY}" fill-opacity="0.08"/>')

    lines.append(f'  <text x="{W // 2}" y="{footer_y + 10}" text-anchor="middle" '
                 f'font-family="Arial, sans-serif" font-size="11" fill="{PRIMARY}" font-weight="600">'
                 f'Программирование · 11 класс</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


def validate_xml(svg_text):
    """Validate that the SVG is well-formed XML."""
    try:
        ET.fromstring(svg_text)
        return True
    except ET.ParseError as e:
        return False


def main():
    print("Generating 32 SVG files for Grade 11 Coding...")
    errors = []

    for num, title, items, formula in LESSONS:
        svg_text = make_svg(num, title, items, formula)

        # Validate
        if not validate_xml(svg_text):
            errors.append(f"Lesson {num}: XML validation FAILED")
            print(f"  ✗ Lesson {num}: XML validation FAILED")
            continue

        # Write file
        filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_text)

        print(f"  ✓ Lesson {num}: {title}")

    if errors:
        print(f"\n❌ {len(errors)} errors encountered:")
        for e in errors:
            print(f"  - {e}")
    else:
        print(f"\n✅ All 32 SVG files generated successfully in: {OUTPUT_DIR}")

    # Summary
    files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.endswith('.svg')])
    print(f"   Files created: {len(files)}")
    total_size = sum(os.path.getsize(os.path.join(OUTPUT_DIR, f)) for f in files)
    print(f"   Total size: {total_size:,} bytes")


if __name__ == "__main__":
    main()
