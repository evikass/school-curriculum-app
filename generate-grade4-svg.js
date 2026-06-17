const fs = require('fs');
const path = require('path');

const GRADE_DIR = 'public/data/grades/4';
const IMG_DIR = 'public/images/lessons/grade4';

// Ensure directories exist
const files = fs.readdirSync(GRADE_DIR).filter(f => f.endsWith('.json') && f !== '_bundle.json');
files.forEach(f => {
  const d = path.join(IMG_DIR, f.replace('.json', ''));
  if (!fs.existsSync(d)) fs.mkdirSync(d, { recursive: true });
});

// ==================== HELPERS ====================
function esc(s) {
  return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function clean(s) {
  return (s||'').replace(/[\u{1F300}-\u{1F9FF}]/gu,'').replace(/[\u{2600}-\u{26FF}]/gu,'').replace(/[\u{2700}-\u{27BF}]/gu,'').replace(/[\u{FE00}-\u{FE0F}]/gu,'').replace(/[\u{200D}]/gu,'').replace(/^#{1,6}\s+/gm,'').replace(/\*\*([^*]+)\*\*/g,'$1').replace(/\*([^*]+)\*/g,'$1').replace(/\n+/g,' ').replace(/\s+/g,' ').trim();
}
function trunc(s, n) { return (s||'').length > n ? (s||'').substring(0,n)+'...' : (s||''); }

// ==================== SUBJECT COLOR THEMES ====================
const themes = {
  math:       { c1:'#1565C0', c2:'#42A5F5', c3:'#BBDEFB', c4:'#0D47A1', c5:'#E3F2FD', name:'Математика' },
  russian:    { c1:'#C62828', c2:'#EF5350', c3:'#FFCDD2', c4:'#B71C1C', c5:'#FFEBEE', name:'Русский язык' },
  english:    { c1:'#2E7D32', c2:'#66BB6A', c3:'#C8E6C9', c4:'#1B5E20', c5:'#E8F5E9', name:'Английский язык' },
  nature:     { c1:'#2E7D32', c2:'#66BB6A', c3:'#C8E6C9', c4:'#1B5E20', c5:'#E8F5E9', name:'Окружающий мир' },
  history:    { c1:'#E65100', c2:'#FFB74D', c3:'#FFE0B2', c4:'#BF360C', c5:'#FFF3E0', name:'История' },
  geography:  { c1:'#00695C', c2:'#4DB6AC', c3:'#B2DFDB', c4:'#004D40', c5:'#E0F2F1', name:'География' },
  music:      { c1:'#6A1B9A', c2:'#AB47BC', c3:'#E1BEE7', c4:'#4A148C', c5:'#F3E5F5', name:'Музыка' },
  art:        { c1:'#AD1457', c2:'#EC407A', c3:'#F8BBD0', c4:'#880E4F', c5:'#FCE4EC', name:'Изобразительное искусство' },
  literature: { c1:'#283593', c2:'#7986CB', c3:'#C5CAE9', c4:'#1A237E', c5:'#E8EAF6', name:'Литература' },
  pe:         { c1:'#F57F17', c2:'#FFEE58', c3:'#FFF9C4', c4:'#F9A825', c5:'#FFFDE7', name:'Физкультура' },
  informatics:{ c1:'#00838F', c2:'#4DD0E1', c3:'#B2EBF2', c4:'#006064', c5:'#E0F7FA', name:'Информатика' },
  tech:       { c1:'#795548', c2:'#A1887F', c3:'#D7CCC8', c4:'#4E342E', c5:'#EFEBE9', name:'Технология' },
  projects:   { c1:'#37474F', c2:'#78909C', c3:'#CFD8DC', c4:'#263238', c5:'#ECEFF1', name:'Проекты' },
  religion:   { c1:'#BF360C', c2:'#FF8A65', c3:'#FFCCBC', c4:'#D84315', c5:'#FBE9E7', name:'Основы религии' },
  world:      { c1:'#1565C0', c2:'#42A5F5', c3:'#BBDEFB', c4:'#0D47A1', c5:'#E3F2FD', name:'Окружающий мир' },
};

// ==================== BASE SVG WRAPPER ====================
function baseSVG(t, title, lessonNum, innerContent) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="${t.c5}"/>
      <stop offset="100%" stop-color="${t.c3}"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="${t.c1}" stroke-width="3"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="${t.c1}" stroke-width="1" opacity="0.3"/>
  <polygon points="10,10 30,10 10,30" fill="${t.c4}" opacity="0.08"/>
  <polygon points="490,10 470,10 490,30" fill="${t.c4}" opacity="0.08"/>
  <polygon points="10,340 30,340 10,320" fill="${t.c2}" opacity="0.08"/>
  <polygon points="490,340 470,340 490,320" fill="${t.c2}" opacity="0.08"/>
  <circle cx="70" cy="15" r="4" fill="${t.c4}" opacity="0.1"/>
  <circle cx="82" cy="15" r="4" fill="${t.c1}" opacity="0.1"/>
  <circle cx="94" cy="15" r="4" fill="${t.c2}" opacity="0.1"/>
  <circle cx="406" cy="15" r="4" fill="${t.c4}" opacity="0.1"/>
  <circle cx="418" cy="15" r="4" fill="${t.c1}" opacity="0.1"/>
  <circle cx="430" cy="15" r="4" fill="${t.c2}" opacity="0.1"/>
  <text x="250" y="50" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="${t.c1}" text-anchor="middle">${esc(trunc(clean(title),32))}</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">${t.name} - Урок ${lessonNum}</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="${t.c1}" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="75" width="60" height="6" fill="${t.c1}" opacity="0.15" rx="1"/>
  <rect x="410" y="75" width="60" height="6" fill="${t.c2}" opacity="0.12" rx="1"/>
  ${innerContent}
  <rect x="15" y="308" width="470" height="30" rx="4" fill="${t.c1}" opacity="0.85"/>
  <text x="250" y="329" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">${esc(trunc(clean(title),32))}</text>
</svg>`;
}

// ==================== CARD HELPER ====================
function card(x, y, w, h, headerText, t, content) {
  return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="6" fill="white" stroke="${t.c1}" stroke-width="1.5" opacity="0.95"/>
  <rect x="${x}" y="${y}" width="${w}" height="24" rx="6" fill="${t.c1}" opacity="0.9"/>
  <rect x="${x}" y="${y+18}" width="${w}" height="8" fill="${t.c1}" opacity="0.9"/>
  <text x="${x+w/2}" y="${y+17}" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">${headerText}</text>
  <line x1="${x+8}" y1="${y+26}" x2="${x+w-8}" y2="${y+26}" stroke="#E0E0E0" stroke-width="1"/>
  ${content}`;
}

// ==================== MATH ILLUSTRATIONS ====================
function mathIll(lessonNum, title, t) {
  // Determine illustration based on lesson number
  if (lessonNum <= 4) {
    // Numbers / place value - show number with place value breakdown
    const num = [3587, 52401, 389120, 67450][lessonNum-1];
    const digits = String(num).split('');
    const labels = ['Ед.','Дес.','Сот.','Тыс.','Дес.тыс.','Сот.тыс.'];
    let placeValue = '';
    digits.forEach((d, i) => {
      const x = 70 + i * 55;
      const label = labels[digits.length - 1 - i];
      placeValue += `<rect x="${x}" y="110" width="45" height="45" rx="4" fill="${i%2===0?t.c1:t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1"/>
      <text x="${x+22}" y="138" font-family="Arial,sans-serif" font-size="22" fill="${t.c1}" text-anchor="middle" font-weight="bold">${d}</text>
      <text x="${x+22}" y="168" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">${label}</text>`;
    });
    const fact1 = lessonNum<=2 ? 'Разряды: единицы, десятки, сотни' : 'Класс тысяч: тысячи, десятки, сотни тысяч';
    const fact2 = lessonNum<=2 ? '10 единиц = 1 десяток' : '1000 единиц = 1 тысяча';
    return baseSVG(t, title, lessonNum,
      card(20, 88, 460, 100, 'РАЗРЯДНЫЙ СОСТАВ', t, placeValue +
        `<text x="250" y="195" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle" font-weight="bold">${num}</text>`) +
      card(20, 198, 220, 95, 'ПРАВИЛО', t,
        `<text x="35" y="235" font-family="Arial,sans-serif" font-size="9" fill="#555">${esc(fact1)}</text>
        <text x="35" y="255" font-family="Arial,sans-serif" font-size="9" fill="#555">${esc(fact2)}</text>`) +
      card(260, 198, 220, 95, 'ПРИМЕР', t,
        `<text x="275" y="235" font-family="Arial,sans-serif" font-size="9" fill="#555">${num} = ${digits.map((d,i)=>d+(labels[digits.length-1-i]==='Ед.'?'':labels[digits.length-1-i]==='Дес.'?'0':labels[digits.length-1-i]==='Сот.'?'00':labels[digits.length-1-i]==='Тыс.'?'000':labels[digits.length-1-i]==='Дес.тыс.'?'0000':'00000')).join(' + ')}</text>`)
    );
  }
  if (lessonNum <= 10) {
    // Arithmetic operations - show visual operation
    const ops = ['+','-','x','/','x0','/0'];
    const opIdx = lessonNum - 5;
    const op = ops[opIdx] || '+';
    const a = [3456, 8000, 234, 672, 450, 3600][opIdx] || 100;
    const b = [2789, 3567, 6, 8, 100, 90][opIdx] || 10;
    let opSymbol = op.replace('x0','x').replace('/0','/');
    const result = op==='+' ? a+b : op==='-' ? a-b : op==='x' ? a*b : op==='/' ? Math.floor(a/b) : op==='x0' ? a*b : a;
    let visual = `<text x="250" y="130" font-family="Arial,sans-serif" font-size="28" fill="${t.c1}" text-anchor="middle" font-weight="bold">${a} ${opSymbol} ${b}</text>
    <line x1="150" y1="145" x2="350" y2="145" stroke="${t.c1}" stroke-width="3"/>
    <text x="250" y="180" font-family="Arial,sans-serif" font-size="32" fill="${t.c4}" text-anchor="middle" font-weight="bold">${result}</text>`;
    if (opIdx >= 4) {
      visual += `<text x="250" y="200" font-family="Arial,sans-serif" font-size="10" fill="#777" text-anchor="middle">${opIdx===4?'Добавляем нули к произведению':'Убираем нули при делении'}</text>`;
    }
    const tips = [
      'Складываем поразрядно, начиная с единиц',
      'Занимаем единицу из старшего разряда',
      'Умножаем каждую цифру на множитель',
      'Делим поразрядно, начиная со старшего',
      'Умножаем, затем добавляем нули',
      'Делим, затем добавляем нули'
    ];
    return baseSVG(t, title, lessonNum,
      card(20, 88, 460, 130, 'ВЫЧИСЛЕНИЕ', t, visual) +
      card(20, 228, 460, 65, 'АЛГОРИТМ', t,
        `<text x="35" y="260" font-family="Arial,sans-serif" font-size="10" fill="#555">${esc(tips[opIdx]||'')}</text>`)
    );
  }
  if (lessonNum <= 16) {
    // Fractions - show circle fractions
    const fracs = [
      {n:1,d:2,label:'1/2'}, {n:1,d:3,label:'1/3'}, {n:1,d:4,label:'1/4'}, {n:3,d:4,label:'3/4'},
      {n:1,d:5,label:'1/5'}, {n:2,d:5,label:'2/5'}
    ];
    const fi = lessonNum - 11;
    const f = fracs[fi];
    // Draw two fraction circles
    let fracVis = '';
    [100, 380].forEach((cx, idx) => {
      const fr = idx===0 ? f : (fi<4 ? fracs[fi+1]||fracs[0] : fracs[fi-1]||fracs[0]);
      const cy = 155;
      const r = 50;
      fracVis += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="white" stroke="${t.c1}" stroke-width="2"/>`;
      // Filled pie slice
      const angle = (fr.n / fr.d) * 360;
      const rad = angle * Math.PI / 180;
      const x2 = cx + r * Math.sin(rad);
      const y2 = cy - r * Math.cos(rad);
      const largeArc = angle > 180 ? 1 : 0;
      if (fr.n === fr.d) {
        fracVis += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${t.c2}" opacity="0.3"/>`;
      } else if (fr.n === 1 && fr.d === 2) {
        fracVis += `<path d="M${cx},${cy} L${cx},${cy-r} A${r},${r} 0 0,1 ${cx},${cy+r} Z" fill="${t.c2}" opacity="0.3"/>`;
      } else {
        fracVis += `<path d="M${cx},${cy} L${cx},${cy-r} A${r},${r} 0 ${largeArc},1 ${x2},${y2} Z" fill="${t.c2}" opacity="0.3"/>`;
      }
      fracVis += `<text x="${cx}" y="${cy+5}" font-family="Arial,sans-serif" font-size="16" fill="${t.c1}" text-anchor="middle" font-weight="bold">${fr.label}</text>`;
    });
    const ops = ['Доля — равная часть','Чем больше знаменатель, тем меньше доля','Одинаковый знаменатель — сравниваем числители','Складываем числители','Вычитаем числители','Находим часть от числа'];
    return baseSVG(t, title, lessonNum,
      card(20, 88, 460, 130, 'ДРОБИ', t, fracVis) +
      card(20, 228, 460, 65, 'ПРАВИЛО', t,
        `<text x="35" y="260" font-family="Arial,sans-serif" font-size="10" fill="#555">${esc(ops[fi]||'')}</text>`)
    );
  }
  if (lessonNum <= 20) {
    // Geometry - shapes and measurements
    const shapes = [
      // 17: Geometric figures
      `<polygon points="100,220 160,130 220,220" fill="none" stroke="${t.c1}" stroke-width="2"/>
      <rect x="270" y="130" width="80" height="80" fill="none" stroke="${t.c1}" stroke-width="2"/>
      <circle cx="420" cy="170" r="40" fill="none" stroke="${t.c1}" stroke-width="2"/>
      <text x="160" y="240" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Треугольник</text>
      <text x="310" y="240" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Прямоугольник</text>
      <text x="420" y="240" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Круг</text>`,
      // 18: Area of rectangle
      `<rect x="100" y="110" width="200" height="140" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="2"/>
      <line x1="100" y1="100" x2="300" y2="100" stroke="${t.c4}" stroke-width="1.5"/>
      <text x="200" y="96" font-family="Arial,sans-serif" font-size="11" fill="${t.c4}" text-anchor="middle">a = 5 см</text>
      <line x1="90" y1="110" x2="90" y2="250" stroke="${t.c4}" stroke-width="1.5"/>
      <text x="75" y="180" font-family="Arial,sans-serif" font-size="11" fill="${t.c4}" text-anchor="middle" transform="rotate(-90,75,180)">b = 7 см</text>
      <text x="200" y="190" font-family="Arial,sans-serif" font-size="18" fill="${t.c1}" text-anchor="middle" font-weight="bold">S = a x b</text>
      <text x="200" y="210" font-family="Arial,sans-serif" font-size="14" fill="${t.c4}" text-anchor="middle">S = 35 кв.см</text>`,
      // 19: Area units
      `<rect x="50" y="110" width="30" height="30" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1"/>
      <text x="65" y="155" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">мм2</text>
      <rect x="100" y="110" width="40" height="40" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1"/>
      <text x="120" y="165" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">см2</text>
      <rect x="160" y="110" width="55" height="55" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1"/>
      <text x="187" y="180" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">дм2</text>
      <rect x="240" y="110" width="75" height="75" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1"/>
      <text x="277" y="200" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">м2</text>
      <text x="370" y="140" font-family="Arial,sans-serif" font-size="9" fill="#555">1 см2 = 100 мм2</text>
      <text x="370" y="158" font-family="Arial,sans-serif" font-size="9" fill="#555">1 дм2 = 100 см2</text>
      <text x="370" y="176" font-family="Arial,sans-serif" font-size="9" fill="#555">1 м2 = 100 дм2</text>`,
      // 20: 3D shapes
      `<rect x="60" y="150" width="70" height="70" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
      <line x1="60" y1="150" x2="85" y2="125" stroke="${t.c1}" stroke-width="1.5"/>
      <line x1="130" y1="150" x2="155" y2="125" stroke="${t.c1}" stroke-width="1.5"/>
      <line x1="130" y1="220" x2="155" y2="195" stroke="${t.c1}" stroke-width="1.5"/>
      <rect x="85" y="125" width="70" height="70" fill="none" stroke="${t.c1}" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="155" y1="125" x2="155" y2="195" stroke="${t.c1}" stroke-width="1.5"/>
      <text x="107" y="245" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Куб</text>
      <ellipse cx="320" cy="190" rx="55" ry="25" fill="none" stroke="${t.c1}" stroke-width="1.5"/>
      <line x1="265" y1="190" x2="265" y2="130" stroke="${t.c1}" stroke-width="1.5"/>
      <line x1="375" y1="190" x2="375" y2="130" stroke="${t.c1}" stroke-width="1.5"/>
      <ellipse cx="320" cy="130" rx="55" ry="25" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
      <text x="320" y="245" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Цилиндр</text>`
    ];
    const shapeIdx = lessonNum - 17;
    const content = shapes[shapeIdx] || shapes[0];
    const tips = ['Многоугольники и окружность','Площадь = длина x ширина','Каждая единица в 100 раз больше','Объёмные тела в пространстве'];
    return baseSVG(t, title, lessonNum,
      card(20, 88, 460, 170, 'ГЕОМЕТРИЯ', t, content) +
      card(20, 268, 460, 30, '', t,
        `<text x="35" y="290" font-family="Arial,sans-serif" font-size="10" fill="#555">${esc(tips[shapeIdx]||'')}</text>`)
    );
  }
  // Lessons 21-28: Units and word problems
  if (lessonNum <= 24) {
    // Units: length, mass, time, quantities
    const unitData = [
      {title:'ЕДИНИЦЫ ДЛИНЫ', units:['1 мм','1 см = 10 мм','1 дм = 10 см','1 м = 10 дм','1 км = 1000 м'], icon:`<line x1="50" y1="180" x2="450" y2="180" stroke="${t.c1}" stroke-width="2"/><line x1="50" y1="175" x2="50" y2="185" stroke="${t.c1}" stroke-width="2"/><line x1="450" y1="175" x2="450" y2="185" stroke="${t.c1}" stroke-width="2"/><text x="250" y="200" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle">Линейка</text>`},
      {title:'ЕДИНИЦЫ МАССЫ', units:['1 г','1 кг = 1000 г','1 ц = 100 кг','1 т = 1000 кг'], icon:`<rect x="190" y="120" width="8" height="60" fill="${t.c1}" opacity="0.5"/><rect x="180" y="175" width="30" height="8" rx="2" fill="${t.c1}" opacity="0.5"/><line x1="198" y1="145" x2="150" y2="115" stroke="${t.c1}" stroke-width="1.5"/><line x1="198" y1="145" x2="250" y2="125" stroke="${t.c1}" stroke-width="1.5"/><rect x="135" y="105" width="30" height="15" rx="3" fill="${t.c2}" opacity="0.3" stroke="${t.c1}"/><rect x="235" y="115" width="30" height="15" rx="3" fill="${t.c2}" opacity="0.3" stroke="${t.c1}"/>`},
      {title:'ЕДИНИЦЫ ВРЕМЕНИ', units:['1 мин = 60 сек','1 ч = 60 мин','1 сут = 24 ч','1 год = 365 сут'], icon:`<circle cx="300" cy="160" r="45" fill="none" stroke="${t.c1}" stroke-width="2"/><line x1="300" y1="160" x2="300" y2="130" stroke="${t.c1}" stroke-width="2"/><line x1="300" y1="160" x2="325" y2="160" stroke="${t.c2}" stroke-width="1.5"/><circle cx="300" cy="160" r="3" fill="${t.c1}"/><text x="300" y="115" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">12</text><text x="350" y="164" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">3</text><text x="300" y="215" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">6</text><text x="250" y="164" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">9</text>`},
      {title:'ДЕЙСТВИЯ С ВЕЛИЧИНАМИ', units:['Складываем одинаковые единицы','Переводим в одну единицу','Сравниваем после перевода','Умножаем и делим величины'], icon:`<text x="250" y="150" font-family="Arial,sans-serif" font-size="24" fill="${t.c1}" text-anchor="middle" font-weight="bold">3 кг + 2 кг = 5 кг</text><text x="250" y="180" font-family="Arial,sans-serif" font-size="14" fill="#555" text-anchor="middle">Одинаковые единицы можно складывать</text>`}
    ];
    const ud = unitData[lessonNum - 21];
    let unitList = ud.units.map((u,i) => `<rect x="35" y="${105+i*22}" width="8" height="8" rx="1" fill="${t.c1}" opacity="0.3"/><text x="50" y="${113+i*22}" font-family="Arial,sans-serif" font-size="10" fill="#555">${esc(u)}</text>`).join('\n');
    return baseSVG(t, title, lessonNum,
      card(20, 88, 240, 200, ud.title, t, unitList) +
      card(260, 88, 220, 200, 'СХЕМА', t, ud.icon)
    );
  }
  // Word problems 25-28
  const problemTypes = [
    {title:'ДВИЖЕНИЕ', formula:'S = v x t', example:'60 км/ч x 3 ч = 180 км',
     icon:`<line x1="60" y1="200" x2="440" y2="200" stroke="${t.c1}" stroke-width="2"/><circle cx="60" cy="195" r="4" fill="${t.c1}"/><circle cx="440" cy="195" r="4" fill="${t.c1}"/><rect x="120" y="175" width="50" height="25" rx="5" fill="${t.c2}" opacity="0.3" stroke="${t.c1}"/><text x="145" y="192" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">v=60</text><line x1="170" y1="187" x2="210" y2="187" stroke="${t.c1}" stroke-width="2" marker-end="url(#arr)"/><text x="250" y="192" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">t=3ч</text><text x="250" y="165" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">180 км</text>`},
    {title:'ВСТРЕЧНОЕ ДВИЖЕНИЕ', formula:'S = (v1+v2) x t', example:'(40+50) x 2 = 180 км',
     icon:`<line x1="60" y1="200" x2="440" y2="200" stroke="${t.c1}" stroke-width="2"/><rect x="80" y="180" width="40" height="20" rx="5" fill="${t.c2}" opacity="0.3" stroke="${t.c1}"/><line x1="120" y1="190" x2="170" y2="190" stroke="${t.c1}" stroke-width="2"/><rect x="420" y="180" width="40" height="20" rx="5" fill="${t.c2}" opacity="0.3" stroke="${t.c4}"/><line x1="420" y1="190" x2="370" y2="190" stroke="${t.c4}" stroke-width="2"/><text x="100" y="175" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}">v1</text><text x="440" y="175" font-family="Arial,sans-serif" font-size="8" fill="${t.c4}">v2</text>`},
    {title:'РАБОТА', formula:'A = v x t', example:'10 дет/ч x 6 ч = 60 дет',
     icon:`<rect x="150" y="130" width="200" height="20" rx="3" fill="${t.c2}" opacity="0.3" stroke="${t.c1}"/><rect x="150" y="160" width="140" height="20" rx="3" fill="${t.c2}" opacity="0.2" stroke="${t.c1}"/><rect x="150" y="190" width="80" height="20" rx="3" fill="${t.c2}" opacity="0.1" stroke="${t.c1}"/><text x="250" y="145" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Производительность v</text><text x="220" y="175" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Время t</text><text x="190" y="205" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Работа A</text>`},
    {title:'СТОИМОСТЬ', formula:'C = a x n', example:'50 руб x 3 шт = 150 руб',
     icon:`<circle cx="200" cy="170" r="40" fill="none" stroke="${t.c1}" stroke-width="2"/><text x="200" y="175" font-family="Arial,sans-serif" font-size="16" fill="${t.c1}" text-anchor="middle">C</text><line x1="200" y1="130" x2="130" y2="100" stroke="${t.c1}" stroke-width="1.5"/><line x1="200" y1="130" x2="270" y2="100" stroke="${t.c1}" stroke-width="1.5"/><circle cx="130" cy="95" r="25" fill="none" stroke="${t.c2}" stroke-width="1.5"/><text x="130" y="100" font-family="Arial,sans-serif" font-size="12" fill="${t.c2}" text-anchor="middle">a</text><circle cx="270" cy="95" r="25" fill="none" stroke="${t.c2}" stroke-width="1.5"/><text x="270" y="100" font-family="Arial,sans-serif" font-size="12" fill="${t.c2}" text-anchor="middle">n</text><text x="130" y="130" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Цена</text><text x="270" y="130" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Кол-во</text>`}
  ];
  const pt = problemTypes[lessonNum - 25];
  return baseSVG(t, title, lessonNum,
    card(20, 88, 460, 80, pt.title, t,
      `<text x="250" y="120" font-family="Arial,sans-serif" font-size="20" fill="${t.c1}" text-anchor="middle" font-weight="bold">${pt.formula}</text>
      <text x="250" y="145" font-family="Arial,sans-serif" font-size="11" fill="#555" text-anchor="middle">${esc(pt.example)}</text>`) +
    card(20, 178, 460, 110, 'СХЕМА ЗАДАЧИ', t, pt.icon)
  );
}

