const fs = require('fs');
const path = require('path');

const GRADE_DIR = '/home/z/school-curriculum-app/public/data/grades/4';
const IMG_DIR = '/home/z/school-curriculum-app/public/images/lessons/grade4';

// Color palettes per subject
const PALETTES = {
  math: { m:'#1565C0',d:'#0D47A1',l:'#42A5F5',bg1:'#E3F2FD',bg2:'#BBDEFB',accent:'#FDD835' },
  russian: { m:'#D32F2F',d:'#B71C1C',l:'#EF5350',bg1:'#FFEBEE',bg2:'#FFCDD2',accent:'#FFCDD2' },
  literature: { m:'#283593',d:'#1A237E',l:'#5C6BC0',bg1:'#E8EAF6',bg2:'#C5CAE9',accent:'#FDD835' },
  nature: { m:'#2E7D32',d:'#1B5E20',l:'#66BB6A',bg1:'#E8F5E9',bg2:'#C8E6C9',accent:'#FDD835' },
  english: { m:'#F57C00',d:'#E65100',l:'#FFB74D',bg1:'#FFF3E0',bg2:'#FFE0B2',accent:'#1565C0' },
  history: { m:'#8D6E63',d:'#5D4037',l:'#BCAAA4',bg1:'#EFEBE9',bg2:'#D7CCC8',accent:'#D32F2F' },
  geography: { m:'#00838F',d:'#006064',l:'#26C6DA',bg1:'#E0F7FA',bg2:'#B2EBF2',accent:'#2E7D32' },
  music: { m:'#AD1457',d:'#880E4F',l:'#EC407A',bg1:'#FCE4EC',bg2:'#F8BBD0',accent:'#FDD835' },
  art: { m:'#6A1B9A',d:'#4A148C',l:'#AB47BC',bg1:'#F3E5F5',bg2:'#E1BEE7',accent:'#FDD835' },
  pe: { m:'#2E7D32',d:'#1B5E20',l:'#66BB6A',bg1:'#E8F5E9',bg2:'#C8E6C9',accent:'#FF9800' },
  tech: { m:'#4E342E',d:'#3E2723',l:'#8D6E63',bg1:'#EFEBE9',bg2:'#D7CCC8',accent:'#FDD835' },
  informatics: { m:'#00695C',d:'#004D40',l:'#26A69A',bg1:'#E0F2F1',bg2:'#B2DFDB',accent:'#1565C0' },
  religion: { m:'#FF8F00',d:'#FF6F00',l:'#FFCA28',bg1:'#FFF8E1',bg2:'#FFECB3',accent:'#D32F2F' },
  projects: { m:'#5D4037',d:'#3E2723',l:'#8D6E63',bg1:'#EFEBE9',bg2:'#D7CCC8',accent:'#2E7D32' },
  world: { m:'#1565C0',d:'#0D47A1',l:'#42A5F5',bg1:'#E3F2FD',bg2:'#BBDEFB',accent:'#2E7D32' },
};

// SVG defs template with gradients and filters
function svgDefs(p) {
  return `<defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="${p.bg1}"/>
      <stop offset="100%" stop-color="${p.bg2}"/>
    </linearGradient>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#87CEEB"/>
      <stop offset="100%" stop-color="#E0F7FA"/>
    </linearGradient>
    <linearGradient id="groundGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#81C784"/>
      <stop offset="100%" stop-color="#4CAF50"/>
    </linearGradient>
    <linearGradient id="waterGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#42A5F5"/>
      <stop offset="100%" stop-color="#1565C0"/>
    </linearGradient>
    <radialGradient id="sunGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9C4"/>
      <stop offset="60%" stop-color="#FDD835"/>
      <stop offset="100%" stop-color="#F9A825"/>
    </radialGradient>
    <filter id="shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.15"/>
    </filter>
    <filter id="softShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="3" dy="3" stdDeviation="5" flood-color="#000" flood-opacity="0.12"/>
    </filter>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>`;
}

// Common scene elements
function sky() {
  return `<rect width="500" height="220" fill="url(#skyGrad)"/>
  <circle cx="430" cy="50" r="35" fill="url(#sunGrad)" filter="url(#glow)"/>
  <path d="M80,40 Q90,25 100,40 Q110,25 120,40" fill="white" opacity="0.7"/>
  <path d="M200,55 Q212,38 224,55 Q236,38 248,55" fill="white" opacity="0.6"/>
  <path d="M340,30 Q348,20 356,30 Q364,20 372,30" fill="white" opacity="0.5"/>`;
}

function ground(y=260) {
  return `<path d="M0,${y} Q125,${y-15} 250,${y} Q375,${y+10} 500,${y} L500,350 L0,350 Z" fill="url(#groundGrad)"/>
  <path d="M0,${y+5} Q125,${y-10} 250,${y+5} Q375,${y+15} 500,${y+5}" fill="#66BB6A" opacity="0.3"/>`;
}

function waterGround(y=270) {
  return `<path d="M0,${y} Q125,${y-10} 250,${y} Q375,${y+8} 500,${y} L500,350 L0,350 Z" fill="url(#waterGrad)" opacity="0.6"/>
  <path d="M0,${y+5} Q80,${y} 160,${y+8} Q240,${y+15} 320,${y+5} Q400,${y-2} 500,${y+8}" fill="none" stroke="white" stroke-width="0.8" opacity="0.4"/>`;
}

function tree(x, y, h=50) {
  return `<rect x="${x-3}" y="${y}" width="6" height="${h*0.4}" rx="2" fill="#795548"/>
  <path d="M${x-h*0.35},${y} Q${x},${y-h*0.8} ${x+h*0.35},${y}" fill="#2E7D32" opacity="0.8"/>
  <path d="M${x-h*0.28},${y-h*0.15} Q${x},${y-h*0.9} ${x+h*0.28},${y-h*0.15}" fill="#388E3C" opacity="0.7"/>
  <path d="M${x-h*0.2},${y-h*0.3} Q${x},${y-h} ${x+h*0.2},${y-h*0.3}" fill="#43A047" opacity="0.6"/>`;
}

function bush(x, y, r=15) {
  return `<ellipse cx="${x}" cy="${y}" rx="${r}" ry="${r*0.7}" fill="#4CAF50" opacity="0.6"/>
  <ellipse cx="${x+r*0.6}" cy="${y+2}" rx="${r*0.7}" ry="${r*0.5}" fill="#388E3C" opacity="0.5"/>`;
}

function flower(x, y, color) {
  return `<line x1="${x}" y1="${y}" x2="${x}" y2="${y+15}" stroke="#4CAF50" stroke-width="1.5"/>
  <circle cx="${x}" cy="${y}" r="4" fill="${color||'#E91E63'}" opacity="0.7"/>
  <circle cx="${x}" cy="${y}" r="2" fill="#FDD835" opacity="0.8"/>`;
}

function bird(x, y) {
  return `<path d="M${x},${y} Q${x+5},${y-5} ${x+10},${y} Q${x+15},${y-5} ${x+20},${y}" fill="none" stroke="#555" stroke-width="1.2"/>`;
}

function cloud(x, y, s=1) {
  return `<g transform="translate(${x},${y}) scale(${s})">
    <ellipse cx="0" cy="0" rx="25" ry="12" fill="white" opacity="0.8"/>
    <ellipse cx="-15" cy="3" rx="18" ry="10" fill="white" opacity="0.7"/>
    <ellipse cx="15" cy="3" rx="20" ry="10" fill="white" opacity="0.7"/>
  </g>`;
}

// Title bar at bottom
function titleBar(title, p) {
  const t = title.replace(/^Урок \d+:\s*/, '').replace(/[^\u0400-\u04FF\s\w\-—.,!?()]/g, '').trim();
  const short = t.length > 40 ? t.substring(0, 37) + '...' : t;
  return `<rect x="0" y="318" width="500" height="32" rx="0" fill="${p.m}" opacity="0.9"/>
  <text x="250" y="339" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="white" font-weight="bold">${escXml(short)}</text>`;
}

function escXml(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }

// ============================================================
// SUBJECT-SPECIFIC SCENE GENERATORS
// Each returns a complete SVG body (without outer <svg> tags)
// ============================================================

const SCENES = {};

