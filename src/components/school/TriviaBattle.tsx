'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Swords, RotateCcw } from 'lucide-react'

const QUESTIONS = [
  { q: 'Столица Франции?', options: ['Лондон', 'Париж', 'Берлин', 'Рим'], correct: 1 },
  { q: 'Самая длинная река?', options: ['Нил', 'Амазонка', 'Миссисипи', 'Волга'], correct: 1 },
  { q: 'Сколько планет в Солнечной системе?', options: ['7', '8', '9', '10'], correct: 1 },
  { q: 'Самый большой океан?', options: ['Атлантический', 'Индийский', 'Тихий', 'Северный'], correct: 2 },
  { q: 'Кто написал "Войну и мир"?', options: ['Пушкин', 'Гоголь', 'Толстой', 'Достоевский'], correct: 2 },
]

export default function TriviaBattle() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [playerHP, setPlayerHP] = useState(100)
  const [enemyHP, setEnemyHP] = useState(100)
  const [finished, setFinished] = useState(false)

  const q = QUESTIONS[index]

  const answer = (idx: number) => {
    if (idx === q.correct) {
      addXP(15)
      setScore(s => s + 1)
      setEnemyHP(h => Math.max(0, h - 25))
    } else {
      setPlayerHP(h => Math.max(0, h - 25))
    }
    if (index < QUESTIONS.length - 1 && playerHP > 0 && enemyHP > 0) {
      setIndex(i => i + 1)
    } else {
      setFinished(true)
    }
  }

  const restart = () => {
    setIndex(0)
    setScore(0)
    setPlayerHP(100)
    setEnemyHP(100)
    setFinished(false)
  }

  if (finished) {
    const won = enemyHP <= 0
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-purple-500/20 border-2 border-indigo-500/30 text-center">
        <div className="text-6xl mb-4">{won ? '🏆' : '💀'}</div>
        <h3 className="text-2xl font-bold text-white mb-2">{won ? 'Победа!' : 'Поражение'}</h3>
        <p className="text-purple-300 mb-4">Правильных ответов: {score}</p>
        <button onClick={restart} className="px-6 py-3 bg-indigo-500 text-white rounded-xl font-bold">
          <RotateCcw className="w-5 h-5 inline mr-2" /> Реванш
        </button>
      </div>
    )
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-purple-500/20 border-2 border-indigo-500/30">
      <div className="flex justify-between mb-4">
        <div>
          <span className="text-white">❤️ Ты</span>
          <div className="w-24 h-3 bg-white/20 rounded-full">
            <div className="h-full bg-green-500 rounded-full transition-all" style={{ width: `${playerHP}%` }} />
          </div>
        </div>
        <Swords className="text-indigo-400 w-6 h-6" />
        <div className="text-right">
          <span className="text-white">🐉 Враг</span>
          <div className="w-24 h-3 bg-white/20 rounded-full">
            <div className="h-full bg-red-500 rounded-full transition-all" style={{ width: `${enemyHP}%` }} />
          </div>
        </div>
      </div>
      <p className="text-lg text-white mb-4">{q.q}</p>
      <div className="grid grid-cols-2 gap-2">
        {q.options.map((opt, i) => (
          <button key={i} onClick={() => answer(i)} className="p-3 bg-white/10 hover:bg-white/20 rounded-xl text-white transition-colors">
            {opt}
          </button>
        ))}
      </div>
    </div>
  )
}
