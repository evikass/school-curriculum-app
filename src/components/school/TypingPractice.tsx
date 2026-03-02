'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { RotateCcw, Check } from 'lucide-react'

const QUESTIONS = [
  { word: 'корова', correct: 'коровы' },
  { word: 'стол', correct: 'столы' },
  { word: 'дом', correct: 'дома' },
  { word: 'кот', correct: 'коты' },
  { word: 'сад', correct: 'сады' },
]

export default function TypingPractice() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [showResult, setShowResult] = useState(false)
  const [score, setScore] = useState(0)

  const q = QUESTIONS[index]
  const correct = input.toLowerCase().trim() === q.correct

  const check = () => {
    setShowResult(true)
    if (correct) {
      addXP(10)
      setScore(s => s + 1)
    }
  }

  const next = () => {
    setIndex(i => (i + 1) % QUESTIONS.length)
    setInput('')
    setShowResult(false)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-slate-500/20 to-gray-500/20 border-2 border-slate-500/30">
      <h3 className="text-xl font-bold text-white mb-4">⌨️ Практика печати</h3>
      <p className="text-purple-300 mb-2">Множественное число от: <span className="text-white font-bold">{q.word}</span></p>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        disabled={showResult}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-lg mb-4 focus:outline-none focus:border-slate-400"
        placeholder="Введите ответ..."
      />
      {!showResult ? (
        <button onClick={check} className="w-full py-3 bg-slate-500 text-white rounded-xl font-bold">
          Проверить
        </button>
      ) : (
        <div>
          <div className={`p-4 rounded-xl mb-4 ${correct ? 'bg-green-500/20 border border-green-400' : 'bg-red-500/20 border border-red-400'}`}>
            <p className="text-white">{correct ? '✅ Правильно!' : `❌ Правильно: ${q.correct}`}</p>
          </div>
          <button onClick={next} className="w-full py-3 bg-slate-500 text-white rounded-xl font-bold">
            Далее
          </button>
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
