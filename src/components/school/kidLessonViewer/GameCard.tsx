'use client'

import { Star, Gamepad2, Play } from 'lucide-react'
import { GameLesson } from '@/data/types'

interface GameCardProps {
  game: GameLesson
  onSelect: (game: GameLesson) => void
}

export function GameCard({ game, onSelect }: GameCardProps) {
  return (
    <button onClick={() => onSelect(game)}
      className="p-8 rounded-3xl bg-gradient-to-br from-purple-500/60 to-pink-500/60 border-4 border-white/20 hover:border-yellow-400 text-left transition-all hover:scale-[1.02] group relative">
      <div className="absolute top-4 right-4 bg-yellow-400 text-purple-900 px-4 py-2 rounded-2xl font-black text-lg flex items-center gap-2">
        <Star className="w-5 h-5 fill-purple-900" />
        {game.reward?.stars || 1}
      </div>
      <div className="flex items-center gap-4 mb-4">
        <div className="p-4 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 group-hover:scale-110 transition-transform">
          <Gamepad2 className="w-10 h-10 text-white" />
        </div>
        <div>
          <h4 className="text-2xl font-bold text-white">{game.title}</h4>
          <p className="text-lg text-purple-200">{game.tasks?.length || 0} заданий</p>
        </div>
      </div>
      <div className="flex items-center gap-3 text-yellow-300 text-xl font-bold">
        <Play className="w-6 h-6" />ИГРАТЬ!
      </div>
    </button>
  )
}
