'use client'

import { BookOpen, Gamepad2, Zap, Flame, Star } from 'lucide-react'
import { getChallengeIconColor } from './utils'

interface Challenge {
  id: string
  title: string
  description: string
  icon: string
  target: number
  reward: number
}

interface ChallengesTabProps {
  challenges: Challenge[]
  completedChallenges: number
  weekNum: number
  getChallengeProgress: (icon: string) => number
}

const getIcon = (icon: string) => {
  switch (icon) {
    case 'lessons': return <BookOpen className="w-5 h-5" />
    case 'games': return <Gamepad2 className="w-5 h-5" />
    case 'points': return <Zap className="w-5 h-5" />
    case 'streak': return <Flame className="w-5 h-5" />
    default: return <Star className="w-5 h-5" />
  }
}

export default function ChallengesTab({
  challenges,
  completedChallenges,
  weekNum,
  getChallengeProgress
}: ChallengesTabProps) {
  return (
    <div className="p-4 space-y-3">
      <div className="text-center text-teal-300 text-sm mb-2">
        Неделя {weekNum} • {completedChallenges}/{challenges.length} выполнено
      </div>
      
      {challenges.map(challenge => {
        const currentProgress = getChallengeProgress(challenge.icon)
        const isCompleted = currentProgress >= challenge.target
        return (
          <div key={challenge.id} className={`p-3 rounded-xl border ${isCompleted ? 'bg-green-500/20 border-green-400/50' : 'bg-white/5 border-white/10'}`}>
            <div className="flex items-center gap-3 mb-2">
              <div className={`p-2 rounded-lg bg-gradient-to-br ${getChallengeIconColor(challenge.icon)} text-white`}>
                {getIcon(challenge.icon)}
              </div>
              <div className="flex-1">
                <h3 className={`font-medium text-sm ${isCompleted ? 'text-green-300' : 'text-white'}`}>{challenge.title}</h3>
                <p className="text-[10px] text-gray-400">{challenge.description}</p>
              </div>
              <div className="text-yellow-400 text-xs font-bold">+{challenge.reward}</div>
            </div>
            <div className="h-2 bg-gray-700 rounded-full overflow-hidden">
              <div className={`h-full rounded-full ${isCompleted ? 'bg-green-400' : 'bg-violet-400'}`} 
                   style={{ width: `${Math.min((currentProgress / challenge.target) * 100, 100)}%` }} />
            </div>
            <div className="flex justify-between text-[10px] text-gray-400 mt-1">
              <span>{currentProgress}/{challenge.target}</span>
              <span>{Math.round((currentProgress / challenge.target) * 100)}%</span>
            </div>
          </div>
        )
      })}
    </div>
  )
}
