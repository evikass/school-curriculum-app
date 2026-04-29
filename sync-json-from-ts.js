#!/usr/bin/env node

/**
 * Sync JSON data files from TypeScript source files.
 *
 * For each grade (0-11) and subject that has both a TS file and JSON file:
 *   1. Reads the TS file and extracts the games array data (titles, metadata, tasks)
 *   2. Reads the corresponding JSON file
 *   3. Updates the JSON file's games array to match what's in the TS file
 *   4. Specifically:
 *      - Updates game titles to match TS (positional matching)
 *      - Adds new games that exist in TS but not in JSON
 *      - Keeps the JSON structure intact (lessons data, etc.)
 */

const fs = require('fs');
const path = require('path');

const BASE_DIR = path.resolve(__dirname);
const SRC_GRADES_DIR = path.join(BASE_DIR, 'src', 'data', 'grades');
const PUBLIC_GRADES_DIR = path.join(BASE_DIR, 'public', 'data', 'grades');

// ── Helpers ──────────────────────────────────────────────────────────────────

/**
 * Extract the games section text from a TS file.
 * Handles both `export const games = [...]` and `export const games: GameLesson[] = [...]`
 */
function extractGamesSection(tsContent) {
  // Find the start of the games export
  const gamesStartRegex = /export\s+const\s+games\s*(?::\s*\w+(?:\[\])?\s*)?\s*=\s*\[/;
  const match = gamesStartRegex.exec(tsContent);
  if (!match) return null;

  const startIdx = match.index;
  // Find the opening bracket of the array
  const arrayStart = tsContent.indexOf('[', startIdx);
  if (arrayStart === -1) return null;

  // Walk the string to find the matching closing bracket
  let depth = 0;
  let i = arrayStart;
  while (i < tsContent.length) {
    const ch = tsContent[i];
    if (ch === '[') depth++;
    else if (ch === ']') {
      depth--;
      if (depth === 0) {
        return tsContent.substring(startIdx, i + 1);
      }
    }
    // Skip string literals so brackets inside them don't count
    if (ch === "'" || ch === '"' || ch === '`') {
      const quote = ch;
      i++;
      while (i < tsContent.length) {
        if (tsContent[i] === '\\') { i += 2; continue; }
        if (tsContent[i] === quote) break;
        i++;
      }
    }
    i++;
  }
  return null;
}

/**
 * Extract individual game objects' raw text from the games array section.
 * Splits on top-level objects within the array.
 */
function splitGameObjects(gamesSection) {
  // Find the opening [ and closing ]
  const arrayStart = gamesSection.indexOf('[');
  const inner = gamesSection.substring(arrayStart + 1);
  
  const objects = [];
  let depth = 0;
  let objStart = -1;
  let i = 0;
  
  while (i < inner.length) {
    const ch = inner[i];
    
    if (ch === '{') {
      if (depth === 0) objStart = i;
      depth++;
    } else if (ch === '}') {
      depth--;
      if (depth === 0 && objStart !== -1) {
        objects.push(inner.substring(objStart, i + 1));
        objStart = -1;
      }
    }
    
    // Skip string literals
    if (ch === "'" || ch === '"' || ch === '`') {
      const quote = ch;
      i++;
      while (i < inner.length) {
        if (inner[i] === '\\') { i += 2; continue; }
        if (inner[i] === quote) break;
        i++;
      }
    }
    i++;
  }
  
  return objects;
}

/**
 * Extract a string property value from a game object text.
 * Handles both single and double quoted strings.
 */
function extractStringProperty(objText, propName) {
  // Match property: 'value' or property: "value"
  const regex = new RegExp(propName + '\\s*:\\s*["\']([^"\']*)["\']');
  const match = regex.exec(objText);
  return match ? match[1] : null;
}

/**
 * Extract the tasks array from a game object text.
 * This is complex because tasks contain nested objects.
 * We'll extract the raw text and attempt a basic parse.
 */
function extractTasksSection(objText) {
  const tasksRegex = /tasks\s*:\s*\[/;
  const match = tasksRegex.exec(objText);
  if (!match) return null;

  const startIdx = match.index + match[0].length - 1; // position of '['
  let depth = 0;
  let i = startIdx;
  
  while (i < objText.length) {
    const ch = objText[i];
    if (ch === '[') depth++;
    else if (ch === ']') {
      depth--;
      if (depth === 0) {
        return objText.substring(startIdx, i + 1);
      }
    }
    if (ch === "'" || ch === '"' || ch === '`') {
      const quote = ch;
      i++;
      while (i < objText.length) {
        if (objText[i] === '\\') { i += 2; continue; }
        if (objText[i] === quote) break;
        i++;
      }
    }
    i++;
  }
  return null;
}

/**
 * Extract the reward object from a game object text.
 */
function extractRewardSection(objText) {
  const rewardRegex = /reward\s*:\s*\{/;
  const match = rewardRegex.exec(objText);
  if (!match) return null;

  const startIdx = match.index + match[0].length - 1; // position of '{'
  let depth = 0;
  let i = startIdx;
  
  while (i < objText.length) {
    const ch = objText[i];
    if (ch === '{') depth++;
    else if (ch === '}') {
      depth--;
      if (depth === 0) {
        return objText.substring(startIdx, i + 1);
      }
    }
    if (ch === "'" || ch === '"' || ch === '`') {
      const quote = ch;
      i++;
      while (i < objText.length) {
        if (objText[i] === '\\') { i += 2; continue; }
        if (objText[i] === quote) break;
        i++;
      }
    }
    i++;
  }
  return null;
}

/**
 * Parse a reward section like `{ stars: 3, message: "foo" }` into an object.
 */
function parseReward(rewardText) {
  if (!rewardText) return { stars: 3, message: 'Отлично! 🎉' };
  
  const starsMatch = /stars\s*:\s*(\d+)/.exec(rewardText);
  const msgMatch = /message\s*:\s*["']([^"']*)["']/.exec(rewardText);
  
  return {
    stars: starsMatch ? parseInt(starsMatch[1]) : 3,
    message: msgMatch ? msgMatch[1] : 'Отлично! 🎉'
  };
}

/**
 * Extract task objects from the tasks array text.
 * Each task has at minimum: type, question, correctAnswer, hint
 * We'll parse them as best we can with regex.
 */
function parseTasks(tasksText) {
  if (!tasksText) return [];
  
  // Split into individual task objects
  const taskObjects = [];
  let depth = 0;
  let objStart = -1;
  let i = 0;
  
  // Skip the opening bracket
  if (tasksText[0] === '[') i = 1;
  
  while (i < tasksText.length) {
    const ch = tasksText[i];
    
    if (ch === '{') {
      if (depth === 0) objStart = i;
      depth++;
    } else if (ch === '}') {
      depth--;
      if (depth === 0 && objStart !== -1) {
        taskObjects.push(tasksText.substring(objStart, i + 1));
        objStart = -1;
      }
    }
    
    if (ch === "'" || ch === '"' || ch === '`') {
      const quote = ch;
      i++;
      while (i < tasksText.length) {
        if (tasksText[i] === '\\') { i += 2; continue; }
        if (tasksText[i] === quote) break;
        i++;
      }
    }
    i++;
  }
  
  // Parse each task object into a JS object
  return taskObjects.map(taskText => {
    const typeMatch = /type\s*:\s*['"](\w+)['"]/.exec(taskText);
    const questionMatch = /question\s*:\s*['"`]([^'"`]*?)['"`]/.exec(taskText);
    const correctAnswerMatch = /correctAnswer\s*:\s*['"`]([^'"`]*?)['"`]/.exec(taskText);
    const hintMatch = /hint\s*:\s*['"`]([^'"`]*?)['"`]/.exec(taskText);
    
    const task = {};
    if (typeMatch) task.type = typeMatch[1];
    if (questionMatch) task.question = questionMatch[1];
    if (correctAnswerMatch) task.correctAnswer = correctAnswerMatch[1];
    if (hintMatch) task.hint = hintMatch[1];
    
    // Try to extract options array (simplified - just string elements)
    const optionsMatch = /options\s*:\s*\[([^\]]*)\]/s.exec(taskText);
    if (optionsMatch) {
      const optsStr = optionsMatch[1];
      const opts = [];
      const optRegex = /['"]([^'"]*)['"]/g;
      let optMatch;
      while ((optMatch = optRegex.exec(optsStr)) !== null) {
        opts.push(optMatch[1]);
      }
      if (opts.length > 0) task.options = opts;
    }
    
    return task;
  });
}

/**
 * Extract game data from a TS file.
 * Returns an array of game objects with title, subject, icon, color, tasks, reward.
 */
function extractGamesFromTS(tsContent) {
  const gamesSection = extractGamesSection(tsContent);
  if (!gamesSection) return [];

  const gameObjects = splitGameObjects(gamesSection);
  
  return gameObjects.map(objText => {
    const title = extractStringProperty(objText, 'title');
    const subject = extractStringProperty(objText, 'subject');
    const icon = extractStringProperty(objText, 'icon');
    const color = extractStringProperty(objText, 'color');
    
    const tasksText = extractTasksSection(objText);
    const tasks = parseTasks(tasksText);
    
    const rewardText = extractRewardSection(objText);
    const reward = parseReward(rewardText);
    
    return {
      title,
      subject: subject || '',
      icon: icon || 'BookOpen',
      color: color || 'text-blue-400',
      tasks,
      reward
    };
  }).filter(g => g.title); // Filter out any games where title couldn't be extracted
}

/**
 * Create a basic game entry for a new game from TS data.
 */
function createNewGameEntry(tsGame) {
  const game = {
    title: tsGame.title,
    subject: tsGame.subject,
    icon: tsGame.icon,
    color: tsGame.color,
    tasks: [],
    reward: tsGame.reward || { stars: 3, message: 'Отлично! 🎉' }
  };
  
  // If we managed to extract tasks from TS, use them
  if (tsGame.tasks && tsGame.tasks.length > 0) {
    game.tasks = tsGame.tasks;
  } else {
    // Create a placeholder task
    game.tasks = [
      {
        type: 'quiz',
        question: `Вопрос по теме: ${tsGame.title}`,
        options: ['Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4', 'Другой ответ'],
        correctAnswer: 'Вариант 1',
        hint: 'Подумай и вспомни правило'
      }
    ];
  }
  
  return game;
}

// ── Main Sync Logic ──────────────────────────────────────────────────────────

function syncGradeSubject(grade, subject) {
  const tsPath = path.join(SRC_GRADES_DIR, String(grade), subject, 'index.ts');
  const jsonPath = path.join(PUBLIC_GRADES_DIR, String(grade), `${subject}.json`);
  
  // Check both files exist
  if (!fs.existsSync(tsPath)) {
    return { status: 'skip', reason: 'no TS file' };
  }
  if (!fs.existsSync(jsonPath)) {
    return { status: 'skip', reason: 'no JSON file' };
  }
  
  // Read both files
  const tsContent = fs.readFileSync(tsPath, 'utf-8');
  const jsonContent = fs.readFileSync(jsonPath, 'utf-8');
  
  // Extract games from TS
  const tsGames = extractGamesFromTS(tsContent);
  if (tsGames.length === 0) {
    return { status: 'skip', reason: 'no games in TS' };
  }
  
  // Parse JSON
  let jsonData;
  try {
    jsonData = JSON.parse(jsonContent);
  } catch (e) {
    return { status: 'error', reason: `JSON parse error: ${e.message}` };
  }
  
  // Get current JSON games
  const jsonGames = jsonData.games || [];
  
  // Build updated games array
  const updatedGames = [];
  const changes = [];
  
  for (let i = 0; i < tsGames.length; i++) {
    const tsGame = tsGames[i];
    
    if (i < jsonGames.length) {
      // Positional match - update the title
      const oldTitle = jsonGames[i].title;
      const newTitle = tsGame.title;
      
      if (oldTitle !== newTitle) {
        changes.push(`  Game ${i + 1}: "${oldTitle}" → "${newTitle}"`);
        // Update the title in the existing JSON game entry
        jsonGames[i].title = newTitle;
        // Also update subject/icon/color if they differ
        if (tsGame.subject && tsGame.subject !== jsonGames[i].subject) {
          jsonGames[i].subject = tsGame.subject;
        }
        if (tsGame.icon && tsGame.icon !== jsonGames[i].icon) {
          jsonGames[i].icon = tsGame.icon;
        }
        if (tsGame.color && tsGame.color !== jsonGames[i].color) {
          jsonGames[i].color = tsGame.color;
        }
      }
      updatedGames.push(jsonGames[i]);
    } else {
      // New game - doesn't exist in JSON yet
      changes.push(`  Game ${i + 1}: NEW "${tsGame.title}"`);
      const newEntry = createNewGameEntry(tsGame);
      updatedGames.push(newEntry);
    }
  }
  
  // Check if any JSON games were removed (more games in JSON than TS)
  if (jsonGames.length > tsGames.length) {
    for (let i = tsGames.length; i < jsonGames.length; i++) {
      changes.push(`  Game ${i + 1}: REMOVED "${jsonGames[i].title}"`);
    }
    // We don't include the extra JSON games in updatedGames
  }
  
  if (changes.length === 0) {
    return { status: 'unchanged', tsCount: tsGames.length, jsonCount: jsonGames.length };
  }
  
  // Update the JSON data
  jsonData.games = updatedGames;
  
  // Write back
  fs.writeFileSync(jsonPath, JSON.stringify(jsonData, null, 2) + '\n', 'utf-8');
  
  return {
    status: 'updated',
    tsCount: tsGames.length,
    jsonCount: jsonGames.length,
    newCount: updatedGames.length,
    changes
  };
}

function main() {
  console.log('═'.repeat(60));
  console.log('  Sync JSON from TypeScript — School Curriculum App');
  console.log('═'.repeat(60));
  console.log();
  
  const stats = {
    processed: 0,
    updated: 0,
    unchanged: 0,
    skipped: 0,
    errors: 0
  };
  
  // Iterate over grades 0-11
  for (let grade = 0; grade <= 11; grade++) {
    const gradeDir = path.join(SRC_GRADES_DIR, String(grade));
    if (!fs.existsSync(gradeDir)) continue;
    
    // Get subject directories
    const entries = fs.readdirSync(gradeDir, { withFileTypes: true });
    const subjects = entries
      .filter(e => e.isDirectory())
      .map(e => e.name)
      .filter(name => !name.startsWith('_') && !name.startsWith('.'));
    
    for (const subject of subjects) {
      stats.processed++;
      const result = syncGradeSubject(grade, subject);
      
      const label = `Grade ${grade}/${subject}`;
      
      switch (result.status) {
        case 'updated':
          stats.updated++;
          console.log(`✅ ${label}: UPDATED (${result.jsonCount} → ${result.newCount} games)`);
          result.changes.forEach(c => console.log(c));
          console.log();
          break;
        case 'unchanged':
          stats.unchanged++;
          console.log(`⏭️  ${label}: unchanged (${result.tsCount} games match)`);
          break;
        case 'skip':
          stats.skipped++;
          console.log(`⏭️  ${label}: skipped (${result.reason})`);
          break;
        case 'error':
          stats.errors++;
          console.log(`❌ ${label}: ERROR — ${result.reason}`);
          break;
      }
    }
  }
  
  console.log();
  console.log('═'.repeat(60));
  console.log('  Summary');
  console.log('═'.repeat(60));
  console.log(`  Processed: ${stats.processed}`);
  console.log(`  Updated:   ${stats.updated}`);
  console.log(`  Unchanged: ${stats.unchanged}`);
  console.log(`  Skipped:   ${stats.skipped}`);
  console.log(`  Errors:    ${stats.errors}`);
  console.log();
  
  if (stats.updated > 0) {
    console.log('✅ JSON files have been synced with TypeScript source.');
  } else if (stats.unchanged === stats.processed) {
    console.log('ℹ️  All JSON files are already in sync.');
  }
}

main();
