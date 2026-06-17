#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 11 Geometry (Геометрия) lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/lessons/grade11/geometry"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme
PRIMARY = "#5C6BC0"
PRIMARY_DARK = "#3F51B5"
PRIMARY_LIGHT = "#7986CB"
BG = "#E8EAF6"
BG_LIGHT = "#FFFFFF"
TEXT_DARK = "#283593"
TEXT_MUTED = "#5C6BC0"
ACCENT = "#FF7043"

NS = 'http://www.w3.org/2000/svg'


def svg_root():
    """Create base SVG element."""
    root = ET.Element('svg')
    root.set('xmlns', NS)
    root.set('viewBox', '0 0 500 350')
    return root


def add_defs(root):
    """Add gradient and pattern defs."""
    defs = ET.SubElement(root, 'defs')
    # Background gradient
    grad = ET.SubElement(defs, 'linearGradient')
    grad.set('id', 'bgGrad')
    grad.set('x1', '0'); grad.set('y1', '0')
    grad.set('x2', '0'); grad.set('y2', '1')
    s1 = ET.SubElement(grad, 'stop')
    s1.set('offset', '0%'); s1.set('stop-color', BG)
    s2 = ET.SubElement(grad, 'stop')
    s2.set('offset', '100%'); s2.set('stop-color', BG_LIGHT)
    # Panel gradient
    pgrad = ET.SubElement(defs, 'linearGradient')
    pgrad.set('id', 'panelGrad')
    pgrad.set('x1', '0'); pgrad.set('y1', '0')
    pgrad.set('x2', '1'); pgrad.set('y2', '0')
    p1 = ET.SubElement(pgrad, 'stop')
    p1.set('offset', '0%'); p1.set('stop-color', PRIMARY)
    p2 = ET.SubElement(pgrad, 'stop')
    p2.set('offset', '100%'); p2.set('stop-color', PRIMARY_DARK)


def add_background(root):
    """Add background rect, border, and decorative corners."""
    # Background
    bg_rect = ET.SubElement(root, 'rect')
    bg_rect.set('width', '500'); bg_rect.set('height', '350')
    bg_rect.set('fill', 'url(#bgGrad)'); bg_rect.set('rx', '10')

    # Border
    border = ET.SubElement(root, 'rect')
    border.set('x', '3'); border.set('y', '3')
    border.set('width', '494'); border.set('height', '344')
    border.set('rx', '8'); border.set('fill', 'none')
    border.set('stroke', PRIMARY); border.set('stroke-width', '2.5')

    # Inner decorative border
    inner = ET.SubElement(root, 'rect')
    inner.set('x', '8'); inner.set('y', '8')
    inner.set('width', '484'); inner.set('height', '334')
    inner.set('rx', '6'); inner.set('fill', 'none')
    inner.set('stroke', PRIMARY); inner.set('stroke-width', '1')
    inner.set('opacity', '0.25')

    # Corner decorations
    corners = [
        ("10,10 30,10 10,30", "0.10"),
        ("490,10 470,10 490,30", "0.10"),
        ("10,340 30,340 10,320", "0.10"),
        ("490,340 470,340 490,320", "0.10"),
    ]
    for pts, op in corners:
        p = ET.SubElement(root, 'polygon')
        p.set('points', pts); p.set('fill', PRIMARY); p.set('opacity', op)


def add_header(root, title, lesson_num):
    """Add header with title and lesson number."""
    # Title
    t = ET.SubElement(root, 'text')
    t.set('x', '250'); t.set('y', '42')
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '20')
    t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
    t.set('text-anchor', 'middle')
    t.text = title

    # Subtitle
    st = ET.SubElement(root, 'text')
    st.set('x', '250'); st.set('y', '62')
    st.set('font-family', 'Arial,sans-serif'); st.set('font-size', '12')
    st.set('fill', TEXT_MUTED); st.set('text-anchor', 'middle')
    st.text = f"Геометрия — Урок {lesson_num}"

    # Separator line
    line = ET.SubElement(root, 'line')
    line.set('x1', '30'); line.set('y1', '72')
    line.set('x2', '470'); line.set('y2', '72')
    line.set('stroke', PRIMARY); line.set('stroke-width', '2')
    line.set('opacity', '0.3')

    # Accent bars on separator
    r1 = ET.SubElement(root, 'rect')
    r1.set('x', '30'); r1.set('y', '69')
    r1.set('width', '50'); r1.set('height', '5')
    r1.set('fill', PRIMARY); r1.set('opacity', '0.15')
    r1.set('rx', '1')
    r2 = ET.SubElement(root, 'rect')
    r2.set('x', '420'); r2.set('y', '69')
    r2.set('width', '50'); r2.set('height', '5')
    r2.set('fill', PRIMARY_DARK); r2.set('opacity', '0.10')
    r2.set('rx', '1')


