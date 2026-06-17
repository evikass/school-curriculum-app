#!/usr/bin/env python3
"""
Restyle all grade 5 SVG images with subject-specific color schemes.
- Replace universal red frame (#C62828) with subject primary color
- Replace universal cream background (#FFFDE7) with subject gradient background
- Replace star decorations with subject-specific decorative elements
- Make each subject visually distinct

Already-styled subjects (skip): biology, literature, pe
Targets: art, crafts, digital, english, finance, geography, history,
         informatics, math, music, robotics, russian, safety, tech
"""
import os, re

BASE = "/home/z/school-curriculum-app"
IMG_DIR = f"{BASE}/public/images/lessons/grade5"

# Skip subjects that are already styled with gradients
SKIP_SUBJECTS = {"biology", "literature", "pe"}

# Subject-specific color schemes — each subject gets a unique visual identity
SUBJECT_COLORS = {
    "math": {
        "primary": "#1565C0", "accent": "#0D47A1",
        "bg_light": "#E3F2FD", "bg_dark": "#BBDEFB",
        "name": "Математика",
        "corners": ["#1565C0", "#0D47A1", "#1976D2", "#42A5F5"],
        "pattern": "grid",
        "icon": "📐"
    },
    "art": {
        "primary": "#8E24AA", "accent": "#6A1B9A",
        "bg_light": "#F3E5F5", "bg_dark": "#E1BEE7",
        "name": "Изобразительное искусство",
        "corners": ["#8E24AA", "#AB47BC", "#E91E63", "#F06292"],
        "pattern": "circles",
        "icon": "🎨"
    },
    "crafts": {
        "primary": "#6D4C41", "accent": "#4E342E",
        "bg_light": "#EFEBE9", "bg_dark": "#D7CCC8",
        "name": "Художественные ремёсла",
        "corners": ["#6D4C41", "#8D6E63", "#A1887F", "#BCAAA4"],
        "pattern": "weave",
        "icon": "🧶"
    },
    "digital": {
        "primary": "#00838F", "accent": "#006064",
        "bg_light": "#E0F7FA", "bg_dark": "#B2EBF2",
        "name": "Цифровая грамотность",
        "corners": ["#00838F", "#0097A7", "#00ACC1", "#26C6DA"],
        "pattern": "circuit",
        "icon": "💻"
    },
    "english": {
        "primary": "#283593", "accent": "#1A237E",
        "bg_light": "#E8EAF6", "bg_dark": "#C5CAE9",
        "name": "Английский язык",
        "corners": ["#283593", "#3F51B5", "#5C6BC0", "#7986CB"],
        "pattern": "waves",
        "icon": "🇬🇧"
    },
    "finance": {
        "primary": "#2E7D32", "accent": "#1B5E20",
        "bg_light": "#E8F5E9", "bg_dark": "#C8E6C9",
        "name": "Финансовая грамотность",
        "corners": ["#2E7D32", "#4CAF50", "#66BB6A", "#81C784"],
        "pattern": "coins",
        "icon": "💰"
    },
    "geography": {
        "primary": "#00838F", "accent": "#006064",
        "bg_light": "#E0F7FA", "bg_dark": "#B2EBF2",
        "name": "География",
        "corners": ["#00838F", "#0097A7", "#00ACC1", "#26C6DA"],
        "pattern": "globe",
        "icon": "🌍"
    },
    "history": {
        "primary": "#E65100", "accent": "#BF360C",
        "bg_light": "#FFF3E0", "bg_dark": "#FFE0B2",
        "name": "История",
        "corners": ["#E65100", "#F57C00", "#FF9800", "#FFB74D"],
        "pattern": "scroll",
        "icon": "📜"
    },
    "informatics": {
        "primary": "#1A237E", "accent": "#0D47A1",
        "bg_light": "#E8EAF6", "bg_dark": "#C5CAE9",
        "name": "Информатика",
        "corners": ["#1A237E", "#283593", "#3949AB", "#5C6BC0"],
        "pattern": "binary",
        "icon": "🖥️"
    },
    "music": {
        "primary": "#AD1457", "accent": "#880E4F",
        "bg_light": "#FCE4EC", "bg_dark": "#F8BBD0",
        "name": "Музыка",
        "corners": ["#AD1457", "#E91E63", "#EC407A", "#F48FB1"],
        "pattern": "notes",
        "icon": "🎵"
    },
    "robotics": {
        "primary": "#37474F", "accent": "#263238",
        "bg_light": "#ECEFF1", "bg_dark": "#CFD8DC",
        "name": "Робототехника",
        "corners": ["#37474F", "#546E7A", "#607D8B", "#78909C"],
        "pattern": "gears",
        "icon": "🤖"
    },
    "russian": {
        "primary": "#D32F2F", "accent": "#C62828",
        "bg_light": "#FFEBEE", "bg_dark": "#FFCDD2",
        "name": "Русский язык",
        "corners": ["#D32F2F", "#E53935", "#EF5350", "#EF9A9A"],
        "pattern": "text",
        "icon": "✍️"
    },
    "safety": {
        "primary": "#F57F17", "accent": "#F9A825",
        "bg_light": "#FFFDE7", "bg_dark": "#FFF9C4",
        "name": "ОБЖ",
        "corners": ["#F57F17", "#FBC02D", "#FFEB3B", "#FFF176"],
        "pattern": "shield",
        "icon": "🛡️"
    },
    "tech": {
        "primary": "#455A64", "accent": "#37474F",
        "bg_light": "#ECEFF1", "bg_dark": "#CFD8DC",
        "name": "Технология",
        "corners": ["#455A64", "#546E7A", "#78909C", "#90A4AE"],
        "pattern": "tools",
        "icon": "🔧"
    },
}


