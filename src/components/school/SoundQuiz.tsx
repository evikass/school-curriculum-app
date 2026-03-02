'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Volume2 } from 'lucide-react'

const SOUNDS = [
  { emoji: '🐕', name: 'Собака', sound: 'Гав!' },
  { emoji: '🐱', name: 'Кошка', sound: 'Мяу!' },
  { emoji: '🐄', name: 'Корова', sound: 'Му!' },
  { emoji: '🐸', name: 'Лягушка', sound: 'Ква!' },
  { emoji: '🦁', name: 'Лев', sound: 'Ррр!' },
]

export default function SoundQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [showSound, setShowSound] = useState(false)
  const [score, setScore] = useState(0)

  const sound = SOUNDS[index]
  const options = SOUNDS.filter(s => s !== sound).slice(0, 3).concat(sound).sort(() => Math.random() - 0.5)

  const answer = (name: string) => {
    if (name === sound.name) {
      addXP(10)
      setScore(s => s + 1)
    }
    setShowSound(false)
    setIndex(i => (i + 1) % SOUNDS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-orange-500/20 to-amber-500/20 border-2 border-orange-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Volume2 className="w-5 h-5" /> Звуковой квиз
      </h3>
      <div className="text-center mb-4">
        <button
          onClick={() => setShowSound(true)}
          className="text-6xl p-4 bg-white/10 rounded-2xl hover:bg-white/20 transition-colors"
        >
          {sound.emoji}
        </button>
        {showSound && (
          <div className="mt-2 text-2xl text-orange-300 animate-pulse">{sound.sound}</div>
        )}
      </div>
      <div className="grid grid-cols-2 gap-3">
        {options.map(opt => (
          <button
            key={opt.name}
            onClick={() => answer(opt.name)}
            className="p-3 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {opt.emoji} {opt.name}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
