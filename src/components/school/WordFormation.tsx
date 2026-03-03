'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Puzzle } from 'lucide-react'

const WORDS = [
  { word: 'ПОДЪЕЗД', parts: ['ПОД', 'Ъ', 'ЕЗД'], correct: 'приставка, корень' },
  { word: 'ШКОЛЬНИК', parts: ['ШКОЛ', 'Ь', 'НИК'], correct: 'корень, суффикс' },
  { word: 'ПРИЛЕТЕЛ', parts: ['ПРИ', 'ЛЕТ', 'ЕЛ'], correct: 'приставка, корень, суффикс' },
  { word: 'КНИЖКА', parts: ['КНИЖ', 'К', 'А'], correct: 'корень, суффикс, окончание' },
  { word: 'ПЕРЕПИСЧИК', parts: ['ПЕРЕ', 'ПИС', 'ЧИК'], correct: 'приставка, корень, суффикс' },
]

export default function WordFormation() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [selected, setSelected] = useState<string[]>([])
  const [score, setScore] = useState(0)

  const word = WORDS[index]

  const toggle = (part: string) => {
    if (selected.includes(part)) {
      setSelected(selected.filter(p => p !== part))
    } else {
      setSelected([...selected, part])
    }
  }

  const check = () => {
    if (selected.length > 0) {
      addXP(10)
      setScore(s => s + 1)
    }
    setSelected([])
    setIndex(i => (i + 1) % WORDS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-500/20 border-2 border-amber-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Puzzle className="w-5 h-5" /> Состав слова
      </h3>
      <p className="text-white mb-2">Разбери слово на части:</p>
      <p className="text-3xl text-amber-300 font-bold mb-6">{word.word}</p>
      <div className="flex flex-wrap gap-2 mb-4">
        {word.parts.map(part => (
          <button
            key={part}
            onClick={() => toggle(part)}
            className={`px-4 py-2 rounded-xl font-bold transition-all ${
              selected.includes(part)
                ? 'bg-amber-500 text-white'
                : 'bg-white/10 text-white hover:bg-white/20'
            }`}
          >
            {part}
          </button>
        ))}
      </div>
      <div className="p-3 bg-white/5 rounded-xl min-h-[40px] text-white mb-4">
        {selected.join(' + ') || 'Выбери части...'}
      </div>
      <button onClick={check} className="w-full py-3 bg-amber-500 text-white rounded-xl font-bold">
        Проверить
      </button>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
