'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { HelpCircle } from 'lucide-react'

const RIDDLES = [
  { q: 'Что можно увидеть с закрытыми глазами?', a: 'Сон', options: ['Сон', 'Мечту', 'Тьму', 'Ничего'] },
  { q: 'Что становится больше, если его перевернуть?', a: 'Число 9', options: ['Число 9', 'Число 6', 'Число 8', 'Число 0'] },
  { q: 'У чего есть голова, но нет мозга?', a: 'Спичка', options: ['Спичка', 'Подушка', 'Лук', 'Чеснок'] },
  { q: 'Что идёт, но не двигается?', a: 'Время', options: ['Время', 'Дорога', 'Вода', 'Ветер'] },
  { q: 'Что можно сломать, даже не дотрагиваясь?', a: 'Слово', options: ['Слово', 'Обещание', 'Молчание', 'Тишина'] },
]

export default function Riddles() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const riddle = RIDDLES[index]

  const answer = (opt: string) => {
    if (opt === riddle.a) {
      addXP(15)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % RIDDLES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-violet-500/20 to-purple-500/20 border-2 border-violet-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <HelpCircle className="w-5 h-5" /> Загадки
      </h3>
      <div className="p-4 bg-white/5 rounded-xl mb-4">
        <p className="text-lg text-white italic">"{riddle.q}"</p>
      </div>
      <div className="grid grid-cols-2 gap-3">
        {riddle.options.map(opt => (
          <button
            key={opt}
            onClick={() => answer(opt)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {opt}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
