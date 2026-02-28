'use client'

import { CheckCircle, XCircle } from 'lucide-react'
import { GameResult } from './types'

interface ResultFeedbackProps {
  result: GameResult
  correctAnswer: string | string[]
}

export function ResultFeedback({ result, correctAnswer }: ResultFeedbackProps) {
  if (result === 'none') return null

  const answerText = Array.isArray(correctAnswer) ? correctAnswer.join(', ') : correctAnswer

  return (
    <div className={`mt-6 p-4 rounded-xl flex items-center gap-3 ${
      result === 'correct'
        ? 'bg-green-500/20 border border-green-500/30'
        : 'bg-red-500/20 border border-red-500/30'
    }`}>
      {result === 'correct' ? (
        <>
          <CheckCircle className="w-8 h-8 text-green-400" />
          <div>
            <p className="text-green-300 font-semibold">Правильно!</p>
            <p className="text-green-200 text-sm">Отличная работа!</p>
          </div>
        </>
      ) : (
        <>
          <XCircle className="w-8 h-8 text-red-400" />
          <div>
            <p className="text-red-300 font-semibold">Неправильно</p>
            <p className="text-red-200 text-sm">Правильный ответ: {answerText}</p>
          </div>
        </>
      )}
    </div>
  )
}
