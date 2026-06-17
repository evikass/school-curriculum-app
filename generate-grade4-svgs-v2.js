const fs = require('fs');
const path = require('path');

const GRADE_DIR = 'public/data/grades/4';
const IMG_DIR = 'public/images/lessons/grade4';

// Subject configs: color palette, display name, illustration style
const SUBJECT_CONFIG = {
  math: {
    name: 'Математика',
    colors: { main: '#1565C0', dark: '#0D47A1', mid: '#1976D2', light: '#42A5F5', lighter: '#64B5F6', bg1: '#E3F2FD', bg2: '#BBDEFB' },
  },
  russian: {
    name: 'Русский язык',
    colors: { main: '#D32F2F', dark: '#B71C1C', mid: '#E53935', light: '#EF5350', lighter: '#E57373', bg1: '#FFEBEE', bg2: '#FFCDD2' },
  },
  literature: {
    name: 'Литература',
    colors: { main: '#283593', dark: '#1A237E', mid: '#3949AB', light: '#5C6BC0', lighter: '#7986CB', bg1: '#E8EAF6', bg2: '#C5CAE9' },
  },
  nature: {
    name: 'Окружающий мир',
    colors: { main: '#2E7D32', dark: '#1B5E20', mid: '#388E3C', light: '#43A047', lighter: '#66BB6A', bg1: '#E8F5E9', bg2: '#C8E6C9' },
  },
  english: {
    name: 'Английский язык',
    colors: { main: '#F57C00', dark: '#E65100', mid: '#FB8C00', light: '#FFA726', lighter: '#FFB74D', bg1: '#FFF3E0', bg2: '#FFE0B2' },
  },
  history: {
    name: 'История',
    colors: { main: '#E65100', dark: '#BF360C', mid: '#F57C00', light: '#FF9800', lighter: '#FFB74D', bg1: '#FFF3E0', bg2: '#FFE0B2' },
  },
  geography: {
    name: 'География',
    colors: { main: '#00838F', dark: '#006064', mid: '#0097A7', light: '#00ACC1', lighter: '#26C6DA', bg1: '#E0F7FA', bg2: '#B2EBF2' },
  },
  music: {
    name: 'Музыка',
    colors: { main: '#AD1457', dark: '#880E4F', mid: '#C2185B', light: '#E91E63', lighter: '#EC407A', bg1: '#FCE4EC', bg2: '#F8BBD0' },
  },
  art: {
    name: 'Изобразительное искусство',
    colors: { main: '#6A1B9A', dark: '#4A148C', mid: '#7B1FA2', light: '#8E24AA', lighter: '#AB47BC', bg1: '#F3E5F5', bg2: '#E1BEE7' },
  },
  pe: {
    name: 'Физическая культура',
    colors: { main: '#2E7D32', dark: '#1B5E20', mid: '#388E3C', light: '#43A047', lighter: '#66BB6A', bg1: '#E8F5E9', bg2: '#C8E6C9' },
  },
  tech: {
    name: 'Технология',
    colors: { main: '#4E342E', dark: '#3E2723', mid: '#5D4037', light: '#6D4C41', lighter: '#8D6E63', bg1: '#EFEBE9', bg2: '#D7CCC8' },
  },
  informatics: {
    name: 'Информатика',
    colors: { main: '#00695C', dark: '#004D40', mid: '#00796B', light: '#00897B', lighter: '#26A69A', bg1: '#E0F2F1', bg2: '#B2DFDB' },
  },
  religion: {
    name: 'Основы религиозных культур',
    colors: { main: '#FF8F00', dark: '#FF6F00', mid: '#FFA000', light: '#FFB300', lighter: '#FFCA28', bg1: '#FFF8E1', bg2: '#FFECB3' },
  },
  projects: {
    name: 'Проектная деятельность',
    colors: { main: '#5D4037', dark: '#3E2723', mid: '#6D4C41', light: '#795548', lighter: '#8D6E63', bg1: '#EFEBE9', bg2: '#D7CCC8' },
  },
  world: {
    name: 'Окружающий мир',
    colors: { main: '#1565C0', dark: '#0D47A1', mid: '#1976D2', light: '#42A5F5', lighter: '#64B5F6', bg1: '#E3F2FD', bg2: '#BBDEFB' },
  },
};

