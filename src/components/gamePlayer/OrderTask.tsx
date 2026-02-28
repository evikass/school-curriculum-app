'use client'

import { GameResult } from './types'

interface OrderTaskProps {
  items: string[]
  result: GameResult
  onMove: (index: number, direction: 'up' | 'down') => void
  onCheck: () => void
}

export function OrderTask({ items, result, onMove, onCheck }: OrderTaskProps) {
  return (
    <div className="space-y-4">
      <div className="space-y-2">
        {items.map((item, index) => (
          <div
            key={index}
            className="flex items-center gap-2 bg-slate-700/50 rounded-xl overflow-hidden"
          >
            <div className="flex flex-col">
              <button
                onClick={() => onMove(index, 'up')}
                disabled={result !== 'none' || index === 0}
                className="p-2 hover:bg-slate-600 disabled:opacity-30"
              >
                ▲
              </button>
              <button
                onClick={() => onMove(index, 'down')}
                disabled={result !== 'none' || index === items.length - 1}
                className="p-2 hover:bg-slate-600 disabled:opacity-30"
              >
                ▼
              </button>
            </div>
            <span className="flex-1 p-4 text-white text-lg">{item}</span>
            <span className="px-4 py-2 bg-slate-600 text-slate-300 rounded-lg m-2">
              {index + 1}
            </span>
          </div>
        ))}
      </div>
      {result === 'none' && (
        <button
          onClick={onCheck}
          className="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-500 hover:opacity-90 rounded-xl text-white font-medium transition-opacity"
        >
          Проверить порядок
        </button>
      )}
    </div>
  )
}
