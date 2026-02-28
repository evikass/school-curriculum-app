'use client'

import { Star, Trophy, RefreshCw, ArrowRight } from 'lucide-react'

interface GameFinishedScreenProps {
  score: number
  totalTasks: number
  stars: number
  rewardMessage: string
  onRestart: () => void
  onBack: () => void
}

export function GameFinishedScreen({ score, totalTasks, stars, rewardMessage, onRestart, onBack }: GameFinishedScreenProps) {
  const messages = ['Попробуй ещё!', 'Хорошо!', 'Отлично!']

  return (
    <div className="min-h-[60vh] flex items-center justify-center">
      <div className="bg-slate-800/80 backdrop-blur-xl rounded-3xl p-8 text-center max-w-md w-full border border-slate-700/50 shadow-2xl">
        <div className="mb-6">
          <Trophy className="w-20 h-20 mx-auto text-yellow-400 animate-bounce" />
        </div>

        <h2 className="text-3xl font-bold text-white mb-4">{messages[stars - 1]}</h2>

        <div className="flex justify-center gap-2 mb-6">
          {[1, 2, 3].map((star) => (
            <Star
              key={star}
              className={`w-12 h-12 transition-all duration-300 ${
                star <= stars
                  ? 'text-yellow-400 fill-yellow-400 scale-110'
                  : 'text-slate-600'
              }`}
              style={{ animationDelay: `${star * 0.2}s` }}
            />
          ))}
        </div>

        <p className="text-slate-300 mb-2">
          Правильных ответов: {score} из {totalTasks}
        </p>

        <p className="text-purple-300 text-lg mb-8">{rewardMessage}</p>

        <div className="flex gap-4 justify-center">
          <button
            onClick={onRestart}
            className="flex items-center gap-2 px-6 py-3 bg-slate-700 hover:bg-slate-600 rounded-xl text-white transition-colors"
          >
            <RefreshCw className="w-5 h-5" />
            Ещё раз
          </button>
          <button
            onClick={onBack}
            className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-500 hover:opacity-90 rounded-xl text-white transition-opacity"
          >
            К урокам
            <ArrowRight className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  )
}
