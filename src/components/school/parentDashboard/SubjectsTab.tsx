'use client'

import { motion } from 'framer-motion'
import { PieChart, Target, ChevronRight } from 'lucide-react'
import { SessionStats } from './types'
import { subjectColors } from './constants'

interface SubjectsTabProps {
  stats: SessionStats
}

export function SubjectsTab({ stats }: SubjectsTabProps) {
  const formatDuration = (minutes: number) => {
    if (minutes < 60) return `${minutes} мин`
    const hours = Math.floor(minutes / 60)
    const mins = minutes % 60
    return `${hours} ч ${mins} мин`
  }

  return (
    <div className="space-y-3">
      <div className="bg-white/5 rounded-2xl p-4">
        <h4 className="text-white font-medium mb-3 flex items-center gap-2">
          <PieChart className="w-4 h-4 text-purple-400" />
          Распределение по предметам
        </h4>
        <div className="space-y-3">
          {Object.entries(stats.bySubject).map(([subject, data], idx) => {
            const total = Object.values(stats.bySubject).reduce((s, d) => s + d.duration, 0)
            const percent = Math.round((data.duration / total) * 100)

            return (
              <div key={subject}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="text-white">{subject}</span>
                  <span className="text-white/50">{formatDuration(data.duration)}</span>
                </div>
                <div className="h-2 bg-white/10 rounded-full overflow-hidden">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${percent}%` }}
                    transition={{ delay: idx * 0.1 }}
                    className={`h-full ${subjectColors[subject] || 'bg-gray-500'}`}
                  />
                </div>
              </div>
            )
          })}
        </div>
      </div>

      {/* Recommendations */}
      <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-2xl p-4">
        <h4 className="text-emerald-300 font-medium mb-2 flex items-center gap-2">
          <Target className="w-4 h-4" />
          Рекомендации
        </h4>
        <ul className="text-emerald-200/80 text-sm space-y-2">
          <li className="flex items-start gap-2">
            <ChevronRight className="w-4 h-4 mt-0.5" />
            <span>Рекомендуется заниматься 20-30 минут в день</span>
          </li>
          <li className="flex items-start gap-2">
            <ChevronRight className="w-4 h-4 mt-0.5" />
            <span>Чередуйте предметы для лучшего запоминания</span>
          </li>
          <li className="flex items-start gap-2">
            <ChevronRight className="w-4 h-4 mt-0.5" />
            <span>Игры помогают закрепить материал</span>
          </li>
        </ul>
      </div>
    </div>
  )
}
