'use client'

import { useSchool } from '@/context/SchoolContext'
import { Gamepad2, Star, Trophy } from 'lucide-react'

export default function Gameplay() {
  const { selectedGame } = useSchool()

  if (!selectedGame) {
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 border-2 border-purple-500/30 text-center">
        <Gamepad2 className="w-16 h-16 text-purple-400 mx-auto mb-4" />
        <p className="text-white">Выберите игру для начала</p>
      </div>
    )
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 border-2 border-purple-500/30">
      <h3 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
        <Gamepad2 className="w-6 h-6" /> {selectedGame.title}
      </h3>
      <p className="text-purple-300 mb-4">{selectedGame.description}</p>
      <div className="flex items-center gap-2 mb-4">
        <Star className="w-5 h-5 text-yellow-400 fill-yellow-400" />
        <span className="text-yellow-400 font-bold">+{selectedGame.reward?.stars || 10} звёзд</span>
      </div>
      <div className="space-y-3">
        {selectedGame.tasks?.map((task: string, i: number) => (
          <div key={i} className="p-4 bg-white/5 rounded-xl text-white">
            {i + 1}. {task}
          </div>
        ))}
      </div>
    </div>
  )
}
