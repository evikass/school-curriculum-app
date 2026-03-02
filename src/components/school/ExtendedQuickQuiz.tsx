'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Gamepad2, Star } from 'lucide-react'

const QUESTIONS = [
  { q: '5 + 3 = ?', options: ['6', '7', '8', '9'], correct: 2 },
  { q: 'Столица Франции?', options: ['Лондон', 'Париж', 'Берлин', 'Рим'], correct: 1 },
  { q: 'Сколько месяцев в году?', options: ['10', '11', '12', '13'], correct: 2 },
  { q: 'Самая большая планета?', options: ['Земля', 'Марс', 'Юпитер', 'Сатурн'], correct: 2 },
  { q: 'Автор "Евгения Онегина"?', options: ['Лермонтов', 'Пушкин', 'Толстой', 'Гоголь'], correct: 1 },
]

export default function ExtendedQuickQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [finished, setFinished] = useState(false)

  const q = QUESTIONS[index]

  const answer = (idx: number) => {
    if (idx === q.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    if (index < QUESTIONS.length - 1) {
      setIndex(i => i + 1)
    } else {
      setFinished(true)
    }
  }

  const restart = () => {
    setIndex(0)
    setScore(0)
    setFinished(false)
  }

  if (finished) {
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-blue-500/20 border-2 border-cyan-500/30 text-center">
        <div className="text-6xl mb-4">🎉</div>
        <h3 className="text-2xl font-bold text-white mb-2">Квиз завершён!</h3>
        <p className="text-cyan-300 mb-4">Результат: {score}/{QUESTIONS.length}</p>
        <button onClick={restart} className="px-6 py-3 bg-cyan-500 text-white rounded-xl font-bold">
          Ещё раз
        </button>
      </div>
    )
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-blue-500/20 border-2 border-cyan-500/30">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-xl font-bold text-white">📋 Большой квиз</h3>
        <span className="text-cyan-300">{index + 1}/{QUESTIONS.length}</span>
      </div>
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
      <div className="flex justify-center gap-1 mt-4">
        {QUESTIONS.map((_, i) => (
          <div
            key={i}
            className={`w-3 h-3 rounded-full ${
              i < index ? 'bg-green-500' : i === index ? 'bg-cyan-500' : 'bg-white/20'
            }`}
          />
        ))}
      </div>
    </div>
  )
}
