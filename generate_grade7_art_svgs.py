#!/usr/bin/env python3
"""Generate Grade 7 Art (ИЗО) SVG lesson images."""

import os
import xml.etree.ElementTree as ET

OUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/7/art"
os.makedirs(OUT_DIR, exist_ok=True)

# Color palette
P = "#EA580C"
PD = "#9A3412"
PL = "#FB923C"
AC = "#D97706"
AL = "#F59E0B"
GD = "#FBBF24"
BT = "#FFFBEB"
BB = "#FED7AA"
TC = "#C2410C"
WR = "#DC2626"
WB = "#78350F"
CB = "#FFF7ED"
CBR = "#FDBA74"
TD = "#431407"
TM = "#7C2D12"
TL = "#A16207"
WH = "#FFFFFF"


def defs():
    return (
        '<defs>\n'
        '  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">\n'
        f'    <stop offset="0%" style="stop-color:{BT};stop-opacity:1" />\n'
        f'    <stop offset="100%" style="stop-color:{BB};stop-opacity:1" />\n'
        '  </linearGradient>\n'
        '  <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">\n'
        f'    <stop offset="0%" style="stop-color:{PD};stop-opacity:1" />\n'
        f'    <stop offset="100%" style="stop-color:{P};stop-opacity:1" />\n'
        '  </linearGradient>\n'
        '  <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">\n'
        f'    <stop offset="0%" style="stop-color:{P};stop-opacity:1" />\n'
        f'    <stop offset="100%" style="stop-color:{AC};stop-opacity:1" />\n'
        '  </linearGradient>\n'
        '  <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">\n'
        f'    <stop offset="0%" style="stop-color:{AC};stop-opacity:1" />\n'
        f'    <stop offset="100%" style="stop-color:{AL};stop-opacity:1" />\n'
        '  </linearGradient>\n'
        '  <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">\n'
        f'    <feDropShadow dx="2" dy="2" stdDeviation="3" floodColor="{PD}" floodOpacity="0.2" />\n'
        '  </filter>\n'
        '  <filter id="softShadow" x="-5%" y="-5%" width="110%" height="110%">\n'
        '    <feDropShadow dx="1" dy="1" stdDeviation="2" floodColor="#000" floodOpacity="0.15" />\n'
        '  </filter>\n'
        '</defs>'
    )


def svg_start():
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">\n'
        + defs() + '\n'
    )


def svg_end():
    return '</svg>'


def header(title, subtitle, num):
    return (
        f'<rect width="800" height="600" fill="url(#bgGrad)" />\n'
        f'<rect x="8" y="8" width="784" height="584" fill="none" stroke="{P}" stroke-width="2" rx="8" />\n'
        f'<rect x="14" y="14" width="772" height="572" fill="none" stroke="{AC}" stroke-width="1" rx="6" stroke-dasharray="8,4" />\n'
        f'<rect x="20" y="16" width="760" height="60" fill="url(#titleGrad)" rx="6" filter="url(#shadow)" />\n'
        f'<text x="400" y="46" fill="{WH}" font-size="22" font-weight="bold" text-anchor="middle" font-family="serif">{title}</text>\n'
        f'<text x="400" y="66" fill="{BB}" font-size="12" text-anchor="middle" font-family="sans-serif">{subtitle}</text>\n'
        f'<circle cx="35" cy="46" r="6" fill="{AC}" opacity="0.6" />\n'
        f'<circle cx="765" cy="46" r="6" fill="{AC}" opacity="0.6" />\n'
        f'<circle cx="400" cy="95" r="14" fill="{P}" filter="url(#softShadow)" />\n'
        f'<text x="400" y="100" fill="{WH}" font-size="14" font-weight="bold" text-anchor="middle" font-family="sans-serif">{num}</text>\n'
    )


def t(x, y, fill, size, text, **kw):
    """Helper to create a text element."""
    weight = kw.get('weight', '')
    anchor = kw.get('anchor', '')
    family = kw.get('family', 'sans-serif')
    style = kw.get('style', '')
    attrs = f'x="{x}" y="{y}" fill="{fill}" font-size="{size}"'
    if weight:
        attrs += f' font-weight="{weight}"'
    if anchor:
        attrs += f' text-anchor="{anchor}"'
    if family:
        attrs += f' font-family="{family}"'
    if style:
        attrs += f' font-style="{style}"'
    return f'<text {attrs}>{text}</text>\n'


def card_start(x, y, w, h, accent_color):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{CB}" rx="6" stroke="{CBR}" stroke-width="1" filter="url(#softShadow)" />\n'
        f'<rect x="{x}" y="{y}" width="{w}" height="4" fill="{accent_color}" rx="2" />\n'
    )


