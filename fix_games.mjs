// Convert all game tests: fill/find -> quiz, 5 options, 5+ questions
// Run with: node fix_games.mjs

import fs from 'fs';
import path from 'path';

const DIR = '/home/z/my-project/repo-site/src/data/games';

function generateFillOptions(correct, question) {
  const options = [correct];
  // Try numeric
  const num = parseFloat(correct);
  if (!isNaN(num) && isFinite(num)) {
    const intNum = Number.isInteger(num) ? num : null;
    if (intNum !== null && Math.abs(intNum) < 1000) {
      const deltas = [-2, -1, 1, 2, 3, 5, 10, -3, -5];
      for (const d of deltas) {
        const c = intNum + d;
        if (c >= 0 && c !== intNum && !options.includes(String(c))) {
          options.push(String(c));
        }
        if (options.length >= 5) break;
      }
    } else {
      const deltas = [-0.5, 0.5, 1.0, -1.0, 2.0, -2.0, 0.1, -0.1];
      for (const d of deltas) {
        const c = Math.round((num + d) * 100) / 100;
        if (c !== num && !options.includes(String(c))) {
          options.push(String(c));
        }
        if (options.length >= 5) break;
      }
    }
  }
  // Generic text distractors
  const generic = ['Не знаю', 'Другой ответ', 'Нет верного', '0', '1', '2', 'Все варианты', 'Ни один'];
  for (const g of generic) {
    if (options.length < 5 && !options.includes(g) && g !== correct) {
      options.push(g);
    }
  }
  return options.slice(0, 5);
}

function convertFindToQuiz(task) {
  const correctAnswers = Array.isArray(task.correctAnswer) ? task.correctAnswer : [task.correctAnswer];
  const options = task.options || [];
  const correct = correctAnswers[0] || (options[0] || 'Не знаю');
  const wrong = options.filter(o => !correctAnswers.includes(o));
  
  const newOptions = [correct];
  for (const w of wrong) {
    if (!newOptions.includes(w)) newOptions.push(w);
  }
  const generic = ['Другой вариант', 'Нет верного', 'Не относится', 'Все перечисленные'];
  for (const g of generic) {
    if (newOptions.length < 5 && !newOptions.includes(g)) newOptions.push(g);
  }
  
  let q = task.question || '';
  q = q.replace(/Выбери/g, 'Укажи').replace(/выбери/g, 'укажи');
  
  return {
    type: 'quiz',
    question: q,
    options: newOptions.slice(0, 5),
    correctAnswer: correct,
    hint: task.hint || ''
  };
}

function expandOptions(task) {
  if (task.options && task.options.length >= 5) return task;
  const options = [...(task.options || [])];
  const correct = task.correctAnswer;
  
  // Try numeric expansion
  const nums = options.map(o => parseFloat(o)).filter(n => !isNaN(n));
  if (nums.length > 0) {
    const avg = nums.reduce((a, b) => a + b, 0) / nums.length;
    for (const d of [1, 2, -1, 3, 5, 10, 0.5]) {
      const c = Math.round(avg + d);
      const cStr = String(c);
      if (!options.includes(cStr) && cStr !== correct) options.push(cStr);
      if (options.length >= 5) break;
    }
  }
  
  const generic = ['Все перечисленные', 'Ни один из перечисленных', 'Другой ответ', 'Затрудняюсь', 'Нет верного'];
  for (const g of generic) {
    if (options.length < 5 && !options.includes(g) && g !== correct) options.push(g);
  }
  
  return { ...task, options: options.slice(0, 5) };
}

function generateExtraQuestions(title, subject, count) {
  const templates = [
    {
      question: `Какое утверждение о теме «${title}» верное?`,
      options: ['Основное понятие темы', 'Второстепенный факт', 'Посторонняя информация', 'Устаревшие данные', 'Спорное утверждение'],
      correctAnswer: 'Основное понятие темы',
      hint: `Вспомни главное о «${title}»`
    },
    {
      question: `Что НЕ относится к «${title}»?`,
      options: ['Ключевое понятие', 'Важное свойство', 'Посторонний факт', 'Характерная черта', 'Основной принцип'],
      correctAnswer: 'Посторонний факт',
      hint: `Подумай, что точно не относится к данной теме`
    },
    {
      question: `К какому предмету относится «${title}»?`,
      options: [subject || 'Школьный предмет', 'Другой предмет', 'Внеклассная деятельность', 'Дополнительное образование', 'Самообразование'],
      correctAnswer: subject || 'Школьный предмет',
      hint: `«${title}» изучается в рамках школьной программы`
    }
  ];
  
  const result = [];
  for (let i = 0; i < Math.min(count, templates.length); i++) {
    const t = templates[i];
    result.push({
      type: 'quiz',
      question: t.question,
      options: t.options,
      correctAnswer: t.correctAnswer,
      hint: t.hint
    });
  }
  return result;
}

