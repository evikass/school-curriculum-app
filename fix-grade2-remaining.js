const fs = require('fs');
const DIR = 'public/data/grades/2';

async function main() {
  const ZAI = (await import('z-ai-web-dev-sdk')).default;
  const zai = await ZAI.create();
  
  const needsFix = {
    literature: { name: 'Литературное чтение', missing: 'facts+tests' },
    pe: { name: 'Физическая культура', missing: 'facts+tests' },
    projects: { name: 'Проектная деятельность', missing: 'kp+ex+tests' },
    tech: { name: 'Технология', missing: 'L5 quiz' },
  };

  for (const [key, info] of Object.entries(needsFix)) {
    const filePath = DIR + '/' + key + '.json';
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const lessons = data.lessons.detailedTopics.flatMap(t => t.lessons || []);
    
    console.log('\n=== ' + info.name + ' (' + lessons.length + ' lessons) ===');
    
    for (let i = 0; i < lessons.length; i++) {
      const l = lessons[i];
      const num = i + 1;
      
      // Check what needs fixing
      const needKP = (l.keyPoints?.length || 0) < 4;
      const needEx = (l.examples?.length || 0) < 4;
      const needFacts = (l.facts?.length || 0) < 3;
      const needQuiz = (l.tests?.quiz?.length || 0) < 5;
      const needFind = (l.tests?.find?.length || 0) < 5;
      const needMatch = (l.tests?.match?.length || 0) < 5;
      
      if (!needKP && !needEx && !needFacts && !needQuiz && !needFind && !needMatch) {
        continue; // already good
      }
      
      process.stdout.write('  L' + num + ': ');
      
      const missing = [];
      if (needKP) missing.push('kp');
      if (needEx) missing.push('ex');
      if (needFacts) missing.push('facts');
      if (needQuiz || needFind || needMatch) missing.push('tests');
      process.stdout.write(missing.join('+') + '... ');
      
      const prompt = 'Для урока 2 класса. Предмет: ' + info.name + '. Урок: ' + l.title + '. Создай: ' +
        (needKP ? 'keyPoints: 5 ключевых пунктов, ' : '') +
        (needEx ? 'examples: 5 примеров, ' : '') +
        (needFacts ? 'facts: 3 интересных факта, ' : '') +
        'tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}. ' +
        'ВЕРНИ JSON с нужными полями.';
      
      try {
        const completion = await zai.chat.completions.create({
          messages: [
            {role:'system',content:'Ты эксперт по начальному образованию. Только валидный JSON.'},
            {role:'user',content:prompt}
          ],
          temperature: 0.7,
          max_tokens: 2000
        });
        
        let text = completion.choices[0]?.message?.content || '';
        text = text.replace(/^```json?\s*/i,'').replace(/\s*```\s*$/i,'');
        const content = JSON.parse(text);
        
        if (content.keyPoints?.length >= 4) l.keyPoints = content.keyPoints;
        if (content.examples?.length >= 4) l.examples = content.examples;
        if (content.facts?.length >= 3) l.facts = content.facts;
        if (content.tests) {
          if (content.tests.quiz?.length >= 5) l.tests.quiz = content.tests.quiz;
          if (content.tests.find?.length >= 5) l.tests.find = content.tests.find;
          if (content.tests.match?.length >= 5) l.tests.match = content.tests.match;
        }
        
        process.stdout.write('OK\n');
      } catch(e) {
        process.stdout.write('FAIL (' + e.message.substring(0,40) + ')\n');
      }
      
      await new Promise(r => setTimeout(r, 500));
    }
    
    // Save
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    console.log('  Saved ' + key + '.json');
  }
  
  console.log('\nDone!');
}

main().catch(e => console.error(e.message));
