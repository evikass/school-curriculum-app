'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { RefreshCw } from 'lucide-react'

const ANAGRAMS = [
  { word: 'КОТ', letters: 'ОТК' },
  { word: 'МАК', letters: 'КМА' },
  { word: 'СОН', letters: 'НСО' },
  { word: 'ЛЕС', letters: 'СЛЕ' },
  { word: 'МИР', letters: 'РИМ' },
]

export default function AnagramGame() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [score, setScore] = useState(0)
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)

  const anagram = ANAGRAMS[index]

  const check = () => {
    const correct = input.toUpperCase().trim() === anagram.word
    setResult(correct ? 'correct' : 'wrong')
    if (correct) {
      addXP(15)
      setScore(s => s + 1)
    }
    setTimeout(() => {
      setIndex(i => (i + 1) % ANAGRAMS.length)
      setInput('')
      setResult(null)
    }, 1500)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-fuchsia-500/20 to-pink-500/20 border-2 border-fuchsia-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <RefreshCw className="w-5 h-5" /> Анаграммы
      </h3>
      <p className="text-purple-300 mb-2">Составь слово из букв:</p>
      <div className="flex justify-center gap-2 mb-4">
        {anagram.letters.split('').map((l, i) => (
          <span key={i} className="w-12 h-12 bg-fuchsia-500/30 rounded-xl flex items-center justify-center text-2xl font-bold text-white">
            {l}
          </span>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        maxLength={anagram.word.length}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center text-xl mb-4"
        placeholder="Слово..."
      />
      {!result && (
        <button onClick={check} className="w-full py-3 bg-fuchsia-500 text-white rounded-xl font-bold">
          Проверить
        </button>
      )}
      {result && (
        <div className={`p-4 rounded-xl text-center font-bold ${result === 'correct' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
          {result === 'correct' ? '✅ Верно!' : `❌ Ответ: ${anagram.word}`}
        </div>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
