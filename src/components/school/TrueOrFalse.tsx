'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { CheckCircle, XCircle } from 'lucide-react'

const QUESTIONS = [
  { q: 'Земля вращается вокруг Солнца', correct: true },
  { q: 'В году 13 месяцев', correct: false },
  { q: 'Вода кипит при 100°C', correct: true },
  { q: 'Луна - это звезда', correct: false },
  { q: 'Москва - столица России', correct: true },
]

export default function TrueOrFalse() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const q = QUESTIONS[index]

  const answer = (guess: boolean) => {
    const correct = guess === q.correct
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % QUESTIONS.length)
      setResult(null)
    }, 1000)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-rose-500/20 to-pink-500/20 border-2 border-rose-500/30">
      <h3 className="text-xl font-bold text-white mb-4">✅ Правда или Ложь</h3>
      <p className="text-lg text-white mb-6 text-center">{q.q}</p>
      {result && (
        <div className={`p-4 rounded-xl mb-4 text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Верно!' : '❌ Неверно!'}
        </div>
      )}
      <div className="flex gap-4">
        <button
          onClick={() => answer(true)}
          disabled={!!result}
          className="flex-1 py-4 bg-green-500 hover:bg-green-600 text-white rounded-xl font-bold flex items-center justify-center gap-2 disabled:opacity-50"
        >
          <CheckCircle /> Правда
        </button>
        <button
          onClick={() => answer(false)}
          disabled={!!result}
          className="flex-1 py-4 bg-red-500 hover:bg-red-600 text-white rounded-xl font-bold flex items-center justify-center gap-2 disabled:opacity-50"
        >
          <XCircle /> Ложь
        </button>
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
