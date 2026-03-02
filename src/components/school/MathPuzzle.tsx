'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Calculator } from 'lucide-react'

const PUZZLES = [
  { puzzle: '?? + ?? = ??\nВсе числа одинаковые', answer: 0, hint: '0 + 0 = 0' },
  { puzzle: 'Два отца и два сына поймали 3 рыб. Как?', answer: 3, hint: 'Дед, отец, внук' },
  { puzzle: 'Сколько сторон у треугольника?', answer: 3, hint: 'ТРИ-угольник' },
  { puzzle: 'Что тяжелее: 1 кг ваты или 1 кг железа?', answer: 0, hint: 'Одинаково!' },
  { puzzle: 'Ты да я, да мы с тобой. Сколько всего?', answer: 2, hint: 'Двое' },
]

export default function MathPuzzle() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [showHint, setShowHint] = useState(false)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const puzzle = PUZZLES[index]

  const check = () => {
    const correct = parseInt(input) === puzzle.answer
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(20)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % PUZZLES.length)
      setInput('')
      setShowHint(false)
      setResult(null)
    }, 2000)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-violet-500/20 border-2 border-indigo-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Calculator className="w-5 h-5" /> Математические загадки
      </h3>
      <div className="p-4 bg-white/5 rounded-xl mb-4 whitespace-pre-line text-white">
        {puzzle.puzzle}
      </div>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-xl mb-4"
        placeholder="Ответ..."
      />
      {!result && (
        <div className="flex gap-2">
          <button onClick={check} className="flex-1 py-3 bg-indigo-500 text-white rounded-xl font-bold">
            Проверить
          </button>
          <button onClick={() => setShowHint(true)} className="px-4 py-3 bg-white/10 text-white rounded-xl">
            💡
          </button>
        </div>
      )}
      {showHint && !result && (
        <div className="p-4 bg-yellow-500/20 rounded-xl text-yellow-300 mt-2">
          Подсказка: {puzzle.hint}
        </div>
      )}
      {result && (
        <div className={`p-4 rounded-xl text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Правильно!' : `❌ Ответ: ${puzzle.answer}`}
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
