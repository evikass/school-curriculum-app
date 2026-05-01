#!/usr/bin/env python3
"""
Generate corrected SVG images for grade 8 subjects where the current SVG
content doesn't match the lesson titles in the data files.
"""
import os, re, json

BASE = "/home/z/my-project/school-curriculum-app"
DATA_DIR = f"{BASE}/src/data/grades/8"
IMG_DIR = f"{BASE}/public/images/lessons/grade8"

# Color schemes per subject
SUBJECT_COLORS = {
    "algebra": {"primary": "#1565C0", "accent": "#0D47A1", "bg": "#E3F2FD", "name": "Алгебра"},
    "art": {"primary": "#6A1B9A", "accent": "#4A148C", "bg": "#F3E5F5", "name": "Изобразительное искусство"},
    "biology": {"primary": "#2E7D32", "accent": "#1B5E20", "bg": "#E8F5E9", "name": "Биология"},
    "chemistry": {"primary": "#00695C", "accent": "#004D40", "bg": "#E0F2F1", "name": "Химия"},
    "coding": {"primary": "#4A148C", "accent": "#311B92", "bg": "#EDE7F6", "name": "Основы программирования"},
    "economy": {"primary": "#E65100", "accent": "#BF360C", "bg": "#FFF3E0", "name": "Экономика"},
    "english": {"primary": "#0D47A1", "accent": "#1A237E", "bg": "#E8EAF6", "name": "Иностранный язык"},
    "geography": {"primary": "#00695C", "accent": "#004D40", "bg": "#E0F2F1", "name": "География"},
    "geometry": {"primary": "#283593", "accent": "#1A237E", "bg": "#E8EAF6", "name": "Геометрия"},
    "history": {"primary": "#E65100", "accent": "#BF360C", "bg": "#FFF3E0", "name": "История"},
    "informatics": {"primary": "#1A237E", "accent": "#0D47A1", "bg": "#E8EAF6", "name": "Информатика"},
    "law": {"primary": "#455A64", "accent": "#263238", "bg": "#ECEFF1", "name": "Основы права"},
    "literature": {"primary": "#6D4C41", "accent": "#3E2723", "bg": "#EFEBE9", "name": "Литература"},
    "music": {"primary": "#6A1B9A", "accent": "#4A148C", "bg": "#F3E5F5", "name": "Музыка"},
    "pe": {"primary": "#E65100", "accent": "#BF360C", "bg": "#FFF3E0", "name": "Физическая культура"},
    "physics": {"primary": "#C62828", "accent": "#B71C1C", "bg": "#FFEBEE", "name": "Физика"},
    "robotics": {"primary": "#37474F", "accent": "#263238", "bg": "#ECEFF1", "name": "Робототехника"},
    "russian": {"primary": "#1565C0", "accent": "#0D47A1", "bg": "#E3F2FD", "name": "Русский язык"},
    "safety": {"primary": "#E65100", "accent": "#BF360C", "bg": "#FFF3E0", "name": "ОБЖ"},
    "social": {"primary": "#1565C0", "accent": "#0D47A1", "bg": "#E3F2FD", "name": "Обществознание"},
    "tech": {"primary": "#37474F", "accent": "#263238", "bg": "#ECEFF1", "name": "Технология"},
}

def extract_lessons(subject):
    """Extract lesson titles from data file, preserving order."""
    idx_file = os.path.join(DATA_DIR, subject, "index.ts")
    if not os.path.isfile(idx_file):
        return []
    
    with open(idx_file, 'r') as f:
        content = f.read()
    
    # Find all detailedTopics lessons
    lessons = []
    # Split by 'detailedTopics' to get the lesson arrays
    # Use a simpler approach: find all title-image pairs within lessons
    pattern = r'title:\s*"([^"]+)"[^}]*?image:\s*"([^"]+)"'
    for m in re.finditer(pattern, content, re.DOTALL):
        title = m.group(1)
        image = m.group(2)
        # Skip the subject title (first occurrence is usually the subject name)
        if title in ["Алгебра", "Биология", "Химия", "Физика", "География", "История",
                      "Литература", "Обществознание", "Экономика", "ОБЖ", "Технология",
                      "Музыка", "Русский язык", "Иностранный язык", "Информатика",
                      "Робототехника", "Основы права", "Изобразительное искусство",
                      "Основы программирования", "Геометрия", "Физическая культура"]:
            continue
        # Extract lesson number from image path
        img_match = re.search(r'lesson(\d+)\.svg', image)
        if img_match:
            lesson_num = int(img_match.group(1))
            lessons.append({"num": lesson_num, "title": title, "image": image})
    
    return lessons

