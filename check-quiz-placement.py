#!/usr/bin/env python3
import re, os
from pathlib import Path

GRADES_DIR = Path("/home/z/my-project/school-curriculum-app/src/data/grades")

def normalize_title(title):
    t = re.sub(r'[\U0001F300-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]', '', title)
    t = re.sub(r'[^\w\s]', '', t)
    return t.strip().lower()

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

def titles_match(lt, gt):
    nl = normalize_title(lt)
    ng = normalize_title(gt)
    if nl == ng:
        return True
    nl2 = re.sub(r'^урок\s*\d+\s*[:.]?\s*', '', nl, flags=re.IGNORECASE).strip()
    ng2 = re.sub(r'^урок\s*\d+\s*[:.]?\s*', '', ng, flags=re.IGNORECASE).strip()
    if nl2 == ng2:
        return True
    if len(nl) > 5 and len(ng) > 5:
        if ng in nl or nl in ng:
            return True
        if ng2 in nl2 or nl2 in ng2:
            return True
    return False

for grade in range(12):
    grade_dir = GRADES_DIR / str(grade)
    if not grade_dir.exists():
        continue
    for subject_dir in sorted(grade_dir.iterdir()):
        if not subject_dir.is_dir():
            continue
        f = subject_dir / 'index.ts'
        if not f.exists():
            continue
        lt, gt = parse_file(f)
        if not lt and not gt:
            continue
        subject = subject_dir.name
        
        matched_l = set()
        for gi, g in enumerate(gt):
            found = False
            for li, l in enumerate(lt):
                if titles_match(l, g):
                    found = True
                    matched_l.add(li)
                    break
            if not found:
                print(f'G_NO_LESSON | {grade} | {subject} | Game="{g}"')
        
        for li, l in enumerate(lt):
            if li in matched_l:
                continue
            found = False
            for g in gt:
                if titles_match(l, g):
                    found = True
                    break
            if not found:
                print(f'L_NO_GAME | {grade} | {subject} | Lesson="{l}"')
