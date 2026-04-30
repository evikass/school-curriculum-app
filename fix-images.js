const fs = require('fs');
const path = require('path');

const subjectConfig = {
  algebra: { color: '#3730a3', icon: '∑', name: 'Алгебра' },
  geometry: { color: '#155e75', icon: '△', name: 'Геометрия' },
  physics: { color: '#581c87', icon: '⚛', name: 'Физика' },
  chemistry: { color: '#065f46', icon: '⚗', name: 'Химия' },
  biology: { color: '#166534', icon: '🧬', name: 'Биология' },
  history: { color: '#78350f', icon: '📜', name: 'История' },
  geography: { color: '#115e59', icon: '🌍', name: 'География' },
  literature: { color: '#581c87', icon: '📖', name: 'Литература' },
  russian: { color: '#991b1b', icon: 'Я', name: 'Русский язык' },
  english: { color: '#1e3a5f', icon: 'A', name: 'Английский язык' },
  social: { color: '#7c2d12', icon: '⚖', name: 'Обществознание' },
  informatics: { color: '#1e40af', icon: '💻', name: 'Информатика' },
  coding: { color: '#065f46', icon: '</>', name: 'Программирование' },
  economy: { color: '#92400e', icon: '📈', name: 'Экономика' },
  business: { color: '#713f12', icon: '💼', name: 'Бизнес' },
  pe: { color: '#15803d', icon: '⚽', name: 'Физкультура' },
  art: { color: '#7e22ce', icon: '🎨', name: 'Искусство' },
  safety: { color: '#991b1b', icon: '🛡', name: 'ОБЖ' },
  astronomy: { color: '#1e1b4b', icon: '🔭', name: 'Астрономия' },
  philosophy: { color: '#4c1d95', icon: '💭', name: 'Философия' },
  career: { color: '#0f766e', icon: '🎯', name: 'Профориентация' },
  tech: { color: '#374151', icon: '🔧', name: 'Технология' },
  ege: { color: '#dc2626', icon: '📝', name: 'ЕГЭ' },
  lab: { color: '#4338ca', icon: '🔬', name: 'Лаборатория' },
  projects: { color: '#0369a1', icon: '📋', name: 'Проекты' },
};

function makeSvg(grade, subject, title) {
  const cfg = subjectConfig[subject] || { color: '#4338ca', icon: '📚', name: subject };
  const shortTitle = title.replace(/^Урок \d+:\s*/, '').substring(0, 30);
  const svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300"><rect width="400" height="300" fill="' + cfg.color + '"/><rect x="20" y="20" width="360" height="60" rx="10" fill="rgba(255,255,255,0.15)"/><text x="200" y="55" text-anchor="middle" fill="white" font-size="22" font-weight="bold">' + shortTitle + '</text><text x="200" y="200" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="60">' + cfg.icon + '</text><text x="200" y="270" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="14">' + grade + ' класс · ' + cfg.name + '</text></svg>';
  return 'data:image/svg+xml,' + encodeURIComponent(svg);
}

let totalImagesAdded = 0;
let totalExamplesAdded = 0;
const report = [];

