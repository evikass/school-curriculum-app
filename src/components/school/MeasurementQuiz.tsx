'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Ruler } from 'lucide-react'

const QUESTIONS = [
  { q: 'Сколько сантиметров в метре?', answer: 100 },
  { q: 'Сколько граммов в килограмме?', answer: 1000 },
  { q: 'Сколько метров в километре?', answer: 1000 },
  { q: 'Сколько секунд в минуте?', answer: 60 },
  { q: 'Сколько миллиметров в сантиметре?', answer: 10 },
]

export default function MeasurementQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const q = QUESTIONS[index]

  const check = () => {
    const correct = parseInt(input) === q.answer
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(15)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % QUESTIONS.length)
      setInput('')
      setResult(null)
    }, 1500)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-teal-500/20 to-cyan-500/20 border-2 border-teal-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Ruler className="w-5 h-5" /> Измерения
      </h3>
      <p className="text-center text-xl text-white mb-4">{q.q}</p>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && check()}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-2xl mb-4"
        placeholder="Ответ"
      />
      {!result && (
        <button onClick={check} className="w-full py-3 bg-teal-500 text-white rounded-xl font-bold">
          Проверить
        </button>
      )}
      {result && (
        <div className={`p-4 rounded-xl text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Верно!' : `❌ Ответ: ${q.answer}`}
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
