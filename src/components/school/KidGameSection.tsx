'use client'

import { useSchool } from '@/context/SchoolContext'
import { GameLesson } from '@/data/types'
import { ArrowLeft, Gamepad2, Star, Play, Sparkles, PartyPopper } from 'lucide-react'

export default function KidGameSection() {
  const { games, selectedClass, selectGame, goBack } = useSchool()
  
  const safeGames = Array.isArray(games) ? games : []
  const gradeEmoji = selectedClass === 0 ? '🎈' : selectedClass === 1 ? '🌟' : '🌈'

  return (
    <div className="w-full">
      <button onClick={goBack}
        className="mb-6 flex items-center gap-3 text-white text-2xl font-black bg-white/10 hover:bg-white/20 
          px-8 py-4 rounded-3xl transition-all hover:scale-105 active:scale-95">
        <ArrowLeft className="w-8 h-8" /> 
        <span>Назад</span>
      </button>

      {/* Header with animation */}
      <div className="text-center mb-10 animate-bounceIn">
        <div className="inline-flex items-center gap-4 mb-6">
          <Sparkles className="w-12 h-12 text-yellow-400 animate-pulse" />
          <Gamepad2 className="w-20 h-20 text-purple-400 animate-bounce" />
          <Sparkles className="w-12 h-12 text-yellow-400 animate-pulse" />
        </div>
        
        <h2 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text 
          bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-4">
          {gradeEmoji} Игры! {gradeEmoji}
        </h2>
        
        <p className="text-2xl text-purple-200 flex items-center justify-center gap-2">
          <PartyPopper className="w-6 h-6" />
          {safeGames.length}好玩的游戏
          <PartyPopper className="w-6 h-6" />
        </p>
      </div>

      {/* Big game cards for kids */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        {safeGames.map((game: GameLesson, index: number) => (
          <button 
            key={index} 
            onClick={() => selectGame(game)}
            className="group relative overflow-hidden p-8 rounded-3xl 
              bg-gradient-to-br from-purple-500/40 to-pink-500/40 
              border-4 border-white/30 hover:border-yellow-400 
              shadow-xl hover:shadow-2xl hover:shadow-purple-500/30
              hover:scale-[1.03] active:scale-95 transition-all duration-300 text-left"
          >
            {/* Animated background */}
            <div className="absolute inset-0 bg-gradient-to-r from-yellow-400/0 via-white/10 to-yellow-400/0 
              translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000" />
            
            {/* Icon */}
            <div className="relative p-6 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 
              inline-block mb-6 group-hover:scale-110 group-hover:rotate-3 transition-transform">
              <Gamepad2 className="w-16 h-16 text-white" />
            </div>
            
            {/* Title */}
            <h3 className="relative text-3xl font-black text-white mb-3">
              {game.title}
            </h3>
            
            {/* Subject */}
            <p className="relative text-xl text-purple-200 mb-4 flex items-center gap-2">
              <span className="text-2xl">
                {game.subject === 'Математика' ? '🔢' :
                 game.subject === 'Русский язык' ? '📝' :
                 game.subject === 'Окружающий мир' ? '🌍' :
                 game.subject === 'Литература' ? '📚' : '🎮'}
              </span>
              {game.subject}
            </p>
            
            {/* Info */}
            <div className="relative flex items-center gap-4 mb-6 flex-wrap">
              <span className="text-lg text-white/90 bg-white/20 px-4 py-2 rounded-xl">
                {game.tasks?.length || 0} заданий
              </span>
              <span className="flex items-center gap-2 text-xl text-yellow-400">
                <Star className="w-6 h-6 fill-yellow-400" />
                {game.reward?.stars || 0}
              </span>
            </div>
            
            {/* Play button */}
            <div className="relative flex items-center gap-3 text-white text-xl font-bold 
              bg-gradient-to-r from-green-400 to-emerald-500 px-6 py-4 rounded-2xl
              group-hover:from-green-300 group-hover:to-emerald-400 transition-all">
              <Play className="w-8 h-8 group-hover:scale-125 transition-transform" />
              <span>Играть!</span>
              <Sparkles className="w-6 h-6 ml-auto animate-pulse" />
            </div>
          </button>
        ))}
      </div>
      
      {/* Fun footer */}
      <div className="mt-10 text-center">
        <p className="text-2xl text-white/60">
          Выбери игру и получи звёздочки! ⭐
        </p>
      </div>
    </div>
  )
}
