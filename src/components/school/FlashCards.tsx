'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { RotateCcw, Check, X } from 'lucide-react'

const CARDS = [
  { q: 'Сколько дней в неделе?', a: '7' },
  { q: 'Сколько месяцев в году?', a: '12' },
  { q: 'Сколько часов в сутках?', a: '24' },
  { q: 'Сколько минут в часе?', a: '60' },
  { q: 'Столица России?', a: 'Москва' },
]

export default function FlashCards() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [show, setShow] = useState(false)
  const [score, setScore] = useState(0)

  const card = CARDS[index]

  const handleAnswer = (correct: boolean) => {
    if (correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setShow(false)
    setIndex(i => (i + 1) % CARDS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-teal-500/20 to-cyan-500/20 border-2 border-teal-500/30">
      <h3 className="text-xl font-bold text-white mb-4">🎴 Карточки</h3>
      <div className="text-center">
        <div className="mb-4 text-purple-300">Счёт: {score}/{CARDS.length}</div>
        <div className="p-8 rounded-2xl bg-white/10 border border-white/20 min-h-[120px] flex items-center justify-center">
          <p className="text-xl text-white">{show ? card.a : card.q}</p>
        </div>
        <div className="flex gap-3 mt-4 justify-center">
          {!show ? (
            <button onClick={() => setShow(true)} className="px-6 py-3 bg-teal-500 text-white rounded-xl font-bold">
              Показать ответ
            </button>
          ) : (
            <>
              <button onClick={() => handleAnswer(true)} className="px-6 py-3 bg-green-500 text-white rounded-xl font-bold">
                <Check className="w-5 h-5 inline" /> Знаю
              </button>
              <button onClick={() => handleAnswer(false)} className="px-6 py-3 bg-red-500 text-white rounded-xl font-bold">
                <X className="w-5 h-5 inline" /> Не знаю
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  )
}
