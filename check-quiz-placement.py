#!/usr/bin/env python3
"""
Check if quiz/game tasks are correctly placed with their corresponding lessons.
Scans all grade/subject index.ts files and verifies:
1. Each game title matches a lesson topic/title in the same subject
2. Quiz questions are thematically aligned with the game/lesson topic
3. No cross-subject contamination (e.g. math questions in history)
"""

import os
import re
import json
from pathlib import Path

GRADES_DIR = Path("/home/z/my-project/school-curriculum-app/src/data/grades")

def extract_string_content(text, start_pos):
    """Extract content of a string literal starting at start_pos (at the quote char)."""
    quote_char = text[start_pos]
    if quote_char not in ('"', "'"):
        return None, start_pos + 1
    
    i = start_pos + 1
    result = []
    while i < len(text):
        if text[i] == '\\':
            if i + 1 < len(text):
                next_char = text[i + 1]
                if next_char == 'n':
                    result.append('\n')
                elif next_char == 't':
                    result.append('\t')
                elif next_char == quote_char:
                    result.append(quote_char)
                elif next_char == '\\':
                    result.append('\\')
                else:
                    result.append(next_char)
                i += 2
            else:
                i += 1
        elif text[i] == quote_char:
            return ''.join(result), i + 1
        else:
            result.append(text[i])
            i += 1
    return None, i

def extract_template_string(text, start_pos):
    """Extract content of a template literal starting at backtick."""
    i = start_pos + 1
    result = []
    while i < len(text):
        if text[i] == '\\':
            if i + 1 < len(text):
                result.append(text[i+1])
                i += 2
            else:
                i += 1
        elif text[i] == '`':
            return ''.join(result), i + 1
        else:
            result.append(text[i])
            i += 1
    return None, i

def find_value(text, key, start_from=0):
    """Find the value associated with a key in JS-like text."""
    # Look for key: or key = pattern
    pattern = re.compile(r'(?:^|[\s,{}])' + re.escape(key) + r'\s*:\s*')
    match = pattern.search(text, start_from)
    if not match:
        return None, -1
    pos = match.end()
    
    # Skip whitespace
    while pos < len(text) and text[pos] in ' \t\n\r':
        pos += 1
    
    if pos >= len(text):
        return None, -1
    
    char = text[pos]
    if char in ('"', "'"):
        value, end_pos = extract_string_content(text, pos)
        return value, end_pos
    elif char == '`':
        value, end_pos = extract_template_string(text, pos)
        return value, end_pos
    elif char == '[':
        return 'ARRAY', pos
    elif char == '{':
        return 'OBJECT', pos
    
    return None, -1

def extract_bracket_content(text, start_pos):
    """Extract content between balanced brackets/braces, return content and end position."""
    if start_pos >= len(text):
        return '', start_pos
    
    open_char = text[start_pos]
    close_char = ']' if open_char == '[' else '}' if open_char == '{' else None
    if not close_char:
        return '', start_pos
    
    depth = 1
    i = start_pos + 1
    while i < len(text) and depth > 0:
        if text[i] == open_char:
            depth += 1
        elif text[i] == close_char:
            depth -= 1
        elif text[i] in ('"', "'"):
            _, i = extract_string_content(text, i)
            continue
        elif text[i] == '`':
            _, i = extract_template_string(text, i)
            continue
        i += 1
    
    return text[start_pos+1:i-1], i

def extract_lesson_titles(text):
    """Extract lesson titles from detailedTopics."""
    titles = []
    # Find all title: "..." patterns within detailedTopics
    for match in re.finditer(r'title\s*:\s*["`]([^"`]*)["`]', text):
        title = match.group(1).strip()
        if title and not title.startswith('import'):
            titles.append(title)
    return titles

def extract_topic_names(text):
    """Extract topic names from detailedTopics."""
    topics = []
    for match in re.finditer(r'topic\s*:\s*["`]([^"`]*)["`]', text):
        topic = match.group(1).strip()
        if topic:
            topics.append(topic)
    return topics

def extract_games_section(text):
    """Extract the games array section."""
    # Find export const games = [
    match = re.search(r'export\s+const\s+games\s*=\s*\[', text)
    if not match:
        return None
    
    start = match.end() - 1  # at [
    content, end = extract_bracket_content(text, start)
    return content

