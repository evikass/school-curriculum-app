'use client'

<<<<<<< HEAD
import { useSchool } from '@/context/SchoolContext'
import { CheckCircle, Circle, Star, Zap, Trophy, Target } from 'lucide-react'

interface DailyTask {
  id: string
  title: string
  description: string
  icon: React.ReactNode
  reward: number
  checkFn: (progress: any) => boolean
}

const dailyTasks: DailyTask[] = [
  {
    id: 'daily_lesson',
    title: 'Урок дня',
    description: 'Завершить 1 урок',
    icon: <Star className="w-6 h-6 text-yellow-400" />,
    reward: 10,
    checkFn: (p) => (p.todayLessons || 0) >= 1
  },
  {
    id: 'daily_game',
    title: 'Игрок дня',
    description: 'Сыграть 1 игру',
    icon: <Trophy className="w-6 h-6 text-purple-400" />,
    reward: 10,
    checkFn: (p) => (p.todayGames || 0) >= 1
  },
  {
    id: 'daily_points',
    title: 'Охотник за очками',
    description: 'Набрать 20 очков',
    icon: <Zap className="w-6 h-6 text-orange-400" />,
    reward: 15,
    checkFn: (p) => (p.todayPoints || 0) >= 20
  },
  {
    id: 'daily_perfect',
    title: 'Идеалист',
    description: 'Пройти игру без ошибок',
    icon: <Target className="w-6 h-6 text-green-400" />,
    reward: 25,
    checkFn: (p) => p.achievements?.includes('daily_perfect')
  }
]

export default function DailyTasks() {
  const { progress } = useSchool()
  
  const completedCount = dailyTasks.filter(t => t.checkFn(progress)).length
  const progressPercent = (completedCount / dailyTasks.length) * 100

  return (
    <div className="w-full p-6 rounded-3xl bg-white/5 backdrop-blur-sm border border-white/10">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <Target className="w-8 h-8 text-purple-400" />
          <div>
            <h3 className="text-xl font-bold text-white">Задания дня</h3>
            <p className="text-purple-300 text-sm">Выполни все и получи бонус!</p>
          </div>
        </div>
        <div className="text-right">
          <span className="text-2xl font-black text-white">{completedCount}/{dailyTasks.length}</span>
          <p className="text-purple-300 text-xs">выполнено</p>
        </div>
      </div>

      {/* Progress bar */}
      <div className="h-3 bg-white/10 rounded-full mb-6 overflow-hidden">
        <div 
          className="h-full bg-gradient-to-r from-purple-500 to-pink-500 rounded-full transition-all duration-500"
          style={{ width: `${progressPercent}%` }}
        />
      </div>

      <div className="grid grid-cols-2 gap-3">
        {dailyTasks.map((task) => {
          const isCompleted = task.checkFn(progress)
          return (
            <div
              key={task.id}
              className={`p-4 rounded-2xl border-2 transition-all ${
                isCompleted 
                  ? 'bg-green-500/20 border-green-400/50' 
                  : 'bg-white/5 border-white/10'
              }`}
            >
              <div className="flex items-start gap-3">
                <div className={`mt-1 ${isCompleted ? 'opacity-100' : 'opacity-60'}`}>
                  {isCompleted ? (
                    <CheckCircle className="w-6 h-6 text-green-400" />
                  ) : (
                    <Circle className="w-6 h-6 text-white/40" />
                  )}
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-1">
                    {task.icon}
                    <h4 className={`font-bold ${isCompleted ? 'text-green-300' : 'text-white'}`}>
                      {task.title}
                    </h4>
                  </div>
                  <p className={`text-sm ${isCompleted ? 'text-green-400/70' : 'text-white/60'}`}>
                    {task.description}
                  </p>
                  <div className="flex items-center gap-1 mt-2">
                    <Zap className="w-4 h-4 text-yellow-400" />
                    <span className="text-sm text-yellow-400 font-bold">+{task.reward}</span>
                  </div>
                </div>
              </div>
            </div>
          )
        })}
      </div>

      {/* Bonus message */}
      {completedCount === dailyTasks.length && (
        <div className="mt-4 p-3 rounded-xl bg-gradient-to-r from-purple-500/30 to-pink-500/30 border border-purple-400/30 text-center">
          <p className="text-lg font-bold text-white">🎉 Все задания выполнены!</p>
          <p className="text-purple-300 text-sm">Приходи завтра за новыми заданиями</p>
        </div>
      )}
=======
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
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
    </div>
  )
}
