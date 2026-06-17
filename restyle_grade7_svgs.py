#!/usr/bin/env python3
"""
Restyle all grade 7 SVG images with subject-specific color schemes.
- Replace universal red frame (#C62828) with subject primary color
- Replace universal beige background (#FFF8E1/#FFFDE7) with subject background
- Vary corner triangles and decorative elements per subject
- Make each subject visually distinct
"""
import os, re

BASE = "/home/z/school-curriculum-app"
IMG_DIR = f"{BASE}/public/images/lessons/grade7"

# Subject-specific color schemes - each subject gets a unique identity
# primary: frame color, title color, accent elements
# accent: gradient end, secondary decorative
# bg_light: light background gradient start
# bg_dark: light background gradient end
# corner_1/2/3/4: colors for 4 corner triangles
SUBJECT_COLORS = {
    "algebra": {
        "primary": "#1565C0", "accent": "#0D47A1",
        "bg_light": "#E3F2FD", "bg_dark": "#BBDEFB",
        "name": "Алгебра",
        "corners": ["#1565C0", "#0D47A1", "#1976D2", "#42A5F5"],
        "pattern": "grid"  # decorative pattern type
    },
    "art": {
        "primary": "#8E24AA", "accent": "#6A1B9A",
        "bg_light": "#F3E5F5", "bg_dark": "#E1BEE7",
        "name": "Изобразительное искусство",
        "corners": ["#8E24AA", "#AB47BC", "#E91E63", "#F06292"],
        "pattern": "circles"
    },
    "biology": {
        "primary": "#2E7D32", "accent": "#1B5E20",
        "bg_light": "#E8F5E9", "bg_dark": "#C8E6C9",
        "name": "Биология",
        "corners": ["#2E7D32", "#4CAF50", "#8BC34A", "#689F38"],
        "pattern": "organic"
    },
    "chemistry": {
        "primary": "#00796B", "accent": "#004D40",
        "bg_light": "#E0F2F1", "bg_dark": "#B2DFDB",
        "name": "Химия",
        "corners": ["#00796B", "#009688", "#26A69A", "#4DB6AC"],
        "pattern": "hexagons"
    },
    "coding": {
        "primary": "#6A1B9A", "accent": "#4A148C",
        "bg_light": "#EDE7F6", "bg_dark": "#D1C4E9",
        "name": "Основы программирования",
        "corners": ["#6A1B9A", "#7E57C2", "#5C6BC0", "#3F51B5"],
        "pattern": "code"
    },
    "ecology": {
        "primary": "#558B2F", "accent": "#33691E",
        "bg_light": "#F1F8E9", "bg_dark": "#DCEDC8",
        "name": "Экология",
        "corners": ["#558B2F", "#7CB342", "#8BC34A", "#9CCC65"],
        "pattern": "leaves"
    },
    "english": {
        "primary": "#283593", "accent": "#1A237E",
        "bg_light": "#E8EAF6", "bg_dark": "#C5CAE9",
        "name": "Английский язык",
        "corners": ["#283593", "#3F51B5", "#5C6BC0", "#7986CB"],
        "pattern": "waves"
    },
    "geography": {
        "primary": "#00838F", "accent": "#006064",
        "bg_light": "#E0F7FA", "bg_dark": "#B2EBF2",
        "name": "География",
        "corners": ["#00838F", "#0097A7", "#00ACC1", "#26C6DA"],
        "pattern": "globe"
    },
    "geometry": {
        "primary": "#303F9F", "accent": "#1A237E",
        "bg_light": "#E8EAF6", "bg_dark": "#C5CAE9",
        "name": "Геометрия",
        "corners": ["#303F9F", "#3F51B5", "#7986CB", "#9FA8DA"],
        "pattern": "triangles"
    },
    "history": {
        "primary": "#E65100", "accent": "#BF360C",
        "bg_light": "#FFF3E0", "bg_dark": "#FFE0B2",
        "name": "История",
        "corners": ["#E65100", "#F57C00", "#FF9800", "#FFB74D"],
        "pattern": "scroll"
    },
    "informatics": {
        "primary": "#1A237E", "accent": "#0D47A1",
        "bg_light": "#E8EAF6", "bg_dark": "#C5CAE9",
        "name": "Информатика",
        "corners": ["#1A237E", "#283593", "#3949AB", "#5C6BC0"],
        "pattern": "circuit"
    },
    "literature": {
        "primary": "#5D4037", "accent": "#3E2723",
        "bg_light": "#EFEBE9", "bg_dark": "#D7CCC8",
        "name": "Литература",
        "corners": ["#5D4037", "#795548", "#8D6E63", "#A1887F"],
        "pattern": "book"
    },
    "music": {
        "primary": "#AD1457", "accent": "#880E4F",
        "bg_light": "#FCE4EC", "bg_dark": "#F8BBD0",
        "name": "Музыка",
        "corners": ["#AD1457", "#E91E63", "#EC407A", "#F48FB1"],
        "pattern": "notes"
    },
    "pe": {
        "primary": "#EF6C00", "accent": "#E65100",
        "bg_light": "#FFF3E0", "bg_dark": "#FFE0B2",
        "name": "Физическая культура",
        "corners": ["#EF6C00", "#FF9800", "#FFA726", "#FFB74D"],
        "pattern": "motion"
    },
    "physics": {
        "primary": "#C62828", "accent": "#B71C1C",
        "bg_light": "#FFEBEE", "bg_dark": "#FFCDD2",
        "name": "Физика",
        "corners": ["#C62828", "#D32F2F", "#E53935", "#EF5350"],
        "pattern": "atom"
    },
    "robotics": {
        "primary": "#37474F", "accent": "#263238",
        "bg_light": "#ECEFF1", "bg_dark": "#CFD8DC",
        "name": "Робототехника",
        "corners": ["#37474F", "#546E7A", "#607D8B", "#78909C"],
        "pattern": "gears"
    },
    "russian": {
        "primary": "#D32F2F", "accent": "#C62828",
        "bg_light": "#FFEBEE", "bg_dark": "#FFCDD2",
        "name": "Русский язык",
        "corners": ["#D32F2F", "#E53935", "#EF5350", "#EF9A9A"],
        "pattern": "text"
    },
    "safety": {
        "primary": "#F57F17", "accent": "#F9A825",
        "bg_light": "#FFFDE7", "bg_dark": "#FFF9C4",
        "name": "ОБЖ",
        "corners": ["#F57F17", "#FBC02D", "#FFEB3B", "#FFF176"],
        "pattern": "shield"
    },
    "social": {
        "primary": "#0277BD", "accent": "#01579B",
        "bg_light": "#E1F5FE", "bg_dark": "#B3E5FC",
        "name": "Обществознание",
        "corners": ["#0277BD", "#0288D1", "#039BE5", "#29B6F6"],
        "pattern": "columns"
    },
    "tech": {
        "primary": "#455A64", "accent": "#37474F",
        "bg_light": "#ECEFF1", "bg_dark": "#CFD8DC",
        "name": "Технология",
        "corners": ["#455A64", "#546E7A", "#78909C", "#90A4AE"],
        "pattern": "tools"
    },
}


