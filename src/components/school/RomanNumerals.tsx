'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Languages } from 'lucide-react'

const NUMBERS = [
  { roman: 'I', arabic: 1 },
  { roman: 'V', arabic: 5 },
  { roman: 'X', arabic: 10 },
  { roman: 'L', arabic: 50 },
  { roman: 'C', arabic: 100 },
  { roman: 'II', arabic: 2 },
  { roman: 'IV', arabic: 4 },
  { roman: 'IX', arabic: 9 },
]

export default function RomanNumerals() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [mode, setMode] = useState<'toArabic' | 'toRoman'>('toArabic')

  const num = NUMBERS[index]
  const options = NUMBERS.filter(n => n !== num).sort(() => Math.random() - 0.5).slice(0, 3).concat(num).sort(() => Math.random() - 0.5)

  const answer = (value: number | string) => {
    const correct = mode === 'toArabic' ? value === num.arabic : value === num.roman
    if (correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % NUMBERS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-stone-500/20 to-zinc-500/20 border-2 border-stone-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Languages className="w-5 h-5" /> Римские цифры
      </h3>
      <div className="flex gap-2 mb-4">
        <button onClick={() => setMode('toArabic')} className={`flex-1 py-2 rounded-xl font-bold ${mode === 'toArabic' ? 'bg-stone-500 text-white' : 'bg-white/10 text-white/50'}`}>
          → Арабские
        </button>
        <button onClick={() => setMode('toRoman')} className={`flex-1 py-2 rounded-xl font-bold ${mode === 'toRoman' ? 'bg-stone-500 text-white' : 'bg-white/10 text-white/50'}`}>
          → Римские
        </button>
      </div>
      <p className="text-center text-4xl text-stone-300 font-bold mb-6">
        {mode === 'toArabic' ? num.roman : num.arabic}
      </p>
      <div className="grid grid-cols-2 gap-3">
        {options.map((opt, i) => (
          <button
            key={i}
            onClick={() => answer(mode === 'toArabic' ? opt.arabic : opt.roman)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold text-xl transition-colors"
          >
            {mode === 'toArabic' ? opt.arabic : opt.roman}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
