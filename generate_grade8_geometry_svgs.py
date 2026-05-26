#!/usr/bin/env python3
"""Generate 12 detailed SVG files for Grade 8 Geometry lessons."""

import os
import xml.etree.ElementTree as ET

OUTPUT_DIR = "/home/z/my-project/school-curriculum-app/public/images/grades/8/geometry"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme — cyan/teal for geometry
PRIMARY = "#06B6D4"
PRIMARY_DARK = "#0891B2"
PRIMARY_LIGHT = "#22D3EE"
PRIMARY_LIGHTER = "#67E8F9"
BG = "#ECFEFF"
BG_LIGHT = "#FFFFFF"
BG_DARK = "#164E63"
TEXT_DARK = "#0E7490"
TEXT_MUTED = "#06B6D4"
ACCENT = "#F59E0B"
ACCENT2 = "#EF4444"
FORMULA_BG = "#FFF7ED"

NS = 'http://www.w3.org/2000/svg'
W, H = 800, 600


def svg_root():
    """Create base SVG element."""
    root = ET.Element('svg')
    root.set('xmlns', NS)
    root.set('width', str(W))
    root.set('height', str(H))
    root.set('viewBox', f'0 0 {W} {H}')
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
    s1.set('offset', '0%'); s1.set('stop-color', '#F0FDFA')
    s2 = ET.SubElement(grad, 'stop')
    s2.set('offset', '100%'); s2.set('stop-color', BG)
    # Header gradient
    hgrad = ET.SubElement(defs, 'linearGradient')
    hgrad.set('id', 'headerGrad')
    hgrad.set('x1', '0'); hgrad.set('y1', '0')
    hgrad.set('x2', '1'); hgrad.set('y2', '0')
    h1 = ET.SubElement(hgrad, 'stop')
    h1.set('offset', '0%'); h1.set('stop-color', PRIMARY_DARK)
    h2 = ET.SubElement(hgrad, 'stop')
    h2.set('offset', '100%'); h2.set('stop-color', PRIMARY)
    # Accent gradient
    agrad = ET.SubElement(defs, 'linearGradient')
    agrad.set('id', 'accentGrad')
    agrad.set('x1', '0'); agrad.set('y1', '0')
    agrad.set('x2', '1'); agrad.set('y2', '0')
    a1 = ET.SubElement(agrad, 'stop')
    a1.set('offset', '0%'); a1.set('stop-color', '#F59E0B')
    a2 = ET.SubElement(agrad, 'stop')
    a2.set('offset', '100%'); a1.set('stop-color', '#D97706')
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
    bg_rect.set('width', str(W)); bg_rect.set('height', str(H))
    bg_rect.set('fill', 'url(#bgGrad)'); bg_rect.set('rx', '12')

    # Outer border
    border = ET.SubElement(root, 'rect')
    border.set('x', '3'); border.set('y', '3')
    border.set('width', str(W - 6)); border.set('height', str(H - 6))
    border.set('rx', '10'); border.set('fill', 'none')
    border.set('stroke', PRIMARY); border.set('stroke-width', '2.5')

    # Inner decorative border
    inner = ET.SubElement(root, 'rect')
    inner.set('x', '8'); inner.set('y', '8')
    inner.set('width', str(W - 16)); inner.set('height', str(H - 16))
    inner.set('rx', '8'); inner.set('fill', 'none')
    inner.set('stroke', PRIMARY); inner.set('stroke-width', '1')
    inner.set('opacity', '0.2')

    # Corner decorations (small triangles)
    corners = [
        (f"12,12 42,12 12,42", "0.08"),
        (f"{W-12},12 {W-42},12 {W-12},42", "0.08"),
        (f"12,{H-12} 42,{H-12} 12,{H-42}", "0.08"),
        (f"{W-12},{H-12} {W-42},{H-12} {W-12},{H-42}", "0.08"),
    ]
    for pts, op in corners:
        p = ET.SubElement(root, 'polygon')
        p.set('points', pts); p.set('fill', PRIMARY); p.set('opacity', op)

    # Decorative geometric shapes in background
    # Small circle top-right area
    ET.SubElement(root, 'circle').set('cx', '740')
    root[-1].set('cy', '100'); root[-1].set('r', '25')
    root[-1].set('fill', 'none'); root[-1].set('stroke', PRIMARY)
    root[-1].set('stroke-width', '1'); root[-1].set('opacity', '0.1')

    # Small triangle bottom-left area
    ET.SubElement(root, 'polygon').set('points', '60,540 80,510 100,540')
    root[-1].set('fill', 'none'); root[-1].set('stroke', PRIMARY)
    root[-1].set('stroke-width', '1'); root[-1].set('opacity', '0.1')

    # Small square top-left area
    ET.SubElement(root, 'rect').set('x', '70')
    root[-1].set('y', '80'); root[-1].set('width', '18')
    root[-1].set('height', '18'); root[-1].set('fill', 'none')
    root[-1].set('stroke', PRIMARY); root[-1].set('stroke-width', '1')
    root[-1].set('opacity', '0.08')
    # Rotate it 45 degrees for diamond shape
    root[-1].set('transform', 'rotate(45, 79, 89)')


