'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Search } from 'lucide-react'

const PUZZLES = [
  { word: 'КОТ', grid: ['КОТКА', 'ПОЛЕТ', 'ТОЧКА', 'КНИГА', 'ОКНО'], positions: [[0,0], [0,1], [0,2]] },
  { word: 'МИР', grid: ['МИРРА', 'ИКРАН', 'РЫБАК', 'МОРЕ'], positions: [[0,0], [0,1], [0,2]] },
]

export default function WordSearch() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [found, setFound] = useState<Set<string>>(new Set())
  const [score, setScore] = useState(0)

  const puzzle = PUZZLES[index]
  const wordFound = puzzle.word.split('').every((_, i) => found.has(`${puzzle.positions[i][0]}-${puzzle.positions[i][1]}`))

  const toggle = (r: number, c: number) => {
    const key = `${r}-${c}`
    const newFound = new Set(found)
    if (newFound.has(key)) {
      newFound.delete(key)
    } else {
      newFound.add(key)
    }
    setFound(newFound)
  }

  const checkWord = () => {
    if (wordFound) {
      addXP(20)
      setScore(s => s + 1)
    }
    setFound(new Set())
    setIndex(i => (i + 1) % PUZZLES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-teal-500/20 border-2 border-cyan-500/30">
      <h3 className="text-xl font-bold text-white mb-2">🔍 Поиск слов</h3>
      <p className="text-cyan-300 mb-4">Найди слово: <span className="font-bold">{puzzle.word}</span></p>
      <div className="flex flex-col gap-1 mb-4">
        {puzzle.grid.map((row, r) => (
          <div key={r} className="flex gap-1">
            {row.split('').map((char, c) => (
              <button
                key={c}
                onClick={() => toggle(r, c)}
                className={`w-10 h-10 rounded-lg font-bold transition-all ${
                  found.has(`${r}-${c}`)
                    ? 'bg-cyan-500 text-white'
                    : 'bg-white/10 text-white hover:bg-white/20'
                }`}
              >
                {char}
              </button>
            ))}
          </div>
        ))}
      </div>
      <button onClick={checkWord} className="w-full py-3 bg-cyan-500 text-white rounded-xl font-bold">
        Проверить
      </button>
      <p className="text-center text-purple-300 mt-4">Найдено: {score}</p>
    </div>
  )
}
