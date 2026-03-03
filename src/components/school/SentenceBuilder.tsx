'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { GripVertical } from 'lucide-react'

const SENTENCES = [
  { words: ['кошка', 'ловит', 'мышь'], correct: 'кошка ловит мышь' },
  { words: ['солнце', 'светит', 'ярко'], correct: 'солнце светит ярко' },
  { words: ['мальчик', 'читает', 'книгу'], correct: 'мальчик читает книгу' },
]

export default function SentenceBuilder() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [selected, setSelected] = useState<string[]>([])
  const [score, setScore] = useState(0)

  const sentence = SENTENCES[index]
  const shuffled = [...sentence.words].sort(() => Math.random() - 0.5)

  const select = (word: string) => {
    if (selected.includes(word)) {
      setSelected(selected.filter(w => w !== word))
    } else {
      setSelected([...selected, word])
    }
  }

  const check = () => {
    if (selected.join(' ') === sentence.correct) {
      addXP(15)
      setScore(s => s + 1)
    }
    setSelected([])
    setIndex(i => (i + 1) % SENTENCES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-green-500/20 border-2 border-emerald-500/30">
      <h3 className="text-xl font-bold text-white mb-4">📝 Построй предложение</h3>
      <div className="flex flex-wrap gap-2 mb-4">
        {shuffled.map(word => (
          <button
            key={word}
            onClick={() => select(word)}
            className={`px-4 py-2 rounded-xl font-bold transition-all ${
              selected.includes(word)
                ? 'bg-emerald-500 text-white'
                : 'bg-white/10 text-white hover:bg-white/20'
            }`}
          >
            {word}
          </button>
        ))}
      </div>
      <div className="p-4 bg-white/5 rounded-xl mb-4 min-h-[50px]">
        {selected.length > 0 ? selected.join(' ') : 'Нажми на слова по порядку...'}
      </div>
      <button onClick={check} className="w-full py-3 bg-emerald-500 text-white rounded-xl font-bold">
        Проверить
      </button>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