def get_subject_decorative(subject, colors):
    """Generate subject-specific decorative elements to replace stars/rays."""
    primary = colors["primary"]
    accent = colors["accent"]
    pattern = colors["pattern"]
    corners = colors["corners"]

    if pattern == "grid":
        # Math: grid pattern + equals sign
        return f'''    <!-- Math: grid pattern -->
    <line x1="430" y1="100" x2="480" y2="100" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
    <line x1="430" y1="115" x2="480" y2="115" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
    <line x1="430" y1="130" x2="480" y2="130" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
    <line x1="430" y1="145" x2="480" y2="145" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
    <line x1="445" y1="92" x2="445" y2="150" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
    <line x1="460" y1="92" x2="460" y2="150" stroke="{primary}" stroke-width="0.5" opacity="0.15"/>
    <text x="20" y="335" font-family="Arial" font-size="28" fill="{corners[2]}" opacity="0.08">=</text>'''

    elif pattern == "circles":
        # Art: overlapping circles
        return f'''    <!-- Art: circles -->
    <circle cx="450" cy="120" r="25" fill="none" stroke="{corners[0]}" stroke-width="1.5" opacity="0.12"/>
    <circle cx="465" cy="135" r="20" fill="none" stroke="{corners[2]}" stroke-width="1.5" opacity="0.1"/>
    <circle cx="440" cy="135" r="15" fill="none" stroke="{corners[3]}" stroke-width="1.5" opacity="0.08"/>
    <circle cx="455" cy="108" r="8" fill="{primary}" opacity="0.06"/>'''

    elif pattern == "weave":
        # Crafts: cross-hatch weave
        return f'''    <!-- Crafts: weave -->
    <line x1="435" y1="100" x2="480" y2="145" stroke="{primary}" stroke-width="1" opacity="0.1"/>
    <line x1="480" y1="100" x2="435" y2="145" stroke="{corners[2]}" stroke-width="1" opacity="0.08"/>
    <line x1="458" y1="95" x2="458" y2="150" stroke="{corners[3]}" stroke-width="0.5" opacity="0.1"/>
    <line x1="430" y1="122" x2="485" y2="122" stroke="{primary}" stroke-width="0.5" opacity="0.08"/>'''

    elif pattern == "circuit":
        # Digital: circuit board traces
        return f'''    <!-- Digital: circuit -->
    <line x1="435" y1="110" x2="455" y2="110" stroke="{primary}" stroke-width="1.5" opacity="0.12"/>
    <circle cx="455" cy="110" r="3" fill="{primary}" opacity="0.15"/>
    <line x1="455" y1="110" x2="455" y2="130" stroke="{corners[2]}" stroke-width="1.5" opacity="0.1"/>
    <circle cx="455" cy="130" r="3" fill="{corners[2]}" opacity="0.12"/>
    <line x1="455" y1="130" x2="480" y2="130" stroke="{corners[3]}" stroke-width="1.5" opacity="0.08"/>
    <circle cx="480" cy="130" r="2.5" fill="{corners[3]}" opacity="0.1"/>'''

    elif pattern == "waves":
        # English: sound/waves
        return f'''    <!-- English: waves -->
    <path d="M430,115 Q445,105 460,115 Q475,125 490,115" fill="none" stroke="{primary}" stroke-width="1.5" opacity="0.12"/>
    <path d="M430,132 Q445,122 460,132 Q475,142 490,132" fill="none" stroke="{corners[2]}" stroke-width="1.5" opacity="0.1"/>
    <path d="M430,148 Q445,140 460,148 Q475,156 490,148" fill="none" stroke="{corners[3]}" stroke-width="1" opacity="0.07"/>'''

    elif pattern == "coins":
        # Finance: stacked coins
        return f'''    <!-- Finance: coins -->
    <circle cx="455" cy="130" r="12" fill="none" stroke="{primary}" stroke-width="1.5" opacity="0.12"/>
    <text x="455" y="135" font-family="Arial" font-size="12" fill="{primary}" opacity="0.15" text-anchor="middle">$</text>
    <ellipse cx="455" cy="118" rx="12" ry="4" fill="none" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>
    <ellipse cx="455" cy="112" rx="12" ry="4" fill="none" stroke="{corners[3]}" stroke-width="1" opacity="0.08"/>'''

    elif pattern == "globe":
        # Geography: globe with meridians
        return f'''    <!-- Geography: globe -->
    <circle cx="455" cy="122" r="22" fill="none" stroke="{primary}" stroke-width="1.5" opacity="0.1"/>
    <ellipse cx="455" cy="122" rx="22" ry="9" fill="none" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>
    <line x1="455" y1="100" x2="455" y2="144" stroke="{corners[3]}" stroke-width="1" opacity="0.1"/>
    <circle cx="448" cy="118" r="3" fill="{primary}" opacity="0.08"/>'''

    elif pattern == "scroll":
        # History: scroll/parchment
        return f'''    <!-- History: scroll -->
    <rect x="440" y="100" width="14" height="42" rx="4" fill="{primary}" opacity="0.1"/>
    <rect x="458" y="105" width="14" height="37" rx="4" fill="{corners[2]}" opacity="0.08"/>
    <rect x="476" y="102" width="10" height="32" rx="3" fill="{corners[3]}" opacity="0.06"/>
    <line x1="445" y1="112" x2="482" y2="112" stroke="{primary}" stroke-width="0.5" opacity="0.08"/>'''

    elif pattern == "binary":
        # Informatics: binary code
        return f'''    <!-- Informatics: binary -->
    <text x="435" y="115" font-family="monospace" font-size="10" fill="{primary}" opacity="0.12">01</text>
    <text x="435" y="128" font-family="monospace" font-size="10" fill="{corners[2]}" opacity="0.1">10</text>
    <text x="435" y="141" font-family="monospace" font-size="10" fill="{corners[3]}" opacity="0.08">01</text>
    <text x="460" y="121" font-family="monospace" font-size="10" fill="{primary}" opacity="0.1">11</text>
    <text x="460" y="134" font-family="monospace" font-size="10" fill="{corners[2]}" opacity="0.08">00</text>'''

    elif pattern == "notes":
        # Music: musical notes
        return f'''    <!-- Music: notes -->
    <circle cx="445" cy="130" r="6" fill="{primary}" opacity="0.15"/>
    <line x1="451" y1="130" x2="451" y2="100" stroke="{primary}" stroke-width="1.5" opacity="0.12"/>
    <circle cx="467" cy="122" r="6" fill="{corners[2]}" opacity="0.12"/>
    <line x1="473" y1="122" x2="473" y2="92" stroke="{corners[2]}" stroke-width="1.5" opacity="0.1"/>
    <line x1="451" y1="100" x2="473" y2="92" stroke="{corners[3]}" stroke-width="2" opacity="0.08"/>'''

    elif pattern == "gears":
        # Robotics: gear wheels
        return f'''    <!-- Robotics: gears -->
    <circle cx="450" cy="118" r="14" fill="none" stroke="{primary}" stroke-width="1.5" opacity="0.12"/>
    <circle cx="450" cy="118" r="5" fill="none" stroke="{corners[2]}" stroke-width="1" opacity="0.1"/>
    <circle cx="472" cy="138" r="10" fill="none" stroke="{corners[3]}" stroke-width="1" opacity="0.1"/>
    <circle cx="472" cy="138" r="3.5" fill="none" stroke="{corners[3]}" stroke-width="0.8" opacity="0.08"/>'''

    elif pattern == "text":
        # Russian: text/letter decorations
        return f'''    <!-- Russian: text -->
    <text x="435" y="125" font-family="Georgia,serif" font-size="28" fill="{primary}" opacity="0.1">Аа</text>
    <line x1="435" y1="138" x2="480" y2="138" stroke="{corners[2]}" stroke-width="1.5" opacity="0.08"/>
    <line x1="435" y1="145" x2="470" y2="145" stroke="{corners[3]}" stroke-width="1" opacity="0.06"/>'''

    elif pattern == "shield":
        # Safety: shield icon
        return f'''    <!-- Safety: shield -->
    <path d="M455,100 L472,108 L472,130 L455,142 L438,130 L438,108 Z" fill="none" stroke="{primary}" stroke-width="1.5" opacity="0.12"/>
    <text x="455" y="126" font-family="Arial" font-size="16" fill="{primary}" opacity="0.12" text-anchor="middle">!</text>
    <circle cx="455" cy="118" r="4" fill="{corners[2]}" opacity="0.08"/>'''

    elif pattern == "tools":
        # Tech: tools/wrench
        return f'''    <!-- Tech: tools -->
    <rect x="440" y="108" width="4" height="32" fill="{primary}" opacity="0.1" transform="rotate(30,442,124)"/>
    <circle cx="435" cy="106" r="7" fill="none" stroke="{primary}" stroke-width="1.5" opacity="0.1"/>
    <rect x="462" y="112" width="4" height="28" fill="{corners[2]}" opacity="0.08" transform="rotate(-25,464,126)"/>
    <circle cx="466" cy="110" r="5" fill="none" stroke="{corners[3]}" stroke-width="1" opacity="0.08"/>'''

    return ""


