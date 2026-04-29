#!/usr/bin/env python3
"""
Check quiz-to-lesson matching using the SAME logic as the app's LessonViewer.tsx startQuiz function.
The app strips "Урок N:" prefix and then does exact match, then substring match.
"""
import re
from pathlib import Path
from collections import defaultdict

GRADES_DIR = Path("/home/z/my-project/school-curriculum-app/src/data/grades")

def strip_lesson_prefix(title):
    """Same logic as app: lessonTitle.split(':')[1].trim() if ':' present"""
    if ':' in title:
        return title.split(':')[1].strip()
    return title.strip()

def normalize(title):
    """Normalize for comparison"""
    t = title.lower().strip()
    # Remove emoji
    t = re.sub(r'[\U0001F300-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]', '', t)
    return t.strip()

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    parts = content.split('export const games')
    lessons_part = parts[0] if len(parts) > 1 else content
    games_part = parts[1] if len(parts) > 1 else ''
    pattern = r'''title:\s*["\x60]([^"\x60]+)["\x60]'''
    lesson_titles = re.findall(pattern, lessons_part)
    game_titles = re.findall(pattern, games_part)
    return lesson_titles, game_titles

def app_match_logic(lesson_title, game_title):
    """
    Mimic the app's startQuiz matching logic:
    1. Strip "Урок N:" from lesson title
    2. Exact match on topic or full title
    3. Substring match
    """
    lesson_topic = strip_lesson_prefix(lesson_title)
    lesson_topic_lower = normalize(lesson_topic)
    lesson_title_lower = normalize(lesson_title)
    game_name_lower = normalize(game_title)
    
    # 1. Exact match
    if game_name_lower == lesson_topic_lower or game_name_lower == lesson_title_lower:
        return True
    
    # 2. Substring match (like the app does)
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
        
        # Filter out subject-name-only lessons (like "Математика", "Биология")
        real_lessons = [lt for lt in lesson_titles if strip_lesson_prefix(lt) != lt or ':' not in lt]
        # Actually, keep all but skip the first one if it matches subject name exactly
        
        matched_games = set()
        matched_lessons = set()
        
        # Try to match each lesson with a game
        for li, lesson_title in enumerate(lesson_titles):
            for gi, game_title in enumerate(game_titles):
                if app_match_logic(lesson_title, game_title):
                    matched_lessons.add(li)
                    matched_games.add(gi)
        
        # Games that no lesson matches
        for gi, game_title in enumerate(game_titles):
            if gi not in matched_games:
                issues.append({
                    'grade': grade_num,
                    'subject': subject,
                    'type': 'unmatched_game',
                    'title': game_title,
                    'lesson_titles': lesson_titles
                })
        
        # Lessons that no game matches
        for li, lesson_title in enumerate(lesson_titles):
            # Skip subject-name lessons (first lesson that matches the subject)
            if li not in matched_lessons:
                issues.append({
                    'grade': grade_num,
                    'subject': subject,
                    'type': 'unmatched_lesson',
                    'title': lesson_title,
                    'game_titles': game_titles
                })
    
    return issues

# Run check
all_issues = []
for grade in range(12):
    all_issues.extend(check_grade(grade))

# Separate by type
unmatched_games = [i for i in all_issues if i['type'] == 'unmatched_game']
unmatched_lessons = [i for i in all_issues if i['type'] == 'unmatched_lesson']

print("=" * 80)
print("QUIZ-LESSON MATCHING CHECK (using app's matching logic)")
print("=" * 80)
print(f"\nUnmatched games (no lesson finds this game): {len(unmatched_games)}")
print(f"Unmatched lessons (no game found for this lesson): {len(unmatched_lessons)}")

# Group by grade
print(f"\n--- Unmatched lessons by grade ---")
by_grade = defaultdict(list)
for i in unmatched_lessons:
    by_grade[i['grade']].append(i)
for grade in sorted(by_grade.keys()):
    items = by_grade[grade]
    subjects = set(i['subject'] for i in items)
    print(f"  Grade {grade}: {len(items)} lessons without games across {len(subjects)} subjects")
    for item in items[:10]:
        print(f"    {item['subject']}: '{item['title']}'")
    if len(items) > 10:
        print(f"    ... and {len(items) - 10} more")

print(f"\n--- Unmatched games by grade ---")
by_grade_g = defaultdict(list)
for i in unmatched_games:
    by_grade_g[i['grade']].append(i)
for grade in sorted(by_grade_g.keys()):
    items = by_grade_g[grade]
    subjects = set(i['subject'] for i in items)
    print(f"  Grade {grade}: {len(items)} games without lessons across {len(subjects)} subjects")
    for item in items[:10]:
        print(f"    {item['subject']}: '{item['title']}'")
    if len(items) > 10:
        print(f"    ... and {len(items) - 10} more")