function processFile(grade, subject) {
  const filePath = 'src/data/grades/' + grade + '/' + subject + '/index.ts';
  if (!fs.existsSync(filePath)) return;
  
  let content = fs.readFileSync(filePath, 'utf8');
  let imagesAdded = 0;
  let examplesAdded = 0;
  
  // Skip files that use createLesson helper that auto-generates images
  if (content.includes('createLesson') && content.includes('finalImage') && grade === 10 && subject === 'coding') {
    // Fix the broken createLesson function in grade 10 coding
    // The function references 'examples' and 'keyPoints' but doesn't accept them as params
    
    // Fix function signature
    content = content.replace(
      'const createLesson = (title: string, image: string, description: string, tasks: string[]) => {',
      'const createLesson = (title: string, image: string, description: string, tasks: string[], examples?: string[], keyPoints?: string[]) => {'
    );
    
    // Fix the references - replace undefined variable checks
    content = content.replace(
      "if (!examples || examples.length === 0) {",
      "if (!examples || examples.length === 0) {"
    );
    content = content.replace(
      "if (!keyPoints || keyPoints.length === 0) {",
      "if (!keyPoints || keyPoints.length === 0) {"
    );
    
    // Fix the return to include examples and keyPoints
    content = content.replace(
      "examples: (examples?.length ? examples : autoEx.slice(0, 3)), keyPoints: (keyPoints?.length ? keyPoints : autoKP.slice(0, 5)) };",
      "examples: (examples?.length ? examples : autoEx.slice(0, 3)), keyPoints: (keyPoints?.length ? keyPoints : autoKP.slice(0, 5)) };"
    );
    
    // Now add examples to createLesson calls that don't have them
    // Find all createLesson calls and check if they need examples added
    // Pattern: createLesson("title", "image", `description`, [tasks])
    // Need to add: , [examples], [keyPoints]
    
    const lines = content.split('\n');
    const newLines = [];
    let inCreateLessonCall = false;
    let parenDepth = 0;
    let callHasExamples = false;
    let arrayCount = 0;
    let callStartLine = -1;
    let callTitle = '';
    
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      
      if (line.includes('createLesson(') && !line.includes('const createLesson')) {
        inCreateLessonCall = true;
        parenDepth = 0;
        arrayCount = 0;
        callHasExamples = false;
        callStartLine = i;
        // Extract title
        const titleMatch = line.match(/createLesson\(\s*["`]([^"`]+)/);
        if (titleMatch) callTitle = titleMatch[1];
      }
      
      if (inCreateLessonCall) {
        // Count brackets to track arrays
        for (const ch of line) {
          if (ch === '[') arrayCount++;
          if (ch === ']') arrayCount--;
          if (ch === '(') parenDepth++;
          if (ch === ')') parenDepth--;
        }
        
        // Check if this line has examples in the call
        if (line.includes('examples:')) callHasExamples = true;
        
        // When the call closes (parenDepth goes to 0 or negative after opening)
        if (parenDepth <= 0 && i > callStartLine) {
          // Check if we need to add examples
          if (!callHasExamples) {
            // Find the closing of the tasks array and add examples
            // The tasks array is the 4th argument
            // We need to add examples after the tasks array
            
            // Strategy: replace the closing ), with , [examples], [keyPoints])
            const shortTitle = callTitle.replace(/^Урок \d+:\s*/, '').substring(0, 30);
            const examplesArr = JSON.stringify([
              'Пример: ' + shortTitle + ' — практическое применение',
              'Задача на понимание: ' + shortTitle,
              'Упражнение: реализация ' + shortTitle.toLowerCase()
            ]);
            const keyPointsArr = JSON.stringify([
              'Ключевое понятие: ' + shortTitle,
              'Практическое применение ' + shortTitle.toLowerCase()
            ]);
            
            // Replace the closing ) of createLesson call
            // Need to find the right closing paren
            const lastParenIdx = line.lastIndexOf(')');
            if (lastParenIdx >= 0) {
              // Insert before the closing paren
              const before = line.substring(0, lastParenIdx);
              const after = line.substring(lastParenIdx);
              const indent = line.match(/^(\s*)/)[1];
              newLines.push(before + ',\n' + indent + '  ' + examplesArr + ',\n' + indent + '  ' + keyPointsArr + after);
              examplesAdded++;
            } else {
              newLines.push(line);
            }
          } else {
            newLines.push(line);
          }
          inCreateLessonCall = false;
          continue;
        }
      }
      
      newLines.push(line);
    }
    
    content = newLines.join('\n');
    
    // Also handle the image generation in createLesson
    // The createLesson already generates images for empty/path-based ones
    
    if (imagesAdded > 0 || examplesAdded > 0) {
      fs.writeFileSync(filePath, content);
    }
    
    report.push({ grade, subject, imagesAdded, examplesAdded });
    totalImagesAdded += imagesAdded;
    totalExamplesAdded += examplesAdded;
    return;
  }
  
  // For other files using createLesson with auto-image generation
  if (content.includes('createLesson') && content.includes('finalImage')) {
    // These handle images automatically, skip
    return;
  }
  
  // For L() helper function files (chemistry, biology)
  // L() passes image as a parameter, so all should have images
  // But let's check if any L() calls have empty images
  
  // For direct object pattern files, process them
  // Find lesson blocks without image fields
  
  const lines = content.split('\n');
  const newLines = [];
  
  for (let i = 0; i < lines.length; i++) {
    newLines.push(lines[i]);
    
    // Check for lesson title patterns
    // Look for: title: "Lesson Title",
    const titleMatch = lines[i].match(/^(\s*)title:\s*["`]([^"`]+)/);
    if (!titleMatch) continue;
    
    // Skip if this is a topic title or subject title
    // Topic titles have 'topic:' on the same or previous line context
    // Subject title is at the top level
    
    // Check if we're inside a lessons array by looking at previous context
    // Simple heuristic: if we've seen 'lessons: [' before this title
    const recentContext = newLines.slice(Math.max(0, newLines.length - 200)).join('\n');
    if (!recentContext.includes('lessons:')) continue;
    
    const indent = titleMatch[1];
    const lessonTitle = titleMatch[2].trim();
    
    // Skip topic-level titles
    if (lines[i].match(/^\s*topic:/)) continue;
    
    // Look ahead for image or description/content
    let hasImage = false;
    let imageLineIdx = -1;
    let descLineIdx = -1;
    let imageIsEmpty = false;
    let imageIsPath = false;
    
    for (let j = i + 1; j < Math.min(i + 20, lines.length); j++) {
      const nextLine = lines[j];
      
      // Check for image field
      if (nextLine.match(/^\s*image:/)) {
        hasImage = true;
        imageLineIdx = j;
        // Check if image is empty or path-based
        if (nextLine.match(/image:\s*["`]$/)) imageIsEmpty = true;
        if (nextLine.match(/image:\s*["`]\/school-curriculum-app\//)) imageIsPath = true;
        break;
      }
      
      // Check for description/content field (means no image before it)
      if (nextLine.match(/^\s*description:/) || nextLine.match(/^\s*content:/)) {
        descLineIdx = j;
        break;
      }
      
      // If we hit another title or closing structure, stop
      if (nextLine.match(/^\s*title:/) || nextLine.match(/^\s*\}\s*[,)]/)) {
        break;
      }
    }
    
    if (!hasImage && descLineIdx > 0) {
      // No image found before description - add one
      // We need to add it right after the title line
      const svgImage = makeSvg(grade, subject, lessonTitle);
      newLines.push(indent + 'image: "' + svgImage + '",');
      imagesAdded++;
    }
  }
  
  // Handle missing examples for grade 10 economy
  // and other subjects that need examples
  
  if (imagesAdded > 0) {
    content = newLines.join('\n');
    fs.writeFileSync(filePath, content);
  }
  
  if (imagesAdded > 0 || examplesAdded > 0) {
    report.push({ grade, subject, imagesAdded, examplesAdded });
    totalImagesAdded += imagesAdded;
    totalExamplesAdded += examplesAdded;
  }
}

const subjects10 = fs.readdirSync('src/data/grades/10').sort();
const subjects11 = fs.readdirSync('src/data/grades/11').sort();

console.log('Processing Grade 10...');
subjects10.forEach(s => { try { processFile(10, s); } catch(e) { console.log('Error in 10/' + s + ': ' + e.message); }});
console.log('Processing Grade 11...');
subjects11.forEach(s => { try { processFile(11, s); } catch(e) { console.log('Error in 11/' + s + ': ' + e.message); }});

console.log('\n=== REPORT ===');
console.log('Total images added:', totalImagesAdded);
console.log('Total examples added:', totalExamplesAdded);
report.forEach(r => console.log('  Grade ' + r.grade + ' ' + r.subject + ': ' + r.imagesAdded + ' images, ' + r.examplesAdded + ' examples'));
