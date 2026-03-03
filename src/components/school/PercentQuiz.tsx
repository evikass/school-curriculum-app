'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Percent } from 'lucide-react'

const QUESTIONS = [
  { q: '50% от 100 = ?', answer: 50 },
  { q: '25% от 200 = ?', answer: 50 },
  { q: '10% от 50 = ?', answer: 5 },
  { q: '75% от 80 = ?', answer: 60 },
  { q: '20% от 150 = ?', answer: 30 },
]

export default function PercentQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const q = QUESTIONS[index]

  const check = () => {
    const correct = parseInt(input) === q.answer
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(15)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % QUESTIONS.length)
      setInput('')
      setResult(null)
    }, 1500)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-orange-500/20 to-amber-500/20 border-2 border-orange-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Percent className="w-5 h-5" /> Проценты
      </h3>
      <p className="text-center text-2xl text-white mb-4">{q.q}</p>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && check()}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-2xl mb-4"
        placeholder="Ответ"
      />
      {!result && (
        <button onClick={check} className="w-full py-3 bg-orange-500 text-white rounded-xl font-bold">
          Проверить
        </button>
      )}
      {result && (
        <div className={`p-4 rounded-xl text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Верно!' : `❌ Ответ: ${q.answer}`}
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