def get_svg_topic(svg_path):
    """Extract the main topic text from an SVG file."""
    if not os.path.isfile(svg_path):
        return None
    with open(svg_path, 'r') as f:
        content = f.read()
    # Get the first substantial text (the title)
    texts = re.findall(r'<text[^>]*>([^<]+)</text>', content)
    for t in texts:
        t = t.strip()
        if t and len(t) > 3 and not t.startswith("Урок") and t not in SUBJECT_COLORS.get("", {}).values():
            return t
    return None

def is_match(data_title, svg_topic):
    """Check if the SVG topic matches the data title - must be very close."""
    if not svg_topic:
        return False
    dt = data_title.lower().strip()
    st = svg_topic.lower().strip()
    # Exact match
    if dt == st:
        return True
    # One is a prefix of the other (e.g. "Внутренняя энергия" vs "Внутренняя энергия и способы")
    if dt.startswith(st) or st.startswith(dt):
        # But only if the shorter one is at least 60% of the longer
        min_len = min(len(dt), len(st))
        max_len = max(len(dt), len(st))
        if min_len >= max_len * 0.6:
            return True
    # Check word overlap - need high overlap
    dt_words = set(w for w in dt.split() if len(w) > 3)
    st_words = set(w for w in st.split() if len(w) > 3)
    if dt_words and st_words:
        overlap = dt_words & st_words
        # Need at least 70% of words from the shorter title to overlap
        min_words = min(len(dt_words), len(st_words))
        if min_words > 0 and len(overlap) >= min_words * 0.7 and len(overlap) >= 2:
            return True
    return False

def extract_key_info(title, description):
    """Extract key formulas/terms from lesson description for SVG content."""
    if not description:
        return []
    # Extract key formulas and terms
    info = []
    # Find formulas (patterns like ax²+bx+c=0, Q=cm(t₂-t₁), etc.)
    formulas = re.findall(r'[*•]\s+\*\*([^*]+)\*\*', description)
    for f in formulas[:5]:
        if len(f) < 60:
            info.append(f.strip())
    # Find bold terms
    bold_terms = re.findall(r'\*\*([^*]{3,40})\*\*', description)
    for t in bold_terms[:8]:
        t = t.strip()
        if t not in info and len(t) > 3:
            info.append(t)
    return info[:8]