def bullet(x, y, fill, size, text, family='sans-serif'):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="{family}">\u2022 {text}</text>\n'


# ─── Lesson 1 ───
def lesson1():
    s = svg_start()
    s += header("Живопись, графика, скульптура",
                "Виды изобразительного искусства: определения, техники, материалы", "1")

    # --- Column 1: Живопись ---
    s += card_start(30, 115, 230, 280, WR)
    # palette icon
    s += f'<ellipse cx="140" cy="145" rx="50" ry="35" fill="{TC}" opacity="0.15" />\n'
    s += '<circle cx="120" cy="138" r="6" fill="#DC2626" opacity="0.6" />\n'
    s += '<circle cx="135" cy="130" r="5" fill="#2563EB" opacity="0.6" />\n'
    s += '<circle cx="150" cy="133" r="5" fill="#16A34A" opacity="0.6" />\n'
    s += '<circle cx="160" cy="145" r="5" fill="#F59E0B" opacity="0.6" />\n'
    s += t(145, 142, PD, 16, "Живопись", weight="bold", anchor="middle", family="serif")
    s += t(145, 158, TL, 10, '(от слова \u201cживо\u201d \u2014 живо писать)', anchor="middle")
    s += t(42, 178, P, 11, "Определение:", weight="bold")
    s += t(42, 194, TM, 10, "Вид искусства, основанный на")
    s += t(42, 207, TM, 10, "использовании цвета (красок)")
    s += t(42, 228, P, 11, "Техники:", weight="bold")
    s += bullet(42, 244, TM, 10, "Масляная живопись \u2014 масло, холст")
    s += bullet(42, 257, TM, 10, "Акварель \u2014 вода, бумага")
    s += bullet(42, 270, TM, 10, "Гуашь \u2014 непрозрачная краска")
    s += bullet(42, 283, TM, 10, "Темпера \u2014 яичная основа")
    s += bullet(42, 296, TM, 10, "Фреска \u2014 по сырой штукатурке")
    s += t(42, 318, P, 11, "Материалы:", weight="bold")
    s += t(42, 334, TM, 10, "Кисти, холст, бумага, палитра,")
    s += t(42, 347, TM, 10, "масляные/акварельные краски")
    s += t(42, 370, P, 11, "Примеры:", weight="bold")
    s += t(42, 386, TM, 10, "Левитан, Айвазовский, Репин")

    # --- Column 2: Графика ---
    s += card_start(280, 115, 230, 280, "#1C1917")
    # pencil icon
    s += f'<rect x="375" y="125" width="3" height="40" fill="{WB}" opacity="0.5" />\n'
    s += '<polygon points="375,165 378,165 376.5,175" fill="#44403C" opacity="0.5" />\n'
    s += t(395, 142, PD, 16, "Графика", weight="bold", anchor="middle", family="serif")
    s += t(395, 158, TL, 10, '(от греч. \u201cgrapho\u201d \u2014 пишу)', anchor="middle")
    s += t(292, 178, P, 11, "Определение:", weight="bold")
    s += t(292, 194, TM, 10, "Вид искусства, использующий")
    s += t(292, 207, TM, 10, "линии, штрихи, точки (ч/б)")
    s += t(292, 228, P, 11, "Виды графики:", weight="bold")
    s += bullet(292, 244, TM, 10, "Рисунок \u2014 основа графики")
    s += bullet(292, 257, TM, 10, "Станковая \u2014 эстампы, литография")
    s += bullet(292, 270, TM, 10, "Книжная \u2014 иллюстрации")
    s += bullet(292, 283, TM, 10, "Прикладная \u2014 плакат, афиша")
    s += t(292, 305, P, 11, "Техники:", weight="bold")
    s += bullet(292, 321, TM, 10, "Карандаш, уголь, сангина")
    s += bullet(292, 334, TM, 10, "Перо и тушь, линогравюра")
    s += bullet(292, 347, TM, 10, "Офорт, ксилография")
    s += t(292, 370, P, 11, "Примеры:", weight="bold")
    s += t(292, 386, TM, 10, "Врубель, Фаворский, Остроумова")

    # --- Column 3: Скульптура ---
    s += card_start(530, 115, 230, 280, AC)
    # sculpture icon
    s += f'<ellipse cx="655" cy="155" rx="25" ry="30" fill="{AC}" opacity="0.12" />\n'
    s += f'<rect x="645" y="155" width="20" height="25" fill="{AC}" opacity="0.12" rx="3" />\n'
    s += f'<rect x="640" y="180" width="30" height="5" fill="{AC}" opacity="0.12" rx="2" />\n'
    s += t(645, 142, PD, 16, "Скульптура", weight="bold", anchor="middle", family="serif")
    s += t(645, 158, TL, 10, '(от лат. \u201csculpere\u201d \u2014 вырезать)', anchor="middle")
    s += t(542, 178, P, 11, "Определение:", weight="bold")
    s += t(542, 194, TM, 10, "Вид искусства, создающий")
    s += t(542, 207, TM, 10, "объёмные формы в реальном")
    s += t(542, 220, TM, 10, "пространстве")
    s += t(542, 241, P, 11, "Виды:", weight="bold")
    s += bullet(542, 257, TM, 10, "Круглая \u2014 осмотр со всех сторон")
    s += bullet(542, 270, TM, 10, "Рельеф \u2014 барельеф/горельеф")
    s += t(542, 291, P, 11, "Материалы:", weight="bold")
    s += bullet(542, 307, TM, 10, "Камень, мрамор, гранит")
    s += bullet(542, 320, TM, 10, "Дерево, глина, бронза")
    s += bullet(542, 333, TM, 10, "Гипс, стекло, пластик")
    s += t(542, 355, P, 11, "Техники:", weight="bold")
    s += t(542, 371, TM, 10, "Лепка, высекание, отливка,")
    s += t(542, 384, TM, 10, "ковка, резьба")

    # --- Bottom comparison table ---
    s += card_start(30, 410, 730, 170, "url(#goldGrad)")
    s += t(400, 435, PD, 14, "Сравнительная характеристика видов изобразительного искусства",
           weight="bold", anchor="middle", family="serif")
    # Table header
    s += f'<rect x="50" y="448" width="130" height="22" fill="{P}" rx="3" />\n'
    s += t(115, 463, WH, 11, "Признак", weight="bold", anchor="middle")
    s += f'<rect x="185" y="448" width="170" height="22" fill="{WR}" rx="3" />\n'
    s += t(270, 463, WH, 11, "Живопись", weight="bold", anchor="middle")
    s += '<rect x="360" y="448" width="170" height="22" fill="#44403C" rx="3" />\n'
    s += t(445, 463, WH, 11, "Графика", weight="bold", anchor="middle")
    s += f'<rect x="535" y="448" width="210" height="22" fill="{AC}" rx="3" />\n'
    s += t(640, 463, WH, 11, "Скульптура", weight="bold", anchor="middle")

    rows = [
        ("Пространство", "2D (плоскость)", "2D (плоскость)", "3D (объём)"),
        ("Глав. средство", "Цвет, колорит", "Линия, штрих, тон", "Форма, объём"),
        ("Восприятие", "Зрительное", "Зрительное", "Зрительно-осязательное"),
        ("Произведение", "Картина, икона, фреска", "Рисунок, гравюра", "Статуя, рельеф, бюст"),
        ("Выразит-ть", "Цвет, свет, тень", "Контраст, ритм", "Пластика, фактура"),
    ]
    for i, (label, c1, c2, c3) in enumerate(rows):
        yy = 486 + i * 17
        s += t(55, yy, TD, 10, label, weight="bold")
        s += t(190, yy, TM, 10, c1)
        s += t(365, yy, TM, 10, c2)
        s += t(540, yy, TM, 10, c3)
        if i < len(rows) - 1:
            s += f'<line x1="50" y1="{yy+6}" x2="745" y2="{yy+6}" stroke="{CBR}" stroke-width="0.5" />\n'

    s += svg_end()
    return s


