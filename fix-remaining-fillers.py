#!/usr/bin/env python3
"""
Fix remaining filler options in quiz tasks across all grades.
Replaces meaningless options with contextually relevant alternatives.
"""

import os
import re
from pathlib import Path

GRADES_DIR = Path("/home/z/my-project/school-curriculum-app/src/data/grades")

FILLER_PATTERNS = [
    'Другой ответ', 'Не подходит', 'Нет ответа', 'Не указано',
    'Иногда', 'Зависит от контекста', 'Зависит от ситуации',
    'Нельзя определить', 'Ни на что', 'Неизвестно', 'Неверно',
    'Зависит от программы', 'Ни один', 'Никто не знает', 'Не знаю',
    'Зависит от условий', 'Нет точного ответа'
]

# Subject-specific distractor pools for replacement
SUBJECT_DISTRACTORS = {
    'geography': [
        'Карта', 'Глобус', 'Компас', 'Меридиан', 'Параллель', 'Экватор',
        'Масштаб', 'Рельеф', 'Климат', 'Атмосфера', 'Литосфера', 'Гидросфера',
        'Широта', 'Долгота', 'Полюс', 'Вулкан', 'Плато', 'Низменность',
        'Цунами', 'Гейзер', 'Ледник', 'Тундра', 'Степь', 'Пустыня',
        'Тайфун', 'Муссон', 'Пассат', 'Бриз', 'Циклон', 'Антициклон',
        'Оазис', 'Фьорд', 'Эстуарий', 'Дельта', 'Пороги', 'Водопад',
        'Сейсмос', 'Обломочн', 'Осадочн', 'Метаморфич', 'Магматич',
        'Материк', 'Остров', 'Полуостров', 'Пролив', 'Залив', 'Мыс'
    ],
    'russian': [
        'Согласный', 'Гласный', 'Ударный', 'Безударный', 'Твёрдый', 'Мягкий',
        'Звонкий', 'Глухой', 'Шипящий', 'Свистящий', 'Суффикс', 'Приставка',
        'Корень', 'Окончание', 'Основа', 'Чередование', 'Приставка',
        'Подлежащее', 'Сказуемое', 'Дополнение', 'Определение', 'Обстоятельство',
        'Однородные', 'Сложное', 'Простое', 'Повествовательное', 'Вопросительное',
        'Побудительное', 'Восклицательное', 'Распространённое',
        'Склонение', 'Спряжение', 'Инфинитив', 'Деепричастие', 'Причастие',
        'Наречие', 'Предлог', 'Союз', 'Частица', 'Междометие',
        'Морфема', 'Фонема', 'Графема', 'Лексема', 'Орфограмма', 'Пунктограмма'
    ],
    'geometry': [
        'Биссектриса', 'Медиана', 'Высота', 'Гипотенуза', 'Катет',
        'Апофема', 'Радиус', 'Диаметр', 'Хорда', 'Секущая', 'Касательная',
        'Вектор', 'Орт', 'Коллинеарные', 'Компланарные', 'Направляющие косинусы',
        'Симметрия', 'Гомотетия', 'Подобие', 'Параллельность', 'Перпендикулярность',
        'Тетраэдр', 'Октаэдр', 'Икосаэдр', 'Додекаэдр', 'Призма',
        'Диагональ', 'Сечение', 'Проекция', 'Развёртка', 'Скрещивающиеся'
    ],
    'safety': [
        'Укрытие', 'Тревога', 'Сирена', 'Маршрут', 'План эвакуации',
        'Огнетушитель', 'Щиток', 'Респиратор', 'Аптечка', 'Бинт',
        'Жилет', 'Свисток', 'Фонарик', 'Рация', 'Сигнал',
        'Обход', 'Ограждение', 'Запрет', 'Предупреждение', 'Инструкция'
    ],
    'informatics': [
        'Файл', 'Папка', 'Ярлык', 'Буфер', 'Кэш', 'Реестр',
        'Сервер', 'Клиент', 'Протокол', 'Порт', 'Хост', 'Домен',
        'Браузер', 'Почта', 'Чат', 'Форум', 'Вики', 'Блог',
        'Бит', 'Байт', 'Пиксель', 'Дюйм', 'Частота', 'Разрешение'
    ],
    'digital': [
        'Файл', 'Ссылка', 'Вкладка', 'Окно', 'Меню', 'Панель',
        'Виджет', 'Гаджет', 'Приложение', 'Сервис', 'Аккаунт', 'Профиль',
        'Трафик', 'Кэш', 'Куки', 'Скрипт', 'Плагин', 'Расширение'
    ],
    'finance': [
        'Вклад', 'Кредит', 'Заём', 'Ипотека', 'Лизинг', 'Страховка',
        'Пенсия', 'Стипендия', 'Пособие', 'Субсидия', 'Льгота', 'Квота',
        'Валюта', 'Обмен', 'Перевод', 'Чек', 'Квитанция', 'Счёт'
    ],
    'robotics': [
        'Сервопривод', 'Шаговый двигатель', 'Редуктор', 'Шестерня', 'Ремень',
        'Подшипник', 'Цепь', 'Маховик', 'Кулачок', 'Рычаг', 'Блок',
        'Порта', 'Пин', 'Шина', 'Канал', 'Такт', 'Цикл', 'Таймер'
    ]
}