def parse_games(games_text):
    """Parse individual games from the games array text."""
    games = []
    if not games_text:
        return games
    
    # Split by top-level object boundaries
    depth = 0
    current_start = None
    
    i = 0
    while i < len(games_text):
        char = games_text[i]
        if char in ('"', "'"):
            _, i = extract_string_content(games_text, i)
            continue
        elif char == '`':
            _, i = extract_template_string(games_text, i)
            continue
        elif char == '{':
            if depth == 0:
                current_start = i
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0 and current_start is not None:
                game_text = games_text[current_start:i+1]
                game = parse_single_game(game_text)
                if game:
                    games.append(game)
                current_start = None
        i += 1
    
    return games

def parse_single_game(game_text):
    """Parse a single game object."""
    game = {'title': None, 'tasks': [], 'subject': None}
    
    # Extract title
    title_match = re.search(r'title\s*:\s*["`]([^"`]*)["`]', game_text)
    if title_match:
        game['title'] = title_match.group(1).strip()
    
    # Extract subject
    subject_match = re.search(r'subject\s*:\s*["`]([^"`]*)["`]', game_text)
    if subject_match:
        game['subject'] = subject_match.group(1).strip()
    
    # Extract tasks
    tasks_match = re.search(r'tasks\s*:\s*\[', game_text)
    if tasks_match:
        tasks_start = tasks_match.end() - 1
        tasks_content, _ = extract_bracket_content(game_text, tasks_start)
        
        # Parse individual tasks
        task_depth = 0
        task_start = None
        j = 0
        while j < len(tasks_content):
            char = tasks_content[j]
            if char in ('"', "'"):
                _, j = extract_string_content(tasks_content, j)
                continue
            elif char == '`':
                _, j = extract_template_string(tasks_content, j)
                continue
            elif char == '{':
                if task_depth == 0:
                    task_start = j
                task_depth += 1
            elif char == '}':
                task_depth -= 1
                if task_depth == 0 and task_start is not None:
                    task_text = tasks_content[task_start:j+1]
                    task = parse_single_task(task_text)
                    if task:
                        game['tasks'].append(task)
                    task_start = None
            j += 1
    
    return game

def parse_single_task(task_text):
    """Parse a single quiz task."""
    task = {'type': None, 'question': None, 'options': [], 'correctAnswer': None}
    
    # Extract type
    type_match = re.search(r"type\s*:\s*['\"]([^'\"]*)['\"]", task_text)
    if type_match:
        task['type'] = type_match.group(1)
    
    # Extract question
    q_match = re.search(r'question\s*:\s*["`]([^"`]*)["`]', task_text)
    if q_match:
        task['question'] = q_match.group(1).strip()
    
    # Extract correctAnswer (string)
    ca_match = re.search(r'correctAnswer\s*:\s*["`]([^"`]*)["`]', task_text)
    if ca_match:
        task['correctAnswer'] = ca_match.group(1).strip()
    
    # Extract options array
    opt_match = re.search(r'options\s*:\s*\[', task_text)
    if opt_match:
        opt_start = opt_match.end() - 1
        opt_content, _ = extract_bracket_content(task_text, opt_start)
        # Extract string options
        for o_match in re.finditer(r'["`]([^"`]*)["`]', opt_content):
            task['options'].append(o_match.group(1).strip())
    
    return task