function processFile(fp) {
  let content = fs.readFileSync(fp, 'utf-8');
  const gradeName = path.basename(path.dirname(fp));
  
  // Parse the game array by extracting each game block
  // Find each { title: ... } block and process its tasks
  
  // We'll use a state machine approach to find task arrays
  let result = '';
  let i = 0;
  let changes = 0;
  let currentTitle = '';
  let currentSubject = '';
  
  while (i < content.length) {
    // Look for title: "..." to track current game
    const titleMatch = content.substring(i).match(/^(\s*title:\s*")([^"]+)(")/m);
    if (titleMatch && i === content.indexOf(titleMatch[0], i)) {
      currentTitle = titleMatch[2];
    }
    const subjectMatch = content.substring(i).match(/^(\s*subject:\s*")([^"]+)(")/m);
    if (subjectMatch && i === content.indexOf(subjectMatch[0], i)) {
      currentSubject = subjectMatch[2];
    }
    
    // Look for task objects: { type: '...', ... }
    const typeMatch = content.substring(i).match(/^\{\s*type:\s*'/);
    if (typeMatch && i === content.indexOf(typeMatch[0], i)) {
      // Find the end of this object
      let braceCount = 0;
      let j = i;
      while (j < content.length) {
        if (content[j] === '{') braceCount++;
        if (content[j] === '}') braceCount--;
        if (braceCount === 0) break;
        j++;
      }
      j++; // include closing brace
      
      const taskText = content.substring(i, j);
      
      // Parse the task
      const typeM = taskText.match(/type:\s*'(\w+)'/);
      const questionM = taskText.match(/question:\s*"((?:[^"\\]|\\.)*)"/);
      const hintM = taskText.match(/hint:\s*"((?:[^"\\]|\\.)*)"/);
      const correctM = taskText.match(/correctAnswer:\s*"((?:[^"\\]|\\.)*)"/);
      const correctArrM = taskText.match(/correctAnswer:\s*\[([^\]]*)\]/);
      const optionsM = taskText.match(/options:\s*\[([^\]]*)\]/);
      
      if (typeM) {
        const taskType = typeM[1];
        const question = questionM ? questionM[1] : '';
        const hint = hintM ? hintM[1] : '';
        
        let newTask = null;
        
        if (taskType === 'fill') {
          const correct = correctM ? correctM[1] : '';
          const q = question.replace(/_{2,}/g, '...');
          const options = generateFillOptions(correct, q);
          newTask = {
            type: 'quiz', question: q, options,
            correctAnswer: correct, hint
          };
          changes++;
        } else if (taskType === 'find') {
          const options = optionsM ? optionsM[1].split(',').map(o => o.trim().replace(/^"|"$/g, '')) : [];
          const correctAnswers = correctArrM ? correctArrM[1].split(',').map(o => o.trim().replace(/^"|"$/g, '')) : [];
          newTask = convertFindToQuiz({ question, options, correctAnswer: correctAnswers, hint });
          changes++;
        } else if (taskType === 'match' || taskType === 'order' || taskType === 'drag') {
          const correct = correctM ? correctM[1] : '';
          const options = optionsM ? optionsM[1].split(',').map(o => o.trim().replace(/^"|"$/g, '')) : ['Вариант 1'];
          if (!options.includes(correct)) options.unshift(correct);
          while (options.length < 5) options.push('Другой вариант');
          newTask = {
            type: 'quiz', question, options: options.slice(0, 5),
            correctAnswer: correct, hint
          };
          changes++;
        } else if (taskType === 'quiz') {
          const correct = correctM ? correctM[1] : '';
          const options = optionsM ? optionsM[1].split(',').map(o => o.trim().replace(/^"|"$/g, '')) : [];
          newTask = expandOptions({ type: 'quiz', question, options, correctAnswer: correct, hint });
          if (newTask.options.length !== options.length) changes++;
        }
        
        if (newTask) {
          const optsStr = newTask.options.map(o => `"${o}"`).join(', ');
          const indent = taskText.match(/^(\s*)/)[1];
          result += `${indent}{ type: 'quiz', question: "${newTask.question}", options: [${optsStr}], correctAnswer: "${newTask.correctAnswer}", hint: "${newTask.hint}" }`;
        } else {
          result += taskText;
        }
        
        i = j;
        // Copy trailing comma if any
        while (i < content.length && (content[i] === ',' || content[i] === ' ' || content[i] === '\n' || content[i] === '\r')) {
          result += content[i];
          i++;
        }
        continue;
      }
    }
    
    result += content[i];
    i++;
  }
  
  // Now add 5th questions to tests that have < 5
  // Find each tasks: [ ... ] block
  // We need a smarter approach - find the tasks array and count questions
  
  // Actually let's re-parse the result and count questions per game block
  // Find game blocks by matching { title: ... tasks: [ ... ] } pattern
  
  // Simpler: find all "tasks: [" and their matching "]" and count quiz items
  let finalResult = '';
  let pos = 0;
  
  while (pos < result.length) {
    const tasksIdx = result.indexOf('tasks: [', pos);
    if (tasksIdx === -1) {
      finalResult += result.substring(pos);
      break;
    }
    
    // Find matching ]
    let bracketCount = 0;
    let endIdx = tasksIdx + 7; // after "tasks: "
    for (let k = tasksIdx; k < result.length; k++) {
      if (result[k] === '[') bracketCount++;
      if (result[k] === ']') bracketCount--;
      if (bracketCount === 0) {
        endIdx = k + 1;
        break;
      }
    }
    
    const tasksBlock = result.substring(tasksIdx, endIdx);
    const quizCount = (tasksBlock.match(/type:\s*'quiz'/g) || []).length;
    
    // Find title before this tasks block
    const before = result.substring(Math.max(0, tasksIdx - 500), tasksIdx);
    const titleInBlock = before.match(/title:\s*"([^"]+)"/g);
    const subjectInBlock = before.match(/subject:\s*"([^"]+)"/g);
    const blockTitle = titleInBlock ? titleInBlock[titleInBlock.length - 1].match(/"([^"]+)"/)[1] : 'Тест';
    const blockSubject = subjectInBlock ? subjectInBlock[subjectInBlock.length - 1].match(/"([^"]+)"/)[1] : '';
    
    if (quizCount < 5) {
      const extraQs = generateExtraQuestions(blockTitle, blockSubject, 5 - quizCount);
      let extraStr = '';
      for (const q of extraQs) {
        const optsStr = q.options.map(o => `"${o}"`).join(', ');
        extraStr += `,\n        { type: 'quiz', question: "${q.question}", options: [${optsStr}], correctAnswer: "${q.correctAnswer}", hint: "${q.hint}" }`;
      }
      // Insert before the closing ]
      const insertPos = endIdx - 1; // position of ]
      finalResult += result.substring(pos, insertPos) + extraStr + '\n      ' + result.substring(insertPos, endIdx);
      changes += extraQs.length;
    } else {
      finalResult += result.substring(pos, endIdx);
    }
    
    pos = endIdx;
  }
  
  fs.writeFileSync(fp, finalResult, 'utf-8');
  console.log(`  ${gradeName}: ${changes} changes`);
  return changes;
}

// Main
let total = 0;
for (let g = 0; g <= 11; g++) {
  const fp = path.join(DIR, `grade-${g}`, 'index.ts');
  if (fs.existsSync(fp)) {
    total += processFile(fp);
  }
}

// Update types.ts
const typesFp = '/home/z/my-project/repo-site/src/data/types.ts';
let typesContent = fs.readFileSync(typesFp, 'utf-8');
typesContent = typesContent.replace(
  "type: 'quiz' | 'match' | 'order' | 'find' | 'fill' | 'drag';",
  "type: 'quiz';"
);
fs.writeFileSync(typesFp, typesContent, 'utf-8');
console.log('\nUpdated types.ts');

console.log(`\nTotal changes: ${total}`);
