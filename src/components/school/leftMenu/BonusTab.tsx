'use client'

import { CheckCircle, Calendar, Sparkles } from 'lucide-react'
import { dailyRewards } from './constants'

interface BonusTabProps {
  currentDay: number
  currentReward: { icon: string; reward: number }
  claimedToday: boolean
  consecutiveDays: number
  onClaim: () => void
}

export default function BonusTab({
  currentDay,
  currentReward,
  claimedToday,
  consecutiveDays,
  onClaim
}: BonusTabProps) {
  return (
    <div className="p-4 space-y-4">
      {/* Current bonus */}
      <div className="p-4 bg-gradient-to-r from-amber-500/20 to-orange-500/20 border border-amber-400/30 rounded-2xl text-center">
        <div className="text-5xl mb-2">{currentReward.icon}</div>
        <p className="text-white mb-1">Бонус за день {currentDay}</p>
        <p className="text-2xl font-black text-yellow-400">+{currentReward.reward} баллов</p>
        
        {!claimedToday ? (
          <button onClick={onClaim} className="mt-3 px-5 py-2 bg-gradient-to-r from-yellow-400 to-amber-500 text-purple-900 rounded-xl font-bold hover:scale-105 transition-transform">
            <Sparkles className="w-4 h-4 inline mr-1" /> Забрать!
          </button>
        ) : (
          <div className="mt-3 flex items-center justify-center gap-2 text-green-400">
            <CheckCircle className="w-4 h-4" /> <span className="font-bold">Получено!</span>
          </div>
        )}
      </div>

      {/* Weekly calendar */}
      <div>
        <h3 className="text-sm font-medium text-white mb-2 flex items-center gap-2">
          <Calendar className="w-4 h-4 text-amber-400" />
          Неделя ({consecutiveDays} дней подряд)
        </h3>
        <div className="grid grid-cols-7 gap-1">
          {dailyRewards.map((reward, i) => {
            const dayNum = i + 1
            const isCompleted = dayNum <= (claimedToday ? currentDay : currentDay - 1)
            const isCurrent = dayNum === currentDay && !claimedToday
            return (
              <div key={i} className={`text-center p-1.5 rounded-lg ${isCompleted ? 'bg-green-500/30 border border-green-400/50' : isCurrent ? 'bg-yellow-500/30 border border-yellow-400/50 animate-pulse' : 'bg-white/5 border border-white/10'}`}>
                <div className="text-lg">{reward.icon}</div>
                <div className="text-[10px] text-yellow-400 font-bold">+{reward.reward}</div>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
