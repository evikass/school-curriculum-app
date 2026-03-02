'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Target } from 'lucide-react'

const PUZZLES = [
  { items: ['Яблоко', 'Груша', 'Банан', 'Морковь'], odd: 3 },
  { items: ['Собака', 'Кошка', 'Корова', 'Стол'], odd: 3 },
  { items: ['Красный', 'Синий', 'Квадрат', 'Зелёный'], odd: 2 },
  { items: ['Лев', 'Тигр', 'Волк', 'Голубь'], odd: 3 },
  { items: ['Москва', 'Париж', 'Лондон', 'Волга'], odd: 3 },
]

export default function OddOneOut() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const puzzle = PUZZLES[index]

  const answer = (idx: number) => {
    if (idx === puzzle.odd) {
      addXP(15)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % PUZZLES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-sky-500/20 to-blue-500/20 border-2 border-sky-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Target className="w-5 h-5" /> Найди лишнее
      </h3>
      <div className="grid grid-cols-2 gap-3">
        {puzzle.items.map((item, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {item}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
