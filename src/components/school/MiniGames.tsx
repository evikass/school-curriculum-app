'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Gamepad2, X, RotateCcw, Trophy, Zap } from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'
import { MathGame } from './mini-games/MathGame'
import { SpeedGame } from './mini-games/SpeedGame'
import { MemoryGame } from './mini-games/MemoryGame'

type GameType = 'math' | 'speed' | 'memory'

const games = [
  { id: 'math' as GameType, title: 'Математика', emoji: '🧮', description: 'Решай примеры на скорость', color: 'from-blue-500 to-cyan-500' },
  { id: 'speed' as GameType, title: 'Скорость', emoji: '⚡', description: 'Находи числа за 30 секунд', color: 'from-yellow-500 to-orange-500' },
  { id: 'memory' as GameType, title: 'Память', emoji: '🧠', description: 'Запоминай последовательности', color: 'from-purple-500 to-pink-500' },
]

export default function MiniGames() {
  const { addPoints } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [selectedGame, setSelectedGame] = useState<GameType | null>(null)
  const [finalScore, setFinalScore] = useState<number | null>(null)
  
  const handleGameComplete = (score: number) => {
    setFinalScore(score)
    addPoints(score)
  }
  
  const resetGame = () => {
    setSelectedGame(null)
    setFinalScore(null)
  }
  
  return (
    <>
      {!isOpen && (
        <motion.button
          initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}
          onClick={() => setIsOpen(true)}
          className="fixed left-4 bottom-40 z-40 bg-gradient-to-r from-emerald-500 to-teal-500 p-4 rounded-full shadow-lg shadow-emerald-500/30 border-2 border-white/20 group"
        >
          <Gamepad2 className="w-6 h-6 text-white" />
          <span className="absolute left-full ml-3 bg-gray-900/90 text-white px-3 py-2 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity">Мини-игры</span>
        </motion.button>
      )}
      
      <AnimatePresence>
        {isOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="bg-gradient-to-br from-slate-900 to-slate-800 rounded-3xl max-w-md w-full overflow-hidden shadow-2xl border-2 border-white/10">
              
              <div className="p-4 border-b border-white/10">
                <div className="flex justify-between items-center">
                  <div className="flex items-center gap-3">
                    <div className="p-2 bg-emerald-500/30 rounded-xl"><Gamepad2 className="w-5 h-5 text-emerald-300" /></div>
                    <h3 className="text-lg font-bold text-white">Мини-игры</h3>
                  </div>
                  <button onClick={() => setIsOpen(false)} className="text-white/50 hover:text-white"><X className="w-5 h-5" /></button>
                </div>
              </div>
              
              <div className="p-4">
                {!selectedGame && !finalScore ? (
                  <div className="space-y-3">
                    {games.map((game) => (
                      <motion.button key={game.id} whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}
                        onClick={() => setSelectedGame(game.id)}
                        className={`w-full p-4 rounded-2xl text-left bg-gradient-to-r ${game.color} hover:opacity-90 transition-all flex items-center gap-4`}>
                        <span className="text-4xl">{game.emoji}</span>
                        <div><h4 className="text-white font-bold text-lg">{game.title}</h4><p className="text-white/70 text-sm">{game.description}</p></div>
                        <Zap className="w-5 h-5 text-white/50 ml-auto" />
                      </motion.button>
                    ))}
                  </div>
                ) : finalScore !== null ? (
                  <div className="text-center py-8">
                    <motion.div animate={{ rotate: 360 }} transition={{ duration: 1 }}><Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" /></motion.div>
                    <h4 className="text-2xl font-bold text-white mb-2">Игра окончена!</h4>
                    <p className="text-yellow-400 text-3xl font-black mb-4">{finalScore} очков</p>
                    <div className="flex gap-2 justify-center">
                      <button onClick={resetGame} className="px-6 py-3 bg-white/10 hover:bg-white/20 text-white rounded-xl font-medium flex items-center gap-2"><RotateCcw className="w-5 h-5" />Заново</button>
                      <button onClick={() => setIsOpen(false)} className="px-6 py-3 bg-emerald-500 hover:bg-emerald-600 text-white rounded-xl font-medium">Готово</button>
                    </div>
                  </div>
                ) : (
                  <div>
                    {selectedGame === 'math' && <MathGame onComplete={handleGameComplete} />}
                    {selectedGame === 'speed' && <SpeedGame onComplete={handleGameComplete} />}
                    {selectedGame === 'memory' && <MemoryGame onComplete={handleGameComplete} />}
                  </div>
                )}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}
