import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';

const GRADE = parseInt(process.argv[2] || '9');
const START = parseInt(process.argv[3] || '1');
const COUNT = parseInt(process.argv[4] || '10');

const FILE_PATH = path.join(process.cwd(), 'public/data/grades', String(GRADE), 'biology.json');

// Emoji map for lesson topics
const TOPIC_EMOJIS = {
  'эволюц': '🧬',
  'строен': '🔬',
  'клетк': '🧫',
  'наследств': '🧪',
  'изменч': '🔄',
  'отбор': '⚡',
  'приспос': '🎯',
  'вид': '🔍',
  'популяц': '👥',
  'борьб': '⚔️',
  'макро': '🌍',
  'микро': '🦠',
  'развит': '🌱',
  'происх': '🦴',
  'обобщ': '📝',
  'обмен': '⚗️',
  'делен': '🔬',
  'ткан': '🫀',
  'орган': '🫁',
  'размнож': '🐣',
  'онтоген': '👶',
  'генет': '🧬',
  'мендел': '📊',
  'сцеплен': '🔗',
  'пол': '⚧️',
  'мутац': '☢️',
  'здоров': '🏥',
  'селекц': '🌾',
  'сред': '🌿',
  'биоцен': '🌳',
  'пищев': '🍕',
  'экос': '🌐',
  'охран': '🛡️',
  'человек': '🧑',
  'скелет': '💀',
  'кост': '🦴',
  'мышц': '💪',
  'кров': '🩸',
  'сердц': '❤️',
  'сосуд': '🫀',
  'дыхан': '🫁',
  'пищевар': '🍽️',
  'обмен': '⚡',
  'кож': '🧴',
  'термор': '🌡️',
  'почки': '🫘',
  'нерв': '🧠',
  'мозг': '🧠',
  'глаз': '👁️',
  'зр': '👁️',
  'слух': '👂',
  'обонян': '👃',
  'вкус': '👅',
  'повед': '🧠',
  'памят': '💭',
  'сон': '😴',
  'гормон': '💉',
  'желез': '🫃',
  'эндокр': '💉',
  'полов': '🧬',
  'бактер': '🦠',
  'гриб': '🍄',
  'водорос': '🌿',
  'мх': '🌱',
  'папорот': '🌿',
  'хвощ': '🌾',
  'плаун': '🌿',
  'голосем': '🌲',
  'покрытосем': '🌸',
  'цветк': '🌺',
  'двудоль': '🌼',
  'однодоль': '🌾',
  'сем': '🫘',
  'корн': '🌱',
  'побег': '🌿',
  'стебел': '🪵',
  'лист': '🍃',
  'почк': '🌱',
  'соцвет': '💐',
  'опылен': '🐝',
  'оплодотв': '🌸',
  'плод': '🍎',
  'систем': '📚',
  'сообществ': '🌲',
  'лишайник': '🔲',
  'фотосинт': '☀️',
  'дыхан': '💨',
  'минераль': '💎',
  'рост': '📈',
  'вегетат': '🌿',
  'взаимосв': '🔗',
  'биоценоз': '🌳',
  'влия': '🏭',
  'классиф': '📋',
  'значен': '⭐',
};

function getEmoji(title) {
  const lower = title.toLowerCase();
  for (const [key, emoji] of Object.entries(TOPIC_EMOJIS)) {
    if (lower.includes(key)) return emoji;
  }
  return '📚';
}

// Icon map
const ICON_MAP = {
  'эволюц': 'Dna',
  'клетк': 'Microscope',
  'наследств': 'FlaskConical',
  'генет': 'Dna',
  'орган': 'Heart',
  'кров': 'Droplets',
  'дыхан': 'Wind',
  'пищевар': 'Utensils',
  'нерв': 'Brain',
  'мышц': 'Dumbbell',
  'скелет': 'Bone',
  'эколог': 'TreePine',
  'бактер': 'Bug',
  'гриб': 'Mushroom',
  'растен': 'Leaf',
  'цветк': 'Flower2',
};

