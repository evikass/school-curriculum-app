'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { ScrollText } from 'lucide-react'

const QUESTIONS = [
  { q: 'Кто основал Москву?', options: ['Пётр I', 'Юрий Долгорукий', 'Иван Грозный', 'Александр Невский'], correct: 1 },
  { q: 'Когда была Великая Отечественная война?', options: ['1941-1945', '1914-1918', '1812', '1905'], correct: 0 },
  { q: 'Кто написал "Евгений Онегин"?', options: ['Лермонтов', 'Толстой', 'Пушкин', 'Гоголь'], correct: 2 },
  { q: 'Какой город был столицей России до Москвы?', options: ['Санкт-Петербург', 'Киев', 'Новгород', 'Владимир'], correct: 1 },
  { q: 'Когда отменили крепостное право?', options: ['1861', '1905', '1917', '1825'], correct: 0 },
]

export default function HistoryQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const q = QUESTIONS[index]

  const answer = (idx: number) => {
    if (idx === q.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % QUESTIONS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-amber-500/20 to-yellow-500/20 border-2 border-amber-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <ScrollText className="w-5 h-5" /> История
      </h3>
      <p className="text-lg text-white mb-4">{q.q}</p>
      <div className="grid grid-cols-2 gap-3">
        {q.options.map((opt, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
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
