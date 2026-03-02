'use client'

import { useSchool } from '@/context/SchoolContext'
import { Trophy, Star, Medal } from 'lucide-react'

const ACHIEVEMENTS = [
  { id: 'first_lesson', title: 'Первый урок', icon: '📚', desc: 'Пройдите первый урок' },
  { id: 'five_games', title: 'Игрок', icon: '🎮', desc: 'Сыграйте 5 игр' },
  { id: 'streak_7', title: 'Неделя', icon: '🔥', desc: '7 дней подряд' },
  { id: 'perfect_quiz', title: 'Отличник', icon: '⭐', desc: '100% в тесте' },
  { id: 'ten_levels', title: 'Мастер', icon: '🏆', desc: 'Достигните 10 уровня' },
]

export default function AchievementsDisplay() {
  const { achievements = [] } = useSchool()

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-yellow-500/20 to-orange-500/20 border-2 border-yellow-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Trophy className="w-6 h-6 text-yellow-400" />
        Достижения
      </h3>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {ACHIEVEMENTS.map(ach => {
          const unlocked = achievements.includes(ach.id)
          return (
            <div
              key={ach.id}
              className={`p-4 rounded-xl text-center transition-all ${
                unlocked
                  ? 'bg-yellow-500/30 border border-yellow-400'
                  : 'bg-white/5 border border-white/10 opacity-50'
              }`}
            >
              <div className="text-3xl mb-2">{ach.icon}</div>
              <div className="font-bold text-white text-sm">{ach.title}</div>
              <div className="text-xs text-purple-300">{ach.desc}</div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
