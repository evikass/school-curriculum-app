'use client'

import { Flame, Gamepad2, Zap } from 'lucide-react'
import { Achievement, allAchievements } from './constants'
import { getIcon } from './utils'

interface AchievementsTabProps {
  progress: {
    streak: number
    gamesPlayed: number
    totalPoints: number
    completedTopics: Record<string, boolean>
    achievements: string[]
    correctAnswers: number
    totalAnswers: number
  }
}

export default function AchievementsTab({ progress }: AchievementsTabProps) {
  return (
    <div className="p-4 space-y-2">
      {/* Stats grid */}
      <div className="grid grid-cols-3 gap-2 mb-3">
        <div className="text-center p-2 rounded-xl bg-white/5 border border-white/10">
          <Flame className="w-4 h-4 text-orange-400 mx-auto mb-1" />
          <div className="text-base font-black text-white">{progress.streak}</div>
          <div className="text-[10px] text-orange-300">дней</div>
        </div>
        <div className="text-center p-2 rounded-xl bg-white/5 border border-white/10">
          <Gamepad2 className="w-4 h-4 text-green-400 mx-auto mb-1" />
          <div className="text-base font-black text-white">{progress.gamesPlayed}</div>
          <div className="text-[10px] text-orange-300">игр</div>
        </div>
        <div className="text-center p-2 rounded-xl bg-white/5 border border-white/10">
          <Zap className="w-4 h-4 text-yellow-400 mx-auto mb-1" />
          <div className="text-base font-black text-white">{progress.totalPoints}</div>
          <div className="text-[10px] text-orange-300">баллов</div>
        </div>
      </div>

      {/* Achievements list */}
      {allAchievements.map(achievement => {
        const isUnlocked = achievement.condition(progress)
        return (
          <div key={achievement.id} className={`p-3 rounded-xl border flex items-center gap-3 ${isUnlocked ? 'bg-gradient-to-r from-yellow-400/20 to-orange-500/20 border-yellow-400/50' : 'bg-white/5 border-white/10 opacity-50'}`}>
            <div className={`p-2 rounded-lg ${isUnlocked ? 'bg-gradient-to-br from-yellow-400 to-orange-500 text-purple-900' : 'bg-gray-700 text-gray-400'}`}>
              {getIcon(achievement.icon)}
            </div>
            <div className="flex-1">
              <h3 className={`font-medium text-sm ${isUnlocked ? 'text-white' : 'text-gray-400'}`}>{achievement.name}</h3>
              <p className="text-[10px] text-gray-400">{achievement.desc}</p>
            </div>
            {isUnlocked && <div className="text-yellow-400 text-xs font-bold">+{achievement.points}</div>}
          </div>
        )
      })}
    </div>
  )
}
