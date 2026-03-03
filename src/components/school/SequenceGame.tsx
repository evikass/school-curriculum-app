'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'

const SEQUENCES = [
  { seq: [2, 4, 6, '?'], answer: 8, hint: '+2' },
  { seq: [1, 3, 5, '?'], answer: 7, hint: '+2' },
  { seq: [5, 10, 15, '?'], answer: 20, hint: '+5' },
  { seq: [3, 6, 9, '?'], answer: 12, hint: '+3' },
  { seq: [1, 4, 7, '?'], answer: 10, hint: '+3' },
]

export default function SequenceGame() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const seq = SEQUENCES[index]

  const check = () => {
    const correct = parseInt(input) === seq.answer
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(15)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % SEQUENCES.length)
      setInput('')
      setResult(null)
    }, 1500)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-violet-500/20 to-purple-500/20 border-2 border-violet-500/30">
      <h3 className="text-xl font-bold text-white mb-4">🔢 Последовательности</h3>
      <div className="flex justify-center gap-2 mb-4">
        {seq.seq.map((n, i) => (
          <div
            key={i}
            className={`w-14 h-14 rounded-xl flex items-center justify-center text-2xl font-bold ${
              n === '?' ? 'bg-violet-500 text-white' : 'bg-white/10 text-white'
            }`}
          >
            {n}
          </div>
        ))}
      </div>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="?"
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-2xl mb-4"
      />
      {!result && (
        <button onClick={check} className="w-full py-3 bg-violet-500 text-white rounded-xl font-bold">
          Проверить
        </button>
      )}
      {result && (
        <div className={`p-4 rounded-xl text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Верно!' : `❌ Ответ: ${seq.answer}`}
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