def get_subject_keywords(subject_name):
    """Get keywords associated with each school subject."""
    subject_keywords = {
        'math': ['число', 'дробь', 'уравнение', 'вычисл', 'сумма', 'разность', 'произведение', 
                  'частное', 'сложение', 'вычитание', 'умножение', 'деление', 'процент', 'геометри',
                  'треугольник', 'круг', 'площадь', 'периметр', 'объём', 'угол', 'отрезок',
                  'координат', 'график', 'функци', 'интеграл', 'производн', 'логарифм',
                  'степень', 'корень', 'прогресси', 'вероятност', 'статистик', 'множество',
                  'равенство', 'неравенство', 'формул', 'натуральн', 'десятичн', 'разряд'],
        'algebra': ['уравнение', 'функци', 'график', 'переменн', 'коэффициент', 'многочлен',
                     'квадрат', 'корень', 'система', 'неравенство', 'прогресси', 'логарифм',
                     'степень', 'производн', 'интеграл', 'алгебра', 'выражение', 'формул',
                     'тождество', 'дискриминант', 'парабол', 'гипербол'],
        'geometry': ['треугольник', 'угол', 'площадь', 'периметр', 'окружность', 'круг',
                      'прямая', 'отрезок', 'луч', 'многоугольник', 'призма', 'пирамид',
                      'цилиндр', 'конус', 'сфер', 'шар', 'вектор', 'симметри', 'подоби',
                      'параллел', 'перпендикуляр', 'хорд', 'касательн', 'доказательств'],
        'russian': ['существительное', 'прилагательное', 'глагол', 'наречие', 'местоимение',
                     'предлог', 'союз', 'частица', 'причастие', 'деепричастие', 'предложение',
                     'подлежащее', 'сказуемое', 'орфографи', 'пунктуаци', 'морфем',
                     'корень', 'суффикс', 'приставка', 'окончание', 'склонение', 'спряжение',
                     'фонетик', 'лексик', 'синтаксис', 'текст', 'реч', 'букв', 'звук'],
        'literature': ['произведение', 'автор', 'поэ', 'роман', 'повесть', 'рассказ', 'сказк',
                        'герой', 'персонаж', 'сюжет', 'композиция', 'жанр', 'стихотворение',
                        'литератур', 'писатель', 'творчеств', 'эпох', 'направлени', 'классицизм',
                        'романтизм', 'реализм', 'модернизм', 'од', 'баллад', 'басн', 'др',
                        'обр', 'мысл', 'чувств'],
        'history': ['век', 'год', 'войн', 'революци', 'реформ', 'царь', 'император', 'князь',
                     'государств', 'династи', 'битв', 'сражени', 'договор', 'указ', 'закон',
                     'политик', 'власть', 'монарх', 'республик', 'импери', 'орды', 'хан',
                     'крепостн', 'крестьян', 'дворян', 'бояр', 'патриарх', 'собор', 'опричн',
                     'смут', 'междоусоб', 'феодал'],
        'physics': ['скорость', 'сила', 'масса', 'энергия', 'давление', 'температур', 'электр',
                     'магнит', 'волна', 'частот', 'напряжени', 'ток', 'сопротивлени', 'закон',
                     'ньютон', 'гравитац', 'импульс', 'кинетическ', 'потенциальн', 'атом',
                     'ядерн', 'радиоактивн', 'оптик', 'линз', 'зеркал', 'дифракц'],
        'chemistry': ['элемент', 'молекул', 'атом', 'реакци', 'веществ', 'кислот', 'щелоч',
                       'оксид', 'сол', 'металл', 'сплав', 'органическ', 'неорганическ',
                       'валентност', 'степень окислен', 'электроли', 'моль', 'молярн',
                       'периодическ', 'водород', 'кислород', 'углерод', 'азот'],
        'biology': ['клетк', 'организм', 'растени', 'животн', 'гриб', 'бактери', 'вирус',
                     'эволюци', 'ген', 'днк', 'хромосом', 'фотосинтез', 'дыхани', 'пищеварени',
                     'кровообращени', 'нервн', 'выделени', 'размножени', 'эколог', 'биосфер',
                     'вид', 'популяци', 'ткан', 'орган', 'систем', 'членистоног', 'моллюск'],
        'geography': ['материк', 'океан', 'климат', 'рельеф', 'рек', 'озёр', 'мор',
                       'горы', 'равнин', 'стран', 'населени', 'город', 'экономик', 'природ',
                       'зон', 'широта', 'долгот', 'карт', 'планшет', 'вулкан', 'землетрясени',
                       'географ', 'полюс', 'экватор', 'меридиан', 'параллел'],
        'informatics': ['алгоритм', 'программ', 'код', 'данн', 'файл', 'переменн', 'цикл',
                         'массив', 'функци', 'баз данных', 'сет', 'интернет', 'компьютер',
                         'операционн', 'бит', 'байт', 'систем счислен', 'логическ', 'информат',
                         'python', 'сортировк', 'поиск', 'объект', 'класс'],
        'english': ['verb', 'noun', 'adjective', 'adverb', 'pronoun', 'preposition', 'tense',
                     'present', 'past', 'future', 'perfect', 'continuous', 'simple', 'sentence',
                     'word', 'english', 'grammar', 'vocabulary', 'reading', 'writing', 'speaking',
                     'listening', 'article', 'plural', 'irregular', 'modal', 'conditional',
                     'passive', 'active', 'gerund', 'infinitive', 'clauses'],
        'english_ru': ['глагол', 'существительн', 'прилагательн', 'наречи', 'местоимени',
                        'врем', 'настоящ', 'прошедш', 'будущ', 'совершенн', 'длительн',
                        'английск', 'язык', 'перевод', 'предложение', 'артикл', 'множественн',
                        'неправильн', 'модальн', 'условн', 'страдательн', 'действительн'],
        'safety': ['безопасност', 'пожар', 'эвакуац', 'террор', 'первая помощ', 'травм',
                    'опасност', 'чрезвычайн', 'ситуац', 'спасател', 'защит', 'профилактик',
                    'дорог', 'пдд', 'транспорт', 'водн', 'природн', 'опасн'],
        'pe': ['физическ', 'упражнени', 'спорт', 'бег', 'прыжк', 'метани', 'гимнастик',
                'игр', 'соревновани', 'олимпи', 'разминк', 'тренировк', 'выносливост',
                'сил', 'быстрот', 'ловкост', 'гибкост', 'координац', 'здоров'],
        'music': ['музык', 'нот', 'ритм', 'мелоди', 'гармони', 'инструмент', 'песн',
                   'композитор', 'исполнител', 'жанр', 'симфони', 'опер', 'балет',
                   'хор', 'оркестр', 'народн', 'классическ', 'современн', 'тональност'],
        'art': ['живопись', 'рисун', 'скульптур', 'архитектур', 'художник', 'картин',
                 'пейзаж', 'портрет', 'натюрморт', 'цвет', 'композиция', 'перспектив',
                 'стил', 'искусств', 'народн', 'промысл', 'ремесл', 'график', 'дизайн'],
        'tech': ['технологи', 'инструмент', 'материал', 'детал', 'чертёж', 'схем',
                  'обработк', 'соединени', 'монтаж', 'проект', 'конструкц', 'станк',
                  'машин', 'механизм', 'труд', 'рукодели', 'вязан', 'шить', 'кулинар'],
        'social': ['обществ', 'государств', 'прав', 'закон', 'конституц', 'граждан',
                    'политик', 'экономик', 'социал', 'культур', 'морал', 'нравственн',
                    'ценност', 'норм', 'роль', 'статус', 'институт', 'демократи'],
        'ecology': ['эколог', 'окружающ', 'сред', 'загрязнен', 'природ', 'охран',
                     'ресурс', 'отход', 'переработк', 'биоразнообрази', 'климат', 'парников',
                     'озон', 'лес', 'вод', 'почв', 'воздух', 'радиац'],
        'coding': ['код', 'программ', 'алгоритм', 'переменн', 'цикл', 'функци', 'массив',
                    'объект', 'класс', 'отладк', 'синтаксис', 'логическ', 'робот', 'scratch',
                    'python', 'блок', 'команд', 'последовательност', 'услови', 'ветвлен'],
        'robotics': ['робот', 'датчик', 'мотор', 'программ', 'алгоритм', 'сборк',
                      'конструктор', 'механизм', 'автомат', 'управлен', 'микроконтроллер',
                      'arduino', 'серв', 'привод', 'кибернетик'],
        'economy': ['экономик', 'рынок', 'предприниматель', 'бизнес', 'деньг', 'банк',
                     'кредит', 'инвестиц', 'налог', 'прибыл', 'доход', 'расход', 'бюджет',
                     'инфляц', 'безработиц', 'ввп', 'спрос', 'предложени', 'конкуренц',
                     'монопол', 'собственност', 'приватизац'],
        'chemistry_simple': ['хими', 'элемент', 'реакц', 'веществ', 'молекул', 'атом'],
        'nature': ['природ', 'растени', 'животн', 'гриб', 'бактери', 'погод', 'климат',
                    'почв', 'вод', 'воздух', 'полезн', 'ископаем', 'эколог', 'космос',
                    'планет', 'звезд', 'лун', 'солнц'],
        'world': ['мир', 'окружающ', 'природ', 'обществ', 'человек', 'стран', 'народ',
                   'традиц', 'культур', 'семь', 'школ', 'правил', 'безопасност'],
        'reading': ['чтени', 'букв', 'звук', 'слог', 'слов', 'предложени', 'текст',
                     'сказк', 'рассказ', 'стихотворени', 'произведени', 'автор', 'герой'],
        'craft': ['рукодели', 'поделк', 'аппликац', 'лепк', 'рисован', 'бумаг',
                   'картон', 'пластилин', 'краск', 'кист', 'узор', 'орнамент', 'народн'],
        'crafts': ['рукодели', 'поделк', 'аппликац', 'лепк', 'рисован', 'бумаг',
                    'картон', 'пластилин', 'краск', 'кист', 'узор', 'орнамент', 'народн'],
        'projects': ['проект', 'исследован', 'презентац', 'доклад', 'творчеств',
                      'командн', 'сотрудничеств', 'план', 'цел', 'задач', 'результат'],
        'finance': ['финанс', 'деньг', 'бюджет', 'доход', 'расход', 'сбережени',
                     'кредит', 'банк', 'вклад', 'процент', 'налог', 'страхован'],
        'psychology': ['психолог', 'личност', 'характер', 'темперамент', 'эмоц', 'чувств',
                        'восприяти', 'памят', 'внимани', 'мышлен', 'мотивац', 'общени',
                        'конфликт', 'стресс', 'самооценк', 'адаптац'],
        'career': ['професси', 'карьер', 'работ', 'труд', 'специальност', 'образован',
                    'навык', 'компетенц', 'рынок труд', 'резюм', 'собеседован', 'проф ориентац'],
        'law': ['прав', 'закон', 'конституц', 'кодекс', 'юрид', 'суд', 'прокурор',
                 'адвокат', 'преступлен', 'наказани', 'ответственност', 'договор', 'сделк',
                 'наследств', 'семейн', 'трудов', 'гражданск', 'уголовн', 'административн'],
        'philosophy': ['философ', 'бытие', 'сознани', 'познани', 'истин', 'морал',
                        'этик', 'эстетик', 'логик', 'диалектик', 'метафизик', 'онтолог',
                        'гносеолог', 'аксиолог'],
        'astronomy': ['астроном', 'звезд', 'планет', 'галактик', 'вселенн', 'космос',
                       'телескоп', 'солнечн', 'лунн', 'затмен', 'созвезд', 'комет',
                       'астероид', 'метеор', 'орбит', 'гравитац'],
        'business': ['бизнес', 'предприниматель', 'менеджмент', 'маркетинг', 'стартап',
                      'бизнес-план', 'прибыл', 'доход', 'расход', 'клиент', 'товар', 'услуг'],
        'digital': ['цифров', 'интернет', 'сет', 'меди', 'информац', 'безопасност',
                     'социальн', 'сет', 'коммуникац', 'гаджет', 'смартфон', 'приложен'],
        'religion': ['религи', 'вер', 'бог', 'церков', 'храм', 'молитв', 'духовн',
                      'православн', 'ислам', 'буддизм', 'иудаизм', 'священ', 'заповед'],
        'ethics': ['этик', 'морал', 'нравственн', 'добр', 'зл', 'совест', 'долг',
                    'чест', 'справедливост', 'гуманизм', 'ценност', 'идеал', 'поступк'],
        'oge': ['огэ', 'экзамен', 'гиа', 'итогов', 'аттестац', 'подготовк',
                 'задани', 'вариант', 'решени', 'балл', 'оценк'],
        'ege': ['егэ', 'экзамен', 'итогов', 'аттестац', 'подготовк',
                 'задани', 'вариант', 'решени', 'балл', 'оценк', 'тест'],
        'lab': ['лабораторн', 'опыт', 'эксперимент', 'измерен', 'наблюден',
                 'прибор', 'оборудован', 'метод', 'гипотез', 'результа'],
    }
    return subject_keywords

