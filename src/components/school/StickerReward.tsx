'use client'

import { Star, Trophy, Award } from 'lucide-react'

export default function StickerReward() {
  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-pink-500/20 to-rose-500/20 border-2 border-pink-500/30 text-center">
      <div className="text-6xl mb-4">⭐</div>
      <h3 className="text-xl font-bold text-white mb-2">Награда!</h3>
      <p className="text-pink-300">Ты получаешь звезду за усердие!</p>
    </div>
  )
}
