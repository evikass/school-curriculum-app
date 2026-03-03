'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'

const PUZZLES = [
  { equation: '? + 3 = 7', answer: 4 },
  { equation: '12 - ? = 5', answer: 7 },
  { equation: '? × 2 = 10', answer: 5 },
  { equation: '15 ÷ ? = 3', answer: 5 },
  { equation: '? + 8 = 15', answer: 7 },
]

export default function NumberPuzzle() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const puzzle = PUZZLES[index]

  const check = () => {
    const correct = parseInt(input) === puzzle.answer
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(15)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % PUZZLES.length)
      setInput('')
      setResult(null)
    }, 1500)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-green-500/20 border-2 border-emerald-500/30">
      <h3 className="text-xl font-bold text-white mb-4">🧩 Числовые головоломки</h3>
      <p className="text-center text-2xl text-white font-bold mb-4">{puzzle.equation}</p>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-2xl mb-4"
        placeholder="?"
      />
      {!result && (
        <button onClick={check} className="w-full py-3 bg-emerald-500 text-white rounded-xl font-bold">
          Проверить
        </button>
      )}
      {result && (
        <div className={`p-4 rounded-xl text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Правильно!' : `❌ Ответ: ${puzzle.answer}`}
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