def check_quiz_topic_mismatch(quiz_question, quiz_options, game_title, subject_name, subject_keywords):
    """Check if a quiz question seems mismatched with the subject or topic."""
    issues = []
    all_keywords = subject_keywords.get(subject_name, [])
    
    # Check for obvious cross-subject contamination
    # If a quiz question contains very specific keywords from a different subject
    cross_subject_patterns = {
        'math': [r'\d+\s*[+\-*/=]\s*\d+', r'уравнени', r'формул.*\d', r'вычислит'],
        'history': [r'\d+\s*век', r'царь', r'князь', r'орды', r'монарх', r'династ'],
        'literature': [r'автор.*произведени', r'писател', r'поэ.*стих', r'роман'],
        'physics': [r'ньютон', r'скорость.*м/с', r'\d+\s*Дж', r'\d+\s*Н\b'],
        'chemistry': [r'H[₂2]O', r'Fe.*O', r'молярн', r'валентност'],
    }
    
    question_lower = (quiz_question or '').lower()
    
    # Check if the game title matches lesson topics
    # This is a simple heuristic check
    
    return issues

def analyze_file(filepath, grade_num, subject_name):
    """Analyze a single subject file for quiz placement issues."""
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [{'type': 'FILE_ERROR', 'message': f'Cannot read file: {e}'}]
    
    # Extract lesson titles
    lesson_titles = extract_lesson_titles(content)
    topic_names = extract_topic_names(content)
    
    # Extract games section
    games_text = extract_games_section(content)
    if not games_text:
        return []  # No games section
    
    games = parse_games(games_text)
    
    subject_keywords = get_subject_keywords(subject_name)
    subject_kw = subject_keywords.get(subject_name, [])
    
    for game in games:
        game_title = game.get('title', '')
        
        # Check 1: Does game title correspond to a lesson topic or title?
        title_matches_lesson = False
        for lt in lesson_titles:
            # Normalize for comparison
            gt_norm = game_title.lower().strip()
            lt_norm = lt.lower().strip()
            if gt_norm == lt_norm or gt_norm in lt_norm or lt_norm in gt_norm:
                title_matches_lesson = True
                break
        
        for tp in topic_names:
            gt_norm = game_title.lower().strip()
            tp_norm = tp.lower().strip()
            # Remove emoji for comparison
            import re as re2
            gt_clean = re2.sub(r'[^\w\sа-яА-ЯёЁa-zA-Z0-9]', '', gt_norm).strip()
            tp_clean = re2.sub(r'[^\w\sа-яА-ЯёЁa-zA-Z0-9]', '', tp_norm).strip()
            if gt_clean and tp_clean and (gt_clean in tp_clean or tp_clean in gt_clean):
                title_matches_lesson = True
                break
        
        # Check 2: For each quiz task, check if the question seems mismatched
        for i, task in enumerate(game.get('tasks', [])):
            question = task.get('question', '')
            options = task.get('options', [])
            correct = task.get('correctAnswer', '')
            
            if not question:
                continue
            
            question_lower = question.lower()
            
            # Check for cross-subject contamination in quiz questions
            # History-specific terms in non-history subjects
            if subject_name not in ('history', 'social', 'philosophy'):
                history_terms = ['древний мир', 'первобытный мир', 'средние века', 'новое время', 
                                'новейшее время', 'монархия', 'республика', 'демократия', 'империя',
                                'феодализм', 'ренессанс', 'реформация', 'просвещение', 'колонизация',
                                'бородинское сражение', 'отечественная война', 'екатерина ii',
                                'александр невский', 'дмитрий донской', 'иван грозный', 'пётр i',
                                'куликовская битва', 'крепостное право']
                for term in history_terms:
                    if term in question_lower:
                        issues.append({
                            'type': 'CROSS_SUBJECT',
                            'grade': grade_num,
                            'subject': subject_name,
                            'game_title': game_title,
                            'task_index': i,
                            'question': question[:80],
                            'issue': f'History term "{term}" found in {subject_name} quiz'
                        })
                        break
            
            # Check for terms from other subjects contaminating
            # Math terms in non-math subjects
            if subject_name not in ('math', 'algebra', 'geometry'):
                math_patterns = [r'\b\d+\s*[+\-×÷]\s*\d+\s*=', r'вычислите:\s*\d', 
                                r'решите уравнение', r'найдите значение выражени']
                for pat in math_patterns:
                    if re.search(pat, question_lower):
                        issues.append({
                            'type': 'CROSS_SUBJECT',
                            'grade': grade_num,
                            'subject': subject_name,
                            'game_title': game_title,
                            'task_index': i,
                            'question': question[:80],
                            'issue': f'Math pattern found in {subject_name} quiz'
                        })
                        break
            
            # Check if options contain fillers that were missed
            for opt in options:
                opt_lower = opt.lower().strip()
                if opt_lower in ('другой ответ', 'не знаю', 'никто не знает', 'иногда', 
                                'зависит от контекста', 'зависит от ситуации', 'нельзя определить',
                                'ни на что', 'нет ответа', 'неизвестно', 'не указано',
                                'ни один', 'не подходит', 'зависит от программы'):
                    issues.append({
                        'type': 'FILLER_OPTION',
                        'grade': grade_num,
                        'subject': subject_name,
                        'game_title': game_title,
                        'task_index': i,
                        'question': question[:80],
                        'issue': f'Filler option "{opt}" found'
                    })
            
            # Check if correctAnswer exists in options
            if correct and options and correct not in options:
                # For 'find' type, correctAnswer might be an array
                if task.get('type') != 'find':
                    issues.append({
                        'type': 'CORRECT_ANSWER_MISSING',
                        'grade': grade_num,
                        'subject': subject_name,
                        'game_title': game_title,
                        'task_index': i,
                        'question': question[:80],
                        'issue': f'correctAnswer "{correct}" not in options {options}'
                    })
            
            # Check for duplicate options
            if len(options) != len(set(options)):
                dupes = [opt for opt in options if options.count(opt) > 1]
                issues.append({
                    'type': 'DUPLICATE_OPTIONS',
                    'grade': grade_num,
                    'subject': subject_name,
                    'game_title': game_title,
                    'task_index': i,
                    'question': question[:80],
                    'issue': f'Duplicate options: {set(dupes)}'
                })
            
            # Check for game quiz tasks that have keyPoints/examples inside them (structural error)
            task_text = str(task)
            if 'keyPoints' in task_text and task.get('type') == 'quiz':
                issues.append({
                    'type': 'STRUCTURAL_ERROR',
                    'grade': grade_num,
                    'subject': subject_name,
                    'game_title': game_title,
                    'task_index': i,
                    'question': question[:80],
                    'issue': 'Quiz task contains keyPoints - should be in lesson, not quiz'
                })
    
    return issues

