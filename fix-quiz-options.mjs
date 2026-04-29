#!/usr/bin/env node
/**
 * Script to replace meaningless quiz options ("Никто не знает", "Не знаю")
 * with meaningful, non-duplicate alternatives using LLM.
 * 
 * Handles both single-line and multi-line quiz formats.
 * 
 * Usage: node fix-quiz-options.mjs [grade] [subject]
 */

import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const GRADES_DIR = '/home/z/my-project/school-curriculum-app/src/data/grades';
const FILLER_STRINGS = ['Никто не знает', 'Не знаю', 'никто не знает', 'не знаю'];

function hasFiller(text) {
  return FILLER_STRINGS.some(p => text.includes(p));
}

function isFillerOption(opt) {
  const trimmed = opt.trim();
  return FILLER_STRINGS.includes(trimmed);
}

function extractQuizzes(content) {
  const quizzes = [];
  
  // Match quiz objects - both single-line and multi-line formats
  // Pattern: { type: 'quiz', ... options: [...], ... }
  // We'll find options arrays that contain filler strings, then find the surrounding quiz object
  
  // Find all options arrays with fillers
  const optionsRegex = /options:\s*\[([^\]]+)\]/g;
  let optMatch;
  
  while ((optMatch = optionsRegex.exec(content)) !== null) {
    const optionsStr = optMatch[1];
    
    if (!hasFiller(optionsStr)) continue;
    
    // Parse individual options
    const options = [];
    const optValRegex = /['"]([^'"]*?)['"]/g;
    let valMatch;
    while ((valMatch = optValRegex.exec(optionsStr)) !== null) {
      options.push(valMatch[1]);
    }
    
    const fillerIndices = [];
    options.forEach((opt, idx) => {
      if (isFillerOption(opt)) {
        fillerIndices.push(idx);
      }
    });
    
    if (fillerIndices.length === 0) continue;
    
    // Now find the enclosing quiz object
    // Search backwards from the options match to find the opening {
    let objStart = optMatch.index;
    let braceCount = 0;
    for (let i = objStart; i >= 0; i--) {
      if (content[i] === '}') braceCount++;
      if (content[i] === '{') {
        if (braceCount === 0) {
          objStart = i;
          break;
        }
        braceCount--;
      }
    }
    
    // Search forward from options match to find the closing }
    let objEnd = optMatch.index + optMatch[0].length;
    braceCount = 0;
    let foundFirst = false;
    for (let i = objStart; i < content.length; i++) {
      if (content[i] === '{') {
        braceCount++;
        foundFirst = true;
      } else if (content[i] === '}') {
        braceCount--;
      }
      if (foundFirst && braceCount === 0) {
        objEnd = i + 1;
        break;
      }
    }
    
    const quizBlock = content.substring(objStart, objEnd);
    
    // Verify this is a quiz type
    if (!quizBlock.includes("type: 'quiz'") && !quizBlock.includes('type: "quiz"')) continue;
    
    // Extract question
    const questionMatch = quizBlock.match(/question:\s*['"](.+?)['"]/);
    if (!questionMatch) continue;
    const question = questionMatch[1];
    
    // Extract correctAnswer
    const correctMatch = quizBlock.match(/correctAnswer:\s*['"](.+?)['"]/);
    if (!correctMatch) continue;
    const correctAnswer = correctMatch[1];
    
    // Extract the options array string for later replacement
    const optionsArrayMatch = quizBlock.match(/options:\s*\[[^\]]+\]/);
    if (!optionsArrayMatch) continue;
    
    quizzes.push({
      question,
      options,
      correctAnswer,
      fillerIndices,
      optionsArrayStr: optionsArrayMatch[0],
      objStart,
      objEnd,
      quizBlock
    });
  }
  
  return quizzes;
}

function generateFallback(quiz, idx, existingOpts, subject) {
  const correct = quiz.correctAnswer;
  const existing = new Set(existingOpts.map(o => o.toLowerCase().trim()));
  existing.add(correct.toLowerCase().trim());
  
  // For numeric answers: try nearby numbers
  const numMatch = correct.match(/^(\d+)$/);
  if (numMatch) {
    const num = parseInt(numMatch[1]);
    const candidates = [num - 2, num - 1, num + 1, num + 2, num * 2, num + 3, num - 3, num + 5, num - 5].filter(n => n >= 0);
    for (const c of candidates) {
      if (!existing.has(String(c))) return String(c);
    }
  }
  
  // Subject-based fallbacks
  const subjectFallbacks = {
    math: ['0', '1', '2', '3', '5', '6', '7', '8', '10', '12', '15', '20', '25', '30', '50', '100'],
    russian: ['Слово', 'Буква', 'Звук', 'Слог', 'Предложение', 'Текст', 'Речь', 'Ударение', 'Гласный', 'Согласный'],
    reading: ['Автор', 'Герой', 'Сказка', 'Рассказ', 'Стих', 'Книга', 'Страница', 'Глава', 'Заголовок', 'Писатель'],
    world: ['Природа', 'Земля', 'Вода', 'Воздух', 'Растение', 'Животное', 'Человек', 'Погода', 'Озеро', 'Лес'],
    music: ['Песня', 'Танец', 'Ритм', 'Нота', 'Мелодия', 'Хор', 'Пианино', 'Громко', 'Тихо', 'Оркестр'],
    art: ['Краски', 'Кисть', 'Линия', 'Цвет', 'Рисунок', 'Холст', 'Палитра', 'Тень', 'Форма', 'Контур'],
    pe: ['Бег', 'Прыжок', 'Мяч', 'Спорт', 'Упражнение', 'Зарядка', 'Сила', 'Ловкость', 'Команда', 'Эстафета'],
    craft: ['Бумага', 'Клей', 'Ножницы', 'Карандаш', 'Краска', 'Линейка', 'Ластик', 'Пластилин', 'Картон', 'Объём'],
    english: ['Hello', 'Yes', 'No', 'Good', 'Cat', 'Dog', 'Book', 'Apple', 'Red', 'Big'],
    literature: ['Поэмa', 'Роман', 'Стихотворение', 'Басня', 'Пьеса', 'Проза', 'Сказ', 'Очерк', 'Былина', 'Комедия'],
    tech: ['Инструмент', 'Деталь', 'Механизм', 'Материал', 'Чертёж', 'Модель', 'Конструкция', 'Схема', 'Сборка', 'Разметка'],
    projects: ['План', 'Идея', 'Цель', 'Задача', 'Результат', 'Команда', 'Презентация', 'Исследование', 'Гипотеза', 'Вывод'],
    informatics: ['Файл', 'Папка', 'Код', 'Программа', 'Экран', 'Клавиатура', 'Мышь', 'Данные', 'Сеть', 'Сайт'],
    robotics: ['Мотор', 'Датчик', 'Робот', 'Алгоритм', 'Цикл', 'Команда', 'Сборка', 'Контроллер', 'Сервопривод', 'Шестерёнка'],
    safety: ['Опасность', 'Правило', 'Знак', 'Осторожно', 'Пожар', 'Дорога', 'Телефон', 'Помощь', 'Эвакуация', 'Аптечка'],
    ethics: ['Добро', 'Зло', 'Совесть', 'Долг', 'Честь', 'Справедливость', 'Милосердие', 'Ответственность', 'Уважение', 'Терпение'],
  };
  
  const fallbacks = subjectFallbacks[subject] || subjectFallbacks.world;
  
  for (const fb of fallbacks) {
    if (!existing.has(fb.toLowerCase().trim())) {
      return fb;
    }
  }
  
  return `Вариант ${idx + 1}`;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function generateReplacementsForBatch(zai, quizzes, subject, grade) {
  const batchSize = 10;
  const allReplacements = [];
  
  for (let i = 0; i < quizzes.length; i += batchSize) {
    // Add delay between batches to avoid rate limiting
    if (i > 0) await sleep(3000);
    const batch = quizzes.slice(i, i + batchSize);
    
    const questionsText = batch.map((q, idx) => {
      const realOptions = q.options.filter((_, i) => !q.fillerIndices.includes(i));
      return `${idx + 1}. Вопрос: "${q.question}"
   Правильный ответ: "${q.correctAnswer}"
   УЖЕ ЕСТЬ варианты (НЕ ПОВТОРЯЙ): ${realOptions.map(o => `"${o}"`).join(', ')}
   Нужно ${q.fillerIndices.length} НОВЫХ варианта`;
    }).join('\n\n');
    
    const prompt = `Замени бессмысленные варианты ("Никто не знает", "Не знаю") в тестах для ${grade} класса по "${subject}".

СТРОГИЕ ПРАВИЛА:
1. Каждый НОВЫЙ вариант УНИКАЛЕН — НЕ ПОВТОРЯТЬ уже существующие варианты
2. Каждый НОВЫЙ вариант — НЕПРАВИЛЬНЫЙ (правильный уже есть)
3. Каждый НОВЫЙ вариант тематически связан с вопросом и правдоподобен
4. ЗАПРЕЩЕНО: "не знаю", "никто не знает", "другой", "-", "затрудняюсь"
5. Все варианты в одном вопросе отличаются друг от друга

${questionsText}

JSON массив. Каждый элемент — массив из строк-замен:
[["замена1", "замена2"], ...]`;

    try {
      const completion = await zai.chat.completions.create({
        messages: [
          { role: 'system', content: 'Ты создаёшь тесты для школы. Ответ ТОЛЬКО JSON. Варианты уникальны, не дублируют существующие. Неправильные но правдоподобные.' },
          { role: 'user', content: prompt }
        ],
        temperature: 0.8,
        max_tokens: 4000
      });
      
      let responseText = completion.choices[0]?.message?.content || '';
      responseText = responseText.replace(/```json\s*/g, '').replace(/```\s*/g, '').trim();
      
      const replacements = JSON.parse(responseText);
      
      for (let j = 0; j < batch.length && j < replacements.length; j++) {
        let opts = Array.isArray(replacements[j]) ? replacements[j] : [String(replacements[j])];
        
        // Post-process: validate no duplicates with existing
        const existingOpts = batch[j].options.filter((_, i) => !batch[j].fillerIndices.includes(i));
        const allExisting = new Set(existingOpts.map(o => o.toLowerCase().trim()));
        allExisting.add(batch[j].correctAnswer.toLowerCase().trim());
        
        const validatedOpts = [];
        const usedInThisRound = new Set();
        
        for (const opt of opts) {
          const optKey = opt.toLowerCase().trim();
          if (allExisting.has(optKey) || usedInThisRound.has(optKey) || FILLER_STRINGS.includes(opt.trim())) {
            validatedOpts.push(generateFallback(batch[j], validatedOpts.length, existingOpts, subject));
          } else {
            usedInThisRound.add(optKey);
            validatedOpts.push(opt);
          }
        }
        
        while (validatedOpts.length < batch[j].fillerIndices.length) {
          validatedOpts.push(generateFallback(batch[j], validatedOpts.length, existingOpts, subject));
        }
        
        allReplacements.push({
          quiz: batch[j],
          newOptions: validatedOpts
        });
      }
      
      console.log(`  Batch ${Math.floor(i/batchSize) + 1}: OK (${replacements.length} sets)`);
    } catch (error) {
      if (error.message && error.message.includes('429')) {
        console.log(`  Rate limited, waiting 10s before retry...`);
        await sleep(10000);
        try {
          const completion = await zai.chat.completions.create({
            messages: [
              { role: 'system', content: 'Ты создаёшь тесты для школы. Ответ ТОЛЬКО JSON. Варианты уникальны, не дублируют существующие. Неправильные но правдоподобные.' },
              { role: 'user', content: prompt }
            ],
            temperature: 0.8,
            max_tokens: 4000
          });
          
          let responseText = completion.choices[0]?.message?.content || '';
          responseText = responseText.replace(/```json\s*/g, '').replace(/```\s*/g, '').trim();
          const replacements = JSON.parse(responseText);
          
          for (let j = 0; j < batch.length && j < replacements.length; j++) {
            let opts = Array.isArray(replacements[j]) ? replacements[j] : [String(replacements[j])];
            const existingOpts = batch[j].options.filter((_, i) => !batch[j].fillerIndices.includes(i));
            const allExisting = new Set(existingOpts.map(o => o.toLowerCase().trim()));
            allExisting.add(batch[j].correctAnswer.toLowerCase().trim());
            const validatedOpts = [];
            const usedInThisRound = new Set();
            for (const opt of opts) {
              const optKey = opt.toLowerCase().trim();
              if (allExisting.has(optKey) || usedInThisRound.has(optKey) || FILLER_STRINGS.includes(opt.trim())) {
                validatedOpts.push(generateFallback(batch[j], validatedOpts.length, existingOpts, subject));
              } else {
                usedInThisRound.add(optKey);
                validatedOpts.push(opt);
              }
            }
            while (validatedOpts.length < batch[j].fillerIndices.length) {
              validatedOpts.push(generateFallback(batch[j], validatedOpts.length, existingOpts, subject));
            }
            allReplacements.push({ quiz: batch[j], newOptions: validatedOpts });
          }
          console.log(`  Batch ${Math.floor(i/batchSize) + 1}: OK after retry (${replacements.length} sets)`);
          continue;
        } catch (e2) {
          console.error(`  Retry also failed: ${e2.message}`);
        }
      }
      
      console.error(`  Batch error: ${error.message}, using fallbacks`);
      for (const q of batch) {
        const existingOpts = q.options.filter((_, i) => !q.fillerIndices.includes(i));
        const fallbacks = q.fillerIndices.map((_, idx) => generateFallback(q, idx, existingOpts, subject));
        allReplacements.push({ quiz: q, newOptions: fallbacks });
      }
    }
  }
  
  return allReplacements;
}

function applyReplacements(content, replacements) {
  // Sort by position descending so we replace from end to beginning
  const sorted = [...replacements].sort((a, b) => b.quiz.objStart - a.quiz.objStart);
  
  for (const { quiz, newOptions } of sorted) {
    const newOpts = [...quiz.options];
    for (let i = 0; i < quiz.fillerIndices.length && i < newOptions.length; i++) {
      newOpts[quiz.fillerIndices[i]] = newOptions[i];
    }
    
    // Final duplicate check
    const finalOpts = [];
    const seen = new Set();
    for (const opt of newOpts) {
      const key = opt.toLowerCase().trim();
      if (!seen.has(key)) {
        seen.add(key);
        finalOpts.push(opt);
      } else {
        const existingNonFiller = newOpts.filter((_, i) => !quiz.fillerIndices.includes(i));
        finalOpts.push(generateFallback(quiz, finalOpts.length, existingNonFiller, ''));
      }
    }
    
    // Build new options array string
    const newOptionsStr = finalOpts.map(o => `"${o}"`).join(', ');
    const newOptionsArray = `options: [${newOptionsStr}]`;
    
    // Replace in content
    const before = content.substring(0, quiz.objStart);
    const quizBlock = content.substring(quiz.objStart, quiz.objEnd);
    const after = content.substring(quiz.objEnd);
    
    const newQuizBlock = quizBlock.replace(quiz.optionsArrayStr, newOptionsArray);
    
    content = before + newQuizBlock + after;
  }
  
  return content;
}

async function processFile(zai, filePath, grade, subject) {
  console.log(`\nProcessing: Grade ${grade}/${subject}`);
  
  const content = fs.readFileSync(filePath, 'utf-8');
  const quizzes = extractQuizzes(content);
  
  if (quizzes.length === 0) {
    console.log(`  No filler options found. Skipping.`);
    return 0;
  }
  
  console.log(`  Found ${quizzes.length} quizzes with filler options`);
  
  const replacements = await generateReplacementsForBatch(zai, quizzes, subject, grade);
  console.log(`  Generated ${replacements.length} replacement sets`);
  
  const newContent = applyReplacements(content, replacements);
  
  const remaining = FILLER_STRINGS.reduce((count, p) => count + (newContent.split(p).length - 1), 0);
  if (remaining > 0) {
    console.log(`  WARNING: ${remaining} filler patterns still remain!`);
  } else {
    console.log(`  All filler options replaced!`);
  }
  
  fs.writeFileSync(filePath, newContent, 'utf-8');
  return quizzes.length;
}

async function main() {
  const targetGrade = process.argv[2];
  const targetSubject = process.argv[3];
  
  console.log('Initializing ZAI...');
  const zai = await ZAI.create();
  
  const grades = targetGrade ? [targetGrade] : ['0', '1', '2', '3'];
  let totalFixed = 0;
  
  for (const grade of grades) {
    const gradeDir = path.join(GRADES_DIR, grade);
    if (!fs.existsSync(gradeDir)) continue;
    
    const subjects = fs.readdirSync(gradeDir).filter(f => {
      return fs.statSync(path.join(gradeDir, f)).isDirectory();
    });
    
    for (const subject of subjects) {
      if (targetSubject && subject !== targetSubject) continue;
      
      const filePath = path.join(gradeDir, subject, 'index.ts');
      if (!fs.existsSync(filePath)) continue;
      
      try {
        const count = await processFile(zai, filePath, grade, subject);
        totalFixed += count;
      } catch (error) {
        console.error(`  Error processing ${grade}/${subject}: ${error.message}`);
      }
    }
  }
  
  console.log(`\n\nDone! Total quizzes fixed: ${totalFixed}`);
}

main().catch(console.error);
