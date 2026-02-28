'use client'

import { useSchool } from '@/context/SchoolContext'
import { GameLesson } from '@/data/types'
import { ArrowLeft, Gamepad2, Star, Play } from 'lucide-react'

export default function KidGameSection() {
  const { games, selectedClass, goBack } = useSchool()
  const gradeEmoji = selectedClass === 0 ? '🎒' : selectedClass === 1 ? '🌟' : '🦋'

  return (
    <div className="w-full animate-bounceIn">
      <button onClick={goBack} className="mb-8 flex items-center gap-3 text-white text-2xl font-bold bg-white/20 hover:bg-white/30 px-8 py-4 rounded-3xl transition-all border-4 border-white/30 hover:border-white/50">
        <ArrowLeft className="w-8 h-8" /> Назад
      </button>

      <div className="text-center mb-10">
        <div className="text-8xl mb-4 animate-float">{gradeEmoji}</div>
        <h2 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-4">ИГРЫ!</h2>
        <p className="text-2xl text-purple-200">Выбери игру и играй! 🎮</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {games.map((game: GameLesson, index: number) => (
          <GameCard key={index} game={game} />
        ))}
      </div>
    </div>
  )
}

function GameCard({ game }: { game: GameLesson }) {
  const { selectGame } = useSchool()
  
  return (
    <button onClick={() => selectGame(game)} className="group relative overflow-hidden p-8 rounded-3xl bg-gradient-to-br from-purple-500/60 to-pink-500/60 border-4 border-white/30 hover:border-yellow-400 shadow-2xl hover:shadow-yellow-400/20 transition-all duration-300 hover:scale-[1.03] text-left">
      <div className="absolute top-4 right-4 bg-yellow-400 text-purple-900 px-4 py-2 rounded-2xl font-black text-lg flex items-center gap-2">
        <Star className="w-6 h-6 fill-purple-900" />{game.reward?.stars || 1}
      </div>
      <div className="p-5 rounded-3xl bg-gradient-to-br from-yellow-400 to-orange-500 inline-block mb-5 group-hover:scale-110 transition-transform">
        <Gamepad2 className="w-14 h-14 text-white" />
      </div>
      <h3 className="text-3xl font-black text-white mb-3">{game.title}</h3>
      <p className="text-xl text-purple-200 mb-4">{game.subject}</p>
      <div className="text-white/80 text-lg">{game.tasks?.length || 0} заданий</div>
      <div className="mt-6 flex items-center gap-3 text-yellow-300 text-xl font-bold">
        <Play className="w-8 h-8" /> ИГРАТЬ!
      </div>
    </button>
  )
}