# ─── Lesson 2 ───
def lesson2():
    s = svg_start()
    s += header("Портрет, пейзаж, натюрморт",
                "Жанры изобразительного искусства: характеристики и знаменитые примеры", "2")

    # --- Портрет ---
    s += card_start(30, 115, 230, 340, WR)
    # face icon
    s += f'<circle cx="145" cy="150" r="22" fill="{P}" opacity="0.15" />\n'
    s += f'<circle cx="145" cy="145" r="14" fill="none" stroke="{P}" stroke-width="1.5" opacity="0.5" />\n'
    s += f'<circle cx="139" cy="142" r="2" fill="{P}" opacity="0.5" />\n'
    s += f'<circle cx="151" cy="142" r="2" fill="{P}" opacity="0.5" />\n'
    s += f'<path d="M139,150 Q145,156 151,150" fill="none" stroke="{P}" stroke-width="1" opacity="0.5" />\n'
    s += t(145, 182, PD, 16, "Портрет", weight="bold", anchor="middle", family="serif")
    s += t(145, 196, TL, 10, "(от фр. portrait \u2014 изображение)", anchor="middle")
    s += t(42, 216, P, 11, "Характеристика:", weight="bold")
    s += t(42, 232, TM, 10, "Изображение человека или группы")
    s += t(42, 245, TM, 10, "людей. Передаёт внешнее сходство")
    s += t(42, 258, TM, 10, "и внутренний мир героя.")
    s += t(42, 280, P, 11, "Виды портрета:", weight="bold")
    s += bullet(42, 296, TM, 10, "Парадный \u2014 торжественный")
    s += bullet(42, 309, TM, 10, "Камерный \u2014 интимный")
    s += bullet(42, 322, TM, 10, "Автопортрет \u2014 самого себя")
    s += bullet(42, 335, TM, 10, "Психологический \u2014 характер")
    s += t(42, 358, P, 11, "Знаменитые примеры:", weight="bold")
    s += t(42, 374, TM, 10, 'Репин \u201cНе ждали\u201d')
    s += t(42, 387, TM, 10, 'Крамской \u201cНеизвестная\u201d')
    s += t(42, 400, TM, 10, 'Серов \u201cДевочка с персиками\u201d')
    s += t(42, 413, TM, 10, 'Леонардо \u201cМона Лиза\u201d')
    s += t(42, 426, TM, 10, "Рембрандт \u2014 автопортреты")

    # --- Пейзаж ---
    s += card_start(280, 115, 230, 340, "#16A34A")
    # landscape icon
    s += '<path d="M370,160 L385,130 L400,160 Z" fill="#16A34A" opacity="0.3" />\n'
    s += '<path d="M390,160 L405,135 L420,160 Z" fill="#15803D" opacity="0.3" />\n'
    s += '<line x1="350" y1="160" x2="430" y2="160" stroke="#16A34A" stroke-width="1" opacity="0.5" />\n'
    s += '<circle cx="425" cy="125" r="8" fill="#F59E0B" opacity="0.3" />\n'
    s += t(395, 182, PD, 16, "Пейзаж", weight="bold", anchor="middle", family="serif")
    s += t(395, 196, TL, 10, "(от фр. pays \u2014 страна, местность)", anchor="middle")
    s += t(292, 216, P, 11, "Характеристика:", weight="bold")
    s += t(292, 232, TM, 10, "Изображение природы, городской")
    s += t(292, 245, TM, 10, "или сельской среды. Главное \u2014")
    s += t(292, 258, TM, 10, "пространство и световоздушная")
    s += t(292, 271, TM, 10, "среда.")
    s += t(292, 293, P, 11, "Виды пейзажа:", weight="bold")
    s += bullet(292, 309, TM, 10, "Сельский \u2014 природа, деревня")
    s += bullet(292, 322, TM, 10, "Городской \u2014 архитектура")
    s += bullet(292, 335, TM, 10, "Марина \u2014 морской")
    s += bullet(292, 348, TM, 10, "Промышленный \u2014 заводы")
    s += t(292, 371, P, 11, "Знаменитые примеры:", weight="bold")
    s += t(292, 387, TM, 10, 'Левитан \u201cЗолотая осень\u201d')
    s += t(292, 400, TM, 10, 'Шишкин \u201cУтро в сосновом лесу\u201d')
    s += t(292, 413, TM, 10, 'Айвазовский \u201cДевятый вал\u201d')
    s += t(292, 426, TM, 10, 'Саврасов \u201cГрачи прилетели\u201d')
    s += t(292, 439, TM, 10, 'Моне \u201cВпечатление. Восход\u201d')

    # --- Натюрморт ---
    s += card_start(530, 115, 230, 340, AC)
    # vase + fruit icon
    s += f'<ellipse cx="645" cy="160" rx="15" ry="5" fill="{AC}" opacity="0.2" />\n'
    s += f'<path d="M638,155 Q640,135 645,130 Q650,135 652,155 Z" fill="{AC}" opacity="0.2" />\n'
    s += '<circle cx="635" cy="162" r="5" fill="#DC2626" opacity="0.3" />\n'
    s += '<circle cx="650" cy="163" r="4" fill="#F59E0B" opacity="0.3" />\n'
    s += t(645, 182, PD, 16, "Натюрморт", weight="bold", anchor="middle", family="serif")
    s += t(645, 196, TL, 10, "(от фр. nature morte \u2014 мёртвая природа)", anchor="middle")
    s += t(542, 216, P, 11, "Характеристика:", weight="bold")
    s += t(542, 232, TM, 10, "Изображение неодушевлённых")
    s += t(542, 245, TM, 10, "предметов: цветы, фрукты, посуда,")
    s += t(542, 258, TM, 10, "книги, музыкальные инструменты.")
    s += t(542, 280, P, 11, "Виды натюрморта:", weight="bold")
    s += bullet(542, 296, TM, 10, "\u201cVanitas\u201d \u2014 бренность бытия")
    s += bullet(542, 309, TM, 10, "Цветочный \u2014 букеты")
    s += bullet(542, 322, TM, 10, "Завтрак \u2014 посуда, еда")
    s += bullet(542, 335, TM, 10, "Символический \u2014 атрибуты")
    s += t(542, 358, P, 11, "Знаменитые примеры:", weight="bold")
    s += t(542, 374, TM, 10, 'Стожаров \u201cХлеб, соль, братина\u201d')
    s += t(542, 387, TM, 10, 'Класс \u201cНатюрморт с шампиньонами\u201d')
    s += t(542, 400, TM, 10, "Сезанн \u2014 натюрморты с яблоками")
    s += t(542, 413, TM, 10, 'Ван Гог \u201cПодсолнухи\u201d')
    s += t(542, 426, TM, 10, 'Петров-Водкин \u201cСкрипка\u201d')

    # --- Bottom key differences ---
    s += card_start(30, 470, 730, 110, "url(#goldGrad)")
    s += t(400, 495, PD, 13, "Ключевые отличия жанров", weight="bold", anchor="middle", family="serif")
    s += t(55, 515, WR, 11, "Портрет:", weight="bold")
    s += t(115, 515, TM, 10, "главный объект \u2014 человек, его характер и эмоции")
    s += t(55, 535, "#16A34A", 11, "Пейзаж:", weight="bold")
    s += t(120, 535, TM, 10, "главный объект \u2014 природа, пространство, атмосфера")
    s += t(55, 555, AC, 11, "Натюрморт:", weight="bold")
    s += t(135, 555, TM, 10, "главный объект \u2014 предметы, их форма, фактура, цвет, композиция")
    s += t(400, 575, TL, 9, "Жанр определяется тем, ЧТО является главным объектом изображения",
           anchor="middle", style="italic")

    s += svg_end()
    return s


