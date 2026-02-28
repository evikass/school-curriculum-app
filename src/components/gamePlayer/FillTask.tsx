'use client'

import { GameTask } from '@/data/types'
import { GameResult } from './types'

interface FillTaskProps {
  task: GameTask
  result: GameResult
  filledAnswer: string
  onFillChange: (answer: string) => void
  onCheck: () => void
}

export function FillTask({ task, result, filledAnswer, onFillChange, onCheck }: FillTaskProps) {
  return (
    <div className="space-y-4">
      <input
        type="text"
        value={filledAnswer}
        onChange={(e) => onFillChange(e.target.value)}
        disabled={result !== 'none'}
        placeholder="Введи букву или число..."
        className="w-full p-4 bg-slate-700/50 border-2 border-slate-600 rounded-xl text-white text-xl text-center placeholder-slate-500 focus:outline-none focus:border-purple-500 disabled:opacity-50"
      />
      {result === 'none' && (
        <button
          onClick={onCheck}
          disabled={!filledAnswer}
          className="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-500 hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed rounded-xl text-white font-medium transition-opacity"
        >
          Проверить ответ
        </button>
      )}
      {result !== 'none' && (
        <div className={`p-4 rounded-xl ${
          result === 'correct'
            ? 'bg-green-500/20 border border-green-500/30'
            : 'bg-red-500/20 border border-red-500/30'
        }`}>
          <p className={result === 'correct' ? 'text-green-300' : 'text-red-300'}>
            Правильный ответ: {task.correctAnswer}
          </p>
        </div>
      )}
    </div>
  )
}
