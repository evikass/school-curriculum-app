'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Brain, RotateCcw } from 'lucide-react'

const PAIRS = [
  { id: 1, emoji: '🍎', name: 'Яблоко' },
  { id: 2, emoji: '🍊', name: 'Апельсин' },
  { id: 3, emoji: '🍋', name: 'Лимон' },
  { id: 4, emoji: '🍇', name: 'Виноград' },
]

export default function MemoryGame() {
  const { addXP } = useSchool()
  const [cards, setCards] = useState<{ id: number; emoji: string; name: string; flipped: boolean; matched: boolean }[]>([])
  const [flipped, setFlipped] = useState<number[]>([])
  const [moves, setMoves] = useState(0)

  const initGame = () => {
    const deck = [...PAIRS, ...PAIRS]
      .sort(() => Math.random() - 0.5)
      .map((card, i) => ({ ...card, id: i, flipped: false, matched: false }))
    setCards(deck)
    setFlipped([])
    setMoves(0)
  }

  useEffect(() => {
    initGame()
  }, [])

  const flip = (index: number) => {
    if (flipped.length === 2 || cards[index].flipped || cards[index].matched) return

    const newCards = [...cards]
    newCards[index].flipped = true
    setCards(newCards)
    setFlipped([...flipped, index])

    if (flipped.length === 1) {
      setMoves(m => m + 1)
      const firstIndex = flipped[0]
      if (cards[firstIndex].emoji === cards[index].emoji) {
        setTimeout(() => {
          const matchedCards = [...cards]
          matchedCards[firstIndex].matched = true
          matchedCards[index].matched = true
          setCards(matchedCards)
          setFlipped([])
          if (matchedCards.every(c => c.matched)) {
            addXP(25)
          }
        }, 500)
      } else {
        setTimeout(() => {
          const resetCards = [...cards]
          resetCards[firstIndex].flipped = false
          resetCards[index].flipped = false
          setCards(resetCards)
          setFlipped([])
        }, 1000)
      }
    }
  }

  const allMatched = cards.length > 0 && cards.every(c => c.matched)

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-indigo-500/20 border-2 border-purple-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Brain className="w-5 h-5" /> Память
      </h3>
      <p className="text-purple-300 mb-4">Ходы: {moves}</p>
      {allMatched && (
        <div className="p-4 bg-green-500/20 rounded-xl mb-4 text-center">
          <p className="text-green-400 font-bold">🎉 Победа за {moves} ходов!</p>
        </div>
      )}
      <div className="grid grid-cols-4 gap-2 mb-4">
        {cards.map((card, i) => (
          <button
            key={card.id}
            onClick={() => flip(i)}
            className={`h-16 rounded-xl text-2xl font-bold transition-all ${
              card.flipped || card.matched
                ? 'bg-purple-500 text-white'
                : 'bg-white/10 hover:bg-white/20'
            }`}
          >
            {card.flipped || card.matched ? card.emoji : '?'}
          </button>
        ))}
      </div>
      <button onClick={initGame} className="w-full py-3 bg-purple-500 text-white rounded-xl font-bold">
        <RotateCcw className="w-5 h-5 inline mr-2" /> Заново
      </button>
    </div>
  )
}
