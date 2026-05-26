const fs = require('fs');
const DIR = 'public/data/grades/2';

async function main() {
  const ZAI = (await import('z-ai-web-dev-sdk')).default;
  const zai = await ZAI.create();
  
  const subjects = {
    literature: 'Литературное чтение',
    pe: 'Физическая культура',
    projects: 'Проектная деятельность',
    tech: 'Технология',
  };

  for (const [key, name] of Object.entries(subjects)) {
    const filePath = DIR + '/' + key + '.json';
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const lessons = data.lessons.detailedTopics.flatMap(t => t.lessons || []);
    
    let fixed = 0;
    console.log('\n=== ' + name + ' (' + lessons.length + ' lessons) ===');
    
    for (let i = 0; i < lessons.length; i++) {
      const l = lessons[i];
      const num = i + 1;
      
      const needKP = (l.keyPoints?.length || 0) < 4;
      const needEx = (l.examples?.length || 0) < 4;
      const needFacts = (l.facts?.length || 0) < 3;
      const needTests = (l.tests?.quiz?.length || 0) < 5 || (l.tests?.find?.length || 0) < 5 || (l.tests?.match?.length || 0) < 5;
      
      if (!needKP && !needEx && !needFacts && !needTests) continue;
      
      const missing = [];
      if (needKP) missing.push('kp');
      if (needEx) missing.push('ex');
      if (needFacts) missing.push('facts');
      if (needTests) missing.push('tests');
      
      process.stdout.write('  L' + num + ' [' + missing.join('+') + ']... ');
      
      const parts = [];
      if (needKP) parts.push('keyPoints: 5 ключевых пунктов');
      if (needEx) parts.push('examples: 5 примеров');
      if (needFacts) parts.push('facts: 3 интересных факта');
      if (needTests) parts.push('tests: {quiz:[5 {question,options[4],correct}], find:[5 {text,answer}], match:[5 {term,definition}]}');
      
      const prompt = 'Урок 2 класса. Предмет: ' + name + '. Урок: ' + l.title + '. Создай: ' + parts.join(', ') + '. ВЕРНИ ТОЛЬКО JSON.';
      
      let success = false;
      for (let attempt = 0; attempt < 3; attempt++) {
        try {
          const completion = await zai.chat.completions.create({
            messages: [
              {role:'system',content:'Ты эксперт по начальному образованию. Только валидный JSON без markdown.'},
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
          if (content.tests?.quiz?.length >= 5) {
            if (!l.tests) l.tests = {};
            l.tests.quiz = content.tests.quiz;
          }
          if (content.tests?.find?.length >= 5) {
            if (!l.tests) l.tests = {};
            l.tests.find = content.tests.find;
          }
          if (content.tests?.match?.length >= 5) {
            if (!l.tests) l.tests = {};
            l.tests.match = content.tests.match;
          }
          
          fixed++;
          success = true;
          process.stdout.write('OK\n');
          break;
        } catch(e) {
          if (attempt < 2) {
            process.stdout.write('retry(' + (attempt+1) + ')... ');
            await new Promise(r => setTimeout(r, 3000));
          } else {
            process.stdout.write('FAIL\n');
          }
        }
      }
      
      // 2 second delay between lessons to avoid rate limit
      await new Promise(r => setTimeout(r, 2000));
    }
    
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    console.log('  Fixed: ' + fixed + ' lessons. Saved.');
  }
  
  console.log('\nAll done!');
}

main().catch(e => console.error(e.message));
