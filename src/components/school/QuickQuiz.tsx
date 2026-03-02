'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { HelpCircle, ChevronRight } from 'lucide-react'

const QUESTIONS = [
  { q: '2 + 2 = ?', options: ['3', '4', '5'], correct: 1 },
  { q: 'Столица России?', options: ['Москва', 'Париж', 'Лондон'], correct: 0 },
  { q: 'Сколько дней в неделе?', options: ['5', '6', '7'], correct: 2 },
]

export default function QuickQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const q = QUESTIONS[index]

  const answer = (idx: number) => {
    if (idx === q.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % QUESTIONS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-teal-500/20 border-2 border-cyan-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <HelpCircle className="w-5 h-5" /> Быстрый квиз
      </h3>
      <p className="text-lg text-white mb-4">{q.q}</p>
      <div className="space-y-2">
        {q.options.map((opt, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
            className="w-full p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold flex items-center justify-between"
          >
            {opt} <ChevronRight className="w-5 h-5" />
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