// Subject-specific SVG illustration generators
const ILLUSTRATIONS = {
  math: {
    // Numeration
    numeration: (c) => `
      <line x1="40" y1="150" x2="220" y2="150" stroke="${c.main}" stroke-width="2"/>
      <circle cx="50" cy="150" r="5" fill="${c.main}"/><text x="50" y="168" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">0</text>
      <circle cx="80" cy="150" r="5" fill="${c.main}"/><text x="80" y="168" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">1</text>
      <circle cx="110" cy="150" r="5" fill="${c.main}"/><text x="110" y="168" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">2</text>
      <circle cx="140" cy="150" r="5" fill="${c.light}"/><text x="140" y="168" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">3</text>
      <circle cx="170" cy="150" r="5" fill="${c.light}"/><text x="170" y="168" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">4</text>
      <circle cx="200" cy="150" r="5" fill="${c.lighter}"/><text x="200" y="168" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">5</text>
      <text x="130" y="185" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle">1, 2, 3, 4, 5 ...</text>`,
    // Place values
    placeValues: (c) => `
      <rect x="40" y="115" width="42" height="45" rx="4" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>
      <text x="61" y="143" font-family="Arial" font-size="20" fill="${c.main}" text-anchor="middle" font-weight="bold">3</text>
      <text x="61" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Тыс.</text>
      <rect x="90" y="115" width="42" height="45" rx="4" fill="${c.light}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>
      <text x="111" y="143" font-family="Arial" font-size="20" fill="${c.main}" text-anchor="middle" font-weight="bold">5</text>
      <text x="111" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Сот.</text>
      <rect x="140" y="115" width="42" height="45" rx="4" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>
      <text x="161" y="143" font-family="Arial" font-size="20" fill="${c.main}" text-anchor="middle" font-weight="bold">8</text>
      <text x="161" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Дес.</text>
      <rect x="190" y="115" width="42" height="45" rx="4" fill="${c.light}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>
      <text x="211" y="143" font-family="Arial" font-size="20" fill="${c.main}" text-anchor="middle" font-weight="bold">7</text>
      <text x="211" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Ед.</text>
      <text x="130" y="190" font-family="Arial" font-size="13" fill="${c.main}" text-anchor="middle" font-weight="bold">3587</text>`,
    // Operations
    operations: (c, op) => `
      <rect x="40" y="120" width="70" height="50" rx="6" fill="${c.main}" opacity="0.1" stroke="${c.main}" stroke-width="1"/>
      <text x="75" y="142" font-family="Arial" font-size="14" fill="${c.main}" text-anchor="middle" font-weight="bold">${op || '+'}</text>
      <rect x="120" y="120" width="70" height="50" rx="6" fill="${c.light}" opacity="0.1" stroke="${c.light}" stroke-width="1"/>
      <text x="155" y="142" font-family="Arial" font-size="14" fill="${c.main}" text-anchor="middle" font-weight="bold">=</text>
      <rect x="200" y="120" width="40" height="50" rx="6" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <text x="220" y="150" font-family="Arial" font-size="18" fill="${c.main}" text-anchor="middle" font-weight="bold">?</text>`,
    // Fractions
    fractions: (c) => `
      <circle cx="80" cy="155" r="35" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="2"/>
      <path d="M80,120 A35,35 0 0,1 110,170 L80,155 Z" fill="${c.main}" opacity="0.35"/>
      <text x="80" y="160" font-family="Arial" font-size="12" fill="${c.main}" text-anchor="middle" font-weight="bold">1/2</text>
      <circle cx="180" cy="155" r="35" fill="${c.light}" opacity="0.12" stroke="${c.light}" stroke-width="2"/>
      <path d="M180,120 A35,35 0 0,1 196,185 L180,155 Z" fill="${c.light}" opacity="0.35"/>
      <path d="M196,185 A35,35 0 0,1 180,190 L180,155 Z" fill="${c.light}" opacity="0.25"/>
      <text x="180" y="160" font-family="Arial" font-size="12" fill="${c.main}" text-anchor="middle" font-weight="bold">1/3</text>`,
    // Geometry
    geometry: (c) => `
      <rect x="40" y="125" width="50" height="35" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="2"/>
      <text x="65" y="175" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">Прямоуг.</text>
      <polygon points="140,125 170,160 110,160" fill="${c.light}" opacity="0.15" stroke="${c.main}" stroke-width="2"/>
      <text x="140" y="175" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">Треуг.</text>
      <circle cx="215" cy="145" r="22" fill="${c.lighter}" opacity="0.15" stroke="${c.main}" stroke-width="2"/>
      <text x="215" y="175" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">Круг</text>`,
    // 3D shapes
    shapes3d: (c) => `
      <rect x="40" y="130" width="35" height="35" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="50" y="120" width="35" height="35" fill="${c.light}" opacity="0.08" stroke="${c.main}" stroke-width="1"/>
      <line x1="40" y1="130" x2="50" y2="120" stroke="${c.main}" stroke-width="1"/>
      <line x1="75" y1="130" x2="85" y2="120" stroke="${c.main}" stroke-width="1"/>
      <line x1="75" y1="165" x2="85" y2="155" stroke="${c.main}" stroke-width="1"/>
      <text x="60" y="185" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Куб</text>
      <ellipse cx="170" cy="155" rx="25" ry="10" fill="${c.light}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="145" y="125" width="50" height="30" fill="${c.main}" opacity="0.08" stroke="${c.main}" stroke-width="1.5"/>
      <ellipse cx="170" cy="125" rx="25" ry="10" fill="${c.lighter}" opacity="0.15" stroke="${c.main}" stroke-width="1.5"/>
      <text x="170" y="185" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Цилиндр</text>`,
    // Units
    units: (c) => `
      <rect x="35" y="120" width="55" height="20" rx="3" fill="${c.main}" opacity="0.15"/>
      <text x="62" y="134" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">мм</text>
      <rect x="35" y="145" width="70" height="20" rx="3" fill="${c.light}" opacity="0.15"/>
      <text x="70" y="159" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">см</text>
      <rect x="35" y="170" width="85" height="20" rx="3" fill="${c.main}" opacity="0.15"/>
      <text x="77" y="184" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">дм</text>
      <rect x="35" y="195" width="100" height="20" rx="3" fill="${c.light}" opacity="0.2"/>
      <text x="85" y="209" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle" font-weight="bold">м</text>
      <rect x="35" y="220" width="120" height="20" rx="3" fill="${c.main}" opacity="0.25"/>
      <text x="95" y="234" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle" font-weight="bold">км</text>`,
    // Motion problems
    motion: (c) => `
      <line x1="40" y1="170" x2="220" y2="170" stroke="${c.main}" stroke-width="2" stroke-dasharray="5,3"/>
      <polygon points="40,170 50,165 50,175" fill="${c.main}"/>
      <rect x="80" y="155" width="30" height="15" rx="3" fill="${c.main}" opacity="0.3"/>
      <circle cx="87" cy="170" r="5" fill="${c.dark}"/><circle cx="103" cy="170" r="5" fill="${c.dark}"/>
      <text x="80" y="148" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">v = 60</text>
      <text x="40" y="190" font-family="Arial" font-size="8" fill="${c.main}">A</text>
      <text x="215" y="190" font-family="Arial" font-size="8" fill="${c.main}">B</text>
      <text x="130" y="165" font-family="Arial" font-size="8" fill="${c.light}">S = v x t</text>`,
  },

  russian: {
    sentence: (c) => `
      <rect x="40" y="120" width="180" height="24" rx="4" fill="white" stroke="${c.main}" stroke-width="1"/>
      <text x="50" y="137" font-family="Arial" font-size="10" fill="${c.dark}" font-weight="bold">Подлежащее</text>
      <line x1="130" y1="120" x2="130" y2="144" stroke="${c.main}" stroke-width="1.5"/>
      <text x="170" y="137" font-family="Arial" font-size="10" fill="${c.mid}" font-weight="bold">Сказуемое</text>
      <line x1="40" y1="155" x2="220" y2="155" stroke="${c.main}" stroke-width="1" stroke-dasharray="3,2"/>
      <rect x="40" y="162" width="80" height="18" rx="3" fill="${c.main}" opacity="0.12"/>
      <text x="80" y="175" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">Второстепенные</text>
      <rect x="130" y="162" width="90" height="18" rx="3" fill="${c.light}" opacity="0.12"/>
      <text x="175" y="175" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">Обстоятельство</text>`,
    wordParts: (c) => `
      <rect x="35" y="130" width="45" height="35" rx="4" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <text x="57" y="152" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle" font-weight="bold">Корень</text>
      <rect x="85" y="130" width="40" height="35" rx="4" fill="${c.light}" opacity="0.2" stroke="${c.light}" stroke-width="1.5"/>
      <text x="105" y="152" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">Прист.</text>
      <rect x="130" y="130" width="40" height="35" rx="4" fill="${c.mid}" opacity="0.15" stroke="${c.mid}" stroke-width="1.5"/>
      <text x="150" y="152" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">Суфф.</text>
      <rect x="175" y="130" width="45" height="35" rx="4" fill="${c.lighter}" opacity="0.2" stroke="${c.lighter}" stroke-width="1.5"/>
      <text x="197" y="152" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle" font-weight="bold">Оконч.</text>
      <text x="130" y="185" font-family="Arial" font-size="10" fill="${c.dark}" text-anchor="middle">пре-ход-и-ть</text>`,
    partsOfSpeech: (c) => `
      <rect x="35" y="120" width="60" height="50" rx="5" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1.5"/>
      <text x="65" y="142" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">Сущ.</text>
      <text x="65" y="158" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">кто? что?</text>
      <rect x="102" y="120" width="60" height="50" rx="5" fill="${c.light}" opacity="0.15" stroke="${c.light}" stroke-width="1.5"/>
      <text x="132" y="142" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">Прил.</text>
      <text x="132" y="158" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">какой?</text>
      <rect x="169" y="120" width="60" height="50" rx="5" fill="${c.mid}" opacity="0.15" stroke="${c.mid}" stroke-width="1.5"/>
      <text x="199" y="142" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">Глагол</text>
      <text x="199" y="158" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">что делать?</text>`,
    spelling: (c) => `
      <text x="130" y="130" font-family="Arial" font-size="22" fill="${c.main}" text-anchor="middle" font-weight="bold">О / А</text>
      <line x1="70" y1="140" x2="190" y2="140" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="40" y="150" width="80" height="22" rx="3" fill="${c.main}" opacity="0.15"/>
      <text x="80" y="165" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle">Проверяй</text>
      <rect x="130" y="150" width="80" height="22" rx="3" fill="${c.light}" opacity="0.15"/>
      <text x="170" y="165" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle">Подбирай</text>
      <text x="130" y="192" font-family="Arial" font-size="8" fill="#555" text-anchor="middle">в_да - в_ды</text>`,
  },

  literature: {
    book: (c) => `
      <path d="M50,120 L110,110 L110,250 L50,260 Z" fill="#FFFDE7" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M110,110 L170,120 L170,260 L110,250 Z" fill="#FFF9C4" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="58" y1="135" x2="100" y2="132" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="58" y1="150" x2="100" y2="147" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="58" y1="165" x2="100" y2="162" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="58" y1="180" x2="100" y2="177" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="58" y1="195" x2="100" y2="192" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="135" x2="162" y2="138" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="150" x2="162" y2="153" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="165" x2="162" y2="168" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="180" x2="162" y2="183" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="195" x2="162" y2="198" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <path d="M162,130 L185,108 Q190,103 185,110 L165,133" fill="${c.light}" opacity="0.3"/>`,
    heroShield: (c) => `
      <path d="M110,115 L150,115 L155,120 L155,175 L130,195 L105,175 L105,120 Z" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="2"/>
      <line x1="130" y1="125" x2="130" y2="185" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="110" y1="150" x2="150" y2="150" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="130" cy="140" r="12" fill="${c.light}" opacity="0.2" stroke="${c.main}" stroke-width="1"/>
      <text x="130" y="144" font-family="Arial" font-size="10" fill="${c.main}" text-anchor="middle" font-weight="bold">P</text>`,
    author: (c) => `
      <circle cx="100" cy="135" r="18" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M82,135 Q100,125 118,135" fill="${c.dark}" opacity="0.1"/>
      <circle cx="93" cy="132" r="2" fill="${c.main}"/><circle cx="107" cy="132" r="2" fill="${c.main}"/>
      <path d="M94,140 Q100,146 106,140" fill="none" stroke="${c.main}" stroke-width="1"/>
      <path d="M75,170 Q88,155 100,160 Q112,155 125,170" fill="${c.mid}" opacity="0.15" stroke="${c.mid}" stroke-width="1"/>
      <text x="100" y="195" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle" font-weight="bold">Автор</text>
      <path d="M140,130 L170,120 L170,180 L140,190 Z" fill="#FFFDE7" stroke="${c.main}" stroke-width="1"/>
      <line x1="146" y1="140" x2="164" y2="137" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="146" y1="152" x2="164" y2="149" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="146" y1="164" x2="164" y2="161" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>`,
  },

  nature: {
    climate: (c) => `
      <circle cx="80" cy="140" r="22" fill="#FDD835" opacity="0.4" stroke="#F9A825" stroke-width="1.5"/>
      <line x1="80" y1="110" x2="80" y2="100" stroke="#F9A825" stroke-width="2"/>
      <line x1="80" y1="170" x2="80" y2="180" stroke="#F9A825" stroke-width="2"/>
      <line x1="50" y1="140" x2="40" y2="140" stroke="#F9A825" stroke-width="2"/>
      <line x1="110" y1="140" x2="120" y2="140" stroke="#F9A825" stroke-width="2"/>
      <path d="M140,120 Q150,110 160,120 Q170,110 180,120" fill="none" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M140,140 Q150,130 160,140 Q170,130 180,140" fill="none" stroke="${c.main}" stroke-width="1.5" opacity="0.7"/>
      <path d="M140,160 Q150,150 160,160 Q170,150 180,160" fill="none" stroke="${c.main}" stroke-width="1.5" opacity="0.5"/>
      <rect x="190" y="130" width="30" height="35" rx="2" fill="${c.light}" opacity="0.2" stroke="${c.main}" stroke-width="1"/>
      <line x1="195" y1="140" x2="215" y2="140" stroke="${c.main}" stroke-width="1"/>
      <line x1="195" y1="150" x2="215" y2="150" stroke="${c.main}" stroke-width="1"/>`,
    ecosystem: (c) => `
      <path d="M50,190 L70,140 L90,190 Z" fill="${c.mid}" opacity="0.3" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="65" y="190" width="10" height="15" fill="${c.dark}" opacity="0.3"/>
      <path d="M120,190 L145,120 L170,190 Z" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="138" y="190" width="14" height="15" fill="${c.dark}" opacity="0.3"/>
      <ellipse cx="90" cy="175" rx="12" ry="8" fill="${c.lighter}" opacity="0.3"/>
      <circle cx="160" cy="170" r="6" fill="${c.lighter}" opacity="0.3"/>
      <path d="M40,205 L180,205" stroke="${c.main}" stroke-width="1.5"/>
      <text x="110" y="220" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">Экосистема</text>`,
    bacteria: (c) => `
      <ellipse cx="70" cy="150" rx="18" ry="10" fill="${c.light}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="70" cy="150" r="5" fill="${c.main}" opacity="0.25"/>
      <ellipse cx="130" cy="140" rx="12" ry="16" fill="${c.mid}" opacity="0.15" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="130" cy="140" r="4" fill="${c.main}" opacity="0.25"/>
      <path d="M155,145 Q165,135 175,140 Q185,130 195,145" fill="none" stroke="${c.main}" stroke-width="2"/>
      <circle cx="155" cy="145" r="4" fill="${c.main}" opacity="0.2"/>
      <circle cx="195" cy="145" r="4" fill="${c.main}" opacity="0.2"/>`,
    mushroom: (c) => `
      <path d="M60,175 Q60,140 90,135 Q120,140 120,175 Z" fill="${c.mid}" opacity="0.3" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="82" y="175" width="16" height="25" rx="3" fill="#FFECB3" stroke="${c.main}" stroke-width="1"/>
      <path d="M140,175 Q140,145 165,140 Q190,145 190,175 Z" fill="${c.light}" opacity="0.3" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="158" y="175" width="14" height="22" rx="3" fill="#FFECB3" stroke="${c.main}" stroke-width="1"/>
      <circle cx="75" cy="155" r="3" fill="white" opacity="0.5"/>
      <circle cx="95" cy="148" r="2" fill="white" opacity="0.5"/>
      <circle cx="105" cy="160" r="2.5" fill="white" opacity="0.5"/>`,
    plant: (c) => `
      <line x1="90" y1="210" x2="90" y2="140" stroke="${c.dark}" stroke-width="3"/>
      <path d="M90,160 Q70,150 60,160 Q70,170 90,160" fill="${c.mid}" opacity="0.3" stroke="${c.main}" stroke-width="1"/>
      <path d="M90,150 Q110,140 120,150 Q110,160 90,150" fill="${c.main}" opacity="0.25" stroke="${c.main}" stroke-width="1"/>
      <path d="M90,175 Q65,165 55,175 Q65,185 90,175" fill="${c.mid}" opacity="0.25" stroke="${c.main}" stroke-width="1"/>
      <circle cx="90" cy="130" r="12" fill="#F48FB1" opacity="0.3" stroke="${c.main}" stroke-width="1"/>
      <circle cx="90" cy="130" r="5" fill="#FFD54F" opacity="0.4"/>`,
    animal: (c) => `
      <ellipse cx="80" cy="170" rx="25" ry="15" fill="${c.mid}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="60" cy="158" r="10" fill="${c.light}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="57" cy="155" r="2" fill="${c.main}"/>
      <path d="M53,148 L50,138 L58,145" fill="${c.mid}" opacity="0.3" stroke="${c.main}" stroke-width="0.5"/>
      <path d="M63,148 L66,138 L60,145" fill="${c.mid}" opacity="0.3" stroke="${c.main}" stroke-width="0.5"/>
      <ellipse cx="160" cy="165" rx="30" ry="18" fill="${c.lighter}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="140" cy="152" r="12" fill="${c.light}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="137" cy="149" r="2" fill="${c.main}"/>
      <path d="M148,148 Q160,135 155,155" fill="none" stroke="${c.main}" stroke-width="1.5"/>`,
  },

  english: {
    greetings: (c) => `
      <rect x="50" y="115" width="120" height="35" rx="8" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <text x="110" y="138" font-family="Arial" font-size="14" fill="${c.main}" text-anchor="middle" font-weight="bold">Hello!</text>
      <rect x="50" y="160" width="120" height="35" rx="8" fill="${c.light}" opacity="0.12" stroke="${c.light}" stroke-width="1.5"/>
      <text x="110" y="183" font-family="Arial" font-size="14" fill="${c.main}" text-anchor="middle" font-weight="bold">Goodbye!</text>
      <path d="M180,130 L195,120 L210,130 L210,160 L195,170 L180,160 Z" fill="${c.main}" opacity="0.08" stroke="${c.main}" stroke-width="1"/>`,
    words: (c) => `
      <rect x="40" y="120" width="170" height="25" rx="4" fill="${c.main}" opacity="0.1" stroke="${c.main}" stroke-width="1"/>
      <text x="50" y="137" font-family="Arial" font-size="10" fill="${c.main}" font-weight="bold">red</text>
      <rect x="100" y="122" width="15" height="20" rx="2" fill="#E53935" opacity="0.5"/>
      <text x="130" y="137" font-family="Arial" font-size="9" fill="#777">красный</text>
      <rect x="40" y="152" width="170" height="25" rx="4" fill="${c.light}" opacity="0.1" stroke="${c.light}" stroke-width="1"/>
      <text x="50" y="169" font-family="Arial" font-size="10" fill="${c.main}" font-weight="bold">blue</text>
      <rect x="100" y="154" width="15" height="20" rx="2" fill="#1565C0" opacity="0.5"/>
      <text x="130" y="169" font-family="Arial" font-size="9" fill="#777">синий</text>
      <rect x="40" y="184" width="170" height="25" rx="4" fill="${c.main}" opacity="0.1" stroke="${c.main}" stroke-width="1"/>
      <text x="50" y="201" font-family="Arial" font-size="10" fill="${c.main}" font-weight="bold">green</text>
      <rect x="100" y="186" width="15" height="20" rx="2" fill="#2E7D32" opacity="0.5"/>
      <text x="130" y="201" font-family="Arial" font-size="9" fill="#777">зелёный</text>`,
    flag: (c) => `
      <rect x="60" y="110" width="120" height="25" fill="#1565C0" opacity="0.7"/>
      <rect x="60" y="135" width="120" height="25" fill="#FFFFFF" opacity="0.8"/>
      <rect x="60" y="160" width="120" height="25" fill="#D32F2F" opacity="0.7"/>
      <rect x="60" y="110" width="50" height="75" fill="#0D47A1" opacity="0.5"/>
      <text x="130" y="210" font-family="Arial" font-size="10" fill="${c.main}" text-anchor="middle" font-weight="bold">English</text>`,
  },

  history: {
    timeline: (c) => `
      <line x1="40" y1="150" x2="220" y2="150" stroke="${c.main}" stroke-width="2"/>
      <polygon points="220,150 215,145 215,155" fill="${c.main}"/>
      <circle cx="60" cy="150" r="5" fill="${c.dark}"/>
      <text x="60" y="140" font-family="Arial" font-size="7" fill="${c.dark}" text-anchor="middle">862</text>
      <circle cx="100" cy="150" r="5" fill="${c.main}"/>
      <text x="100" y="140" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">988</text>
      <circle cx="150" cy="150" r="5" fill="${c.mid}"/>
      <text x="150" y="140" font-family="Arial" font-size="7" fill="${c.mid}" text-anchor="middle">1147</text>
      <circle cx="190" cy="150" r="5" fill="${c.light}"/>
      <text x="190" y="140" font-family="Arial" font-size="7" fill="${c.light}" text-anchor="middle">1380</text>
      <text x="60" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Русь</text>
      <text x="100" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Крещение</text>
      <text x="150" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Москва</text>
      <text x="190" y="168" font-family="Arial" font-size="7" fill="#777" text-anchor="middle">Куликово</text>`,
    kremlin: (c) => `
      <rect x="60" y="170" width="100" height="40" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M60,170 L70,150 L80,170" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1"/>
      <path d="M90,170 L100,145 L110,170" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1"/>
      <path d="M120,170 L130,150 L140,170" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1"/>
      <path d="M150,170 L160,155 L160,170" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1"/>
      <rect x="85" y="185" width="25" height="25" rx="8" fill="${c.mid}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>
      <rect x="115" y="185" width="20" height="20" rx="2" fill="${c.light}" opacity="0.1" stroke="${c.main}" stroke-width="1"/>`,
    sword: (c) => `
      <line x1="110" y1="110" x2="110" y2="190" stroke="${c.main}" stroke-width="3"/>
      <line x1="90" y1="140" x2="130" y2="140" stroke="${c.mid}" stroke-width="3"/>
      <circle cx="110" cy="110" r="4" fill="${c.light}"/>
      <rect x="105" y="190" width="10" height="15" rx="2" fill="${c.dark}" opacity="0.3"/>
      <line x1="108" y1="205" x2="112" y2="205" stroke="${c.main}" stroke-width="2"/>
      <text x="110" y="225" font-family="Arial" font-size="8" fill="${c.main}" text-anchor="middle">Богатырь</text>`,
    church: (c) => `
      <rect x="70" y="160" width="70" height="50" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M70,160 L105,125 L140,160" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="105" y1="125" x2="105" y2="108" stroke="${c.main}" stroke-width="2"/>
      <path d="M100,108 L105,100 L110,108" fill="${c.light}" opacity="0.4" stroke="${c.main}" stroke-width="1"/>
      <circle cx="105" cy="110" r="3" fill="${c.light}"/>
      <rect x="90" y="180" width="30" height="30" rx="10" fill="${c.mid}" opacity="0.1" stroke="${c.mid}" stroke-width="1"/>
      <rect x="95" y="185" width="20" height="25" rx="6" fill="${c.lighter}" opacity="0.15"/>`,
  },

  geography: {
    globe: (c) => `
      <circle cx="100" cy="165" r="45" fill="${c.light}" opacity="0.15" stroke="${c.main}" stroke-width="2"/>
      <ellipse cx="100" cy="165" rx="45" ry="10" fill="none" stroke="${c.main}" stroke-width="0.7" stroke-dasharray="3,2"/>
      <line x1="100" y1="120" x2="100" y2="210" stroke="${c.main}" stroke-width="0.7" stroke-dasharray="3,2"/>
      <path d="M70,145 Q85,138 95,148 Q105,140 120,148" fill="#2E7D32" opacity="0.4"/>
      <path d="M75,170 Q90,165 100,175 Q115,168 125,172" fill="#2E7D32" opacity="0.35"/>
      <text x="100" y="225" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle">Россия</text>`,
    map: (c) => `
      <rect x="40" y="115" width="160" height="100" rx="4" fill="#E8F5E9" opacity="0.3" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M60,135 L100,130 L140,135 L150,155 L130,175 L80,180 L55,160 Z" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="110" cy="150" r="4" fill="#D32F2F" opacity="0.6"/>
      <text x="110" y="145" font-family="Arial" font-size="7" fill="${c.dark}" text-anchor="middle">Москва</text>
      <path d="M75,160 Q85,155 95,165" fill="none" stroke="#1565C0" stroke-width="1.5" opacity="0.5"/>`,
    river: (c) => `
      <path d="M40,140 Q70,130 100,150 Q130,170 160,155 Q190,140 220,150" fill="none" stroke="#1565C0" stroke-width="3" opacity="0.5"/>
      <path d="M40,145 Q70,135 100,155 Q130,175 160,160 Q190,145 220,155" fill="none" stroke="#42A5F5" stroke-width="2" opacity="0.3"/>
      <circle cx="80" cy="130" r="5" fill="${c.main}" opacity="0.3"/>
      <text x="80" y="125" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Исток</text>
      <polygon points="220,150 215,145 215,155" fill="#1565C0" opacity="0.5"/>`,
    mountain: (c) => `
      <path d="M40,200 L100,120 L160,200" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="2"/>
      <path d="M85,135 L100,120 L115,135" fill="white" opacity="0.5"/>
      <path d="M100,200 L160,140 L220,200" fill="${c.mid}" opacity="0.12" stroke="${c.mid}" stroke-width="1.5"/>
      <path d="M148,152 L160,140 L172,152" fill="white" opacity="0.4"/>
      <line x1="40" y1="200" x2="220" y2="200" stroke="${c.main}" stroke-width="1"/>`,
  },

  music: {
    notes: (c) => `
      <line x1="40" y1="120" x2="220" y2="120" stroke="${c.main}" stroke-width="0.6" opacity="0.25"/>
      <line x1="40" y1="130" x2="220" y2="130" stroke="${c.main}" stroke-width="0.6" opacity="0.25"/>
      <line x1="40" y1="140" x2="220" y2="140" stroke="${c.main}" stroke-width="0.6" opacity="0.25"/>
      <line x1="40" y1="150" x2="220" y2="150" stroke="${c.main}" stroke-width="0.6" opacity="0.25"/>
      <line x1="40" y1="160" x2="220" y2="160" stroke="${c.main}" stroke-width="0.6" opacity="0.25"/>
      <ellipse cx="70" cy="148" rx="7" ry="5" fill="${c.main}" opacity="0.5" transform="rotate(-15,70,148)"/>
      <line x1="77" y1="148" x2="77" y2="115" stroke="${c.main}" stroke-width="1.5"/>
      <ellipse cx="130" cy="135" rx="7" ry="5" fill="${c.mid}" opacity="0.5" transform="rotate(-15,130,135)"/>
      <line x1="137" y1="135" x2="137" y2="102" stroke="${c.mid}" stroke-width="1.5"/>
      <ellipse cx="180" cy="142" rx="7" ry="5" fill="${c.light}" opacity="0.5" transform="rotate(-15,180,142)"/>
      <line x1="187" y1="142" x2="187" y2="109" stroke="${c.light}" stroke-width="1.5"/>`,
    violin: (c) => `
      <ellipse cx="100" cy="160" rx="22" ry="30" fill="${c.mid}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <ellipse cx="100" cy="130" rx="16" ry="20" fill="${c.light}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="100" y1="110" x2="100" y2="85" stroke="${c.dark}" stroke-width="2"/>
      <line x1="80" y1="155" x2="120" y2="155" stroke="${c.main}" stroke-width="0.5" opacity="0.5"/>
      <line x1="80" y1="160" x2="120" y2="160" stroke="${c.main}" stroke-width="0.5" opacity="0.5"/>
      <line x1="80" y1="165" x2="120" y2="165" stroke="${c.main}" stroke-width="0.5" opacity="0.5"/>
      <text x="100" y="210" font-family="Arial" font-size="9" fill="${c.main}" text-anchor="middle" font-weight="bold">Скрипка</text>`,
    piano: (c) => `
      <rect x="40" y="120" width="180" height="80" rx="3" fill="white" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="40" y="120" width="22" height="50" fill="white" stroke="${c.main}" stroke-width="1"/>
      <rect x="62" y="120" width="16" height="30" fill="${c.dark}" opacity="0.7"/>
      <rect x="78" y="120" width="22" height="50" fill="white" stroke="${c.main}" stroke-width="1"/>
      <rect x="100" y="120" width="16" height="30" fill="${c.dark}" opacity="0.7"/>
      <rect x="116" y="120" width="22" height="50" fill="white" stroke="${c.main}" stroke-width="1"/>
      <rect x="138" y="120" width="16" height="30" fill="${c.dark}" opacity="0.7"/>
      <rect x="154" y="120" width="22" height="50" fill="white" stroke="${c.main}" stroke-width="1"/>
      <rect x="176" y="120" width="22" height="50" fill="white" stroke="${c.main}" stroke-width="1"/>
      <rect x="176" y="120" width="16" height="30" fill="${c.dark}" opacity="0.7"/>`,
  },

  art: {
    palette: (c) => `
      <ellipse cx="110" cy="155" rx="55" ry="35" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="80" cy="140" r="8" fill="#E53935" opacity="0.6"/><circle cx="100" cy="132" r="8" fill="#FDD835" opacity="0.6"/>
      <circle cx="125" cy="132" r="8" fill="#1565C0" opacity="0.6"/><circle cx="140" cy="145" r="8" fill="#2E7D32" opacity="0.6"/>
      <circle cx="85" cy="165" r="6" fill="#FF9800" opacity="0.5"/>
      <ellipse cx="120" cy="165" rx="10" ry="8" fill="white" opacity="0.5"/>`,
    painting: (c) => `
      <rect x="50" y="110" width="120" height="90" rx="3" fill="white" stroke="${c.main}" stroke-width="2"/>
      <rect x="55" y="115" width="110" height="80" fill="#E8F5E9" opacity="0.3"/>
      <path d="M55,170 Q80,140 110,160 Q130,145 165,170 L165,195 L55,195 Z" fill="#2E7D32" opacity="0.2"/>
      <circle cx="140" cy="135" r="10" fill="#FDD835" opacity="0.4"/>
      <rect x="45" y="200" width="130" height="6" rx="1" fill="${c.dark}" opacity="0.2"/>`,
    easel: (c) => `
      <line x1="90" y1="100" x2="70" y2="210" stroke="${c.dark}" stroke-width="2"/>
      <line x1="130" y1="100" x2="150" y2="210" stroke="${c.dark}" stroke-width="2"/>
      <line x1="110" y1="100" x2="110" y2="210" stroke="${c.dark}" stroke-width="2"/>
      <rect x="75" y="105" width="70" height="55" fill="white" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="110" cy="130" r="15" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>
      <path d="M85,120 Q100,110 110,120 Q120,110 135,120" fill="${c.light}" opacity="0.2"/>`,
  },

  pe: {
    running: (c) => `
      <circle cx="80" cy="125" r="10" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="80" y1="135" x2="80" y2="165" stroke="${c.main}" stroke-width="2"/>
      <line x1="80" y1="145" x2="65" y2="155" stroke="${c.main}" stroke-width="2"/>
      <line x1="80" y1="145" x2="95" y2="152" stroke="${c.main}" stroke-width="2"/>
      <line x1="80" y1="165" x2="68" y2="190" stroke="${c.main}" stroke-width="2"/>
      <line x1="80" y1="165" x2="95" y2="188" stroke="${c.main}" stroke-width="2"/>
      <line x1="40" y1="195" x2="200" y2="195" stroke="${c.main}" stroke-width="1" stroke-dasharray="5,3"/>`,
    ball: (c) => `
      <circle cx="110" cy="155" r="35" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="2"/>
      <path d="M75,155 Q110,130 145,155" fill="none" stroke="${c.mid}" stroke-width="1.5"/>
      <path d="M75,155 Q110,180 145,155" fill="none" stroke="${c.light}" stroke-width="1.5"/>
      <line x1="110" y1="120" x2="110" y2="190" stroke="${c.main}" stroke-width="1" opacity="0.3"/>`,
    skiing: (c) => `
      <circle cx="90" cy="120" r="8" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="90" y1="128" x2="90" y2="165" stroke="${c.main}" stroke-width="2"/>
      <line x1="90" y1="140" x2="75" y2="155" stroke="${c.main}" stroke-width="2"/>
      <line x1="75" y1="155" x2="70" y2="148" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="90" y1="140" x2="110" y2="150" stroke="${c.main}" stroke-width="2"/>
      <line x1="90" y1="165" x2="80" y2="190" stroke="${c.main}" stroke-width="2"/>
      <line x1="80" y1="190" x2="120" y2="192" stroke="${c.main}" stroke-width="2.5"/>
      <line x1="65" y1="192" x2="130" y2="195" stroke="${c.dark}" stroke-width="2" opacity="0.5"/>`,
  },

  tech: {
    scissors: (c) => `
      <circle cx="75" cy="175" r="12" fill="none" stroke="${c.main}" stroke-width="2"/>
      <circle cx="105" cy="175" r="12" fill="none" stroke="${c.main}" stroke-width="2"/>
      <line x1="75" y1="163" x2="105" y2="125" stroke="${c.main}" stroke-width="2.5"/>
      <line x1="105" y1="163" x2="75" y2="125" stroke="${c.main}" stroke-width="2.5"/>`,
    craft: (c) => `
      <rect x="50" y="120" width="60" height="80" rx="4" fill="#FFECB3" opacity="0.4" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M55,130 L80,130 L80,190 L55,190 Z" fill="${c.main}" opacity="0.08"/>
      <line x1="65" y1="135" x2="65" y2="185" stroke="${c.main}" stroke-width="0.5" stroke-dasharray="2,2"/>
      <rect x="120" y="135" width="70" height="55" rx="4" fill="${c.light}" opacity="0.1" stroke="${c.main}" stroke-width="1.5"/>
      <polygon points="155,135 175,160 155,185 135,160" fill="${c.mid}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>`,
    sewing: (c) => `
      <line x1="50" y1="170" x2="200" y2="140" stroke="${c.main}" stroke-width="1.5" stroke-dasharray="4,3"/>
      <circle cx="65" cy="167" r="3" fill="${c.light}"/>
      <line x1="50" y1="165" x2="45" y2="155" stroke="${c.dark}" stroke-width="1.5"/>
      <line x1="45" y1="155" x2="55" y2="155" stroke="${c.dark}" stroke-width="1.5"/>
      <rect x="140" y="130" width="40" height="40" rx="2" fill="#FFECB3" opacity="0.3" stroke="${c.main}" stroke-width="1"/>
      <line x1="145" y1="145" x2="175" y2="145" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="145" y1="155" x2="175" y2="155" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>`,
  },

  informatics: {
    keyboard: (c) => `
      <rect x="40" y="130" width="180" height="60" rx="6" fill="${c.main}" opacity="0.1" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="48" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="64" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="80" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="96" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="112" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="128" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="144" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="160" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="176" y="138" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="192" y="138" width="20" height="12" rx="2" fill="${c.light}" opacity="0.2" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="48" y="156" width="16" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="68" y="156" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="84" y="156" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="100" y="156" width="60" height="12" rx="2" fill="${c.mid}" opacity="0.15" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="164" y="156" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>
      <rect x="180" y="156" width="12" height="12" rx="2" fill="white" stroke="${c.main}" stroke-width="0.8"/>`,
    screen: (c) => `
      <rect x="45" y="110" width="140" height="100" rx="6" fill="${c.main}" opacity="0.08" stroke="${c.main}" stroke-width="2"/>
      <rect x="55" y="120" width="120" height="70" rx="2" fill="${c.light}" opacity="0.1"/>
      <line x1="65" y1="135" x2="145" y2="135" stroke="${c.main}" stroke-width="0.8" opacity="0.3"/>
      <line x1="65" y1="148" x2="130" y2="148" stroke="${c.main}" stroke-width="0.8" opacity="0.3"/>
      <line x1="65" y1="161" x2="155" y2="161" stroke="${c.main}" stroke-width="0.8" opacity="0.3"/>
      <rect x="100" y="210" width="30" height="5" rx="1" fill="${c.main}" opacity="0.15"/>
      <line x1="115" y1="215" x2="115" y2="225" stroke="${c.main}" stroke-width="1.5"/>`,
    search: (c) => `
      <circle cx="110" cy="150" r="30" fill="none" stroke="${c.main}" stroke-width="2.5"/>
      <line x1="132" y1="172" x2="155" y2="195" stroke="${c.main}" stroke-width="3"/>
      <text x="110" y="155" font-family="Arial" font-size="18" fill="${c.main}" text-anchor="middle" opacity="0.3">?</text>`,
  },

  religion: {
    churchSmall: (c) => `
      <rect x="75" y="160" width="60" height="45" fill="${c.main}" opacity="0.12" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M75,160 L105,130 L135,160" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="105" y1="130" x2="105" y2="115" stroke="${c.main}" stroke-width="2"/>
      <path d="M100,115 L105,108 L110,115" fill="${c.light}" opacity="0.4" stroke="${c.main}" stroke-width="1"/>
      <circle cx="105" cy="117" r="3" fill="${c.light}"/>
      <rect x="92" y="180" width="26" height="25" rx="8" fill="${c.mid}" opacity="0.1" stroke="${c.mid}" stroke-width="1"/>`,
    candle: (c) => `
      <rect x="100" y="155" width="16" height="50" rx="2" fill="#FFECB3" stroke="${c.main}" stroke-width="1"/>
      <ellipse cx="108" cy="155" rx="6" ry="3" fill="#FFECB3" stroke="${c.main}" stroke-width="0.5"/>
      <line x1="108" y1="155" x2="108" y2="140" stroke="${c.dark}" stroke-width="1"/>
      <ellipse cx="108" cy="135" rx="5" ry="8" fill="#FDD835" opacity="0.5"/>
      <ellipse cx="108" cy="133" rx="3" ry="5" fill="#FFF9C4" opacity="0.7"/>
      <path d="M90,135 Q108,110 126,135" fill="none" stroke="${c.light}" stroke-width="0.5" opacity="0.3"/>`,
    bookHoly: (c) => `
      <path d="M60,125 L110,115 L110,215 L60,225 Z" fill="#FFF8E1" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M110,115 L160,125 L160,225 L110,215 Z" fill="#FFFDE7" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="68" y1="140" x2="100" y2="137" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="68" y1="155" x2="100" y2="152" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="68" y1="170" x2="100" y2="167" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="68" y1="185" x2="100" y2="182" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="140" x2="152" y2="143" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="155" x2="152" y2="158" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="170" x2="152" y2="173" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>
      <line x1="118" y1="185" x2="152" y2="188" stroke="${c.main}" stroke-width="0.5" opacity="0.3"/>`,
  },

  projects: {
    magnifier: (c) => `
      <circle cx="100" cy="145" r="28" fill="none" stroke="${c.main}" stroke-width="2.5"/>
      <line x1="120" y1="165" x2="145" y2="190" stroke="${c.main}" stroke-width="3"/>
      <text x="100" y="150" font-family="Arial" font-size="16" fill="${c.main}" text-anchor="middle" opacity="0.3">?</text>`,
    presentation: (c) => `
      <rect x="50" y="110" width="120" height="80" rx="4" fill="white" stroke="${c.main}" stroke-width="2"/>
      <rect x="55" y="115" width="110" height="55" fill="${c.main}" opacity="0.06"/>
      <rect x="60" y="120" width="40" height="8" rx="2" fill="${c.main}" opacity="0.2"/>
      <rect x="60" y="132" width="100" height="4" rx="1" fill="${c.main}" opacity="0.1"/>
      <rect x="60" y="140" width="80" height="4" rx="1" fill="${c.main}" opacity="0.1"/>
      <rect x="60" y="148" width="90" height="4" rx="1" fill="${c.main}" opacity="0.1"/>
      <circle cx="130" cy="130" r="12" fill="${c.light}" opacity="0.15" stroke="${c.main}" stroke-width="1"/>
      <rect x="100" y="190" width="20" height="10" rx="1" fill="${c.main}" opacity="0.15"/>
      <line x1="110" y1="200" x2="110" y2="210" stroke="${c.main}" stroke-width="1.5"/>`,
    tools: (c) => `
      <rect x="50" y="120" width="40" height="70" rx="3" fill="${c.main}" opacity="0.1" stroke="${c.main}" stroke-width="1.5"/>
      <rect x="55" y="125" width="30" height="20" rx="2" fill="${c.light}" opacity="0.15"/>
      <text x="70" y="139" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Данные</text>
      <rect x="100" y="120" width="40" height="70" rx="3" fill="${c.mid}" opacity="0.1" stroke="${c.mid}" stroke-width="1.5"/>
      <rect x="105" y="125" width="30" height="20" rx="2" fill="${c.light}" opacity="0.15"/>
      <text x="120" y="139" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Анализ</text>
      <rect x="150" y="120" width="40" height="70" rx="3" fill="${c.lighter}" opacity="0.1" stroke="${c.lighter}" stroke-width="1.5"/>
      <rect x="155" y="125" width="30" height="20" rx="2" fill="${c.light}" opacity="0.15"/>
      <text x="170" y="139" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Выводы</text>
      <path d="M90,155 L100,155" stroke="${c.main}" stroke-width="1" marker-end="url(#arrow)"/>
      <path d="M140,155 L150,155" stroke="${c.main}" stroke-width="1"/>`,
  },

  world: {
    natureZone: (c) => `
      <path d="M40,140 L60,120 L80,140 L100,120 L120,140 L140,120 L160,140 L180,120 L200,140" fill="none" stroke="${c.main}" stroke-width="2"/>
      <rect x="40" y="140" width="160" height="30" fill="${c.mid}" opacity="0.1"/>
      <text x="60" y="158" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Тундра</text>
      <text x="120" y="158" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Лес</text>
      <text x="180" y="158" font-family="Arial" font-size="7" fill="${c.main}" text-anchor="middle">Степь</text>
      <path d="M55,130 L60,118 L65,130" fill="#81D4FA" opacity="0.3"/>
      <path d="M115,130 L120,115 L125,130" fill="#2E7D32" opacity="0.2"/>
      <path d="M175,135 Q180,130 185,135" fill="#FDD835" opacity="0.2"/>`,
    humanBody: (c) => `
      <circle cx="110" cy="120" r="12" fill="${c.main}" opacity="0.15" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="110" y1="132" x2="110" y2="170" stroke="${c.main}" stroke-width="2"/>
      <line x1="110" y1="142" x2="90" y2="158" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="110" y1="142" x2="130" y2="158" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="110" y1="170" x2="95" y2="195" stroke="${c.main}" stroke-width="1.5"/>
      <line x1="110" y1="170" x2="125" y2="195" stroke="${c.main}" stroke-width="1.5"/>
      <circle cx="110" cy="155" r="8" fill="#D32F2F" opacity="0.15" stroke="#D32F2F" stroke-width="1"/>
      <text x="125" y="158" font-family="Arial" font-size="7" fill="#D32F2F">Сердце</text>`,
    water: (c) => `
      <path d="M60,160 Q80,140 100,160 Q120,140 140,160 Q160,140 180,160" fill="none" stroke="#1565C0" stroke-width="2.5" opacity="0.4"/>
      <path d="M50,170 Q70,150 90,170 Q110,150 130,170 Q150,150 170,170 Q190,150 210,170" fill="none" stroke="#42A5F5" stroke-width="1.5" opacity="0.25"/>
      <circle cx="150" cy="130" r="12" fill="#E3F2FD" stroke="#1565C0" stroke-width="1" opacity="0.5"/>
      <text x="150" y="133" font-family="Arial" font-size="7" fill="#1565C0" text-anchor="middle">H2O</text>`,
    recycling: (c) => `
      <path d="M80,140 L100,125 L120,140 L110,140 L110,170 L90,170 L90,140 Z" fill="${c.main}" opacity="0.2" stroke="${c.main}" stroke-width="1.5"/>
      <path d="M130,140 L150,125 L170,140 L160,140 L160,170 L140,170 L140,140 Z" fill="${c.light}" opacity="0.2" stroke="${c.light}" stroke-width="1.5"/>
      <path d="M80,175 Q110,195 140,175 Q170,195 200,175" fill="none" stroke="${c.main}" stroke-width="1.5" stroke-dasharray="3,2"/>
      <path d="M195,175 L200,170 L200,180 Z" fill="${c.main}"/>`,
  },
};