# ─── Lesson 3 ───
def lesson3():
    s = svg_start()
    s += header("Исторический и бытовой жанры",
                "Жанры, рассказывающие о жизни людей: от великих событий до повседневности", "3")

    # --- Исторический жанр ---
    s += card_start(30, 115, 360, 250, WR)
    s += '<line x1="60" y1="130" x2="80" y2="160" stroke="' + WR + '" stroke-width="2" opacity="0.3" />\n'
    s += '<line x1="80" y1="130" x2="60" y2="160" stroke="' + WR + '" stroke-width="2" opacity="0.3" />\n'
    s += t(210, 142, PD, 16, "Исторический жанр", weight="bold", anchor="middle", family="serif")
    s += t(210, 158, TL, 10, "События истории, подвиги, трагедии народа", anchor="middle")
    s += t(42, 180, P, 11, "Особенности:", weight="bold")
    s += bullet(42, 196, TM, 10, "Изображает значительные исторические события")
    s += bullet(42, 209, TM, 10, "Герои \u2014 реальные исторические личности")
    s += bullet(42, 222, TM, 10, "Драматизм, монументальность, масштабность")
    s += bullet(42, 235, TM, 10, "Подчёркивает патриотизм и народный дух")
    s += t(42, 257, P, 11, "Поджанры:", weight="bold")
    s += bullet(42, 273, TM, 10, "Батальный \u2014 сцены сражений")
    s += bullet(42, 286, TM, 10, "Историко-бытовой \u2014 быт в прошлом")
    s += bullet(42, 299, TM, 10, "Мифологический \u2014 мифы и легенды")
    s += t(42, 322, P, 11, "Произведения:", weight="bold")
    s += t(42, 338, TM, 10, 'Суриков \u201cУтро стрелецкой казни\u201d, \u201cБоярыня Морозова\u201d')
    s += t(42, 351, TM, 10, 'Репин \u201cИван Грозный и сын его Иван\u201d')

    # --- Бытовой жанр ---
    s += card_start(410, 115, 360, 250, AC)
    s += f'<rect x="440" y="142" width="18" height="14" fill="none" stroke="{AC}" stroke-width="1.5" opacity="0.4" />\n'
    s += f'<polygon points="440,142 449,132 458,142" fill="none" stroke="{AC}" stroke-width="1.5" opacity="0.4" />\n'
    s += t(590, 142, PD, 16, "Бытовой жанр", weight="bold", anchor="middle", family="serif")
    s += t(590, 158, TL, 10, "Повседневная жизнь, труд и отдых людей", anchor="middle")
    s += t(422, 180, P, 11, "Особенности:", weight="bold")
    s += bullet(422, 196, TM, 10, "Изображает повседневную жизнь людей")
    s += bullet(422, 209, TM, 10, "Герои \u2014 обычные люди, крестьяне, горожане")
    s += bullet(422, 222, TM, 10, "Жизненность, правдивость, простота")
    s += bullet(422, 235, TM, 10, "Часто \u2014 социальная критика, сочувствие")
    s += t(422, 257, P, 11, "Виды:", weight="bold")
    s += bullet(422, 273, TM, 10, "Сценки из крестьянской жизни")
    s += bullet(422, 286, TM, 10, "Городские сцены, интерьеры")
    s += bullet(422, 299, TM, 10, "Семейные сцены, трактирные")
    s += t(422, 322, P, 11, "Произведения:", weight="bold")
    s += t(422, 338, TM, 10, 'Венецианов \u201cНа пашне. Весна\u201d')
    s += t(422, 351, TM, 10, 'Перов \u201cТройка\u201d, \u201cОхотники на привале\u201d')

    # --- Comparison ---
    s += card_start(30, 380, 740, 90, "url(#goldGrad)")
    s += t(400, 405, PD, 13, "Сравнение жанров", weight="bold", anchor="middle", family="serif")
    s += f'<line x1="400" y1="412" x2="400" y2="465" stroke="{CBR}" stroke-width="1" />\n'
    s += t(55, 425, WR, 11, "Исторический жанр:", weight="bold")
    s += bullet(55, 441, TM, 10, "Исключительные события, герои, масштаб")
    s += t(55, 457, TM, 10, "Цель \u2014 напомнить о великом, воспитать патриотизм")
    s += t(420, 425, AC, 11, "Бытовой жанр:", weight="bold")
    s += bullet(420, 441, TM, 10, "Обычные события, простые люди, будни")
    s += t(420, 457, TM, 10, "Цель \u2014 показать реальную жизнь, вызвать сочувствие")

    # --- Timeline ---
    s += card_start(30, 485, 740, 95, "url(#accentGrad)")
    s += t(400, 508, PD, 13, "Развитие жанров в русском искусстве", weight="bold", anchor="middle", family="serif")
    s += f'<line x1="70" y1="535" x2="730" y2="535" stroke="{P}" stroke-width="2" />\n'

    points = [
        (120, "XI\u2013XVII вв.", "Иконопись, фрески"),
        (250, "XVIII в.", "Академизм, историч. жанр"),
        (400, "1860-е", "Передвижники, быт. жанр"),
        (550, "Кон. XIX в.", "Расцвет обоих жанров"),
        (690, "XX\u2013XXI вв.", "Смешение жанров"),
    ]
    for cx, label, desc in points:
        s += f'<circle cx="{cx}" cy="535" r="6" fill="{P}" />\n'
        s += t(cx, 555, TD, 9, label, weight="bold", anchor="middle")
        s += t(cx, 568, TM, 8, desc.split(",")[0], anchor="middle")
        if "," in desc:
            s += t(cx, 578, TM, 8, desc.split(",")[1].strip(), anchor="middle")

    s += svg_end()
    return s


