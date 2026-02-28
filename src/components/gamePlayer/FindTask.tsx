'use client'

import { GameTask } from '@/data/types'
import { GameResult } from './types'

interface FindTaskProps {
  task: GameTask
  result: GameResult
  selectedItems: string[]
  onToggleItem: (item: string) => void
  onCheck: () => void
}

export function FindTask({ task, result, selectedItems, onToggleItem, onCheck }: FindTaskProps) {
  const correctAnswers = task.correctAnswer as string[]

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap gap-3">
        {task.options?.map((option, index) => {
          const isSelected = selectedItems.includes(option)
          const isCorrect = correctAnswers.includes(option)
          return (
            <button
              key={index}
              onClick={() => result === 'none' && onToggleItem(option)}
              disabled={result !== 'none'}
              className={`px-5 py-3 rounded-xl text-lg font-medium transition-all ${
                result !== 'none'
                  ? isCorrect
                    ? 'bg-green-500/30 border-2 border-green-500 text-green-300'
                    : isSelected && !isCorrect
                    ? 'bg-red-500/30 border-2 border-red-500 text-red-300'
                    : 'bg-slate-700/50 border-2 border-slate-600 text-slate-400'
                  : isSelected
                  ? 'bg-purple-500/30 border-2 border-purple-500 text-white'
                  : 'bg-slate-700/50 hover:bg-slate-600/50 border-2 border-slate-600 hover:border-purple-500 text-white'
              }`}
            >
              {option}
            </button>
          )
        })}
      </div>
      {result === 'none' && (
        <button
          onClick={onCheck}
          disabled={selectedItems.length === 0}
          className="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-500 hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed rounded-xl text-white font-medium transition-opacity"
        >
          Проверить ответ
        </button>
      )}
    </div>
  )
}