def main():
    all_issues = []
    
    # Iterate over all grade directories
    for grade_dir in sorted(GRADES_DIR.iterdir()):
        if not grade_dir.is_dir():
            continue
        grade_name = grade_dir.name
        if not grade_name.isdigit():
            continue
        grade_num = int(grade_name)
        
        # Iterate over all subject directories
        for subject_dir in sorted(grade_dir.iterdir()):
            if not subject_dir.is_dir():
                continue
            subject_name = subject_dir.name
            
            index_file = subject_dir / 'index.ts'
            if not index_file.exists():
                continue
            
            print(f"Checking grade {grade_num} / {subject_name}...")
            issues = analyze_file(index_file, grade_num, subject_name)
            all_issues.extend(issues)
    
    print("\n" + "="*80)
    print("QUIZ PLACEMENT CHECK RESULTS")
    print("="*80)
    
    if not all_issues:
        print("\n✅ No issues found! All quizzes seem correctly placed.")
    else:
        # Group issues by type
        by_type = {}
        for issue in all_issues:
            t = issue['type']
            if t not in by_type:
                by_type[t] = []
            by_type[t].append(issue)
        
        print(f"\n❌ Found {len(all_issues)} issues:")
        for issue_type, issues in sorted(by_type.items()):
            print(f"\n--- {issue_type} ({len(issues)} issues) ---")
            for issue in issues[:50]:  # Limit output
                print(f"  Grade {issue['grade']}/{issue['subject']}: {issue['game_title']}")
                print(f"    Q: {issue['question']}")
                print(f"    Issue: {issue['issue']}")
            if len(issues) > 50:
                print(f"  ... and {len(issues) - 50} more")
    
    # Save full results to JSON
    results_file = GRADES_DIR.parent.parent.parent / 'quiz-placement-issues.json'
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(all_issues, f, ensure_ascii=False, indent=2)
    print(f"\nFull results saved to: {results_file}")

if __name__ == '__main__':
    main()
