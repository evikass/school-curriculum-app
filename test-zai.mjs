import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  console.log('Initializing ZAI...');
  const zai = await ZAI.create();
  console.log('ZAI initialized!');
  
  const response = await zai.chat.completions.create({
    model: 'default',
    messages: [
      { role: 'system', content: 'Ты эксперт. Отвечай ТОЛЬКО валидным JSON.' },
      { role: 'user', content: 'Скажи привет. Верни JSON: {"greeting":"..."}' },
    ],
    temperature: 0.7,
    max_tokens: 100,
  });
  
  console.log('Response:', JSON.stringify(response, null, 2));
}

main().catch(err => console.error('Error:', err));
