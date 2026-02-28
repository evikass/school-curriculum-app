'use client'

import { motion } from 'framer-motion'
import { Clock, BookOpen, Gamepad2, Star, TrendingUp, Award } from 'lucide-react'
import { SessionStats } from './types'

interface OverviewTabProps {
  stats: SessionStats
  sessions: { date: string; duration: number }[]
  totalStars: number
  totalPoints: number
  achievements: string[]
}

export function OverviewTab({ stats, sessions, totalStars, totalPoints, achievements }: OverviewTabProps) {
  const formatDuration = (minutes: number) => {
    if (minutes < 60) return `${minutes} мин`
    const hours = Math.floor(minutes / 60)
    const mins = minutes % 60
    return `${hours} ч ${mins} мин`
  }

  return (
    <div className="space-y-4">
      {/* Stats cards */}
      <div className="grid grid-cols-2 gap-3">
        <div className="bg-white/5 rounded-2xl p-4">
          <div className="flex items-center gap-2 text-white/50 mb-2">
            <Clock className="w-4 h-4" />
            <span className="text-sm">Время учёбы</span>
          </div>
          <p className="text-2xl font-bold text-white">{formatDuration(stats.totalDuration)}</p>
          <p className="text-xs text-emerald-400 flex items-center gap-1 mt-1">
            <TrendingUp className="w-3 h-3" />
            +{formatDuration(stats.weekDuration)} за неделю
          </p>
        </div>

        <div className="bg-white/5 rounded-2xl p-4">
          <div className="flex items-center gap-2 text-white/50 mb-2">
            <BookOpen className="w-4 h-4" />
            <span className="text-sm">Уроков пройдено</span>
          </div>
          <p className="text-2xl font-bold text-white">{stats.totalLessons}</p>
          <p className="text-xs text-white/30 mt-1">~{stats.avgDuration} мин на урок</p>
        </div>

        <div className="bg-white/5 rounded-2xl p-4">
          <div className="flex items-center gap-2 text-white/50 mb-2">
            <Gamepad2 className="w-4 h-4" />
            <span className="text-sm">Игр сыграно</span>
          </div>
          <p className="text-2xl font-bold text-white">{stats.totalGames}</p>
        </div>

        <div className="bg-white/5 rounded-2xl p-4">
          <div className="flex items-center gap-2 text-white/50 mb-2">
            <Star className="w-4 h-4" />
            <span className="text-sm">Награды</span>
          </div>
          <p className="text-2xl font-bold text-white">{totalStars} ⭐</p>
          <p className="text-xs text-yellow-400 mt-1">{totalPoints} XP</p>
        </div>
      </div>

      {/* Weekly activity */}
      <div className="bg-white/5 rounded-2xl p-4">
        <h4 className="text-white font-medium mb-3 flex items-center gap-2">
          <TrendingUp className="w-4 h-4 text-emerald-400" />
          Активность за неделю
        </h4>
        <div className="flex gap-1">
          {Array.from({ length: 7 }).map((_, idx) => {
            const day = new Date()
            day.setDate(day.getDate() - (6 - idx))
            const dayStr = day.toISOString().split('T')[0]
            const daySessions = sessions.filter(s => s.date === dayStr)
            const duration = daySessions.reduce((sum, s: { date: string; duration: number }) => sum + s.duration, 0)
            const maxDuration = 60
            const height = Math.min(100, (duration / maxDuration) * 100)

            return (
              <div key={idx} className="flex-1 flex flex-col items-center">
                <div className="w-full h-20 bg-white/5 rounded flex items-end">
                  <motion.div
                    initial={{ height: 0 }}
                    animate={{ height: `${height}%` }}
                    transition={{ delay: idx * 0.05 }}
                    className={`w-full rounded-t ${duration > 30 ? 'bg-emerald-500' : duration > 0 ? 'bg-emerald-500/50' : 'bg-white/10'}`}
                  />
                </div>
                <span className="text-[10px] text-white/30 mt-1">
                  {['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'][day.getDay() - 1] || 'Вс'}
                </span>
              </div>
            )
          })}
        </div>
      </div>

      {/* Achievements */}
      <div className="bg-white/5 rounded-2xl p-4">
        <h4 className="text-white font-medium mb-3 flex items-center gap-2">
          <Award className="w-4 h-4 text-yellow-400" />
          Достижения ({achievements.length})
        </h4>
        <div className="flex flex-wrap gap-2">
          {achievements.length > 0 ? (
            achievements.slice(0, 6).map((ach, idx) => (
              <div key={idx} className="px-3 py-1 rounded-full text-sm bg-yellow-500/20 text-yellow-300">
                🏆 {ach}
              </div>
            ))
          ) : (
            <p className="text-white/50 text-sm">Пока нет достижений</p>
          )}
        </div>
      </div>
    </div>
  )
}