# ─── Lesson 4 ───
def lesson4():
    s = svg_start()
    s += header("Передвижники",
                "Товарищество передвижных художественных выставок (1870\u20131923)", "4")

    # Intro card
    s += card_start(30, 115, 740, 80, "url(#titleGrad)")
    s += t(400, 140, PD, 13, "Художники-передвижники \u2014 искусство на службе народа",
           weight="bold", anchor="middle", family="serif")
    s += bullet(42, 160, TM, 10, "Основано в 1870 г. по инициативе Г. Мясоедова, И. Крамского, Н. Ге и др.")
    s += bullet(42, 175, TM, 10, "Цель: нести искусство в народ, показывать правду жизни, отказаться от академических условностей")
    s += bullet(42, 190, TM, 10, "Выставки передвигались по городам: Москва, Киев, Харьков, Казань и др.")

    artists = [
        {
            "name": "Илья Репин",
            "years": "(1844\u20131930)",
            "accent": WR,
            "desc": "Великий русский живописец, мастер портрета и исторической картины",
            "works": [
                "\u201cБурлаки на Волге\u201d \u2014 тяжёлый труд народа",
                "\u201cИван Грозный и сын\u201d \u2014 психологич. драма",
                "\u201cЗапорожцы\u201d \u2014 юмор и свобода",
                "\u201cНе ждали\u201d \u2014 возвращение ссыльного",
                "\u201cКрестный ход в Курской губ.\u201d",
            ],
            "x": 30, "y": 210,
        },
        {
            "name": "Василий Суриков",
            "years": "(1848\u20131916)",
            "accent": "#7C3AED",
            "desc": "Мастер масштабных исторических полотен, колорист",
            "works": [
                "\u201cУтро стрелецкой казни\u201d \u2014 Пётр I",
                "\u201cБоярыня Морозова\u201d \u2014 раскольница",
                "\u201cМеньшиков в Березове\u201d \u2014 опала",
                "\u201cПокорение Сибири Ермаком\u201d",
                "\u201cПереход Суворова через Альпы\u201d",
            ],
            "x": 400, "y": 210,
        },
        {
            "name": "Иван Шишкин",
            "years": "(1832\u20131898)",
            "accent": "#16A34A",
            "desc": "Певец русского леса, мастер пейзажной живописи",
            "works": [
                "\u201cУтро в сосновом лесу\u201d \u2014 медведи",
                "\u201cРожь\u201d \u2014 бескрайние поля",
                "\u201cКорабельная роща\u201d \u2014 величие леса",
                "\u201cЛесные дали\u201d \u2014 панорама",
                "\u201cСосновый лес. Мачтовый лес\u201d",
            ],
            "x": 30, "y": 370,
        },
        {
            "name": "Исаак Левитан",
            "years": "(1860\u20131900)",
            "accent": AC,
            "desc": 'Мастер \u201cпейзажа настроения\u201d, тонкий лирик',
            "works": [
                "\u201cЗолотая осень\u201d \u2014 яркие краски",
                "\u201cВладимирка\u201d \u2014 путь ссыльных",
                "\u201cНад вечным покоем\u201d \u2014 философия",
                "\u201cМарт\u201d \u2014 пробуждение весны",
                "\u201cВечерний звон\u201d \u2014 монастырь",
            ],
            "x": 400, "y": 370,
        },
    ]

    for a in artists:
        x, y = a["x"], a["y"]
        s += card_start(x, y, 355, 148, a["accent"])
        s += f'<circle cx="{x+20}" cy="{y+24}" r="10" fill="{a["accent"]}" opacity="0.15" />\n'
        s += t(x+38, y+24, PD, 14, a["name"], weight="bold", family="serif")
        s += t(x+38, y+38, TL, 9, a["years"])
        s += t(x+12, y+54, TM, 10, a["desc"], style="italic")
        for i, work in enumerate(a["works"]):
            s += bullet(x+12, y+72+i*14, TM, 10, work)

    # Bottom bar
    s += card_start(30, 535, 740, 45, "url(#goldGrad)")
    s += t(55, 562, PD, 11, "Главные идеи передвижников:", weight="bold", family="serif")
    s += t(280, 562, TM, 10, "реализм \u2022 народность \u2022 правда жизни \u2022 социальная значимость \u2022 гражданственность")

    s += svg_end()
    return s


