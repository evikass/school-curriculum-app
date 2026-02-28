'use client'

import { motion } from 'framer-motion'
import { Clock, CheckCircle, Trash2 } from 'lucide-react'
import { ScheduleItem } from './types'
import { subjects } from './constants'

interface ScheduleListItemProps {
  item: ScheduleItem
  index: number
  onToggle: (id: string) => void
  onRemove: (id: string) => void
}

export function ScheduleListItem({ item, index, onToggle, onRemove }: ScheduleListItemProps) {
  const subjectInfo = subjects.find(s => s.name === item.subject) || subjects[0]

  return (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ delay: index * 0.05 }}
      className={`flex items-center gap-3 p-3 rounded-xl
        ${item.active ? 'bg-white/5' : 'bg-white/5 opacity-50'}`}
    >
      <span className="text-2xl">{subjectInfo.icon}</span>
      <div className="flex-1">
        <p className="text-white font-medium">{item.subject}</p>
        <p className="text-white/50 text-sm flex items-center gap-2">
          <Clock className="w-3 h-3" />
          {item.time} • {item.duration} мин
        </p>
      </div>
      <div className="flex items-center gap-2">
        <button
          onClick={() => onToggle(item.id)}
          className={`p-2 rounded-lg transition-colors
            ${item.active
              ? 'bg-green-500/20 text-green-400'
              : 'bg-white/5 text-white/30'}`}
        >
          <CheckCircle className="w-4 h-4" />
        </button>
        <button
          onClick={() => onRemove(item.id)}
          className="p-2 hover:bg-red-500/20 rounded-lg text-white/30 hover:text-red-400 transition-colors"
        >
          <Trash2 className="w-4 h-4" />
        </button>
      </div>
    </motion.div>
  )
}
