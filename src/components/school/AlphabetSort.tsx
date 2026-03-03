'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { ArrowUpAz } from 'lucide-react'

const ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.split('')

export default function AlphabetSort() {
  const { addXP } = useSchool()
  const [letters, setLetters] = useState<string[]>([])
  const [selected, setSelected] = useState<string[]>([])
  const [score, setScore] = useState(0)

  const newRound = () => {
    const shuffled = [...ALPHABET].sort(() => Math.random() - 0.5).slice(0, 5)
    setLetters(shuffled)
    setSelected([])
  }

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    newRound()
  }, [])

  const select = (letter: string) => {
    if (selected.includes(letter)) {
      setSelected(selected.filter(l => l !== letter))
    } else {
      setSelected([...selected, letter])
    }
  }

  const check = () => {
    const sorted = [...letters].sort((a, b) => ALPHABET.indexOf(a) - ALPHABET.indexOf(b))
    if (JSON.stringify(selected) === JSON.stringify(sorted)) {
      addXP(15)
      setScore(s => s + 1)
    }
    setTimeout(newRound, 1000)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-teal-500/20 to-cyan-500/20 border-2 border-teal-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <ArrowUpAz className="w-5 h-5" /> По алфавиту
      </h3>
      <p className="text-teal-300 mb-4">Выбери буквы по порядку алфавита:</p>
      <div className="flex flex-wrap gap-2 mb-4">
        {letters.map(l => (
          <button
            key={l}
            onClick={() => select(l)}
            className={`w-12 h-12 rounded-xl text-xl font-bold transition-all ${
              selected.includes(l)
                ? 'bg-teal-500 text-white scale-110'
                : 'bg-white/10 text-white hover:bg-white/20'
            }`}
          >
            {l}
          </button>
        ))}
      </div>
      <div className="p-3 bg-white/5 rounded-xl min-h-[50px] text-white">
        {selected.length > 0 ? selected.join(' → ') : 'Нажми по порядку...'}
      </div>
      <button onClick={check} className="w-full py-3 mt-4 bg-teal-500 text-white rounded-xl font-bold">
        Проверить
      </button>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
