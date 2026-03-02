'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Atom } from 'lucide-react'

const QUESTIONS = [
  { q: 'Какая планета ближе всех к Солнцу?', options: ['Венера', 'Меркурий', 'Земля', 'Марс'], correct: 1 },
  { q: 'Сколько планет в Солнечной системе?', options: ['7', '8', '9', '10'], correct: 1 },
  { q: 'Что такое H2O?', options: ['Водород', 'Кислород', 'Вода', 'Углерод'], correct: 2 },
  { q: 'Какая самая большая планета?', options: ['Сатурн', 'Юпитер', 'Нептун', 'Уран'], correct: 1 },
  { q: 'Что изучает физика?', options: ['Растения', 'Животных', 'Природу', 'Языки'], correct: 2 },
]

export default function ScienceQuiz() {
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
    <div className="p-6 rounded-2xl bg-gradient-to-br from-violet-500/20 to-purple-500/20 border-2 border-violet-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Atom className="w-5 h-5" /> Наука
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
