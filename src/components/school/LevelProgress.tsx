'use client'

import { useSchool } from '@/context/SchoolContext'
import { Star } from 'lucide-react'

export default function LevelProgress() {
  const { xp, level } = useSchool()
  const xpForNextLevel = level * 100
  const progress = (xp % xpForNextLevel) / xpForNextLevel * 100

  return (
    <div className="mb-4 p-3 rounded-xl bg-white/10 border border-white/20">
      <div className="flex items-center gap-3">
        <div className="p-2 rounded-lg bg-yellow-500/30">
          <Star className="w-5 h-5 text-yellow-400 fill-yellow-400" />
        </div>
        <div className="flex-1">
          <div className="flex justify-between text-sm mb-1">
            <span className="text-white font-bold">Уровень {level}</span>
            <span className="text-purple-300">{xp} XP</span>
          </div>
          <div className="h-2 bg-white/20 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-yellow-400 to-orange-500 transition-all"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>
      </div>
    </div>
  )
}