def get_subject_decorative(subject, colors):
    """Generate subject-specific decorative elements for the illustration area."""
    primary = colors["primary"]
    accent = colors["accent"]
    pattern = colors["pattern"]
    corners = colors["corners"]
    
    if pattern == "grid":
        # Algebra: coordinate grid lines
        return f'''<line x1="430" y1="100" x2="480" y2="100" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
  <line x1="430" y1="120" x2="480" y2="120" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
  <line x1="430" y1="140" x2="480" y2="140" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
  <line x1="445" y1="90" x2="445" y2="150" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
  <line x1="460" y1="90" x2="460" y2="150" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>'''
    
    elif pattern == "circles":
        # Art: overlapping circles
        return f'''<circle cx="450" cy="120" r="25" fill="{corners[0]}" opacity="0.08"/>
  <circle cx="465" cy="135" r="20" fill="{corners[2]}" opacity="0.08"/>
  <circle cx="440" cy="135" r="15" fill="{corners[3]}" opacity="0.08"/>'''
    
    elif pattern == "organic":
        # Biology: organic shapes
        return f'''<ellipse cx="450" cy="125" rx="20" ry="15" fill="{primary}" opacity="0.08"/>
  <circle cx="460" cy="140" r="8" fill="{corners[2]}" opacity="0.06"/>
  <circle cx="440" cy="140" r="6" fill="{corners[3]}" opacity="0.06"/>'''
    
    elif pattern == "hexagons":
        # Chemistry: hexagonal shapes
        return f'''<polygon points="450,110 460,115 460,125 450,130 440,125 440,115" fill="none" stroke="{primary}" stroke-width="1" opacity="0.12"/>
  <polygon points="468,125 478,130 478,140 468,145 458,140 458,130" fill="none" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>'''
    
    elif pattern == "code":
        # Coding: code brackets
        return f'''<text x="435" y="125" font-family="monospace" font-size="18" fill="{primary}" opacity="0.12">&lt;/&gt;</text>
  <rect x="440" y="135" width="30" height="4" rx="1" fill="{corners[2]}" opacity="0.1"/>
  <rect x="435" y="145" width="25" height="4" rx="1" fill="{corners[3]}" opacity="0.08"/>'''
    
    elif pattern == "leaves":
        # Ecology: leaf shapes
        return f'''<ellipse cx="450" cy="120" rx="12" ry="18" fill="{primary}" opacity="0.1" transform="rotate(-30,450,120)"/>
  <line x1="450" y1="105" x2="450" y2="140" stroke="{corners[2]}" stroke-width="0.5" opacity="0.15"/>
  <ellipse cx="462" cy="135" rx="8" ry="12" fill="{corners[3]}" opacity="0.08" transform="rotate(20,462,135)"/>'''
    
    elif pattern == "waves":
        # English: wave patterns
        return f'''<path d="M430,120 Q445,110 460,120 Q475,130 490,120" fill="none" stroke="{primary}" stroke-width="1" opacity="0.12"/>
  <path d="M430,135 Q445,125 460,135 Q475,145 490,135" fill="none" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>'''
    
    elif pattern == "globe":
        # Geography: globe/meridian lines
        return f'''<circle cx="455" cy="125" r="20" fill="none" stroke="{primary}" stroke-width="1" opacity="0.1"/>
  <ellipse cx="455" cy="125" rx="20" ry="8" fill="none" stroke="{corners[2]}" stroke-width="0.8" opacity="0.1"/>
  <line x1="455" y1="105" x2="455" y2="145" stroke="{corners[3]}" stroke-width="0.8" opacity="0.1"/>'''
    
    elif pattern == "triangles":
        # Geometry: triangle shapes
        return f'''<polygon points="445,105 465,145 425,145" fill="none" stroke="{primary}" stroke-width="1" opacity="0.12"/>
  <polygon points="470,110 485,140 455,140" fill="none" stroke="{corners[2]}" stroke-width="0.8" opacity="0.1"/>'''
    
    elif pattern == "scroll":
        # History: scroll/column shapes
        return f'''<rect x="440" y="105" width="12" height="40" rx="3" fill="{primary}" opacity="0.1"/>
  <rect x="458" y="110" width="12" height="35" rx="3" fill="{corners[2]}" opacity="0.08"/>
  <rect x="476" y="108" width="8" height="30" rx="2" fill="{corners[3]}" opacity="0.06"/>'''
    
    elif pattern == "circuit":
        # Informatics: circuit paths
        return f'''<line x1="430" y1="120" x2="450" y2="120" stroke="{primary}" stroke-width="1" opacity="0.12"/>
  <circle cx="450" cy="120" r="3" fill="{primary}" opacity="0.12"/>
  <line x1="450" y1="120" x2="450" y2="140" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>
  <circle cx="450" cy="140" r="3" fill="{corners[2]}" opacity="0.1"/>
  <line x1="450" y1="140" x2="475" y2="140" stroke="{corners[3]}" stroke-width="1" opacity="0.08"/>'''
    
    elif pattern == "book":
        # Literature: book shapes
        return f'''<rect x="435" y="108" width="25" height="35" rx="2" fill="{primary}" opacity="0.08"/>
  <line x1="447" y1="108" x2="447" y2="143" stroke="{corners[2]}" stroke-width="0.8" opacity="0.12"/>
  <rect x="438" y="112" width="8" height="2" fill="{corners[3]}" opacity="0.1"/>
  <rect x="438" y="118" width="8" height="2" fill="{corners[3]}" opacity="0.1"/>'''
    
    elif pattern == "notes":
        # Music: music notes
        return f'''<circle cx="445" cy="130" r="5" fill="{primary}" opacity="0.12"/>
  <line x1="450" y1="130" x2="450" y2="105" stroke="{primary}" stroke-width="1" opacity="0.12"/>
  <circle cx="465" cy="125" r="5" fill="{corners[2]}" opacity="0.1"/>
  <line x1="470" y1="125" x2="470" y2="100" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>'''
    
    elif pattern == "motion":
        # PE: motion lines
        return f'''<line x1="435" y1="120" x2="475" y2="120" stroke="{primary}" stroke-width="2" opacity="0.1"/>
  <line x1="440" y1="130" x2="480" y2="130" stroke="{corners[2]}" stroke-width="1.5" opacity="0.08"/>
  <circle cx="480" cy="120" r="4" fill="{corners[3]}" opacity="0.1"/>'''
    
    elif pattern == "atom":
        # Physics: atom orbits
        return f'''<circle cx="455" cy="125" r="4" fill="{primary}" opacity="0.15"/>
  <ellipse cx="455" cy="125" rx="20" ry="8" fill="none" stroke="{primary}" stroke-width="0.8" opacity="0.1"/>
  <ellipse cx="455" cy="125" rx="20" ry="8" fill="none" stroke="{corners[2]}" stroke-width="0.8" opacity="0.1" transform="rotate(60,455,125)"/>
  <ellipse cx="455" cy="125" rx="20" ry="8" fill="none" stroke="{corners[3]}" stroke-width="0.8" opacity="0.1" transform="rotate(-60,455,125)"/>'''
    
    elif pattern == "gears":
        # Robotics: gear shapes
        return f'''<circle cx="450" cy="120" r="12" fill="none" stroke="{primary}" stroke-width="1" opacity="0.12"/>
  <circle cx="450" cy="120" r="5" fill="none" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>
  <circle cx="470" cy="138" r="8" fill="none" stroke="{corners[3]}" stroke-width="0.8" opacity="0.1"/>
  <circle cx="470" cy="138" r="3" fill="none" stroke="{corners[3]}" stroke-width="0.8" opacity="0.08"/>'''
    
    elif pattern == "text":
        # Russian: text/calligraphy shapes
        return f'''<text x="435" y="130" font-family="serif" font-size="24" fill="{primary}" opacity="0.1">Аа</text>
  <line x1="435" y1="140" x2="475" y2="140" stroke="{corners[2]}" stroke-width="1" opacity="0.08"/>'''
    
    elif pattern == "shield":
        # Safety: shield shape
        return f'''<path d="M455,105 L470,112 L470,130 L455,140 L440,130 L440,112 Z" fill="none" stroke="{primary}" stroke-width="1" opacity="0.12"/>
  <text x="455" y="128" font-family="Arial" font-size="14" fill="{primary}" opacity="0.1" text-anchor="middle">!</text>'''
    
    elif pattern == "columns":
        # Social studies: building columns
        return f'''<rect x="440" y="120" width="6" height="30" fill="{primary}" opacity="0.1"/>
  <rect x="452" y="120" width="6" height="30" fill="{corners[2]}" opacity="0.08"/>
  <rect x="464" y="120" width="6" height="30" fill="{corners[3]}" opacity="0.06"/>
  <rect x="435" y="115" width="42" height="4" fill="{primary}" opacity="0.1"/>'''
    
    elif pattern == "tools":
        # Technology: tool shapes
        return f'''<rect x="440" y="110" width="4" height="30" fill="{primary}" opacity="0.1" transform="rotate(30,442,125)"/>
  <circle cx="435" cy="108" r="6" fill="none" stroke="{primary}" stroke-width="1.5" opacity="0.1"/>
  <rect x="460" y="115" width="4" height="25" fill="{corners[2]}" opacity="0.08" transform="rotate(-20,462,128)"/>'''
    
    return ""


