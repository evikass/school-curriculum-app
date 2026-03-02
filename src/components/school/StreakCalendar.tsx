'use client'

import { Calendar, Flame } from 'lucide-react'

const DAYS = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

export default function StreakCalendar() {
  const today = new Date().getDay()
  const streak = 5 // Demo

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-orange-500/20 to-red-500/20 border-2 border-orange-500/30">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-bold text-white flex items-center gap-2">
          <Calendar className="w-5 h-5 text-orange-400" />
          Календарь
        </h3>
        <div className="flex items-center gap-2 text-orange-400">
          <Flame className="w-5 h-5" />
          <span className="font-bold">{streak} дней</span>
        </div>
      </div>
      <div className="grid grid-cols-7 gap-2">
        {DAYS.map((day, i) => (
          <div
            key={day}
            className={`p-2 rounded-lg text-center text-sm font-medium ${
              i < streak
                ? 'bg-orange-500 text-white'
                : i === today
                ? 'bg-orange-500/30 text-orange-300 border border-orange-400'
                : 'bg-white/10 text-white/50'
            }`}
          >
            {day}
          </div>
        ))}
      </div>
    </div>
  )
}