// Select which illustration function to use based on lesson title keywords
function getIllustration(subject, title, c) {
  const illus = ILLUSTRATIONS[subject];
  if (!illus) return ILLUSTRATIONS.math.numeration(c);

  const t = title.toLowerCase();
  const keys = Object.keys(illus);

  // Try to match by keyword
  if (t.includes('нумераци') || t.includes('чисел') || t.includes('ряд')) return illus.numeration ? illus.numeration(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('разряд') || t.includes('класс') || t.includes('состав') || t.includes('многознач')) return illus.placeValues ? illus.placeValues(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('склад') || t.includes('вычитан') || t.includes('действ')) return illus.operations ? illus.operations(c, t.includes('склад') ? '+' : '-') : illus[Object.keys(illus)[0]](c);
  if (t.includes('умнож')) return illus.operations ? illus.operations(c, '\u00D7') : illus[Object.keys(illus)[0]](c);
  if (t.includes('делен')) return illus.operations ? illus.operations(c, '\u00F7') : illus[Object.keys(illus)[0]](c);
  if (t.includes('дроб') || t.includes('дол')) return illus.fractions ? illus.fractions(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('геометр') || t.includes('фигур') || t.includes('площад')) return illus.geometry ? illus.geometry(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('тела') || t.includes('объём') || t.includes('объем')) return illus.shapes3d ? illus.shapes3d(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('единиц') || t.includes('величин') || t.includes('длин') || t.includes('масс') || t.includes('времен')) return illus.units ? illus.units(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('движен') || t.includes('задач') || t.includes('работ') || t.includes('цен') || t.includes('стоимост')) return illus.motion ? illus.motion(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('предложен')) return illus.sentence ? illus.sentence(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('корен') || t.includes('пристав') || t.includes('суффикс') || t.includes('окончан') || t.includes('слово')) return illus.wordParts ? illus.wordParts(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('существ') || t.includes('прилагат') || t.includes('глагол') || t.includes('местоим')) return illus.partsOfSpeech ? illus.partsOfSpeech(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('гласн') || t.includes('согласн') || t.includes('правопис') || t.includes('безударн') || t.includes('орфограф')) return illus.spelling ? illus.spelling(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('сказк')) return illus.book ? illus.book(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('былин') || t.includes('богатыр') || t.includes('илья') || t.includes('добрын') || t.includes('алёш') || t.includes('алеш')) return illus.heroShield ? illus.heroShield(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('пушкин') || t.includes('толст') || t.includes('чуковск') || t.includes('маршак') || t.includes('автор') || t.includes('писател')) return illus.author ? illus.author(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('климат') || t.includes('погод') || t.includes('сезон') || t.includes('времен год')) return illus.climate ? illus.climate(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('экосист') || t.includes('лес') || t.includes('водоём') || t.includes('водоем') || t.includes('природ')) return illus.ecosystem ? illus.ecosystem(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('бактер')) return illus.bacteria ? illus.bacteria(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('гриб')) return illus.mushroom ? illus.mushroom(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('растен')) return illus.plant ? illus.plant(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('животн') || t.includes('звер')) return illus.animal ? illus.animal(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('приветств') || t.includes('знакомств') || t.includes('представлен') || t.includes('вежлив')) return illus.greetings ? illus.greetings(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('цвет') || t.includes('числ') || t.includes('слов') || t.includes('семь') || t.includes('дом') || t.includes('город') || t.includes('продукт') || t.includes('транспорт') || t.includes('стран')) return illus.words ? illus.words(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('английск') || t.includes('англ')) return illus.flag ? illus.flag(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('русь') || t.includes('исток') || t.includes('князь') || t.includes('княж') || t.includes('игор') || t.includes('ольг') || t.includes('святослав') || t.includes('владимир') || t.includes('ярослав') || t.includes('монгол') || t.includes('куликов')) return illus.timeline ? illus.timeline(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('храм') || t.includes('церков') || t.includes('крещен') || t.includes('христиан')) return illus.church ? illus.church(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('культур') || t.includes('москов') || t.includes('кремл')) return illus.kremlin ? illus.kremlin(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('глоб') || t.includes('земл') || t.includes('карт') || t.includes('росси')) return illus.globe ? illus.globe(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('рек') || t.includes('озёр') || t.includes('озер') || t.includes('мор') || t.includes('водн')) return illus.river ? illus.river(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('гор') || t.includes('горо') || t.includes('столиц') || t.includes('субъект') || t.includes('миллион')) return illus.map ? illus.map(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('природн') || t.includes('зон') || t.includes('ископаем') || t.includes('охран')) return illus.mountain ? illus.mountain(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('нот') || t.includes('грамот') || t.includes('тембр') || t.includes('регистр')) return illus.notes ? illus.notes(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('инструмент') || t.includes('глинк') || t.includes('чайковск') || t.includes('римск') || t.includes('прокоф')) return illus.violin ? illus.violin(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('опера') || t.includes('балет') || t.includes('концерт') || t.includes('симфон') || t.includes('песн') || t.includes('романс')) return illus.piano ? illus.piano(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('живопись') || t.includes('натюрморт') || t.includes('портрет') || t.includes('пейзаж') || t.includes('цвет') || t.includes('художник')) return illus.palette ? illus.palette(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('музе') || t.includes('искусств') || t.includes('проект') || t.includes('компози') || illus === ILLUSTRATIONS.art) return illus.painting ? illus.painting(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('бег') || t.includes('прыжк') || t.includes('метан') || t.includes('строе') || t.includes('гимнаст') || t.includes('упражнен')) return illus.running ? illus.running(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('футбол') || t.includes('баскетбол') || t.includes('волейбол') || t.includes('игр')) return illus.ball ? illus.ball(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('лыж') || t.includes('коньк') || t.includes('зимн')) return illus.skiing ? illus.skiing(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('бумаг') || t.includes('вырезан') || t.includes('разметк') || t.includes('аппликац')) return illus.scissors ? illus.scissors(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('ткан') || t.includes('шв') || t.includes('пуговиц') || t.includes('игрушк')) return illus.sewing ? illus.sewing(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('модел') || t.includes('макет') || t.includes('пласт') || t.includes('глин') || t.includes('тесто') || t.includes('поделк') || t.includes('выставк')) return illus.craft ? illus.craft(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('клавиатур') || t.includes('печать') || t.includes('клавиш')) return illus.keyboard ? illus.keyboard(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('paint') || t.includes('редактор') || t.includes('рисован') || t.includes('графич') || t.includes('документ') || t.includes('текстов')) return illus.screen ? illus.screen(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('интернет') || t.includes('поиск') || t.includes('безопасн') || t.includes('проект')) return illus.search ? illus.search(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('религи') || t.includes('православ') || t.includes('ислам') || t.includes('храм') || t.includes('богослуж')) return illus.churchSmall ? illus.churchSmall(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('молитв') || t.includes('пост') || t.includes('праздник') || t.includes('традиц')) return illus.candle ? illus.candle(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('книг') || t.includes('заповед') || t.includes('добр') || t.includes('зл') || t.includes('милосерд') || t.includes('семь')) return illus.bookHoly ? illus.bookHoly(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('исследов') || t.includes('тему') || t.includes('информац') || t.includes('метод')) return illus.magnifier ? illus.magnifier(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('презентац') || t.includes('слайд') || t.includes('выступлен') || t.includes('конференц')) return illus.presentation ? illus.presentation(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('анализ') || t.includes('вывод') || t.includes('макет') || t.includes('сборк') || t.includes('материал')) return illus.tools ? illus.tools(c) : illus[Object.keys(illus)[0]](c);

  if (t.includes('арктик') || t.includes('тундр') || t.includes('зон') || t.includes('лес') || t.includes('степ') || t.includes('пустын')) return illus.natureZone ? illus.natureZone(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('тел') || t.includes('человек') || t.includes('пищевар') || t.includes('дыхан') || t.includes('кровообращ') || t.includes('сердц')) return illus.humanBody ? illus.humanBody(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('вод') || t.includes('воздух') || t.includes('почв')) return illus.water ? illus.water(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('эколог') || t.includes('охран') || t.includes('красн') || t.includes('заповедн') || t.includes('чист')) return illus.recycling ? illus.recycling(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('славян') || t.includes('древн') || t.includes('крещен')) return illus.church ? illus.church(c) : illus[Object.keys(illus)[0]](c);
  if (t.includes('ископаем') || t.includes('растен') || t.includes('животн')) return illus.ecosystem ? illus.ecosystem(c) : illus[Object.keys(illus)[0]](c);

  // Default: pick based on lesson index
  return illus[keys[0]](c);
}

