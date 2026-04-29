#!/usr/bin/env python3
"""
Check quiz-to-lesson matching with improved title extraction.
Handles both `title: "..."` and `L("title", ...)` patterns.
"""
import re
from pathlib import Path
from collections import defaultdict

GRADES_DIR = Path("/home/z/my-project/school-curriculum-app/src/data/grades")

def strip_lesson_prefix(title):
    if ':' in title:
        return title.split(':')[1].strip()
    return title.strip()

def normalize(title):
    t = title.lower().strip()
    t = re.sub(r'[\U0001F300-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]', '', t)
    return t.strip()

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    parts = content.split('export const games') if 'export const games' in content else content.split('const games')
    # Also try splitting by 'const games' if 'export const games' not found
    if len(parts) < 2:
        parts = content.split('const games')
    lessons_part = parts[0] if len(parts) > 1 else content
    games_part = parts[1] if len(parts) > 1 else ''
    
    # Pattern 1: title: "..." or title: `...`
    pattern1 = r'title:\s*["\x60]([^"\x60]+)["\x60]'
    # Pattern 2: L("title", ...) - helper function
    pattern2 = r'L\(\s*"([^"]+)"'
    # Pattern 3: L(`title`, ...) - helper with backtick
    pattern3 = r'L\(\s*\x60([^\x60]+)\x60'
    # Pattern 4: createLesson("title", ...) helper function
    pattern4 = r'createLesson\(\s*"([^"]+)"'
    
    lesson_titles = set()
    lesson_titles.update(re.findall(pattern1, lessons_part))
    lesson_titles.update(re.findall(pattern2, lessons_part))
    lesson_titles.update(re.findall(pattern3, lessons_part))
    lesson_titles.update(re.findall(pattern4, lessons_part))
    
    game_titles = []
    game_titles.extend(re.findall(pattern1, games_part))
    
    return list(lesson_titles), game_titles

def app_match_logic(lesson_title, game_title):
    lesson_topic = strip_lesson_prefix(lesson_title)
    lesson_topic_lower = normalize(lesson_topic)
    lesson_title_lower = normalize(lesson_title)
    game_name_lower = normalize(game_title)
    
    if game_name_lower == lesson_topic_lower or game_name_lower == lesson_title_lower:
        return True
    if game_name_lower in lesson_topic_lower or lesson_topic_lower in game_name_lower:
        return True
    if game_name_lower in lesson_title_lower or lesson_title_lower in game_name_lower:
        return True
    return False

def check_grade(grade_num):
    grade_dir = GRADES_DIR / str(grade_num)
    if not grade_dir.exists():
        return []
    issues = []
    for subject_dir in sorted(grade_dir.iterdir()):
        if not subject_dir.is_dir():
            continue
        f = subject_dir / "index.ts"
        if not f.exists():
            continue
        subject = subject_dir.name
        lesson_titles, game_titles = parse_file(f)
        
        matched_games = set()
        matched_lessons = set()
        
        for li, lesson_title in enumerate(lesson_titles):
            for gi, game_title in enumerate(game_titles):
                if app_match_logic(lesson_title, game_title):
                    matched_lessons.add(li)
                    matched_games.add(gi)
        
        for gi, game_title in enumerate(game_titles):
            if gi not in matched_games:
                issues.append({
                    'grade': grade_num,
                    'subject': subject,
                    'type': 'unmatched_game',
                    'title': game_title,
                    'lesson_titles': lesson_titles
                })
        
        for li, lesson_title in enumerate(lesson_titles):
            if li not in matched_lessons:
                issues.append({
                    'grade': grade_num,
                    'subject': subject,
                    'type': 'unmatched_lesson',
                    'title': lesson_title,
                    'game_titles': game_titles
                })
    return issues

all_issues = []
for grade in range(12):
    all_issues.extend(check_grade(grade))

unmatched_games = [i for i in all_issues if i['type'] == 'unmatched_game']
unmatched_lessons = [i for i in all_issues if i['type'] == 'unmatched_lesson']

print("=" * 80)
print("QUIZ-LESSON MATCHING CHECK v3")
print("=" * 80)
print(f"\nUnmatched games: {len(unmatched_games)}")
print(f"Unmatched lessons: {len(unmatched_lessons)}")

print(f"\n--- Unmatched lessons by grade ---")
by_grade = defaultdict(list)
for i in unmatched_lessons:
    by_grade[i['grade']].append(i)
for grade in sorted(by_grade.keys()):
    items = by_grade[grade]
    subjects = defaultdict(list)
    for item in items:
        subjects[item['subject']].append(item['title'])
    print(f"\n  Grade {grade}: {len(items)} lessons without games")
    for subj, titles in sorted(subjects.items()):
        print(f"    {subj}: {len(titles)} lessons")
        for t in titles[:5]:
            print(f"      - '{t}'")
        if len(titles) > 5:
            print(f"      ... and {len(titles)-5} more")

print(f"\n--- Unmatched games by grade ---")
by_grade_g = defaultdict(list)
for i in unmatched_games:
    by_grade_g[i['grade']].append(i)
for grade in sorted(by_grade_g.keys()):
    items = by_grade_g[grade]
    subjects = defaultdict(list)
    for item in items:
        subjects[item['subject']].append(item['title'])
    print(f"\n  Grade {grade}: {len(items)} games without lessons")
    for subj, titles in sorted(subjects.items()):
        print(f"    {subj}: {len(titles)} games")
        for t in titles[:3]:
            print(f"      - '{t}'")
        if len(titles) > 3:
            print(f"      ... and {len(titles)-3} more")