# ─── Lesson 5 ───
def lesson5():
    s = svg_start()
    s += header("Направления XX\u2013XXI века",
                "Абстракционизм, поп-арт, сюрреализм, цифровое искусство", "5")

    movements = [
        {
            "title": "Абстракционизм",
            "years": "1910-е \u2014 наст. время",
            "accent": "#2563EB",
            "desc": "Отказ от изображения реальных объектов. Главные средства \u2014 цвет, линия, форма.",
            "details": [
                'Основатель: В. Кандинский (\u201cКомпозиции\u201d)',
                'Геометрическая абстракция: Малевич (\u201cЧёрный квадрат\u201d)',
                "Супрематизм \u2014 чистые формы и цвет",
                "Неопластицизм: Мондриан",
            ],
            "icon": '<circle cx="90" cy="158" r="12" fill="#2563EB" opacity="0.15"/>'
                    '<circle cx="90" cy="158" r="6" fill="#2563EB" opacity="0.25"/>'
                    '<circle cx="90" cy="158" r="2" fill="#2563EB" opacity="0.4"/>',
            "x": 30, "y": 115,
        },
        {
            "title": "Поп-арт",
            "years": "1950-е \u2014 1960-е",
            "accent": WR,
            "desc": "Искусство, вдохновлённое массовой культурой: реклама, комиксы, товары.",
            "details": [
                'Энди Уорхол \u2014 \u201cБанка супа Кэмпбелл\u201d',
                'Рой Лихтенстайн \u2014 стиль комиксов',
                "Использование готовых образов (ready-made)",
                "Ирония, повтор, яркие цвета",
            ],
            "icon": (f'<rect x="275" y="148" width="16" height="16" fill="{WR}" opacity="0.2" rx="2"/>'
                     f'<rect x="295" y="148" width="16" height="16" fill="{AC}" opacity="0.2" rx="2"/>'
                     f'<rect x="275" y="168" width="16" height="16" fill="{AL}" opacity="0.2" rx="2"/>'
                     f'<rect x="295" y="168" width="16" height="16" fill="{WR}" opacity="0.2" rx="2"/>'),
            "x": 410, "y": 115,
        },
        {
            "title": "Сюрреализм",
            "years": "1920-е \u2014 наст. время",
            "accent": "#7C3AED",
            "desc": "Мир снов и подсознания. Соединение несоединимого, иррациональность.",
            "details": [
                'Сальвадор Дали \u2014 \u201cПостоянство памяти\u201d',
                'Рене Магритт \u2014 \u201cСын человеческий\u201d',
                'Марк Шагал \u2014 сказочный мир',
                "Метод: автоматическое письмо, сны",
            ],
            "icon": ('<ellipse cx="610" cy="155" rx="14" ry="10" fill="#7C3AED" opacity="0.15"/>'
                     '<path d="M604,158 Q610,148 616,158" fill="none" stroke="#7C3AED" stroke-width="1.5" opacity="0.3"/>'
                     '<circle cx="610" cy="148" r="3" fill="#7C3AED" opacity="0.2"/>'),
            "x": 30, "y": 330,
        },
        {
            "title": "Цифровое искусство",
            "years": "1990-е \u2014 наст. время",
            "accent": "#0891B2",
            "desc": "Искусство, созданное с помощью компьютера: графика, анимация, NFT, ИИ.",
            "details": [
                "CGI, 3D-моделирование, анимация",
                "Генеративное искусство (алгоритмы)",
                "Нейросети: Midjourney, DALL-E, Stable Diffusion",
                "NFT \u2014 цифровые сертификаты уникальности",
            ],
            "icon": ('<rect x="705" y="148" width="18" height="14" fill="none" stroke="#0891B2" '
                     'stroke-width="1.5" opacity="0.3" rx="2"/>'
                     '<line x1="714" y1="162" x2="714" y2="168" stroke="#0891B2" '
                     'stroke-width="1.5" opacity="0.3"/>'
                     '<line x1="707" y1="168" x2="721" y2="168" stroke="#0891B2" '
                     'stroke-width="1.5" opacity="0.3"/>'),
            "x": 410, "y": 330,
        },
    ]

    for m in movements:
        x, y = m["x"], m["y"]
        s += card_start(x, y, 355, 200, m["accent"])
        s += m["icon"] + "\n"
        s += t(x+20, y+30, PD, 15, m["title"], weight="bold", family="serif")
        s += t(x+20, y+44, TL, 9, m["years"])
        s += t(x+12, y+62, TM, 10, m["desc"])
        for i, d in enumerate(m["details"]):
            s += bullet(x+12, y+82+i*16, TM, 10, d)

    # Evolution bar
    s += card_start(30, 545, 740, 38, "url(#accentGrad)")
    s += t(55, 568, PD, 11, "Эволюция:", weight="bold", family="serif")
    s += t(120, 568, "#2563EB", 10, "Абстракция", weight="bold")
    s += t(195, 568, TM, 10, "\u2192")
    s += t(210, 568, WR, 10, "Поп-арт", weight="bold")
    s += t(265, 568, TM, 10, "\u2192")
    s += t(280, 568, "#7C3AED", 10, "Сюрреализм", weight="bold")
    s += t(360, 568, TM, 10, "\u2192")
    s += t(375, 568, AC, 10, "Модернизм", weight="bold")
    s += t(450, 568, TM, 10, "\u2192")
    s += t(465, 568, "#16A34A", 10, "Концептуализм", weight="bold")
    s += t(555, 568, TM, 10, "\u2192")
    s += t(570, 568, "#0891B2", 10, "Цифровое искусство + ИИ", weight="bold")

    s += svg_end()
    return s


