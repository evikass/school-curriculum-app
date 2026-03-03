'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Timer, Gift, BarChart, Brain } from 'lucide-react'

export default function ChallengeMode() {
  const { addXP } = useSchool()
  const [score, setScore] = useState(0)
  const [question, setQuestion] = useState(1)

  const questions = [
    { q: '2 + 2 = ?', a: 4 },
    { q: 'Столица России?', a: 'Москва' },
    { q: '5 × 3 = ?', a: 15 },
  ]

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-red-500/20 to-rose-500/20 border-2 border-red-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Timer className="w-5 h-5" /> Челлендж
      </h3>
      <p className="text-white mb-4">Вопрос {question}/10</p>
      <div className="p-4 bg-white/5 rounded-xl mb-4">
        <p className="text-lg text-white">Режим челленджа! Отвечай быстро!</p>
      </div>
      <div className="text-center">
        <p className="text-3xl text-red-300 font-bold mb-4">Готов?</p>
        <button onClick={() => { addXP(50); setScore(s => s + 1) }} className="px-8 py-4 bg-red-500 text-white rounded-xl font-bold">
          Начать!
        </button>
      </div>
      <p className="text-center text-purple-300 mt-4">Очки: {score}</p>
    </div>
  )
}
