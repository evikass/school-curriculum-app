'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { BookOpenCheck } from 'lucide-react'

const QUESTIONS = [
  { word: 'бежать', part: 'глагол', options: ['существительное', 'прилагательное', 'глагол', 'наречие'] },
  { word: 'красивый', part: 'прилагательное', options: ['существительное', 'прилагательное', 'глагол', 'наречие'] },
  { word: 'стол', part: 'существительное', options: ['существительное', 'прилагательное', 'глагол', 'наречие'] },
  { word: 'быстро', part: 'наречие', options: ['существительное', 'прилагательное', 'глагол', 'наречие'] },
  { word: 'читать', part: 'глагол', options: ['существительное', 'прилагательное', 'глагол', 'наречие'] },
]

export default function PartsOfSpeech() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const q = QUESTIONS[index]

  const answer = (part: string) => {
    if (part === q.part) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % QUESTIONS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-rose-500/20 to-pink-500/20 border-2 border-rose-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <BookOpenCheck className="w-5 h-5" /> Части речи
      </h3>
      <p className="text-white mb-2">Какая часть речи?</p>
      <p className="text-3xl text-rose-300 font-bold mb-6">{q.word}</p>
      <div className="grid grid-cols-2 gap-3">
        {q.options.map(opt => (
          <button
            key={opt}
            onClick={() => answer(opt)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {opt}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
