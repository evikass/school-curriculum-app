'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Clock } from 'lucide-react'

export function SpeedGame({ onComplete }: { onComplete: (score: number) => void }) {
  const [target, setTarget] = useState(0)
  const [numbers, setNumbers] = useState<number[]>([])
  const [timeLeft, setTimeLeft] = useState(30)
  const [isPlaying, setIsPlaying] = useState(true)
  const [score, setScore] = useState(0)

  const generateNewTarget = () => {
    setTarget(Math.floor(Math.random() * 20) + 1)
    setNumbers(Array.from({ length: 20 }, (_, i) => i + 1).sort(() => Math.random() - 0.5).slice(0, 12))
  }

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    generateNewTarget()
  }, [])
  
  useEffect(() => {
    if (!isPlaying) return
    
    const timer = setInterval(() => {
      setTimeLeft(t => {
        if (t <= 1) {
          setIsPlaying(false)
          onComplete(score)
          return 0
        }
        return t - 1
      })
    }, 1000)
    
    return () => clearInterval(timer)
  }, [isPlaying, score, onComplete])
  
  const handleClick = (num: number) => {
    if (num === target) {
      setScore(s => s + 5)
      generateNewTarget()
    }
  }
  
  return (
    <div className="text-center">
      <div className="mb-4 flex justify-between items-center">
        <span className="text-white/50">Найди: <span className="text-2xl font-bold text-yellow-400">{target}</span></span>
        <span className={`font-bold flex items-center gap-1 ${timeLeft <= 10 ? 'text-red-400 animate-pulse' : 'text-white'}`}>
          <Clock className="w-4 h-4" /> {timeLeft}с
        </span>
      </div>
      
      <div className="grid grid-cols-4 gap-2">
        {numbers.map((num) => (
          <motion.button
            key={num}
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
            onClick={() => handleClick(num)}
            className="aspect-square bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl text-2xl font-bold text-white shadow-lg hover:shadow-purple-500/30 transition-all"
          >
            {num}
          </motion.button>
        ))}
      </div>
      
      <p className="text-white/50 mt-4 text-sm">Очки: {score}</p>
    </div>
  )
}
