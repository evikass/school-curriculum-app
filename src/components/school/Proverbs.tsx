'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { BookOpen } from 'lucide-react'

const PROVERBS = [
  { start: 'Без труда не выловишь...', options: ['и рыбку из пруда', 'птицу из гнезда', 'золотую рыбку'], correct: 0 },
  { start: 'Терпение и труд...', options: ['всё перетрут', 'всё дадут', 'всё стерпят'], correct: 0 },
  { start: 'Век живи...', options: ['век учись', 'век надейся', 'и радуйся'], correct: 0 },
  { start: 'Семь раз отмерь...', options: ['один раз отрежь', 'семь раз прикинь', 'потом решай'], correct: 0 },
  { start: 'Делу время...', options: ['потехе час', 'а отдыху срок', 'работе конец'], correct: 0 },
]

export default function Proverbs() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const proverb = PROVERBS[index]

  const answer = (idx: number) => {
    if (idx === proverb.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % PROVERBS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-rose-500/20 to-pink-500/20 border-2 border-rose-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <BookOpen className="w-5 h-5" /> Пословицы
      </h3>
      <p className="text-lg text-white mb-6">Закончите пословицу:</p>
      <p className="text-xl text-rose-300 font-bold mb-6">"{proverb.start}"</p>
      <div className="space-y-3">
        {proverb.options.map((opt, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
            className="w-full p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {opt}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
