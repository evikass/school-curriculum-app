'use client'

import { motion } from 'framer-motion'
import { Plus } from 'lucide-react'
import { subjects, dayNames } from './constants'

interface AddScheduleFormProps {
  show: boolean
  newItem: { subject: string; time: string; duration: number; days: number[] }
  setNewItem: (item: { subject: string; time: string; duration: number; days: number[] }) => void
  onAdd: () => void
  onCancel: () => void
}

export function AddScheduleForm({ show, newItem, setNewItem, onAdd, onCancel }: AddScheduleFormProps) {
  if (!show) return null

  const toggleDay = (day: number) => {
    const newDays = newItem.days.includes(day)
      ? newItem.days.filter(d => d !== day)
      : [...newItem.days, day]
    setNewItem({ ...newItem, days: newDays.sort() })
  }

  return (
    <motion.div
      initial={{ height: 0, opacity: 0 }}
      animate={{ height: 'auto', opacity: 1 }}
      exit={{ height: 0, opacity: 0 }}
      className="border-t border-white/10 pt-4 overflow-hidden"
    >
      <div className="space-y-3">
        <select
          value={newItem.subject}
          onChange={(e) => setNewItem({ ...newItem, subject: e.target.value })}
          className="w-full bg-white/10 text-white rounded-xl p-3 border border-white/10"
        >
          {subjects.map(s => (
            <option key={s.name} value={s.name} className="bg-slate-800">
              {s.icon} {s.name}
            </option>
          ))}
        </select>

        <div className="flex gap-2">
          <input
            type="time"
            value={newItem.time}
            onChange={(e) => setNewItem({ ...newItem, time: e.target.value })}
            className="flex-1 bg-white/10 text-white rounded-xl p-3 border border-white/10"
          />
          <input
            type="number"
            value={newItem.duration}
            onChange={(e) => setNewItem({ ...newItem, duration: parseInt(e.target.value) || 30 })}
            min={10}
            max={120}
            className="w-24 bg-white/10 text-white rounded-xl p-3 border border-white/10"
          />
          <span className="flex items-center text-white/50 text-sm">мин</span>
        </div>

        <div className="flex gap-1">
          {dayNames.map((day, idx) => (
            <button
              key={idx}
              onClick={() => toggleDay(idx)}
              className={`flex-1 py-2 rounded-lg text-sm font-medium transition-all
                ${newItem.days.includes(idx)
                  ? 'bg-blue-500 text-white'
                  : 'bg-white/5 text-white/50 hover:bg-white/10'
                }`}
            >
              {day}
            </button>
          ))}
        </div>

        <div className="flex gap-2">
          <button
            onClick={onCancel}
            className="flex-1 py-3 bg-white/5 hover:bg-white/10 text-white rounded-xl transition-colors"
          >
            Отмена
          </button>
          <button
            onClick={onAdd}
            className="flex-1 py-3 bg-blue-500 hover:bg-blue-600 text-white rounded-xl transition-colors flex items-center justify-center gap-2"
          >
            <Plus className="w-4 h-4" />
            Добавить
          </button>
        </div>
      </div>
    </motion.div>
  )
}
