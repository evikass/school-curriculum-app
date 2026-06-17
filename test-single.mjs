import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  console.log('ZAI ready');
  
  const response = await zai.chat.completions.create({
    model: 'default',
    messages: [
      { role: 'system', content: 'Ты эксперт по начальному образованию России. Отвечай ТОЛЬКО валидным JSON без markdown обёрток.' },
      { role: 'user', content: 'Создай ПОДРОБНЫЙ контент урока для 2 класса (8 лет). Предмет: Технология. Урок: Свойства бумаги. Описание должно быть НЕ МЕНЕЕ 800 символов, с заголовками ## и **жирным текстом**. ВЕРНИ ТОЛЬКО JSON: {"description":"...минимум 800 символов...","keyPoints":["...5 пунктов..."],"examples":["...5 примеров..."],"facts":["...3 факта..."],"tests":{"quiz":[{"question":"...","options":["...","...","...","..."],"correct":0},...5 вопросов],"find":[{"text":"...","answer":"..."},...5 заданий],"match":[{"term":"...","definition":"..."},...5 пар]}}' },
    ],
    temperature: 0.7,
    max_tokens: 3000,
  });
  
  const text = response.choices[0].message.content;
  console.log('RAW RESPONSE LENGTH:', text.length);
  console.log('FIRST 500 CHARS:', text.substring(0, 500));
  
  // Parse JSON
  let cleaned = text.replace(/^```(?:json)?\s*/i, '').replace(/\s*```\s*$/i, '');
  try {
    const parsed = JSON.parse(cleaned);
    console.log('\n✅ Parsed successfully!');
    console.log('Description length:', parsed.description?.length);
    console.log('keyPoints:', parsed.keyPoints?.length);
    console.log('examples:', parsed.examples?.length);
    console.log('facts:', parsed.facts?.length);
    console.log('quiz:', parsed.tests?.quiz?.length);
    console.log('find:', parsed.tests?.find?.length);
    console.log('match:', parsed.tests?.match?.length);
  } catch(e) {
    console.log('Parse error:', e.message);
    const objMatch = cleaned.match(/\{[\s\S]*\}/);
    if (objMatch) {
      const parsed2 = JSON.parse(objMatch[0]);
      console.log('Parsed via regex extraction');
      console.log('Description length:', parsed2.description?.length);
    }
  }
}

main().catch(err => console.error('Error:', err));
