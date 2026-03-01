'use client'

import { useState, useEffect, useMemo } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Gift, Star, Zap, X, CheckCircle, Calendar, Flame, Sparkles, ChevronRight } from 'lucide-react'

const dailyRewards = [
  { day: 1, reward: 5, icon: '⭐' },
  { day: 2, reward: 10, icon: '🌟' },
  { day: 3, reward: 15, icon: '💫' },
  { day: 4, reward: 20, icon: '✨' },
  { day: 5, reward: 30, icon: '🔮' },
  { day: 6, reward: 40, icon: '💎' },
  { day: 7, reward: 100, icon: '🎁' }, // Большой бонус за неделю
]

function getInitialClaimedState(today: string): boolean {
  if (typeof window === 'undefined') return false
  const lastClaimDate = localStorage.getItem('lastBonusClaim')
  return lastClaimDate === today
}

export default function DailyBonus() {
  const { progress, addPoints } = useSchool()
  const today = new Date().toISOString().split('T')[0]
  const [isOpen, setIsOpen] = useState(false)
  const [showClaimAnimation, setShowClaimAnimation] = useState(false)
  const [claimedToday, setClaimedToday] = useState(() => getInitialClaimedState(today))

  // Calculate consecutive login days
  const consecutiveDays = useMemo(() => {
    if (typeof window === 'undefined') return 0
    
    const lastClaimDate = localStorage.getItem('lastBonusClaim')
    const savedStreak = parseInt(localStorage.getItem('bonusStreak') || '0', 10)
    
    if (!lastClaimDate) return 0
    
    const yesterday = new Date()
    yesterday.setDate(yesterday.getDate() - 1)
    const yesterdayStr = yesterday.toISOString().split('T')[0]
    
    if (lastClaimDate === yesterdayStr) {
      return savedStreak
    } else if (lastClaimDate === today) {
      return savedStreak
    }
    return 0
  }, [today])

  const currentDay = (consecutiveDays % 7) + 1
  const currentReward = dailyRewards[currentDay - 1]

  const claimBonus = () => {
    if (claimedToday) return
    
    const newStreak = consecutiveDays + 1
    localStorage.setItem('lastBonusClaim', today)
    localStorage.setItem('bonusStreak', newStreak.toString())
    
    addPoints(currentReward.reward)
    setShowClaimAnimation(true)
    setClaimedToday(true)
    
    setTimeout(() => {
      setShowClaimAnimation(false)
    }, 2000)
  }

  const getNextReward = () => {
    const nextDay = (consecutiveDays + 1) % 7 + 1
    return dailyRewards[nextDay - 1]
  }

  return (
    <>
      {/* Кнопка открытия */}
      <button
        onClick={() => setIsOpen(true)}
        className="fixed bottom-56 left-4 z-40 p-4 rounded-full 
                   bg-gradient-to-br from-amber-400 to-yellow-500 
                   shadow-xl hover:scale-110 transition-transform
                   flex items-center gap-2 text-purple-900 font-bold relative"
      >
        <Gift className="w-6 h-6" />
        {!claimedToday && (
          <span className="absolute -top-2 -right-2 w-6 h-6 bg-red-500 text-white 
                           rounded-full text-sm font-black flex items-center justify-center animate-bounce">
            !
          </span>
        )}
      </button>

      {/* Анимация получения бонуса */}
      {showClaimAnimation && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center pointer-events-none">
          <div className="animate-bounceIn">
            <div className="text-8xl mb-4 text-center">{currentReward.icon}</div>
            <div className="px-8 py-4 rounded-2xl bg-gradient-to-r from-yellow-400 to-amber-500 
                            shadow-2xl text-purple-900 text-center">
              <p className="text-2xl font-black">+{currentReward.reward} баллов!</p>
              <p className="text-lg">{consecutiveDays + 1} день подряд 🎉</p>
            </div>
          </div>
        </div>
      )}

      {/* Модальное окно */}
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 
                        bg-black/60 backdrop-blur-sm animate-fadeIn">
          <div className="w-full max-w-md 
                          bg-gradient-to-br from-gray-900 to-amber-900 
                          rounded-3xl border-4 border-amber-500/30 shadow-2xl overflow-hidden">
            {/* Header */}
            <div className="bg-amber-600 p-6 flex justify-between items-center">
              <div className="flex items-center gap-4">
                <div className="p-3 rounded-2xl bg-white/20">
                  <Gift className="w-8 h-8 text-white" />
                </div>
                <div>
                  <h2 className="text-2xl font-black text-white">Ежедневный бонус</h2>
                  <p className="text-amber-200">{consecutiveDays} дней подряд</p>
                </div>
              </div>
              <button
                onClick={() => setIsOpen(false)}
                className="p-2 rounded-xl hover:bg-white/20 transition-colors"
              >
                <X className="w-6 h-6 text-white" />
              </button>
            </div>

            {/* Current reward */}
            <div className="p-6 bg-gradient-to-r from-amber-500/20 to-orange-500/20 border-b border-amber-400/20">
              <div className="text-center">
                <div className="text-6xl mb-3">{currentReward.icon}</div>
                <p className="text-xl text-white mb-2">Бонус за день {currentDay}</p>
                <p className="text-3xl font-black text-yellow-400">+{currentReward.reward} баллов</p>
                
                {!claimedToday ? (
                  <button
                    onClick={claimBonus}
                    className="mt-4 px-8 py-3 bg-gradient-to-r from-yellow-400 to-amber-500 
                               text-purple-900 rounded-2xl font-bold text-lg hover:scale-105 transition-transform
                               flex items-center gap-2 mx-auto"
                  >
                    <Sparkles className="w-5 h-5" />
                    Забрать бонус!
                  </button>
                ) : (
                  <div className="mt-4 flex items-center justify-center gap-2 text-green-400">
                    <CheckCircle className="w-5 h-5" />
                    <span className="font-bold">Бонус получен!</span>
                  </div>
                )}
              </div>
            </div>

            {/* Week progress */}
            <div className="p-6">
              <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                <Calendar className="w-5 h-5 text-amber-400" />
                Прогресс недели
              </h3>
              
              <div className="grid grid-cols-7 gap-2">
                {dailyRewards.map((reward, i) => {
                  const dayNum = i + 1
                  const isCompleted = dayNum <= (claimedToday ? currentDay : currentDay - 1)
                  const isCurrent = dayNum === currentDay && !claimedToday
                  const isNext = dayNum === ((consecutiveDays % 7) + 2) || (currentDay === 7 && dayNum === 1)
                  
                  return (
                    <div
                      key={i}
                      className={`text-center p-2 rounded-xl transition-all ${
                        isCompleted 
                          ? 'bg-green-500/30 border-2 border-green-400/50' 
                          : isCurrent 
                            ? 'bg-yellow-500/30 border-2 border-yellow-400/50 animate-pulse' 
                            : 'bg-white/5 border-2 border-white/10'
                      }`}
                    >
                      <div className="text-2xl mb-1">{reward.icon}</div>
                      <div className="text-xs text-gray-400">День {dayNum}</div>
                      <div className="text-sm font-bold text-yellow-400">+{reward.reward}</div>
                      {isCompleted && <CheckCircle className="w-4 h-4 text-green-400 mx-auto mt-1" />}
                    </div>
                  )
                })}
              </div>
              
              {/* Next reward hint */}
              {claimedToday && (
                <div className="mt-4 p-3 rounded-xl bg-white/5 flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Flame className="w-5 h-5 text-orange-400" />
                    <span className="text-gray-300">Завтра:</span>
                  </div>
                  <div className="flex items-center gap-2 text-yellow-400 font-bold">
                    <span>{getNextReward().icon}</span>
                    <span>+{getNextReward().reward} баллов</span>
                  </div>
                </div>
              )}
            </div>

            {/* Footer */}
            <div className="p-4 bg-gray-800/50 border-t border-white/10">
              <p className="text-center text-gray-400 text-sm">
                Заходи каждый день и получай бонусы! 🎁
              </p>
            </div>
          </div>
        </div>
      )}
    </>
  )
}
