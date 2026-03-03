'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Link2 } from 'lucide-react'

const CHAINS = [
  { start: 'КОТ', chain: ['КОТ', 'ТОК', 'КОК', 'КОД'] },
  { start: 'МИР', chain: ['МИР', 'РИМ', 'РАК', 'МАК'] },
]

export default function WordChain() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [current, setCurrent] = useState('')
  const [chain, setChain] = useState<string[]>([])
  const [score, setScore] = useState(0)

  const game = CHAINS[index]

  const startGame = () => {
    setCurrent(game.start)
    setChain([game.start])
  }

  const submit = () => {
    const last = chain[chain.length - 1]
    if (current[0] === last[last.length - 1] && current !== last) {
      addXP(10)
      setScore(s => s + 1)
      setChain([...chain, current])
    }
    setCurrent('')
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-green-500/20 to-emerald-500/20 border-2 border-green-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Link2 className="w-5 h-5" /> Цепочка слов
      </h3>
      {chain.length === 0 ? (
        <button onClick={startGame} className="w-full py-4 bg-green-500 text-white rounded-xl font-bold">
          Начать
        </button>
      ) : (
        <>
          <p className="text-green-300 mb-2">Цепочка: {chain.join(' → ')}</p>
          <p className="text-white mb-2">Слово должно начинаться на: <strong>{chain[chain.length - 1][chain[chain.length - 1].length - 1]}</strong></p>
          <input
            type="text"
            value={current}
            onChange={e => setCurrent(e.target.value.toUpperCase())}
            onKeyDown={e => e.key === 'Enter' && submit()}
            className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white text-center mb-4"
            placeholder="Слово..."
          />
          <button onClick={submit} className="w-full py-3 bg-green-500 text-white rounded-xl font-bold">
            Добавить
          </button>
        </>
      )}
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
