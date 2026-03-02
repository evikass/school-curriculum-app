'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'

const CROSSWORD = {
  grid: [
    ['К', 'О', 'Т', '', ''],
    ['', 'П', 'Р', 'О', 'Т'],
    ['', 'Н', '', 'Л', ''],
    ['', 'И', '', 'Ь', ''],
    ['', 'К', '', '', ''],
  ],
  words: ['КОТ', 'ПРОТЬ', 'ПРОЛЬ']
}

export default function CrosswordGame() {
  const { addXP } = useSchool()
  const [answers, setAnswers] = useState<string[][]>(() => 
    CROSSWORD.grid.map(row => row.map(() => ''))
  )
  const [score, setScore] = useState(0)

  const check = () => {
    let correct = true
    for (let i = 0; i < CROSSWORD.grid.length; i++) {
      for (let j = 0; j < CROSSWORD.grid[i].length; j++) {
        if (CROSSWORD.grid[i][j] && answers[i][j].toUpperCase() !== CROSSWORD.grid[i][j]) {
          correct = false
        }
      }
    }
    if (correct) {
      addXP(25)
      setScore(s => s + 1)
    }
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-blue-500/20 to-cyan-500/20 border-2 border-blue-500/30">
      <h3 className="text-xl font-bold text-white mb-4">📰 Кроссворд</h3>
      <div className="flex flex-col gap-1 mb-4">
        {CROSSWORD.grid.map((row, i) => (
          <div key={i} className="flex gap-1">
            {row.map((cell, j) => cell ? (
              <input
                key={j}
                maxLength={1}
                value={answers[i][j]}
                onChange={e => {
                  const newAnswers = [...answers]
                  newAnswers[i][j] = e.target.value
                  setAnswers(newAnswers)
                }}
                className="w-10 h-10 text-center text-xl font-bold bg-white text-black rounded"
              />
            ) : (
              <div key={j} className="w-10 h-10 bg-white/5 rounded" />
            ))}
          </div>
        ))}
      </div>
      <button onClick={check} className="w-full py-3 bg-blue-500 text-white rounded-xl font-bold">
        Проверить
      </button>
      <p className="text-center text-purple-300 mt-4">Решено: {score}</p>
    </div>
  )
}
