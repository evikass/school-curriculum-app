'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Clock } from 'lucide-react'

const QUESTIONS = [
  { time: '15:30', q: 'Который час?', options: ['3:30', '15:30', '5:30', '13:30'], correct: 1 },
  { time: '09:00', q: 'Который час?', options: ['9:00', '21:00', '6:00', '12:00'], correct: 0 },
  { time: '18:45', q: 'Который час?', options: ['6:45', '8:45', '18:45', '16:45'], correct: 2 },
  { time: '12:00', q: 'Сколько времени?', options: ['Полночь', 'Полдень', 'Утро', 'Вечер'], correct: 1 },
  { time: '07:15', q: 'Который час?', options: ['7:15', '17:15', '5:15', '19:15'], correct: 0 },
]

export default function TimeQuiz() {
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
    <div className="p-6 rounded-2xl bg-gradient-to-br from-amber-500/20 to-yellow-500/20 border-2 border-amber-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Clock className="w-5 h-5" /> Время
      </h3>
      <div className="text-center mb-4">
        <div className="text-6xl mb-2">🕐</div>
        <p className="text-3xl font-bold text-white">{q.time}</p>
      </div>
      <p className="text-white mb-4">{q.q}</p>
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
