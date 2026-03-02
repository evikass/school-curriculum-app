'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Calendar, CheckCircle } from 'lucide-react'

const TASKS = [
  { id: 1, title: 'Пройти урок математики', xp: 50 },
  { id: 2, title: 'Сыграть 3 игры', xp: 30 },
  { id: 3, title: 'Открыть достижение', xp: 40 },
]

export default function DailyTasksDisplay() {
  const { addXP } = useSchool()
  const [completed, setCompleted] = useState<number[]>([])

  const complete = (id: number, xp: number) => {
    if (!completed.includes(id)) {
      addXP(xp)
      setCompleted([...completed, id])
    }
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-orange-500/20 to-amber-500/20 border-2 border-orange-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Calendar className="w-5 h-5" /> Задания на сегодня
      </h3>
      <div className="space-y-3">
        {TASKS.map(task => (
          <div
            key={task.id}
            className={`p-4 rounded-xl flex items-center justify-between ${
              completed.includes(task.id) ? 'bg-green-500/20' : 'bg-white/5'
            }`}
          >
            <div>
              <p className="text-white font-medium">{task.title}</p>
              <p className="text-orange-300 text-sm">+{task.xp} XP</p>
            </div>
            {completed.includes(task.id) ? (
              <CheckCircle className="text-green-400 w-6 h-6" />
            ) : (
              <button
                onClick={() => complete(task.id, task.xp)}
                className="px-4 py-2 bg-orange-500 text-white rounded-lg text-sm font-bold"
              >
                Выполнить
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}
