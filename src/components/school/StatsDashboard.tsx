'use client'

import { BarChart } from 'lucide-react'

export default function StatsDashboard() {
  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-blue-500/20 to-indigo-500/20 border-2 border-blue-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <BarChart className="w-5 h-5" /> Статистика
      </h3>
      <div className="space-y-4">
        <div className="flex justify-between items-center p-3 bg-white/5 rounded-xl">
          <span className="text-white">Уроков пройдено</span>
          <span className="text-blue-400 font-bold">42</span>
        </div>
        <div className="flex justify-between items-center p-3 bg-white/5 rounded-xl">
          <span className="text-white">Игр сыграно</span>
          <span className="text-green-400 font-bold">128</span>
        </div>
        <div className="flex justify-between items-center p-3 bg-white/5 rounded-xl">
          <span className="text-white">Время обучения</span>
          <span className="text-purple-400 font-bold">15ч 30м</span>
        </div>
        <div className="flex justify-between items-center p-3 bg-white/5 rounded-xl">
          <span className="text-white">Серия дней</span>
          <span className="text-amber-400 font-bold">7 🔥</span>
        </div>
      </div>
    </div>
  )
}
