'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { ArrowRightLeft } from 'lucide-react'

const PAIRS = [
  { word: 'Большой', synonyms: ['Огромный', 'Маленький', 'Великий'], correct: 0 },
  { word: 'Быстрый', synonyms: ['Тихий', 'Скорый', 'Медленный'], correct: 1 },
  { word: 'Весёлый', synonyms: ['Радостный', 'Грустный', 'Сердитый'], correct: 0 },
  { word: 'Трудный', synonyms: ['Лёгкий', 'Сложный', 'Простой'], correct: 1 },
  { word: 'Красивый', synonyms: ['Уродливый', 'Прекрасный', 'Странный'], correct: 1 },
]

export default function SynonymAntonym() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const pair = PAIRS[index]

  const answer = (idx: number) => {
    if (idx === pair.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % PAIRS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-violet-500/20 border-2 border-purple-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <ArrowRightLeft className="w-5 h-5" /> Синонимы
      </h3>
      <p className="text-center text-white mb-2">Синоним к слову:</p>
      <p className="text-center text-3xl font-bold text-purple-300 mb-6">{pair.word}</p>
      <div className="space-y-2">
        {pair.synonyms.map((syn, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
            className="w-full p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {syn}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
