'use client'

import { TrendingUp } from 'lucide-react'

export default function SubjectProgress() {
  const subjects = [
    { name: 'Математика', progress: 75, color: 'from-blue-500 to-cyan-500' },
    { name: 'Русский язык', progress: 60, color: 'from-pink-500 to-rose-500' },
    { name: 'Окружающий мир', progress: 45, color: 'from-green-500 to-emerald-500' },
  ]

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-violet-500/20 to-purple-500/20 border-2 border-violet-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <TrendingUp className="w-5 h-5" /> Прогресс по предметам
      </h3>
      <div className="space-y-4">
        {subjects.map(s => (
          <div key={s.name}>
            <div className="flex justify-between mb-1">
              <span className="text-white">{s.name}</span>
              <span className="text-violet-300">{s.progress}%</span>
            </div>
            <div className="h-2 bg-white/20 rounded-full overflow-hidden">
              <div className={`h-full bg-gradient-to-r ${s.color} transition-all`} style={{ width: `${s.progress}%` }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
