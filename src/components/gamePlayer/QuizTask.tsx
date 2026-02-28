'use client'

import { GameTask } from '@/data/types'
import { GameResult } from './types'

interface QuizTaskProps {
  task: GameTask
  result: GameResult
  selectedAnswer: string | null
  onAnswer: (answer: string) => void
}

export function QuizTask({ task, result, selectedAnswer, onAnswer }: QuizTaskProps) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
      {task.options?.map((option, index) => (
        <button
          key={index}
          onClick={() => result === 'none' && onAnswer(option)}
          disabled={result !== 'none'}
          className={`p-4 rounded-xl text-lg font-medium transition-all ${
            result !== 'none' && option === task.correctAnswer
              ? 'bg-green-500/30 border-2 border-green-500 text-green-300'
              : result !== 'none' && selectedAnswer === option && option !== task.correctAnswer
              ? 'bg-red-500/30 border-2 border-red-500 text-red-300'
              : result === 'none'
              ? 'bg-slate-700/50 hover:bg-slate-600/50 border-2 border-slate-600 hover:border-purple-500 text-white'
              : 'bg-slate-700/50 border-2 border-slate-600 text-slate-400'
          }`}
        >
          <span className="flex items-center gap-3">
            <span className="w-8 h-8 rounded-full bg-slate-600 flex items-center justify-center text-sm">
              {String.fromCharCode(65 + index)}
            </span>
            {option}
          </span>
        </button>
      ))}
    </div>
  )
}