// Get a second illustration (for the side card)
function getSecondaryIllustration(subject, title, c) {
  const illus = ILLUSTRATIONS[subject];
  if (!illus) return '';
  const keys = Object.keys(illus);
  if (keys.length < 2) return '';

  // Pick a different one from the primary
  const primary = getIllustration(subject, title, c);
  for (let i = 1; i < keys.length; i++) {
    const candidate = illus[keys[i]](c);
    if (candidate !== primary) return candidate;
  }
  return '';
}

// Clean text - remove emojis and markdown
function cleanText(text) {
  return text
    .replace(/[\u{1F000}-\u{1FFFF}]/gu, '')
    .replace(/[\u{2600}-\u{27BF}]/gu, '')
    .replace(/[\u{FE00}-\u{FE0F}]/gu, '')
    .replace(/[\u{1F900}-\u{1F9FF}]/gu, '')
    .replace(/[\u{2702}-\u{27B0}]/gu, '')
    .replace(/\*\*/g, '')
    .replace(/\*/g, '')
    .replace(/_/g, '')
    .replace(/`/g, '')
    .replace(/##/g, '')
    .replace(/#/g, '')
    .trim();
}

function truncate(text, maxLen) {
  if (text.length <= maxLen) return text;
  return text.substring(0, maxLen - 3) + '...';
}

// Extract lesson number from title
function getLessonNum(title) {
  const m = title.match(/Урок\s+(\d+)/i);
  return m ? parseInt(m[1]) : 1;
}

// Get key concepts from lesson data
function getKeyConcepts(lesson) {
  if (lesson.keyPoints && lesson.keyPoints.length > 0) {
    return lesson.keyPoints.slice(0, 4).map(k => cleanText(truncate(k, 30)));
  }
  return [];
}

function getFacts(lesson) {
  if (lesson.facts && lesson.facts.length > 0) {
    return lesson.facts.slice(0, 3).map(f => cleanText(truncate(f, 40)));
  }
  return [];
}

// Main SVG generator - rich style like grade 5
function generateRichSVG(subject, lesson, lessonIndex, totalLessons) {
  const config = SUBJECT_CONFIG[subject];
  if (!config) return '';

  const c = config.colors;
  const title = cleanText(lesson.title || 'Урок ' + (lessonIndex + 1));
  const lessonNum = getLessonNum(lesson.title || '');
  const concepts = getKeyConcepts(lesson);
  const facts = getFacts(lesson);
  const subjectName = config.name;

  // Get illustration
  const illustration = getIllustration(subject, lesson.title || '', c);

  // Choose layout variant based on lesson index
  const variant = lessonIndex % 4;

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 350">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="${c.bg1}"/>
      <stop offset="100%" stop-color="${c.bg2}"/>
    </linearGradient>
  </defs>
  <rect width="500" height="350" fill="url(#bg)" rx="10"/>
  <rect x="3" y="3" width="494" height="344" rx="8" fill="none" stroke="${c.main}" stroke-width="3"/>
  <rect x="8" y="8" width="484" height="334" rx="6" fill="none" stroke="${c.main}" stroke-width="1" opacity="0.3"/>
  <polygon points="10,10 30,10 10,30" fill="${c.dark}" opacity="0.08"/>
  <polygon points="490,10 470,10 490,30" fill="${c.dark}" opacity="0.08"/>
  <polygon points="10,340 30,340 10,320" fill="${c.light}" opacity="0.08"/>
  <polygon points="490,340 470,340 490,320" fill="${c.lighter}" opacity="0.08"/>
  <circle cx="70" cy="15" r="4" fill="${c.dark}" opacity="0.1"/>
  <circle cx="82" cy="15" r="4" fill="${c.main}" opacity="0.1"/>
  <circle cx="94" cy="15" r="4" fill="${c.mid}" opacity="0.1"/>
  <circle cx="406" cy="15" r="4" fill="${c.dark}" opacity="0.1"/>
  <circle cx="418" cy="15" r="4" fill="${c.main}" opacity="0.1"/>
  <circle cx="430" cy="15" r="4" fill="${c.mid}" opacity="0.1"/>
  <text x="250" y="50" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="${c.main}" text-anchor="middle">${truncate(title, 35)}</text>
  <text x="250" y="68" font-family="Arial,sans-serif" font-size="12" fill="#777" text-anchor="middle">${subjectName} - Урок ${lessonNum}</text>
  <line x1="30" y1="78" x2="470" y2="78" stroke="${c.main}" stroke-width="2" opacity="0.25"/>
  <rect x="30" y="75" width="60" height="6" fill="${c.main}" opacity="0.15" rx="1"/>
  <rect x="410" y="75" width="60" height="6" fill="${c.light}" opacity="0.12" rx="1"/>`;

  if (variant === 0) {
    // Layout: Large illustration card (left) + Key concepts card (right top) + Facts card (right bottom)
    svg += `
  <rect x="20" y="88" width="230" height="200" rx="6" fill="white" stroke="${c.main}" stroke-width="1.5" opacity="0.95"/>
  <rect x="20" y="88" width="230" height="24" rx="6" fill="${c.main}" opacity="0.9"/>
  <rect x="20" y="104" width="230" height="8" fill="${c.main}" opacity="0.9"/>
  <text x="135" y="105" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">${truncate(title.toUpperCase(), 25)}</text>
  ${illustration}`;

    if (concepts.length > 0) {
      svg += `
  <rect x="260" y="88" width="220" height="${facts.length > 0 ? '95' : '200'}" rx="6" fill="white" stroke="${c.mid}" stroke-width="1.5" opacity="0.95"/>
  <rect x="260" y="88" width="220" height="24" rx="6" fill="${c.mid}" opacity="0.9"/>
  <rect x="260" y="104" width="220" height="8" fill="${c.mid}" opacity="0.9"/>
  <text x="370" y="105" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">КЛЮЧЕВЫЕ ПОНЯТИЯ</text>`;
      concepts.forEach((concept, i) => {
        const y = 125 + i * 18;
        const colorArr = [c.main, c.dark, c.mid, c.light];
        svg += `
  <rect x="268" y="${y - 6}" width="8" height="8" rx="1" fill="${colorArr[i % 4]}" opacity="0.3"/>
  <text x="282" y="${y + 2}" font-family="Arial,sans-serif" font-size="9" fill="#555" text-anchor="start">${concept}</text>`;
      });
    }

    if (facts.length > 0) {
      const factY = concepts.length > 0 ? 195 : 88;
      svg += `
  <rect x="260" y="${factY}" width="220" height="${350 - factY - 47}" rx="6" fill="white" stroke="${c.light}" stroke-width="1.5" opacity="0.95"/>
  <rect x="260" y="${factY}" width="220" height="24" rx="6" fill="${c.light}" opacity="0.9"/>
  <rect x="260" y="${factY + 16}" width="220" height="8" fill="${c.light}" opacity="0.9"/>
  <text x="370" y="${factY + 17}" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">ИНТЕРЕСНЫЙ ФАКТ</text>`;
      facts.forEach((fact, i) => {
        const fy = factY + 32 + i * 20;
        svg += `
  <text x="370" y="${fy}" font-family="Arial,sans-serif" font-size="9" fill="${c.main}" text-anchor="middle">${fact}</text>`;
      });
    }
  } else if (variant === 1) {
    // Layout: Full-width illustration card (top) + Two side-by-side cards (bottom)
    svg += `
  <rect x="20" y="88" width="460" height="120" rx="6" fill="white" stroke="${c.main}" stroke-width="1.5" opacity="0.95"/>
  <rect x="20" y="88" width="460" height="24" rx="6" fill="${c.main}" opacity="0.9"/>
  <rect x="20" y="104" width="460" height="8" fill="${c.main}" opacity="0.9"/>
  <text x="250" y="105" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">${truncate(title.toUpperCase(), 30)}</text>
  ${illustration}`;

    svg += `
  <rect x="20" y="218" width="220" height="80" rx="6" fill="white" stroke="${c.mid}" stroke-width="1.5" opacity="0.95"/>
  <rect x="20" y="218" width="220" height="24" rx="6" fill="${c.mid}" opacity="0.9"/>
  <rect x="20" y="234" width="220" height="8" fill="${c.mid}" opacity="0.9"/>
  <text x="130" y="235" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">ОСНОВНЫЕ ПОНЯТИЯ</text>`;
    concepts.slice(0, 3).forEach((concept, i) => {
      const y = 258 + i * 16;
      const colorArr = [c.main, c.dark, c.mid];
      svg += `
  <rect x="30" y="${y - 6}" width="8" height="8" rx="1" fill="${colorArr[i]}" opacity="0.3"/>
  <text x="44" y="${y + 2}" font-family="Arial,sans-serif" font-size="9" fill="#555">${concept}</text>`;
    });

    svg += `
  <rect x="260" y="218" width="220" height="80" rx="6" fill="white" stroke="${c.light}" stroke-width="1.5" opacity="0.95"/>
  <rect x="260" y="218" width="220" height="24" rx="6" fill="${c.light}" opacity="0.9"/>
  <rect x="260" y="234" width="220" height="8" fill="${c.light}" opacity="0.9"/>
  <text x="370" y="235" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">ФАКТЫ</text>`;
    facts.slice(0, 3).forEach((fact, i) => {
      const y = 258 + i * 16;
      svg += `
  <text x="270" y="${y}" font-family="Arial,sans-serif" font-size="9" fill="#555">${truncate(fact, 30)}</text>`;
    });
  } else if (variant === 2) {
    // Layout: Three columns - illustration, concepts, facts
    svg += `
  <rect x="20" y="88" width="150" height="200" rx="6" fill="white" stroke="${c.main}" stroke-width="1.5" opacity="0.95"/>
  <rect x="20" y="88" width="150" height="24" rx="6" fill="${c.main}" opacity="0.9"/>
  <rect x="20" y="104" width="150" height="8" fill="${c.main}" opacity="0.9"/>
  <text x="95" y="105" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="white" text-anchor="middle">ИЛЛЮСТРАЦИЯ</text>
  ${illustration}`;

    svg += `
  <rect x="180" y="88" width="155" height="200" rx="6" fill="white" stroke="${c.mid}" stroke-width="1.5" opacity="0.95"/>
  <rect x="180" y="88" width="155" height="24" rx="6" fill="${c.mid}" opacity="0.9"/>
  <rect x="180" y="104" width="155" height="8" fill="${c.mid}" opacity="0.9"/>
  <text x="257" y="105" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="white" text-anchor="middle">ПОНЯТИЯ</text>`;
    concepts.forEach((concept, i) => {
      const y = 128 + i * 20;
      svg += `
  <rect x="190" y="${y - 6}" width="8" height="8" rx="1" fill="${[c.main, c.dark, c.mid, c.light][i % 4]}" opacity="0.3"/>
  <text x="204" y="${y + 2}" font-family="Arial,sans-serif" font-size="9" fill="#555">${truncate(concept, 18)}</text>`;
    });

    svg += `
  <rect x="345" y="88" width="135" height="200" rx="6" fill="white" stroke="${c.light}" stroke-width="1.5" opacity="0.95"/>
  <rect x="345" y="88" width="135" height="24" rx="6" fill="${c.light}" opacity="0.9"/>
  <rect x="345" y="104" width="135" height="8" fill="${c.light}" opacity="0.9"/>
  <text x="412" y="105" font-family="Arial,sans-serif" font-size="9" font-weight="bold" fill="white" text-anchor="middle">ФАКТЫ</text>`;
    facts.slice(0, 5).forEach((fact, i) => {
      const y = 128 + i * 18;
      svg += `
  <rect x="353" y="${y - 10}" width="118" height="15" rx="3" fill="${c.bg1}" opacity="0.5"/>
  <text x="412" y="${y}" font-family="Arial,sans-serif" font-size="8" fill="${c.main}" text-anchor="middle">${truncate(fact, 16)}</text>`;
    });
  } else {
    // Layout: Timeline/step style at top + illustration below + concepts as tags
    svg += `
  <rect x="20" y="88" width="460" height="55" rx="6" fill="white" stroke="${c.main}" stroke-width="1.5" opacity="0.95"/>
  <line x1="35" y1="115" x2="465" y2="115" stroke="${c.main}" stroke-width="2"/>
  <circle cx="80" cy="115" r="5" fill="${c.main}"/>
  <rect x="48" y="125" width="64" height="14" rx="7" fill="${c.main}" opacity="0.15"/>
  <text x="80" y="136" font-family="Arial,sans-serif" font-size="8" fill="${c.main}" text-anchor="middle" font-weight="bold">${truncate(concepts[0] || 'Начало', 10)}</text>
  <circle cx="180" cy="115" r="5" fill="${c.dark}"/>
  <rect x="148" y="125" width="64" height="14" rx="7" fill="${c.dark}" opacity="0.15"/>
  <text x="180" y="136" font-family="Arial,sans-serif" font-size="8" fill="${c.dark}" text-anchor="middle" font-weight="bold">${truncate(concepts[1] || 'Развитие', 10)}</text>
  <circle cx="310" cy="115" r="5" fill="${c.mid}"/>
  <rect x="278" y="125" width="64" height="14" rx="7" fill="${c.mid}" opacity="0.15"/>
  <text x="310" y="136" font-family="Arial,sans-serif" font-size="8" fill="${c.mid}" text-anchor="middle" font-weight="bold">${truncate(concepts[2] || 'Основное', 10)}</text>
  <circle cx="420" cy="115" r="5" fill="${c.light}"/>
  <rect x="388" y="125" width="64" height="14" rx="7" fill="${c.light}" opacity="0.15"/>
  <text x="420" y="136" font-family="Arial,sans-serif" font-size="8" fill="${c.light}" text-anchor="middle" font-weight="bold">${truncate(concepts[3] || 'Итог', 10)}</text>`;

    svg += `
  <rect x="20" y="152" width="240" height="145" rx="6" fill="white" stroke="${c.main}" stroke-width="1.5" opacity="0.95"/>
  <rect x="20" y="152" width="240" height="24" rx="6" fill="${c.main}" opacity="0.9"/>
  <rect x="20" y="168" width="240" height="8" fill="${c.main}" opacity="0.9"/>
  <text x="140" y="169" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">${truncate(title.toUpperCase(), 22)}</text>
  ${illustration}`;

    svg += `
  <rect x="270" y="152" width="210" height="145" rx="6" fill="white" stroke="${c.light}" stroke-width="1.5" opacity="0.95"/>
  <rect x="270" y="152" width="210" height="24" rx="6" fill="${c.light}" opacity="0.9"/>
  <rect x="270" y="168" width="210" height="8" fill="${c.light}" opacity="0.9"/>
  <text x="375" y="169" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">ТЕМЫ УРОКА</text>`;

    const tagConcepts = concepts.length > 0 ? concepts : [title];
    tagConcepts.forEach((concept, i) => {
      const col = i % 2;
      const row = Math.floor(i / 2);
      const x = 280 + col * 100;
      const y = 190 + row * 28;
      const colors = [c.main, c.dark, c.mid, c.light, c.lighter];
      svg += `
  <rect x="${x}" y="${y}" width="90" height="22" rx="11" fill="${colors[i % 5]}" opacity="0.15"/>
  <text x="${x + 45}" y="${y + 15}" font-family="Arial,sans-serif" font-size="9" fill="${colors[i % 5]}" text-anchor="middle" font-weight="bold">${truncate(concept, 12)}</text>`;
    });

    if (facts.length > 0) {
      const fy = 250;
      svg += `
  <text x="375" y="${fy}" font-family="Arial,sans-serif" font-size="9" fill="${c.main}" text-anchor="middle" font-weight="bold">${truncate(facts[0], 28)}</text>`;
      if (facts.length > 1) {
        svg += `
  <text x="375" y="${fy + 16}" font-family="Arial,sans-serif" font-size="8" fill="#888" text-anchor="middle">${truncate(facts[1], 28)}</text>`;
      }
    }
  }

  // Bottom bar
  svg += `
  <rect x="15" y="308" width="470" height="30" rx="4" fill="${c.main}" opacity="0.85"/>
  <text x="250" y="329" font-family="Arial,sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="bold">${truncate(title, 35)}</text>
</svg>`;

  return svg;
}

// Main execution
function main() {
  const subjects = Object.keys(SUBJECT_CONFIG);
  let totalGenerated = 0;

  subjects.forEach(subject => {
    const dataFile = path.join(GRADE_DIR, subject + '.json');
    if (!fs.existsSync(dataFile)) return;

    const data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
    const lessonsData = data.lessons || data;
    if (!lessonsData.detailedTopics) return;

    const allLessons = [];
    lessonsData.detailedTopics.forEach(topic => {
      (topic.lessons || []).forEach(lesson => allLessons.push(lesson));
    });

    // Create output directory
    const outDir = path.join(IMG_DIR, subject);
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

    allLessons.forEach((lesson, idx) => {
      const svg = generateRichSVG(subject, lesson, idx, allLessons.length);
      if (svg) {
        const outFile = path.join(outDir, `lesson${idx + 1}.svg`);
        fs.writeFileSync(outFile, svg, 'utf8');
        totalGenerated++;
      }
    });

    console.log(`${subject}: generated ${allLessons.length} SVGs`);
  });

  console.log(`\nTotal: ${totalGenerated} SVG files generated`);
}

main();
