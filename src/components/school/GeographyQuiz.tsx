'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Globe } from 'lucide-react'

const QUESTIONS = [
  { q: 'Какой материк самый большой?', options: ['Африка', 'Евразия', 'С.Америка', 'Ю.Америка'], correct: 1 },
  { q: 'Столица Японии?', options: ['Сеул', 'Токио', 'Пекин', 'Бангкок'], correct: 1 },
  { q: 'Самое глубокое озеро?', options: ['Каспийское', 'Байкал', 'Виктория', 'Танганьика'], correct: 1 },
  { q: 'Сколько океанов на Земле?', options: ['3', '4', '5', '6'], correct: 2 },
  { q: 'Самая высокая гора?', options: ['Килиманджаро', 'Эверест', 'Эльбрус', 'Мак-Кинли'], correct: 1 },
]

export default function GeographyQuiz() {
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
    <div className="p-6 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-green-500/20 border-2 border-emerald-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Globe className="w-5 h-5" /> География
      </h3>
      <p className="text-lg text-white mb-4">{q.q}</p>
      <div className="grid grid-cols-2 gap-3">
        {q.options.map((opt, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
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