def add_footer(root):
    """Add footer."""
    # Footer background
    fb = ET.SubElement(root, 'rect')
    fb.set('x', '10'); fb.set('y', '305')
    fb.set('width', '480'); fb.set('height', '35')
    fb.set('fill', 'url(#panelGrad)'); fb.set('opacity', '0.08')
    fb.set('rx', '5')

    # Footer text
    ft = ET.SubElement(root, 'text')
    ft.set('x', '250'); ft.set('y', '327')
    ft.set('font-family', 'Arial,sans-serif'); ft.set('font-size', '11')
    ft.set('fill', PRIMARY); ft.set('text-anchor', 'middle')
    ft.set('opacity', '0.65')
    ft.text = "Геометрия · 11 класс"


def add_content_box(root, x, y, w, h, title, lines, box_id=""):
    """Add a content box with title and text lines."""
    # Box background
    box = ET.SubElement(root, 'rect')
    box.set('x', str(x)); box.set('y', str(y))
    box.set('width', str(w)); box.set('height', str(h))
    box.set('fill', BG); box.set('rx', '6')
    box.set('stroke', PRIMARY); box.set('stroke-width', '1')
    box.set('opacity', '0.9')

    # Title bar
    tbar = ET.SubElement(root, 'rect')
    tbar.set('x', str(x)); tbar.set('y', str(y))
    tbar.set('width', str(w)); tbar.set('height', '18')
    tbar.set('fill', PRIMARY); tbar.set('rx', '6')
    tbar.set('opacity', '0.18')

    # Cover bottom corners of title bar
    tbc = ET.SubElement(root, 'rect')
    tbc.set('x', str(x)); tbc.set('y', str(y + 12))
    tbc.set('width', str(w)); tbc.set('height', '6')
    tbc.set('fill', PRIMARY); tbc.set('opacity', '0.18')

    # Box title
    bt = ET.SubElement(root, 'text')
    bt.set('x', str(x + w // 2)); bt.set('y', str(y + 13))
    bt.set('font-family', 'Arial,sans-serif'); bt.set('font-size', '10')
    bt.set('font-weight', 'bold'); bt.set('fill', TEXT_DARK)
    bt.set('text-anchor', 'middle')
    bt.text = title

    # Content lines
    for i, line in enumerate(lines):
        lt = ET.SubElement(root, 'text')
        lt.set('x', str(x + 8)); lt.set('y', str(y + 30 + i * 15))
        lt.set('font-family', 'Arial,sans-serif'); lt.set('font-size', '10')
        lt.set('fill', '#37474F')
        lt.text = line


def add_formula_box(root, x, y, w, h, title, formulas):
    """Add a formula box with highlighted formulas."""
    # Box background
    box = ET.SubElement(root, 'rect')
    box.set('x', str(x)); box.set('y', str(y))
    box.set('width', str(w)); box.set('height', str(h))
    box.set('fill', '#FFFFFF'); box.set('rx', '6')
    box.set('stroke', ACCENT); box.set('stroke-width', '1.5')
    box.set('opacity', '0.95')

    # Title bar
    tbar = ET.SubElement(root, 'rect')
    tbar.set('x', str(x)); tbar.set('y', str(y))
    tbar.set('width', str(w)); tbar.set('height', '18')
    tbar.set('fill', ACCENT); tbar.set('rx', '6')
    tbar.set('opacity', '0.2')

    tbc = ET.SubElement(root, 'rect')
    tbc.set('x', str(x)); tbc.set('y', str(y + 12))
    tbc.set('width', str(w)); tbc.set('height', '6')
    tbc.set('fill', ACCENT); tbc.set('opacity', '0.2')

    # Title
    bt = ET.SubElement(root, 'text')
    bt.set('x', str(x + w // 2)); bt.set('y', str(y + 13))
    bt.set('font-family', 'Arial,sans-serif'); bt.set('font-size', '10')
    bt.set('font-weight', 'bold'); bt.set('fill', '#BF360C')
    bt.set('text-anchor', 'middle')
    bt.text = title

    # Formulas
    for i, formula in enumerate(formulas):
        ft = ET.SubElement(root, 'text')
        ft.set('x', str(x + 8)); ft.set('y', str(y + 32 + i * 16))
        ft.set('font-family', 'Arial,sans-serif'); ft.set('font-size', '10')
        ft.set('fill', '#BF360C'); ft.set('font-weight', 'bold')
        ft.text = formula


def add_illustration_area(root, x, y, w, h):
    """Add a clipped illustration area."""
    # Outer clip rect definition
    defs = root.find('defs')
    if defs is None:
        defs = root.find(f'{{{NS}}}defs')
    if defs is None:
        # Search iteratively
        for child in root:
            if child.tag == 'defs' or child.tag == f'{{{NS}}}defs':
                defs = child
                break
    if defs is None:
        defs = ET.SubElement(root, 'defs')
    clip = ET.SubElement(defs, 'clipPath')
    clip.set('id', 'ill')
    cr = ET.SubElement(clip, 'rect')
    cr.set('x', str(x)); cr.set('y', str(y))
    cr.set('width', str(w)); cr.set('height', str(h))
    cr.set('rx', '6')

    g = ET.SubElement(root, 'g')
    g.set('clip-path', 'url(#ill)')

    # Background
    ill_bg = ET.SubElement(g, 'rect')
    ill_bg.set('x', str(x)); ill_bg.set('y', str(y))
    ill_bg.set('width', str(w)); ill_bg.set('height', str(h))
    ill_bg.set('fill', BG); ill_bg.set('opacity', '0.5')

    return g


def build_svg(lesson_num, title, content_fn):
    """Build a complete SVG for a lesson."""
    root = svg_root()
    add_defs(root)
    add_background(root)
    add_header(root, title, lesson_num)

    # Main content area
    content_fn(root)

    add_footer(root)
    return root


def write_svg(root, filepath):
    """Write SVG to file with XML declaration."""
    tree = ET.ElementTree(root)
    ET.indent(tree, space='  ')
    xml_bytes = ET.tostring(root, encoding='unicode', xml_declaration=False)
    # Add XML declaration manually
    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_bytes
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(xml_str)


# ============================================================
# LESSON CONTENT GENERATORS
# ============================================================

def lesson1_prism(root):
    """Призма - Prism."""
    # Left: Definition box
    add_content_box(root, 18, 82, 225, 110, "Определение", [
        "Призма — многогранник, два",
        "грани которого — равные",
        "многоугольники (основания),",
        "а остальные — параллелограммы.",
        "",
        "Прямая призма: боковые рёбра",
        "перпендикулярны основаниям.",
    ])

    # Right: Formula box
    add_formula_box(root, 255, 82, 225, 110, "Формулы", [
        "V = S_осн · h",
        "S_бок = P_осн · h  (прямая)",
        "S_полн = S_бок + 2·S_осн",
        "Диагональ: d² = a² + b² + h²",
    ])

    # Bottom left: Properties
    add_content_box(root, 18, 202, 225, 95, "Свойства", [
      "• Основания параллельны и равны",
      "• Боковые рёбра параллельны",
      "• Боковые грани — параллелограммы",
      "• S_полн = S_бок + 2·S_осн",
      "• Высота h ⊥ основаниям",
    ])

    # Bottom right: Illustration area with prism drawing
    g = add_illustration_area(root, 255, 202, 225, 95)
    # Draw a simple 3D prism
    # Front face
    ET.SubElement(g, 'polygon').set('points', '290,220 340,220 340,275 290,275')
    g[-1].set('fill', 'none'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    # Top face
    ET.SubElement(g, 'polygon').set('points', '290,220 340,220 370,205 320,205')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.12'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Right face
    ET.SubElement(g, 'polygon').set('points', '340,220 370,205 370,260 340,275')
    g[-1].set('fill', PRIMARY_DARK); g[-1].set('opacity', '0.08'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Height line
    ET.SubElement(g, 'line').set('x1', '290'); g[-1].set('y1', '275'); g[-1].set('x2', '290'); g[-1].set('y2', '220')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1.5'); g[-1].set('stroke-dasharray', '4,3')
    # h label
    t = ET.SubElement(g, 'text')
    t.set('x', '280'); t.set('y', '250'); t.set('font-family', 'Arial,sans-serif')
    t.set('font-size', '11'); t.set('fill', ACCENT); t.set('font-style', 'italic')
    t.text = 'h'
    # Caption
    t2 = ET.SubElement(g, 'text')
    t2.set('x', '370'); t2.set('y', '293'); t2.set('font-family', 'Arial,sans-serif')
    t2.set('font-size', '9'); t2.set('fill', PRIMARY); t2.set('text-anchor', 'middle')
    t2.set('opacity', '0.7')
    t2.text = 'Прямая призма'


def lesson2_pyramid(root):
    """Пирамида - Pyramid."""
    add_content_box(root, 18, 82, 225, 110, "Определение", [
        "Пирамида — многогранник,",
        "основание — многоугольник,",
        "остальные грани — треугольники",
        "с общей вершиной.",
        "",
        "Правильная пирамида: основание",
        "— прав. многоугольник, вершина",
        "проектируется в центр основания.",
    ])

    add_formula_box(root, 255, 82, 225, 110, "Формулы", [
        "V = ⅓ · S_осн · h",
        "S_бок = ½ · P_осн · l (прав.)",
        "S_полн = S_бок + S_осн",
        "l² = h² + R²  (апофема)",
    ])

    add_content_box(root, 18, 202, 225, 95, "Виды пирамид", [
        "• Треугольная (тетраэдр)",
        "• Четырёхугольная",
        "• Правильная пирамида",
        "• Усечённая пирамида:",
        "  V = ⅓h(S₁+√(S₁S₂)+S₂)",
    ])

    # Pyramid illustration
    g = add_illustration_area(root, 255, 202, 225, 95)
    # Base
    ET.SubElement(g, 'polygon').set('points', '310,275 380,275 400,260 330,260')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.08'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Side faces
    ET.SubElement(g, 'line').set('x1', '310'); g[-1].set('y1', '275'); g[-1].set('x2', '355'); g[-1].set('y2', '215')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    ET.SubElement(g, 'line').set('x1', '380'); g[-1].set('y1', '275'); g[-1].set('x2', '355'); g[-1].set('y2', '215')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    ET.SubElement(g, 'line').set('x1', '400'); g[-1].set('y1', '260'); g[-1].set('x2', '355'); g[-1].set('y2', '215')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    ET.SubElement(g, 'line').set('x1', '330'); g[-1].set('y1', '260'); g[-1].set('x2', '355'); g[-1].set('y2', '215')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Hidden edge
    ET.SubElement(g, 'line').set('x1', '330'); g[-1].set('y1', '260'); g[-1].set('x2', '310'); g[-1].set('y2', '275')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1'); g[-1].set('stroke-dasharray', '3,3')
    # Height
    ET.SubElement(g, 'line').set('x1', '355'); g[-1].set('y1', '215'); g[-1].set('x2', '355'); g[-1].set('y2', '268')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1.5'); g[-1].set('stroke-dasharray', '4,3')
    t = ET.SubElement(g, 'text')
    t.set('x', '365'); t.set('y', '245'); t.set('font-family', 'Arial,sans-serif')
    t.set('font-size', '11'); t.set('fill', ACCENT); t.set('font-style', 'italic')
    t.text = 'h'
    t2 = ET.SubElement(g, 'text')
    t2.set('x', '370'); t2.set('y', '293'); t2.set('font-family', 'Arial,sans-serif')
    t2.set('font-size', '9'); t2.set('fill', PRIMARY); t2.set('text-anchor', 'middle'); t2.set('opacity', '0.7')
    t2.text = 'Пирамида'


def lesson3_polyhedra(root):
    """Правильные многогранники - Regular polyhedra."""
    add_content_box(root, 18, 82, 225, 80, "Определение", [
        "Правильный многогранник —",
        "выпуклый многогранник, все",
        "грани — равные правильные",
        "многоугольники, в каждой",
        "вершине сходится одинаковое",
        "число рёбер.",
    ])

    add_content_box(root, 18, 170, 225, 82, "Теорема Эйлера", [
        "Для любого выпуклого",
        "многогранника:",
        "  В − Р + Г = 2",
        "В — вершины, Р — рёбра,",
        "Г — грани",
    ])

    # Five Platonic solids table
    add_content_box(root, 255, 82, 225, 170, "Пять правильных многогранников", [
        "Тетраэдр: 4Δ   (В=4 Р=6 Г=4)",
        "Куб:       6□   (В=8 Р=12 Г=6)",
        "Октаэдр:   8Δ   (В=6 Р=12 Г=8)",
        "Додекаэдр: 12⬠  (В=20 Р=30 Г=12)",
        "Икосаэдр:  20Δ  (В=12 Р=30 Г=20)",
        "",
        "Только 5 правильных",
        "многогранников существует!",
    ])

    # Bottom: Illustration with shapes
    g = add_illustration_area(root, 18, 260, 462, 38)
    # Small tetrahedron
    ET.SubElement(g, 'polygon').set('points', '50,280 75,268 75,288')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.15'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Small cube
    ET.SubElement(g, 'polygon').set('points', '130,270 155,270 155,290 130,290')
    g[-1].set('fill', PRIMARY_LIGHT); g[-1].set('opacity', '0.12'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    ET.SubElement(g, 'polygon').set('points', '155,270 168,263 168,283 155,290')
    g[-1].set('fill', PRIMARY_DARK); g[-1].set('opacity', '0.10'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    ET.SubElement(g, 'polygon').set('points', '130,270 155,270 168,263 143,263')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.15'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Octahedron hint
    ET.SubElement(g, 'polygon').set('points', '250,263 262,275 250,287 238,275')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.12'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Labels
    for x, label in [(60, "Δ₄"), (148, "□₆"), (250, "Δ₈"), (350, "⬠₁₂"), (430, "Δ₂₀")]:
        t = ET.SubElement(g, 'text')
        t.set('x', str(x)); t.set('y', '296'); t.set('font-family', 'Arial,sans-serif')
        t.set('font-size', '8'); t.set('fill', PRIMARY); t.set('text-anchor', 'middle'); t.set('opacity', '0.6')
        t.text = label


def lesson4_cylinder(root):
    """Цилиндр - Cylinder."""
    add_content_box(root, 18, 82, 225, 100, "Определение", [
        "Цилиндр — тело, ограниченное",
        "цилиндрической поверхностью",
        "и двумя кругами (основания).",
        "",
        "Прямой круговой цилиндр:",
        "образующие ⊥ основаниям.",
        "R — радиус, h — высота",
    ])

    add_formula_box(root, 255, 82, 225, 100, "Формулы", [
        "V = πR²h",
        "S_бок = 2πRh",
        "S_полн = 2πR(R + h)",
        "S_осн = πR²",
        "l = h  (образующая прям.)",
    ])

    add_content_box(root, 18, 190, 225, 95, "Свойства", [
        "• Образующие параллельны и =",
        "• Осевое сечение — прямоуг.",
        "• Сечение ⊥ оси — круг",
        "• Развёртка бок. пов. —",
        "  прямоугольник 2πR × h",
    ])

    # Cylinder illustration
    g = add_illustration_area(root, 255, 190, 225, 95)
    # Bottom ellipse
    ET.SubElement(g, 'ellipse').set('cx', '370'); g[-1].set('cy', '275'); g[-1].set('rx', '40'); g[-1].set('ry', '12')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.10'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Side lines
    ET.SubElement(g, 'line').set('x1', '330'); g[-1].set('y1', '275'); g[-1].set('x2', '330'); g[-1].set('y2', '215')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    ET.SubElement(g, 'line').set('x1', '410'); g[-1].set('y1', '275'); g[-1].set('x2', '410'); g[-1].set('y2', '215')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    # Top ellipse
    ET.SubElement(g, 'ellipse').set('cx', '370'); g[-1].set('cy', '215'); g[-1].set('rx', '40'); g[-1].set('ry', '12')
    g[-1].set('fill', BG_LIGHT); g[-1].set('opacity', '0.8'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Height label
    ET.SubElement(g, 'line').set('x1', '330'); g[-1].set('y1', '275'); g[-1].set('x2', '322'); g[-1].set('y2', '275')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1')
    ET.SubElement(g, 'line').set('x1', '322'); g[-1].set('y1', '275'); g[-1].set('x2', '322'); g[-1].set('y2', '215')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1.5'); g[-1].set('stroke-dasharray', '3,2')
    ET.SubElement(g, 'line').set('x1', '322'); g[-1].set('y1', '215'); g[-1].set('x2', '330'); g[-1].set('y2', '215')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1')
    t = ET.SubElement(g, 'text')
    t.set('x', '315'); t.set('y', '248'); t.set('font-family', 'Arial,sans-serif')
    t.set('font-size', '11'); t.set('fill', ACCENT); t.set('font-style', 'italic')
    t.text = 'h'
    t2 = ET.SubElement(g, 'text')
    t2.set('x', '390'); t2.set('y', '213'); t2.set('font-family', 'Arial,sans-serif')
    t2.set('font-size', '9'); t.set('fill', PRIMARY); t2.set('text-anchor', 'middle'); t2.set('opacity', '0.7')
    t2.text = 'R'
    # R line
    ET.SubElement(g, 'line').set('x1', '370'); g[-1].set('y1', '215'); g[-1].set('x2', '410'); g[-1].set('y2', '215')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1'); g[-1].set('stroke-dasharray', '3,2')


def lesson5_cone(root):
    """Конус - Cone."""
    add_content_box(root, 18, 82, 225, 100, "Определение", [
        "Конус — тело, ограниченное",
        "конической поверхностью и",
        "кругом (основание).",
        "",
        "R — радиус основания",
        "l — образующая",
        "h — высота",
    ])

    add_formula_box(root, 255, 82, 225, 100, "Формулы", [
        "V = ⅓πR²h",
        "S_бок = πRl",
        "S_полн = πR(R + l)",
        "l² = R² + h²",
        "S_осн = πR²",
    ])

    add_content_box(root, 18, 190, 225, 95, "Свойства и сечения", [
        "• Осевое сечение — равнобедр. Δ",
        "• Сечение ⊥ оси — круг",
        "• Развёртка бок. пов. — сектор",
        "• Ус. конус: V=⅓πh(R²+Rr+r²)",
        "• S_бок ус. = π(R+r)l",
    ])

    # Cone illustration
    g = add_illustration_area(root, 255, 190, 225, 95)
    # Base ellipse
    ET.SubElement(g, 'ellipse').set('cx', '370'); g[-1].set('cy', '278'); g[-1].set('rx', '45'); g[-1].set('ry', '10')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.08'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')
    # Cone lines
    ET.SubElement(g, 'line').set('x1', '370'); g[-1].set('y1', '210'); g[-1].set('x2', '325'); g[-1].set('y2', '278')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    ET.SubElement(g, 'line').set('x1', '370'); g[-1].set('y1', '210'); g[-1].set('x2', '415'); g[-1].set('y2', '278')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    # Hidden base arc
    ET.SubElement(g, 'path').set('d', 'M325,278 Q370,295 415,278')
    g[-1].set('fill', 'none'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1'); g[-1].set('stroke-dasharray', '3,3')
    # Height line
    ET.SubElement(g, 'line').set('x1', '370'); g[-1].set('y1', '210'); g[-1].set('x2', '370'); g[-1].set('y2', '278')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1.5'); g[-1].set('stroke-dasharray', '4,3')
    # Labels
    t = ET.SubElement(g, 'text')
    t.set('x', '380'); t.set('y', '250'); t.set('font-family', 'Arial,sans-serif')
    t.set('font-size', '10'); t.set('fill', ACCENT); t.set('font-style', 'italic')
    t.text = 'h'
    t2 = ET.SubElement(g, 'text')
    t2.set('x', '390'); t2.set('y', '248'); t2.set('font-family', 'Arial,sans-serif')
    t2.set('font-size', '10'); t2.set('fill', PRIMARY_LIGHT); t2.set('font-style', 'italic')
    t2.text = 'l'
    # R line
    ET.SubElement(g, 'line').set('x1', '370'); g[-1].set('y1', '278'); g[-1].set('x2', '415'); g[-1].set('y2', '278')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1'); g[-1].set('stroke-dasharray', '3,2')
    t3 = ET.SubElement(g, 'text')
    t3.set('x', '395'); t3.set('y', '290'); t3.set('font-family', 'Arial,sans-serif')
    t3.set('font-size', '9'); t3.set('fill', ACCENT); t3.set('text-anchor', 'middle')
    t3.text = 'R'


def lesson6_sphere(root):
    """Сфера и шар - Sphere and ball."""
    add_content_box(root, 18, 82, 225, 100, "Определения", [
        "Сфера — поверхность, сост.",
        "из точек, равноудалённых от",
        "центра на расстояние R.",
        "",
        "Шар — тело, ограниченное",
        "сферой. R — радиус,",
        "d — диаметр, d = 2R",
    ])

    add_formula_box(root, 255, 82, 225, 100, "Формулы", [
        "S_сф = 4πR²",
        "V_шар = ⁴⁄₃πR³",
        "S_сеч = πr²  (r — радиус сеч.)",
        "r² = R² − d²  (d от центра)",
        "Уравн. сферы: x²+y²+z²=R²",
    ])

    add_content_box(root, 18, 190, 225, 95, "Свойства", [
        "• Все точки сферы = от центра",
        "• Сечение сферы — круг",
        "• Большой круг: r = R",
        "• Касательная плоскость ⊥ R",
        "• Шаровой сегмент, слой, сектор",
    ])

    # Sphere illustration
    g = add_illustration_area(root, 255, 190, 225, 95)
    # Main circle
    ET.SubElement(g, 'circle').set('cx', '370'); g[-1].set('cy', '248'); g[-1].set('r', '35')
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.08'); g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2')
    # Equator ellipse
    ET.SubElement(g, 'ellipse').set('cx', '370'); g[-1].set('cy', '248'); g[-1].set('rx', '35'); g[-1].set('ry', '12')
    g[-1].set('fill', 'none'); g[-1].set('stroke', PRIMARY_LIGHT); g[-1].set('stroke-width', '1'); g[-1].set('stroke-dasharray', '3,3')
    # Center dot
    ET.SubElement(g, 'circle').set('cx', '370'); g[-1].set('cy', '248'); g[-1].set('r', '2.5')
    g[-1].set('fill', ACCENT)
    # Radius line
    ET.SubElement(g, 'line').set('x1', '370'); g[-1].set('y1', '248'); g[-1].set('x2', '405'); g[-1].set('y2', '248')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '1.5')
    # R label
    t = ET.SubElement(g, 'text')
    t.set('x', '388'); t.set('y', '244'); t.set('font-family', 'Arial,sans-serif')
    t.set('font-size', '11'); t.set('fill', ACCENT); t.set('font-style', 'italic')
    t.text = 'R'
    # Vertical axis
    ET.SubElement(g, 'line').set('x1', '370'); g[-1].set('y1', '210'); g[-1].set('x2', '370'); g[-1].set('y2', '286')
    g[-1].set('stroke', PRIMARY_LIGHT); g[-1].set('stroke-width', '0.8'); g[-1].set('stroke-dasharray', '2,2')


def lesson7_volumes(root):
    """Объёмы тел - Volumes of bodies."""
    add_formula_box(root, 18, 82, 225, 108, "Объёмы основных тел", [
        "Призма:     V = S_осн · h",
        "Пирамида:    V = ⅓ · S_осн · h",
        "Цилиндр:     V = πR²h",
        "Конус:       V = ⅓πR²h",
        "Шар:         V = ⁴⁄₃πR³",
        "Ус. пирамида: V = ⅓h(S₁+√S₁S₂+S₂)",
    ])

    add_formula_box(root, 255, 82, 225, 108, "Объёмы (продолжение)", [
        "Ус. конус: V = ⅓πh(R²+Rr+r²)",
        "Цилиндр (общ.): V = S_осн · l",
        "Шар. сегмент: V = πh²(R−⅓h)",
        "Шар. слой: V = V_сегм₁ + V_сегм₂",
        "Шар. сектор: V = ⅔πR²h",
        "",
    ])

    add_content_box(root, 18, 198, 225, 95, "Принцип Кавальери", [
        "Если два тела заключены между",
        "параллельными плоскостями и",
        "площади сечений равны, то",
        "объёмы этих тел равны.",
        "",
        "Следствие: V = S_осн · h",
    ])

    add_content_box(root, 255, 198, 225, 95, "Отношения объёмов", [
      "• V_пир = ⅓ · V_приз (S, h те же)",
      "• V_кон = ⅓ · V_цил (R, h те же)",
      "• Подобные тела: V₁/V₂ = k³",
      "• V_шар = ⁴⁄₃πR³",
      "• Объём тетраэдра: V=⅓S·h",
    ])


def lesson8_areas(root):
    """Площади поверхностей - Surface areas."""
    add_formula_box(root, 18, 82, 225, 108, "Площади боковой поверхности", [
        "Призма (прямая): S_бок = P·h",
        "Пирамида (прав.): S_бок = ½P·l",
        "Цилиндр:  S_бок = 2πRh",
        "Конус:    S_бок = πRl",
        "Ус. конус: S_бок = π(R+r)l",
        "Ус. пир.(прав.): S_бок = ½(P₁+P₂)l",
    ])

    add_formula_box(root, 255, 82, 225, 108, "Площади полной поверхности", [
        "Призма: S = S_бок + 2S_осн",
        "Пирамида: S = S_бок + S_осн",
        "Цилиндр: S = 2πR(R + h)",
        "Конус:   S = πR(R + l)",
        "Сфера:   S = 4πR²",
        "Ус. конус: S = π(R+r)l + πR² + πr²",
    ])

    add_content_box(root, 18, 198, 462, 85, "Развёртки поверхностей", [
        "Цилиндр: прямоугольник (2πR × h) + 2 круга (πR²)     •     Конус: сектор (πRl по дуге 2πR) + круг (πR²)",
        "Призма: прямоугольники боковых граней + 2 основания   •     Пирамида: треугольники граней + основание",
        "Сфера: не имеет развёртки на плоскость (теорема)      •     S_сф = 4πR² — вывод через предел",
    ])


def lesson9_combinations(root):
    """Комбинации тел - Combinations of bodies."""
    add_content_box(root, 18, 82, 225, 108, "Шар и многогранник", [
        "Шар вписан в многогранник:",
        "  касается всех граней",
        "  R_впис = r (впис. сфера)",
        "",
        "Шар описан около многогран.:",
        "  все вершины на сфере",
        "  R_опис = R (опис. сфера)",
    ])

    add_content_box(root, 255, 82, 225, 108, "Типичные комбинации", [
        "• Шар вписан в цилиндр: R_ш = R",
        "  h = 2R (равностор. сечение)",
        "• Шар вписан в конус:",
        "  r = R·h/(R+l)",
        "• Конус вписан в шар:",
        "  R_ш = (h²+R²)/(2h)",
        "• Цилиндр вписан в шар:",
        "  R_ш² = R² + (h/2)²",
    ])

    add_formula_box(root, 18, 198, 225, 85, "Ключевые формулы", [
        "R_шара = abc/(4S)  (в ∆)",
        "r_впис = S/p  (в треугольник)",
        "R_оп.куб = a√3/2",
        "R_вп.куб = a/2",
    ])

    add_content_box(root, 255, 198, 225, 85, "Метод решения", [
        "1. Найти осевое сечение",
        "2. Свести к плоской задаче",
        "3. Использовать свойства",
        "   вписанных/описанных фигур",
        "4. Применить теорему Пифагора",
    ])


def lesson10_coordinates(root):
    """Координаты в пространстве - Coordinates in space."""
    add_content_box(root, 18, 82, 225, 108, "Прямоугольная система", [
        "Oxyz — декартова система",
        "координат в пространстве.",
        "",
        "Точка M(x, y, z):",
        "  x — абсцисса",
        "  y — ордината",
        "  z — аппликата",
    ])

    add_formula_box(root, 255, 82, 225, 108, "Формулы", [
        "d = √((x₂−x₁)²+(y₂−y₁)²+(z₂−z₁)²)",
        "M_серед = ((x₁+x₂)/2, (y₁+y₂)/2,",
        "           (z₁+z₂)/2)",
        "Уравн. плоскости: Ax+By+Cz+D=0",
        "Уравн. сферы:",
        "  (x−a)²+(y−b)²+(z−c)²=R²",
    ])

    add_content_box(root, 18, 198, 225, 85, "Координаты и плоскости", [
        "Плоскость xOy: z = 0",
        "Плоскость xOz: y = 0",
        "Плоскость yOz: x = 0",
        "Ось Ox: y = 0, z = 0",
        "Ось Oy: x = 0, z = 0",
    ])

    add_content_box(root, 255, 198, 225, 85, "Расстояние и угол", [
        "От точки до плоскости:",
        "  d = |Ax₀+By₀+Cz₀+D|/√(A²+B²+C²)",
        "Угол между плоскостями:",
        "  cos α = |A₁A₂+B₁B₂+C₁C₂|/",
        "         (√(A₁²+B₁²+C₁²)·√(A₂²+...))",
    ])


def lesson11_vectors(root):
    """Векторы в пространстве - Vectors in space."""
    add_content_box(root, 18, 82, 225, 100, "Определение", [
        "Вектор — направленный отрезок.",
        "a⃗ = AB⃗, где A — начало, B — конец",
        "",
        "Координаты: a⃗ = (x, y, z)",
        "Длина: |a⃗| = √(x² + y² + z²)",
        "Нулевой вектор: 0⃗ = (0, 0, 0)",
    ])

    add_formula_box(root, 255, 82, 225, 100, "Операции", [
        "a⃗+b⃗ = (x₁+x₂, y₁+y₂, z₁+z₂)",
        "a⃗−b⃗ = (x₁−x₂, y₁−y₂, z₁−z₂)",
        "k·a⃗ = (kx, ky, kz)",
        "a⃗·b⃗ = x₁x₂+y₁y₂+z₁z₂",
        "cosα = (a⃗·b⃗)/(|a⃗|·|b⃗|)",
    ])

    add_content_box(root, 18, 190, 225, 95, "Свойства", [
        "• Коммутативность: a⃗+b⃗ = b⃗+a⃗",
        "• Ассоциативность: (a⃗+b⃗)+c⃗ = a⃗+(b⃗+c⃗)",
        "• a⃗⊥b⃗ ⟺ a⃗·b⃗ = 0",
        "• a⃗∥b⃗ ⟺ a⃗ = k·b⃗",
        "• Коллинеарные векторы",
    ])

    add_formula_box(root, 255, 190, 225, 95, "Векторное произведение", [
        "a⃗ × b⃗ — вектор ⊥ a⃗ и ⊥ b⃗",
        "|a⃗ × b⃗| = |a⃗|·|b⃗|·sinα",
        "S_парал = |a⃗ × b⃗|",
        "S_треуг = ½|a⃗ × b⃗|",
        "Смешанное: (a⃗×b⃗)·c⃗ = V_парал",
    ])


def lesson12_coord_method(root):
    """Метод координат - Coordinate method."""
    add_content_box(root, 18, 82, 225, 100, "Суть метода", [
        "Геометрическая задача →",
        "алгебраическая с помощью",
        "системы координат.",
        "",
        "1. Ввести систему координат",
        "2. Записать координаты точек",
        "3. Вычислить алгебраически",
    ])

    add_formula_box(root, 255, 82, 225, 100, "Основные формулы", [
        "Угол между прямыми:",
        " cosα = |a⃗·b⃗|/(|a⃗|·|b⃗|)",
        "Угол прямой и плоск.:",
        " sinα = |a⃗·n⃗|/(|a⃗|·|n⃗|)",
        "Угол между плоскостями:",
        " cosα = |n₁⃗·n₂⃗|/(|n₁⃗|·|n₂⃗|)",
    ])

    add_content_box(root, 18, 190, 225, 95, "Уравнения", [
        "Прямая: (x−x₀)/a = (y−y₀)/b",
        "             = (z−z₀)/c",
        "Плоскость: Ax+By+Cz+D=0",
        "Нормаль: n⃗ = (A, B, C)",
        "Направл. вектор: s⃗ = (a,b,c)",
    ])

    add_content_box(root, 255, 190, 225, 95, "Применение", [
        "• Доказательство ⊥ и ∥",
        "• Вычисление расстояний",
        "• Нахождение углов",
        "• Вычисление площадей сеч.",
        "• Задачи C2 ЕГЭ",
    ])


# ============================================================
# MAIN
# ============================================================

LESSONS = [
    (1, "Призма", lesson1_prism),
    (2, "Пирамида", lesson2_pyramid),
    (3, "Правильные многогранники", lesson3_polyhedra),
    (4, "Цилиндр", lesson4_cylinder),
    (5, "Конус", lesson5_cone),
    (6, "Сфера и шар", lesson6_sphere),
    (7, "Объёмы тел", lesson7_volumes),
    (8, "Площади поверхностей", lesson8_areas),
    (9, "Комбинации тел", lesson9_combinations),
    (10, "Координаты в пространстве", lesson10_coordinates),
    (11, "Векторы в пространстве", lesson11_vectors),
    (12, "Метод координат", lesson12_coord_method),
]


def main():
    generated = 0
    errors = []

    for num, title, content_fn in LESSONS:
        try:
            root = build_svg(num, title, content_fn)
            filepath = os.path.join(OUTPUT_DIR, f"lesson{num}.svg")
            write_svg(root, filepath)

            # Validate as XML
            try:
                tree = ET.parse(filepath)
                tree.getroot()
                print(f"✓ lesson{num}.svg — {title} (valid XML)")
                generated += 1
            except ET.ParseError as e:
                errors.append(f"lesson{num}.svg: XML validation failed: {e}")
                print(f"✗ lesson{num}.svg — XML validation error: {e}")

        except Exception as e:
            errors.append(f"lesson{num}.svg: Generation failed: {e}")
            print(f"✗ lesson{num}.svg — Generation error: {e}")

    print(f"\n{'='*50}")
    print(f"Generated: {generated}/{len(LESSONS)} SVG files")
    if errors:
        print(f"Errors: {len(errors)}")
        for err in errors:
            print(f"  - {err}")
    else:
        print("All files generated and validated successfully!")


if __name__ == "__main__":
    main()
