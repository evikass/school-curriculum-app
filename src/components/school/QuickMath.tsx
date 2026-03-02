'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Zap } from 'lucide-react'

export default function QuickMath() {
  const { addXP } = useSchool()
  const [num1, setNum1] = useState(0)
  const [num2, setNum2] = useState(0)
  const [op, setOp] = useState('+')
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [time, setTime] = useState(30)

  useEffect(() => {
    newProblem()
  }, [])

  useEffect(() => {
    if (time > 0) {
      const t = setTimeout(() => setTime(t => t - 1), 1000)
      return () => clearTimeout(t)
    }
  }, [time])

  const newProblem = () => {
    setNum1(Math.floor(Math.random() * 10) + 1)
    setNum2(Math.floor(Math.random() * 10) + 1)
    setOp(['+', '-', '×'][Math.floor(Math.random() * 3)])
  }

  const getAnswer = () => {
    if (op === '+') return num1 + num2
    if (op === '-') return num1 - num2
    return num1 * num2
  }

  const check = () => {
    if (parseInt(input) === getAnswer()) {
      addXP(5)
      setScore(s => s + 1)
    }
    setInput('')
    newProblem()
  }

  if (time === 0) {
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-500/20 border-2 border-amber-500/30 text-center">
        <Zap className="w-12 h-12 text-amber-400 mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-white mb-2">Время вышло!</h3>
        <p className="text-amber-300 text-xl mb-4">Результат: {score}</p>
        <button onClick={() => { setTime(30); setScore(0); newProblem() }} className="px-6 py-3 bg-amber-500 text-white rounded-xl font-bold">
          Ещё раз
        </button>
      </div>
    )
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-500/20 border-2 border-amber-500/30">
      <div className="flex justify-between mb-4">
        <h3 className="text-xl font-bold text-white">⚡ Быстрая математика</h3>
        <span className="text-2xl font-bold text-amber-400">{time}с</span>
      </div>
      <p className="text-center text-4xl text-white font-bold mb-4">
        {num1} {op} {num2} = ?
      </p>
      <div className="flex gap-2">
        <input
          type="number"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && check()}
          className="flex-1 p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-2xl"
        />
        <button onClick={check} className="px-6 py-3 bg-amber-500 text-white rounded-xl font-bold">✓</button>
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