function getIcon(title) {
  const lower = title.toLowerCase();
  for (const [key, icon] of Object.entries(ICON_MAP)) {
    if (lower.includes(key)) return icon;
  }
  return 'BookOpenText';
}

async function generateQuestionsForLesson(zai, lesson, lessonIndex, grade) {
  const title = lesson.title;
  const description = lesson.description || '';
  const keyPoints = (lesson.keyPoints || []).join('\n');
  const facts = (lesson.facts || []).join('\n');
  const examples = (lesson.examples || []).join('\n');
  const tasks = (lesson.tasks || []).join('\n');

  // Take first 2000 chars of content to stay within token limits
  const contentSummary = (lesson.content || '').substring(0, 3000);

  const prompt = `Ты — опытный преподаватель биологии в российской школе. Создай 5 тестовых вопросов по уроку биологии для ${grade} класса.

УРОК: ${title}
ОПИСАНИЕ: ${description}
КЛЮЧЕВЫЕ ПОЛОЖЕНИЯ: ${keyPoints}
ФАКТЫ: ${facts}
ПРИМЕРЫ: ${examples}
ЗАДАЧИ УРОКА: ${tasks}
СОДЕРЖАНИЕ УРОКА (сокращённо): ${contentSummary}

ТРЕБОВАНИЯ К ВОПРОСАМ:
1. Каждый вопрос проверяет конкретное знание из урока
2. 4 варианта ответа (один правильный) + пятый вариант "Не знаю"
3. Правильный ответ должен быть первым в списке (я перемешаю позже)
4. Вопросы должны быть разнообразными: что/кто/какой/где/сколько/почему
5. Неправильные варианты должны быть правдоподобными, но однозначно неверными
6. Подсказка (hint) должна направлять к правильному ответу, не называя его

Ответь ТОЛЬКО валидным JSON-массивом из 5 объектов, без markdown:
[
  {
    "question": "Текст вопроса?",
    "options": ["Правильный ответ", "Неправильный 1", "Неправильный 2", "Неправильный 3", "Не знаю"],
    "correctAnswer": "Правильный ответ",
    "hint": "Подсказка"
  }
]`;

  try {
    const completion = await zai.chat.completions.create({
      messages: [
        { role: 'system', content: 'Ты — опытный преподаватель биологии. Отвечай ТОЛЬКО валидным JSON без markdown-обёрток.' },
        { role: 'user', content: prompt }
      ],
      temperature: 0.7,
      max_tokens: 2000,
    });

    let responseText = completion.choices[0]?.message?.content || '';
    // Clean up response - remove markdown code blocks if present
    responseText = responseText.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();

    const questions = JSON.parse(responseText);

    if (!Array.isArray(questions) || questions.length < 5) {
      console.error(`  Lesson ${lessonIndex + 1}: Got ${questions?.length || 0} questions, expected 5. Retrying...`);
      return null;
    }

    // Shuffle options for each question (move correct answer from position 0 to random position)
    const processedQuestions = questions.map(q => {
      const correctAnswer = q.correctAnswer;
      let options = [...q.options];

      // Remove "Не знаю" if present, we'll add it at the end
      const neZnayuIdx = options.indexOf('Не знаю');
      if (neZnayuIdx >= 0) options.splice(neZnayuIdx, 1);

      // Ensure correct answer is in options
      if (!options.includes(correctAnswer)) {
        options[0] = correctAnswer;
      }

      // Shuffle the non-"Не знаю" options
      for (let i = options.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [options[i], options[j]] = [options[j], options[i]];
      }

      // Add "Не знаю" at the end
      options.push('Не знаю');

      return {
        type: 'quiz',
        question: q.question,
        options: options,
        correctAnswer: correctAnswer,
        hint: q.hint || '',
        examples: (lesson.examples || []).slice(0, 3),
        keyPoints: (lesson.keyPoints || []).slice(0, 3)
      };
    });

    return processedQuestions;
  } catch (error) {
    console.error(`  Lesson ${lessonIndex + 1}: Error generating questions: ${error.message}`);
    return null;
  }
}

