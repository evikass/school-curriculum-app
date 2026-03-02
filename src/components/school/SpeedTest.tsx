'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Zap } from 'lucide-react'

const QUESTIONS = [
  { q: '2 + 2 = ?', options: ['3', '4', '5', '6'], correct: 1 },
  { q: '3 × 3 = ?', options: ['6', '8', '9', '12'], correct: 2 },
  { q: '10 - 7 = ?', options: ['2', '3', '4', '5'], correct: 1 },
  { q: '15 ÷ 3 = ?', options: ['3', '4', '5', '6'], correct: 2 },
  { q: '8 + 9 = ?', options: ['15', '16', '17', '18'], correct: 2 },
]

export default function SpeedTest() {
  const { addXP } = useSchool()
  const [qIndex, setQIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [time, setTime] = useState(30)
  const [finished, setFinished] = useState(false)

  useEffect(() => {
    if (time > 0 && !finished) {
      const t = setTimeout(() => setTime(t => t - 1), 1000)
      return () => clearTimeout(t)
    } else if (time === 0) {
      setFinished(true)
    }
  }, [time, finished])

  const answer = (idx: number) => {
    if (idx === QUESTIONS[qIndex].correct) {
      addXP(5)
      setScore(s => s + 1)
    }
    if (qIndex < QUESTIONS.length - 1) {
      setQIndex(i => i + 1)
    } else {
      setFinished(true)
    }
  }

  if (finished) {
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-yellow-500/20 to-orange-500/20 border-2 border-yellow-500/30 text-center">
        <Zap className="w-12 h-12 text-yellow-400 mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-white mb-2">Результат: {score}/{QUESTIONS.length}</h3>
        <button onClick={() => { setQIndex(0); setScore(0); setTime(30); setFinished(false) }} className="px-6 py-3 bg-yellow-500 text-white rounded-xl font-bold mt-4">
          Заново
        </button>
      </div>
    )
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-yellow-500/20 to-orange-500/20 border-2 border-yellow-500/30">
      <div className="flex justify-between mb-4">
        <h3 className="text-xl font-bold text-white">⚡ Спид-тест</h3>
        <span className="text-2xl font-bold text-yellow-400">{time}с</span>
      </div>
      <p className="text-xl text-white mb-4">{QUESTIONS[qIndex].q}</p>
      <div className="grid grid-cols-2 gap-3">
        {QUESTIONS[qIndex].options.map((opt, i) => (
          <button key={i} onClick={() => answer(i)} className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors">
            {opt}
          </button>
        ))}
      </div>
    </div>
  )
}