// ==================== RUSSIAN ILLUSTRATIONS ====================
function russianIll(lessonNum, title, t) {
  if (lessonNum <= 3) {
    // Sentence structure
    const diagrams = [
      `<rect x="40" y="110" width="420" height="40" rx="6" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
      <text x="250" y="135" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle">Подлежащее  +  Сказуемое</text>
      <line x1="165" y1="120" x2="165" y2="140" stroke="${t.c1}" stroke-width="1"/>
      <line x1="335" y1="120" x2="335" y2="140" stroke="${t.c1}" stroke-width="1"/>
      <text x="250" y="175" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Предложение выражает законченную мысль</text>
      <text x="250" y="200" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Начинается с большой буквы, заканчивается . ! ?</text>`,
      `<rect x="60" y="110" width="140" height="50" rx="6" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="2"/>
      <text x="130" y="140" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle" font-weight="bold">Подлежащее</text>
      <text x="130" y="170" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">(кто? что?)</text>
      <rect x="300" y="110" width="140" height="50" rx="6" fill="${t.c2}" opacity="0.3" stroke="${t.c4}" stroke-width="2"/>
      <text x="370" y="140" font-family="Arial,sans-serif" font-size="12" fill="${t.c4}" text-anchor="middle" font-weight="bold">Сказуемое</text>
      <text x="370" y="170" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">(что делает?)</text>
      <line x1="200" y1="135" x2="300" y2="135" stroke="${t.c1}" stroke-width="2"/>`,
      `<rect x="40" y="100" width="200" height="30" rx="4" fill="${t.c2}" opacity="0.2" stroke="${t.c1}"/>
      <text x="140" y="120" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle">Главные члены</text>
      <rect x="260" y="100" width="200" height="30" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c2}"/>
      <text x="360" y="120" font-family="Arial,sans-serif" font-size="10" fill="${t.c2}" text-anchor="middle">Второстепенные члены</text>
      <rect x="60" y="140" width="80" height="25" rx="4" fill="${t.c1}" opacity="0.1"/><text x="100" y="157" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Подлежащее</text>
      <rect x="150" y="140" width="80" height="25" rx="4" fill="${t.c1}" opacity="0.1"/><text x="190" y="157" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Сказуемое</text>
      <rect x="270" y="140" width="80" height="25" rx="4" fill="${t.c2}" opacity="0.1"/><text x="310" y="157" font-family="Arial,sans-serif" font-size="8" fill="${t.c2}" text-anchor="middle">Определение</text>
      <rect x="360" y="140" width="80" height="25" rx="4" fill="${t.c2}" opacity="0.1"/><text x="400" y="157" font-family="Arial,sans-serif" font-size="8" fill="${t.c2}" text-anchor="middle">Дополнение</text>`
    ];
    return baseSVG(t, title, lessonNum,
      card(20, 88, 460, 130, 'СТРУКТУРА ПРЕДЛОЖЕНИЯ', t, diagrams[lessonNum-1]) +
      card(20, 228, 460, 65, 'ПРАВИЛО', t,
        `<text x="35" y="258" font-family="Arial,sans-serif" font-size="10" fill="#555">${esc(['Основа предложения — подлежащее и сказуемое','Подлежащее отвечает на вопрос кто? что?','Второстепенные члены поясняют главные'][lessonNum-1])}</text>`)
    );
  }
  if (lessonNum <= 6) {
    // Word structure: root, prefix, suffix, ending
    const parts = [
      {label:'КОРЕНЬ', desc:'Общая часть родственных слов', ex:'лес - лесной - лесник'},
      {label:'ПРИСТАВКА И СУФФИКС', desc:'Приставка перед корнем, суффикс после', ex:'пере-ход-ить, дом-ик'},
      {label:'ОКОНЧАНИЕ', desc:'Изменяемая часть слова', ex:'дом, дома, дому, домом'}
    ];
    const p = parts[lessonNum-4];
    let wordDiagram = '';
    if (lessonNum === 4) {
      wordDiagram = `<rect x="80" y="115" width="340" height="40" rx="6" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="2"/>
      <text x="250" y="140" font-family="Arial,sans-serif" font-size="18" fill="${t.c1}" text-anchor="middle" font-weight="bold">лес</text>
      <line x1="80" y1="155" x2="80" y2="170" stroke="${t.c1}" stroke-width="1"/><line x1="420" y1="155" x2="420" y2="170" stroke="${t.c1}" stroke-width="1"/>
      <rect x="80" y="170" width="340" height="25" rx="4" fill="${t.c1}" opacity="0.1"/>
      <text x="250" y="187" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle">Корень «лес» — общая часть</text>
      <text x="120" y="220" font-family="Arial,sans-serif" font-size="11" fill="#555">лес</text>
      <text x="200" y="220" font-family="Arial,sans-serif" font-size="11" fill="#555">лесной</text>
      <text x="300" y="220" font-family="Arial,sans-serif" font-size="11" fill="#555">лесник</text>
      <rect x="115" y="224" width="30" height="12" rx="2" fill="${t.c2}" opacity="0.3"/><rect x="195" y="224" width="30" height="12" rx="2" fill="${t.c2}" opacity="0.3"/><rect x="295" y="224" width="30" height="12" rx="2" fill="${t.c2}" opacity="0.3"/>`;
    } else if (lessonNum === 5) {
      wordDiagram = `<rect x="50" y="115" width="80" height="35" rx="4" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="90" y="137" font-family="Arial,sans-serif" font-size="10" fill="#4CAF50" text-anchor="middle">Приставка</text>
      <rect x="140" y="115" width="100" height="35" rx="4" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="2"/>
      <text x="190" y="137" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle" font-weight="bold">Корень</text>
      <rect x="250" y="115" width="80" height="35" rx="4" fill="#FFF3E0" stroke="#FF9800" stroke-width="1.5"/>
      <text x="290" y="137" font-family="Arial,sans-serif" font-size="10" fill="#FF9800" text-anchor="middle">Суффикс</text>
      <rect x="340" y="115" width="80" height="35" rx="4" fill="#F3E5F5" stroke="#9C27B0" stroke-width="1.5"/>
      <text x="380" y="137" font-family="Arial,sans-serif" font-size="10" fill="#9C27B0" text-anchor="middle">Окончание</text>
      <text x="250" y="175" font-family="Arial,sans-serif" font-size="14" fill="#555" text-anchor="middle">пере-ход-ик-а</text>
      <rect x="170" y="180" width="50" height="3" fill="#4CAF50"/><rect x="220" y="180" width="60" height="3" fill="${t.c1}"/><rect x="280" y="180" width="40" height="3" fill="#FF9800"/><rect x="320" y="180" width="30" height="3" fill="#9C27B0"/>`;
    } else {
      wordDiagram = `<text x="250" y="130" font-family="Arial,sans-serif" font-size="16" fill="#555" text-anchor="middle">дом  /  дома  /  дому  /  домом</text>
      <rect x="100" y="145" width="60" height="25" rx="4" fill="#F3E5F5" stroke="#9C27B0" stroke-width="1.5"/>
      <text x="130" y="162" font-family="Arial,sans-serif" font-size="10" fill="#9C27B0" text-anchor="middle">нулевое</text>
      <rect x="190" y="145" width="60" height="25" rx="4" fill="#F3E5F5" stroke="#9C27B0" stroke-width="1.5"/>
      <text x="220" y="162" font-family="Arial,sans-serif" font-size="10" fill="#9C27B0" text-anchor="middle">-а</text>
      <rect x="280" y="145" width="60" height="25" rx="4" fill="#F3E5F5" stroke="#9C27B0" stroke-width="1.5"/>
      <text x="310" y="162" font-family="Arial,sans-serif" font-size="10" fill="#9C27B0" text-anchor="middle">-у</text>
      <rect x="370" y="145" width="60" height="25" rx="4" fill="#F3E5F5" stroke="#9C27B0" stroke-width="1.5"/>
      <text x="400" y="162" font-family="Arial,sans-serif" font-size="10" fill="#9C27B0" text-anchor="middle">-ом</text>`;
    }
    return baseSVG(t, title, lessonNum,
      card(20, 88, 460, 160, p.label, t, wordDiagram) +
      card(20, 258, 460, 35, '', t,
        `<text x="35" y="282" font-family="Arial,sans-serif" font-size="10" fill="#555">${esc(p.desc + ': ' + p.ex)}</text>`)
    );
  }
  // Parts of speech and spelling rules
  if (lessonNum <= 10) {
    const posData = [
      {name:'ИМЯ СУЩЕСТВИТЕЛЬНОЕ', q:'кто? что?', ex:'стол, кот, Москва, дружба', color:t.c1},
      {name:'ИМЯ ПРИЛАГАТЕЛЬНОЕ', q:'какой? какая? какие?', ex:'красный, большой, добрый', color:'#FF9800'},
      {name:'ГЛАГОЛ', q:'что делать? что сделать?', ex:'бежать, читать, рисовать', color:'#4CAF50'},
      {name:'МЕСТОИМЕНИЕ', q:'кто? что? (вместо имени)', ex:'я, ты, он, мы, они', color:'#9C27B0'}
    ];
    const pd = posData[lessonNum-7];
    return baseSVG(t, title, lessonNum,
      card(20, 88, 460, 100, pd.name, t,
        `<text x="250" y="130" font-family="Arial,sans-serif" font-size="18" fill="${pd.color}" text-anchor="middle" font-weight="bold">${pd.q}</text>
        <text x="250" y="160" font-family="Arial,sans-serif" font-size="12" fill="#555" text-anchor="middle">${esc(pd.ex)}</text>`) +
      card(20, 198, 460, 95, 'ПРИЗНАКИ', t,
        `<rect x="35" y="215" width="90" height="22" rx="11" fill="${pd.color}" opacity="0.15"/><text x="80" y="230" font-family="Arial,sans-serif" font-size="9" fill="${pd.color}" text-anchor="middle">Число</text>
        <rect x="135" y="215" width="90" height="22" rx="11" fill="${pd.color}" opacity="0.15"/><text x="180" y="230" font-family="Arial,sans-serif" font-size="9" fill="${pd.color}" text-anchor="middle">Род</text>
        <rect x="235" y="215" width="90" height="22" rx="11" fill="${pd.color}" opacity="0.15"/><text x="280" y="230" font-family="Arial,sans-serif" font-size="9" fill="${pd.color}" text-anchor="middle">Падеж</text>
        <rect x="335" y="215" width="120" height="22" rx="11" fill="${pd.color}" opacity="0.15"/><text x="395" y="230" font-family="Arial,sans-serif" font-size="9" fill="${pd.color}" text-anchor="middle">Склонение</text>`)
    );
  }
  // Spelling rules 11-13
  const spellData = [
    {name:'БЕЗУДАРНЫЕ ГЛАСНЫЕ', rule:'Проверяй ударением: измени форму слова', ex:'л\у0433а — луг, тр\у0433а — травы', visual:`<text x="250" y="140" font-family="Arial,sans-serif" font-size="20" fill="${t.c1}" text-anchor="middle">тр а в а</text><line x1="230" y1="148" x2="270" y2="148" stroke="red" stroke-width="3"/><text x="250" y="170" font-family="Arial,sans-serif" font-size="11" fill="#555" text-anchor="middle">тр а вы — под ударением</text>`},
    {name:'ПАРНЫЕ СОГЛАСНЫЕ', rule:'Проверяй перед гласной или н', ex:'ду[п] — дубы, мя[к]ий — мягок', visual:`<text x="250" y="140" font-family="Arial,sans-serif" font-size="20" fill="${t.c1}" text-anchor="middle">дуб / дубы</text><circle cx="205" cy="135" r="12" fill="red" opacity="0.15"/><text x="250" y="170" font-family="Arial,sans-serif" font-size="11" fill="#555" text-anchor="middle">Проверочное слово: перед гласной</text>`},
    {name:'РАЗДЕЛИТЕЛЬНЫЕ Ь И Ъ', rule:'Ь перед е,ё,ю,я,и в корне; Ъ после приставки', ex:'вьются, подъезд', visual:`<rect x="100" y="115" width="130" height="40" rx="6" fill="${t.c2}" opacity="0.2" stroke="${t.c1}"/><text x="165" y="140" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle">в ь ются</text><rect x="270" y="115" width="130" height="40" rx="6" fill="${t.c2}" opacity="0.2" stroke="${t.c4}"/><text x="335" y="140" font-family="Arial,sans-serif" font-size="14" fill="${t.c4}" text-anchor="middle">под ъ езд</text><text x="165" y="172" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">Ь — в корне/перед окончанием</text><text x="335" y="172" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">Ъ — после приставки на согласн.</text>`}
  ];
  const sp = spellData[lessonNum-11];
  return baseSVG(t, title, lessonNum,
    card(20, 88, 460, 110, sp.name, t, sp.visual) +
    card(20, 208, 460, 85, 'ПРАВИЛО', t,
      `<text x="35" y="238" font-family="Arial,sans-serif" font-size="11" fill="#555">${esc(sp.rule)}</text>
      <text x="35" y="265" font-family="Arial,sans-serif" font-size="11" fill="${t.c1}" font-weight="bold">${esc(sp.ex)}</text>`)
  );
}

