'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Flag } from 'lucide-react'

const FLAGS = [
  { emoji: '🇷🇺', country: 'Россия' },
  { emoji: '🇺🇸', country: 'США' },
  { emoji: '🇫🇷', country: 'Франция' },
  { emoji: '🇩🇪', country: 'Германия' },
  { emoji: '🇬🇧', country: 'Великобритания' },
  { emoji: '🇯🇵', country: 'Япония' },
  { emoji: '🇨🇳', country: 'Китай' },
  { emoji: '🇮🇹', country: 'Италия' },
]

export default function FlagsQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const flag = FLAGS[index]
  const options = FLAGS.filter(f => f !== flag).sort(() => Math.random() - 0.5).slice(0, 3).concat(flag).sort(() => Math.random() - 0.5)

  const answer = (country: string) => {
    if (country === flag.country) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % FLAGS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-blue-500/20 to-indigo-500/20 border-2 border-blue-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Flag className="w-5 h-5" /> Флаги
      </h3>
      <div className="text-center text-8xl mb-6">{flag.emoji}</div>
      <div className="grid grid-cols-2 gap-3">
        {options.map(opt => (
          <button
            key={opt.country}
            onClick={() => answer(opt.country)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {opt.country}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
