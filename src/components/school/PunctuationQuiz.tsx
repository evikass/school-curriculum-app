'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { PenTool } from 'lucide-react'

const SENTENCES = [
  { text: 'Мама мыла раму___', options: ['.', '!', '?', ','], correct: 0 },
  { text: 'Кто там___', options: ['.', '!', '?', ','], correct: 2 },
  { text: 'Какой красивый день___', options: ['.', '!', '?', ','], correct: 1 },
  { text: 'В лесу, на поляне___ растут цветы.', options: ['.', '!', '?', ','], correct: 3 },
  { text: 'Привет___ Как дела?', options: ['.', '!', '?', ','], correct: 0 },
]

export default function PunctuationQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const sentence = SENTENCES[index]

  const answer = (idx: number) => {
    if (idx === sentence.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % SENTENCES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-teal-500/20 border-2 border-cyan-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <PenTool className="w-5 h-5" /> Пунктуация
      </h3>
      <p className="text-lg text-white mb-2">Какой знак нужен?</p>
      <p className="text-xl text-cyan-300 font-bold mb-6">{sentence.text}</p>
      <div className="grid grid-cols-4 gap-3">
        {sentence.options.map((opt, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white text-2xl font-bold transition-colors"
          >
            {opt}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
