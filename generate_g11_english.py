#!/usr/bin/env python3
"""Generate 10 detailed SVG files for Grade 11 English lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/english"

# ── Lesson data ──────────────────────────────────────────────────────────────

lessons = [
    {
        "num": 1,
        "title": "Mixed Conditionals",
        "subtitle": "Смешанные условные предложения",
        "intro": "Смешанные условные объединяют разные типы условий и результатов для выражения нереальных ситуаций",
        "boxes": [
            {
                "heading": "Условие 3 + Результат 2",
                "formula": "If + Past Perfect, would + V₁",
                "example": "If she had studied, she would pass the exam",
                "note": "Прошлое условие → настоящий результат"
            },
            {
                "heading": "Условие 2 + Результат 3",
                "formula": "If + Past Simple, would have + V₃",
                "example": "If I knew her number, I would have called",
                "note": "Настоящее условие → прошедший результат"
            },
            {
                "heading": "Ключевые маркеры",
                "formula": "If only / I wish / But for / Unless",
                "example": "But for the rain, we would have gone out",
                "note": "But for + существительное = если бы не"
            },
        ],
    },
    {
        "num": 2,
        "title": "Inversion",
        "subtitle": "Инверсия в английском языке",
        "intro": "Инверсия — изменение порядка слов для эмфазы и стилистической выразительности речи",
        "boxes": [
            {
                "heading": "Отрицательная инверсия",
                "formula": "Never / Rarely / Hardly + вспом. глагол + подлежащее",
                "example": "Never have I seen such beauty",
                "note": "Вынесение отрицания на первое место"
            },
            {
                "heading": "Инверсия с So / Such",
                "formula": "So + прил./нареч. + вспом. глагол + подл.",
                "example": "So impressive was the view that we stopped",
                "note": "Акцент на степени качества"
            },
            {
                "heading": "Условная инверсия",
                "formula": "Had / Were / Should + подлежащее + ...",
                "example": "Had I known, I would have acted differently",
                "note": "Замена if в условных 2 и 3 типа"
            },
        ],
    },
    {
        "num": 3,
        "title": "Subjunctive Mood",
        "subtitle": "Сослагательное наклонение",
        "intro": "Сослагательное наклонение выражает желание, предложение, требование или нереальную ситуацию",
        "boxes": [
            {
                "heading": "Present Subjunctive",
                "formula": "suggest / demand / insist + that + V₁",
                "example": "The teacher insisted that he be present",
                "note": "Глагол без окончаний для всех лиц"
            },
            {
                "heading": "Past Subjunctive",
                "formula": "If I were / I wish I were / as if I were",
                "example": "I wish I were taller / If I were you",
                "note": "Were для всех лиц (формальный стиль)"
            },
            {
                "heading": "Фразы с сослагательным",
                "formula": "It's time / It's high time + Past Simple",
                "example": "It's high time we left the office",
                "note": "It's time выражает упрёк или срочность"
            },
        ],
    },
    {
        "num": 4,
        "title": "Complex Structures",
        "subtitle": "Сложные синтаксические конструкции",
        "intro": "Продвинутые конструкции: причастия, герундий, инфинитив и сложное дополнение",
        "boxes": [
            {
                "heading": "Complex Object",
                "formula": "подлежащее + V + объект + V-inf / V-ing / V₃",
                "example": "I want him to finish the report",
                "note": "Глаголы: want, expect, let, make, see"
            },
            {
                "heading": "Complex Subject",
                "formula": "подлежащее + is said/believed + to + V",
                "example": "She is known to have written 10 novels",
                "note": "Пассивная конструкция с инфинитивом"
            },
            {
                "heading": "Participle Clauses",
                "formula": "V-ing / Having + V₃, подлежащее + V",
                "example": "Having finished the test, she left early",
                "note": "Причастный оборот заменяет придаточное"
            },
        ],
    },
    {
        "num": 5,
        "title": "Academic Vocabulary",
        "subtitle": "Академическая лексика",
        "intro": "Слова и фразы, необходимые для написания эссе, статей и академических текстов",
        "boxes": [
            {
                "heading": "Введение и логика",
                "formula": "Furthermore / Moreover / In addition / Consequently",
                "example": "Moreover, recent studies confirm this trend",
                "note": "Связки для добавления аргументов"
            },
            {
                "heading": "Контраст и уступка",
                "formula": "Nevertheless / Nonetheless / Whereas / Albeit",
                "example": "Nevertheless, the results remain inconclusive",
                "note": "Выражение противопоставления"
            },
            {
                "heading": "Заключение и итог",
                "formula": "In conclusion / To summarise / On the whole / Thus",
                "example": "In conclusion, further research is required",
                "note": "Фразы для подведения итогов"
            },
        ],
    },
    {
        "num": 6,
        "title": "Essay Writing",
        "subtitle": "Написание эссе",
        "intro": "Структура и приёмы написания аргументативного эссе на английском языке",
        "boxes": [
            {
                "heading": "Структура эссе",
                "formula": "Introduction → Body (2-3) → Conclusion",
                "example": "Intro: Hook + Thesis statement",
                "note": "Каждый абзац — одна главная мысль"
            },
            {
                "heading": "Thesis Statement",
                "formula": "Тема + позиция автора + план",
                "example": "Technology improves education by enhancing access and engagement",
                "note": "Одно предложение — суть всего эссе"
            },
            {
                "heading": "PEEL-метод",
                "formula": "Point → Evidence → Explanation → Link",
                "example": "Point: Social media harms focus. Evidence: Studies show...",
                "note": "Формула каждого абзаца тела эссе"
            },
        ],
    },
    {
        "num": 7,
        "title": "Debating Skills",
        "subtitle": "Навыки дискуссии и дебатов",
        "intro": "Языковые средства для аргументации, опровержения и ведения дебатов на английском",
        "boxes": [
            {
                "heading": "Представление аргумента",
                "formula": "I firmly believe / The key issue is / It is evident that",
                "example": "I firmly believe that education should be free for all",
                "note": "Уверенное и уважительное выражение мнения"
            },
            {
                "heading": "Опровержение (Rebuttal)",
                "formula": "While I see your point / However, this overlooks / That said",
                "example": "While I see your point, this overlooks the cost factor",
                "note": "Признание + контраргумент"
            },
            {
                "heading": "Подведение итогов",
                "formula": "To sum up our position / Ultimately / On balance",
                "example": "On balance, the benefits outweigh the drawbacks",
                "note": "Завершающая фраза в дебатах"
            },
        ],
    },
    {
        "num": 8,
        "title": "Business English",
        "subtitle": "Деловой английский",
        "intro": "Ключевые фразы и лексика для деловой переписки, переговоров и корпоративного общения",
        "boxes": [
            {
                "heading": "Деловая переписка",
                "formula": "I am writing to / Please find attached / Kindly note",
                "example": "I am writing to inquire about the partnership opportunity",
                "note": "Формальный стиль без сокращений"
            },
            {
                "heading": "Переговоры и встречи",
                "formula": "Let's move on to / I'd like to point out / We're willing to",
                "example": "We're willing to compromise on the delivery date",
                "note": "Вежливая настойчивость в деловом тоне"
            },
            {
                "heading": "Финансовая лексика",
                "formula": "Revenue / Turnover / Profit margin / ROI / Deadline",
                "example": "Our Q3 revenue exceeded the projected profit margin",
                "note": "Термины для отчётов и презентаций"
            },
        ],
    },
    {
        "num": 9,
        "title": "Job Interview",
        "subtitle": "Собеседование на работу",
        "intro": "Языковые стратегии и фразы для успешного прохождения собеседования на английском",
        "boxes": [
            {
                "heading": "Самопрезентация",
                "formula": "I have extensive experience / My background includes / I specialise in",
                "example": "My background includes 5 years in project management",
                "note": "Акцент на достижениях и релевантности"
            },
            {
                "heading": "Ответы на сложные вопросы",
                "formula": "STAR: Situation → Task → Action → Result",
                "example": "Situation: Sales were dropping. Action: I redesigned the process. Result: +30%",
                "note": "Метод STAR для поведенческих вопросов"
            },
            {
                "heading": "Вопросы кандидата",
                "formula": "What does a typical day look like? / What are the team's priorities?",
                "example": "How would you describe the company culture?",
                "note": "Показывает заинтересованность и подготовку"
            },
        ],
    },
    {
        "num": 10,
        "title": "Presentation Skills",
        "subtitle": "Навыки презентации",
        "intro": "Языковые клише и структуры для проведения презентаций на английском языке",
        "boxes": [
            {
                "heading": "Открытие презентации",
                "formula": "Good morning / Today I'd like to talk about / My presentation covers",
                "example": "Today I'd like to talk about our growth strategy for 2025",
                "note": "Приветствие + тема + план выступления"
            },
            {
                "heading": "Переходы и визуальные ссылки",
                "formula": "Moving on to / As you can see / Let's look at / This brings us to",
                "example": "As you can see on this slide, revenue grew by 15%",
                "note": "Плавное переключение между слайдами"
            },
            {
                "heading": "Завершение и вопросы",
                "formula": "To wrap up / In summary / I'd be happy to answer questions",
                "example": "To wrap up, our strategy focuses on three key areas",
                "note": "Итог + приглашение к вопросам аудитории"
            },
        ],
    },
]


def escape(text: str) -> str:
    """Escape XML special characters."""
    return (
        text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_svg(lesson: dict) -> str:
    """Build SVG string for a single lesson."""
    n = lesson["num"]
    title = lesson["title"]
    subtitle = lesson["subtitle"]
    intro = lesson["intro"]
    boxes = lesson["boxes"]

    lines: list[str] = []
    w = 500
    h = 350

    def add(s: str):
        lines.append(s)

    # ── Header ──
    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">')
    add("  <defs>")
    add('    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">')
    add('      <stop offset="0%" stop-color="#E8EAF6"/>')
    add('      <stop offset="100%" stop-color="#FFFFFF"/>')
    add("    </linearGradient>")
    add("  </defs>")

    # ── Background ──
    add(f'  <rect width="{w}" height="{h}" fill="url(#bg)" rx="10"/>')
    add(f'  <rect x="3" y="3" width="{w-6}" height="{h-6}" rx="8" fill="none" stroke="#283593" stroke-width="2.5"/>')

    # ── Title ──
    add(f'  <text x="250" y="36" font-family="Arial,sans-serif" font-size="17" font-weight="bold" fill="#283593" text-anchor="middle">{escape(title)}</text>')
    add(f'  <text x="250" y="54" font-family="Arial,sans-serif" font-size="11" fill="#888888" text-anchor="middle">Английский язык — Урок {n}</text>')

    # ── Divider ──
    add(f'  <line x1="30" y1="62" x2="470" y2="62" stroke="#283593" stroke-width="2" opacity="0.25"/>')

    # ── Intro box ──
    intro_y = 70
    add(f'  <rect x="20" y="{intro_y}" width="460" height="30" rx="5" fill="#283593" opacity="0.10"/>')
    add(f'  <text x="250" y="{intro_y + 20}" font-family="Arial,sans-serif" font-size="11" fill="#283593" text-anchor="middle" font-weight="bold">{escape(intro)}</text>')

    # ── Content boxes ──
    box_top = intro_y + 38
    box_height = 64
    box_gap = 6

    for i, box in enumerate(boxes):
        y = box_top + i * (box_height + box_gap)
        opacity = "0.06" if i % 2 == 0 else "0.04"
        add(f'  <rect x="20" y="{y}" width="460" height="{box_height}" rx="5" fill="#283593" opacity="{opacity}"/>')

        # Heading
        add(f'  <text x="30" y="{y + 16}" font-family="Arial,sans-serif" font-size="11.5" fill="#283593" font-weight="bold">{escape(box["heading"])}</text>')

        # Formula (red)
        add(f'  <text x="30" y="{y + 32}" font-family="Arial,sans-serif" font-size="9.5" fill="#C62828">{escape(box["formula"])}</text>')

        # Example
        add(f'  <text x="30" y="{y + 47}" font-family="Arial,sans-serif" font-size="9.5" fill="#333333" font-style="italic">{escape(box["example"])}</text>')

        # Note (right-aligned)
        add(f'  <text x="475" y="{y + 58}" font-family="Arial,sans-serif" font-size="7.5" fill="#999999" text-anchor="end">{escape(box["note"])}</text>')

    # ── Footer ──
    add(f'  <ellipse cx="250" cy="330" rx="200" ry="10" fill="#283593" opacity="0.06"/>')
    add(f'  <text x="250" y="342" font-family="Arial,sans-serif" font-size="11" fill="#283593" text-anchor="middle" font-style="italic">English · Grade 11</text>')

    add("</svg>")
    return "\n".join(lines)


def validate_xml(svg_text: str) -> bool:
    """Validate SVG as well-formed XML."""
    try:
        ET.fromstring(svg_text)
        return True
    except ET.ParseError as e:
        print(f"  XML validation error: {e}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

    for lesson in lessons:
        n = lesson["num"]
        filename = f"lesson{n}.svg"
        filepath = os.path.join(OUTPUT_DIR, filename)

        svg_text = build_svg(lesson)

        if not validate_xml(svg_text):
            print(f"  ERROR: {filename} is not valid XML — skipping write")
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_text)

        size = os.path.getsize(filepath)
        print(f"  ✓ {filename} ({size} bytes)")

    print(f"\nDone! Generated {len(lessons)} SVG files in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
