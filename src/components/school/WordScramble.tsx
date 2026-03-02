'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { CheckCircle } from 'lucide-react'

export default function WordScramble() {
  const { addXP } = useSchool()
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)

  const WORDS = [
    { scrambled: 'КОТ', word: 'КОТ' },
    { scrambled: 'МАК', word: 'МАК' },
    { scrambled: 'СОН', word: 'СОН' },
  ]

  const [index, setIndex] = useState(0)
  const current = WORDS[index]

  const check = () => {
    if (input.toUpperCase() === current.word) {
      addXP(10)
      setScore(s => s + 1)
    }
    setInput('')
    setIndex(i => (i + 1) % WORDS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-teal-500/20 to-cyan-500/20 border-2 border-teal-500/30">
      <h3 className="text-xl font-bold text-white mb-4">🔤 Переставь буквы</h3>
      <p className="text-purple-300 mb-2">Составь слово из букв:</p>
      <p className="text-4xl text-teal-300 font-bold mb-4 tracking-widest">{current.scrambled.split('').join(' ')}</p>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && check()}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-xl mb-4"
        placeholder="Слово..."
      />
      <button onClick={check} className="w-full py-3 bg-teal-500 text-white rounded-xl font-bold">
        Проверить
      </button>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