def restyle_svg(content, subject, colors):
    """Restyle an SVG with subject-specific colors."""
    primary = colors["primary"]
    accent = colors["accent"]
    bg_light = colors["bg_light"]
    bg_dark = colors["bg_dark"]
    corners = colors["corners"]
    subj_name = colors["name"]
    
    # 1. Replace background gradient
    content = re.sub(
        r'stop-color="#FFF8E1"',
        f'stop-color="{bg_light}"',
        content
    )
    content = re.sub(
        r'stop-color="#FFFDE7"',
        f'stop-color="{bg_dark}"',
        content
    )
    
    # 2. Replace frame colors - but ONLY in template parts
    # The outer frame (stroke="#C62828" stroke-width="3")
    # The inner frame (stroke="#C62828" stroke-width="1" opacity="0.3")
    # These are always in the first ~15 lines of the SVG
    
    lines = content.split('\n')
    new_lines = []
    in_template = True
    template_line_count = 0
    
    for line in lines:
        template_line_count += 1
        
        # Template part: first ~22 lines (before the illustration area)
        if template_line_count <= 22:
            # Replace frame strokes
            line = line.replace('stroke="#C62828"', f'stroke="{primary}"')
            # Replace corner triangles
            line = re.sub(r'fill="#C62828"', f'fill="{corners[0]}"', line, count=1)
            line = re.sub(r'fill="#C62828"', f'fill="{corners[0]}"', line)
            # Replace corner triangle colors with subject-specific
            line = line.replace('fill="#1565C0"', f'fill="{corners[1]}"')
            line = line.replace('fill="#F9A825"', f'fill="{corners[2]}"')
            line = line.replace('fill="#2E7D32"', f'fill="{corners[3]}"')
            # Replace title fill color
            line = re.sub(r'fill="#C62828" text-anchor="middle"', f'fill="{primary}" text-anchor="middle"', line)
            # Replace divider line stroke
            line = re.sub(r'stroke="#C62828" stroke-width="2" opacity="0.25"', f'stroke="{primary}" stroke-width="2" opacity="0.25"', line)
            # Replace accent bar fills
            line = re.sub(r'fill="#C62828" opacity="0.15"', f'fill="{primary}" opacity="0.15"', line)
            line = re.sub(r'fill="#1565C0" opacity="0.12"', f'fill="{corners[1]}" opacity="0.12"', line)
            # Replace circle fills
            # circles at top use #C62828, #1565C0, #F9A825 - replace with subject colors
            # Already handled above with fill="#C62828" -> corners[0] and fill="#1565C0" -> corners[1]
            line = line.replace('fill="#F9A825"', f'fill="{corners[2]}"')
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # 3. Replace bottom panel
    # Old: <rect ... fill="#C62828" opacity="0.85"/> or similar patterns
    # Also: <rect ... fill="url(#panel)"/> patterns
    content = re.sub(
        r'fill="#C62828" opacity="0\.85"',
        f'fill="{primary}" opacity="0.85"',
        content
    )
    content = re.sub(
        r'fill="#C62828"/>',
        f'fill="{primary}"/>',
        content
    )
    
    # Also handle gradient-based bottom panels
    content = re.sub(
        r'(<linearGradient id="panel"[^>]*>.*?<stop offset="0%"[^>]*stop-color=")([^"]+)(".*?<stop offset="100%"[^>]*stop-color=")([^"]+)(")',
        lambda m: f'{m.group(1)}{accent}{m.group(3)}{primary}{m.group(5)}',
        content,
        flags=re.DOTALL
    )
    
    # 4. Add subject-specific decorative elements
    # Insert before the closing </svg> tag
    decorative = get_subject_decorative(subject, colors)
    if decorative and '</svg>' in content:
        content = content.replace('</svg>', f'  {decorative}\n</svg>')
    
    return content