def add_header(root, title, lesson_num):
    """Add header with title and lesson number."""
    # Header background bar
    hdr = ET.SubElement(root, 'rect')
    hdr.set('x', '15'); hdr.set('y', '15')
    hdr.set('width', str(W - 30)); hdr.set('height', '55')
    hdr.set('fill', 'url(#headerGrad)'); hdr.set('rx', '8')
    hdr.set('opacity', '0.92')

    # Lesson number badge
    badge = ET.SubElement(root, 'rect')
    badge.set('x', '25'); badge.set('y', '22')
    badge.set('width', '50'); badge.set('height', '38')
    badge.set('fill', '#FFFFFF'); badge.set('rx', '6')
    badge.set('opacity', '0.25')

    # Lesson number text
    nt = ET.SubElement(root, 'text')
    nt.set('x', '50'); nt.set('y', '49')
    nt.set('font-family', 'Arial,sans-serif'); nt.set('font-size', '22')
    nt.set('font-weight', 'bold'); nt.set('fill', '#FFFFFF')
    nt.set('text-anchor', 'middle')
    nt.text = str(lesson_num)

    # Title
    t = ET.SubElement(root, 'text')
    t.set('x', str(W // 2 + 10)); t.set('y', '48')
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '24')
    t.set('font-weight', 'bold'); t.set('fill', '#FFFFFF')
    t.set('text-anchor', 'middle')
    t.text = title

    # Subject label
    st = ET.SubElement(root, 'text')
    st.set('x', str(W - 40)); st.set('y', '35')
    st.set('font-family', 'Arial,sans-serif'); st.set('font-size', '10')
    st.set('fill', '#FFFFFF'); st.set('text-anchor', 'end')
    st.set('opacity', '0.7')
    st.text = "8 класс"

    # Subject label 2
    st2 = ET.SubElement(root, 'text')
    st2.set('x', str(W - 40)); st2.set('y', '50')
    st2.set('font-family', 'Arial,sans-serif'); st2.set('font-size', '10')
    st2.set('fill', '#FFFFFF'); st2.set('text-anchor', 'end')
    st2.set('opacity', '0.7')
    st2.text = "Геометрия"

    # Separator line
    line = ET.SubElement(root, 'line')
    line.set('x1', '20'); line.set('y1', '80')
    line.set('x2', str(W - 20)); line.set('y2', '80')
    line.set('stroke', PRIMARY); line.set('stroke-width', '2')
    line.set('opacity', '0.25')


def add_footer(root):
    """Add footer."""
    # Footer background
    fb = ET.SubElement(root, 'rect')
    fb.set('x', '15'); fb.set('y', str(H - 40))
    fb.set('width', str(W - 30)); fb.set('height', '28')
    fb.set('fill', 'url(#panelGrad)'); fb.set('opacity', '0.08')
    fb.set('rx', '6')

    # Footer text
    ft = ET.SubElement(root, 'text')
    ft.set('x', str(W // 2)); ft.set('y', str(H - 22))
    ft.set('font-family', 'Arial,sans-serif'); ft.set('font-size', '11')
    ft.set('fill', PRIMARY); ft.set('text-anchor', 'middle')
    ft.set('opacity', '0.6')
    ft.text = "Геометрия \u00b7 8 класс"

    # Decorative protractor icon (left side of footer)
    ET.SubElement(root, 'circle').set('cx', '35')
    root[-1].set('cy', str(H - 26)); root[-1].set('r', '8')
    root[-1].set('fill', 'none'); root[-1].set('stroke', PRIMARY)
    root[-1].set('stroke-width', '1'); root[-1].set('opacity', '0.3')
    # Compass icon (right side)
    ET.SubElement(root, 'circle').set('cx', str(W - 35))
    root[-1].set('cy', str(H - 26)); root[-1].set('r', '8')
    root[-1].set('fill', 'none'); root[-1].set('stroke', PRIMARY)
    root[-1].set('stroke-width', '1'); root[-1].set('opacity', '0.3')


def add_content_box(root, x, y, w, h, title, lines, box_id=""):
    """Add a content box with title and text lines."""
    # Shadow
    shadow = ET.SubElement(root, 'rect')
    shadow.set('x', str(x + 3)); shadow.set('y', str(y + 3))
    shadow.set('width', str(w)); shadow.set('height', str(h))
    shadow.set('fill', '#000000'); shadow.set('rx', '8')
    shadow.set('opacity', '0.05')

    # Box background
    box = ET.SubElement(root, 'rect')
    box.set('x', str(x)); box.set('y', str(y))
    box.set('width', str(w)); box.set('height', str(h))
    box.set('fill', BG_LIGHT); box.set('rx', '8')
    box.set('stroke', PRIMARY); box.set('stroke-width', '1.5')
    box.set('opacity', '0.95')

    # Title bar
    tbar = ET.SubElement(root, 'rect')
    tbar.set('x', str(x)); tbar.set('y', str(y))
    tbar.set('width', str(w)); tbar.set('height', '24')
    tbar.set('fill', PRIMARY); tbar.set('rx', '8')
    tbar.set('opacity', '0.15')

    # Cover bottom corners of title bar
    tbc = ET.SubElement(root, 'rect')
    tbc.set('x', str(x)); tbc.set('y', str(y + 16))
    tbc.set('width', str(w)); tbc.set('height', '8')
    tbc.set('fill', PRIMARY); tbc.set('opacity', '0.15')

    # Box title
    bt = ET.SubElement(root, 'text')
    bt.set('x', str(x + w // 2)); bt.set('y', str(y + 17))
    bt.set('font-family', 'Arial,sans-serif'); bt.set('font-size', '12')
    bt.set('font-weight', 'bold'); bt.set('fill', TEXT_DARK)
    bt.set('text-anchor', 'middle')
    bt.text = title

    # Content lines
    for i, line in enumerate(lines):
        lt = ET.SubElement(root, 'text')
        lt.set('x', str(x + 12)); lt.set('y', str(y + 40 + i * 17))
        lt.set('font-family', 'Arial,sans-serif'); lt.set('font-size', '12')
        lt.set('fill', '#37474F')
        lt.text = line


def add_formula_box(root, x, y, w, h, title, formulas):
    """Add a formula box with highlighted formulas."""
    # Shadow
    shadow = ET.SubElement(root, 'rect')
    shadow.set('x', str(x + 3)); shadow.set('y', str(y + 3))
    shadow.set('width', str(w)); shadow.set('height', str(h))
    shadow.set('fill', '#000000'); shadow.set('rx', '8')
    shadow.set('opacity', '0.05')

    # Box background
    box = ET.SubElement(root, 'rect')
    box.set('x', str(x)); box.set('y', str(y))
    box.set('width', str(w)); box.set('height', str(h))
    box.set('fill', FORMULA_BG); box.set('rx', '8')
    box.set('stroke', ACCENT); box.set('stroke-width', '2')
    box.set('opacity', '0.95')

    # Title bar
    tbar = ET.SubElement(root, 'rect')
    tbar.set('x', str(x)); tbar.set('y', str(y))
    tbar.set('width', str(w)); tbar.set('height', '24')
    tbar.set('fill', ACCENT); tbar.set('rx', '8')
    tbar.set('opacity', '0.2')

    tbc = ET.SubElement(root, 'rect')
    tbc.set('x', str(x)); tbc.set('y', str(y + 16))
    tbc.set('width', str(w)); tbc.set('height', '8')
    tbc.set('fill', ACCENT); tbc.set('opacity', '0.2')

    # Title
    bt = ET.SubElement(root, 'text')
    bt.set('x', str(x + w // 2)); bt.set('y', str(y + 17))
    bt.set('font-family', 'Arial,sans-serif'); bt.set('font-size', '12')
    bt.set('font-weight', 'bold'); bt.set('fill', '#92400E')
    bt.set('text-anchor', 'middle')
    bt.text = title

    # Formulas
    for i, formula in enumerate(formulas):
        ft = ET.SubElement(root, 'text')
        ft.set('x', str(x + 12)); ft.set('y', str(y + 40 + i * 18))
        ft.set('font-family', 'Arial,sans-serif'); ft.set('font-size', '12')
        ft.set('fill', '#92400E'); ft.set('font-weight', 'bold')
        ft.text = formula


def add_illustration_area(root, x, y, w, h, clip_id="ill"):
    """Add an illustration area with clipping."""
    defs = root.find(f'{{{NS}}}defs')
    if defs is None:
        for child in root:
            if child.tag == 'defs' or child.tag == f'{{{NS}}}defs':
                defs = child
                break
    if defs is None:
        defs = ET.SubElement(root, 'defs')
    clip = ET.SubElement(defs, 'clipPath')
    clip.set('id', clip_id)
    cr = ET.SubElement(clip, 'rect')
    cr.set('x', str(x)); cr.set('y', str(y))
    cr.set('width', str(w)); cr.set('height', str(h))
    cr.set('rx', '8')

    g = ET.SubElement(root, 'g')
    g.set('clip-path', f'url(#{clip_id})')

    # Background
    ill_bg = ET.SubElement(g, 'rect')
    ill_bg.set('x', str(x)); ill_bg.set('y', str(y))
    ill_bg.set('width', str(w)); ill_bg.set('height', str(h))
    ill_bg.set('fill', '#F0FDFA'); ill_bg.set('opacity', '0.6')

    # Border
    ill_border = ET.SubElement(g, 'rect')
    ill_border.set('x', str(x)); ill_border.set('y', str(y))
    ill_border.set('width', str(w)); ill_border.set('height', str(h))
    ill_border.set('fill', 'none'); ill_border.set('rx', '8')
    ill_border.set('stroke', PRIMARY); ill_border.set('stroke-width', '1.5')
    ill_border.set('opacity', '0.4')

    return g


def add_decorative_shape(g, shape_type, cx, cy, size, color=PRIMARY, opacity=0.15):
    """Add a small decorative geometric shape."""
    if shape_type == 'triangle':
        pts = f"{cx},{cy-size} {cx-size*0.87},{cy+size*0.5} {cx+size*0.87},{cy+size*0.5}"
        p = ET.SubElement(g, 'polygon')
        p.set('points', pts); p.set('fill', color); p.set('opacity', str(opacity))
        p.set('stroke', color); p.set('stroke-width', '1')
    elif shape_type == 'square':
        r = ET.SubElement(g, 'rect')
        r.set('x', str(cx - size)); r.set('y', str(cy - size))
        r.set('width', str(size * 2)); r.set('height', str(size * 2))
        r.set('fill', color); r.set('opacity', str(opacity))
        r.set('stroke', color); r.set('stroke-width', '1')
    elif shape_type == 'circle':
        c = ET.SubElement(g, 'circle')
        c.set('cx', str(cx)); c.set('cy', str(cy)); c.set('r', str(size))
        c.set('fill', color); c.set('opacity', str(opacity))
        c.set('stroke', color); c.set('stroke-width', '1')


def add_labeled_polygon(g, points, labels, color=PRIMARY, fill_opacity=0.1, stroke_width=2):
    """Draw a polygon with vertex labels."""
    pts_str = " ".join(f"{x},{y}" for x, y in points)
    p = ET.SubElement(g, 'polygon')
    p.set('points', pts_str); p.set('fill', color)
    p.set('opacity', str(fill_opacity)); p.set('stroke', color)
    p.set('stroke-width', str(stroke_width))

    # Labels
    for i, (label, (lx, ly)) in enumerate(zip(labels, points)):
        t = ET.SubElement(g, 'text')
        # Offset label outward
        cx = sum(p[0] for p in points) / len(points)
        cy = sum(p[1] for p in points) / len(points)
        dx = lx - cx
        dy = ly - cy
        dist = (dx**2 + dy**2) ** 0.5
        if dist > 0:
            offset = 14
            tx = lx + dx / dist * offset
            ty = ly + dy / dist * offset
        else:
            tx, ty = lx, ly
        t.set('x', str(int(tx))); t.set('y', str(int(ty) + 4))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '13')
        t.set('font-weight', 'bold'); t.set('fill', color)
        t.set('text-anchor', 'middle')
        t.text = label


def add_labeled_line(g, x1, y1, x2, y2, label, color=ACCENT, dasharray=None):
    """Draw a line with a label in the middle."""
    line = ET.SubElement(g, 'line')
    line.set('x1', str(x1)); line.set('y1', str(y1))
    line.set('x2', str(x2)); line.set('y2', str(y2))
    line.set('stroke', color); line.set('stroke-width', '2')
    if dasharray:
        line.set('stroke-dasharray', dasharray)

    if label:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        t = ET.SubElement(g, 'text')
        t.set('x', str(int(mx))); t.set('y', str(int(my) - 6))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '12')
        t.set('font-weight', 'bold'); t.set('fill', color)
        t.set('text-anchor', 'middle'); t.set('font-style', 'italic')
        t.text = label


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

def lesson1_polygons(root):
    """Многоугольники — polygons, sum of angles, diagonals, exterior angles."""
    # Left: Definition box
    add_content_box(root, 20, 90, 370, 130, "Определение", [
        "Многоугольник — фигура, состоящая",
        "из n точек (вершин) и n отрезков",
        "(сторон), последовательно их",
        "соединяющих.",
        "",
        "Выпуклый многоугольник лежит по",
        "одну сторону от каждой прямой,",
        "проходящей через его сторону.",
    ])

    # Right: Formula box
    add_formula_box(root, 410, 90, 370, 130, "Формулы", [
        "Сумма углов: S = (n \u2212 2) \u00b7 180\u00b0",
        "",
        "Число диагоналей из одной вершины:",
        "  d = n \u2212 3",
        "",
        "Все диагонали: D = n(n \u2212 3) / 2",
        "",
        "Внешний угол: \u03b2 = 180\u00b0 \u2212 \u03b1",
    ])

    # Bottom left: Properties
    add_content_box(root, 20, 235, 370, 130, "Свойства", [
        "\u2022 Сумма внешних углов = 360\u00b0",
        "\u2022 Правильный: все стороны и углы равны",
        "\u2022 Внутренний угол прав. мн-ка:",
        "  \u03b1 = (n \u2212 2) \u00b7 180\u00b0 / n",
        "\u2022 Внешний угол прав. мн-ка:",
        "  \u03b2 = 360\u00b0 / n",
        "\u2022 Число треугольников при разбиении:",
        "  T = n \u2212 2",
    ])

    # Bottom right: Illustration — pentagon with diagonals
    g = add_illustration_area(root, 410, 235, 370, 130, "ill1")
    # Pentagon
    cx, cy, r = 595, 295, 50
    pts = []
    for i in range(5):
        import math
        angle = math.radians(-90 + i * 72)
        pts.append((int(cx + r * math.cos(angle)), int(cy + r * math.sin(angle))))

    pts_str = " ".join(f"{x},{y}" for x, y in pts)
    p = ET.SubElement(g, 'polygon')
    p.set('points', pts_str); p.set('fill', PRIMARY); p.set('opacity', '0.1')
    p.set('stroke', PRIMARY); p.set('stroke-width', '2')

    # Diagonals
    for i in range(5):
        for j in range(i + 2, 5):
            if j == (i + 4) % 5 + i + 1 - 1 and i == 0:
                continue  # skip the side
            if abs(i - j) == 1 or (i == 0 and j == 4):
                continue  # skip sides
            line = ET.SubElement(g, 'line')
            line.set('x1', str(pts[i][0])); line.set('y1', str(pts[i][1]))
            line.set('x2', str(pts[j][0])); line.set('y2', str(pts[j][1]))
            line.set('stroke', ACCENT); line.set('stroke-width', '1')
            line.set('stroke-dasharray', '4,3')

    # Vertex labels
    labels = ['A', 'B', 'C', 'D', 'E']
    for i, (label, (lx, ly)) in enumerate(zip(labels, pts)):
        angle = math.radians(-90 + i * 72)
        tx = lx + 14 * math.cos(angle)
        ty = ly + 14 * math.sin(angle) + 4
        t = ET.SubElement(g, 'text')
        t.set('x', str(int(tx))); t.set('y', str(int(ty)))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '13')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.set('text-anchor', 'middle')
        t.text = label

    # Caption
    t2 = ET.SubElement(g, 'text')
    t2.set('x', '595'); t2.set('y', '360')
    t2.set('font-family', 'Arial,sans-serif'); t2.set('font-size', '11')
    t2.set('fill', PRIMARY); t2.set('text-anchor', 'middle'); t2.set('opacity', '0.8')
    t2.text = 'Пятиугольник и его диагонали'

    # Bottom: Table of angle sums
    add_content_box(root, 20, 380, 760, 60, "Таблица: сумма углов многоугольников", [
        "n=3: S=180\u00b0    n=4: S=360\u00b0    n=5: S=540\u00b0    n=6: S=720\u00b0    n=8: S=1080\u00b0    n=10: S=1440\u00b0    n=12: S=1800\u00b0",
    ])

    # Additional: Example
    add_formula_box(root, 20, 455, 760, 80, "Пример", [
        "Сколько диагоналей у выпуклого шестиугольника?",
        "D = n(n \u2212 3) / 2 = 6(6 \u2212 3) / 2 = 6 \u00b7 3 / 2 = 9 диагоналей",
        "Сумма углов: S = (6 \u2212 2) \u00b7 180\u00b0 = 4 \u00b7 180\u00b0 = 720\u00b0",
    ])


def lesson2_parallelogram(root):
    """Параллелограмм — parallelogram, properties."""
    add_content_box(root, 20, 90, 370, 110, "Определение", [
        "Параллелограмм — четырёхугольник,",
        "у которого противоположные",
        "стороны попарно параллельны.",
        "",
        "ABCD: AB \u2225 CD, BC \u2225 AD",
    ])

    add_formula_box(root, 410, 90, 370, 110, "Свойства", [
        "1. AB = CD, BC = AD (стороны)",
        "2. \u2220A = \u2220C, \u2220B = \u2220D (углы)",
        "3. AO = OC, BO = OD (диагонали)",
        "4. \u2220A + \u2220B = 180\u00b0",
        "5. S = a \u00b7 h",
    ])

    # Illustration: Parallelogram
    g = add_illustration_area(root, 20, 215, 380, 170, "ill2")
    # Parallelogram vertices
    pa = (120, 310)
    pb = (300, 310)
    pc = (350, 240)
    pd = (170, 240)

    pts_str = f"{pa[0]},{pa[1]} {pb[0]},{pb[1]} {pc[0]},{pc[1]} {pd[0]},{pd[1]}"
    p = ET.SubElement(g, 'polygon')
    p.set('points', pts_str); p.set('fill', PRIMARY); p.set('opacity', '0.08')
    p.set('stroke', PRIMARY); p.set('stroke-width', '2.5')

    # Diagonals
    add_labeled_line(g, pa[0], pa[1], pc[0], pc[1], "", PRIMARY, "5,4")
    add_labeled_line(g, pb[0], pb[1], pd[0], pd[1], "", PRIMARY, "5,4")

    # Intersection point O
    ox, oy = (pa[0] + pc[0]) // 2, (pa[1] + pc[1]) // 2
    ET.SubElement(g, 'circle').set('cx', str(ox))
    g[-1].set('cy', str(oy)); g[-1].set('r', '4')
    g[-1].set('fill', ACCENT)

    # Labels
    for label, (lx, ly), offset in [('A', pa, (-12, 8)), ('B', pb, (8, 8)),
                                      ('C', pc, (8, -5)), ('D', pd, (-12, -5))]:
        t = ET.SubElement(g, 'text')
        t.set('x', str(lx + offset[0])); t.set('y', str(ly + offset[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '14')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label

    # O label
    t = ET.SubElement(g, 'text')
    t.set('x', str(ox + 8)); t.set('y', str(oy - 4))
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '12')
    t.set('font-weight', 'bold'); t.set('fill', ACCENT)
    t.text = 'O'

    # Height line
    add_labeled_line(g, pd[0], pd[1], pd[0], pa[1], "h", ACCENT2, "3,2")

    # Side labels
    t = ET.SubElement(g, 'text')
    t.set('x', str((pa[0] + pb[0]) // 2)); t.set('y', str(pa[1] + 18))
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '12')
    t.set('fill', PRIMARY); t.set('font-style', 'italic'); t.set('text-anchor', 'middle')
    t.text = 'a'

    # Parallel marks
    t2 = ET.SubElement(g, 'text')
    t2.set('x', str((pd[0] + pc[0]) // 2 + 8)); t2.set('y', str((pd[1] + pc[1]) // 2 - 8))
    t2.set('font-family', 'Arial,sans-serif'); t2.set('font-size', '12')
    t2.set('fill', PRIMARY); t2.set('font-style', 'italic')
    t2.text = 'a'

    # Caption
    tc = ET.SubElement(g, 'text')
    tc.set('x', '210'); tc.set('y', '380')
    tc.set('font-family', 'Arial,sans-serif'); tc.set('font-size', '11')
    tc.set('fill', PRIMARY); tc.set('text-anchor', 'middle'); tc.set('opacity', '0.8')
    tc.text = 'ABCD \u2014 параллелограмм'

    # Right: Signs of parallelogram
    add_content_box(root, 410, 215, 370, 170, "Признаки параллелограмма", [
        "1. AB = CD и AB \u2225 CD",
        "   (одна пара равных и паралл.)",
        "2. AB = CD и BC = AD",
        "   (обе пары сторон равны)",
        "3. AO = OC и BO = OD",
        "   (диагонали точкой делятся",
        "   пополам)",
        "4. \u2220A = \u2220C и \u2220B = \u2220D",
        "   (обе пары углов равны)",
    ])

    # Bottom: Area and special cases
    add_formula_box(root, 20, 400, 760, 70, "Площадь параллелограмма", [
        "S = a \u00b7 h   где a \u2014 основание, h \u2014 высота     |     S = d\u2081 \u00b7 d\u2082 \u00b7 sin(\u03b1) / 2   где \u03b1 \u2014 угол между диагоналями",
    ])

    add_content_box(root, 20, 485, 760, 55, "Частные случаи", [
        "\u2022 Прямоугольник \u2014 все углы 90\u00b0     \u2022 Ромб \u2014 все стороны равны     \u2022 Квадрат \u2014 прямоугольник и ромб одновременно",
    ])


def lesson3_rect_rhombus_square(root):
    """Прямоугольник, ромб, квадрат — rectangle, rhombus, square."""
    # Three columns for each shape
    # Rectangle
    add_content_box(root, 20, 90, 245, 100, "Прямоугольник", [
        "\u2022 Все углы = 90\u00b0",
        "\u2022 Противоп. стороны равны",
        "\u2022 Диагонали равны: d\u2081 = d\u2082",
        "\u2022 Диагонали делятся пополам",
        "\u2022 S = a \u00b7 b",
    ])

    # Rhombus
    add_content_box(root, 280, 90, 245, 100, "Ромб", [
        "\u2022 Все стороны равны: a = b",
        "\u2022 Диагонали \u22a5 друг другу",
        "\u2022 Диагонали \u2014 биссектрисы",
        "\u2022 S = d\u2081 \u00b7 d\u2082 / 2",
        "\u2022 S = a\u00b2 \u00b7 sin(\u03b1)",
    ])

    # Square
    add_content_box(root, 540, 90, 240, 100, "Квадрат", [
        "\u2022 Все стороны = a",
        "\u2022 Все углы = 90\u00b0",
        "\u2022 d = a\u221a2",
        "\u2022 S = a\u00b2",
        "\u2022 Диагонали \u22a5 и равны",
    ])

    # Illustrations for each shape
    # Rectangle illustration
    g1 = add_illustration_area(root, 20, 205, 245, 155, "ill3a")
    # Draw rectangle
    rect_pts = "80,240 220,240 220,310 80,310"
    p1 = ET.SubElement(g1, 'polygon')
    p1.set('points', rect_pts); p1.set('fill', PRIMARY); p1.set('opacity', '0.08')
    p1.set('stroke', PRIMARY); p1.set('stroke-width', '2')
    # Diagonal
    add_labeled_line(g1, 80, 240, 220, 310, "d", ACCENT, "4,3")
    add_labeled_line(g1, 220, 240, 80, 310, "d", ACCENT, "4,3")
    # Labels
    for label, (lx, ly), off in [('A', (80, 240), (-12, -5)), ('B', (220, 240), (8, -5)),
                                   ('C', (220, 310), (8, 12)), ('D', (80, 310), (-12, 12))]:
        t = ET.SubElement(g1, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '12')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label
    # Side labels
    t = ET.SubElement(g1, 'text')
    t.set('x', '150'); t.set('y', '237')
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '11')
    t.set('fill', ACCENT2); t.set('text-anchor', 'middle'); t.set('font-style', 'italic')
    t.text = 'a'
    t2 = ET.SubElement(g1, 'text')
    t2.set('x', '228'); t2.set('y', '280')
    t2.set('font-family', 'Arial,sans-serif'); t2.set('font-size', '11')
    t2.set('fill', ACCENT2); t2.set('font-style', 'italic')
    t2.text = 'b'

    # Right angle marks at corners
    for rx, ry in [(80, 240), (220, 240), (220, 310), (80, 310)]:
        ET.SubElement(g1, 'rect').set('x', str(rx + (5 if rx == 80 else -10)))
        g1[-1].set('y', str(ry + (5 if ry == 240 else -10)))
        g1[-1].set('width', '5'); g1[-1].set('height', '5')
        g1[-1].set('fill', 'none'); g1[-1].set('stroke', PRIMARY)
        g1[-1].set('stroke-width', '0.8'); g1[-1].set('opacity', '0.5')

    # Rhombus illustration
    g2 = add_illustration_area(root, 280, 205, 245, 155, "ill3b")
    rh_pts = "402,235 452,275 402,315 352,275"
    p2 = ET.SubElement(g2, 'polygon')
    p2.set('points', rh_pts); p2.set('fill', PRIMARY); p2.set('opacity', '0.08')
    p2.set('stroke', PRIMARY); p2.set('stroke-width', '2')
    # Diagonals (perpendicular)
    add_labeled_line(g2, 402, 235, 402, 315, "d\u2082", ACCENT, "4,3")
    add_labeled_line(g2, 352, 275, 452, 275, "d\u2081", ACCENT, "4,3")
    # Right angle mark at center
    ET.SubElement(g2, 'rect').set('x', '402')
    g2[-1].set('y', '275'); g2[-1].set('width', '6')
    g2[-1].set('height', '6'); g2[-1].set('fill', 'none')
    g2[-1].set('stroke', ACCENT2); g2[-1].set('stroke-width', '1')
    # Labels
    for label, (lx, ly), off in [('A', (402, 235), (-10, -8)), ('B', (452, 275), (8, 4)),
                                   ('C', (402, 315), (-10, 14)), ('D', (352, 275), (-16, 4))]:
        t = ET.SubElement(g2, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '12')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label

    # Square illustration
    g3 = add_illustration_area(root, 540, 205, 240, 155, "ill3c")
    sq_pts = "610,240 690,240 690,320 610,320"
    p3 = ET.SubElement(g3, 'polygon')
    p3.set('points', sq_pts); p3.set('fill', PRIMARY); p3.set('opacity', '0.08')
    p3.set('stroke', PRIMARY); p3.set('stroke-width', '2')
    add_labeled_line(g3, 610, 240, 690, 320, "d", ACCENT, "4,3")
    add_labeled_line(g3, 690, 240, 610, 320, "d", ACCENT, "4,3")
    # Side label
    t = ET.SubElement(g3, 'text')
    t.set('x', '650'); t.set('y', '237')
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '11')
    t.set('fill', ACCENT2); t.set('text-anchor', 'middle'); t.set('font-style', 'italic')
    t.text = 'a'

    # Bottom: Comparison table
    add_content_box(root, 20, 375, 760, 85, "Сравнительная таблица свойств", [
        "Свойство              | Прямоугольник | Ромб        | Квадрат",
        "\u22a5 диагонали           | \u2014             | +           | +",
        "= диагонали           | +             | \u2014           | +",
        "Диаг. \u2014 биссектрисы   | \u2014             | +           | +",
        "Все стороны равны     | \u2014             | +           | +",
    ])

    # Formula summary
    add_formula_box(root, 20, 475, 760, 75, "Формулы площадей", [
        "Прямоугольник: S = a \u00b7 b        Ромб: S = d\u2081 \u00b7 d\u2082 / 2 = a\u00b2 \u00b7 sin(\u03b1)        Квадрат: S = a\u00b2 = d\u00b2 / 2",
    ])


def lesson4_trapezoid(root):
    """Трапеция — trapezoid, midline, area, isosceles trapezoid."""
    add_content_box(root, 20, 90, 370, 110, "Определение", [
        "Трапеция \u2014 четырёхугольник, у",
        "которого две стороны параллельны",
        "(основания), а две другие \u2014 нет",
        "(боковые стороны).",
        "",
        "AD \u2225 BC \u2014 основания",
        "AB, CD \u2014 боковые стороны",
    ])

    add_formula_box(root, 410, 90, 370, 110, "Формулы", [
        "Средняя линия: m = (a + b) / 2",
        "",
        "Площадь: S = (a + b) / 2 \u00b7 h",
        "",
        "S = m \u00b7 h",
    ])

    # Illustration: Trapezoid
    g = add_illustration_area(root, 20, 215, 380, 175, "ill4")
    # Trapezoid vertices
    ta = (80, 350)
    tb = (300, 350)
    tc = (260, 270)
    td = (120, 270)

    pts_str = f"{ta[0]},{ta[1]} {tb[0]},{tb[1]} {tc[0]},{tc[1]} {td[0]},{td[1]}"
    p = ET.SubElement(g, 'polygon')
    p.set('points', pts_str); p.set('fill', PRIMARY); p.set('opacity', '0.08')
    p.set('stroke', PRIMARY); p.set('stroke-width', '2.5')

    # Midline
    m1 = ((ta[0] + td[0]) // 2, (ta[1] + td[1]) // 2)
    m2 = ((tb[0] + tc[0]) // 2, (tb[1] + tc[1]) // 2)
    add_labeled_line(g, m1[0], m1[1], m2[0], m2[1], "m", ACCENT2, "5,3")

    # Height
    add_labeled_line(g, td[0], td[1], td[0], ta[1], "h", ACCENT, "3,2")

    # Labels
    for label, (lx, ly), off in [('A', ta, (-12, 14)), ('B', tb, (8, 14)),
                                   ('C', tc, (8, -5)), ('D', td, (-12, -5))]:
        t = ET.SubElement(g, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '13')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label

    # Base labels
    t = ET.SubElement(g, 'text')
    t.set('x', str((ta[0] + tb[0]) // 2)); t.set('y', str(ta[1] + 16))
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '12')
    t.set('fill', ACCENT2); t.set('text-anchor', 'middle'); t.set('font-style', 'italic')
    t.text = 'a (AD)'

    t2 = ET.SubElement(g, 'text')
    t2.set('x', str((td[0] + tc[0]) // 2)); t2.set('y', str(td[1] - 8))
    t2.set('font-family', 'Arial,sans-serif'); t2.set('font-size', '12')
    t2.set('fill', ACCENT2); t.set('text-anchor', 'middle'); t2.set('font-style', 'italic')
    t2.text = 'b (BC)'

    # M1, M2 labels
    t3 = ET.SubElement(g, 'text')
    t3.set('x', str(m1[0] - 14)); t3.set('y', str(m1[1] + 4))
    t3.set('font-family', 'Arial,sans-serif'); t3.set('font-size', '10')
    t3.set('fill', ACCENT2); t3.set('font-weight', 'bold')
    t3.text = 'M\u2081'

    t4 = ET.SubElement(g, 'text')
    t4.set('x', str(m2[0] + 8)); t4.set('y', str(m2[1] + 4))
    t4.set('font-family', 'Arial,sans-serif'); t4.set('font-size', '10')
    t4.set('fill', ACCENT2); t4.set('font-weight', 'bold')
    t4.text = 'M\u2082'

    # Right: Properties of isosceles trapezoid
    add_content_box(root, 410, 215, 370, 175, "Равнобедренная трапеция", [
        "\u2022 Боковые стороны равны: AB = CD",
        "\u2022 Углы при основании равны:",
        "  \u2220A = \u2220D, \u2220B = \u2220C",
        "\u2022 Диагонали равны: AC = BD",
        "\u2022 Осевая симметрия",
        "\u2022 Можно вписать окружность,",
        "  если a + b = c + d",
        "  (сумма оснований = сумме",
        "  боковых сторон)",
    ])

    # Bottom: Types of trapezoids
    add_content_box(root, 20, 405, 370, 75, "Виды трапеций", [
        "\u2022 Равнобедренная (AB = CD)",
        "\u2022 Прямоугольная (\u2220A = 90\u00b0 или \u2220D = 90\u00b0)",
        "\u2022 Произвольная",
    ])

    add_formula_box(root, 410, 405, 370, 75, "Дополнительно", [
        "S = \u00bd \u00b7 (a + b) \u00b7 h",
        "h = c \u00b7 sin(\u03b1)  (c \u2014 бок. сторона)",
    ])


def lesson5_area_rect_square(root):
    """Площадь прямоугольника и квадрата."""
    add_content_box(root, 20, 90, 370, 95, "Площадь прямоугольника", [
        "Площадь прямоугольника равна",
        "произведению его смежных сторон.",
        "",
        "S = a \u00b7 b",
        "где a и b \u2014 длины смежных сторон",
    ])

    add_formula_box(root, 410, 90, 370, 95, "Площадь квадрата", [
        "S = a\u00b2",
        "",
        "где a \u2014 сторона квадрата",
        "",
        "Через диагональ: S = d\u00b2 / 2",
    ])

    # Rectangle illustration
    g1 = add_illustration_area(root, 20, 200, 380, 160, "ill5a")
    # Rectangle
    ET.SubElement(g1, 'rect').set('x', '100')
    g1[-1].set('y', '230'); g1[-1].set('width', '200')
    g1[-1].set('height', '100'); g1[-1].set('fill', PRIMARY)
    g1[-1].set('opacity', '0.1'); g1[-1].set('stroke', PRIMARY)
    g1[-1].set('stroke-width', '2.5')

    # Side labels
    t = ET.SubElement(g1, 'text')
    t.set('x', '200'); t.set('y', '225')
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '16')
    t.set('fill', ACCENT2); t.set('text-anchor', 'middle'); t.set('font-style', 'italic')
    t.set('font-weight', 'bold')
    t.text = 'a'

    t2 = ET.SubElement(g1, 'text')
    t2.set('x', '310'); t2.set('y', '285')
    t2.set('font-family', 'Arial,sans-serif'); t2.set('font-size', '16')
    t2.set('fill', ACCENT2); t2.set('font-style', 'italic'); t2.set('font-weight', 'bold')
    t2.text = 'b'

    # Formula inside
    t3 = ET.SubElement(g1, 'text')
    t3.set('x', '200'); t3.set('y', '285')
    t3.set('font-family', 'Arial,sans-serif'); t3.set('font-size', '18')
    t3.set('fill', TEXT_DARK); t3.set('text-anchor', 'middle')
    t3.set('font-weight', 'bold')
    t3.text = 'S = a \u00b7 b'

    # Unit grid lines (visual)
    for i in range(1, 5):
        line = ET.SubElement(g1, 'line')
        line.set('x1', str(100 + i * 40)); line.set('y1', '230')
        line.set('x2', str(100 + i * 40)); line.set('y2', '330')
        line.set('stroke', PRIMARY); line.set('stroke-width', '0.5')
        line.set('opacity', '0.2')
    for i in range(1, 2):
        line = ET.SubElement(g1, 'line')
        line.set('x1', '100'); line.set('y1', str(230 + i * 50))
        line.set('x2', '300'); line.set('y2', str(230 + i * 50))
        line.set('stroke', PRIMARY); line.set('stroke-width', '0.5')
        line.set('opacity', '0.2')

    # Square illustration
    g2 = add_illustration_area(root, 410, 200, 380, 160, "ill5b")
    # Square
    ET.SubElement(g2, 'rect').set('x', '530')
    g2[-1].set('y', '230'); g2[-1].set('width', '120')
    g2[-1].set('height', '120'); g2[-1].set('fill', PRIMARY)
    g2[-1].set('opacity', '0.1'); g2[-1].set('stroke', PRIMARY)
    g2[-1].set('stroke-width', '2.5')

    # Diagonal
    add_labeled_line(g2, 530, 230, 650, 350, "d", ACCENT, "4,3")

    # Side label
    t4 = ET.SubElement(g2, 'text')
    t4.set('x', '590'); t4.set('y', '225')
    t4.set('font-family', 'Arial,sans-serif'); t4.set('font-size', '16')
    t4.set('fill', ACCENT2); t4.set('text-anchor', 'middle')
    t4.set('font-style', 'italic'); t4.set('font-weight', 'bold')
    t4.text = 'a'

    # Formulas
    t5 = ET.SubElement(g2, 'text')
    t5.set('x', '590'); t5.set('y', '295')
    t5.set('font-family', 'Arial,sans-serif'); t5.set('font-size', '16')
    t5.set('fill', TEXT_DARK); t5.set('text-anchor', 'middle')
    t5.set('font-weight', 'bold')
    t5.text = 'S = a\u00b2'

    # Bottom: Units and examples
    add_content_box(root, 20, 375, 370, 80, "Единицы измерения площади", [
        "1 мм\u00b2, 1 см\u00b2, 1 дм\u00b2, 1 м\u00b2, 1 км\u00b2",
        "1 га = 10 000 м\u00b2 = 100 ар",
        "1 ар (сотка) = 100 м\u00b2",
        "1 км\u00b2 = 100 га",
    ])

    add_formula_box(root, 410, 375, 370, 80, "Примеры", [
        "a = 5 см, b = 8 см: S = 5\u00b78 = 40 см\u00b2",
        "a = 6 см: S = 6\u00b2 = 36 см\u00b2",
        "d = 10 см: S = 10\u00b2/2 = 50 см\u00b2",
    ])

    # Properties
    add_content_box(root, 20, 470, 760, 65, "Свойства площади", [
        "1. Равные фигуры имеют равные площади",
        "2. Площадь фигуры = сумме площадей её частей",
        "3. Площадь квадрата со стороной 1 \u2014 единица площади",
    ])


def lesson6_area_parallelogram_triangle(root):
    """Площадь параллелограмма и треугольника."""
    add_content_box(root, 20, 90, 370, 100, "Площадь параллелограмма", [
        "Площадь параллелограмма равна",
        "произведению основания на высоту.",
        "",
        "S = a \u00b7 h",
        "S = a \u00b7 b \u00b7 sin(\u03b1)",
    ])

    add_formula_box(root, 410, 90, 370, 100, "Площадь треугольника", [
        "S = \u00bd \u00b7 a \u00b7 h   (основная)",
        "",
        "S = \u00bd \u00b7 a \u00b7 b \u00b7 sin(\u03b3)",
        "",
        "S = \u221a(p(p\u2212a)(p\u2212b)(p\u2212c))  (Герон)",
    ])

    # Parallelogram illustration
    g1 = add_illustration_area(root, 20, 205, 380, 160, "ill6a")
    # Parallelogram
    pa = (100, 320); pb = (280, 320); pc = (330, 260); pd = (150, 260)
    pts = f"{pa[0]},{pa[1]} {pb[0]},{pb[1]} {pc[0]},{pc[1]} {pd[0]},{pd[1]}"
    ET.SubElement(g1, 'polygon').set('points', pts)
    g1[-1].set('fill', PRIMARY); g1[-1].set('opacity', '0.08')
    g1[-1].set('stroke', PRIMARY); g1[-1].set('stroke-width', '2.5')

    # Height line
    add_labeled_line(g1, pd[0], pd[1], pd[0], pa[1], "h", ACCENT, "3,2")
    # Base label
    t = ET.SubElement(g1, 'text')
    t.set('x', str((pa[0] + pb[0]) // 2)); t.set('y', str(pa[1] + 16))
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '14')
    t.set('fill', ACCENT2); t.set('text-anchor', 'middle'); t.set('font-style', 'italic')
    t.set('font-weight', 'bold')
    t.text = 'a'

    # Formula
    t2 = ET.SubElement(g1, 'text')
    t2.set('x', '200'); t2.set('y', '295')
    t2.set('font-family', 'Arial,sans-serif'); t2.set('font-size', '16')
    t2.set('fill', TEXT_DARK); t2.set('text-anchor', 'middle'); t2.set('font-weight', 'bold')
    t2.text = 'S = a \u00b7 h'

    # Hatching for height
    for i in range(3):
        lx = pd[0] + 3 + i * 4
        ET.SubElement(g1, 'line').set('x1', str(lx))
        g1[-1].set('y1', str(pd[1] - 3)); g1[-1].set('x2', str(lx - 4))
        g1[-1].set('y2', str(pd[1])); g1[-1].set('stroke', ACCENT)
        g1[-1].set('stroke-width', '1'); g1[-1].set('opacity', '0.6')

    # Triangle illustration
    g2 = add_illustration_area(root, 410, 205, 380, 160, "ill6b")
    # Triangle
    ta = (580, 320); tb = (700, 320); tc = (620, 240)
    tri_pts = f"{ta[0]},{ta[1]} {tb[0]},{tb[1]} {tc[0]},{tc[1]}"
    ET.SubElement(g2, 'polygon').set('points', tri_pts)
    g2[-1].set('fill', PRIMARY); g2[-1].set('opacity', '0.08')
    g2[-1].set('stroke', PRIMARY); g2[-1].set('stroke-width', '2.5')

    # Height
    add_labeled_line(g2, tc[0], tc[1], tc[0], ta[1], "h", ACCENT, "3,2")
    # Base label
    t3 = ET.SubElement(g2, 'text')
    t3.set('x', str((ta[0] + tb[0]) // 2)); t3.set('y', str(ta[1] + 16))
    t3.set('font-family', 'Arial,sans-serif'); t3.set('font-size', '14')
    t3.set('fill', ACCENT2); t3.set('text-anchor', 'middle'); t3.set('font-style', 'italic')
    t3.set('font-weight', 'bold')
    t3.text = 'a'

    # Vertex labels
    for label, (lx, ly), off in [('A', ta, (-12, 14)), ('B', tb, (8, 14)), ('C', tc, (-2, -8))]:
        t = ET.SubElement(g2, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '13')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label

    # Right angle mark for height
    ET.SubElement(g2, 'rect').set('x', str(tc[0]))
    g2[-1].set('y', str(ta[1] - 8)); g2[-1].set('width', '8')
    g2[-1].set('height', '8'); g2[-1].set('fill', 'none')
    g2[-1].set('stroke', ACCENT); g2[-1].set('stroke-width', '1')

    # Formula
    t4 = ET.SubElement(g2, 'text')
    t4.set('x', '600'); t4.set('y', '290')
    t4.set('font-family', 'Arial,sans-serif'); t4.set('font-size', '15')
    t4.set('fill', TEXT_DARK); t4.set('text-anchor', 'middle'); t4.set('font-weight', 'bold')
    t4.text = 'S = \u00bd \u00b7 a \u00b7 h'

    # Bottom: Heron's formula
    add_formula_box(root, 20, 380, 760, 90, "Формула Герона", [
        "S = \u221a(p \u00b7 (p\u2212a) \u00b7 (p\u2212b) \u00b7 (p\u2212c))",
        "где p = (a + b + c) / 2 \u2014 полупериметр",
        "Пример: a=3, b=4, c=5;  p = 6;  S = \u221a(6\u00b73\u00b72\u00b71) = \u221a36 = 6",
    ])

    # Right triangle area
    add_content_box(root, 20, 485, 760, 55, "Прямоугольный треугольник", [
        "S = \u00bd \u00b7 a \u00b7 b  (a, b \u2014 катеты)     |     S = \u00bd \u00b7 c \u00b7 h_c  (c \u2014 гипотенуза, h_c \u2014 высота к гипотенузе)     |     Равносторонний: S = a\u00b2\u221a3 / 4",
    ])


def lesson7_pythagorean(root):
    """Теорема Пифагора — Pythagorean theorem."""
    # Main theorem
    add_formula_box(root, 20, 90, 760, 75, "Теорема Пифагора", [
        "В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов:",
        "c\u00b2 = a\u00b2 + b\u00b2        где c \u2014 гипотенуза, a, b \u2014 катеты",
    ])

    # Illustration: Right triangle with squares
    g = add_illustration_area(root, 20, 180, 480, 210, "ill7")
    # Right triangle
    ta = (180, 360); tb = (380, 360); tc = (180, 210)
    tri_pts = f"{ta[0]},{ta[1]} {tb[0]},{tb[1]} {tc[0]},{tc[1]}"
    ET.SubElement(g, 'polygon').set('points', tri_pts)
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.08')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2.5')

    # Right angle mark
    ET.SubElement(g, 'rect').set('x', '180')
    g[-1].set('y', '345'); g[-1].set('width', '15')
    g[-1].set('height', '15'); g[-1].set('fill', 'none')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '1.5')

    # Square on side a (bottom)
    sq_a = "180,360 380,360 380,410 180,410"
    # (simplified - just show as a filled area indicator)

    # Side labels
    t = ET.SubElement(g, 'text')
    t.set('x', '280'); t.set('y', '378')
    t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '15')
    t.set('fill', ACCENT2); t.set('text-anchor', 'middle')
    t.set('font-style', 'italic'); t.set('font-weight', 'bold')
    t.text = 'a'

    t2 = ET.SubElement(g, 'text')
    t2.set('x', '170'); t2.set('y', '290')
    t2.set('font-family', 'Arial,sans-serif'); t2.set('font-size', '15')
    t2.set('fill', ACCENT2); t2.set('font-style', 'italic'); t2.set('font-weight', 'bold')
    t2.text = 'b'

    t3 = ET.SubElement(g, 'text')
    t3.set('x', '295'); t3.set('y', '275')
    t3.set('font-family', 'Arial,sans-serif'); t3.set('font-size', '15')
    t3.set('fill', ACCENT2); t3.set('font-style', 'italic'); t3.set('font-weight', 'bold')
    t3.text = 'c'

    # Vertex labels
    for label, (lx, ly), off in [('C', ta, (-14, 14)), ('B', tb, (8, 14)), ('A', tc, (-14, -5))]:
        t = ET.SubElement(g, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '14')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label

    # Squares on sides (visual)
    # Square on bottom side (a)
    ET.SubElement(g, 'rect').set('x', '180')
    g[-1].set('y', '360'); g[-1].set('width', '200')
    g[-1].set('height', '50'); g[-1].set('fill', '#06B6D4')
    g[-1].set('opacity', '0.08'); g[-1].set('stroke', '#06B6D4')
    g[-1].set('stroke-width', '1'); g[-1].set('stroke-dasharray', '3,2')
    t_sq = ET.SubElement(g, 'text')
    t_sq.set('x', '280'); t_sq.set('y', '390')
    t_sq.set('font-family', 'Arial,sans-serif'); t_sq.set('font-size', '12')
    t_sq.set('fill', PRIMARY); t_sq.set('text-anchor', 'middle')
    t_sq.text = 'a\u00b2'

    # Square on left side (b)
    ET.SubElement(g, 'rect').set('x', '130')
    g[-1].set('y', '210'); g[-1].set('width', '50')
    g[-1].set('height', '150'); g[-1].set('fill', '#06B6D4')
    g[-1].set('opacity', '0.08'); g[-1].set('stroke', '#06B6D4')
    g[-1].set('stroke-width', '1'); g[-1].set('stroke-dasharray', '3,2')
    t_sq2 = ET.SubElement(g, 'text')
    t_sq2.set('x', '155'); t_sq2.set('y', '290')
    t_sq2.set('font-family', 'Arial,sans-serif'); t_sq2.set('font-size', '12')
    t_sq2.set('fill', PRIMARY); t_sq2.set('text-anchor', 'middle')
    t_sq2.set('transform', 'rotate(-90, 155, 290)')
    t_sq2.text = 'b\u00b2'

    # Big formula
    t_form = ET.SubElement(g, 'text')
    t_form.set('x', '280'); t_form.set('y', '250')
    t_form.set('font-family', 'Arial,sans-serif'); t_form.set('font-size', '18')
    t_form.set('fill', ACCENT2); t_form.set('text-anchor', 'middle')
    t_form.set('font-weight', 'bold')
    t_form.text = 'c\u00b2 = a\u00b2 + b\u00b2'

    # Right side: Pythagorean triples and converse
    add_content_box(root, 510, 180, 270, 110, "Пифагоровы тройки", [
        "\u2022 3, 4, 5   (9 + 16 = 25)",
        "\u2022 5, 12, 13  (25 + 144 = 169)",
        "\u2022 8, 15, 17  (64 + 225 = 289)",
        "\u2022 7, 24, 25  (49 + 576 = 625)",
        "\u2022 6, 8, 10   (кратная 3,4,5)",
    ])

    add_content_box(root, 510, 305, 270, 85, "Обратная теорема", [
        "Если c\u00b2 = a\u00b2 + b\u00b2, то",
        "треугольник прямоугольный.",
        "",
        "Применяется для проверки",
        "прямоугольности треугольника.",
    ])

    # Bottom examples
    add_formula_box(root, 20, 405, 760, 80, "Примеры решения задач", [
        "1) a=3, b=4: c = \u221a(9+16) = \u221a25 = 5",
        "2) c=13, b=5: a = \u221a(169\u221225) = \u221a144 = 12",
        "3) Диагональ квадрата: d = a\u221a2",
    ])

    add_content_box(root, 20, 500, 760, 55, "Следствия", [
        "\u2022 Диагональ квадрата: d = a\u221a2     \u2022 Высота равностороннего \u0394: h = a\u221a3/2     \u2022 Катет против угла 30\u00b0 = половине гипотенузы",
    ])


def lesson8_similar_triangles(root):
    """Подобные треугольники — similar triangles."""
    add_content_box(root, 20, 90, 370, 105, "Определение", [
        "Подобные треугольники \u2014 треугольники,",
        "у которых углы соответственно равны,",
        "а сходственные стороны пропорциональны.",
        "",
        "\u0394ABC ~ \u0394A\u2081B\u2081C\u2081",
        "k = A\u2081B\u2081/AB = B\u2081C\u2081/BC = A\u2081C\u2081/AC",
    ])

    add_formula_box(root, 410, 90, 370, 105, "Свойства подобных треугольников", [
        "\u2220A = \u2220A\u2081, \u2220B = \u2220B\u2081, \u2220C = \u2220C\u2081",
        "Отношение сторон: k (коэфф. подобия)",
        "Отношение площадей: S\u2081/S\u2082 = k\u00b2",
        "Отношение периметров: P\u2081/P\u2082 = k",
        "Отношение высот: h\u2081/h\u2082 = k",
    ])

    # Similar triangles illustration
    g = add_illustration_area(root, 20, 210, 480, 180, "ill8")
    # Smaller triangle
    s1 = (80, 360); s2 = (220, 360); s3 = (120, 270)
    tri1 = f"{s1[0]},{s1[1]} {s2[0]},{s2[1]} {s3[0]},{s3[1]}"
    ET.SubElement(g, 'polygon').set('points', tri1)
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.1')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2.5')

    # Larger triangle (scaled)
    sc = 1.7
    cx_s, cy_s = (s1[0] + s2[0] + s3[0]) / 3, (s1[1] + s2[1] + s3[1]) / 3
    l1 = (int(cx_s + (s1[0] - cx_s) * sc), int(cy_s + (s1[1] - cy_s) * sc))
    l2 = (int(cx_s + (s2[0] - cx_s) * sc), int(cy_s + (s2[1] - cy_s) * sc))
    l3 = (int(cx_s + (s3[0] - cx_s) * sc), int(cy_s + (s3[1] - cy_s) * sc))
    tri2 = f"{l1[0]},{l1[1]} {l2[0]},{l2[1]} {l3[0]},{l3[1]}"
    ET.SubElement(g, 'polygon').set('points', tri2)
    g[-1].set('fill', ACCENT); g[-1].set('opacity', '0.06')
    g[-1].set('stroke', ACCENT); g[-1].set('stroke-width', '2')

    # Labels for small
    for label, (lx, ly), off in [('A', s1, (-12, 14)), ('B', s2, (8, 14)), ('C', s3, (-10, -5))]:
        t = ET.SubElement(g, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '13')
        t.set('font-weight', 'bold'); t.set('fill', PRIMARY)
        t.text = label

    # Labels for large
    for label, (lx, ly), off in [('A\u2081', l1, (-18, 14)), ('B\u2081', l2, (8, 14)), ('C\u2081', l3, (-5, -8))]:
        t = ET.SubElement(g, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '13')
        t.set('font-weight', 'bold'); t.set('fill', ACCENT)
        t.text = label

    # ~ symbol
    t_sim = ET.SubElement(g, 'text')
    t_sim.set('x', '360'); t_sim.set('y', '310')
    t_sim.set('font-family', 'Arial,sans-serif'); t_sim.set('font-size', '18')
    t_sim.set('fill', TEXT_DARK); t_sim.set('font-weight', 'bold')
    t_sim.text = '~'

    # k label
    t_k = ET.SubElement(g, 'text')
    t_k.set('x', '360'); t_k.set('y', '330')
    t_k.set('font-family', 'Arial,sans-serif'); t_k.set('font-size', '14')
    t_k.set('fill', ACCENT2); t_k.set('font-style', 'italic'); t_k.set('font-weight', 'bold')
    t_k.text = 'k'

    # Right: 3 similarity criteria
    add_content_box(root, 510, 210, 270, 180, "Признаки подобия", [
        "1. По двум углам:",
        "   \u2220A = \u2220A\u2081 и \u2220B = \u2220B\u2081",
        "",
        "2. По двум пропорциональным",
        "   сторонам и углу между ними:",
        "   A\u2081B\u2081/AB = A\u2081C\u2081/AC, \u2220A = \u2220A\u2081",
        "",
        "3. По трём пропорциональным",
        "   сторонам:",
        "   A\u2081B\u2081/AB = B\u2081C\u2081/BC = A\u2081C\u2081/AC",
    ])

    # Bottom
    add_formula_box(root, 20, 405, 760, 80, "Ключевые формулы", [
        "S\u2081/S\u2082 = k\u00b2     |     P\u2081/P\u2082 = k     |     k = A\u2081B\u2081/AB     |     Отношение медиан, биссектрис, высот = k",
    ])

    add_content_box(root, 20, 500, 760, 55, "Применение", [
        "\u2022 Нахождение неизвестных сторон     \u2022 Доказательство пропорциональности     \u2022 Задачи на построение     \u2022 Измерение расстояний (недоступных)",
    ])


def lesson9_midline_triangle(root):
    """Средняя линия треугольника."""
    add_content_box(root, 20, 90, 370, 110, "Определение", [
        "Средняя линия треугольника \u2014",
        "отрезок, соединяющий середины",
        "двух его сторон.",
        "",
        "DE \u2014 средняя линия \u0394ABC,",
        "где D \u2014 середина AB,",
        "E \u2014 середина BC",
    ])

    add_formula_box(root, 410, 90, 370, 110, "Свойства средней линии", [
        "1. DE \u2225 AC (параллельна 3-й стороне)",
        "",
        "2. DE = AC / 2 (равна половине)",
        "",
        "3. \u0394DBE ~ \u0394ABC, k = \u00bd",
    ])

    # Illustration: Triangle with midline
    g = add_illustration_area(root, 20, 215, 480, 190, "ill9")
    # Triangle
    ta = (240, 370); tb = (100, 250); tc = (400, 250)
    tri_pts = f"{ta[0]},{ta[1]} {tb[0]},{tb[1]} {tc[0]},{tc[1]}"
    ET.SubElement(g, 'polygon').set('points', tri_pts)
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.06')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2.5')

    # Midpoints
    d = ((ta[0] + tb[0]) // 2, (ta[1] + tb[1]) // 2)
    e = ((ta[0] + tc[0]) // 2, (ta[1] + tc[1]) // 2)
    f_mid = ((tb[0] + tc[0]) // 2, (tb[1] + tc[1]) // 2)

    # Midline DE (highlighted)
    add_labeled_line(g, d[0], d[1], e[0], e[1], "DE", ACCENT2, None)

    # Another midline (lighter)
    add_labeled_line(g, d[0], d[1], f_mid[0], f_mid[1], "", PRIMARY, "4,3")
    add_labeled_line(g, e[0], e[1], f_mid[0], f_mid[1], "", PRIMARY, "4,3")

    # Midpoint dots
    for pt, label, off in [(d, 'D', (-14, 4)), (e, 'E', (8, 4)), (f_mid, 'F', (0, -8))]:
        ET.SubElement(g, 'circle').set('cx', str(pt[0]))
        g[-1].set('cy', str(pt[1])); g[-1].set('r', '4')
        g[-1].set('fill', ACCENT2)
        t = ET.SubElement(g, 'text')
        t.set('x', str(pt[0] + off[0])); t.set('y', str(pt[1] + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '13')
        t.set('font-weight', 'bold'); t.set('fill', ACCENT2)
        t.text = label

    # Vertex labels
    for label, (lx, ly), off in [('A', ta, (6, 14)), ('B', tb, (-14, -5)), ('C', tc, (8, -5))]:
        t = ET.SubElement(g, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '14')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label

    # AC label
    t_ac = ET.SubElement(g, 'text')
    t_ac.set('x', str((tb[0] + tc[0]) // 2)); t_ac.set('y', str(tb[1] - 8))
    t_ac.set('font-family', 'Arial,sans-serif'); t_ac.set('font-size', '13')
    t_ac.set('fill', PRIMARY); t_ac.set('text-anchor', 'middle'); t_ac.set('font-style', 'italic')
    t_ac.text = 'AC'

    # Formula on diagram
    t_form = ET.SubElement(g, 'text')
    t_form.set('x', '250'); t_form.set('y', '310')
    t_form.set('font-family', 'Arial,sans-serif'); t_form.set('font-size', '16')
    t_form.set('fill', ACCENT2); t_form.set('font-weight', 'bold')
    t_form.text = 'DE = AC/2, DE \u2225 AC'

    # Right: Midline of trapezoid
    add_content_box(root, 510, 215, 270, 130, "Средняя линия трапеции", [
        "Соединяет середины боковых",
        "сторон трапеции.",
        "",
        "m = (a + b) / 2",
        "",
        "m \u2225 основаниям a и b",
        "m = (AD + BC) / 2",
    ])

    # Additional properties
    add_content_box(root, 510, 360, 270, 50, "Дополнительные свойства", [
        "3 средние линии делят \u0394 на 4",
        "равных треугольника",
    ])

    # Bottom
    add_formula_box(root, 20, 420, 760, 80, "Ключевые формулы", [
        "DE \u2225 AC,  DE = AC / 2     |     \u0394DBE ~ \u0394ABC,  k = 1/2     |     S(DBE) = S(ABC) / 4     |     Средние линии \u0394 \u2192 4 равных \u0394",
    ])

    add_content_box(root, 20, 515, 760, 40, "Пример", [
        "AC = 12 см, D и E \u2014 середины AB и BC. DE = AC/2 = 6 см, DE \u2225 AC",
    ])


def lesson10_tangent(root):
    """Касательная к окружности."""
    add_content_box(root, 20, 90, 370, 110, "Определение", [
        "Касательная к окружности \u2014 прямая,",
        "имеющая с окружностью ровно",
        "одну общую точку (точку касания).",
        "",
        "Прямая a \u2014 касательная",
        "Точка K \u2014 точка касания",
    ])

    add_formula_box(root, 410, 90, 370, 110, "Свойства касательной", [
        "1. Касательная \u22a5 радиусу в точке",
        "   касания: a \u22a5 OK",
        "",
        "2. Отрезки касательных, проведённых",
        "   из одной точки, равны:",
        "   AM = AN",
    ])

    # Illustration: Circle with tangent
    g = add_illustration_area(root, 20, 215, 480, 190, "ill10")
    # Circle
    cx, cy, r = 260, 320, 70
    ET.SubElement(g, 'circle').set('cx', str(cx))
    g[-1].set('cy', str(cy)); g[-1].set('r', str(r))
    g[-1].set('fill', PRIMARY); g[-1].set('opacity', '0.06')
    g[-1].set('stroke', PRIMARY); g[-1].set('stroke-width', '2.5')

    # Center
    ET.SubElement(g, 'circle').set('cx', str(cx))
    g[-1].set('cy', str(cy)); g[-1].set('r', '3')
    g[-1].set('fill', ACCENT)

    # O label
    t_o = ET.SubElement(g, 'text')
    t_o.set('x', str(cx - 6)); t_o.set('y', str(cy - 8))
    t_o.set('font-family', 'Arial,sans-serif'); t_o.set('font-size', '13')
    t_o.set('font-weight', 'bold'); t_o.set('fill', ACCENT)
    t_o.text = 'O'

    # Radius to tangent point
    kx, ky = 330, 280  # tangent point on circle
    # Adjust to be on circle
    import math
    angle_k = math.radians(-30)
    kx = int(cx + r * math.cos(angle_k))
    ky = int(cy + r * math.sin(angle_k))

    add_labeled_line(g, cx, cy, kx, ky, "r", ACCENT, None)

    # Tangent line at K
    # Perpendicular to OK
    dx, dy = kx - cx, ky - cy
    dist = math.sqrt(dx**2 + dy**2)
    nx, ny = -dy / dist, dx / dist  # perpendicular direction
    t_len = 80
    ET.SubElement(g, 'line').set('x1', str(int(kx - t_len * nx)))
    g[-1].set('y1', str(int(ky - t_len * ny)))
    g[-1].set('x2', str(int(kx + t_len * nx)))
    g[-1].set('y2', str(int(ky + t_len * ny)))
    g[-1].set('stroke', ACCENT2); g[-1].set('stroke-width', '2.5')

    # Tangent point
    ET.SubElement(g, 'circle').set('cx', str(kx))
    g[-1].set('cy', str(ky)); g[-1].set('r', '4')
    g[-1].set('fill', ACCENT2)

    # K label
    t_k = ET.SubElement(g, 'text')
    t_k.set('x', str(kx + 10)); t_k.set('y', str(ky - 6))
    t_k.set('font-family', 'Arial,sans-serif'); t_k.set('font-size', '13')
    t_k.set('font-weight', 'bold'); t_k.set('fill', ACCENT2)
    t_k.text = 'K'

    # Right angle mark at K
    mark_size = 10
    mx1 = int(kx + mark_size * dx / dist)
    my1 = int(ky + mark_size * dy / dist)
    mx2 = int(mx1 + mark_size * nx)
    my2 = int(my1 + mark_size * ny)
    mx3 = int(kx + mark_size * nx)
    my3 = int(ky + mark_size * ny)
    ET.SubElement(g, 'polygon').set('points',
        f"{kx},{ky} {mx1},{my1} {mx2},{my2} {mx3},{my3}")
    g[-1].set('fill', 'none'); g[-1].set('stroke', ACCENT2)
    g[-1].set('stroke-width', '1')

    # Tangent line label
    t_a = ET.SubElement(g, 'text')
    t_a.set('x', str(int(kx + t_len * nx))); t_a.set('y', str(int(ky + t_len * ny) - 6))
    t_a.set('font-family', 'Arial,sans-serif'); t_a.set('font-size', '12')
    t_a.set('fill', ACCENT2); t_a.set('font-style', 'italic')
    t_a.text = 'a'

    # Second illustration: Two tangents from one point
    g2 = add_illustration_area(root, 510, 215, 270, 190, "ill10b")
    cx2, cy2, r2 = 640, 330, 50

    ET.SubElement(g2, 'circle').set('cx', str(cx2))
    g2[-1].set('cy', str(cy2)); g2[-1].set('r', str(r2))
    g2[-1].set('fill', PRIMARY); g2[-1].set('opacity', '0.06')
    g2[-1].set('stroke', PRIMARY); g2[-1].set('stroke-width', '2')

    # External point A
    ax, ay = 540, 250
    ET.SubElement(g2, 'circle').set('cx', str(ax))
    g2[-1].set('cy', str(ay)); g2[-1].set('r', '3')
    g2[-1].set('fill', ACCENT2)

    # Tangent points
    # Calculate tangent points from A to circle
    dx_a = cx2 - ax; dy_a = cy2 - ay
    dist_a = math.sqrt(dx_a**2 + dy_a**2)
    # tangent length
    tang_len = math.sqrt(dist_a**2 - r2**2)
    # angle
    base_angle = math.atan2(dy_a, dx_a)
    offset_angle = math.asin(r2 / dist_a)

    m1x = int(cx2 + r2 * math.cos(base_angle + math.pi + offset_angle))
    m1y = int(cy2 + r2 * math.sin(base_angle + math.pi + offset_angle))
    m2x = int(cx2 + r2 * math.cos(base_angle + math.pi - offset_angle))
    m2y = int(cy2 + r2 * math.sin(base_angle + math.pi - offset_angle))

    # Tangent lines from A
    ET.SubElement(g2, 'line').set('x1', str(ax)); g2[-1].set('y1', str(ay))
    g2[-1].set('x2', str(m1x)); g2[-1].set('y2', str(m1y))
    g2[-1].set('stroke', ACCENT2); g2[-1].set('stroke-width', '2')

    ET.SubElement(g2, 'line').set('x1', str(ax)); g2[-1].set('y1', str(ay))
    g2[-1].set('x2', str(m2x)); g2[-1].set('y2', str(m2y))
    g2[-1].set('stroke', ACCENT2); g2[-1].set('stroke-width', '2')

    # Labels
    t_a2 = ET.SubElement(g2, 'text')
    t_a2.set('x', str(ax - 10)); t_a2.set('y', str(ay - 8))
    t_a2.set('font-family', 'Arial,sans-serif'); t_a2.set('font-size', '12')
    t_a2.set('font-weight', 'bold'); t_a2.set('fill', ACCENT2)
    t_a2.text = 'A'

    t_m = ET.SubElement(g2, 'text')
    t_m.set('x', str(m1x - 10)); t_m.set('y', str(m1y + 4))
    t_m.set('font-family', 'Arial,sans-serif'); t_m.set('font-size', '11')
    t_m.set('font-weight', 'bold'); t_m.set('fill', PRIMARY)
    t_m.text = 'M'

    t_n = ET.SubElement(g2, 'text')
    t_n.set('x', str(m2x + 6)); t_n.set('y', str(m2y + 4))
    t_n.set('font-family', 'Arial,sans-serif'); t_n.set('font-size', '11')
    t_n.set('font-weight', 'bold'); t_n.set('fill', PRIMARY)
    t_n.text = 'N'

    # AM = AN label
    t_eq = ET.SubElement(g2, 'text')
    t_eq.set('x', '640'); t_eq.set('y', '260')
    t_eq.set('font-family', 'Arial,sans-serif'); t_eq.set('font-size', '12')
    t_eq.set('fill', ACCENT2); t_eq.set('font-weight', 'bold')
    t_eq.set('text-anchor', 'middle')
    t_eq.text = 'AM = AN'

    # Bottom: Properties summary
    add_formula_box(root, 20, 420, 760, 80, "Ключевые свойства", [
        "1. Касательная \u22a5 радиусу: OK \u22a5 a     2. AM = AN (отрезки из одной точки)     3. OM \u22a5 AM, ON \u22a5 AN",
    ])

    add_content_box(root, 20, 515, 760, 40, "Признак касательной", [
        "Если прямая проходит через точку окружности и перпендикулярна радиусу, проведённому в эту точку, то она \u2014 касательная.",
    ])


def lesson11_central_inscribed_angles(root):
    """Центральные и вписанные углы."""
    add_content_box(root, 20, 90, 370, 110, "Определения", [
        "Центральный угол \u2014 угол с вершиной",
        "в центре окружности.",
        "\u2220AOB \u2014 центральный",
        "",
        "Вписанный угол \u2014 угол, вершина",
        "которого лежит на окружности,",
        "а стороны пересекают окружность.",
        "\u2220ACB \u2014 вписанный",
    ])

    add_formula_box(root, 410, 90, 370, 110, "Основная теорема", [
        "Вписанный угол равен половине",
        "дуги, на которую он опирается:",
        "",
        "\u2220ACB = \u00bd \u00b7 \u2329AB",
        "",
        "Центральный: \u2220AOB = \u2329AB",
        "\u2220ACB = \u00bd \u00b7 \u2220AOB",
    ])

    # Illustration: Central angle
    g1 = add_illustration_area(root, 20, 215, 230, 175, "ill11a")
    cx, cy, r = 135, 320, 65
    ET.SubElement(g1, 'circle').set('cx', str(cx))
    g1[-1].set('cy', str(cy)); g1[-1].set('r', str(r))
    g1[-1].set('fill', PRIMARY); g1[-1].set('opacity', '0.04')
    g1[-1].set('stroke', PRIMARY); g1[-1].set('stroke-width', '2')

    # Points A, B on circle
    import math
    ax = int(cx + r * math.cos(math.radians(-60)))
    ay = int(cy + r * math.sin(math.radians(-60)))
    bx = int(cx + r * math.cos(math.radians(60)))
    by = int(cy + r * math.sin(math.radians(60)))

    # Lines OA, OB
    add_labeled_line(g1, cx, cy, ax, ay, "", PRIMARY, None)
    add_labeled_line(g1, cx, cy, bx, by, "", PRIMARY, None)

    # Arc AB (highlighted)
    ET.SubElement(g1, 'path').set('d',
        f'M {ax},{ay} A {r},{r} 0 0 1 {bx},{by}')
    g1[-1].set('fill', 'none'); g1[-1].set('stroke', ACCENT)
    g1[-1].set('stroke-width', '3'); g1[-1].set('opacity', '0.5')

    # Angle arc
    ET.SubElement(g1, 'path').set('d',
        f'M {cx+20},{cy} A 20,20 0 0 0 {int(cx+20*math.cos(math.radians(60)))},{int(cy-20*math.sin(math.radians(60)))}')
    g1[-1].set('fill', 'none'); g1[-1].set('stroke', ACCENT2)
    g1[-1].set('stroke-width', '2')

    # Labels
    ET.SubElement(g1, 'text').set('x', str(cx)); g1[-1].set('y', str(cy - 10))
    g1[-1].set('font-family', 'Arial,sans-serif'); g1[-1].set('font-size', '12')
    g1[-1].set('fill', ACCENT); g1[-1].set('text-anchor', 'middle')
    g1[-1].set('font-weight', 'bold')
    g1[-1].text = 'O'

    ET.SubElement(g1, 'text').set('x', str(ax - 8)); g1[-1].set('y', str(ay - 5))
    g1[-1].set('font-family', 'Arial,sans-serif'); g1[-1].set('font-size', '11')
    g1[-1].set('font-weight', 'bold'); g1[-1].set('fill', TEXT_DARK)
    g1[-1].text = 'A'

    ET.SubElement(g1, 'text').set('x', str(bx + 6)); g1[-1].set('y', str(by - 5))
    g1[-1].set('font-family', 'Arial,sans-serif'); g1[-1].set('font-size', '11')
    g1[-1].set('font-weight', 'bold'); g1[-1].set('fill', TEXT_DARK)
    g1[-1].text = 'B'

    ET.SubElement(g1, 'text').set('x', '135'); g1[-1].set('y', '380')
    g1[-1].set('font-family', 'Arial,sans-serif'); g1[-1].set('font-size', '10')
    g1[-1].set('fill', PRIMARY); g1[-1].set('text-anchor', 'middle')
    g1[-1].set('opacity', '0.7')
    g1[-1].text = 'Центральный угол'

    # Illustration: Inscribed angle
    g2 = add_illustration_area(root, 260, 215, 230, 175, "ill11b")
    cx2, cy2, r2 = 375, 320, 65
    ET.SubElement(g2, 'circle').set('cx', str(cx2))
    g2[-1].set('cy', str(cy2)); g2[-1].set('r', str(r2))
    g2[-1].set('fill', PRIMARY); g2[-1].set('opacity', '0.04')
    g2[-1].set('stroke', PRIMARY); g2[-1].set('stroke-width', '2')

    # Points A, B, C on circle
    a2x = int(cx2 + r2 * math.cos(math.radians(-30)))
    a2y = int(cy2 + r2 * math.sin(math.radians(-30)))
    b2x = int(cx2 + r2 * math.cos(math.radians(30)))
    b2y = int(cy2 + r2 * math.sin(math.radians(30)))
    c2x = int(cx2 + r2 * math.cos(math.radians(200)))
    c2y = int(cy2 + r2 * math.sin(math.radians(200)))

    # Lines CA, CB
    add_labeled_line(g2, c2x, c2y, a2x, a2y, "", ACCENT2, None)
    add_labeled_line(g2, c2x, c2y, b2x, b2y, "", ACCENT2, None)

    # Arc AB (highlighted)
    ET.SubElement(g2, 'path').set('d',
        f'M {a2x},{a2y} A {r2},{r2} 0 0 1 {b2x},{b2y}')
    g2[-1].set('fill', 'none'); g2[-1].set('stroke', ACCENT)
    g2[-1].set('stroke-width', '3'); g2[-1].set('opacity', '0.5')

    # Labels
    for label, lx, ly, off in [('A', a2x, a2y, (-4, -8)), ('B', b2x, b2y, (6, -5)), ('C', c2x, c2y, (-10, 6))]:
        t = ET.SubElement(g2, 'text')
        t.set('x', str(lx + off[0])); t.set('y', str(ly + off[1]))
        t.set('font-family', 'Arial,sans-serif'); t.set('font-size', '11')
        t.set('font-weight', 'bold'); t.set('fill', TEXT_DARK)
        t.text = label

    ET.SubElement(g2, 'text').set('x', '375'); g2[-1].set('y', '380')
    g2[-1].set('font-family', 'Arial,sans-serif'); g2[-1].set('font-size', '10')
    g2[-1].set('fill', PRIMARY); g2[-1].set('text-anchor', 'middle')
    g2[-1].set('opacity', '0.7')
    g2[-1].text = 'Вписанный угол'

    # Right: Additional properties
    add_content_box(root, 500, 215, 280, 175, "Следствия и свойства", [
        "\u2022 Вписанные углы, опирающиеся",
        "  на одну дугу, равны",
        "",
        "\u2022 Вписанный угол, опирающийся",
        "  на диаметр = 90\u00b0",
        "",
        "\u2022 Угол между хордами:",
        "  \u2220 = \u00bd(\u2329AB + \u2329CD)",
        "",
        "\u2022 Угол между секущими:",
        "  \u2220 = \u00bd(\u2329AB \u2212 \u2329CD)",
    ])

    # Bottom: Summary
    add_formula_box(root, 20, 405, 760, 85, "Ключевые формулы", [
        "\u2220AOB (центр.) = \u2329AB                                    \u2220ACB (впис.) = \u00bd \u00b7 \u2329AB = \u00bd \u00b7 \u2220AOB",
        "Вписанный угол = \u00bd центрального (на той же дуге)     |     Угол через диаметр = 90\u00b0     |     Впис. углы на одной дуге равны",
    ])

    add_content_box(root, 20, 505, 760, 50, "Пример", [
        "\u0394AB = 120\u00b0. Центральный угол \u2220AOB = 120\u00b0. Вписанный угол \u2220ACB = 60\u00b0. Если \u0394AB = 180\u00b0 (диаметр), то \u2220ACB = 90\u00b0.",
    ])


def lesson12_inscribed_circumscribed_circles(root):
    """Вписанная и описанная окружности."""
    add_content_box(root, 20, 90, 370, 110, "Вписанная окружность", [
        "Вписанная окружность \u2014 окружность,",
        "касающаяся всех сторон многоугол.",
        "",
        "Центр \u2014 точка пересечения",
        "биссектрис внутренних углов.",
        "r = S / p  (в треугольнике)",
    ])

    add_content_box(root, 410, 90, 370, 110, "Описанная окружность", [
        "Описанная окружность \u2014 окружность,",
        "проходящая через все вершины.",
        "",
        "Центр \u2014 точка пересечения",
        "серединных перпендикуляров.",
        "R = abc / (4S)  (в треугольнике)",
    ])

    # Illustration: Triangle with inscribed circle
    g1 = add_illustration_area(root, 20, 215, 230, 180, "ill12a")
    # Triangle
    ta = (135, 360); tb = (50, 260); tc = (220, 260)
    tri_pts = f"{ta[0]},{ta[1]} {tb[0]},{tb[1]} {tc[0]},{tc[1]}"
    ET.SubElement(g1, 'polygon').set('points', tri_pts)
    g1[-1].set('fill', PRIMARY); g1[-1].set('opacity', '0.04')
    g1[-1].set('stroke', PRIMARY); g1[-1].set('stroke-width', '2')

    # Inscribed circle (approximate)
    import math
    # Incenter
    icx = int((ta[0] + tb[0] + tc[0]) / 3)
    icy = int((ta[1] + tb[1] + tc[1]) / 3) + 10
    ir = 28
    ET.SubElement(g1, 'circle').set('cx', str(icx))
    g1[-1].set('cy', str(icy)); g1[-1].set('r', str(ir))
    g1[-1].set('fill', PRIMARY); g1[-1].set('opacity', '0.08')
    g1[-1].set('stroke', PRIMARY); g1[-1].set('stroke-width', '1.5')

    # Center dot
    ET.SubElement(g1, 'circle').set('cx', str(icx))
    g1[-1].set('cy', str(icy)); g1[-1].set('r', '2.5')
    g1[-1].set('fill', ACCENT)

    # I label
    ET.SubElement(g1, 'text').set('x', str(icx + 8)); g1[-1].set('y', str(icy - 5))
    g1[-1].set('font-family', 'Arial,sans-serif'); g1[-1].set('font-size', '12')
    g1[-1].set('font-weight', 'bold'); g1[-1].set('fill', ACCENT)
    g1[-1].text = 'I'

    # r line
    ET.SubElement(g1, 'line').set('x1', str(icx)); g1[-1].set('y1', str(icy))
    g1[-1].set('x2', str(icx)); g1[-1].set('y2', str(icy + ir))
    g1[-1].set('stroke', ACCENT); g1[-1].set('stroke-width', '1.5')
    g1[-1].set('stroke-dasharray', '3,2')

    # r label
    ET.SubElement(g1, 'text').set('x', str(icx + 10)); g1[-1].set('y', str(icy + ir // 2 + 2))
    g1[-1].set('font-family', 'Arial,sans-serif'); g1[-1].set('font-size', '11')
    g1[-1].set('fill', ACCENT); g1[-1].set('font-style', 'italic')
    g1[-1].text = 'r'

    # Caption
    ET.SubElement(g1, 'text').set('x', '135'); g1[-1].set('y', '387')
    g1[-1].set('font-family', 'Arial,sans-serif'); g1[-1].set('font-size', '10')
    g1[-1].set('fill', PRIMARY); g1[-1].set('text-anchor', 'middle')
    g1[-1].set('opacity', '0.7')
    g1[-1].text = 'Вписанная окружность'

    # Illustration: Triangle with circumscribed circle
    g2 = add_illustration_area(root, 260, 215, 230, 180, "ill12b")
    cx, cy, R = 375, 310, 70
    ET.SubElement(g2, 'circle').set('cx', str(cx))
    g2[-1].set('cy', str(cy)); g2[-1].set('r', str(R))
    g2[-1].set('fill', PRIMARY); g2[-1].set('opacity', '0.04')
    g2[-1].set('stroke', PRIMARY); g2[-1].set('stroke-width', '2')

    # Triangle vertices on circle
    a2x = int(cx + R * math.cos(math.radians(-90)))
    a2y = int(cy + R * math.sin(math.radians(-90)))
    b2x = int(cx + R * math.cos(math.radians(150)))
    b2y = int(cy + R * math.sin(math.radians(150)))
    c2x = int(cx + R * math.cos(math.radians(30)))
    c2y = int(cy + R * math.sin(math.radians(30)))

    tri2_pts = f"{a2x},{a2y} {b2x},{b2y} {c2x},{c2y}"
    ET.SubElement(g2, 'polygon').set('points', tri2_pts)
    g2[-1].set('fill', PRIMARY); g2[-1].set('opacity', '0.06')
    g2[-1].set('stroke', PRIMARY); g2[-1].set('stroke-width', '2')

    # Center dot
    ET.SubElement(g2, 'circle').set('cx', str(cx))
    g2[-1].set('cy', str(cy)); g2[-1].set('r', '2.5')
    g2[-1].set('fill', ACCENT2)

    # O label
    ET.SubElement(g2, 'text').set('x', str(cx + 8)); g2[-1].set('y', str(cy - 5))
    g2[-1].set('font-family', 'Arial,sans-serif'); g2[-1].set('font-size', '12')
    g2[-1].set('font-weight', 'bold'); g2[-1].set('fill', ACCENT2)
    g2[-1].text = 'O'

    # R line
    ET.SubElement(g2, 'line').set('x1', str(cx)); g2[-1].set('y1', str(cy))
    g2[-1].set('x2', str(c2x)); g2[-1].set('y2', str(c2y))
    g2[-1].set('stroke', ACCENT2); g2[-1].set('stroke-width', '1.5')
    g2[-1].set('stroke-dasharray', '3,2')

    # R label
    mx, my = (cx + c2x) // 2, (cy + c2y) // 2
    ET.SubElement(g2, 'text').set('x', str(mx + 10)); g2[-1].set('y', str(my - 5))
    g2[-1].set('font-family', 'Arial,sans-serif'); g2[-1].set('font-size', '11')
    g2[-1].set('fill', ACCENT2); g2[-1].set('font-style', 'italic')
    g2[-1].text = 'R'

    # Caption
    ET.SubElement(g2, 'text').set('x', '375'); g2[-1].set('y', '387')
    g2[-1].set('font-family', 'Arial,sans-serif'); g2[-1].set('font-size', '10')
    g2[-1].set('fill', PRIMARY); g2[-1].set('text-anchor', 'middle')
    g2[-1].set('opacity', '0.7')
    g2[-1].text = 'Описанная окружность'

    # Right: Center locations and radii
    add_content_box(root, 500, 215, 280, 180, "Расположение центров", [
        "\u0394 остроугольный: O внутри \u0394",
        "\u0394 прямоугольный: O на середине",
        "  гипотенузы, R = c/2",
        "\u0394 тупоугольный: O вне \u0394",
        "",
        "Впис. окружность \u0394 всегда внутри",
        "",
        "Для прямоугольного \u0394:",
        "  r = (a + b \u2212 c) / 2",
        "  R = c / 2",
    ])

    # Bottom: Key formulas
    add_formula_box(root, 20, 410, 760, 90, "Ключевые формулы", [
        "r = S / p  (впис. в \u0394)          |          R = abc / (4S)  (опис. около \u0394)          |          R \u2265 2r  (неравенство Эйлера)",
        "Для прав. \u0394: R = a/\u221a3,  r = a/(2\u221a3)     |     Для квадрата: R = a\u221a2/2,  r = a/2     |     Для прав. 6-уг: R = a,  r = a\u221a3/2",
    ])

    add_content_box(root, 20, 515, 760, 40, "Теорема: около любого треугольника можно описать и в любой треугольник вписать окружность", [
        "Для четырёхугольника: описанная \u2194 сумма противоп. сторон равна (a+c=b+d) | вписанная \u2194 сумма противоп. углов = 180\u00b0",
    ])


# ============================================================
# MAIN
# ============================================================

LESSONS = [
    (1, "Многоугольники", lesson1_polygons),
    (2, "Параллелограмм", lesson2_parallelogram),
    (3, "Прямоугольник, ромб, квадрат", lesson3_rect_rhombus_square),
    (4, "Трапеция", lesson4_trapezoid),
    (5, "Площадь прямоугольника и квадрата", lesson5_area_rect_square),
    (6, "Площадь параллелограмма и треугольника", lesson6_area_parallelogram_triangle),
    (7, "Теорема Пифагора", lesson7_pythagorean),
    (8, "Подобные треугольники", lesson8_similar_triangles),
    (9, "Средняя линия треугольника", lesson9_midline_triangle),
    (10, "Касательная к окружности", lesson10_tangent),
    (11, "Центральные и вписанные углы", lesson11_central_inscribed_angles),
    (12, "Вписанная и описанная окружности", lesson12_inscribed_circumscribed_circles),
]


def main():
    generated = 0
    errors = []

    for num, title, content_fn in LESSONS:
        try:
            root = build_svg(num, title, content_fn)
            filepath = os.path.join(OUTPUT_DIR, f"lesson-{num}.svg")
            write_svg(root, filepath)

            # Validate as XML
            try:
                tree = ET.parse(filepath)
                tree.getroot()
                print(f"\u2713 lesson-{num}.svg \u2014 {title} (valid XML)")
                generated += 1
            except ET.ParseError as e:
                errors.append(f"lesson-{num}.svg: XML validation failed: {e}")
                print(f"\u2717 lesson-{num}.svg \u2014 XML validation error: {e}")

        except Exception as e:
            errors.append(f"lesson-{num}.svg: Generation failed: {e}")
            print(f"\u2717 lesson-{num}.svg \u2014 Generation error: {e}")
            import traceback
            traceback.print_exc()

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
