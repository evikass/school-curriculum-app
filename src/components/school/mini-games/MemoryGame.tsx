'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'

export function MemoryGame({ onComplete }: { onComplete: (score: number) => void }) {
  const [sequence, setSequence] = useState<number[]>([])
  const [playerSeq, setPlayerSeq] = useState<number[]>([])
  const [showingSeq, setShowingSeq] = useState(true)
  const [activeTile, setActiveTile] = useState<number | null>(null)
  const [score, setScore] = useState(0)
  const [level, setLevel] = useState(1)
  
  useEffect(() => {
    const newSeq = [...sequence, Math.floor(Math.random() * 9)]
    setSequence(newSeq)
    setPlayerSeq([])
    
    let idx = 0
    const showInterval = setInterval(() => {
      if (idx < newSeq.length) {
        setActiveTile(newSeq[idx])
        setTimeout(() => setActiveTile(null), 400)
        idx++
      } else {
        setShowingSeq(false)
        clearInterval(showInterval)
      }
    }, 600)
    
    return () => clearInterval(showInterval)
  }, [level])
  
  const handleTileClick = (tile: number) => {
    if (showingSeq) return
    
    const newPlayerSeq = [...playerSeq, tile]
    setPlayerSeq(newPlayerSeq)
    
    if (newPlayerSeq[newPlayerSeq.length - 1] !== sequence[newPlayerSeq.length - 1]) {
      onComplete(score)
      return
    }
    
    if (newPlayerSeq.length === sequence.length) {
      setScore(s => s + level * 10)
      if (level < 10) {
        setLevel(l => l + 1)
        setShowingSeq(true)
      } else {
        onComplete(score + level * 10)
      }
    }
  }
  
  return (
    <div className="text-center">
      <div className="mb-4 flex justify-between items-center">
        <span className="text-white/50">Уровень {level}</span>
        <span className="text-yellow-400 font-bold">Очки: {score}</span>
      </div>
      
      <p className={`text-white mb-4 ${showingSeq ? 'animate-pulse' : ''}`}>
        {showingSeq ? 'Запомни последовательность...' : 'Повтори!'}
      </p>
      
      <div className="grid grid-cols-3 gap-3">
        {Array.from({ length: 9 }, (_, i) => (
          <motion.button
            key={i}
            whileHover={{ scale: showingSeq ? 1 : 1.05 }}
            whileTap={{ scale: showingSeq ? 1 : 0.95 }}
            onClick={() => handleTileClick(i)}
            disabled={showingSeq}
            className={`aspect-square rounded-2xl transition-all duration-200
              ${activeTile === i 
                ? 'bg-yellow-400 shadow-lg shadow-yellow-500/50' 
                : 'bg-white/10 hover:bg-white/20 border-2 border-white/20'
              }`}
          >
            <span className={`text-2xl font-bold ${activeTile === i ? 'text-purple-900' : 'text-white/30'}`}>
              {i + 1}
            </span>
          </motion.button>
        ))}
      </div>
    </div>
  )
}