def get_replacement(subject, question, existing_options, filler_text):
    """Get a contextually appropriate replacement for a filler option."""
    pool = SUBJECT_DISTRACTORS.get(subject, SUBJECT_DISTRACTORS.get('informatics', []))
    
    # Filter out options already in use
    existing_lower = [o.lower().strip() for o in existing_options]
    
    # Try to find a replacement from the pool that's not already used
    for candidate in pool:
        if candidate.lower() not in existing_lower and len(candidate) > 2:
            return candidate
    
    # Fallback: generate a generic but meaningful alternative
    return None

def fix_fillers_in_file(filepath, grade_num, subject_name):
    """Fix filler options in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Find all quiz option arrays and check for fillers
    # We need to process each quiz task individually
    
    # Pattern to find options arrays in quiz tasks
    # This is tricky because we need to maintain context (what question, what other options)
    
    # Let's find all occurrences of filler text in option strings
    for filler in FILLER_PATTERNS:
        # Find filler as a standalone option in an array
        # Pattern: "filler" or 'filler' as a complete option
        escaped = re.escape(filler)
        
        # Find all positions where this filler appears as an option
        pattern = rf'["\']({escaped})["\']'
        
        for match in re.finditer(pattern, content):
            filler_pos = match.start()
            filler_text = match.group(1)
            
            # Find the surrounding context to determine the quiz task
            # Look backward for the nearest question
            before_text = content[:filler_pos]
            
            # Find the nearest "question:" before this position
            q_match = list(re.finditer(r'question\s*:\s*["`]([^"`]*)["`]', before_text))
            if not q_match:
                continue
            last_q = q_match[-1]
            question = last_q.group(1)
            
            # Find all options in the same task (between question and current position + some range)
            # Look for the options array containing this filler
            after_text = content[filler_pos:]
            
            # Find the start of the options array (look backward for 'options: [')
            before_short = before_text[-500:]  # Last 500 chars should be enough
            opt_start_match = list(re.finditer(r'options\s*:\s*\[', before_short))
            if not opt_start_match:
                continue
            
            # Find all options in this array - get text from options:[ to the matching ]
            opt_start_pos = filler_pos - (len(before_short) - opt_start_match[-1].start())
            
            # Extract options from the options array
            # Find the end of the array
            depth = 0
            arr_start = content.index('[', opt_start_pos + len('options: '))
            i = arr_start
            while i < len(content) and depth >= 0:
                if content[i] == '[':
                    depth += 1
                elif content[i] == ']':
                    depth -= 1
                elif content[i] in ('"', "'"):
                    # Skip string
                    q = content[i]
                    i += 1
                    while i < len(content) and content[i] != q:
                        if content[i] == '\\':
                            i += 1
                        i += 1
                i += 1
            
            arr_text = content[arr_start:i]
            
            # Extract all options from this array
            existing_options = []
            for o_match in re.finditer(r'["`]([^"`]*)["`]', arr_text):
                existing_options.append(o_match.group(1))
            
            # Get a replacement
            replacement = get_replacement(subject_name, question, existing_options, filler_text)
            if replacement:
                # Replace just this specific occurrence
                old = f'"{filler_text}"'
                # We need to be careful to replace only the specific occurrence
                # Find the exact position and replace
                new = f'"{replacement}"'
                content = content[:match.start()] + new + content[match.end():]
                changes.append(f'  "{filler_text}" → "{replacement}" (Q: {question[:50]})')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return []

def main():
    all_changes = {}
    
    # Process files with known filler issues
    files_to_fix = {
        '10/geometry': 'geometry',
        '3/informatics': 'informatics',
        '3/safety': 'safety',
        '5/digital': 'digital',
        '5/finance': 'finance',
        '5/geography': 'geography',
        '5/informatics': 'informatics',
        '5/robotics': 'robotics',
        '5/russian': 'russian',
    }
    
    for gs, subject in files_to_fix.items():
        grade, subj = gs.split('/')
        filepath = GRADES_DIR / grade / subject / 'index.ts'
        if not filepath.exists():
            print(f"File not found: {filepath}")
            continue
        
        print(f"\nProcessing Grade {grade}/{subject}...")
        changes = fix_fillers_in_file(filepath, int(grade), subject)
        if changes:
            all_changes[f"{grade}/{subject}"] = changes
            for c in changes:
                print(c)
        else:
            print("  No changes needed")
    
    print(f"\n\nTotal files modified: {len(all_changes)}")
    total_changes = sum(len(c) for c in all_changes.values())
    print(f"Total filler options replaced: {total_changes}")

if __name__ == '__main__':
    main()
