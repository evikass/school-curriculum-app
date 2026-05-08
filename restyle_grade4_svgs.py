#!/usr/bin/env python3
"""
Restyle all Grade 4 SVGs from old red-beige cards to subject-specific infographic style.
Each subject gets unique gradient colors and visual identity.
"""
import json
import os
import re
import html

GRADE_DIR = "public/data/grades/4"
IMAGES_DIR = "public/images/lessons/grade4"

# Subject-specific color schemes and visual themes
SUBJECT_THEMES = {
    "art": {
        "name": "Изобразительное искусство",
        "gradient": ["#8E24AA", "#CE93D8"],
        "accent": "#E1BEE7",
        "icon_path": "M30,30 L70,30 L70,70 L30,70 Z M40,20 L60,20 L55,30 L45,30 Z",  # palette
        "pattern": "circles",
    },
    "english": {
        "name": "Иностранный язык",
        "gradient": ["#283593", "#5C6BC0"],
        "accent": "#C5CAE9",
        "icon_path": "M50,25 L30,75 L40,75 L45,60 L55,60 L60,75 L70,75 Z M48,35 L52,50 L47,50 Z",  # A letter
        "pattern": "dots",
    },
    "geography": {
        "name": "География: Россия",
        "gradient": ["#00838F", "#4DD0E1"],
        "accent": "#B2EBF2",
        "icon_path": "M50,20 C65,20 75,35 75,50 C75,65 50,80 50,80 C50,80 25,65 25,50 C25,35 35,20 50,20 Z",  # map pin
        "pattern": "waves",
    },
    "history": {
        "name": "История России",
        "gradient": ["#E65100", "#FFB74D"],
        "accent": "#FFE0B2",
        "icon_path": "M40,75 L40,45 L30,45 L50,20 L70,45 L60,45 L60,75 Z",  # tower/kremlin
        "pattern": "diagonal",
    },
    "informatics": {
        "name": "Информатика",
        "gradient": ["#1A237E", "#42A5F5"],
        "accent": "#BBDEFB",
        "icon_path": "M30,35 L70,35 L70,65 L30,65 Z M45,65 L45,75 L55,75 L55,65 M40,75 L60,75",  # monitor
        "pattern": "grid",
    },
    "literature": {
        "name": "Литературное чтение",
        "gradient": ["#E65100", "#FF8A65"],
        "accent": "#FFCCBC",
        "icon_path": "M35,20 L35,80 L65,80 L65,35 L50,20 Z M50,20 L50,35 L65,35",  # book
        "pattern": "lines",
    },
    "math": {
        "name": "Математика",
        "gradient": ["#1565C0", "#64B5F6"],
        "accent": "#BBDEFB",
        "icon_path": "M50,25 L55,40 L70,40 L58,50 L62,65 L50,55 L38,65 L42,50 L30,40 L45,40 Z",  # star
        "pattern": "numbers",
    },
    "music": {
        "name": "Музыка",
        "gradient": ["#AD1457", "#F48FB1"],
        "accent": "#F8BBD0",
        "icon_path": "M40,70 L40,30 L65,25 L65,65 C65,70 55,75 50,72 C45,69 40,73 40,70 Z",  # note
        "pattern": "notes",
    },
    "nature": {
        "name": "Природоведение",
        "gradient": ["#2E7D32", "#81C784"],
        "accent": "#C8E6C9",
        "icon_path": "M50,75 L50,40 C50,25 65,20 65,35 C65,45 55,40 50,40",  # leaf
        "pattern": "leaves",
    },
    "pe": {
        "name": "Физическая культура",
        "gradient": ["#C62828", "#EF5350"],
        "accent": "#FFCDD2",
        "icon_path": "M50,20 C53,20 55,22 55,25 C55,28 53,30 50,30 C47,30 45,28 45,25 C45,22 47,20 50,20 M35,55 L50,40 L65,55 M50,40 L50,75 M40,60 L60,60",  # person
        "pattern": "dynamic",
    },
    "projects": {
        "name": "Проектная деятельность",
        "gradient": ["#F57F17", "#FFD54F"],
        "accent": "#FFF9C4",
        "icon_path": "M45,25 L55,25 L55,45 L75,45 L75,55 L55,55 L55,75 L45,75 L45,55 L25,55 L25,45 L45,45 Z",  # plus/cross
        "pattern": "bulbs",
    },
    "religion": {
        "name": "Основы религиозных культур",
        "gradient": ["#6A1B9A", "#BA68C8"],
        "accent": "#E1BEE7",
        "icon_path": "M50,25 L50,75 M35,40 L65,40 M40,30 L50,25 L60,30",  # cross
        "pattern": "ornate",
    },
    "russian": {
        "name": "Русский язык",
        "gradient": ["#C62828", "#EF5350"],
        "accent": "#FFCDD2",
        "icon_path": "M35,25 L35,75 M35,25 L55,25 C65,25 65,40 55,40 L35,40 M35,40 L55,40 C65,40 65,55 55,55 L35,55",  # letter Я
        "pattern": "letters",
    },
    "tech": {
        "name": "Технология",
        "gradient": ["#455A64", "#90A4AE"],
        "accent": "#CFD8DC",
        "icon_path": "M40,30 L60,30 L60,50 L55,50 L55,70 L45,70 L45,50 L40,50 Z M45,35 L55,35 M45,42 L55,42",  # wrench
        "pattern": "tools",
    },
    "world": {
        "name": "Окружающий мир",
        "gradient": ["#1B5E20", "#66BB6A"],
        "accent": "#C8E6C9",
        "icon_path": "M50,25 C70,25 80,50 50,80 C20,50 30,25 50,25 M50,25 L50,80 M30,45 L70,45",  # globe
        "pattern": "globe",
    },
}


