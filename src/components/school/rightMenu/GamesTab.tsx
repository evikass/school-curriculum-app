'use client'

import { Zap, Trophy } from 'lucide-react'
import { MathGame, MemoryGame } from './MiniGames'

interface GamesTabProps {
  selectedGame: 'math' | 'memory' | null
  setSelectedGame: (g: 'math' | 'memory' | null) => void
  finalScore: number | null
  setFinalScore: (s: number | null) => void
  addPoints: (p: number) => void
  onClose: () => void
}

const games = [
  { id: 'math' as const, title: 'Математика', emoji: '🧮', description: 'Решай примеры', color: 'from-blue-500 to-cyan-500' },
  { id: 'memory' as const, title: 'Память', emoji: '🧠', description: 'Запоминай', color: 'from-purple-500 to-pink-500' },
]

export default function GamesTab({ selectedGame, setSelectedGame, finalScore, setFinalScore, addPoints, onClose }: GamesTabProps) {
  const handleGameComplete = (score: number) => {
    setFinalScore(score)
    addPoints(score)
  }

  const resetGame = () => {
    setSelectedGame(null)
    setFinalScore(null)
  }

  if (finalScore !== null) {
    return (
      <div className="p-4">
        <div className="text-center py-6">
          <Trophy className="w-12 h-12 text-yellow-400 mx-auto mb-3" />
          <h4 className="text-xl font-bold text-white mb-2">Игра окончена!</h4>
          <p className="text-yellow-400 text-2xl font-black mb-4">{finalScore} очков</p>
          <div className="flex gap-2 justify-center">
            <button onClick={resetGame} className="px-4 py-2 bg-white/10 text-white rounded-xl text-sm">Заново</button>
            <button onClick={() => { resetGame(); onClose() }} className="px-4 py-2 bg-emerald-500 text-white rounded-xl text-sm">Готово</button>
          </div>
        </div>
      </div>
    )
  }

  if (selectedGame) {
    return (
      <div className="p-4">
        {selectedGame === 'math' && <MathGame onComplete={handleGameComplete} />}
        {selectedGame === 'memory' && <MemoryGame onComplete={handleGameComplete} />}
      </div>
    )
  }

  return (
    <div className="p-4">
      <div className="space-y-2">
        {games.map(game => (
          <button key={game.id} onClick={() => setSelectedGame(game.id)}
            className={`w-full p-3 rounded-xl text-left bg-gradient-to-r ${game.color} flex items-center gap-3`}>
            <span className="text-3xl">{game.emoji}</span>
            <div>
              <h4 className="text-white font-bold">{game.title}</h4>
              <p className="text-white/70 text-xs">{game.description}</p>
            </div>
            <Zap className="w-4 h-4 text-white/50 ml-auto" />
          </button>
        ))}
      </div>
    </div>
  )
}