def restyle_svg(content, subject, colors):
    """Restyle an SVG with subject-specific colors, replacing the generic red card template."""
    primary = colors["primary"]
    accent = colors["accent"]
    bg_light = colors["bg_light"]
    bg_dark = colors["bg_dark"]
    corners = colors["corners"]

    # Skip SVGs that are already styled (have gradient backgrounds or are 800x500 infographics)
    if 'linearGradient' in content or 'viewBox="0 0 800' in content:
        return content

    # Only process SVGs with the red card template
    if '#C62828' not in content:
        return content

    # 1. Replace the solid cream background with a gradient
    # Replace: <rect width="500" height="350" fill="#FFFDE7" rx="10"/>
    # With: gradient definition + rect using gradient
    content = content.replace(
        '<rect width="500" height="350" fill="#FFFDE7" rx="10"/>',
        f'''<defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:{bg_light};stop-opacity:0.7"/><stop offset="100%" style="stop-color:{bg_dark};stop-opacity:0.4"/>
  </linearGradient></defs>
  <rect width="500" height="350" fill="url(#bg)" rx="14"/>'''
    )

    # 2. Replace the outer/inner border frames
    content = content.replace(
        'stroke="#C62828" stroke-width="3"/>',
        f'stroke="{primary}" stroke-width="2.5" opacity="0.35"/>'
    )
    content = content.replace(
        'stroke="#C62828" stroke-width="1" opacity="0.3"/>',
        f'stroke="{primary}" stroke-width="1" opacity="0.15"/>'
    )

    # 3. Remove sun-ray lines (7 lines from top center) and replace with subject decoration
    # Remove all the sun-ray lines: <line x1="250" y1="5" x2="..." stroke="#C62828" ...opacity="0.08"/>
    content = re.sub(r'\s*<line x1="250" y1="5"[^>]*stroke="#C62828"[^>]*/>\s*', '\n', content)

    # 4. Replace star decorations with subject-specific decorative elements
    decorative = get_subject_decorative(subject, colors)

    # Remove the star polygons
    content = re.sub(
        r'\s*<polygon points="35,12[^/]*/>\s*',
        '\n', content
    )
    content = re.sub(
        r'\s*<polygon points="465,12[^/]*/>\s*',
        '\n', content
    )

    # 5. Replace all remaining #C62828 references with subject primary color
    # Title text fill
    content = re.sub(
        r'fill="#C62828" text-anchor="middle"',
        f'fill="{primary}" text-anchor="middle"',
        content
    )
    # Divider line
    content = re.sub(
        r'stroke="#C62828" stroke-width="2" opacity="0\.25"',
        f'stroke="{primary}" stroke-width="2" opacity="0.3"',
        content
    )
    # Card strokes
    content = content.replace(
        'stroke="#C62828" stroke-width="2.5"',
        f'stroke="{primary}" stroke-width="2.5"'
    )
    # Footer bar
    content = re.sub(
        r'fill="#C62828" opacity="0\.85"',
        f'fill="{primary}" opacity="0.85"',
        content
    )
    # Any remaining C62828 fills
    content = content.replace('fill="#C62828"', f'fill="{primary}"')
    # Any remaining C62828 strokes
    content = content.replace('stroke="#C62828"', f'stroke="{primary}"')

    # 6. Add subject-specific decorative elements before </svg>
    if decorative and '</svg>' in content:
        content = content.replace('</svg>', f'{decorative}\n</svg>')

    # 7. Add subject icon watermark in bottom-right corner area
    icon = colors.get("icon", "")
    if icon:
        # Add a subtle icon watermark
        content = content.replace('</svg>', f'  <text x="20" y="335" font-size="22" opacity="0.06">{icon}</text>\n</svg>')

    # 8. Update corner accent colors in divider bar
    content = re.sub(
        r'<rect x="40" y="74" width="100" height="5" rx="2\.5" fill="[^"]*" opacity="0\.2"/>',
        f'<rect x="40" y="74" width="100" height="5" rx="2.5" fill="{primary}" opacity="0.2"/>',
        content
    )

    # 9. Add a small accent color strip below the title area
    if f'fill="{primary}" opacity="0.2"' not in content:
        # Insert after the divider line
        content = content.replace(
            f'stroke="{primary}" stroke-width="2" opacity="0.3"/>',
            f'stroke="{primary}" stroke-width="2" opacity="0.3"/>\n  <rect x="40" y="74" width="100" height="5" rx="2.5" fill="{primary}" opacity="0.15"/>'
        )

    return content


