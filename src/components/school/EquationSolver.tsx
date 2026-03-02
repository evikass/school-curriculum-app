'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Calculator } from 'lucide-react'

const EQUATIONS = [
  { eq: 'x + 5 = 10', answer: 5 },
  { eq: 'x - 3 = 7', answer: 10 },
  { eq: '2x = 12', answer: 6 },
  { eq: 'x / 2 = 4', answer: 8 },
  { eq: 'x + 8 = 15', answer: 7 },
]

export default function EquationSolver() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const eq = EQUATIONS[index]

  const check = () => {
    const correct = parseFloat(input) === eq.answer
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(15)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % EQUATIONS.length)
      setInput('')
      setResult(null)
    }, 1500)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-violet-500/20 border-2 border-indigo-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Calculator className="w-5 h-5" /> Уравнения
      </h3>
      <p className="text-center text-2xl text-white mb-4">Реши: <span className="font-bold">{eq.eq}</span></p>
      <p className="text-center text-indigo-300 mb-4">Найди x</p>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && check()}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-2xl mb-4"
        placeholder="x = ?"
      />
      {!result && (
        <button onClick={check} className="w-full py-3 bg-indigo-500 text-white rounded-xl font-bold">
          Проверить
        </button>
      )}
      {result && (
        <div className={`p-4 rounded-xl text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Верно!' : `❌ x = ${eq.answer}`}
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