def generate_svg(subject, lesson_num, title, key_info=None):
    """Generate a Bauhaus-style SVG for a lesson."""
    colors = SUBJECT_COLORS.get(subject, {"primary": "#1565C0", "accent": "#0D47A1", "bg": "#E3F2FD", "name": subject.capitalize()})
    primary = colors["primary"]
    accent = colors["accent"]
    bg_color = colors["bg"]
    subj_name = colors["name"]
    
    # Determine illustration content
    if not key_info:
        key_info = []
    
    # Truncate title if too long
    display_title = title if len(title) <= 40 else title[:38] + "..."
    
    # Build illustration area content
    ill_content = f'<rect x="15" y="85" width="470" height="215" fill="{bg_color}"/>'
    
    # Main title in illustration area
    ill_content += f'<text x="250" y="130" font-family="Arial,sans-serif" font-size="20" fill="{primary}" text-anchor="middle" font-weight="bold">{escape_xml(display_title)}</text>'
    
    # Add key info items as styled boxes/text
    y_pos = 155
    items_to_show = key_info[:6]
    
    if items_to_show:
        # Calculate layout for info items
        items_per_row = min(3, len(items_to_show))
        rows = (len(items_to_show) + items_per_row - 1) // items_per_row
        
        box_width = min(140, 430 // max(1, items_per_row))
        box_height = 45
        gap_x = (440 - items_per_row * box_width) / (items_per_row + 1)
        gap_y = 10
        
        for i, item in enumerate(items_to_show[:6]):
            row = i // items_per_row
            col = i % items_per_row
            x = 20 + gap_x + col * (box_width + gap_x)
            y = y_pos + row * (box_height + gap_y)
            
            # Alternate colors
            item_colors = [primary, accent, "#F9A825", "#2E7D32", "#6A1B9A", "#E65100"]
            item_color = item_colors[i % len(item_colors)]
            light_colors = ["#E3F2FD", "#FFF3E0", "#FFFDE7", "#E8F5E9", "#F3E5F5", "#FFEBEE"]
            light = light_colors[i % len(light_colors)]
            
            display_item = item if len(item) <= 25 else item[:23] + "..."
            
            ill_content += f'<rect x="{x:.0f}" y="{y:.0f}" width="{box_width}" height="{box_height}" rx="5" fill="{light}" stroke="{item_color}" stroke-width="1.5"/>'
            ill_content += f'<text x="{x + box_width/2:.0f}" y="{y + box_height/2 + 5:.0f}" font-family="Arial" font-size="12" fill="{item_color}" text-anchor="middle">{escape_xml(display_item)}</text>'
    
    # Add a decorative element based on subject type
    decorative = get_decorative_element(subject, primary, accent)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFF8E1"/>
      <stop offset="100%" stop-color="#FFFDE7"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{primary}"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="{primary}" stroke-width="3"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="{primary}" stroke-width="1" opacity="0.3"/>
  <!-- Bauhaus corner accents -->
  <polygon points="10,10 30,10 10,30" fill="{primary}" opacity="0.12"/>
  <polygon points="490,10 470,10 490,30" fill="#1565C0" opacity="0.12"/>
  <polygon points="10,340 30,340 10,320" fill="#F9A825" opacity="0.12"/>
  <polygon points="490,340 470,340 490,320" fill="#2E7D32" opacity="0.12"/>
  <!-- Title -->
  <text x="250" y="48" font-family="Arial,sans-serif" font-size="22" font-weight="bold" fill="{primary}" text-anchor="middle">{escape_xml(display_title)}</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">{subj_name} - Урок {lesson_num}</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="{primary}" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="75" width="60" height="5" fill="{primary}" opacity="0.18" rx="1"/>
  <rect x="410" y="75" width="60" height="5" fill="#1565C0" opacity="0.12" rx="1"/>
  <!-- ILLUSTRATION AREA -->
  <clipPath id="ill"><rect x="15" y="85" width="470" height="215" rx="6"/></clipPath>
  <g clip-path="url(#ill)">
  {ill_content}
  {decorative}
  </g>
  <!-- Bottom panel -->
  <rect x="12" y="305" width="476" height="32" rx="5" fill="url(#panel)"/>
  <line x1="20" y1="308" x2="20" y2="334" stroke="#F9A825" stroke-width="1.5" opacity="0.6"/>
  <line x1="480" y1="308" x2="480" y2="334" stroke="#F9A825" stroke-width="1.5" opacity="0.6"/>
  <text x="250" y="326" font-family="Arial,sans-serif" font-size="15" text-anchor="middle" fill="white" font-weight="bold">{subj_name}</text>
</svg>'''
    return svg

def escape_xml(text):
    """Escape XML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def get_decorative_element(subject, primary, accent):
    """Return a small decorative element for the illustration area."""
    # Simple geometric decorations based on subject type
    if subject in ["algebra", "geometry"]:
        return f'<circle cx="450" cy="110" r="15" fill="{primary}" opacity="0.15"/><circle cx="440" cy="120" r="8" fill="{accent}" opacity="0.1"/>'
    elif subject in ["physics"]:
        return f'<circle cx="60" cy="280" r="20" fill="{primary}" opacity="0.1"/><polygon points="440,275 460,290 440,305" fill="{accent}" opacity="0.1"/>'
    elif subject in ["biology"]:
        return f'<circle cx="450" cy="270" r="18" fill="{primary}" opacity="0.1"/><circle cx="455" cy="265" r="10" fill="#2E7D32" opacity="0.08"/>'
    elif subject in ["chemistry"]:
        return f'<circle cx="55" cy="275" r="16" fill="{primary}" opacity="0.12"/><circle cx="65" cy="268" r="10" fill="#00695C" opacity="0.08"/>'
    elif subject in ["history", "social", "law"]:
        return f'<rect x="435" y="268" width="30" height="25" rx="3" fill="{primary}" opacity="0.1"/>'
    elif subject in ["geography"]:
        return f'<circle cx="50" cy="270" r="20" fill="{primary}" opacity="0.1"/><ellipse cx="55" cy="265" rx="12" ry="8" fill="#00695C" opacity="0.08"/>'
    elif subject in ["english"]:
        return f'<rect x="430" y="270" width="25" height="20" rx="2" fill="{primary}" opacity="0.12"/>'
    elif subject in ["music", "art"]:
        return f'<circle cx="55" cy="275" r="16" fill="{primary}" opacity="0.15"/><circle cx="65" cy="268" r="8" fill="{accent}" opacity="0.1"/>'
    elif subject in ["pe", "safety"]:
        return f'<polygon points="50,270 60,285 40,285" fill="{primary}" opacity="0.12"/>'
    elif subject in ["coding", "informatics", "robotics"]:
        return f'<rect x="435" y="270" width="20" height="20" rx="2" fill="{primary}" opacity="0.12"/><rect x="445" y="280" width="15" height="15" rx="2" fill="{accent}" opacity="0.08"/>'
    elif subject in ["tech"]:
        return f'<polygon points="50,275 65,265 65,285" fill="{primary}" opacity="0.1"/>'
    elif subject in ["economy"]:
        return f'<circle cx="450" cy="275" r="15" fill="{primary}" opacity="0.12"/>'
    elif subject in ["literature"]:
        return f'<rect x="430" y="268" width="25" height="30" rx="2" fill="{primary}" opacity="0.1"/>'
    elif subject in ["russian"]:
        return f'<circle cx="55" cy="275" r="16" fill="{primary}" opacity="0.12"/>'
    else:
        return f'<circle cx="450" cy="275" r="15" fill="{primary}" opacity="0.1"/>'

def extract_description(subject, lesson_title):
    """Extract the description from the data file for a given lesson."""
    idx_file = os.path.join(DATA_DIR, subject, "index.ts")
    if not os.path.isfile(idx_file):
        return ""
    with open(idx_file, 'r') as f:
        content = f.read()
    
    # Find the lesson block with this title
    escaped_title = re.escape(lesson_title)
    pattern = r'title:\s*"' + escaped_title + r'"[^}]*?description:\s*`([^`]*)`'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return m.group(1)
    return ""

def main():
    total_mismatches = 0
    total_generated = 0
    subjects_processed = 0
    
    for subject in sorted(os.listdir(DATA_DIR)):
        lessons = extract_lessons(subject)
        if not lessons:
            continue
        
        svg_dir = os.path.join(IMG_DIR, subject)
        if not os.path.isdir(svg_dir):
            os.makedirs(svg_dir, exist_ok=True)
        
        subject_mismatches = 0
        
        for lesson in lessons:
            num = lesson["num"]
            title = lesson["title"]
            svg_path = os.path.join(svg_dir, f"lesson{num}.svg")
            
            # Check if current SVG matches
            svg_topic = get_svg_topic(svg_path)
            
            if is_match(title, svg_topic):
                continue
            
            # Mismatch found - generate new SVG
            subject_mismatches += 1
            total_mismatches += 1
            
            # Extract key info from description
            description = extract_description(subject, title)
            key_info = extract_key_info(title, description)
            
            # Generate and save SVG
            svg_content = generate_svg(subject, num, title, key_info)
            with open(svg_path, 'w') as f:
                f.write(svg_content)
            
            total_generated += 1
        
        if subject_mismatches > 0:
            subjects_processed += 1
            print(f"  {subject}: {subject_mismatches} SVGs regenerated")
    
    print(f"\nTotal: {total_mismatches} mismatched SVGs found and regenerated across {subjects_processed} subjects")

if __name__ == "__main__":
    main()
