'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Scale } from 'lucide-react'

const FRACTIONS = [
  { frac1: '1/2', frac2: '1/4', answer: '>' },
  { frac1: '1/3', frac2: '1/2', answer: '<' },
  { frac1: '2/3', frac2: '1/2', answer: '>' },
  { frac1: '3/4', frac2: '1/4', answer: '>' },
  { frac1: '1/5', frac2: '1/3', answer: '<' },
]

export default function FractionCompare() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const frac = FRACTIONS[index]

  const answer = (comparison: string) => {
    if (comparison === frac.answer) {
      addXP(15)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % FRACTIONS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-blue-500/20 border-2 border-indigo-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Scale className="w-5 h-5" /> Сравнение дробей
      </h3>
      <div className="flex items-center justify-center gap-4 mb-6">
        <span className="text-4xl font-bold text-white bg-white/10 px-6 py-4 rounded-xl">{frac.frac1}</span>
        <span className="text-3xl text-indigo-300">?</span>
        <span className="text-4xl font-bold text-white bg-white/10 px-6 py-4 rounded-xl">{frac.frac2}</span>
      </div>
      <div className="flex justify-center gap-4">
        <button onClick={() => answer('<')} className="w-20 h-20 bg-white/10 hover:bg-white/20 rounded-xl text-white text-4xl font-bold transition-colors">&lt;</button>
        <button onClick={() => answer('=')} className="w-20 h-20 bg-white/10 hover:bg-white/20 rounded-xl text-white text-4xl font-bold transition-colors">=</button>
        <button onClick={() => answer('>')} className="w-20 h-20 bg-white/10 hover:bg-white/20 rounded-xl text-white text-4xl font-bold transition-colors">&gt;</button>
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
