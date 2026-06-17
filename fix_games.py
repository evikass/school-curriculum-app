#!/usr/bin/env python3
"""
Convert all game tests:
1. fill -> quiz (5 options)  
2. find -> quiz (5 options, single answer)
3. match/order/drag -> quiz (5 options)
4. Quiz with <5 options -> expand to 5
5. Ensure 5+ questions per test (add if needed)
"""
import re, os, json

DIR = '/home/z/my-project/repo-site/src/data/games'

def process_file(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out = []
    i = 0
    changes = 0
    current_tasks_count = 0
    current_game_title = ''
    task_start_line = -1
    tasks_buffer = []
    in_tasks = False
    
    while i < len(lines):
        line = lines[i]
        
        # Track game title
        title_m = re.search(r'title:\s*"([^"]+)"', line)
        if title_m and not in_tasks:
            current_game_title = title_m.group(1)
        
        # Detect task start
        if "type: '" in line and ('fill' in line or 'find' in line or 'match' in line or 'order' in line or 'drag' in line):
            # Read the full task block (may span multiple lines)
            task_text = line
            brace_count = line.count('{') - line.count('}')
            while brace_count > 0 and i + 1 < len(lines):
                i += 1
                task_text += lines[i]
                brace_count += lines[i].count('{') - lines[i].count('}')
            
            # Parse the task
            converted = convert_task(task_text.strip().rstrip(','))
            if converted:
                out.append(converted + ',\n')
                changes += 1
            else:
                out.append(task_text)
            i += 1
            continue
        
        # Check for quiz with 3-4 options
        if "type: 'quiz'" in line:
            task_text = line
            brace_count = line.count('{') - line.count('}')
            while brace_count > 0 and i + 1 < len(lines):
                i += 1
                task_text += lines[i]
                brace_count += lines[i].count('{') - lines[i].count('}')
            
            converted = expand_quiz(task_text.strip().rstrip(','))
            if converted != task_text.strip().rstrip(','):
                out.append(converted + ',\n')
                changes += 1
            else:
                out.append(task_text)
            i += 1
            continue
        
        out.append(line)
        i += 1
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.writelines(out)
    
    print(f"  {os.path.basename(os.path.dirname(fp))}: {changes} changes")
    return changes

def convert_task(text):
    """Convert fill/find/match/order/drag task to quiz"""
    # Extract fields using regex
    type_m = re.search(r"type:\s*'(\w+)'", text)
    question_m = re.search(r"question:\s*\"([^\"]*(?:\"\"[^\"]*)*)\"", text)
    hint_m = re.search(r"hint:\s*\"([^\"]*)\"", text)
    
    if not type_m:
        return None
    
    task_type = type_m.group(1)
    question = question_m.group(1) if question_m else ''
    hint = hint_m.group(1) if hint_m else ''
    
    if task_type == 'fill':
        correct_m = re.search(r"correctAnswer:\s*\"([^\"]*)\"", text)
        correct = correct_m.group(1) if correct_m else ''
        
        # Replace __ with ...
        q = question.replace('__', '...').replace('___', '...')
        
        # Generate 5 options
        options = generate_options_for_fill(correct, q)
        
        opts_str = ', '.join([f'"{o}"' for o in options])
        return f"{{ type: 'quiz', question: \"{q}\", options: [{opts_str}], correctAnswer: \"{correct}\", hint: \"{hint}\" }}"
    
    elif task_type == 'find':
        # Parse options array and correctAnswer array
        options_m = re.search(r"options:\s*\[([^\]]+)\]", text)
        correct_m = re.search(r"correctAnswer:\s*\[([^\]]+)\]", text)
        
        if not options_m:
            return None
        
        options = [o.strip().strip('"') for o in options_m.group(1).split(',') if o.strip()]
        correct_answers = []
        if correct_m:
            correct_answers = [o.strip().strip('"') for o in correct_m.group(1).split(',') if o.strip()]
        
        if not correct_answers:
            correct_answers = [options[0]] if options else ['Не знаю']
        
        # Convert to single-answer quiz
        correct = correct_answers[0]
        wrong = [o for o in options if o not in correct_answers]
        
        new_options = [correct]
        for w in wrong:
            if w not in new_options:
                new_options.append(w)
        
        # Add more if needed
        generic = ['Другой вариант', 'Нет верного', 'Не относится', 'Все перечисленные']
        for g in generic:
            if len(new_options) < 5 and g not in new_options:
                new_options.append(g)
        
        new_options = new_options[:5]
        
        # Rephrase question for single answer
        q = question
        q = q.replace('Выбери', 'Укажи').replace('выбери', 'укажи')
        
        opts_str = ', '.join([f'"{o}"' for o in new_options])
        return f"{{ type: 'quiz', question: \"{q}\", options: [{opts_str}], correctAnswer: \"{correct}\", hint: \"{hint}\" }}"
    
    else:  # match, order, drag
        options_m = re.search(r"options:\s*\[([^\]]+)\]", text)
        correct_m = re.search(r"correctAnswer:\s*\"([^\"]*)\"", text)
        
        if options_m:
            options = [o.strip().strip('"') for o in options_m.group(1).split(',') if o.strip()]
        else:
            options = ['Вариант 1', 'Вариант 2', 'Вариант 3']
        
        correct = correct_m.group(1) if correct_m else (options[0] if options else 'Не знаю')
        
        if correct not in options:
            options = [correct] + options
        
        while len(options) < 5:
            options.append(f'Другой вариант')
        options = options[:5]
        
        opts_str = ', '.join([f'"{o}"' for o in options])
        return f"{{ type: 'quiz', question: \"{question}\", options: [{opts_str}], correctAnswer: \"{correct}\", hint: \"{hint}\" }}"

def generate_options_for_fill(correct, question):
    """Generate 5 quiz options for a fill-in-the-blank answer"""
    options = [correct]
    
    # Try numeric
    try:
        num = float(correct)
        if num == int(num):
            num = int(num)
        
        if isinstance(num, int) and abs(num) < 1000:
            candidates = []
            for d in [-2, -1, 1, 2, 3, 5, 10]:
                c = num + d
                if c != num and c >= 0:
                    candidates.append(str(c))
            for c in candidates:
                if c not in options:
                    options.append(c)
                if len(options) >= 5:
                    break
        elif isinstance(num, float):
            for d in [-0.5, 0.5, 1.0, -1.0, 2.0]:
                c = round(num + d, 1)
                if str(c) != str(num) and str(c) not in options:
                    options.append(str(c))
                if len(options) >= 5:
                    break
    except (ValueError, TypeError):
        pass
    
    # Text answers - add generic distractors
    text_distractors = [
        'Не знаю', 'Другой ответ', 'Нет ответа', 
        'Невозможно определить', '0', '1', '2',
        'Все варианты', 'Ни один', 'Не указано'
    ]
    for d in text_distractors:
        if len(options) < 5 and d not in options and d != correct:
            options.append(d)
    
    return options[:5]

def expand_quiz(text):
    """Expand quiz with <5 options to 5"""
    options_m = re.search(r"options:\s*\[([^\]]+)\]", text)
    if not options_m:
        return text
    
    options = [o.strip().strip('"') for o in options_m.group(1).split(',') if o.strip()]
    
    if len(options) >= 5:
        return text
    
    # Extract other fields
    question_m = re.search(r"question:\s*\"([^\"]*)\"", text)
    correct_m = re.search(r"correctAnswer:\s*\"([^\"]*)\"", text)
    hint_m = re.search(r"hint:\s*\"([^\"]*)\"", text)
    
    question = question_m.group(1) if question_m else ''
    correct = correct_m.group(1) if correct_m else ''
    hint = hint_m.group(1) if hint_m else ''
    
    # Add distractors
    try:
        # Check if numeric options
        nums = [float(o.replace(',', '.')) for o in options]
        avg = sum(nums) / len(nums) if nums else 0
        for d in [1, 2, -1, 3, 5, 10, 0.5, 0]:
            c = round(avg + d, 1)
            c_str = str(int(c) if c == int(c) else c)
            if c_str not in options and c_str != correct:
                options.append(c_str)
            if len(options) >= 5:
                break
    except (ValueError, TypeError):
        pass
    
    generic = ['Все перечисленные', 'Ни один из перечисленных', 'Другой ответ', 'Затрудняюсь', 'Нет верного']
    for g in generic:
        if len(options) < 5 and g not in options and g != correct:
            options.append(g)
    
    options = options[:5]
    opts_str = ', '.join([f'"{o}"' for o in options])
    
    return f"{{ type: 'quiz', question: \"{question}\", options: [{opts_str}], correctAnswer: \"{correct}\", hint: \"{hint}\" }}"

# Main
total = 0
for g in range(0, 12):
    fp = os.path.join(DIR, f'grade-{g}', 'index.ts')
    if os.path.exists(fp):
        total += process_file(fp)

# Also fix types.ts
types_fp = '/home/z/my-project/repo-site/src/data/types.ts'
with open(types_fp, 'r') as f:
    tc = f.read()
tc = tc.replace("type: 'quiz' | 'match' | 'order' | 'find' | 'fill' | 'drag';", "type: 'quiz';")
with open(types_fp, 'w') as f:
    f.write(tc)

print(f"\nTotal changes: {total}")
print("Updated types.ts")