// ==================== GENERIC SUBJECT ILLUSTRATIONS ====================
// For subjects with too many unique lessons, create themed illustrations
function genericIll(subj, lessonNum, title, t) {
  const cleanTitle = clean(title);

  // Each subject has its own set of illustration builders
  const builders = {
    english: () => {
      const themes = [
        {h:'GREETINGS',items:['Hello!','Hi!','Good morning!','Good afternoon!']},
        {h:'INTRODUCTIONS',items:["My name is...","I'm from...","Nice to meet you!","How do you do?"]},
        {h:'POLITE WORDS',items:['Please','Thank you','Sorry','Excuse me']},
        {h:'QUESTION WORDS',items:['Who?','What?','Where?','When?','Why?','How?']},
        {h:'COLOURS',items:['Red','Blue','Green','Yellow','Orange','Purple']},
        {h:'NUMBERS',items:['1-10: one two three...','11-20: eleven twelve...','30, 40, 50...','100: a hundred']},
        {h:'BODY PARTS',items:['Head','Arms','Legs','Eyes & Ears']},
        {h:'CLOTHES',items:['Shirt','Trousers','Dress','Jacket']},
        {h:'SCHOOL THINGS',items:['Pen & Pencil','Book & Notebook','Ruler & Eraser','Bag']},
        {h:'IN CLASS',items:['Desk','Board','Teacher','Pupil']},
        {h:'SCHOOL SUBJECTS',items:['Maths','English','Science','Art']},
        {h:'TIMETABLE',items:['Monday','Tuesday','Wednesday','Thursday','Friday']},
        {h:'FAMILY',items:['Mother','Father','Sister','Brother']},
        {h:'MY HOUSE',items:['Kitchen','Bedroom','Bathroom','Living room']},
        {h:'MY ROOM',items:['Bed','Desk','Wardrobe','Shelf']},
        {h:'WEEKDAYS & WEEKEND',items:['School days','Weekend','Morning routine','Free time']},
        {h:'FOOD',items:['Bread','Cheese','Meat','Rice']},
        {h:'DRINKS',items:['Water','Tea','Milk','Juice']},
        {h:'FRUIT & VEGETABLES',items:['Apple & Banana','Carrot & Potato','Tomato & Cucumber','Orange & Grape']},
        {h:'AT A CAFE',items:['Menu','Order','Bill','Waiter']},
        {h:'TRANSPORT',items:['Bus','Car','Train','Bicycle']},
        {h:'IN THE CITY',items:['Street','Park','Shop','Hospital']},
        {h:'SIGHTS',items:['Museum','Monument','Bridge','Tower']},
        {h:'COUNTRIES',items:['Russia','Great Britain','USA','France']}
      ];
      const th = themes[lessonNum-1] || themes[0];
      const itemsSvg = th.items.map((item,i) => {
        const col = i % 2;
        const row = Math.floor(i / 2);
        const x = 35 + col * 230;
        const y = 115 + row * 35;
        return `<rect x="${x}" y="${y}" width="210" height="28" rx="6" fill="${t.c2}" opacity="${0.1+col*0.05}" stroke="${t.c1}" stroke-width="1"/>
        <text x="${x+105}" y="${y+19}" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle">${esc(item)}</text>`;
      }).join('\n');
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, th.h, t, itemsSvg));
    },

    nature: () => {
      const ills = [
        // Climate
        `<circle cx="250" cy="160" r="60" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="2"/>
        <line x1="250" y1="130" x2="250" y2="100" stroke="${t.c1}" stroke-width="2"/>
        <line x1="250" y1="130" x2="230" y2="115" stroke="${t.c1}" stroke-width="2"/>
        <line x1="250" y1="130" x2="270" y2="115" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="250" cy="160" r="15" fill="${t.c1}" opacity="0.3"/>
        <text x="250" y="240" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Климат — многолетний режим погоды</text>`,
        // Climate zones
        `<rect x="60" y="95" width="380" height="25" rx="4" fill="#B3E5FC" opacity="0.5"/><text x="250" y="112" font-family="Arial,sans-serif" font-size="9" fill="#0277BD" text-anchor="middle">Холодный пояс</text>
        <rect x="60" y="130" width="380" height="35" rx="4" fill="${t.c2}" opacity="0.3"/><text x="250" y="152" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Умеренный пояс</text>
        <rect x="60" y="175" width="380" height="25" rx="4" fill="#FFCCBC" opacity="0.5"/><text x="250" y="192" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" text-anchor="middle">Тропический пояс</text>`,
        // Seasons
        `<rect x="40" y="105" width="100" height="80" rx="6" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5"/><text x="90" y="135" font-family="Arial,sans-serif" font-size="10" fill="#4CAF50" text-anchor="middle">Весна</text><text x="90" y="155" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">март-май</text>
        <rect x="150" y="105" width="100" height="80" rx="6" fill="#FFF9C4" stroke="#F9A825" stroke-width="1.5"/><text x="200" y="135" font-family="Arial,sans-serif" font-size="10" fill="#F9A825" text-anchor="middle">Лето</text><text x="200" y="155" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">июнь-авг</text>
        <rect x="260" y="105" width="100" height="80" rx="6" fill="#FFE0B2" stroke="#E65100" stroke-width="1.5"/><text x="310" y="135" font-family="Arial,sans-serif" font-size="10" fill="#E65100" text-anchor="middle">Осень</text><text x="310" y="155" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">сент-нояб</text>
        <rect x="370" y="105" width="100" height="80" rx="6" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/><text x="420" y="135" font-family="Arial,sans-serif" font-size="10" fill="#1565C0" text-anchor="middle">Зима</text><text x="420" y="155" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">дек-фев</text>`,
        // Climate and life
        `<circle cx="130" cy="155" r="40" fill="#FFCCBC" opacity="0.3" stroke="#BF360C" stroke-width="1.5"/><text x="130" y="150" font-family="Arial,sans-serif" font-size="9" fill="#BF360C" text-anchor="middle">Жаркий</text><text x="130" y="165" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">климат</text>
        <circle cx="370" cy="155" r="40" fill="#B3E5FC" opacity="0.3" stroke="#0277BD" stroke-width="1.5"/><text x="370" y="150" font-family="Arial,sans-serif" font-size="9" fill="#0277BD" text-anchor="middle">Холодный</text><text x="370" y="165" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">климат</text>
        <text x="250" y="155" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Животные и растения</text><text x="250" y="170" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">приспосабливаются</text>`,
        // Bacteria
        `<ellipse cx="150" cy="155" rx="30" ry="15" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <ellipse cx="250" cy="140" rx="20" ry="20" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="250" y1="120" x2="260" y2="105" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="250" y1="120" x2="240" y2="105" stroke="${t.c1}" stroke-width="1.5"/>
        <ellipse cx="350" cy="155" rx="15" ry="25" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="150" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Кокки</text>
        <text x="250" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Палочки</text>
        <text x="350" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Спириллы</text>`,
        // Mushrooms
        `<rect x="170" y="150" width="10" height="50" rx="3" fill="#8D6E63" opacity="0.5"/><ellipse cx="175" cy="150" rx="35" ry="20" fill="${t.c2}" opacity="0.4" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="300" y="155" width="8" height="40" rx="3" fill="#8D6E63" opacity="0.5"/><ellipse cx="304" cy="155" rx="25" ry="15" fill="red" opacity="0.2" stroke="red" stroke-width="1"/>
        <text x="175" y="220" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Шляпка + Ножка</text><text x="304" y="215" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Грибница</text>`,
        // Plants
        `<line x1="250" y1="230" x2="250" y2="130" stroke="#4CAF50" stroke-width="3"/><circle cx="250" cy="120" r="20" fill="#81C784" opacity="0.4" stroke="#4CAF50" stroke-width="1.5"/>
        <ellipse cx="220" cy="160" rx="25" ry="12" fill="#81C784" opacity="0.3" stroke="#4CAF50" stroke-width="1" transform="rotate(-30,220,160)"/>
        <ellipse cx="280" cy="170" rx="25" ry="12" fill="#81C784" opacity="0.3" stroke="#4CAF50" stroke-width="1" transform="rotate(30,280,170)"/>
        <line x1="250" y1="230" x2="220" y2="250" stroke="#795548" stroke-width="1.5"/><line x1="250" y1="230" x2="280" y2="250" stroke="#795548" stroke-width="1.5"/>
        <text x="250" y="270" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Корень — Стебель — Листья — Цветок</text>`,
        // Animals
        `<ellipse cx="150" cy="160" rx="35" ry="25" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/><circle cx="125" cy="145" r="15" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/><circle cx="121" cy="142" r="3" fill="${t.c1}"/>
        <ellipse cx="350" cy="165" rx="20" ry="30" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/><polygon points="340,135 350,120 360,135" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1"/><circle cx="350" y="125" r="2" fill="${t.c1}"/>
        <text x="150" y="200" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Млекопитающие</text>
        <text x="350" y="210" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Птицы</text>`,
        // Ecosystem
        `<circle cx="250" cy="160" r="70" fill="none" stroke="${t.c1}" stroke-width="2" stroke-dasharray="5,5"/>
        <text x="250" y="140" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle" font-weight="bold">Экосистема</text>
        <text x="250" y="160" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Растения</text>
        <text x="250" y="178" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Животные</text>
        <text x="250" y="196" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Грибы + Бактерии</text>
        <line x1="250" y1="155" x2="200" y2="120" stroke="${t.c1}" stroke-width="0.5" opacity="0.5"/>
        <line x1="250" y1="170" x2="310" y2="125" stroke="${t.c1}" stroke-width="0.5" opacity="0.5"/>`,
        // Forest ecosystem
        `<polygon points="100,220 130,130 160,220" fill="#81C784" opacity="0.3" stroke="#4CAF50" stroke-width="1.5"/>
        <polygon points="300,220 330,140 360,220" fill="#81C784" opacity="0.3" stroke="#4CAF50" stroke-width="1.5"/>
        <rect x="125" y="220" width="10" height="20" fill="#795548" opacity="0.5"/>
        <rect x="325" y="220" width="10" height="20" fill="#795548" opacity="0.5"/>
        <circle cx="230" cy="200" r="8" fill="#8D6E63" opacity="0.3" stroke="#795548"/>
        <text x="230" y="250" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Деревья, кустарники, травы, грибы</text>`,
        // Water ecosystem
        `<ellipse cx="250" cy="180" rx="180" ry="60" fill="#B3E5FC" opacity="0.3" stroke="#0277BD" stroke-width="1.5"/>
        <path d="M70,140 Q250,120 430,140" fill="none" stroke="#0277BD" stroke-width="1" opacity="0.5"/>
        <text x="250" y="175" font-family="Arial,sans-serif" font-size="10" fill="#0277BD" text-anchor="middle">Водоём</text>
        <text x="250" y="195" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Рыбы, водоросли, моллюски</text>`,
        // Ecology problems
        `<rect x="60" y="110" width="120" height="80" rx="6" fill="#FFCDD2" opacity="0.5" stroke="#C62828" stroke-width="1.5"/><text x="120" y="145" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Загрязнение</text><text x="120" y="160" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">воздуха</text>
        <rect x="200" y="110" width="120" height="80" rx="6" fill="#FFCDD2" opacity="0.5" stroke="#C62828" stroke-width="1.5"/><text x="260" y="145" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Загрязнение</text><text x="260" y="160" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">воды</text>
        <rect x="340" y="110" width="120" height="80" rx="6" fill="#FFCDD2" opacity="0.5" stroke="#C62828" stroke-width="1.5"/><text x="400" y="145" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">Вырубка</text><text x="400" y="160" font-family="Arial,sans-serif" font-size="9" fill="#C62828" text-anchor="middle">лесов</text>`
      ];
      const ill = ills[lessonNum-1] || ills[0];
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ill));
    },

    history: () => {
      const ills = [
        // 1: Origins of Rus
        `<path d="M80,200 Q150,170 250,180 Q350,190 420,200" fill="none" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="80" cy="200" r="8" fill="${t.c1}"/><text x="80" y="225" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Славяне</text>
        <circle cx="250" cy="180" r="8" fill="${t.c1}"/><text x="250" y="205" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Племена</text>
        <circle cx="420" cy="200" r="8" fill="${t.c1}"/><text x="420" y="225" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Русь</text>`,
        // 2: First princes
        `<rect x="100" y="120" width="300" height="40" rx="6" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="250" y="145" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle" font-weight="bold">Рюрик</text>
        <line x1="250" y1="160" x2="200" y2="180" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="250" y1="160" x2="300" y2="180" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="130" y="180" width="120" height="30" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c2}"/><text x="190" y="200" font-family="Arial,sans-serif" font-size="11" fill="${t.c2}" text-anchor="middle">Олег</text>
        <rect x="270" y="180" width="120" height="30" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c2}"/><text x="330" y="200" font-family="Arial,sans-serif" font-size="11" fill="${t.c2}" text-anchor="middle">Игорь</text>`,
        // 3-4: Igor, Olga, Svyatoslav
        `<rect x="60" y="120" width="120" height="50" rx="6" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="120" y="150" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle">Игорь</text>
        <rect x="200" y="120" width="120" height="50" rx="6" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="260" y="150" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle">Ольга</text>
        <rect x="340" y="120" width="120" height="50" rx="6" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="400" y="150" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle">Святослав</text>
        <line x1="180" y1="145" x2="200" y2="145" stroke="${t.c1}" stroke-width="1"/>
        <line x1="320" y1="145" x2="340" y2="145" stroke="${t.c1}" stroke-width="1"/>
        <text x="250" y="210" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Правление и защита Руси</text>`,
        // 5-6: Vladimir, Christianity
        `<rect x="130" y="110" width="240" height="50" rx="8" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="2"/>
        <text x="250" y="140" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle" font-weight="bold">Князь Владимир</text>
        <text x="250" y="185" font-family="Arial,sans-serif" font-size="12" fill="#555" text-anchor="middle">988 год — Крещение Руси</text>
        <line x1="250" y1="195" x2="250" y2="220" stroke="${t.c1}" stroke-width="2"/>
        <line x1="240" y1="220" x2="260" y2="220" stroke="${t.c1}" stroke-width="3"/>`,
        // 7: Yaroslav the Wise
        `<rect x="100" y="110" width="300" height="50" rx="8" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="2"/>
        <text x="250" y="140" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle" font-weight="bold">Ярослав Мудрый</text>
        <rect x="70" y="175" width="130" height="30" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c1}"/><text x="135" y="195" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Русская Правда</text>
        <rect x="210" y="175" width="100" height="30" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c1}"/><text x="260" y="195" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Храмы</text>
        <rect x="320" y="175" width="100" height="30" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c1}"/><text x="370" y="195" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Книги</text>`,
        // 8: Culture of Ancient Rus
        `<rect x="50" y="115" width="180" height="130" rx="6" fill="#FFF3E0" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="50" y="115" width="180" height="22" rx="6" fill="${t.c1}" opacity="0.8"/>
        <text x="140" y="132" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">АРХИТЕКТУРА</text>
        <polygon points="140,140 100,200 180,200" fill="#FFB74D" opacity="0.3" stroke="${t.c1}"/>
        <rect x="280" y="115" width="180" height="130" rx="6" fill="#E8F5E9" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="280" y="115" width="180" height="22" rx="6" fill="${t.c1}" opacity="0.8"/>
        <text x="370" y="132" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle" font-weight="bold">РЕМЕСЛО</text>
        <circle cx="340" cy="180" r="20" fill="#81C784" opacity="0.2" stroke="${t.c1}"/><circle cx="400" cy="180" r="15" fill="#81C784" opacity="0.2" stroke="${t.c1}"/>`,
        // 9-12: Mongol invasion to liberation
        `<line x1="50" y1="160" x2="450" y2="160" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="100" cy="160" r="6" fill="${t.c1}"/><text x="100" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">1237</text>
        <circle cx="200" cy="160" r="6" fill="${t.c1}"/><text x="200" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">1240</text>
        <circle cx="300" cy="160" r="6" fill="${t.c1}"/><text x="300" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">1380</text>
        <circle cx="400" cy="160" r="6" fill="${t.c1}"/><text x="400" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">1480</text>
        <text x="100" y="145" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Нашествие</text>
        <text x="200" y="145" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Разрушение</text>
        <text x="300" y="145" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Куликово</text>
        <text x="400" y="145" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Освобождение</text>`
      ];
      const ill = ills[Math.min(lessonNum-1, ills.length-1)];
      // For lessons 3-4 and 5-6, reuse adjacent illustrations
      const illIdx = lessonNum<=2 ? lessonNum-1 : lessonNum<=4 ? 2 : lessonNum<=6 ? 4 : lessonNum<=8 ? lessonNum-4 : 8;
      const finalIll = ills[illIdx] || ill;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, finalIll));
    },

    geography: () => {
      const ills = [
        // Russia on map
        `<ellipse cx="250" cy="160" rx="180" ry="80" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="2"/>
        <text x="250" y="155" font-family="Arial,sans-serif" font-size="20" fill="${t.c1}" text-anchor="middle" font-weight="bold">РОССИЯ</text>
        <text x="250" y="178" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Самая большая страна в мире</text>`,
        // Subjects
        `<rect x="50" y="105" width="190" height="80" rx="6" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="145" y="135" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle" font-weight="bold">Республики</text>
        <text x="145" y="155" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">22 республики</text>
        <rect x="260" y="105" width="190" height="80" rx="6" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="355" y="135" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle" font-weight="bold">Области</text>
        <text x="355" y="155" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">46 областей</text>`,
        // Capital
        `<polygon points="210,210 210,140 250,120 290,140 290,210" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="2"/>
        <rect x="230" y="160" width="40" height="50" rx="3" fill="${t.c1}" opacity="0.15"/>
        <text x="250" y="240" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle" font-weight="bold">Москва</text>
        <text x="250" y="258" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Столица России</text>`,
        // Million cities
        `<circle cx="130" cy="155" r="30" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="130" y="152" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Москва</text>
        <text x="130" y="164" font-family="Arial,sans-serif" font-size="7" fill="#777">12 млн</text>
        <circle cx="250" cy="155" r="22" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="250" y="152" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">СПб</text>
        <text x="250" y="164" font-family="Arial,sans-serif" font-size="7" fill="#777">5 млн</text>
        <circle cx="370" cy="155" r="18" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="370" y="152" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Нск</text>
        <text x="370" y="164" font-family="Arial,sans-serif" font-size="7" fill="#777">1.6 млн</text>`,
        // Rivers, lakes, seas, water
        `<path d="M100,110 Q200,150 150,200 Q100,250 200,270" fill="none" stroke="#1565C0" stroke-width="3" opacity="0.5"/>
        <text x="120" y="130" font-family="Arial,sans-serif" font-size="9" fill="#1565C0">Волга</text>
        <ellipse cx="350" cy="160" rx="50" ry="30" fill="#B3E5FC" opacity="0.4" stroke="#0277BD" stroke-width="1.5"/>
        <text x="350" y="165" font-family="Arial,sans-serif" font-size="9" fill="#0277BD" text-anchor="middle">Озеро</text>`,
        // Natural zones
        `<rect x="50" y="100" width="400" height="20" rx="3" fill="#E3F2FD"/><text x="250" y="114" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">Арктическая пустыня</text>
        <rect x="50" y="125" width="400" height="25" rx="3" fill="#C8E6C9"/><text x="250" y="142" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Тундра</text>
        <rect x="50" y="155" width="400" height="35" rx="3" fill="#A5D6A7"/><text x="250" y="177" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle">Лесная зона</text>
        <rect x="50" y="195" width="400" height="25" rx="3" fill="#FFF9C4"/><text x="250" y="212" font-family="Arial,sans-serif" font-size="8" fill="#F57F17" text-anchor="middle">Степь</text>`,
        // Minerals, nature protection
        `<polygon points="150,200 180,140 210,200" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <polygon points="300,200 330,130 360,200" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <circle cx="180" cy="170" r="8" fill="${t.c1}" opacity="0.2"/>
        <circle cx="330" cy="165" r="10" fill="${t.c1}" opacity="0.2"/>
        <text x="250" y="230" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Полезные ископаемые России</text>`
      ];
      const illIdx = Math.min(lessonNum-1, ills.length-1);
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    music: () => {
      const ills = [
        // Instruments
        `<rect x="80" y="120" width="30" height="100" rx="3" fill="#795548" opacity="0.3" stroke="${t.c1}"/><rect x="75" y="110" width="40" height="15" rx="3" fill="#795548" opacity="0.5" stroke="${t.c1}"/>
        <line x1="85" y1="125" x2="85" y2="210" stroke="${t.c1}" stroke-width="0.5"/><line x1="95" y1="125" x2="95" y2="210" stroke="${t.c1}" stroke-width="0.5"/>
        <circle cx="350" cy="160" r="35" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/><line x1="350" y1="125" x2="350" y2="105" stroke="${t.c1}" stroke-width="2"/>
        <text x="95" y="240" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Фортепиано</text><text x="350" y="210" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Барабан</text>`,
        // Music notes
        `<line x1="70" y1="120" x2="430" y2="120" stroke="${t.c1}" stroke-width="0.8" opacity="0.3"/>
        <line x1="70" y1="135" x2="430" y2="135" stroke="${t.c1}" stroke-width="0.8" opacity="0.3"/>
        <line x1="70" y1="150" x2="430" y2="150" stroke="${t.c1}" stroke-width="0.8" opacity="0.3"/>
        <line x1="70" y1="165" x2="430" y2="165" stroke="${t.c1}" stroke-width="0.8" opacity="0.3"/>
        <line x1="70" y1="180" x2="430" y2="180" stroke="${t.c1}" stroke-width="0.8" opacity="0.3"/>
        <ellipse cx="150" cy="130" rx="10" ry="7" fill="${t.c1}" opacity="0.8" transform="rotate(-15,150,130)"/>
        <line x1="160" y1="128" x2="160" y2="95" stroke="${t.c1}" stroke-width="2"/>
        <ellipse cx="250" cy="155" rx="10" ry="7" fill="${t.c1}" opacity="0.8" transform="rotate(-15,250,155)"/>
        <line x1="260" y1="153" x2="260" y2="120" stroke="${t.c1}" stroke-width="2"/>
        <ellipse cx="350" cy="142" rx="10" ry="7" fill="${t.c1}" opacity="0.8" transform="rotate(-15,350,142)"/>
        <line x1="360" y1="140" x2="360" y2="107" stroke="${t.c1}" stroke-width="2"/>`,
        // Composers (3-7), opera, concert, song, folk
        `<rect x="80" y="110" width="340" height="120" rx="8" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="150" cy="155" r="30" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="150" y="160" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle">Портрет</text>
        <text x="300" y="145" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle" font-weight="bold">${esc(trunc(cleanTitle,20))}</text>
        <text x="300" y="165" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Русский композитор</text>
        <rect x="270" y="175" width="60" height="18" rx="9" fill="${t.c1}" opacity="0.15"/><text x="300" y="188" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Произведения</text>`
      ];
      const illIdx = lessonNum<=2 ? lessonNum-1 : 2;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    art: () => {
      const ills = [
        // Genres, still life, portrait, landscape
        `<rect x="60" y="110" width="170" height="120" rx="4" fill="white" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="145" cy="155" r="25" fill="${t.c2}" opacity="0.3"/><rect x="120" y="180" width="20" height="30" rx="2" fill="${t.c2}" opacity="0.2"/>
        <rect x="280" y="110" width="170" height="120" rx="4" fill="white" stroke="${t.c1}" stroke-width="2"/>
        <polygon points="365,125 400,190 330,190" fill="${t.c2}" opacity="0.3"/><circle cx="365" cy="130" r="12" fill="#FFF9C4" opacity="0.5"/>`,
        // Russian artists, museums
        `<rect x="80" y="115" width="150" height="110" rx="4" fill="${t.c2}" opacity="0.1" stroke="${t.c1}" stroke-width="2"/>
        <rect x="85" y="120" width="140" height="80" fill="white" stroke="${t.c1}" stroke-width="1"/>
        <circle cx="155" cy="145" r="15" fill="${t.c2}" opacity="0.3"/><rect x="140" y="165" width="30" height="20" fill="${t.c2}" opacity="0.2"/>
        <rect x="270" y="115" width="150" height="110" rx="4" fill="${t.c2}" opacity="0.1" stroke="${t.c1}" stroke-width="2"/>
        <rect x="275" y="120" width="140" height="80" fill="white" stroke="${t.c1}" stroke-width="1"/>
        <polygon points="345,135 375,175 315,175" fill="${t.c2}" opacity="0.3"/>`,
        // Drawing, color, composition, light
        `<circle cx="200" cy="155" r="50" fill="none" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="185" cy="140" r="15" fill="red" opacity="0.3"/><circle cx="215" cy="140" r="15" fill="blue" opacity="0.3"/>
        <circle cx="200" cy="165" r="15" fill="yellow" opacity="0.3"/>
        <text x="200" y="220" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Основные цвета</text>
        <rect x="320" y="120" width="80" height="100" rx="4" fill="${t.c2}" opacity="0.1" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="340" y1="140" x2="380" y2="140" stroke="${t.c1}" stroke-width="2"/><line x1="340" y1="160" x2="380" y2="160" stroke="${t.c2}" stroke-width="2"/>`
      ];
      const illIdx = Math.min(Math.floor((lessonNum-1)/3), ills.length-1);
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    literature: () => {
      const ills = [
        // Folk tales, magic tales, etc
        `<rect x="130" y="100" width="80" height="110" rx="4" fill="#FFF3E0" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="140" y="110" width="60" height="80" fill="white" stroke="${t.c1}" stroke-width="0.5"/>
        <text x="170" y="145" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Сказка</text>
        <rect x="280" y="100" width="80" height="110" rx="4" fill="#E8F5E9" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="290" y="110" width="60" height="80" fill="white" stroke="${t.c1}" stroke-width="0.5"/>
        <text x="320" y="145" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Былина</text>`,
        // Bogatyrs
        `<polygon points="150,220 150,130 170,110 190,130 190,220" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <circle cx="170" cy="120" r="12" fill="${t.c2}" opacity="0.3"/>
        <line x1="170" y1="140" x2="170" y2="200" stroke="${t.c1}" stroke-width="1"/>
        <text x="170" y="240" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Богатырь</text>
        <rect x="250" y="120" width="140" height="25" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c1}"/>
        <text x="320" y="137" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Защитник Руси</text>`,
        // Authors
        `<rect x="100" y="110" width="300" height="130" rx="8" fill="${t.c2}" opacity="0.1" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="170" cy="155" r="30" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="170" y="160" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Портрет</text>
        <text x="320" y="145" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle" font-weight="bold">${esc(trunc(cleanTitle,22))}</text>
        <text x="320" y="168" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Русский писатель</text>
        <rect x="270" y="180" width="100" height="18" rx="9" fill="${t.c1}" opacity="0.15"/><text x="320" y="193" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Произведения</text>`
      ];
      const illIdx = lessonNum<=4 ? 0 : lessonNum<=7 ? 1 : 2;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    pe: () => {
      const sportsIcons = [
        // Building exercises, gymnastics
        `<line x1="200" y1="200" x2="200" y2="130" stroke="${t.c1}" stroke-width="3"/>
        <circle cx="200" cy="120" r="12" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="200" y1="150" x2="170" y2="180" stroke="${t.c1}" stroke-width="2"/>
        <line x1="200" y1="150" x2="230" y2="180" stroke="${t.c1}" stroke-width="2"/>
        <line x1="200" y1="200" x2="180" y2="250" stroke="${t.c1}" stroke-width="2"/>
        <line x1="200" y1="200" x2="220" y2="250" stroke="${t.c1}" stroke-width="2"/>`,
        // Running, jumping, throwing
        `<line x1="170" y1="200" x2="170" y2="135" stroke="${t.c1}" stroke-width="3"/>
        <circle cx="170" cy="125" r="12" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="170" y1="155" x2="140" y2="175" stroke="${t.c1}" stroke-width="2"/>
        <line x1="170" y1="155" x2="210" y2="145" stroke="${t.c1}" stroke-width="2"/>
        <line x1="170" y1="200" x2="145" y2="250" stroke="${t.c1}" stroke-width="2"/>
        <line x1="170" y1="200" x2="200" y2="240" stroke="${t.c1}" stroke-width="2"/>
        <path d="M210,240 L230,240 L230,235" fill="none" stroke="${t.c1}" stroke-width="1" opacity="0.5"/>`,
        // Ball sports
        `<circle cx="250" cy="160" r="30" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="2"/>
        <line x1="230" y1="140" x2="270" y2="180" stroke="${t.c1}" stroke-width="1"/>
        <line x1="270" y1="140" x2="230" y2="180" stroke="${t.c1}" stroke-width="1"/>
        <text x="250" y="210" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle">${esc(trunc(cleanTitle,20))}</text>`,
        // Winter sports
        `<line x1="170" y1="200" x2="170" y2="135" stroke="${t.c1}" stroke-width="3"/>
        <circle cx="170" cy="125" r="12" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="170" y1="155" x2="140" y2="170" stroke="${t.c1}" stroke-width="2"/>
        <line x1="170" y1="155" x2="200" y2="170" stroke="${t.c1}" stroke-width="2"/>
        <line x1="155" y1="250" x2="200" y2="250" stroke="${t.c1}" stroke-width="2"/>
        <line x1="170" y1="200" x2="155" y2="250" stroke="${t.c1}" stroke-width="2"/>`
      ];
      const illIdx = lessonNum<=3 ? 0 : lessonNum<=6 ? 1 : lessonNum<=9 ? 2 : 3;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, sportsIcons[illIdx]));
    },

    informatics: () => {
      const ills = [
        // Keyboard
        `<rect x="60" y="110" width="380" height="120" rx="8" fill="#37474F" opacity="0.1" stroke="${t.c1}" stroke-width="2"/>
        <rect x="80" y="125" width="25" height="22" rx="3" fill="white" stroke="${t.c1}" stroke-width="1"/><text x="92" y="140" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Q</text>
        <rect x="110" y="125" width="25" height="22" rx="3" fill="white" stroke="${t.c1}" stroke-width="1"/><text x="122" y="140" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">W</text>
        <rect x="140" y="125" width="25" height="22" rx="3" fill="white" stroke="${t.c1}" stroke-width="1"/><text x="152" y="140" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">E</text>
        <rect x="170" y="125" width="25" height="22" rx="3" fill="white" stroke="${t.c1}" stroke-width="1"/><text x="182" y="140" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">R</text>
        <rect x="200" y="125" width="25" height="22" rx="3" fill="white" stroke="${t.c1}" stroke-width="1"/><text x="212" y="140" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">T</text>
        <rect x="230" y="125" width="25" height="22" rx="3" fill="white" stroke="${t.c1}" stroke-width="1"/><text x="242" y="140" font-family="Arial,sans-serif" font-size="8" fill="${t.c1}" text-anchor="middle">Y</text>`,
        // Paint, drawing tools
        `<rect x="100" y="105" width="200" height="140" rx="4" fill="white" stroke="${t.c1}" stroke-width="2"/>
        <rect x="100" y="105" width="200" height="20" rx="4" fill="${t.c1}" opacity="0.8"/>
        <text x="200" y="119" font-family="Arial,sans-serif" font-size="9" fill="white" text-anchor="middle">Paint</text>
        <circle cx="200" cy="175" r="25" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="320" y="120" width="40" height="8" rx="4" fill="red" opacity="0.5"/><rect x="320" y="132" width="40" height="8" rx="4" fill="blue" opacity="0.5"/>
        <rect x="320" y="144" width="40" height="8" rx="4" fill="green" opacity="0.5"/><rect x="320" y="156" width="40" height="8" rx="4" fill="yellow" opacity="0.5"/>`,
        // Internet safety, search, documents
        `<rect x="120" y="110" width="260" height="150" rx="8" fill="#E0F7FA" opacity="0.5" stroke="${t.c1}" stroke-width="2"/>
        <rect x="120" y="110" width="260" height="25" rx="8" fill="${t.c1}" opacity="0.8"/>
        <text x="250" y="127" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle">Браузер</text>
        <rect x="135" y="145" width="230" height="100" rx="4" fill="white" stroke="${t.c1}" stroke-width="1"/>
        <text x="250" y="175" font-family="Arial,sans-serif" font-size="11" fill="${t.c1}" text-anchor="middle">${esc(trunc(cleanTitle,25))}</text>
        <text x="250" y="200" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Информатика 4 класс</text>`
      ];
      const illIdx = lessonNum<=4 ? 0 : lessonNum<=8 ? 1 : 2;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    tech: () => {
      const ills = [
        // Paper, cutting, applique
        `<rect x="100" y="110" width="130" height="100" rx="4" fill="white" stroke="${t.c1}" stroke-width="2" transform="rotate(-5,165,160)"/>
        <line x1="110" y1="130" x2="220" y2="130" stroke="${t.c1}" stroke-width="0.5" opacity="0.5"/>
        <line x1="110" y1="150" x2="220" y2="150" stroke="${t.c1}" stroke-width="0.5" opacity="0.5"/>
        <polygon points="300,130 370,130 370,200 300,200" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5" stroke-dasharray="5,5"/>
        <line x1="370" y1="130" x2="300" y2="200" stroke="red" stroke-width="1" stroke-dasharray="3,3"/>`,
        // Fabric, sewing, buttons
        `<rect x="80" y="120" width="150" height="90" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="90" y1="135" x2="220" y2="135" stroke="${t.c1}" stroke-width="0.5" opacity="0.3"/>
        <line x1="90" y1="150" x2="220" y2="150" stroke="${t.c1}" stroke-width="0.5" opacity="0.3"/>
        <circle cx="320" cy="155" r="15" fill="white" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="320" cy="155" r="3" fill="${t.c1}" opacity="0.3"/>
        <line x1="305" y1="155" x2="335" y2="155" stroke="${t.c1}" stroke-width="0.5"/>
        <line x1="320" y1="140" x2="320" y2="170" stroke="${t.c1}" stroke-width="0.5"/>`,
        // 3D models, clay, plasticine
        `<polygon points="150,200 200,130 250,200" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="300" y="140" width="60" height="60" rx="30" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <circle cx="250" cy="170" r="20" fill="#8D6E63" opacity="0.3" stroke="#795548" stroke-width="1.5"/>
        <text x="200" y="230" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Бумага</text>
        <text x="330" y="230" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="middle">Пластилин</text>`,
        // Projects - gift, new year, room
        `<rect x="80" y="110" width="340" height="130" rx="8" fill="${t.c2}" opacity="0.1" stroke="${t.c1}" stroke-width="2"/>
        <polygon points="250,130 220,180 280,180" fill="${t.c2}" opacity="0.3" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="240" y="180" width="20" height="25" fill="#795548" opacity="0.3"/>
        <text x="250" y="225" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">${esc(trunc(cleanTitle,25))}</text>`
      ];
      const illIdx = lessonNum<=4 ? 0 : lessonNum<=8 ? 1 : lessonNum<=15 ? 2 : 3;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    projects: () => {
      const ills = [
        // Research, info, methods
        `<circle cx="250" cy="150" r="40" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="2"/>
        <line x1="250" y1="110" x2="250" y2="140" stroke="${t.c1}" stroke-width="2"/>
        <line x1="250" y1="110" x2="235" y2="125" stroke="${t.c1}" stroke-width="2"/>
        <line x1="250" y1="110" x2="265" y2="125" stroke="${t.c1}" stroke-width="2"/>
        <text x="250" y="210" font-family="Arial,sans-serif" font-size="10" fill="${t.c1}" text-anchor="middle">${esc(trunc(cleanTitle,25))}</text>`,
        // Model, materials, assembly
        `<rect x="100" y="110" width="300" height="130" rx="8" fill="${t.c2}" opacity="0.1" stroke="${t.c1}" stroke-width="2"/>
        <rect x="130" y="130" width="80" height="60" rx="4" fill="white" stroke="${t.c1}" stroke-width="1"/>
        <line x1="130" y1="150" x2="210" y2="150" stroke="${t.c1}" stroke-width="0.5"/>
        <line x1="130" y1="165" x2="210" y2="165" stroke="${t.c1}" stroke-width="0.5"/>
        <rect x="280" y="130" width="80" height="60" rx="4" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="320" y="165" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Схема</text>`,
        // Presentation, slides, audience
        `<rect x="100" y="105" width="300" height="140" rx="4" fill="white" stroke="${t.c1}" stroke-width="2"/>
        <rect x="100" y="105" width="300" height="25" rx="4" fill="${t.c1}" opacity="0.8"/>
        <text x="250" y="122" font-family="Arial,sans-serif" font-size="10" fill="white" text-anchor="middle">Презентация</text>
        <text x="250" y="165" font-family="Arial,sans-serif" font-size="12" fill="${t.c1}" text-anchor="middle">${esc(trunc(cleanTitle,25))}</text>
        <rect x="130" y="185" width="50" height="8" rx="2" fill="${t.c2}" opacity="0.3"/><rect x="200" y="185" width="50" height="8" rx="2" fill="${t.c2}" opacity="0.3"/><rect x="270" y="185" width="50" height="8" rx="2" fill="${t.c2}" opacity="0.3"/>`
      ];
      const illIdx = lessonNum<=4 ? 0 : lessonNum<=8 ? 1 : 2;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    religion: () => {
      const ills = [
        // What is religion, orthodoxy, islam
        `<circle cx="130" cy="160" r="50" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="130" y1="130" x2="130" y2="190" stroke="${t.c1}" stroke-width="1.5"/>
        <line x1="100" y1="160" x2="160" y2="160" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="130" y="225" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">Христианство</text>
        <circle cx="370" cy="160" r="50" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
        <path d="M345,160 L370,135 L395,160 L370,185 Z" fill="none" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="370" y="225" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">Ислам</text>`,
        // Temple, prayer, holidays
        `<polygon points="250,100 180,180 320,180" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="2"/>
        <rect x="200" y="180" width="100" height="50" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="1.5"/>
        <rect x="230" y="195" width="40" height="35" rx="20" fill="${t.c1}" opacity="0.1"/>
        <line x1="250" y1="90" x2="250" y2="100" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="250" cy="88" r="5" fill="${t.c1}" opacity="0.3"/>`,
        // Good/evil, commandments, mercy, family
        `<rect x="60" y="115" width="170" height="100" rx="6" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5"/>
        <text x="145" y="150" font-family="Arial,sans-serif" font-size="14" fill="#4CAF50" text-anchor="middle">Добро</text>
        <text x="145" y="175" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">Помощь, милосердие</text>
        <rect x="270" y="115" width="170" height="100" rx="6" fill="#FFEBEE" stroke="#C62828" stroke-width="1.5"/>
        <text x="355" y="150" font-family="Arial,sans-serif" font-size="14" fill="#C62828" text-anchor="middle">Зло</text>
        <text x="355" y="175" font-family="Arial,sans-serif" font-size="9" fill="#777" text-anchor="middle">Жестокость, обман</text>`
      ];
      const illIdx = lessonNum<=4 ? 0 : lessonNum<=8 ? 1 : 2;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },

    world: () => {
      const ills = [
        // Map of natural zones, arctic, forests, steppes
        `<rect x="60" y="100" width="380" height="20" rx="3" fill="#E3F2FD"/><text x="250" y="114" font-family="Arial,sans-serif" font-size="8" fill="#1565C0" text-anchor="middle">Арктика</text>
        <rect x="60" y="125" width="380" height="25" rx="3" fill="#C8E6C9"/><text x="250" y="142" font-family="Arial,sans-serif" font-size="8" fill="#2E7D32" text-anchor="middle">Тундра</text>
        <rect x="60" y="155" width="380" height="35" rx="3" fill="#A5D6A7"/><text x="250" y="177" font-family="Arial,sans-serif" font-size="8" fill="#1B5E20" text-anchor="middle">Леса</text>
        <rect x="60" y="195" width="380" height="25" rx="3" fill="#FFF9C4"/><text x="250" y="212" font-family="Arial,sans-serif" font-size="8" fill="#F57F17" text-anchor="middle">Степи и пустыни</text>`,
        // Ancient Slavs, Rus, baptism
        `<line x1="50" y1="160" x2="450" y2="160" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="100" cy="160" r="6" fill="${t.c1}"/><text x="100" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Славяне</text>
        <circle cx="200" cy="160" r="6" fill="${t.c1}"/><text x="200" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Русь</text>
        <circle cx="300" cy="160" r="6" fill="${t.c1}"/><text x="300" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Крещение</text>
        <circle cx="400" cy="160" r="6" fill="${t.c1}"/><text x="400" y="185" font-family="Arial,sans-serif" font-size="8" fill="#777" text-anchor="middle">Князья</text>`,
        // Human body, digestion, breathing, circulation
        `<ellipse cx="250" cy="160" rx="40" ry="70" fill="${t.c2}" opacity="0.15" stroke="${t.c1}" stroke-width="2"/>
        <circle cx="250" cy="120" r="20" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <circle cx="250" cy="155" r="15" fill="red" opacity="0.15" stroke="red" stroke-width="1"/>
        <text x="250" y="158" font-family="Arial,sans-serif" font-size="8" fill="red" text-anchor="middle">Сердце</text>
        <rect x="240" y="175" width="20" height="30" rx="3" fill="#81C784" opacity="0.2" stroke="#4CAF50"/>
        <text x="250" y="195" font-family="Arial,sans-serif" font-size="7" fill="#4CAF50" text-anchor="middle">Лёгкие</text>`,
        // Water, minerals, soil, plants/animals
        `<ellipse cx="200" cy="170" rx="60" ry="35" fill="#B3E5FC" opacity="0.3" stroke="#0277BD" stroke-width="1.5"/>
        <text x="200" y="175" font-family="Arial,sans-serif" font-size="9" fill="#0277BD" text-anchor="middle">Вода</text>
        <circle cx="370" cy="170" r="35" fill="${t.c2}" opacity="0.2" stroke="${t.c1}" stroke-width="1.5"/>
        <text x="370" y="175" font-family="Arial,sans-serif" font-size="9" fill="${t.c1}" text-anchor="middle">Почва</text>`,
        // Nature protection, Red Book, reserves
        `<rect x="60" y="110" width="380" height="120" rx="8" fill="#E8F5E9" opacity="0.5" stroke="#4CAF50" stroke-width="2"/>
        <text x="250" y="140" font-family="Arial,sans-serif" font-size="16" fill="#4CAF50" text-anchor="middle" font-weight="bold">${esc(trunc(cleanTitle,25))}</text>
        <text x="250" y="170" font-family="Arial,sans-serif" font-size="10" fill="#555" text-anchor="middle">Защита и сохранение природы</text>
        <circle cx="200" cy="200" r="10" fill="#81C784" opacity="0.3" stroke="#4CAF50"/><circle cx="300" cy="200" r="10" fill="#81C784" opacity="0.3" stroke="#4CAF50"/>`
      ];
      const illIdx = lessonNum<=4 ? 0 : lessonNum<=8 ? 1 : lessonNum<=12 ? 2 : lessonNum<=16 ? 3 : 4;
      return baseSVG(t, title, lessonNum,
        card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t, ills[illIdx]));
    },
  };

  const builder = builders[subj];
  if (builder) return builder();
  // Fallback
  return baseSVG(t, title, lessonNum,
    card(20, 88, 460, 200, cleanTitle.toUpperCase().substring(0,25), t,
      `<text x="250" y="165" font-family="Arial,sans-serif" font-size="14" fill="${t.c1}" text-anchor="middle">${esc(trunc(cleanTitle,30))}</text>`));
}

// ==================== MAIN ====================
function generateAll() {
  let total = 0;
  files.forEach(f => {
    const subj = f.replace('.json', '');
    const data = JSON.parse(fs.readFileSync(path.join(GRADE_DIR, f), 'utf8'));
    const sd = data.lessons || data;
    const dts = sd.detailedTopics || [];
    const t = themes[subj] || themes.math;
    let idx = 0;
    dts.forEach(dt => {
      if (!dt.lessons) return;
      dt.lessons.forEach(lesson => {
        idx++;
        const title = lesson.title || '';
        const img = lesson.image || '';
        const svgName = img.split('/').pop() || `lesson${idx}.svg`;
        const outPath = path.join(IMG_DIR, subj, svgName);

        let svg;
        if (subj === 'math') svg = mathIll(idx, title, t);
        else if (subj === 'russian') svg = russianIll(idx, title, t);
        else svg = genericIll(subj, idx, title, t);

        fs.writeFileSync(outPath, svg);
        total++;
      });
    });
    console.log(`${subj}: ${idx} SVGs`);
  });
  console.log(`Total: ${total}`);
}

generateAll();