def generate_infographic_svg(subject_key, lesson_data, lesson_index, total_lessons):
    """Generate a modern infographic-style SVG for a lesson."""
    theme = SUBJECT_THEMES.get(subject_key, SUBJECT_THEMES["math"])
    title = lesson_data.get('title', '').replace(f'Урок {lesson_index}: ', '').strip()
    description = lesson_data.get('description', '')
    facts = lesson_data.get('facts', [])
    tasks = lesson_data.get('tasks', [])
    
    # Clean emoji from title for SVG
    clean_title = re.sub(r'[\U0001F300-\U0001F9FF]', '', title).strip()
    clean_title = clean_title.replace('️', '').strip()
    
    # Truncate for display
    display_title = clean_title[:35] + '...' if len(clean_title) > 35 else clean_title
    display_desc = description[:60] + '...' if len(description) > 60 else description
    
    # Layout variations based on lesson index
    layout_type = lesson_index % 4
    
    grad_start, grad_end = theme["gradient"]
    accent = theme["accent"]
    
    # Build SVG
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">')
    
    # Definitions
    svg_parts.append(f'<defs>')
    svg_parts.append(f'  <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg_parts.append(f'    <stop offset="0%" style="stop-color:{grad_start}"/>')
    svg_parts.append(f'    <stop offset="100%" style="stop-color:{grad_end}"/>')
    svg_parts.append(f'  </linearGradient>')
    svg_parts.append(f'  <linearGradient id="card" x1="0%" y1="0%" x2="0%" y2="100%">')
    svg_parts.append(f'    <stop offset="0%" style="stop-color:rgba(255,255,255,0.95)"/>')
    svg_parts.append(f'    <stop offset="100%" style="stop-color:rgba(255,255,255,0.85)"/>')
    svg_parts.append(f'  </linearGradient>')
    svg_parts.append(f'</defs>')
    
    # Background
    svg_parts.append(f'<rect width="500" height="350" fill="url(#bg)"/>')
    
    # Pattern overlay based on subject
    svg_parts.append(generate_pattern(theme["pattern"], grad_start, grad_end, accent))
    
    # Main card
    card_y = 50
    card_h = 270
    svg_parts.append(f'<rect x="20" y="{card_y}" width="460" height="{card_h}" rx="16" fill="url(#card)" opacity="0.92"/>')
    
    # Subject badge
    svg_parts.append(f'<rect x="30" y="{card_y+10}" width="auto" height="24" rx="12" fill="{grad_start}" opacity="0.9"/>')
    subject_name = theme["name"]
    badge_width = len(subject_name) * 8 + 20
    svg_parts.append(f'<rect x="30" y="{card_y+10}" width="{badge_width}" height="24" rx="12" fill="{grad_start}" opacity="0.9"/>')
    svg_parts.append(f'<text x="{30 + badge_width//2}" y="{card_y+27}" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="white" font-weight="bold">{html.escape(subject_name)}</text>')
    
    # Lesson number
    svg_parts.append(f'<text x="470" y="{card_y+27}" text-anchor="end" font-family="Arial,sans-serif" font-size="11" fill="{grad_start}" font-weight="bold">Урок {lesson_index}</text>')
    
    # Title
    title_y = card_y + 55
    svg_parts.append(f'<text x="40" y="{title_y}" font-family="Arial,sans-serif" font-size="18" fill="#1a1a1a" font-weight="bold">{html.escape(display_title)}</text>')
    
    # Separator line
    svg_parts.append(f'<line x1="40" y1="{title_y+10}" x2="460" y2="{title_y+10}" stroke="{accent}" stroke-width="2"/>')
    
    # Description
    desc_y = title_y + 30
    if display_desc:
        svg_parts.append(f'<text x="40" y="{desc_y}" font-family="Arial,sans-serif" font-size="13" fill="#444">{html.escape(display_desc)}</text>')
    
    # Content area with layout variation
    content_y = desc_y + 20
    
    if layout_type == 0:
        # Layout: Tasks list
        svg_parts.append(generate_tasks_layout(tasks, content_y, grad_start, accent))
    elif layout_type == 1:
        # Layout: Facts cards
        svg_parts.append(generate_facts_layout(facts, content_y, grad_start, accent))
    elif layout_type == 2:
        # Layout: Mixed tasks + facts
        svg_parts.append(generate_mixed_layout(tasks, facts, content_y, grad_start, accent))
    else:
        # Layout: Icon + key points
        svg_parts.append(generate_icon_layout(tasks, content_y, grad_start, accent, theme))
    
    # Decorative corner
    svg_parts.append(f'<circle cx="460" cy="{card_y + card_h - 10}" r="25" fill="{grad_start}" opacity="0.15"/>')
    svg_parts.append(f'<circle cx="460" cy="{card_y + card_h - 10}" r="15" fill="{grad_start}" opacity="0.1"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_pattern(pattern_type, color1, color2, accent):
    """Generate background pattern for visual variety."""
    parts = []
    opacity = "0.08"
    
    if pattern_type == "circles":
        for i in range(5):
            x = 50 + i * 110
            y = 30 + (i % 3) * 120
            parts.append(f'<circle cx="{x}" cy="{y}" r="40" fill="white" opacity="{opacity}"/>')
    elif pattern_type == "dots":
        for i in range(8):
            for j in range(4):
                x = 30 + i * 65
                y = 20 + j * 90
                parts.append(f'<circle cx="{x}" cy="{y}" r="3" fill="white" opacity="{opacity}"/>')
    elif pattern_type == "waves":
        for i in range(3):
            y = 80 + i * 100
            parts.append(f'<path d="M0,{y} Q125,{y-30} 250,{y} Q375,{y+30} 500,{y}" fill="none" stroke="white" stroke-width="2" opacity="{opacity}"/>')
    elif pattern_type == "diagonal":
        for i in range(8):
            x = i * 80 - 50
            parts.append(f'<line x1="{x}" y1="0" x2="{x+200}" y2="350" stroke="white" stroke-width="1.5" opacity="{opacity}"/>')
    elif pattern_type == "grid":
        for i in range(7):
            x = i * 80
            parts.append(f'<line x1="{x}" y1="0" x2="{x}" y2="350" stroke="white" stroke-width="0.5" opacity="{opacity}"/>')
        for i in range(5):
            y = i * 80
            parts.append(f'<line x1="0" y1="{y}" x2="500" y2="{y}" stroke="white" stroke-width="0.5" opacity="{opacity}"/>')
    elif pattern_type == "lines":
        for i in range(12):
            y = 20 + i * 30
            parts.append(f'<line x1="0" y1="{y}" x2="500" y2="{y}" stroke="white" stroke-width="1" opacity="{opacity}"/>')
    elif pattern_type == "numbers":
        nums = ["7", "3", "5", "9", "2", "4", "8", "6"]
        for i, n in enumerate(nums):
            x = 40 + (i % 4) * 120
            y = 50 + (i // 4) * 150
            parts.append(f'<text x="{x}" y="{y}" font-family="Arial" font-size="50" fill="white" opacity="{opacity}" font-weight="bold">{n}</text>')
    elif pattern_type == "notes":
        positions = [(80,40),(200,80),(350,50),(420,120),(150,180),(300,200),(80,260),(450,280)]
        for x, y in positions:
            parts.append(f'<circle cx="{x}" cy="{y}" r="8" fill="white" opacity="{opacity}"/>')
            parts.append(f'<line x1="{x+8}" y1="{y}" x2="{x+8}" y2="{y-30}" stroke="white" stroke-width="1.5" opacity="{opacity}"/>')
    elif pattern_type == "leaves":
        positions = [(60,50),(180,30),(350,70),(440,40),(100,180),(300,160),(60,280),(420,250)]
        for x, y in positions:
            parts.append(f'<ellipse cx="{x}" cy="{y}" rx="15" ry="8" fill="white" opacity="{opacity}" transform="rotate(-30 {x} {y})"/>')
    elif pattern_type == "dynamic":
        for i in range(6):
            y = 30 + i * 60
            x = 20 + (i % 3) * 170
            parts.append(f'<line x1="{x}" y1="{y}" x2="{x+60}" y2="{y}" stroke="white" stroke-width="3" opacity="{opacity}" stroke-linecap="round"/>')
    elif pattern_type == "bulbs":
        for i in range(4):
            x = 80 + i * 120
            y = 60 + (i % 2) * 180
            parts.append(f'<circle cx="{x}" cy="{y}" r="20" fill="white" opacity="{opacity}"/>')
            parts.append(f'<line x1="{x-5}" y1="{y+20}" x2="{x-5}" y2="{y+30}" stroke="white" stroke-width="1.5" opacity="{opacity}"/>')
            parts.append(f'<line x1="{x+5}" y1="{y+20}" x2="{x+5}" y2="{y+30}" stroke="white" stroke-width="1.5" opacity="{opacity}"/>')
    elif pattern_type == "ornate":
        for i in range(5):
            x = 50 + i * 110
            y = 30 + (i % 2) * 280
            parts.append(f'<circle cx="{x}" cy="{y}" r="25" fill="none" stroke="white" stroke-width="1" opacity="{opacity}"/>')
            parts.append(f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="white" stroke-width="0.5" opacity="{opacity}"/>')
    elif pattern_type == "letters":
        letters = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж"]
        for i, l in enumerate(letters):
            x = 30 + (i % 4) * 130
            y = 40 + (i // 4) * 160
            parts.append(f'<text x="{x}" y="{y}" font-family="Arial" font-size="45" fill="white" opacity="{opacity}" font-weight="bold">{l}</text>')
    elif pattern_type == "tools":
        for i in range(6):
            x = 50 + (i % 3) * 180
            y = 40 + (i // 3) * 180
            parts.append(f'<rect x="{x}" y="{y}" width="30" height="6" rx="3" fill="white" opacity="{opacity}" transform="rotate(-45 {x+15} {y+3})"/>')
    elif pattern_type == "globe":
        parts.append(f'<circle cx="400" cy="80" r="50" fill="none" stroke="white" stroke-width="1" opacity="{opacity}"/>')
        parts.append(f'<ellipse cx="400" cy="80" rx="25" ry="50" fill="none" stroke="white" stroke-width="0.5" opacity="{opacity}"/>')
        parts.append(f'<line x1="350" y1="80" x2="450" y2="80" stroke="white" stroke-width="0.5" opacity="{opacity}"/>')
    
    return '\n'.join(parts)


def generate_tasks_layout(tasks, start_y, color, accent):
    """Generate tasks list layout."""
    parts = []
    y = start_y
    
    for i, task in enumerate(tasks[:4]):
        if isinstance(task, str):
            task_text = task
        elif isinstance(task, dict):
            task_text = task.get('question', '')
        else:
            continue
        
        display_text = task_text[:45] + '...' if len(task_text) > 45 else task_text
        display_text = re.sub(r'[\U0001F300-\U0001F9FF]', '', display_text).strip()
        
        # Bullet
        parts.append(f'<circle cx="50" cy="{y + 5}" r="4" fill="{color}"/>')
        parts.append(f'<text x="62" y="{y + 10}" font-family="Arial,sans-serif" font-size="12" fill="#333">{html.escape(display_text)}</text>')
        y += 25
    
    # Add "задания" label
    parts.append(f'<rect x="40" y="{y + 5}" width="70" height="18" rx="9" fill="{color}" opacity="0.15"/>')
    parts.append(f'<text x="75" y="{y + 18}" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="{color}" font-weight="bold">{len(tasks)} заданий</text>')
    
    return '\n'.join(parts)


def generate_facts_layout(facts, start_y, color, accent):
    """Generate facts cards layout."""
    parts = []
    y = start_y
    
    for i, fact in enumerate(facts[:3]):
        if not isinstance(fact, str):
            continue
        clean_fact = re.sub(r'[\U0001F300-\U0001F9FF]', '', fact).strip()
        display_fact = clean_fact[:50] + '...' if len(clean_fact) > 50 else clean_fact
        
        # Fact card
        card_w = 420
        parts.append(f'<rect x="40" y="{y}" width="{card_w}" height="30" rx="6" fill="{color}" opacity="0.08"/>')
        parts.append(f'<text x="50" y="{y + 20}" font-family="Arial,sans-serif" font-size="11" fill="#444">{html.escape(display_fact)}</text>')
        y += 36
    
    return '\n'.join(parts)


def generate_mixed_layout(tasks, facts, start_y, color, accent):
    """Generate mixed tasks + facts layout."""
    parts = []
    y = start_y
    
    # Left column: tasks
    parts.append(f'<text x="40" y="{y}" font-family="Arial,sans-serif" font-size="11" fill="{color}" font-weight="bold">Задания:</text>')
    y += 18
    for i, task in enumerate(tasks[:2]):
        if isinstance(task, str):
            task_text = task
        elif isinstance(task, dict):
            task_text = task.get('question', '')
        else:
            continue
        clean = re.sub(r'[\U0001F300-\U0001F9FF]', '', task_text).strip()
        display = clean[:40] + '...' if len(clean) > 40 else clean
        parts.append(f'<circle cx="48" cy="{y + 4}" r="3" fill="{color}"/>')
        parts.append(f'<text x="58" y="{y + 8}" font-family="Arial,sans-serif" font-size="11" fill="#444">{html.escape(display)}</text>')
        y += 20
    
    # Separator
    y += 5
    parts.append(f'<line x1="40" y1="{y}" x2="460" y2="{y}" stroke="{accent}" stroke-width="1"/>')
    y += 12
    
    # Facts
    parts.append(f'<text x="40" y="{y}" font-family="Arial,sans-serif" font-size="11" fill="{color}" font-weight="bold">Факты:</text>')
    y += 16
    for fact in facts[:2]:
        if not isinstance(fact, str):
            continue
        clean = re.sub(r'[\U0001F300-\U0001F9FF]', '', fact).strip()
        display = clean[:45] + '...' if len(clean) > 45 else clean
        parts.append(f'<text x="50" y="{y}" font-family="Arial,sans-serif" font-size="10" fill="#555">💡 {html.escape(display)}</text>')
        y += 18
    
    return '\n'.join(parts)


def generate_icon_layout(tasks, start_y, color, accent, theme):
    """Generate icon + key points layout."""
    parts = []
    y = start_y
    
    # Key points
    parts.append(f'<text x="40" y="{y}" font-family="Arial,sans-serif" font-size="11" fill="{color}" font-weight="bold">Ключевые темы:</text>')
    y += 20
    
    for i, task in enumerate(tasks[:3]):
        if isinstance(task, str):
            task_text = task
        elif isinstance(task, dict):
            task_text = task.get('question', '')
        else:
            continue
        clean = re.sub(r'[\U0001F300-\U0001F9FF]', '', task_text).strip()
        display = clean[:42] + '...' if len(clean) > 42 else clean
        
        # Numbered bullet
        num = i + 1
        parts.append(f'<circle cx="48" cy="{y}" r="9" fill="{color}" opacity="0.15"/>')
        parts.append(f'<text x="48" y="{y + 4}" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="{color}" font-weight="bold">{num}</text>')
        parts.append(f'<text x="64" y="{y + 4}" font-family="Arial,sans-serif" font-size="11" fill="#444">{html.escape(display)}</text>')
        y += 24
    
    return '\n'.join(parts)


def main():
    subjects = {}
    for f in sorted(os.listdir(GRADE_DIR)):
        if f.endswith('.json') and f != '_bundle.json':
            filepath = os.path.join(GRADE_DIR, f)
            with open(filepath, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            subject_key = f.replace('.json', '')
            subjects[subject_key] = data

    total_generated = 0

    for key, data in sorted(subjects.items()):
        lessons_data = data.get('lessons', data)
        topics = lessons_data.get('detailedTopics', lessons_data.get('topics', []))
        
        subject_dir = os.path.join(IMAGES_DIR, key)
        os.makedirs(subject_dir, exist_ok=True)
        
        lesson_idx = 0
        for topic in topics:
            if not isinstance(topic, dict):
                continue
            for lesson in topic.get('lessons', []):
                lesson_idx += 1
                
                # Determine SVG filename from image path
                image_path = lesson.get('image', '')
                if image_path:
                    filename = os.path.basename(image_path)
                else:
                    filename = f"lesson{lesson_idx}.svg"
                
                # Generate SVG
                svg_content = generate_infographic_svg(key, lesson, lesson_idx, lesson_idx)
                
                # Save
                svg_path = os.path.join(subject_dir, filename)
                with open(svg_path, 'w', encoding='utf-8') as fh:
                    fh.write(svg_content)
                
                total_generated += 1
        
        print(f"  ✅ {key}: {lesson_idx} SVGs restyled")

    print(f"\n{'='*60}")
    print(f"TOTAL: {total_generated} SVGs restyled")


if __name__ == "__main__":
    main()