def main():
    total_restyled = 0
    subjects_processed = 0
    
    for subject in sorted(os.listdir(IMG_DIR)):
        subj_dir = os.path.join(IMG_DIR, subject)
        if not os.path.isdir(subj_dir):
            continue
        
        colors = SUBJECT_COLORS.get(subject)
        if not colors:
            print(f"  SKIP {subject}: no color scheme defined")
            continue
        
        svg_files = [f for f in os.listdir(subj_dir) if f.endswith('.svg')]
        if not svg_files:
            continue
        
        subjects_processed += 1
        subj_count = 0
        
        for svg_file in sorted(svg_files):
            path = os.path.join(subj_dir, svg_file)
            with open(path, 'r') as f:
                content = f.read()
            
            # Check if this SVG needs restyling (has the old red frame)
            if '#C62828' not in content and '#FFF8E1' not in content:
                continue
            
            # Restyle
            new_content = restyle_svg(content, subject, colors)
            
            with open(path, 'w') as f:
                f.write(new_content)
            
            subj_count += 1
            total_restyled += 1
        
        print(f"  {subject:15s}: {subj_count} SVGs restyled ({colors['primary']} frame)")
    
    print(f"\nTotal: {total_restyled} SVGs restyled across {subjects_processed} subjects")


if __name__ == "__main__":
    main()
