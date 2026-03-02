'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'

const WORDS = [
  { word: 'м_локо', missing: 'о', options: ['а', 'о', 'и', 'е'] },
  { word: 'к_рова', missing: 'о', options: ['а', 'о', 'и', 'е'] },
  { word: 'с_бака', missing: 'о', options: ['а', 'о', 'и', 'е'] },
  { word: 'в_да', missing: 'о', options: ['а', 'о', 'и', 'е'] },
  { word: 'л_сица', missing: 'и', options: ['а', 'о', 'и', 'е'] },
]

export default function SpellingGame() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [answered, setAnswered] = useState(false)

  const q = WORDS[index]

  const answer = (letter: string) => {
    if (letter === q.missing) {
      addXP(10)
      setScore(s => s + 1)
    }
    setAnswered(true)
    setTimeout(() => {
      setIndex(i => (i + 1) % WORDS.length)
      setAnswered(false)
    }, 1000)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-pink-500/20 to-rose-500/20 border-2 border-pink-500/30">
      <h3 className="text-xl font-bold text-white mb-4">✏️ Орфография</h3>
      <p className="text-center text-3xl text-white font-bold mb-6">{q.word}</p>
      <div className="flex justify-center gap-3">
        {q.options.map(opt => (
          <button
            key={opt}
            onClick={() => !answered && answer(opt)}
            disabled={answered}
            className={`w-14 h-14 rounded-xl text-2xl font-bold transition-all ${
              answered && opt === q.missing
                ? 'bg-green-500 text-white'
                : answered
                ? 'bg-red-500/50 text-white/50'
                : 'bg-white/10 hover:bg-white/20 text-white'
            }`}
          >
            {opt}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