# ─── Generate & Validate ───

generators = [
    (1, lesson1),
    (2, lesson2),
    (3, lesson3),
    (4, lesson4),
    (5, lesson5),
]

print("=" * 60)
print("Generating Grade 7 Art SVG files")
print("=" * 60)

all_ok = True
for num, gen in generators:
    path = os.path.join(OUT_DIR, f"lesson-{num}.svg")
    svg_content = gen()

    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"  Written: {path} ({len(svg_content):,} bytes)")

    try:
        tree = ET.parse(path)
        root = tree.getroot()
        ns = "{http://www.w3.org/2000/svg}"
        assert root.tag == f"{ns}svg", f"Root tag is {root.tag}"
        assert root.get("width") == "800", f"Width is {root.get('width')}"
        assert root.get("height") == "600", f"Height is {root.get('height')}"
        children = list(root)
        print(f"    VALID XML: root=svg, 800x600, {len(children)} child elements")
    except ET.ParseError as e:
        print(f"    XML PARSE ERROR: {e}")
        all_ok = False
    except AssertionError as e:
        print(f"    Assertion failed: {e}")
        all_ok = False

print()
if all_ok:
    print("All 5 SVG files generated and validated successfully!")
else:
    print("Some files had validation errors - check above.")

print("\nGenerated files:")
for f in sorted(os.listdir(OUT_DIR)):
    full = os.path.join(OUT_DIR, f)
    size = os.path.getsize(full)
    print(f"  {f}  ({size:,} bytes)")
