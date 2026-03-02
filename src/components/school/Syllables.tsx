'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { AudioLines } from 'lucide-react'

const WORDS = [
  { word: 'МА-ШИ-НА', syllables: 3 },
  { word: 'СО-БА-КА', syllables: 3 },
  { word: 'ПАР-ТА', syllables: 2 },
  { word: 'КА-РАН-ДАШ', syllables: 3 },
  { word: 'У-РОК', syllables: 2 },
]

export default function Syllables() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const word = WORDS[index]

  const answer = (num: number) => {
    if (num === word.syllables) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % WORDS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-teal-500/20 border-2 border-cyan-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <AudioLines className="w-5 h-5" /> Слоги
      </h3>
      <p className="text-white mb-2">Сколько слогов в слове?</p>
      <p className="text-3xl text-cyan-300 font-bold mb-6">{word.word}</p>
      <div className="flex justify-center gap-3">
        {[1, 2, 3, 4, 5].map(n => (
          <button
            key={n}
            onClick={() => answer(n)}
            className="w-14 h-14 bg-white/10 hover:bg-white/20 rounded-xl text-white text-2xl font-bold transition-colors"
          >
            {n}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
