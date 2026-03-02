'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Car, RotateCcw } from 'lucide-react'

const QUESTIONS = [
  { q: '3 + 4', a: 7 },
  { q: '8 - 5', a: 3 },
  { q: '6 + 2', a: 8 },
  { q: '9 - 3', a: 6 },
  { q: '5 + 5', a: 10 },
]

export default function MathRacing() {
  const { addXP } = useSchool()
  const [position, setPosition] = useState(0)
  const [qIndex, setQIndex] = useState(0)
  const [input, setInput] = useState('')
  const [finished, setFinished] = useState(false)

  const q = QUESTIONS[qIndex]

  const answer = () => {
    if (parseInt(input) === q.a) {
      addXP(10)
      setPosition(p => Math.min(p + 20, 100))
    }
    setInput('')
    if (qIndex < QUESTIONS.length - 1) {
      setQIndex(i => i + 1)
    } else {
      setFinished(true)
    }
  }

  const restart = () => {
    setPosition(0)
    setQIndex(0)
    setInput('')
    setFinished(false)
  }

  if (finished) {
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-orange-500/20 to-red-500/20 border-2 border-orange-500/30 text-center">
        <div className="text-6xl mb-4">🏁</div>
        <h3 className="text-2xl font-bold text-white mb-4">{position >= 80 ? '🏆 Победа!' : 'Попробуй ещё!'}</h3>
        <button onClick={restart} className="px-6 py-3 bg-orange-500 text-white rounded-xl font-bold">
          <RotateCcw className="w-5 h-5 inline mr-2" /> Заново
        </button>
      </div>
    )
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-orange-500/20 to-red-500/20 border-2 border-orange-500/30">
      <h3 className="text-xl font-bold text-white mb-2">🏎️ Математические гонки</h3>
      <div className="relative h-8 bg-white/10 rounded-full mb-6 overflow-hidden">
        <div className="absolute inset-y-0 left-0 bg-orange-500 transition-all" style={{ width: `${position}%` }} />
        <Car className="absolute top-1 text-white transition-all" style={{ left: `calc(${position}% - 16px)` }} />
        <div className="absolute right-2 top-1 text-white">🏁</div>
      </div>
      <p className="text-center text-2xl text-white font-bold mb-4">{q.q} = ?</p>
      <div className="flex gap-2">
        <input
          type="number"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && answer()}
          className="flex-1 p-3 rounded-xl bg-white/10 border border-white/20 text-white text-xl"
          placeholder="Ответ"
        />
        <button onClick={answer} className="px-6 py-3 bg-orange-500 text-white rounded-xl font-bold">Go!</button>
      </div>
    </div>
  )
}