// ---- MATH ----
SCENES.math = [
  // L1: Нумерация чисел от 1 до 1000
  (p) => `${svgDefs(p)}
  ${sky()}${ground(270)}
  ${tree(50,230,45)}${tree(440,225,40)}${bush(100,260)}${bush(380,258)}
  <rect x="60" y="130" width="200" height="130" rx="8" fill="white" opacity="0.92" filter="url(#shadow)"/>
  <rect x="60" y="130" width="200" height="28" rx="8" fill="${p.m}" opacity="0.9"/>
  <rect x="60" y="150" width="200" height="8" fill="${p.m}" opacity="0.9"/>
  <text x="160" y="149" font-family="Arial" font-size="11" fill="white" text-anchor="middle" font-weight="bold">ЧИСЛА</text>
  <text x="85" y="182" font-family="Arial" font-size="28" fill="${p.d}" font-weight="bold">1</text>
  <text x="120" y="182" font-family="Arial" font-size="28" fill="${p.m}" font-weight="bold">10</text>
  <text x="165" y="182" font-family="Arial" font-size="28" fill="${p.l}" font-weight="bold">100</text>
  <text x="215" y="182" font-family="Arial" font-size="22" fill="${p.accent}" font-weight="bold">1000</text>
  <line x1="80" y1="195" x2="240" y2="195" stroke="${p.m}" stroke-width="1" opacity="0.3"/>
  <text x="160" y="215" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Единицы → Десятки → Сотни → Тысячи</text>
  <text x="160" y="232" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle">1 2 3 ... 999 1000</text>
  ${bird(300,80)}${bird(330,95)}
  <g transform="translate(290,140)">
    <rect x="0" y="0" width="160" height="115" rx="8" fill="white" opacity="0.92" filter="url(#shadow)"/>
    <rect x="0" y="0" width="160" height="28" rx="8" fill="${p.d}" opacity="0.85"/>
    <rect x="0" y="20" width="160" height="8" fill="${p.d}" opacity="0.85"/>
    <text x="80" y="19" font-family="Arial" font-size="10" fill="white" text-anchor="middle" font-weight="bold">РАЗРЯДЫ</text>
    <rect x="10" y="36" width="40" height="65" rx="4" fill="${p.m}" opacity="0.12" stroke="${p.m}" stroke-width="1"/>
    <text x="30" y="58" font-family="Arial" font-size="18" fill="${p.m}" text-anchor="middle" font-weight="bold">3</text>
    <text x="30" y="75" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Тысячи</text>
    <rect x="56" y="36" width="40" height="65" rx="4" fill="${p.l}" opacity="0.12" stroke="${p.m}" stroke-width="1"/>
    <text x="76" y="58" font-family="Arial" font-size="18" fill="${p.m}" text-anchor="middle" font-weight="bold">5</text>
    <text x="76" y="75" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Сотни</text>
    <rect x="102" y="36" width="40" height="65" rx="4" fill="${p.m}" opacity="0.12" stroke="${p.m}" stroke-width="1"/>
    <text x="122" y="58" font-family="Arial" font-size="18" fill="${p.m}" text-anchor="middle" font-weight="bold">8</text>
    <text x="122" y="75" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Десятки</text>
    <text x="80" y="100" font-family="Arial" font-size="14" fill="${p.d}" text-anchor="middle" font-weight="bold">= 3580</text>
  </g>
  ${titleBar('Нумерация чисел от 1 до 1000', p)}`,

  // L2: Класс единиц и класс тысяч
  (p) => `${svgDefs(p)}
  ${sky()}${ground(270)}
  ${tree(30,225,50)}${tree(460,230,42)}${bush(90,258)}
  <g transform="translate(40,90)" filter="url(#shadow)">
    <rect width="200" height="170" rx="10" fill="white" opacity="0.93"/>
    <rect width="200" height="30" rx="10" fill="${p.m}" opacity="0.9"/>
    <rect y="22" width="200" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="100" y="20" font-family="Arial" font-size="11" fill="white" text-anchor="middle" font-weight="bold">КЛАСС ЕДИНИЦ</text>
    <rect x="15" y="40" width="50" height="55" rx="5" fill="${p.m}" opacity="0.1" stroke="${p.m}" stroke-width="1.5"/>
    <text x="40" y="62" font-family="Arial" font-size="20" fill="${p.m}" text-anchor="middle" font-weight="bold">7</text>
    <text x="40" y="82" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Единицы</text>
    <rect x="75" y="40" width="50" height="55" rx="5" fill="${p.l}" opacity="0.1" stroke="${p.m}" stroke-width="1.5"/>
    <text x="100" y="62" font-family="Arial" font-size="20" fill="${p.m}" text-anchor="middle" font-weight="bold">5</text>
    <text x="100" y="82" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Десятки</text>
    <rect x="135" y="40" width="50" height="55" rx="5" fill="${p.m}" opacity="0.15" stroke="${p.m}" stroke-width="1.5"/>
    <text x="160" y="62" font-family="Arial" font-size="20" fill="${p.m}" text-anchor="middle" font-weight="bold">2</text>
    <text x="160" y="82" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Сотни</text>
    <line x1="20" y1="105" x2="180" y2="105" stroke="${p.m}" stroke-width="1.5" stroke-dasharray="4,3"/>
    <text x="100" y="125" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">257</text>
    <text x="100" y="145" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">II класс — класс тысяч</text>
    <text x="100" y="158" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">I класс — класс единиц</text>
  </g>
  <g transform="translate(270,95)" filter="url(#shadow)">
    <rect width="190" height="160" rx="10" fill="white" opacity="0.93"/>
    <rect width="190" height="30" rx="10" fill="${p.d}" opacity="0.9"/>
    <rect y="22" width="190" height="8" fill="${p.d}" opacity="0.9"/>
    <text x="95" y="20" font-family="Arial" font-size="11" fill="white" text-anchor="middle" font-weight="bold">КЛАСС ТЫСЯЧ</text>
    <rect x="12" y="40" width="50" height="50" rx="5" fill="${p.d}" opacity="0.1" stroke="${p.d}" stroke-width="1.5"/>
    <text x="37" y="60" font-family="Arial" font-size="18" fill="${p.d}" text-anchor="middle" font-weight="bold">1</text>
    <text x="37" y="78" font-family="Arial" font-size="6" fill="#777" text-anchor="middle">Ед.тыс.</text>
    <rect x="70" y="40" width="50" height="50" rx="5" fill="${p.m}" opacity="0.1" stroke="${p.d}" stroke-width="1.5"/>
    <text x="95" y="60" font-family="Arial" font-size="18" fill="${p.d}" text-anchor="middle" font-weight="bold">4</text>
    <text x="95" y="78" font-family="Arial" font-size="6" fill="#777" text-anchor="middle">Дес.тыс.</text>
    <rect x="128" y="40" width="50" height="50" rx="5" fill="${p.l}" opacity="0.1" stroke="${p.d}" stroke-width="1.5"/>
    <text x="153" y="60" font-family="Arial" font-size="18" fill="${p.d}" text-anchor="middle" font-weight="bold">3</text>
    <text x="153" y="78" font-family="Arial" font-size="6" fill="#777" text-anchor="middle">Сот.тыс.</text>
    <line x1="15" y1="100" x2="175" y2="100" stroke="${p.d}" stroke-width="1.5" stroke-dasharray="4,3"/>
    <text x="95" y="125" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">341 257</text>
    <text x="95" y="145" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">341 тыс. + 257 = 341 257</text>
  </g>
  ${bird(150,60)}${bird(180,50)}
  ${titleBar('Класс единиц и класс тысяч', p)}`,

  // L3: Чтение и запись многозначных чисел
  (p) => `${svgDefs(p)}
  ${sky()}${ground(270)}
  ${tree(40,228,48)}${tree(450,232,38)}
  <g transform="translate(50,80)" filter="url(#softShadow)">
    <rect width="400" height="180" rx="12" fill="white" opacity="0.94"/>
    <rect width="400" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="400" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="200" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">ЧТЕНИЕ И ЗАПИСЬ ЧИСЕЛ</text>
    <g transform="translate(20,45)">
      <rect width="360" height="50" rx="6" fill="${p.bg1}" opacity="0.5" stroke="${p.m}" stroke-width="1"/>
      <text x="180" y="22" font-family="Arial" font-size="22" fill="${p.d}" text-anchor="middle" font-weight="bold">5 032 716</text>
      <text x="180" y="42" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Пять миллионов тридцать две тысячи семьсот шестнадцать</text>
    </g>
    <g transform="translate(20,108)">
      <rect width="110" height="55" rx="5" fill="${p.m}" opacity="0.08" stroke="${p.m}" stroke-width="1"/>
      <text x="55" y="18" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle" font-weight="bold">Миллионы</text>
      <text x="55" y="38" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">5</text>
    </g>
    <g transform="translate(140,108)">
      <rect width="110" height="55" rx="5" fill="${p.l}" opacity="0.08" stroke="${p.m}" stroke-width="1"/>
      <text x="55" y="18" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle" font-weight="bold">Тысячи</text>
      <text x="55" y="38" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">032</text>
    </g>
    <g transform="translate(260,108)">
      <rect width="110" height="55" rx="5" fill="${p.m}" opacity="0.12" stroke="${p.m}" stroke-width="1"/>
      <text x="55" y="18" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle" font-weight="bold">Единицы</text>
      <text x="55" y="38" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">716</text>
    </g>
  </g>
  ${bird(200,55)}${flower(150,260,'#E91E63')}${flower(350,258,'#FF9800')}
  ${titleBar('Чтение и запись многозначных чисел', p)}`,

  // L4: Увеличение и уменьшение чисел
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(50,40)" filter="url(#softShadow)">
    <rect width="400" height="270" rx="12" fill="white" opacity="0.94"/>
    <rect width="400" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="400" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="200" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">УВЕЛИЧЕНИЕ И УМЕНЬШЕНИЕ</text>
    <g transform="translate(20,50)">
      <rect x="0" y="0" width="165" height="100" rx="8" fill="${p.bg1}" opacity="0.5" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="82" y="22" font-family="Arial" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Увеличить на</text>
      <text x="82" y="50" font-family="Arial" font-size="22" fill="#2E7D32" text-anchor="middle" font-weight="bold">+ 10</text>
      <text x="82" y="72" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">150 → 160</text>
      <text x="82" y="90" font-family="Arial" font-size="9" fill="#2E7D32" text-anchor="middle">Число становится больше</text>
    </g>
    <g transform="translate(210,50)">
      <rect x="0" y="0" width="165" height="100" rx="8" fill="#FFEBEE" opacity="0.5" stroke="#D32F2F" stroke-width="1.5"/>
      <text x="82" y="22" font-family="Arial" font-size="10" fill="#D32F2F" text-anchor="middle" font-weight="bold">Уменьшить на</text>
      <text x="82" y="50" font-family="Arial" font-size="22" fill="#D32F2F" text-anchor="middle" font-weight="bold">− 10</text>
      <text x="82" y="72" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">150 → 140</text>
      <text x="82" y="90" font-family="Arial" font-size="9" fill="#D32F2F" text-anchor="middle">Число становится меньше</text>
    </g>
    <g transform="translate(20,165)">
      <rect x="0" y="0" width="165" height="85" rx="8" fill="#E8F5E9" opacity="0.5" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="82" y="20" font-family="Arial" font-size="10" fill="#2E7D32" text-anchor="middle" font-weight="bold">Увеличить в</text>
      <text x="82" y="48" font-family="Arial" font-size="22" fill="#2E7D32" text-anchor="middle" font-weight="bold">× 3</text>
      <text x="82" y="68" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">50 → 150</text>
    </g>
    <g transform="translate(210,165)">
      <rect x="0" y="0" width="165" height="85" rx="8" fill="#FFEBEE" opacity="0.5" stroke="#D32F2F" stroke-width="1.5"/>
      <text x="82" y="20" font-family="Arial" font-size="10" fill="#D32F2F" text-anchor="middle" font-weight="bold">Уменьшить в</text>
      <text x="82" y="48" font-family="Arial" font-size="22" fill="#D32F2F" text-anchor="middle" font-weight="bold">÷ 3</text>
      <text x="82" y="68" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">150 → 50</text>
    </g>
  </g>
  ${titleBar('Увеличение и уменьшение чисел', p)}`,

  // L5: Сложение многозначных чисел
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">СЛОЖЕНИЕ МНОГОЗНАЧНЫХ ЧИСЕЛ</text>
    <g transform="translate(30,50)">
      <rect width="360" height="130" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="200" y="25" font-family="monospace" font-size="18" fill="${p.d}" text-anchor="end" font-weight="bold">  24 568</text>
      <text x="200" y="50" font-family="monospace" font-size="18" fill="${p.d}" text-anchor="end" font-weight="bold">+ 13 724</text>
      <line x1="80" y1="58" x2="210" y2="58" stroke="${p.m}" stroke-width="2.5"/>
      <text x="200" y="82" font-family="monospace" font-size="18" fill="${p.accent}" text-anchor="end" font-weight="bold">  38 292</text>
      <text x="290" y="25" font-family="Arial" font-size="8" fill="#777">Разряд единиц: 8+4=12</text>
      <text x="290" y="45" font-family="Arial" font-size="8" fill="#777">Перенос: 1 дес.</text>
      <text x="290" y="65" font-family="Arial" font-size="8" fill="#777">6+2+1=9 дес.</text>
      <text x="290" y="85" font-family="Arial" font-size="8" fill="#777">5+7=12 → перенос</text>
      <text x="290" y="105" font-family="Arial" font-size="8" fill="#777">4+3+1=8 сот.</text>
      <text x="290" y="125" font-family="Arial" font-size="8" fill="#777">2+1=3 тыс.</text>
    </g>
    <g transform="translate(30,195)">
      <rect width="160" height="70" rx="6" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1"/>
      <text x="80" y="20" font-family="Arial" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">ПРАВИЛО</text>
      <text x="80" y="38" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Складываем поразрядно,</text>
      <text x="80" y="52" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">начиная с единиц</text>
    </g>
    <g transform="translate(210,195)">
      <rect width="170" height="70" rx="6" fill="#FFF3E0" stroke="#FF9800" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">ЗАПОМНИ</text>
      <text x="85" y="38" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Если сумма &gt; 9, то</text>
      <text x="85" y="52" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">переносим 1 в след. разряд</text>
    </g>
  </g>
  ${titleBar('Сложение многозначных чисел', p)}`,

  // L6: Вычитание многозначных чисел
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">ВЫЧИТАНИЕ МНОГОЗНАЧНЫХ ЧИСЕЛ</text>
    <g transform="translate(30,50)">
      <rect width="360" height="130" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="200" y="25" font-family="monospace" font-size="18" fill="${p.d}" text-anchor="end" font-weight="bold">  45 302</text>
      <text x="200" y="50" font-family="monospace" font-size="18" fill="${p.d}" text-anchor="end" font-weight="bold">− 18 657</text>
      <line x1="80" y1="58" x2="210" y2="58" stroke="${p.m}" stroke-width="2.5"/>
      <text x="200" y="82" font-family="monospace" font-size="18" fill="${p.accent}" text-anchor="end" font-weight="bold">  26 645</text>
      <text x="290" y="25" font-family="Arial" font-size="8" fill="#777">2−7: занимаем 1 дес.</text>
      <text x="290" y="45" font-family="Arial" font-size="8" fill="#777">12−7=5 единиц</text>
      <text x="290" y="65" font-family="Arial" font-size="8" fill="#777">9−5=4 десятка</text>
      <text x="290" y="85" font-family="Arial" font-size="8" fill="#777">2−6: занимаем 1 тыс.</text>
      <text x="290" y="105" font-family="Arial" font-size="8" fill="#777">12−6=6 сотен</text>
      <text x="290" y="125" font-family="Arial" font-size="8" fill="#777">4−1−1=2 тыс.</text>
    </g>
    <g transform="translate(30,195)">
      <rect width="160" height="70" rx="6" fill="#FFEBEE" stroke="#D32F2F" stroke-width="1"/>
      <text x="80" y="20" font-family="Arial" font-size="9" fill="#D32F2F" text-anchor="middle" font-weight="bold">ЗАЁМ</text>
      <text x="80" y="38" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Если не хватает,</text>
      <text x="80" y="52" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">занимаем из старшего</text>
    </g>
    <g transform="translate(210,195)">
      <rect width="170" height="70" rx="6" fill="#E3F2FD" stroke="${p.m}" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle" font-weight="bold">ПРОВЕРКА</text>
      <text x="85" y="38" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">26 645 + 18 657</text>
      <text x="85" y="52" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">= 45 302 ✓</text>
    </g>
  </g>
  ${titleBar('Вычитание многозначных чисел', p)}`,

  // L7: Умножение на однозначное число
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,25)" filter="url(#softShadow)">
    <rect width="420" height="290" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">УМНОЖЕНИЕ НА ОДНОЗНАЧНОЕ ЧИСЛО</text>
    <g transform="translate(30,45)">
      <rect width="220" height="175" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="150" y="25" font-family="monospace" font-size="16" fill="${p.d}" text-anchor="end" font-weight="bold">  2 347</text>
      <text x="150" y="48" font-family="monospace" font-size="16" fill="${p.d}" text-anchor="end" font-weight="bold">      × 5</text>
      <line x1="50" y1="55" x2="160" y2="55" stroke="${p.m}" stroke-width="2.5"/>
      <text x="150" y="78" font-family="monospace" font-size="16" fill="${p.accent}" text-anchor="end" font-weight="bold">  11 735</text>
      <text x="110" y="110" font-family="Arial" font-size="8" fill="#777" text-anchor="middle">7×5=35, пишем 5, переносим 3</text>
      <text x="110" y="125" font-family="Arial" font-size="8" fill="#777" text-anchor="middle">4×5+3=23, пишем 3, переносим 2</text>
      <text x="110" y="140" font-family="Arial" font-size="8" fill="#777" text-anchor="middle">3×5+2=17, пишем 7, переносим 1</text>
      <text x="110" y="155" font-family="Arial" font-size="8" fill="#777" text-anchor="middle">2×5+1=11</text>
    </g>
    <g transform="translate(270,45)">
      <rect width="120" height="175" rx="8" fill="#FFF3E0" opacity="0.4" stroke="#FF9800" stroke-width="1"/>
      <text x="60" y="20" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">АЛГОРИТМ</text>
      <circle cx="20" cy="45" r="10" fill="#FF9800" opacity="0.3"/><text x="20" y="49" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">1</text>
      <text x="70" y="49" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Умнож един.</text>
      <circle cx="20" cy="75" r="10" fill="#FF9800" opacity="0.3"/><text x="20" y="79" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">2</text>
      <text x="70" y="79" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Умнож десятки</text>
      <circle cx="20" cy="105" r="10" fill="#FF9800" opacity="0.3"/><text x="20" y="109" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">3</text>
      <text x="70" y="109" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Умнож сотни</text>
      <circle cx="20" cy="135" r="10" fill="#FF9800" opacity="0.3"/><text x="20" y="139" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">4</text>
      <text x="70" y="139" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Умнож тысячи</text>
      <circle cx="20" cy="165" r="10" fill="#FF9800" opacity="0.3"/><text x="20" y="169" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">5</text>
      <text x="70" y="169" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">+ перенос</text>
    </g>
  </g>
  ${titleBar('Умножение на однозначное число', p)}`,

  // L8: Деление на однозначное число
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,25)" filter="url(#softShadow)">
    <rect width="420" height="290" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">ДЕЛЕНИЕ НА ОДНОЗНАЧНОЕ ЧИСЛО</text>
    <g transform="translate(40,50)">
      <rect width="340" height="160" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="60" y="25" font-family="monospace" font-size="18" fill="${p.d}" font-weight="bold">7 5 6</text>
      <line x1="0" y1="5" x2="0" y2="30" stroke="${p.m}" stroke-width="2.5"/>
      <line x1="0" y1="5" x2="90" y2="5" stroke="${p.m}" stroke-width="2.5"/>
      <text x="40" y="0" font-family="monospace" font-size="14" fill="${p.accent}" font-weight="bold">3</text>
      <text x="160" y="25" font-family="monospace" font-size="18" fill="${p.m}" font-weight="bold">2 5 2</text>
      <text x="60" y="50" font-family="monospace" font-size="13" fill="#777">7:3=2 (ост.1)</text>
      <text x="60" y="70" font-family="monospace" font-size="13" fill="#777">15:3=5</text>
      <text x="60" y="90" font-family="monospace" font-size="13" fill="#777">6:3=2</text>
      <text x="160" y="50" font-family="Arial" font-size="10" fill="${p.d}" font-weight="bold">← частное</text>
      <text x="160" y="120" font-family="Arial" font-size="11" fill="${p.m}" text-anchor="start" font-weight="bold">756 : 3 = 252</text>
      <text x="160" y="140" font-family="Arial" font-size="9" fill="#555" text-anchor="start">Проверка: 252 × 3 = 756 ✓</text>
    </g>
  </g>
  ${titleBar('Деление на однозначное число', p)}`,

  // L9: Умножение на числа с нулями
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">УМНОЖЕНИЕ НА ЧИСЛА С НУЛЯМИ</text>
    <g transform="translate(30,50)">
      <rect width="170" height="140" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle" font-weight="bold">× 10, × 100, × 1000</text>
      <text x="85" y="48" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">45 × 10 = 450</text>
      <text x="85" y="68" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">45 × 100 = 4500</text>
      <text x="85" y="88" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">45 × 1000 = 45000</text>
      <text x="85" y="115" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Приписываем столько</text>
      <text x="85" y="128" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">нулей, сколько в множителе</text>
    </g>
    <g transform="translate(220,50)">
      <rect width="170" height="140" rx="8" fill="#FFF3E0" opacity="0.4" stroke="#FF9800" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">× 20, × 300</text>
      <text x="85" y="48" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">34 × 20 = 680</text>
      <text x="85" y="68" font-family="Arial" font-size="10" fill="#777" text-anchor="middle">= 34 × 2 × 10</text>
      <text x="85" y="95" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">12 × 300 = 3600</text>
      <text x="85" y="115" font-family="Arial" font-size="10" fill="#777" text-anchor="middle">= 12 × 3 × 100</text>
      <text x="85" y="135" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Умножаем на число без нулей,</text>
    </g>
  </g>
  ${titleBar('Умножение на числа с нулями', p)}`,

  // L10: Деление на числа с нулями
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="13" fill="white" text-anchor="middle" font-weight="bold">ДЕЛЕНИЕ НА ЧИСЛА С НУЛЯМИ</text>
    <g transform="translate(30,50)">
      <rect width="170" height="140" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle" font-weight="bold">÷ 10, ÷ 100, ÷ 1000</text>
      <text x="85" y="48" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">450 : 10 = 45</text>
      <text x="85" y="68" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">4500 : 100 = 45</text>
      <text x="85" y="88" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">45000 : 1000 = 45</text>
      <text x="85" y="115" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Отбрасываем столько</text>
      <text x="85" y="128" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">нулей, сколько в делителе</text>
    </g>
    <g transform="translate(220,50)">
      <rect width="170" height="140" rx="8" fill="#FFF3E0" opacity="0.4" stroke="#FF9800" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">÷ 20, ÷ 300</text>
      <text x="85" y="48" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">680 : 20 = 34</text>
      <text x="85" y="68" font-family="Arial" font-size="10" fill="#777" text-anchor="middle">= 680 : 10 : 2</text>
      <text x="85" y="95" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">3600 : 300 = 12</text>
      <text x="85" y="115" font-family="Arial" font-size="10" fill="#777" text-anchor="middle">= 3600 : 100 : 3</text>
    </g>
  </g>
  ${titleBar('Деление на числа с нулями', p)}`,

  // L11: Доли и дроби
  (p) => `${svgDefs(p)}
  ${sky()}${ground(275)}
  ${tree(30,228,50)}${tree(460,230,38)}
  <g transform="translate(40,55)" filter="url(#softShadow)">
    <rect width="190" height="210" rx="10" fill="white" opacity="0.94"/>
    <rect width="190" height="28" rx="10" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="190" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="95" y="19" font-family="Arial" font-size="11" fill="white" text-anchor="middle" font-weight="bold">ДОЛИ</text>
    <circle cx="95" cy="80" r="40" fill="${p.bg1}" stroke="${p.m}" stroke-width="2"/>
    <path d="M95,40 A40,40 0 0,1 135,80 L95,80 Z" fill="${p.m}" opacity="0.35"/>
    <text x="95" y="85" font-family="Arial" font-size="14" fill="${p.d}" text-anchor="middle" font-weight="bold">1/2</text>
    <text x="95" y="140" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Половина — 1 доля из 2</text>
    <circle cx="95" cy="195" r="25" fill="${p.bg1}" stroke="${p.m}" stroke-width="1.5"/>
    <path d="M95,170 A25,25 0 0,1 120,195 L95,195 Z" fill="${p.m}" opacity="0.35"/>
    <path d="M95,170 A25,25 0 0,0 70,195 L95,195 Z" fill="${p.l}" opacity="0.25"/>
    <text x="95" y="200" font-family="Arial" font-size="11" fill="${p.d}" text-anchor="middle" font-weight="bold">1/2</text>
  </g>
  <g transform="translate(260,55)" filter="url(#softShadow)">
    <rect width="200" height="210" rx="10" fill="white" opacity="0.94"/>
    <rect width="200" height="28" rx="10" fill="${p.d}" opacity="0.9"/>
    <rect y="20" width="200" height="8" fill="${p.d}" opacity="0.9"/>
    <text x="100" y="19" font-family="Arial" font-size="11" fill="white" text-anchor="middle" font-weight="bold">ДРОБИ</text>
    <circle cx="100" cy="80" r="40" fill="${p.bg1}" stroke="${p.d}" stroke-width="2"/>
    <path d="M100,40 A40,40 0 0,1 140,80 L100,80 Z" fill="${p.d}" opacity="0.35"/>
    <text x="100" y="85" font-family="Arial" font-size="14" fill="${p.d}" text-anchor="middle" font-weight="bold">1/4</text>
    <text x="100" y="140" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Числитель / Знаменатель</text>
    <text x="100" y="158" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle">1 — сколько долей взяли</text>
    <text x="100" y="175" font-family="Arial" font-size="9" fill="${p.d}" text-anchor="middle">4 — на сколько разделили</text>
    <circle cx="100" cy="218" r="15" fill="${p.bg1}" stroke="${p.d}" stroke-width="1"/>
  </g>
  ${flower(220,268,'#E91E63')}${flower(240,272,'#FF9800')}
  ${titleBar('Доли и дроби', p)}`,

  // L12-L28: Generic math scene with formulas
  (p, title, num) => {
    const topics = {
      12: { label:'СРАВНЕНИЕ ДРОБЕЙ', formula:'1/3 < 1/2', detail:'Из двух дробей с одинаковым знаменателем меньше та, у которой меньше числитель', color1:'#E8F5E9', border:'#4CAF50' },
      13: { label:'СЛОЖЕНИЕ ДРОБЕЙ', formula:'1/4 + 2/4 = 3/4', detail:'Складываем числители, знаменатель оставляем тот же', color1:'#E3F2FD', border:p.m },
      14: { label:'ВЫЧИТАНИЕ ДРОБЕЙ', formula:'3/5 − 1/5 = 2/5', detail:'Вычитаем числители, знаменатель оставляем тот же', color1:'#FFEBEE', border:'#D32F2F' },
      15: { label:'ЧАСТЬ ЧИСЛА', formula:'1/4 от 20 = 5', detail:'Чтобы найти часть, делим число на знаменатель и умножаем на числитель', color1:'#FFF3E0', border:'#FF9800' },
      16: { label:'ЧИСЛО ПО ЧАСТИ', formula:'5 это 1/4 → 20', detail:'Чтобы найти число, делим часть на числитель и умножаем на знаменатель', color1:'#E0F2F1', border:'#00897B' },
      17: { label:'ГЕОМЕТРИЧЕСКИЕ ФИГУРЫ', formula:'△ ○ □ ◇', detail:'Треугольник, круг, прямоугольник, ромб — основные геометрические фигуры', color1:'#F3E5F5', border:'#7B1FA2' },
      18: { label:'ПЛОЩАДЬ', formula:'S = a × b', detail:'Площадь прямоугольника равна произведению его длины и ширины', color1:'#E8F5E9', border:'#2E7D32' },
      19: { label:'ЕДИНИЦЫ ПЛОЩАДИ', formula:'1 м² = 100 дм²', detail:'мм² → см² → дм² → м² → км² — единицы измерения площади', color1:'#E3F2FD', border:p.m },
      20: { label:'ГЕОМЕТРИЧЕСКИЕ ТЕЛА', formula:'□ ○ △ 3D', detail:'Куб, шар, пирамида, цилиндр — объёмные геометрические тела', color1:'#FFF3E0', border:'#FF9800' },
      21: { label:'ЕДИНИЦЫ ДЛИНЫ', formula:'1 км = 1000 м', detail:'мм → см → дм → м → км', color1:'#E0F7FA', border:'#00838F' },
      22: { label:'ЕДИНИЦЫ МАССЫ', formula:'1 т = 1000 кг', detail:'г → кг → ц → т', color1:'#EFEBE9', border:'#795548' },
      23: { label:'ЕДИНИЦЫ ВРЕМЕНИ', formula:'1 ч = 60 мин', detail:'с → мин → ч → сут → нед → мес → год → век', color1:'#FCE4EC', border:'#AD1457' },
      24: { label:'ДЕЙСТВИЯ С ВЕЛИЧИНАМИ', formula:'2 м 30 см + 1 м 70 см', detail:'Величины складывают и вычитают поразрядно', color1:'#E8EAF6', border:'#283593' },
      25: { label:'ЗАДАЧИ НА ДВИЖЕНИЕ', formula:'S = v × t', detail:'Расстояние = скорость × время', color1:'#E3F2FD', border:p.m },
      26: { label:'ПРОТИВОПОЛОЖНОЕ ДВИЖЕНИЕ', formula:'v = v₁ + v₂', detail:'При противоположном движении скорости складываются', color1:'#FFEBEE', border:'#D32F2F' },
      27: { label:'ЗАДАЧИ НА РАБОТУ', formula:'A = v × t', detail:'Работа = производительность × время', color1:'#FFF3E0', border:'#FF9800' },
      28: { label:'ЦЕНА, КОЛИЧЕСТВО, СТОИМОСТЬ', formula:'C = Ц × К', detail:'Стоимость = цена × количество', color1:'#E8F5E9', border:'#2E7D32' },
    };
    const t = topics[num] || { label:escXml(title), formula:'Математика', detail:'', color1:p.bg1, border:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(30,50)">
      <rect width="360" height="90" rx="8" fill="${t.color1}" opacity="0.4" stroke="${t.border}" stroke-width="1.5"/>
      <text x="180" y="40" font-family="Arial" font-size="28" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.formula}</text>
      <text x="180" y="70" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">${t.detail}</text>
    </g>
    <g transform="translate(30,160)">
      <rect width="170" height="100" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle" font-weight="bold">ПРИМЕР</text>
      <text x="85" y="50" font-family="Arial" font-size="11" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.formula}</text>
      <text x="85" y="75" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">${t.detail.substring(0,35)}</text>
    </g>
    <g transform="translate(220,160)">
      <rect width="170" height="100" rx="8" fill="#FFF3E0" opacity="0.4" stroke="#FF9800" stroke-width="1"/>
      <text x="85" y="20" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">ЗАПОМНИ</text>
      <text x="85" y="50" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Решай по шагам!</text>
      <text x="85" y="70" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">1. Прочитай условие</text>
      <text x="85" y="83" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">2. Запиши формулу</text>
      <text x="85" y="96" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">3. Подставь значения</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];


// ---- RUSSIAN ----
SCENES.russian = [
  // L1: Что такое предложение
  (p) => `${svgDefs(p)}
  ${sky()}${ground(270)}
  ${tree(40,228,48)}${tree(455,232,38)}${bush(90,258)}
  <g transform="translate(40,50)" filter="url(#softShadow)">
    <rect width="420" height="210" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">ПРЕДЛОЖЕНИЕ</text>
    <g transform="translate(15,40)">
      <rect width="390" height="38" rx="6" fill="#FFEBEE" opacity="0.4" stroke="${p.m}" stroke-width="1"/>
      <text x="195" y="25" font-family="Arial" font-size="14" fill="${p.d}" text-anchor="middle" font-weight="bold">Мальчик читает интересную книгу.</text>
    </g>
    <g transform="translate(15,90)">
      <rect width="120" height="55" rx="6" fill="${p.m}" opacity="0.1" stroke="${p.m}" stroke-width="1.5"/>
      <text x="60" y="22" font-family="Arial" font-size="10" fill="${p.m}" text-anchor="middle" font-weight="bold">Подлежащее</text>
      <text x="60" y="40" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Мальчик (кто?)</text>
      <rect x="5" y="48" width="110" height="4" rx="2" fill="${p.m}" opacity="0.3"/>
    </g>
    <g transform="translate(150,90)">
      <rect width="120" height="55" rx="6" fill="${p.l}" opacity="0.12" stroke="${p.m}" stroke-width="1.5"/>
      <text x="60" y="22" font-family="Arial" font-size="10" fill="${p.m}" text-anchor="middle" font-weight="bold">Сказуемое</text>
      <text x="60" y="40" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">читает (что делает?)</text>
      <rect x="5" y="48" width="110" height="4" rx="2" fill="${p.m}" opacity="0.3"/>
    </g>
    <g transform="translate(285,90)">
      <rect width="120" height="55" rx="6" fill="#FFF3E0" opacity="0.5" stroke="#FF9800" stroke-width="1"/>
      <text x="60" y="22" font-family="Arial" font-size="10" fill="#E65100" text-anchor="middle" font-weight="bold">Второстепенные</text>
      <text x="60" y="40" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">интересную книгу</text>
    </g>
    <text x="210" y="170" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Предложение выражает законченную мысль</text>
    <text x="210" y="188" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle">Начинается с большой буквы, заканчивается . ! ?</text>
  </g>
  ${bird(200,45)}${bird(230,35)}
  ${titleBar('Что такое предложение', p)}`,

  // L2: Главные члены предложения
  (p) => `${svgDefs(p)}
  ${sky()}${ground(270)}
  <g transform="translate(40,40)" filter="url(#softShadow)">
    <rect width="420" height="220" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">ГЛАВНЫЕ ЧЛЕНЫ ПРЕДЛОЖЕНИЯ</text>
    <g transform="translate(15,40)">
      <rect width="390" height="35" rx="6" fill="#FFEBEE" opacity="0.4" stroke="${p.m}" stroke-width="1"/>
      <text x="195" y="23" font-family="Arial" font-size="13" fill="${p.d}" text-anchor="middle" font-weight="bold">Солнце освещает поле.</text>
    </g>
    <g transform="translate(20,90)">
      <rect width="180" height="110" rx="8" fill="${p.m}" opacity="0.08" stroke="${p.m}" stroke-width="2"/>
      <text x="90" y="22" font-family="Arial" font-size="11" fill="${p.m}" text-anchor="middle" font-weight="bold">ПОДЛЕЖАЩЕЕ</text>
      <line x1="20" y1="30" x2="160" y2="30" stroke="${p.m}" stroke-width="1" stroke-dasharray="3,2"/>
      <text x="90" y="50" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">Солнце</text>
      <text x="90" y="70" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Кто? Что?</text>
      <text x="90" y="90" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">Предмет, о котором</text>
      <text x="90" y="102" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">говорится в предложении</text>
    </g>
    <g transform="translate(220,90)">
      <rect width="180" height="110" rx="8" fill="${p.l}" opacity="0.08" stroke="${p.m}" stroke-width="2"/>
      <text x="90" y="22" font-family="Arial" font-size="11" fill="${p.m}" text-anchor="middle" font-weight="bold">СКАЗУЕМОЕ</text>
      <line x1="20" y1="30" x2="160" y2="30" stroke="${p.m}" stroke-width="1" stroke-dasharray="3,2"/>
      <text x="90" y="50" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">освещает</text>
      <text x="90" y="70" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Что делает?</text>
      <text x="90" y="90" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">Что говорится о</text>
      <text x="90" y="102" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">подлежащем</text>
    </g>
  </g>
  ${titleBar('Главные члены предложения', p)}`,

  // L3-L13: Generic Russian scenes
  (p, title, num) => {
    const topics = {
      3: { label:'ВТОРОСТЕПЕННЫЕ ЧЛЕНЫ', info:'Дополнение, определение, обстоятельство', example:'Вчера (когда?) мальчик (кто?) читал (что делал?) книгу (что?)', accent:'#FF9800' },
      4: { label:'КОРЕНЬ СЛОВА', info:'Общая часть родственных слов', example:'лес — лесок — лесной — лесник', accent:'#2E7D32' },
      5: { label:'ПРИСТАВКА И СУФФИКС', info:'Приставка перед корнем, суффикс после корня', example:'пере-ход-и-ть', accent:'#1565C0' },
      6: { label:'ОКОНЧАНИЕ СЛОВА', info:'Изменяемая часть слова для связи слов', example:'дом, дома, дому, домом', accent:'#AD1457' },
      7: { label:'ИМЯ СУЩЕСТВИТЕЛЬНОЕ', info:'Обозначает предмет: кто? что?', example:'стол, кот, Москва, радость', accent:'#6A1B9A' },
      8: { label:'ИМЯ ПРИЛАГАТЕЛЬНОЕ', info:'Обозначает признак: какой? какая?', example:'красивый, умная, быстрое', accent:'#E65100' },
      9: { label:'ГЛАГОЛ', info:'Обозначает действие: что делать?', example:'бежать, читать, писать', accent:'#2E7D32' },
      10: { label:'МЕСТОИМЕНИЕ', info:'Указывает на предмет, не называя его', example:'я, ты, он, она, мы, вы, они', accent:'#1565C0' },
      11: { label:'БЕЗУДАРНЫЕ ГЛАСНЫЕ', info:'Проверяй ударением: в_да — в_ды', example:'трава — травы, вода — воды', accent:'#D32F2F' },
      12: { label:'ПАРНЫЕ СОГЛАСНЫЕ', info:'Проверяй перед гласной или н', example:'дуб — дубы, мороз — морозы', accent:'#00838F' },
      13: { label:'РАЗДЕЛИТЕЛЬНЫЕ Ь И Ъ', info:'Ь — перед е, ё, ю, я, и; Ъ — после приставок на согласную', example:'вьётся, подъезд', accent:'#5D4037' },
    };
    const t = topics[num] || { label:escXml(title), info:'Русский язык', example:'', accent:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="75" rx="8" fill="#FFEBEE" opacity="0.3" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="30" font-family="Arial" font-size="13" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.info}</text>
      <text x="190" y="55" font-family="Arial" font-size="11" fill="#555" text-anchor="middle">${t.example}</text>
    </g>
    <g transform="translate(20,140)">
      <rect width="380" height="130" rx="8" fill="white" stroke="${t.accent}" stroke-width="1.5"/>
      <rect width="380" height="24" rx="8" fill="${t.accent}" opacity="0.85"/>
      <rect y="18" width="380" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="190" y="17" font-family="Arial" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ЗАПОМНИ ПРАВИЛО</text>
      <text x="190" y="55" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">${t.info}</text>
      <text x="190" y="80" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.example}</text>
      <text x="190" y="108" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle">Проверяй правило на каждом слове!</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];

// ---- LITERATURE ----
SCENES.literature = [
  // L1: Русские народные сказки
  (p) => `${svgDefs(p)}
  ${sky()}${ground(265)}
  ${tree(30,215,55)}${tree(460,220,45)}${bush(85,248)}${bush(400,250)}
  <g transform="translate(60,40)" filter="url(#softShadow)">
    <rect width="380" height="220" rx="12" fill="white" opacity="0.94"/>
    <rect width="380" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="380" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="190" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">РУССКИЕ НАРОДНЫЕ СКАЗКИ</text>
    <g transform="translate(15,40)">
      <path d="M20,35 L100,25 L100,160 L20,170 Z" fill="#FFFDE7" stroke="${p.m}" stroke-width="1.5" rx="2"/>
      <path d="M100,25 L180,35 L180,170 L100,160 Z" fill="#FFF9C4" stroke="${p.m}" stroke-width="1.5" rx="2"/>
      <line x1="30" y1="50" x2="90" y2="47" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <line x1="30" y1="62" x2="90" y2="59" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <line x1="30" y1="74" x2="90" y2="71" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <line x1="30" y1="86" x2="90" y2="83" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <line x1="110" y1="50" x2="170" y2="53" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <line x1="110" y1="62" x2="170" y2="65" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <line x1="110" y1="74" x2="170" y2="77" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <line x1="110" y1="86" x2="170" y2="89" stroke="${p.m}" stroke-width="0.5" opacity="0.3"/>
      <text x="100" y="110" font-family="Arial" font-size="10" fill="${p.d}" text-anchor="middle" font-weight="bold">Сказки</text>
    </g>
    <g transform="translate(210,38)">
      <rect width="155" height="45" rx="6" fill="#FFF3E0" stroke="#FF9800" stroke-width="1"/>
      <text x="77" y="18" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">Волшебные</text>
      <text x="77" y="35" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Кощей, Баба-Яга, Змей</text>
    </g>
    <g transform="translate(210,92)">
      <rect width="155" height="45" rx="6" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1"/>
      <text x="77" y="18" font-family="Arial" font-size="9" fill="#2E7D32" text-anchor="middle" font-weight="bold">Бытовые</text>
      <text x="77" y="35" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Мужик и медведь</text>
    </g>
    <g transform="translate(210,146)">
      <rect width="155" height="45" rx="6" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
      <text x="77" y="18" font-family="Arial" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">О животных</text>
      <text x="77" y="35" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">Лиса и заяц, Волк и коза</text>
    </g>
  </g>
  ${bird(300,50)}${bird(330,40)}
  ${titleBar('Русские народные сказки', p)}`,

  // L2-L12: Literature generic
  (p, title, num) => {
    const topics = {
      2: { label:'ВОЛШЕБНЫЕ СКАЗКИ', desc:'Чудесные превращения и волшебные предметы', items:'Ковёр-самолёт, шапка-невидимка, волшебная палочка', accent:'#6A1B9A' },
      3: { label:'БЫТОВЫЕ СКАЗКИ', desc:'Рассказывают о повседневной жизни', items:'Мужик и медведь, Лиса и журавль', accent:'#795548' },
      4: { label:'СКАЗКИ О ЖИВОТНЫХ', desc:'Животные наделены человеческими качествами', items:'Лиса — хитрость, Волк — глупость, Заяц — трусость', accent:'#2E7D32' },
      5: { label:'ИЛЬЯ МУРОМЕЦ', desc:'Главный русский богатырь', items:'Сидел 33 года, получил силу от калик перехожих', accent:'#D32F2F' },
      6: { label:'ДОБРЫНЯ НИКИТИЧ', desc:'Богатырь — дипломат и герой', items:'Бился со Змеем, служил князю Владимиру', accent:'#1565C0' },
      7: { label:'АЛЁША ПОПОВИЧ', desc:'Младший из трёх богатырей', items:'Хитростью и смекалкой побеждал врагов', accent:'#FF8F00' },
      8: { label:'А.С. ПУШКИН', desc:'Великий русский поэт', items:'Сказки, стихи, поэмы, романы', accent:'#283593' },
      9: { label:'Л.Н. ТОЛСТОЙ', desc:'Великий русский писатель', items:'Рассказы для детей, басни, повести', accent:'#5D4037' },
      10: { label:'К.И. ЧУКОВСКИЙ', desc:'Детский писатель и поэт', items:'Мойдодыр, Айболит, Бармалей', accent:'#2E7D32' },
      11: { label:'С.Я. МАРШАК', desc:'Поэт, переводчик, драматург', items:'Двенадцать месяцев, Усатый-полосатый', accent:'#00838F' },
      12: { label:'ИТОГОВЫЙ УРОК', desc:'Повторяем всё изученное', items:'Сказки, былины, стихи, рассказы', accent:p.m },
    };
    const t = topics[num] || { label:escXml(title), desc:'Литература', items:'', accent:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="60" rx="8" fill="#E8EAF6" opacity="0.3" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="25" font-family="Arial" font-size="13" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
      <text x="190" y="48" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">${t.items}</text>
    </g>
    <g transform="translate(20,125)">
      <rect width="190" height="140" rx="8" fill="white" stroke="${t.accent}" stroke-width="1.5"/>
      <rect width="190" height="24" rx="8" fill="${t.accent}" opacity="0.85"/>
      <rect y="18" width="190" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="95" y="17" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">О ЧЁМ?</text>
      <text x="95" y="55" font-family="Arial" font-size="10" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
      <text x="95" y="80" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">${t.items.substring(0,30)}</text>
    </g>
    <g transform="translate(225,125)">
      <rect width="175" height="140" rx="8" fill="white" stroke="${p.l}" stroke-width="1.5"/>
      <rect width="175" height="24" rx="8" fill="${p.l}" opacity="0.85"/>
      <rect y="18" width="175" height="6" fill="${p.l}" opacity="0.85"/>
      <text x="87" y="17" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПРИМЕРЫ</text>
      <text x="87" y="50" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">${t.items}</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];


// ---- ENGLISH ----
SCENES.english = [
  // L1: Приветствие
  (p) => `${svgDefs(p)}
  ${sky()}${ground(270)}
  ${tree(30,225,48)}${tree(460,228,40)}
  <g transform="translate(40,40)" filter="url(#softShadow)">
    <rect width="420" height="225" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">GREETINGS — ПРИВЕТСТВИЕ</text>
    <g transform="translate(20,40)">
      <rect width="180" height="55" rx="8" fill="${p.bg1}" stroke="${p.m}" stroke-width="1.5"/>
      <text x="90" y="25" font-family="Arial" font-size="16" fill="${p.m}" text-anchor="middle" font-weight="bold">Hello!</text>
      <text x="90" y="45" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Привет!</text>
    </g>
    <g transform="translate(220,40)">
      <rect width="180" height="55" rx="8" fill="#FFF3E0" stroke="#FF9800" stroke-width="1.5"/>
      <text x="90" y="25" font-family="Arial" font-size="16" fill="#E65100" text-anchor="middle" font-weight="bold">Good morning!</text>
      <text x="90" y="45" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Доброе утро!</text>
    </g>
    <g transform="translate(20,108)">
      <rect width="180" height="55" rx="8" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="90" y="25" font-family="Arial" font-size="16" fill="#2E7D32" text-anchor="middle" font-weight="bold">How are you?</text>
      <text x="90" y="45" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Как дела?</text>
    </g>
    <g transform="translate(220,108)">
      <rect width="180" height="55" rx="8" fill="#FCE4EC" stroke="#E91E63" stroke-width="1.5"/>
      <text x="90" y="25" font-family="Arial" font-size="16" fill="#AD1457" text-anchor="middle" font-weight="bold">Goodbye!</text>
      <text x="90" y="45" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">До свидания!</text>
    </g>
    <g transform="translate(20,178)">
      <rect width="380" height="35" rx="6" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="190" y="22" font-family="Arial" font-size="10" fill="${p.m}" text-anchor="middle" font-weight="bold">Nice to meet you! — Приятно познакомиться!</text>
    </g>
  </g>
  ${bird(250,50)}${bird(280,38)}
  ${titleBar('Приветствие', p)}`,

  // L2-L24: Generic English
  (p, title, num) => {
    const topics = {
      2: { en:'My name is...', ru:'Меня зовут...', accent:'#1565C0' },
      3: { en:'Please, Thank you, Sorry', ru:'Пожалуйста, Спасибо, Извините', accent:'#2E7D32' },
      4: { en:'Who? What? Where? When?', ru:'Кто? Что? Где? Когда?', accent:'#6A1B9A' },
      5: { en:'Red, Blue, Green, Yellow', ru:'Красный, Синий, Зелёный, Жёлтый', accent:'#D32F2F' },
      6: { en:'One, Two, Three...', ru:'Один, Два, Три...', accent:'#FF8F00' },
      7: { en:'Head, Shoulders, Knees', ru:'Голова, Плечи, Колени', accent:'#00838F' },
      8: { en:'Shirt, Pants, Dress', ru:'Рубашка, Брюки, Платье', accent:'#AD1457' },
      9: { en:'Pen, Book, Ruler', ru:'Ручка, Книга, Линейка', accent:'#5D4037' },
      10: { en:'In the classroom', ru:'В классе', accent:'#1565C0' },
      11: { en:'Math, English, Art', ru:'Математика, Английский, ИЗО', accent:'#2E7D32' },
      12: { en:'Monday, Tuesday...', ru:'Понедельник, Вторник...', accent:'#6A1B9A' },
      13: { en:'Mother, Father, Sister', ru:'Мама, Папа, Сестра', accent:'#E65100' },
      14: { en:'My house', ru:'Мой дом', accent:'#795548' },
      15: { en:'My room', ru:'Моя комната', accent:'#00838F' },
      16: { en:'Weekdays and weekends', ru:'Будни и выходные', accent:'#D32F2F' },
      17: { en:'Bread, Milk, Cheese', ru:'Хлеб, Молоко, Сыр', accent:'#FF8F00' },
      18: { en:'Water, Juice, Tea', ru:'Вода, Сок, Чай', accent:'#2E7D32' },
      19: { en:'Apple, Banana, Carrot', ru:'Яблоко, Банан, Морковь', accent:'#AD1457' },
      20: { en:'At the cafe', ru:'В кафе', accent:'#5D4037' },
      21: { en:'Bus, Car, Train', ru:'Автобус, Машина, Поезд', accent:'#1565C0' },
      22: { en:'City, Street, Park', ru:'Город, Улица, Парк', accent:'#00838F' },
      23: { en:'Big Ben, Tower', ru:'Биг-Бен, Башня', accent:'#E65100' },
      24: { en:'Russia, England, USA', ru:'Россия, Англия, США', accent:'#283593' },
    };
    const t = topics[num] || { en:escXml(title), ru:'', accent:p.m };
    const cleanTitle = title.replace(/^Урок \d+:\s*/,'').replace(/[^\u0400-\u04FF\s\w\-—.,!?()]/g,'').trim();
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${escXml(cleanTitle.toUpperCase())}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="70" rx="8" fill="${p.bg1}" opacity="0.4" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="30" font-family="Arial" font-size="22" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.en}</text>
      <text x="190" y="55" font-family="Arial" font-size="12" fill="#555" text-anchor="middle">${t.ru}</text>
    </g>
    <g transform="translate(20,135)">
      <rect width="185" height="130" rx="8" fill="white" stroke="${t.accent}" stroke-width="1.5"/>
      <rect width="185" height="24" rx="8" fill="${t.accent}" opacity="0.85"/>
      <rect y="18" width="185" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="92" y="17" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПО-АНГЛИЙСКИ</text>
      <text x="92" y="55" font-family="Arial" font-size="14" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.en}</text>
    </g>
    <g transform="translate(220,135)">
      <rect width="180" height="130" rx="8" fill="white" stroke="${p.l}" stroke-width="1.5"/>
      <rect width="180" height="24" rx="8" fill="${p.l}" opacity="0.85"/>
      <rect y="18" width="180" height="6" fill="${p.l}" opacity="0.85"/>
      <text x="90" y="17" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПО-РУССКИ</text>
      <text x="90" y="55" font-family="Arial" font-size="14" fill="#555" text-anchor="middle" font-weight="bold">${t.ru}</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];

// ---- NATURE ----
SCENES.nature = [
  (p) => `${svgDefs(p)}
  ${sky()}${ground(265)}
  ${tree(30,210,58)}${tree(460,215,45)}
  <circle cx="420" cy="60" r="30" fill="url(#sunGrad)" filter="url(#glow)"/>
  <g transform="translate(50,45)" filter="url(#softShadow)">
    <rect width="400" height="215" rx="12" fill="white" opacity="0.94"/>
    <rect width="400" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="400" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="200" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">ЧТО ТАКОЕ КЛИМАТ</text>
    <g transform="translate(15,38)">
      <rect width="370" height="40" rx="6" fill="#E8F5E9" opacity="0.4" stroke="${p.m}" stroke-width="1"/>
      <text x="185" y="26" font-family="Arial" font-size="11" fill="${p.d}" text-anchor="middle" font-weight="bold">Климат — многолетний режим погоды</text>
    </g>
    <g transform="translate(15,90)">
      <rect width="115" height="110" rx="6" fill="#FFF3E0" stroke="#FF9800" stroke-width="1"/>
      <text x="57" y="18" font-family="Arial" font-size="9" fill="#E65100" text-anchor="middle" font-weight="bold">Тропики</text>
      <circle cx="57" cy="55" r="22" fill="#FDD835" opacity="0.4"/>
      <text x="57" y="60" font-family="Arial" font-size="8" fill="#E65100" text-anchor="middle">Жарко</text>
      <text x="57" y="95" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">+25...+35°C</text>
    </g>
    <g transform="translate(142,90)">
      <rect width="115" height="110" rx="6" fill="#E3F2FD" stroke="#1565C0" stroke-width="1"/>
      <text x="57" y="18" font-family="Arial" font-size="9" fill="#1565C0" text-anchor="middle" font-weight="bold">Умеренный</text>
      <path d="M30,40 Q40,30 50,40 Q60,35 70,40 Q80,30 90,40" fill="none" stroke="#5C6BC0" stroke-width="1.5"/>
      <text x="57" y="70" font-family="Arial" font-size="8" fill="#1565C0" text-anchor="middle">Тепло/Холодно</text>
      <text x="57" y="95" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">−10...+25°C</text>
    </g>
    <g transform="translate(270,90)">
      <rect width="115" height="110" rx="6" fill="#E0F7FA" stroke="#00838F" stroke-width="1"/>
      <text x="57" y="18" font-family="Arial" font-size="9" fill="#00838F" text-anchor="middle" font-weight="bold">Арктика</text>
      <circle cx="57" cy="55" r="18" fill="white" stroke="#00ACC1" stroke-width="1"/>
      <text x="57" y="60" font-family="Arial" font-size="8" fill="#00838F" text-anchor="middle">❄</text>
      <text x="57" y="95" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">−30...−5°C</text>
    </g>
  </g>
  ${titleBar('Что такое климат', p)}`,

  // L2-L12: Generic nature
  (p, title, num) => {
    const topics = {
      2: { label:'ТЁПЛЫЕ И ХОЛОДНЫЕ ЗОНЫ', desc:'Экватор — жарко, полюса — холодно', accent:'#FF9800' },
      3: { label:'СЕЗОНЫ ГОДА', desc:'Весна, Лето, Осень, Зима', accent:'#4CAF50' },
      4: { label:'КЛИМАТ И ЖИЗНЬ', desc:'Животные и растения приспосабливаются к климату', accent:'#2E7D32' },
      5: { label:'ЦАРСТВО БАКТЕРИЙ', desc:'Микроскопические организмы, есть повсюду', accent:'#795548' },
      6: { label:'ЦАРСТВО ГРИБОВ', desc:'Шляпка, ножка, грибница — строение гриба', accent:'#FF8F00' },
      7: { label:'ЦАРСТВО РАСТЕНИЙ', desc:'Корень, стебель, лист, цветок, плод', accent:'#2E7D32' },
      8: { label:'ЦАРСТВО ЖИВОТНЫХ', desc:'Насекомые, рыбы, птицы, звери', accent:'#E65100' },
      9: { label:'ЭКОСИСТЕМА', desc:'Взаимосвязь живых организмов и среды', accent:'#00838F' },
      10: { label:'ЛЕС КАК ЭКОСИСТЕМА', desc:'Деревья, кустарники, травы, грибы, животные', accent:'#2E7D32' },
      11: { label:'ВОДОЁМ КАК ЭКОСИСТЕМА', desc:'Рыбы, водоросли, моллюски, птицы', accent:'#1565C0' },
      12: { label:'ЭКОЛОГИЧЕСКИЕ ПРОБЛЕМЫ', desc:'Загрязнение, вырубка лесов, исчезновение видов', accent:'#D32F2F' },
    };
    const t = topics[num] || { label:escXml(title), desc:'', accent:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="70" rx="8" fill="${p.bg1}" opacity="0.4" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="30" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
    <g transform="translate(20,135)">
      <rect width="380" height="130" rx="8" fill="white" stroke="${t.accent}" stroke-width="1.5"/>
      <rect width="380" height="24" rx="8" fill="${t.accent}" opacity="0.85"/>
      <rect y="18" width="380" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="190" y="17" font-family="Arial" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ГЛАВНОЕ</text>
      <text x="190" y="55" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
      <text x="190" y="85" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Окружающий мир — 4 класс</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];

// ---- HISTORY ----
SCENES.history = [
  (p) => `${svgDefs(p)}
  <rect width="500" height="260" fill="#FFF8E1"/>
  <path d="M0,220 Q125,200 250,215 Q375,230 500,210 L500,350 L0,350 Z" fill="#8D6E63" opacity="0.3"/>
  <g transform="translate(40,25)" filter="url(#softShadow)">
    <rect width="420" height="200" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">ИСТОКИ РУСИ</text>
    <g transform="translate(15,40)">
      <path d="M30,130 L30,70 L50,60 L50,130 Z" fill="#D32F2F" stroke="#B71C1C" stroke-width="1.5"/>
      <path d="M22,70 L58,70 L58,58 L22,58 Z" fill="#C62828" stroke="#B71C1C" stroke-width="1"/>
      <path d="M70,130 L70,80 L90,70 L90,130 Z" fill="#E8EAF6" stroke="#3F51B5" stroke-width="1.5"/>
      <path d="M65,80 L95,80 L95,68 L65,68 Z" fill="#C5CAE9" stroke="#3F51B5" stroke-width="1"/>
      <path d="M110,130 L110,85 L130,75 L130,130 Z" fill="#4CAF50" stroke="#2E7D32" stroke-width="1.5"/>
      <text x="80" y="145" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Древние города</text>
    </g>
    <g transform="translate(160,38)">
      <rect width="245" height="155" rx="6" fill="#FFF8E1" opacity="0.4" stroke="${p.m}" stroke-width="1"/>
      <text x="122" y="18" font-family="Arial" font-size="10" fill="${p.d}" text-anchor="middle" font-weight="bold">ПЕРВЫЕ ПЛЕМЕНА</text>
      <line x1="20" y1="35" x2="225" y2="35" stroke="${p.m}" stroke-width="2"/>
      <circle cx="40" cy="35" r="5" fill="${p.m}"/>
      <text x="40" y="55" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Славяне</text>
      <circle cx="100" cy="35" r="5" fill="${p.l}"/>
      <text x="100" y="55" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Варяги</text>
      <circle cx="160" cy="35" r="5" fill="${p.d}"/>
      <text x="160" y="55" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Византия</text>
      <circle cx="210" cy="35" r="5" fill="#BCAAA4"/>
      <text x="210" y="55" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Хазары</text>
      <text x="122" y="80" font-family="Arial" font-size="9" fill="${p.d}" text-anchor="middle" font-weight="bold">862 год — призвание Рюрика</text>
      <text x="122" y="100" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Славянские племена объединялись</text>
      <text x="122" y="118" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">для защиты от врагов</text>
      <text x="122" y="140" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">Новгород → Киев → Древняя Русь</text>
    </g>
  </g>
  ${titleBar('Истоки Руси', p)}`,

  // L2-L12
  (p, title, num) => {
    const topics = {
      2: { label:'ПЕРВЫЕ КНЯЗЬЯ', desc:'Рюрик, Олег, Игорь — основатели государства', accent:'#8D6E63' },
      3: { label:'КНЯЗЬ ИГОРЬ И ОЛЬГА', desc:'Игорь — сбор дани, Ольга — реформа управления', accent:'#5D4037' },
      4: { label:'СВЯТОСЛАВ', desc:'Великий воин-князь, расширил границы Руси', accent:'#D32F2F' },
      5: { label:'КНЯЗЬ ВЛАДИМИР', desc:'Крестил Русь в 988 году', accent:'#1565C0' },
      6: { label:'РАСПРОСТРАНЕНИЕ ХРИСТИАНСТВА', desc:'Церкви, монастыри, грамотность', accent:'#FF8F00' },
      7: { label:'ЯРОСЛАВ МУДРЫЙ', desc:'Русская Правда, строительство, образование', accent:'#2E7D32' },
      8: { label:'КУЛЬТУРА ДРЕВНЕЙ РУСИ', desc:'Летописи, иконы, храмы, былины', accent:'#6A1B9A' },
      9: { label:'НАШЕСТВИЕ МОНГОЛОВ', desc:'1237 — Батый напал на Русь', accent:'#B71C1C' },
      10: { label:'БОРЬБА С ИГОМ', desc:'1240 — Невская битва, Ледовое побоище', accent:'#D32F2F' },
      11: { label:'КУЛИКОВСКАЯ БИТВА', desc:'1380 — Дмитрий Донской разбил Мамая', accent:'#E65100' },
      12: { label:'ОСВОБОЖДЕНИЕ', desc:'1480 — Стояние на Угре, конец ига', accent:'#2E7D32' },
    };
    const t = topics[num] || { label:escXml(title), desc:'', accent:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="260" fill="#FFF8E1"/>
  <path d="M0,225 Q125,210 250,220 Q375,232 500,215 L500,350 L0,350 Z" fill="#8D6E63" opacity="0.25"/>
  <g transform="translate(40,25)" filter="url(#softShadow)">
    <rect width="420" height="200" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(20,40)">
      <rect width="380" height="55" rx="6" fill="#FFF8E1" opacity="0.5" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="25" font-family="Arial" font-size="14" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
    <g transform="translate(20,110)">
      <rect width="380" height="75" rx="6" fill="white" stroke="${t.accent}" stroke-width="1"/>
      <rect width="380" height="22" rx="6" fill="${t.accent}" opacity="0.85"/>
      <rect y="16" width="380" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="190" y="16" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ИСТОРИЧЕСКИЙ ФАКТ</text>
      <text x="190" y="48" font-family="Arial" font-size="10" fill="${p.d}" text-anchor="middle">${t.desc}</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];


// ---- GEOGRAPHY ----
SCENES.geography = [
  (p) => `${svgDefs(p)}
  ${sky()}${ground(270)}
  <g transform="translate(40,35)" filter="url(#softShadow)">
    <rect width="420" height="230" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="28" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="20" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="19" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">РОССИЯ НА КАРТЕ</text>
    <g transform="translate(15,38)">
      <rect width="220" height="180" rx="6" fill="#E0F7FA" opacity="0.3" stroke="${p.m}" stroke-width="1.5"/>
      <path d="M30,30 L80,20 L140,25 L180,40 L190,70 L170,100 L140,130 L100,145 L60,140 L25,120 L15,90 L20,55 Z" fill="${p.m}" opacity="0.12" stroke="${p.m}" stroke-width="1.5"/>
      <path d="M45,50 Q60,45 75,55 Q85,48 100,55" fill="none" stroke="#1565C0" stroke-width="1" opacity="0.5"/>
      <circle cx="85" cy="80" r="5" fill="#D32F2F" opacity="0.7"/>
      <text x="85" y="73" font-family="Arial" font-size="7" fill="${p.d}" text-anchor="middle" font-weight="bold">Москва</text>
      <circle cx="130" cy="50" r="3" fill="#FF9800" opacity="0.7"/>
      <text x="145" y="53" font-family="Arial" font-size="6" fill="#555">Екатеринбург</text>
      <circle cx="55" cy="95" r="3" fill="#2E7D32" opacity="0.7"/>
      <text x="68" y="98" font-family="Arial" font-size="6" fill="#555">С-Петербург</text>
      <text x="110" y="170" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">Самая большая страна</text>
    </g>
    <g transform="translate(250,38)">
      <rect width="155" height="180" rx="6" fill="white" stroke="${p.m}" stroke-width="1"/>
      <rect width="155" height="22" rx="6" fill="${p.m}" opacity="0.85"/>
      <rect y="16" width="155" height="6" fill="${p.m}" opacity="0.85"/>
      <text x="77" y="16" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ФАКТЫ</text>
      <text x="77" y="42" font-family="Arial" font-size="8" fill="${p.d}" font-weight="bold">17 100 000 км²</text>
      <text x="77" y="56" font-family="Arial" font-size="7" fill="#555">Площадь России</text>
      <text x="77" y="76" font-family="Arial" font-size="8" fill="${p.d}" font-weight="bold">146 млн чел.</text>
      <text x="77" y="90" font-family="Arial" font-size="7" fill="#555">Население</text>
      <text x="77" y="110" font-family="Arial" font-size="8" fill="${p.d}" font-weight="bold">11 часовых поясов</text>
      <text x="77" y="124" font-family="Arial" font-size="7" fill="#555">От Калининграда</text>
      <text x="77" y="136" font-family="Arial" font-size="7" fill="#555">до Камчатки</text>
      <text x="77" y="158" font-family="Arial" font-size="8" fill="${p.m}" font-weight="bold">Соседи: 18 стран</text>
      <text x="77" y="172" font-family="Arial" font-size="7" fill="#555">Больше всех в мире!</text>
    </g>
  </g>
  ${titleBar('Россия на карте', p)}`,

  // L2-L12
  (p, title, num) => {
    const topics = {
      2: { label:'СУБЪЕКТЫ РОССИИ', desc:'89 субъектов: республики, края, области', accent:'#8D6E63' },
      3: { label:'СТОЛИЦА РОССИИ', desc:'Москва — Кремль, Красная площадь', accent:'#D32F2F' },
      4: { label:'ГОРОДА-МИЛЛИОННИКИ', desc:'15 городов с населением более 1 млн', accent:'#FF9800' },
      5: { label:'РЕКИ РОССИИ', desc:'Волга, Обь, Енисей, Лена, Амур', accent:'#1565C0' },
      6: { label:'ОЗЁРА РОССИИ', desc:'Байкал — самое глубокое озеро мира', accent:'#00838F' },
      7: { label:'МОРЯ РОССИИ', desc:'12 морей омывают берега России', accent:'#0D47A1' },
      8: { label:'ВОДНЫЕ РЕСУРСЫ', desc:'Реки, озёра, моря — богатство России', accent:'#006064' },
      9: { label:'ПРИРОДНЫЕ ЗОНЫ', desc:'Тундра, тайга, смешанный лес, степь, пустыня', accent:'#2E7D32' },
      10: { label:'ЖИВОТНЫЙ МИР', desc:'От белого медведя до снежного барса', accent:'#E65100' },
      11: { label:'ПОЛЕЗНЫЕ ИСКОПАЕМЫЕ', desc:'Нефть, газ, уголь, железо, золото', accent:'#795548' },
      12: { label:'ОХРАНА ПРИРОДЫ', desc:'Заповедники, национальные парки', accent:'#2E7D32' },
    };
    const t = topics[num] || { label:escXml(title), desc:'', accent:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="70" rx="8" fill="${p.bg1}" opacity="0.4" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="30" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
    <g transform="translate(20,135)">
      <rect width="380" height="130" rx="8" fill="white" stroke="${t.accent}" stroke-width="1.5"/>
      <rect width="380" height="24" rx="8" fill="${t.accent}" opacity="0.85"/>
      <rect y="18" width="380" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="190" y="17" font-family="Arial" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ЗАПОМНИ</text>
      <text x="190" y="55" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];

// ---- MUSIC ----
SCENES.music = [
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">МУЗЫКАЛЬНЫЕ ИНСТРУМЕНТЫ</text>
    <g transform="translate(15,45)">
      <rect width="125" height="120" rx="8" fill="#FCE4EC" stroke="${p.m}" stroke-width="1.5"/>
      <text x="62" y="18" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle" font-weight="bold">СТРУННЫЕ</text>
      <ellipse cx="62" cy="65" rx="18" ry="28" fill="${p.m}" opacity="0.1" stroke="${p.m}" stroke-width="1.5"/>
      <line x1="62" y1="37" x2="62" y2="93" stroke="${p.m}" stroke-width="2"/>
      <line x1="52" y1="62" x2="72" y2="62" stroke="${p.m}" stroke-width="0.5"/>
      <line x1="52" y1="68" x2="72" y2="68" stroke="${p.m}" stroke-width="0.5"/>
      <text x="62" y="112" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Скрипка, Гитара</text>
    </g>
    <g transform="translate(150,45)">
      <rect width="125" height="120" rx="8" fill="#F3E5F5" stroke="${p.l}" stroke-width="1.5"/>
      <text x="62" y="18" font-family="Arial" font-size="8" fill="${p.l}" text-anchor="middle" font-weight="bold">КЛАВИШНЫЕ</text>
      <rect x="20" y="30" width="84" height="45" rx="3" fill="white" stroke="${p.m}" stroke-width="1"/>
      <rect x="24" y="33" width="10" height="20" fill="white" stroke="#555" stroke-width="0.5"/>
      <rect x="36" y="33" width="10" height="20" fill="#333"/>
      <rect x="48" y="33" width="10" height="20" fill="white" stroke="#555" stroke-width="0.5"/>
      <rect x="60" y="33" width="10" height="20" fill="#333"/>
      <rect x="72" y="33" width="10" height="20" fill="#333"/>
      <rect x="84" y="33" width="10" height="20" fill="white" stroke="#555" stroke-width="0.5"/>
      <text x="62" y="112" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Пианино, Орган</text>
    </g>
    <g transform="translate(285,45)">
      <rect width="125" height="120" rx="8" fill="#FFF3E0" stroke="#FF9800" stroke-width="1.5"/>
      <text x="62" y="18" font-family="Arial" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">ДУХОВЫЕ</text>
      <path d="M30,70 Q40,50 50,60 L80,55 Q90,50 95,55 L100,60" fill="none" stroke="#E65100" stroke-width="3" stroke-linecap="round"/>
      <circle cx="100" cy="60" r="6" fill="#FF9800" opacity="0.3"/>
      <text x="62" y="112" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Флейта, Труба</text>
    </g>
    <g transform="translate(15,180)">
      <rect width="125" height="90" rx="8" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1.5"/>
      <text x="62" y="18" font-family="Arial" font-size="8" fill="#2E7D32" text-anchor="middle" font-weight="bold">УДАРНЫЕ</text>
      <ellipse cx="62" cy="50" rx="25" ry="12" fill="#8D6E63" opacity="0.3" stroke="#5D4037" stroke-width="1.5"/>
      <line x1="62" y1="38" x2="62" y2="62" stroke="#5D4037" stroke-width="1"/>
      <text x="62" y="80" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Барабан, Бубен</text>
    </g>
    <g transform="translate(150,180)">
      <rect width="260" height="90" rx="8" fill="${p.bg1}" opacity="0.3" stroke="${p.m}" stroke-width="1"/>
      <text x="130" y="18" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle" font-weight="bold">НАРОДНЫЕ ИНСТРУМЕНТЫ</text>
      <text x="130" y="40" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Балалайка, Гармонь, Домра</text>
      <text x="130" y="58" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Гусли, Рожок, Ложки</text>
      <text x="130" y="80" font-family="Arial" font-size="8" fill="${p.m}" text-anchor="middle">Традиционные русские инструменты</text>
    </g>
  </g>
  ${titleBar('Музыкальные инструменты', p)}`,

  // L2-L12
  (p, title, num) => {
    const topics = {
      2: { label:'НОТНАЯ ГРАМОТА', desc:'До, Ре, Ми, Фа, Соль, Ля, Си — 7 нот', accent:'#E91E63' },
      3: { label:'ТЕМБР И РЕГИСТР', desc:'Высокий, средний, низкий регистр', accent:'#9C27B0' },
      4: { label:'М.И. ГЛИНКА', desc:'Основоположник русской классической музыки', accent:'#3F51B5' },
      5: { label:'П.И. ЧАЙКОВСКИЙ', desc:'Щелкунчик, Лебединое озеро, Спящая красавица', accent:'#F44336' },
      6: { label:'Н.А. РИМСКИЙ-КОРСАКОВ', desc:'Садко, Шехеразада, Снегурочка', accent:'#FF9800' },
      7: { label:'С.С. ПРОКОФЬЕВ', desc:'Петя и волк, Ромео и Джульетта', accent:'#4CAF50' },
      8: { label:'ОПЕРА И БАЛЕТ', desc:'Опера — поют, Балет — танцуют', accent:'#E91E63' },
      9: { label:'КОНЦЕРТ И СИМФОНИЯ', desc:'Оркестр — группа музыкантов', accent:'#9C27B0' },
      10: { label:'ПЕСНЯ И РОМАНС', desc:'Песня — народная, Романс — камерная', accent:'#FF9800' },
      11: { label:'РУССКИЕ НАРОДНЫЕ ИНСТРУМЕНТЫ', desc:'Балалайка, гармонь, гусли', accent:'#795548' },
      12: { label:'РУССКИЕ НАРОДНЫЕ ПЕСНИ', desc:'Калинка, Катюша, Во поле берёза', accent:'#2E7D32' },
    };
    const t = topics[num] || { label:escXml(title), desc:'', accent:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="70" rx="8" fill="${p.bg1}" opacity="0.4" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="30" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
    <g transform="translate(20,135)">
      <rect width="380" height="130" rx="8" fill="white" stroke="${t.accent}" stroke-width="1.5"/>
      <rect width="380" height="24" rx="8" fill="${t.accent}" opacity="0.85"/>
      <rect y="18" width="380" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="190" y="17" font-family="Arial" font-size="10" fill="white" text-anchor="middle" font-weight="bold">МУЗЫКА</text>
      <text x="190" y="55" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];

// ---- ART ----
SCENES.art = [
  (p) => `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,25)" filter="url(#softShadow)">
    <rect width="420" height="290" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">ЖАНРЫ ЖИВОПИСИ</text>
    <g transform="translate(15,45)">
      <rect width="130" height="120" rx="8" fill="#FFF3E0" stroke="#FF9800" stroke-width="1.5"/>
      <text x="65" y="16" font-family="Arial" font-size="8" fill="#E65100" text-anchor="middle" font-weight="bold">НАТЮРМОРТ</text>
      <rect x="20" y="25" width="90" height="65" rx="2" fill="#FFFDE7" stroke="#E65100" stroke-width="1"/>
      <path d="M35,55 Q45,45 55,55 Q65,45 75,55" fill="#E91E63" opacity="0.3"/>
      <circle cx="45" cy="50" r="8" fill="#F44336" opacity="0.4"/>
      <circle cx="65" cy="48" r="7" fill="#FF9800" opacity="0.4"/>
      <rect x="30" y="65" width="50" height="15" rx="2" fill="#8D6E63" opacity="0.3"/>
      <text x="65" y="108" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Изображение предметов</text>
    </g>
    <g transform="translate(155,45)">
      <rect width="130" height="120" rx="8" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
      <text x="65" y="16" font-family="Arial" font-size="8" fill="#1565C0" text-anchor="middle" font-weight="bold">ПЕЙЗАЖ</text>
      <rect x="20" y="25" width="90" height="65" rx="2" fill="#E8F5E9" stroke="#1565C0" stroke-width="1"/>
      <path d="M20,75 Q40,45 60,60 Q80,40 110,75" fill="#4CAF50" opacity="0.3"/>
      <circle cx="90" cy="38" r="8" fill="#FDD835" opacity="0.5"/>
      <path d="M20,75 L110,75 L110,90 L20,90 Z" fill="#81C784" opacity="0.3"/>
      <text x="65" y="108" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Изображение природы</text>
    </g>
    <g transform="translate(295,45)">
      <rect width="110" height="120" rx="8" fill="#FCE4EC" stroke="#E91E63" stroke-width="1.5"/>
      <text x="55" y="16" font-family="Arial" font-size="8" fill="#AD1457" text-anchor="middle" font-weight="bold">ПОРТРЕТ</text>
      <rect x="20" y="25" width="70" height="65" rx="2" fill="#FFF3E0" stroke="#E91E63" stroke-width="1"/>
      <circle cx="55" cy="45" r="12" fill="#FFCCBC" opacity="0.5"/>
      <path d="M40,65 Q55,58 70,65" fill="#E91E63" opacity="0.15"/>
      <text x="55" y="108" font-family="Arial" font-size="7" fill="#555" text-anchor="middle">Изображение людей</text>
    </g>
    <g transform="translate(15,180)">
      <rect width="390" height="90" rx="8" fill="white" stroke="${p.m}" stroke-width="1"/>
      <rect width="390" height="22" rx="8" fill="${p.m}" opacity="0.85"/>
      <rect y="16" width="390" height="6" fill="${p.m}" opacity="0.85"/>
      <text x="195" y="16" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ДРУГИЕ ЖАНРЫ</text>
      <text x="195" y="48" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Анималистический • Исторический • Батальный • Бытовой</text>
      <text x="195" y="70" font-family="Arial" font-size="9" fill="${p.m}" text-anchor="middle">Каждый жанр рассказывает свою историю через краски</text>
    </g>
  </g>
  ${titleBar('Жанры живописи', p)}`,

  // L2-L12
  (p, title, num) => {
    const topics = {
      2: { label:'НАТЮРМОРТ', desc:'Композиция из неживых предметов: фрукты, цветы, посуда', accent:'#FF9800' },
      3: { label:'ПОРТРЕТ', desc:'Изображение человека, передающее его характер', accent:'#E91E63' },
      4: { label:'ПЕЙЗАЖ', desc:'Картина природы: лес, поле, река, горы', accent:'#2E7D32' },
      5: { label:'РУССКИЕ ХУДОЖНИКИ', desc:'Левитан, Шишкин, Суриков, Репин, Айвазовский', accent:'#6A1B9A' },
      6: { label:'МУЗЕИ РОССИИ', desc:'Третьяковская галерея, Эрмитаж, Русский музей', accent:'#8D6E63' },
      7: { label:'РИСУНОК И ГРАФИКА', desc:'Линия, штрих, пятно — средства графики', accent:'#424242' },
      8: { label:'НАРОДНОЕ ИСКУССТВО', desc:'Хохлома, Гжель, Дымка, Жостово', accent:'#D32F2F' },
      9: { label:'ОСНОВЫ ЦВЕТА', desc:'Тёплые и холодные цвета, цветовой круг', accent:'#FDD835' },
      10: { label:'КОМПОЗИЦИЯ', desc:'Правило третей, центр внимания, ритм', accent:'#1565C0' },
      11: { label:'СВЕТ И ТЕНЬ', desc:'Блик, полутень, тень, рефлекс, падающая тень', accent:'#424242' },
      12: { label:'ТВОРЧЕСКИЙ ПРОЕКТ', desc:'Создаём свою картину!', accent:'#6A1B9A' },
    };
    const t = topics[num] || { label:escXml(title), desc:'', accent:p.m };
    return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${t.label}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="70" rx="8" fill="${p.bg1}" opacity="0.4" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="30" font-family="Arial" font-size="16" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
    <g transform="translate(20,135)">
      <rect width="380" height="130" rx="8" fill="white" stroke="${t.accent}" stroke-width="1.5"/>
      <rect width="380" height="24" rx="8" fill="${t.accent}" opacity="0.85"/>
      <rect y="18" width="380" height="6" fill="${t.accent}" opacity="0.85"/>
      <text x="190" y="17" font-family="Arial" font-size="10" fill="white" text-anchor="middle" font-weight="bold">ИЗО</text>
      <text x="190" y="55" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">${t.desc}</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
  },
];

// ---- PE, TECH, INFORMATICS, RELIGION, PROJECTS, WORLD ----
// Generic scene generators for remaining subjects

function genericScene(p, title, subject, num) {
  const subjectInfo = {
    pe: { name:'ФИЗКУЛЬТУРА', icon:'🏃', accent:'#2E7D32' },
    tech: { name:'ТЕХНОЛОГИЯ', icon:'🔧', accent:'#4E342E' },
    informatics: { name:'ИНФОРМАТИКА', icon:'💻', accent:'#00695C' },
    religion: { name:'ОСНОВЫ РЕЛИГИОЗНЫХ КУЛЬТУР', icon:'🕊', accent:'#FF8F00' },
    projects: { name:'ПРОЕКТНАЯ ДЕЯТЕЛЬНОСТЬ', icon:'💡', accent:'#5D4037' },
    world: { name:'ОКРУЖАЮЩИЙ МИР', icon:'🌍', accent:'#1565C0' },
  };
  const si = subjectInfo[subject] || { name:subject.toUpperCase(), icon:'', accent:p.m };
  const cleanTitle = title.replace(/^Урок \d+:\s*/,'').replace(/[^\u0400-\u04FF\s\w\-—.,!?()]/g,'').trim();
  return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,30)" filter="url(#softShadow)">
    <rect width="420" height="285" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${escXml(cleanTitle.toUpperCase())}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="80" rx="8" fill="${p.bg1}" opacity="0.5" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="35" font-family="Arial" font-size="18" fill="${p.d}" text-anchor="middle" font-weight="bold">${escXml(cleanTitle)}</text>
      <text x="190" y="60" font-family="Arial" font-size="11" fill="#555" text-anchor="middle">${si.name} — 4 класс, Урок ${num}</text>
    </g>
    <g transform="translate(20,145)">
      <rect width="185" height="120" rx="8" fill="white" stroke="${p.m}" stroke-width="1.5"/>
      <rect width="185" height="22" rx="8" fill="${p.m}" opacity="0.85"/>
      <rect y="16" width="185" height="6" fill="${p.m}" opacity="0.85"/>
      <text x="92" y="16" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ТЕМА УРОКА</text>
      <text x="92" y="55" font-family="Arial" font-size="11" fill="${p.d}" text-anchor="middle" font-weight="bold">${escXml(cleanTitle)}</text>
      <text x="92" y="78" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">4 класс</text>
      <text x="92" y="95" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Урок ${num}</text>
    </g>
    <g transform="translate(220,145)">
      <rect width="180" height="120" rx="8" fill="white" stroke="${si.accent}" stroke-width="1.5"/>
      <rect width="180" height="22" rx="8" fill="${si.accent}" opacity="0.85"/>
      <rect y="16" width="180" height="6" fill="${si.accent}" opacity="0.85"/>
      <text x="90" y="16" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ПРЕДМЕТ</text>
      <text x="90" y="55" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">${si.name}</text>
      <text x="90" y="80" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Четвёртый класс</text>
      <text x="90" y="98" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">Начальная школа</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
}


// ============================================================
// MAIN GENERATOR
// ============================================================

// Subject-specific scene data for PE, TECH, INFORMATICS, RELIGION, PROJECTS, WORLD
const SUBJECT_TOPICS = {
  pe: [
    { label:'Строевые упражнения', desc:'Построение, перестроение, повороты' },
    { label:'Гимнастические упражнения', desc:'Кувырки, стойка на лопатках, мост' },
    { label:'Упражнения с предметами', desc:'Мяч, скакалка, обруч, гимнастическая палка' },
    { label:'Бег и ходьба', desc:'Бег на короткие и длинные дистанции' },
    { label:'Прыжки', desc:'Прыжки в длину, в высоту, через скакалку' },
    { label:'Метание', desc:'Метание малого мяча на дальность и точность' },
    { label:'Футбол', desc:'Ведение мяча, передача, удар по воротам' },
    { label:'Баскетбол', desc:'Ведение, бросок, передача мяча' },
    { label:'Волейбол', desc:'Подача, приём, передача мяча' },
    { label:'Лыжная подготовка', desc:'Попеременный двухшажный ход, подъём, спуск' },
    { label:'Катание на коньках', desc:'Скольжение, торможение, повороты' },
    { label:'Подвижные игры зимой', desc:'Снежки, хоккей, эстафеты на снегу' },
  ],
  tech: [
    { label:'Свойства бумаги', desc:'Сгибается, режется, склеивается' },
    { label:'Разметка деталей', desc:'Линейка, угольник, шаблон' },
    { label:'Вырезание деталей', desc:'Ножницы, правила безопасности' },
    { label:'Аппликация', desc:'Наклеивание вырезанных деталей' },
    { label:'Свойства ткани', desc:'Ткётся, шьётся, кроится' },
    { label:'Ручные швы', desc:'Шов «вперёд иголку», «назад иголку»' },
    { label:'Пришивание пуговиц', desc:'Пуговица с 2 и 4 отверстиями' },
    { label:'Изготовление игрушки', desc:'Лекало, раскрой, сборка, оформление' },
    { label:'Объёмные модели из бумаги', desc:'Куб, пирамида, цилиндр из бумаги' },
    { label:'Модели из природного материала', desc:'Шишки, жёлуди, листья' },
    { label:'Технические модели', desc:'Машины, корабли, самолёты' },
    { label:'Архитектурные модели', desc:'Дома, мосты, замки' },
    { label:'Пластилин', desc:'Лепка, примазывание, сглаживание' },
    { label:'Солёное тесто', desc:'Замешивание, формовка, сушка, роспись' },
    { label:'Глина', desc:'Лепка посуды, фигурок' },
    { label:'Подарок маме', desc:'Открытка, брелок, игрушка' },
    { label:'Новогодняя игрушка', desc:'Ёлочные украшения, гирлянды' },
    { label:'Макет моей комнаты', desc:'Мебель, стены, окно из картона' },
    { label:'Поделка для школы', desc:'Оформление класса к празднику' },
    { label:'Итоговая выставка', desc:'Представление работ, оценка' },
  ],
  informatics: [
    { label:'Знакомство с клавиатурой', desc:'Буквы, цифры, знаки — назначение клавиш' },
    { label:'Слепая печать', desc:'Печать без взгляда на клавиатуру' },
    { label:'Специальные клавиши', desc:'Enter, Space, Shift, Ctrl, Alt, Backspace' },
    { label:'Русская и английская раскладка', desc:'Переключение языков: Shift+Alt, Ctrl+Shift' },
    { label:'Графический редактор Paint', desc:'Заливка, кисть, ластик, выделение' },
    { label:'Инструменты рисования', desc:'Карандаш, кисть, распылитель, линия' },
    { label:'Геометрические фигуры', desc:'Прямоугольник, эллипс, многоугольник' },
    { label:'Редактирование рисунка', desc:'Копировать, вставить, отменить, повторить' },
    { label:'Безопасный интернет', desc:'Не делись личной информацией, пароли' },
    { label:'Поиск информации', desc:'Поисковик, ключевые слова, запрос' },
    { label:'Текстовые документы', desc:'Набор текста, форматирование, сохранение' },
    { label:'Итоговый проект', desc:'Создание рисунка и текста на тему' },
  ],
  religion: [
    { label:'Что такое религия', desc:'Вера, традиции, духовные ценности' },
    { label:'Православие в России', desc:'Главная религия, храмы, традиции' },
    { label:'Ислам и другие религии', desc:'Уважение к вере других людей' },
    { label:'Священные книги', desc:'Библия, Коран, Тора — книги мудрости' },
    { label:'Православный храм', desc:'Купола, колокольня, алтарь, иконы' },
    { label:'Молитва и богослужение', desc:'Обращение к Богу, церковная служба' },
    { label:'Православные праздники', desc:'Пасха, Рождество, Троица, Крещение' },
    { label:'Пост и традиции', desc:'Ограничения, покаяние, духовное очищение' },
    { label:'Добро и зло', desc:'Мораль, выбор, ответственность' },
    { label:'Десять заповедей', desc:'Правила жизни, данные Богом' },
    { label:'Милосердие и помощь', desc:'Помощь ближнему, благотворительность' },
    { label:'Семья и традиции', desc:'Семейные ценности, любовь, уважение' },
  ],
  projects: [
    { label:'Выбор темы исследования', desc:'Интерес, актуальность, доступность' },
    { label:'Сбор информации', desc:'Книги, интернет, наблюдения, интервью' },
    { label:'Методы исследования', desc:'Наблюдение, эксперимент, сравнение' },
    { label:'Анализ и выводы', desc:'Обобщение данных, формулирование выводов' },
    { label:'Проектирование макета', desc:'Чертёж, размеры, материалы' },
    { label:'Работа с материалами', desc:'Бумага, картон, ткань, клей' },
    { label:'Сборка и отделка', desc:'Соединение деталей, оформление' },
    { label:'Макеты природных объектов', desc:'Вулкан, гора, река из папье-маше' },
    { label:'Структура презентации', desc:'Введение, основная часть, заключение' },
    { label:'Создание слайдов', desc:'Заголовок, текст, иллюстрации' },
    { label:'Выступление перед аудиторией', desc:'Речь, жесты, контакт со слушателями' },
    { label:'Классная конференция', desc:'Представление проектов, вопросы, оценка' },
  ],
  world: [
    { label:'Карта природных зон', desc:'Тундра, тайга, степь, пустыня на карте' },
    { label:'Арктика и тундра', desc:'Вечная мерзлота, полярная ночь, северное сияние' },
    { label:'Леса России', desc:'Тайга, смешанный лес, широколиственный лес' },
    { label:'Степи и пустыни', desc:'Степь — ковыль, пустыня — барханы' },
    { label:'Древние славяне', desc:'Племена, занятия, верования' },
    { label:'Образование Древней Руси', desc:'862 — призвание Рюрика' },
    { label:'Крещение Руси', desc:'988 — князь Владимир крестил Русь' },
    { label:'Князья Руси', desc:'Олег, Святослав, Ярослав Мудрый' },
    { label:'Строение тела человека', desc:'Голова, туловище, конечности, органы' },
    { label:'Пищеварение', desc:'Рот, желудок, кишечник — путь пищи' },
    { label:'Дыхание', desc:'Лёгкие, бронхи, трахея — газообмен' },
    { label:'Кровообращение', desc:'Сердце, сосуды, кровь — транспорт' },
    { label:'Вода и воздух', desc:'Свойства воды и воздуха, значение для жизни' },
    { label:'Полезные ископаемые', desc:'Нефть, газ, уголь, железо, гранит, мел' },
    { label:'Почва', desc:'Плодородный слой, перегной, минералы' },
    { label:'Растения и животные', desc:'Классификация, приспособление к среде' },
    { label:'Охрана природы', desc:'Заповедники, национальные парки, законы' },
    { label:'Красная книга', desc:'Исчезающие виды животных и растений' },
    { label:'Заповедники России', desc:'Охраняемые территории, уникальная природа' },
    { label:'Экологически чистый мир', desc:'Раздельный сбор, экономия ресурсов' },
  ],
};

// Enhanced generic scene with subject-specific content
function enhancedGenericScene(p, title, subject, num) {
  const topics = SUBJECT_TOPICS[subject];
  const topic = topics && topics[num-1] ? topics[num-1] : { label:title.replace(/^Урок \d+:\s*/,'').replace(/[^\u0400-\u04FF\s\w\-—.,!?()]/g,'').trim(), desc:'' };
  const cleanLabel = topic.label.replace(/[^\u0400-\u04FF\s\w\-—.,!?()]/g,'').trim();
  return `${svgDefs(p)}
  <rect width="500" height="350" fill="url(#bgGrad)"/>
  <g transform="translate(40,25)" filter="url(#softShadow)">
    <rect width="420" height="290" rx="12" fill="white" opacity="0.94"/>
    <rect width="420" height="32" rx="12" fill="${p.m}" opacity="0.9"/>
    <rect y="24" width="420" height="8" fill="${p.m}" opacity="0.9"/>
    <text x="210" y="22" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="bold">${escXml(cleanLabel.toUpperCase())}</text>
    <g transform="translate(20,48)">
      <rect width="380" height="75" rx="8" fill="${p.bg1}" opacity="0.5" stroke="${p.m}" stroke-width="1.5"/>
      <text x="190" y="30" font-family="Arial" font-size="18" fill="${p.d}" text-anchor="middle" font-weight="bold">${escXml(cleanLabel)}</text>
      <text x="190" y="55" font-family="Arial" font-size="11" fill="#555" text-anchor="middle">${escXml(topic.desc)}</text>
    </g>
    <g transform="translate(20,140)">
      <rect width="185" height="130" rx="8" fill="white" stroke="${p.m}" stroke-width="1.5"/>
      <rect width="185" height="24" rx="8" fill="${p.m}" opacity="0.85"/>
      <rect y="18" width="185" height="6" fill="${p.m}" opacity="0.85"/>
      <text x="92" y="17" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">ТЕМА</text>
      <text x="92" y="55" font-family="Arial" font-size="12" fill="${p.d}" text-anchor="middle" font-weight="bold">${escXml(cleanLabel)}</text>
      <text x="92" y="80" font-family="Arial" font-size="9" fill="#555" text-anchor="middle">${escXml(topic.desc.substring(0,35))}</text>
    </g>
    <g transform="translate(220,140)">
      <rect width="180" height="130" rx="8" fill="white" stroke="${p.l}" stroke-width="1.5"/>
      <rect width="180" height="24" rx="8" fill="${p.l}" opacity="0.85"/>
      <rect y="18" width="180" height="6" fill="${p.l}" opacity="0.85"/>
      <text x="90" y="17" font-family="Arial" font-size="9" fill="white" text-anchor="middle" font-weight="bold">УРОК ${num}</text>
      <text x="90" y="55" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Четвёртый класс</text>
      <text x="90" y="75" font-family="Arial" font-size="10" fill="#555" text-anchor="middle">Начальная школа</text>
    </g>
  </g>
  ${titleBar(title, p)}`;
}

// Generate all SVGs
function generateAll() {
  const subjects = Object.keys(PALETTES);
  let total = 0;

  subjects.forEach(subject => {
    const dataPath = path.join(GRADE_DIR, subject + '.json');
    if (!fs.existsSync(dataPath)) {
      console.log(`SKIP ${subject}: no data file`);
      return;
    }

    const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
    const lessons = data.lessons?.detailedTopics?.flatMap(t => t.lessons || []) || [];
    if (lessons.length === 0) {
      console.log(`SKIP ${subject}: no lessons`);
      return;
    }

    const outDir = path.join(IMG_DIR, subject);
    fs.mkdirSync(outDir, { recursive: true });

    const p = PALETTES[subject];
    const scenes = SCENES[subject];

    lessons.forEach((lesson, idx) => {
      const num = idx + 1;
      const title = lesson.title || `Урок ${num}`;
      let svgContent;

      if (scenes && scenes.length > 0) {
        // Use specific scene if available, otherwise use last (generic) one
        const sceneIdx = Math.min(num - 1, scenes.length - 1);
        svgContent = scenes[sceneIdx](p, title, num);
      } else {
        svgContent = enhancedGenericScene(p, title, subject, num);
      }

      const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">\n${svgContent}\n</svg>`;
      const outPath = path.join(outDir, `lesson${num}.svg`);
      fs.writeFileSync(outPath, svg);
      total++;
    });

    console.log(`${subject}: ${lessons.length} SVGs generated`);
  });

  console.log(`\nTotal: ${total} SVGs generated`);
}

generateAll();