async function main() {
  console.log(`\n=== Generating biology tests for Grade ${GRADE}, Lessons ${START}-${START + COUNT - 1} ===\n`);

  const zai = await ZAI.create();

  // Read current data
  const data = JSON.parse(fs.readFileSync(FILE_PATH, 'utf-8'));

  // Collect all lessons
  const allLessons = [];
  for (const topic of data.lessons.detailedTopics) {
    for (const lesson of topic.lessons) {
      allLessons.push(lesson);
    }
  }

  console.log(`Total lessons found: ${allLessons.length}`);

  // Generate games for specified range
  const newGames = [];
  for (let i = START - 1; i < Math.min(START - 1 + COUNT, allLessons.length); i++) {
    const lesson = allLessons[i];
    const lessonNum = i + 1;
    console.log(`Generating questions for Lesson ${lessonNum}: ${lesson.title}...`);

    let questions = null;
    let retries = 0;

    while (!questions && retries < 3) {
      questions = await generateQuestionsForLesson(zai, lesson, i, GRADE);
      if (!questions) {
        retries++;
        console.log(`  Retry ${retries}...`);
      }
    }

    if (questions) {
      const emoji = getEmoji(lesson.title);
      const icon = getIcon(lesson.title);
      // Extract lesson title without "Урок N: " prefix
      const cleanTitle = lesson.title.replace(/^Урок\s+\d+:\s*/i, '').trim();

      const game = {
        title: `${cleanTitle} ${emoji}`,
        subject: 'Биология',
        icon: icon,
        color: 'text-green-400',
        tasks: questions
      };

      newGames.push({ lessonIndex: i, game: game });
      console.log(`  ✓ Generated ${questions.length} questions`);
    } else {
      console.error(`  ✗ FAILED to generate questions for Lesson ${lessonNum} after 3 retries`);
    }

    // Small delay between requests
    await new Promise(resolve => setTimeout(resolve, 500));
  }

  console.log(`\nGenerated ${newGames.length} games`);

  // Now update the biology.json
  // We need to replace existing games with new ones
  // First, let's figure out which games already exist and their mapping
  const existingGames = data.games || [];

  // Build a map: for each lesson index, find if there's an existing game
  // Since current games may not match 1:1 with lessons, we'll rebuild the entire games array
  // We need to preserve games that we're NOT replacing

  // For now, since we're rebuilding all games for the grade, let's collect all generated games
  // and add them in lesson order

  // If we have existing games and this is a partial update, we need to be careful
  if (existingGames.length > 0 && newGames.length < allLessons.length) {
    // Partial update - replace/add only the games in our range
    // We assume games are ordered by lesson
    // For simplicity, rebuild the full games array

    // First, collect any previously generated games outside our range
    // Since games don't have lessonIndex, we'll just append our new games
    // Actually, the safest approach is to replace all games with new ones
    // when we've generated all, or append new ones if partial

    // For now: if we have existing games, keep them for lessons NOT in our range
    // This is tricky without a lesson index in games. Let's just rebuild.
    // We'll keep existing games that aren't replaced

    // Simple approach: if we're generating the first batch, start fresh
    if (START === 1) {
      // Keep only games for lessons beyond our range (if any were generated before)
      // Actually since we're starting fresh, just use our new games
      data.games = newGames.map(g => g.game);
    } else {
      // Append to existing
      data.games = [...existingGames, ...newGames.map(g => g.game)];
    }
  } else {
    // No existing games or full replacement
    data.games = newGames.map(g => g.game);
  }

  // Write back
  fs.writeFileSync(FILE_PATH, JSON.stringify(data, null, 2), 'utf-8');
  console.log(`\n✓ Updated ${FILE_PATH} with ${data.games.length} games`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