def main():
    total_restyled = 0
    total_skipped = 0
    subjects_processed = 0

    for subject in sorted(os.listdir(IMG_DIR)):
        subj_dir = os.path.join(IMG_DIR, subject)
        if not os.path.isdir(subj_dir):
            continue

        # Skip already-styled subjects
        if subject in SKIP_SUBJECTS:
            print(f"  SKIP {subject}: already styled with gradient")
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
        subj_skipped = 0

        for svg_file in sorted(svg_files):
            path = os.path.join(subj_dir, svg_file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if this SVG needs restyling (has red card template)
            if '#C62828' not in content:
                subj_skipped += 1
                total_skipped += 1
                continue

            # Check if already has gradient (already partially styled)
            if 'linearGradient' in content:
                subj_skipped += 1
                total_skipped += 1
                continue

            # Restyle
            new_content = restyle_svg(content, subject, colors)

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                subj_count += 1
                total_restyled += 1
            else:
                subj_skipped += 1
                total_skipped += 1

        print(f"  {subject:15s}: {subj_count} restyled, {subj_skipped} skipped ({colors['primary']} frame)")

    print(f"\nTotal: {total_restyled} SVGs restyled across {subjects_processed} subjects, {total_skipped} skipped")


if __name__ == "__main__":
    main()
