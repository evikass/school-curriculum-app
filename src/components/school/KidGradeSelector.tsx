'use client'

import { useSchool } from '@/context/SchoolContext'
<<<<<<< HEAD

const gradeConfig = [
  { grade: 0, emoji: '🎒', name: 'Подготовишки', color: 'from-pink-400 to-purple-500', description: 'Учимся играть' },
  { grade: 1, emoji: '🌟', name: '1 класс', color: 'from-yellow-400 to-orange-500', description: 'Первые шаги' },
  { grade: 2, emoji: '🦋', name: '2 класс', color: 'from-blue-400 to-cyan-500', description: 'Учимся читать' },
  { grade: 3, emoji: '🚀', name: '3 класс', color: 'from-green-400 to-emerald-500', description: 'Полетели!' },
  { grade: 4, emoji: '🎯', name: '4 класс', color: 'from-purple-400 to-indigo-500', description: 'Точно в цель' },
  { grade: 5, emoji: '📚', name: '5 класс', color: 'from-red-400 to-pink-500', description: 'Новые предметы' },
  { grade: 6, emoji: '🔬', name: '6 класс', color: 'from-teal-400 to-cyan-500', description: 'Эксперименты' },
  { grade: 7, emoji: '⚗️', name: '7 класс', color: 'from-amber-400 to-yellow-500', description: 'Химия и физика' },
  { grade: 8, emoji: '🧬', name: '8 класс', color: 'from-lime-400 to-green-500', description: 'Биология' },
  { grade: 9, emoji: '🏆', name: '9 класс', color: 'from-violet-400 to-purple-500', description: 'ОГЭ близко' },
  { grade: 10, emoji: '🎓', name: '10 класс', color: 'from-rose-400 to-pink-500', description: 'Профиль' },
  { grade: 11, emoji: '👑', name: '11 класс', color: 'from-yellow-400 to-amber-500', description: 'ЕГЭ!' },
]
=======
import { X } from 'lucide-react'
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c

export default function KidGradeSelector() {
  const { goToClass } = useSchool()

<<<<<<< HEAD
  return (
    <div className="w-full animate-bounceIn">
      <div className="text-center mb-10">
        <div className="text-8xl mb-4 animate-float">🏫</div>
        <h2 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text 
                       bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-4">
          ИНЕТШКОЛА
        </h2>
        <p className="text-2xl text-purple-200">Выбери свой класс! 📚</p>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 max-w-5xl mx-auto">
        {gradeConfig.map((config) => (
          <button
            key={config.grade}
            onClick={() => goToClass(config.grade)}
            className={`group relative overflow-hidden p-6 rounded-3xl
                       bg-gradient-to-br ${config.color}
                       border-4 border-white/20 hover:border-white/50
                       shadow-xl hover:shadow-2xl hover:scale-105
                       transition-all duration-300 text-center
                       animate-popIn`}
            style={{ animationDelay: `${config.grade * 0.05}s` }}
          >
            <div className="text-6xl mb-3 group-hover:scale-125 transition-transform">
              {config.emoji}
            </div>
            <h3 className="text-xl md:text-2xl font-black text-white mb-1">
              {config.name}
            </h3>
            <p className="text-white/80 text-sm">{config.description}</p>
          </button>
        ))}
      </div>
=======
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
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
    </div>
  )
}
