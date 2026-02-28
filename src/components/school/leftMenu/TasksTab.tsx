'use client'

import { BookOpen, Gamepad2, Zap, Flame, CheckCircle, Gift, Star } from 'lucide-react'

interface DailyTask {
  id: string
  title: string
  description: string
  points: number
  progress: number
  total: number
  type: 'lessons' | 'games' | 'points' | 'streak'
  icon: 'book' | 'game' | 'zap' | 'flame'
}

interface TasksTabProps {
  tasks: DailyTask[]
  todayLessons: number
  todayGames: number
  todayPoints: number
  allCompleted: boolean
  totalReward: number
  taskBonusClaimed: boolean
  onClaimBonus: () => void
}

const getIcon = (icon: string) => {
  switch (icon) {
    case 'book': return <BookOpen className="w-5 h-5" />
    case 'game': return <Gamepad2 className="w-5 h-5" />
    case 'zap': return <Zap className="w-5 h-5" />
    case 'flame': return <Flame className="w-5 h-5" />
    default: return <Star className="w-5 h-5" />
  }
}

export default function TasksTab({
  tasks,
  todayLessons,
  todayGames,
  todayPoints,
  allCompleted,
  totalReward,
  taskBonusClaimed,
  onClaimBonus
}: TasksTabProps) {
  return (
    <div className="p-4 space-y-3">
      {/* Stats grid */}
      <div className="grid grid-cols-3 gap-2 mb-3">
        <div className="text-center p-2 rounded-xl bg-white/5 border border-white/10">
          <BookOpen className="w-4 h-4 text-blue-400 mx-auto mb-1" />
          <div className="text-base font-black text-white">{todayLessons}</div>
          <div className="text-[10px] text-teal-300">уроков</div>
        </div>
        <div className="text-center p-2 rounded-xl bg-white/5 border border-white/10">
          <Gamepad2 className="w-4 h-4 text-green-400 mx-auto mb-1" />
          <div className="text-base font-black text-white">{todayGames}</div>
          <div className="text-[10px] text-teal-300">игр</div>
        </div>
        <div className="text-center p-2 rounded-xl bg-white/5 border border-white/10">
          <Zap className="w-4 h-4 text-yellow-400 mx-auto mb-1" />
          <div className="text-base font-black text-white">{todayPoints}</div>
          <div className="text-[10px] text-teal-300">баллов</div>
        </div>
      </div>

      {/* Bonus claim */}
      {allCompleted && !taskBonusClaimed && (
        <div className="p-3 bg-gradient-to-r from-yellow-400/20 to-orange-400/20 border border-yellow-400/30 rounded-xl text-center">
          <Gift className="w-5 h-5 text-yellow-400 mx-auto mb-1" />
          <p className="font-bold text-yellow-300 text-sm mb-2">Все задания выполнены! 🎉</p>
          <button onClick={onClaimBonus} className="px-3 py-1.5 bg-yellow-400 text-purple-900 rounded-lg font-bold text-xs">
            Забрать {totalReward} баллов!
          </button>
        </div>
      )}

      {/* Tasks list */}
      {tasks.filter(t => t.points > 0).map(task => {
        const isCompleted = task.progress >= task.total
        return (
          <div key={task.id} className={`p-3 rounded-xl border ${isCompleted ? 'bg-green-500/20 border-green-400/50' : 'bg-white/5 border-white/10'}`}>
            <div className="flex items-center gap-2 mb-2">
              <div className={`p-1.5 rounded-lg ${isCompleted ? 'bg-green-500 text-white' : 'bg-gray-600 text-gray-300'}`}>
                {isCompleted ? <CheckCircle className="w-4 h-4" /> : getIcon(task.icon)}
              </div>
              <div className="flex-1">
                <h3 className={`font-medium text-sm ${isCompleted ? 'text-green-300' : 'text-white'}`}>{task.title}</h3>
                <p className="text-[10px] text-gray-400">{task.description}</p>
              </div>
              <div className="text-yellow-400 text-xs font-bold">+{task.points}</div>
            </div>
            <div className="h-1.5 bg-gray-700 rounded-full overflow-hidden">
              <div className={`h-full rounded-full ${isCompleted ? 'bg-green-400' : 'bg-teal-400'}`} 
                   style={{ width: `${Math.min((task.progress / task.total) * 100, 100)}%` }} />
            </div>
          </div>
        )
      })}
    </div>
  )
}
