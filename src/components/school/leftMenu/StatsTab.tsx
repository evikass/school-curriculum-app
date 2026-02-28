'use client'

import { Zap, BookOpen, Gamepad2, Flame, Trophy, TrendingUp } from 'lucide-react'
import { getLevel, getLeaderboard } from './constants'
import { getRankIcon } from './utils'

interface StatsTabProps {
  totalPoints: number
  completedLessons: number
  gamesPlayed: number
  streak: number
  achievements: number
  accuracy: number
}

export default function StatsTab({
  totalPoints,
  completedLessons,
  gamesPlayed,
  streak,
  achievements,
  accuracy
}: StatsTabProps) {
  const level = getLevel(totalPoints)
  const leaderboard = getLeaderboard(totalPoints, streak, gamesPlayed)
  const playerRank = leaderboard.findIndex(p => p.isPlayer) + 1

  return (
    <div className="p-4 space-y-4">
      {/* Level card */}
      <div className="p-4 bg-gradient-to-r from-indigo-500/20 to-purple-500/20 border border-white/10 rounded-xl flex items-center gap-4">
        <div className={`p-3 rounded-xl bg-gradient-to-br ${level.color}`}>
          <span className="text-3xl">{level.icon}</span>
        </div>
        <div className="flex-1">
          <p className="text-indigo-300 text-xs">Уровень</p>
          <h3 className="text-xl font-black text-white">{level.name}</h3>
          <div className="flex items-center gap-1 text-yellow-400 text-sm">
            <Zap className="w-3 h-3" /> {totalPoints} баллов
          </div>
        </div>
        <div className="text-right">
          <div className="text-3xl font-black text-white">{accuracy}%</div>
          <div className="text-indigo-300 text-xs">точность</div>
        </div>
      </div>

      {/* Stats grid */}
      <div className="grid grid-cols-2 gap-2">
        {[
          { label: 'Уроков', value: completedLessons, icon: <BookOpen className="w-4 h-4" />, color: 'text-blue-400' },
          { label: 'Игр', value: gamesPlayed, icon: <Gamepad2 className="w-4 h-4" />, color: 'text-green-400' },
          { label: 'Дней подряд', value: streak, icon: <Flame className="w-4 h-4" />, color: 'text-orange-400' },
          { label: 'Достижений', value: achievements, icon: <Trophy className="w-4 h-4" />, color: 'text-purple-400' },
        ].map((stat, i) => (
          <div key={i} className="p-3 rounded-xl bg-white/5 border border-white/10">
            <div className={`flex items-center gap-1 mb-1 ${stat.color}`}>
              {stat.icon}
              <span className="text-[10px] text-gray-400">{stat.label}</span>
            </div>
            <div className="text-xl font-black text-white">{stat.value}</div>
          </div>
        ))}
      </div>

      {/* Leaderboard */}
      <div>
        <h3 className="text-sm font-medium text-white mb-2 flex items-center gap-2">
          <TrendingUp className="w-4 h-4" /> Лидерборд (#{playerRank})
        </h3>
        <div className="space-y-1">
          {leaderboard.slice(0, 3).map((player, i) => (
            <div key={player.name} className={`p-2 rounded-lg flex items-center gap-2 ${player.isPlayer ? 'bg-yellow-400/20 border border-yellow-400/50' : 'bg-white/5'}`}>
              <div className="w-6">{getRankIcon(i + 1)}</div>
              <div className={`w-7 h-7 rounded-full flex items-center justify-center text-sm ${player.isPlayer ? 'bg-gradient-to-br from-yellow-400 to-orange-500' : 'bg-gray-600'}`}>
                {player.isPlayer ? '😊' : '👤'}
              </div>
              <span className={`flex-1 text-sm ${player.isPlayer ? 'text-white font-bold' : 'text-gray-300'}`}>{player.name}</span>
              <span className="text-white font-bold text-sm">{player.points}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
