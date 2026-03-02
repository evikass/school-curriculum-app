'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Leaf } from 'lucide-react'

const QUESTIONS = [
  { q: 'Какое животное самое быстрое?', options: ['Лев', 'Гепард', 'Слон', 'Зебра'], correct: 1 },
  { q: 'Сколько ног у паука?', options: ['6', '8', '10', '4'], correct: 1 },
  { q: 'Какое растение даёт кислород?', options: ['Камень', 'Дерево', 'Песок', 'Вода'], correct: 1 },
  { q: 'Какая птица не летает?', options: ['Орёл', 'Страус', 'Голубь', 'Воробей'], correct: 1 },
  { q: 'Где живут киты?', options: ['В лесу', 'В море', 'В пустыне', 'В горах'], correct: 1 },
]

export default function NatureQuiz() {
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
    <div className="p-6 rounded-2xl bg-gradient-to-br from-green-500/20 to-emerald-500/20 border-2 border-green-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Leaf className="w-5 h-5" /> Природа
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
