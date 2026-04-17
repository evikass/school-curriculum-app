// Generate tests WITHOUT AI - using templates based on lesson content
import fs from 'fs';
import path from 'path';

const args = process.argv.slice(2);
const grade = parseInt(args[0]);
const dir = args[1];
const count = parseInt(args[2]) || 1;

const filePath = path.join('./src/data/grades', String(grade), dir, 'index.ts');

function extractInfo(content) {
  let subjectTitle = null, icon = 'BookOpen', color = 'text-blue-400';
  const tm = content.match(/title:\s*['"](.+?)['"]/);
  if (tm) subjectTitle = tm[1];
  const im = content.match(/icon:\s*['"](.+?)['"]/);
  if (im) icon = im[1];
  const cm = content.match(/color:\s*['"](.+?)['"]/);
  if (cm) color = cm[1];
  
  const lessons = [];
  // Match "Урок N: ..." format
  const lr1 = /(?:title:\s*['"]|createLesson\(\s*['"])(Урок \d+[^'"]*)['"]/g;
  let m;
  while ((m = lr1.exec(content)) !== null) lessons.push(m[1].trim());
  // If no "Урок" lessons found, match any lesson titles inside detailedTopics
  if (lessons.length === 0) {
    const lr2 = /(?:^\s*title:\s*['"])([^'"]+)['"]/gm;
    while ((m = lr2.exec(content)) !== null) {
      const t = m[1].trim();
      // Skip the subject title (first one) and topics array titles
      if (t.length > 2 && !t.startsWith('Урок')) {
        // Only add if it looks like a lesson title (not a topic category)
        const lineStart = content.lastIndexOf('\n', m.index) + 1;
        const linePrefix = content.substring(lineStart, m.index).trim();
        if (linePrefix.includes('title:') && content.substring(lineStart, m.index).includes('{')) {
          // Check indentation - lessons are deeper than topics
          const indent = (m.index - lineStart);
          if (indent > 10) lessons.push(t);
        }
      }
    }
  }
  // Final fallback: extract all indented title values (these are lessons, not subjects)
  if (lessons.length === 0) {
    const lr3 = /title:\s*['"]([^'"]+)['"]/g;
    let first = true;
    while ((m = lr3.exec(content)) !== null) {
      if (first) { first = false; continue; } // Skip subject title
      const t = m[1].trim();
      if (t.length > 2) lessons.push(t);
    }
  }
  
  const descs = {};
  const dr = /createLesson\(\s*['"]([^'"]+)['"]\s*,\s*`([\s\S]*?)`\s*,\s*\[/g;
  while ((m = dr.exec(content)) !== null) descs[m[1]] = m[2];
  const dr2 = /title:\s*['"]([^'"]+)['"][\s\S]*?description:\s*`([\s\S]*?)`/g;
  while ((m = dr2.exec(content)) !== null) { if (!descs[m[1]]) descs[m[1]] = m[2]; }
  
  const games = [];
  const gs = content.indexOf('export const games');
  if (gs !== -1) {
    const gc = content.substring(gs);
    const gr = /title:\s*['"](.+?)['"]/g;
    while ((m = gr.exec(gc)) !== null) games.push(m[1].trim());
  }
  
  return { subjectTitle, icon, color, lessons, descs, games, hasGames: gs !== -1 };
}

// Extract key terms and sentences from description
function extractKeywords(desc) {
  // Get sentences that define terms (:- or ** patterns)
  const sentences = desc.replace(/\n/g, ' ').split(/[.!]+/).map(s => s.trim()).filter(s => s.length > 20 && s.length < 200);
  // Extract bold terms
  const boldTerms = [...desc.matchAll(/\*\*([^*]+)\*\*/g)].map(m => m[1].trim()).filter(t => t.length > 3 && t.length < 60);
  // Extract terms after :- or :
  const defTerms = [...desc.matchAll(/[>\-!]\s*\*?([^*:—\n]{3,50})\*?\s*[—:–-]/g)].map(m => m[1].trim()).filter(t => t.length > 3);
  return { sentences, boldTerms, defTerms };
}

// Shuffle array
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

// Generate distractors from other parts of the text
function generateDistractors(correct, allTerms, context, count = 4) {
  const distractors = [];
  // Use other terms from the same lesson
  const others = allTerms.filter(t => t !== correct && t.length > 2 && t.length < 50);
  for (const t of shuffle(others)) {
    if (distractors.length >= count) break;
    if (!distractors.includes(t) && t !== correct) distractors.push(t);
  }
  // Fill with generic distractors if needed
  const generic = ['Всё вышеперечисленное', 'Ни один из вариантов', 'Только A и B', 'Зависит от контекста', 'Не применяется', 'Только в теории', 'Во всех случаях', 'Ни в каком из случаев'];
  while (distractors.length < count) {
    const g = generic[Math.floor(Math.random() * generic.length)];
    if (!distractors.includes(g) && g !== correct) distractors.push(g);
  }
  return distractors.slice(0, count);
}

function generateTestForLesson(lessonTitle, desc, subjectTitle, icon, color, allDescs) {
  const { sentences, boldTerms, defTerms } = extractKeywords(desc);
  const allBold = Object.values(allDescs).flatMap(d => {
    const { boldTerms: bt } = extractKeywords(d);
    return bt;
  });
  
  const topic = lessonTitle.replace(/Урок\s*\d+\s*[:\-]?\s*/, '').trim() || lessonTitle;
  const emojis = ['📚', '🎯', '🧠', '💡', '✨', '🏆', '⭐', '🔑', '📝', '🔍'];
  const emoji = emojis[Math.floor(Math.random() * emojis.length)];
  
  const tasks = [];
  
  // Question type 1: Definition question
  if (defTerms.length >= 2) {
    const term = defTerms[Math.floor(Math.random() * defTerms.length)];
    // Find the definition
    const defMatch = desc.match(new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '[^.\n]{5,100}'));
    const definition = defMatch ? defMatch[0].replace(/^[—:–-]\s*/, '').trim().substring(0, 80) : 'основное понятие темы';
    const distractors = generateDistractors(term, [...allBold, ...defTerms], desc);
    const options = shuffle([term, ...distractors]);
    tasks.push({
      type: 'quiz',
      question: `Что означает термин "${definition.substring(0, 50)}..."?`,
      options,
      correctAnswer: term,
      hint: `Этот термин связан с темой: ${topic}`
    });
  }
  
  // Question type 2: Bold term question
  if (boldTerms.length >= 2) {
    const idx = Math.floor(Math.random() * Math.min(boldTerms.length, 8));
    const term = boldTerms[idx];
    if (term.length > 3 && term.length < 50) {
      const distractors = generateDistractors(term, [...allBold, ...defTerms], desc);
      const options = shuffle([term, ...distractors]);
      tasks.push({
        type: 'quiz',
        question: `Какое понятие относится к теме "${topic}"?`,
        options,
        correctAnswer: term,
        hint: `Ответ связан с уроком: ${topic}`
      });
    }
  }
  
  // Question type 3: Sentence-based question
  if (sentences.length >= 3) {
    const s = sentences[Math.floor(Math.random() * Math.min(sentences.length, 6))];
    // Extract key fact from sentence
    const factMatch = s.match(/(.{10,80})\s*$/);
    const fact = factMatch ? factMatch[1].trim() : s.trim().substring(0, 80);
    const words = fact.split(' ').filter(w => w.length > 3).slice(-4);
    const keyWord = words[words.length - 1] || topic;
    const distractors = generateDistractors(keyWord, [...allBold, ...defTerms, ...boldTerms], desc);
    const options = shuffle([keyWord, ...distractors]);
    tasks.push({
      type: 'quiz',
      question: `Какое из следующих утверждений верно относительно темы "${topic}"?`,
      options,
      correctAnswer: keyWord,
      hint: `Обратите внимание на ключевое слово в описании урока`
    });
  }
  
  // Question type 4: Find correct answers
  if (boldTerms.length >= 5) {
    const selected = shuffle(boldTerms).slice(0, 3);
    const extra = shuffle(boldTerms.filter(t => !selected.includes(t))).slice(0, 3);
    const options = shuffle([...selected, ...extra]);
    tasks.push({
      type: 'find',
      question: `Выберите понятия, связанные с темой "${topic}":`,
      options,
      correctAnswer: selected,
      hint: `Ищите термины, которые встречаются в уроке ${topic}`
    });
  }
  
  // Question type 5: Topic question
  if (sentences.length >= 2) {
    const s2 = sentences[Math.min(1, sentences.length - 1)];
    const keyPhrase = s2.split(',')[0].trim().substring(0, 60);
    const distractors = generateDistractors(keyPhrase, [...boldTerms, ...defTerms], desc);
    const options = shuffle([keyPhrase, ...distractors]);
    tasks.push({
      type: 'quiz',
      question: `Что является основным понятием урока "${topic}"?`,
      options,
      correctAnswer: keyPhrase,
      hint: `Ответ содержится в описании урока`
    });
  }
  
  // Fallback questions if we don't have enough
  while (tasks.length < 5) {
    const t = boldTerms[tasks.length % Math.max(boldTerms.length, 1)] || topic;
    const distractors = generateDistractors(t, [...allBold, ...defTerms], desc);
    const options = shuffle([t, ...distractors]);
    tasks.push({
      type: 'quiz',
      question: `Вопрос ${tasks.length + 1} по теме "${topic}"`,
      options,
      correctAnswer: t,
      hint: `Ответ связан с материалом урока`
    });
  }
  
  return tasks.slice(0, 5);
}

function formatTestAsTS(testTitle, subjectTitle, icon, color, tasks) {
  const tasksStr = tasks.map(t => {
    const ca = JSON.stringify(t.correctAnswer);
    return `      { type: '${t.type}', question: ${JSON.stringify(t.question)}, options: ${JSON.stringify(t.options)}, correctAnswer: ${ca}, hint: ${JSON.stringify(t.hint)} }`;
  }).join(',\n');
  
  return `  {
    title: ${JSON.stringify(testTitle)},
    subject: ${JSON.stringify(subjectTitle)},
    icon: ${JSON.stringify(icon)},
    color: ${JSON.stringify(color)},
    tasks: [\n${tasksStr}\n    ],
    reward: { stars: 3, message: ${JSON.stringify('Отлично! Ты справился! 🎉')} }
  }`;
}

async function main() {
  const content = fs.readFileSync(filePath, 'utf-8');
  const info = extractInfo(content);
  
  if (!info.subjectTitle) { console.log('ERROR: No subject title'); process.exit(1); }
  console.log(`Subject: ${info.subjectTitle}, Lessons: ${info.lessons.length}, Games: ${info.games.length}`);
  
  // Find uncovered lessons
  const covered = new Set();
  for (const g of info.games) {
    for (const l of info.lessons) {
      const lw = l.toLowerCase().replace(/урок\s*\d+\s*[:\-]?\s*/, '').trim().split(' ').slice(0, 3);
      const gw = g.toLowerCase().split(' ').slice(0, 3);
      if (lw.some(w => w.length > 2 && gw.some(gw2 => gw2.includes(w) || w.includes(gw2)))) covered.add(l);
    }
  }
  
  let needTests = info.lessons.filter(l => !covered.has(l));
  if (needTests.length < count) needTests = info.lessons.slice(info.games.length);
  needTests = needTests.slice(0, count);
  
  if (needTests.length === 0) { console.log('No lessons need tests'); process.exit(0); }
  
  const allDescs = info.descs;
  const testEntries = [];
  
  for (const lt of needTests) {
    const desc = allDescs[lt] || '';
    const topic = lt.replace(/Урок\s*\d+\s*[:\-]?\s*/, '').trim();
    const tasks = generateTestForLesson(lt, desc, info.subjectTitle, info.icon, info.color, allDescs);
    testEntries.push(formatTestAsTS(`${topic} 📚`, info.subjectTitle, info.icon, info.color, tasks));
  }
  
  const testsCode = testEntries.join(',\n');
  let newContent = content;
  
  if (!info.hasGames) {
    if (!content.includes('GameLesson')) {
      newContent = content.replace(/import\s*\{([^}]+)\}\s*from/, (match, imp) => `import { ${imp}, GameLesson } from`);
    }
    newContent = newContent + `\n\nexport const games: GameLesson[] = [\n${testsCode}\n]\n`;
  } else {
    const gsIdx = newContent.indexOf('export const games');
    let bc = 0, as = -1, ae = -1;
    for (let i = gsIdx; i < newContent.length; i++) {
      if (newContent[i] === '[') { if (as === -1) as = i; bc++; }
      else if (newContent[i] === ']') { bc--; if (bc === 0) { ae = i; break; } }
    }
    if (ae === -1) { console.log('ERROR: No array end'); process.exit(1); }
    const arrC = newContent.substring(as + 1, ae).trim();
    if (arrC === '' || arrC === '[]') {
      newContent = newContent.substring(0, gsIdx) + `export const games: GameLesson[] = [\n${testsCode}\n]` + newContent.substring(ae + 1);
    } else {
      newContent = newContent.substring(0, ae) + ',\n' + testsCode + newContent.substring(ae);
    }
  }
  
  fs.writeFileSync(filePath, newContent);
  console.log(`Generated ${testEntries.length} tests (template-based). Done!`);
}

main().catch(e => { console.error(e); process.exit(1); });
