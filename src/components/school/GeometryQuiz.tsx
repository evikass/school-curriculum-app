'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { CircleDot } from 'lucide-react'

const SHAPES = [
  { name: 'Треугольник', sides: 3, angles: 3 },
  { name: 'Квадрат', sides: 4, angles: 4 },
  { name: 'Пятиугольник', sides: 5, angles: 5 },
  { name: 'Шестиугольник', sides: 6, angles: 6 },
  { name: 'Восьмиугольник', sides: 8, angles: 8 },
]

export default function GeometryQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const shape = SHAPES[index]

  const answer = (num: number) => {
    if (num === shape.sides) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % SHAPES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-lime-500/20 to-green-500/20 border-2 border-lime-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <CircleDot className="w-5 h-5" /> Геометрия
      </h3>
      <p className="text-center text-white mb-2">Сколько сторон у:</p>
      <p className="text-center text-3xl text-lime-300 font-bold mb-6">{shape.name}?</p>
      <div className="grid grid-cols-3 gap-3">
        {[3, 4, 5, 6, 7, 8].map(n => (
          <button
            key={n}
            onClick={() => answer(n)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white text-2xl font-bold transition-colors"
          >
            {n}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
