'use client'

import { useSchool } from '@/context/SchoolContext'
import { X } from 'lucide-react'

export default function KidGradeSelector() {
  const { goToClass } = useSchool()

  const grades = [
    { id: 0, name: 'Подготовительный', emoji: '🎒', color: 'from-pink-400 to-rose-500' },
    { id: 1, name: '1 класс', emoji: '🌟', color: 'from-yellow-400 to-orange-500' },
    { id: 2, name: '2 класс', emoji: '🦋', color: 'from-green-400 to-teal-500' },
    { id: 3, name: '3 класс', emoji: '🌈', color: 'from-blue-400 to-indigo-500' },
    { id: 4, name: '4 класс', emoji: '🎪', color: 'from-purple-400 to-pink-500' },
    { id: 5, name: '5 класс', emoji: '🎨', color: 'from-red-400 to-orange-500' },
    { id: 6, name: '6 класс', emoji: '🔬', color: 'from-cyan-400 to-blue-500' },
    { id: 7, name: '7 класс', emoji: '📐', color: 'from-emerald-400 to-green-500' },
    { id: 8, name: '8 класс', emoji: '🧪', color: 'from-violet-400 to-purple-500' },
    { id: 9, name: '9 класс', emoji: '📖', color: 'from-amber-400 to-yellow-500' },
    { id: 10, name: '10 класс', emoji: '🎓', color: 'from-rose-400 to-pink-500' },
    { id: 11, name: '11 класс', emoji: '🏆', color: 'from-indigo-400 to-violet-500' },
  ]

  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
      {grades.map(grade => (
        <button
          key={grade.id}
          onClick={() => goToClass(grade.id)}
          className={`p-6 rounded-3xl bg-gradient-to-br ${grade.color} text-white font-black text-lg
                     transform hover:scale-105 transition-all shadow-lg hover:shadow-xl
                     border-4 border-white/30 hover:border-white/50`}
        >
          <div className="text-4xl mb-2">{grade.emoji}</div>
          <div>{grade.name}</div>
        </button>
      ))}
    </div>
  )
}
