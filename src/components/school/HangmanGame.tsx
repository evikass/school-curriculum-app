'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Gamepad2, RotateCcw } from 'lucide-react'

const WORDS = ['КОШКА', 'СОБАКА', 'МАШИНА', 'УРОК', 'ШКОЛА', 'КНИГА']

export default function HangmanGame() {
  const { addXP } = useSchool()
  const [word, setWord] = useState(WORDS[0])
  const [guessed, setGuessed] = useState<Set<string>>(new Set())
  const [wrong, setWrong] = useState(0)
  const [score, setScore] = useState(0)

  const alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.split('')
  const won = word.split('').every(l => guessed.has(l))
  const lost = wrong >= 6

  const guess = (letter: string) => {
    if (guessed.has(letter) || won || lost) return
    const newGuessed = new Set(guessed)
    newGuessed.add(letter)
    setGuessed(newGuessed)
    if (!word.includes(letter)) {
      setWrong(w => w + 1)
    }
    if (word.split('').every(l => newGuessed.has(l))) {
      addXP(20)
      setScore(s => s + 1)
    }
  }

  const restart = () => {
    setWord(WORDS[Math.floor(Math.random() * WORDS.length)])
    setGuessed(new Set())
    setWrong(0)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-slate-500/20 to-gray-500/20 border-2 border-slate-500/30">
      <h3 className="text-xl font-bold text-white mb-4">🎮 Виселица</h3>
      <div className="text-center text-4xl mb-4 font-mono">
        {word.split('').map((l, i) => (
          <span key={i} className="mx-1">
            {guessed.has(l) || lost ? l : '_'}
          </span>
        ))}
      </div>
      <div className="text-center text-red-400 mb-4">
        Ошибок: {wrong}/6 {'❤️'.repeat(6 - wrong)}
      </div>
      {(won || lost) && (
        <div className={`p-4 rounded-xl mb-4 text-center font-bold ${won ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {won ? '🎉 Угадал!' : `💀 Слово: ${word}`}
          <button onClick={restart} className="ml-4 px-4 py-1 bg-slate-500 rounded-lg text-white">
            Заново
          </button>
        </div>
      )}
      <div className="flex flex-wrap gap-1 justify-center">
        {alphabet.map(l => (
          <button
            key={l}
            onClick={() => guess(l)}
            disabled={guessed.has(l) || won || lost}
            className={`w-8 h-8 rounded font-bold text-sm transition-all ${
              guessed.has(l)
                ? word.includes(l) ? 'bg-green-500 text-white' : 'bg-red-500/50 text-white/50'
                : 'bg-white/10 hover:bg-white/20 text-white'
            }`}
          >
            {l}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Отгадано: {score}</p>
    </div>
  )
}
