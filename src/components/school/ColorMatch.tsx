'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'

const COLORS = [
  { name: 'Красный', hex: '#FF0000' },
  { name: 'Синий', hex: '#0000FF' },
  { name: 'Зелёный', hex: '#00FF00' },
  { name: 'Жёлтый', hex: '#FFFF00' },
  { name: 'Оранжевый', hex: '#FFA500' },
  { name: 'Фиолетовый', hex: '#800080' },
]

export default function ColorMatch() {
  const { addXP } = useSchool()
  const [target, setTarget] = useState(COLORS[0])
  const [options, setOptions] = useState<typeof COLORS>([])
  const [score, setScore] = useState(0)
  const [time, setTime] = useState(10)

  useEffect(() => {
    newRound()
  }, [])

  useEffect(() => {
    if (time > 0) {
      const t = setTimeout(() => setTime(t => t - 1), 1000)
      return () => clearTimeout(t)
    }
  }, [time])

  const newRound = () => {
    const t = COLORS[Math.floor(Math.random() * COLORS.length)]
    const opts = [t, ...COLORS.filter(c => c !== t).sort(() => Math.random() - 0.5).slice(0, 3)].sort(() => Math.random() - 0.5)
    setTarget(t)
    setOptions(opts)
    setTime(10)
  }

  const answer = (color: typeof COLORS[0]) => {
    if (color.hex === target.hex) {
      addXP(10)
      setScore(s => s + 1)
    }
    newRound()
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-pink-500/20 to-rose-500/20 border-2 border-pink-500/30">
      <h3 className="text-xl font-bold text-white mb-2">🎨 Цвета</h3>
      <p className="text-center text-purple-300 mb-2">Время: {time}с</p>
      <div
        className="w-full h-24 rounded-xl mb-4 flex items-center justify-center"
        style={{ backgroundColor: target.hex }}
      >
        <span className="text-white font-bold text-2xl drop-shadow-lg">{target.name}</span>
      </div>
      <div className="grid grid-cols-2 gap-2">
        {options.map(opt => (
          <button
            key={opt.hex}
            onClick={() => answer(opt)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {opt.name}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
