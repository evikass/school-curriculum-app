'use client'

import { motion } from 'framer-motion'
import { StudySession } from './types'
import { subjectColors } from './constants'

interface HistoryTabProps {
  sessions: StudySession[]
}

export function HistoryTab({ sessions }: HistoryTabProps) {
  const formatDuration = (minutes: number) => {
    if (minutes < 60) return `${minutes} мин`
    const hours = Math.floor(minutes / 60)
    const mins = minutes % 60
    return `${hours} ч ${mins} мин`
  }

  return (
    <div className="space-y-2">
      {sessions.slice(0, 10).map((session, idx) => (
        <motion.div
          key={idx}
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: idx * 0.03 }}
          className="bg-white/5 rounded-xl p-3 flex items-center gap-3"
        >
          <div className={`w-2 h-12 rounded-full ${subjectColors[session.subject] || 'bg-gray-500'}`} />
          <div className="flex-1">
            <p className="text-white font-medium">{session.subject}</p>
            <p className="text-white/50 text-sm">
              {new Date(session.date).toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' })}
            </p>
          </div>
          <div className="text-right">
            <p className="text-white">{formatDuration(session.duration)}</p>
            <p className="text-white/30 text-sm">
              {session.lessonsCompleted} уроков • {session.pointsEarned} XP
            </p>
          </div>
        </motion.div>
      ))}
    </div>
  )
}
