'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Gift, Star, Sparkles } from 'lucide-react'

export default function DailyBonus({ onClose }: { onClose: () => void }) {
  const { addXP } = useSchool()
  const [claimed, setClaimed] = useState(false)

  const handleClaim = () => {
    addXP(50)
    setClaimed(true)
    setTimeout(onClose, 2000)
  }

  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4">
      <div className="bg-gradient-to-br from-purple-600 to-pink-600 rounded-3xl p-8 max-w-md w-full text-center animate-bounceIn">
        <div className="text-6xl mb-4">🎁</div>
        <h2 className="text-2xl font-black text-white mb-2">
          {claimed ? 'Получено!' : 'Ежедневный бонус!'}
        </h2>
        <p className="text-purple-200 mb-6">
          {claimed ? '+50 XP добавлены!' : 'Забери свои ежедневные 50 XP!'}
        </p>
        {!claimed && (
          <button
            onClick={handleClaim}
            className="w-full py-4 bg-gradient-to-r from-yellow-400 to-orange-500 text-white rounded-2xl font-bold text-lg hover:scale-105 transition-transform"
          >
            <Gift className="w-6 h-6 inline mr-2" />
            Забрать!
          </button>
        )}
        {claimed && (
          <div className="text-4xl animate-pulse">✨⭐✨</div>
        )}
      </div>
    </div>
  )
}
