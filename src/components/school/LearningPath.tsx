'use client'

import { useSchool } from '@/context/SchoolContext'
import { Map, ChevronRight } from 'lucide-react'

const PATHS = [
  { id: 1, title: 'Основы счёта', subject: 'Математика', progress: 100 },
  { id: 2, title: 'Буквы и звуки', subject: 'Русский язык', progress: 75 },
  { id: 3, title: 'Окружающий мир', subject: 'Окружающий мир', progress: 30 },
  { id: 4, title: 'Чтение', subject: 'Литература', progress: 0 },
]

export default function LearningPath() {
  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-violet-500/20 to-purple-500/20 border-2 border-violet-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Map className="w-5 h-5 text-violet-400" />
        Путь обучения
      </h3>
      <div className="space-y-3">
        {PATHS.map(path => (
          <div
            key={path.id}
            className="p-4 rounded-xl bg-white/5 border border-white/10 hover:border-violet-400/50 transition-colors"
          >
            <div className="flex items-center justify-between mb-2">
              <span className="font-bold text-white">{path.title}</span>
              <span className="text-sm text-purple-300">{path.subject}</span>
            </div>
            <div className="h-2 bg-white/10 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-violet-400 to-purple-500 transition-all"
                style={{ width: `${path.progress}%` }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
