'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Smile } from 'lucide-react'

const QUIZZES = [
  { emoji: '🦁', options: ['Кот', 'Лев', 'Тигр', 'Собака'], correct: 1 },
  { emoji: '🍎', options: ['Груша', 'Яблоко', 'Апельсин', 'Банан'], correct: 1 },
  { emoji: '🚗', options: ['Самолёт', 'Корабль', 'Машина', 'Велосипед'], correct: 2 },
  { emoji: '☀️', options: ['Луна', 'Звезда', 'Солнце', 'Планета'], correct: 2 },
  { emoji: '🏠', options: ['Дом', 'Школа', 'Магазин', 'Больница'], correct: 0 },
]

export default function EmojiQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const quiz = QUIZZES[index]

  const answer = (idx: number) => {
    if (idx === quiz.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % QUIZZES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-amber-500/20 to-yellow-500/20 border-2 border-amber-500/30">
      <h3 className="text-xl font-bold text-white mb-4">😀 Эмодзи-квиз</h3>
      <div className="text-center text-8xl mb-6">{quiz.emoji}</div>
      <div className="grid grid-cols-2 gap-3">
        {quiz.options.map((opt, i) => (
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
