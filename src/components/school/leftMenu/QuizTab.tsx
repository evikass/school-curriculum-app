'use client'

import { Trophy, Sparkles, X, Brain, Star } from 'lucide-react'

interface QuizQuestion {
  id: number
  question: string
  options: string[]
  correct: number
  subject: string
  difficulty: number
}

interface QuizTabProps {
  quizAnswered: boolean
  quizComplete: boolean
  quizSelectedAnswer: number | null
  todayQuestion: QuizQuestion
  onAnswer: (index: number) => void
}

export default function QuizTab({
  quizAnswered,
  quizComplete,
  quizSelectedAnswer,
  todayQuestion,
  onAnswer
}: QuizTabProps) {
  if (quizAnswered) {
    return (
      <div className="p-4">
        <div className="text-center py-8">
          <Trophy className="w-12 h-12 text-yellow-400 mx-auto mb-3" />
          <h4 className="text-lg font-bold text-white mb-2">Викторина пройдена!</h4>
          <p className="text-teal-300 text-sm">Заходи завтра за новым вопросом</p>
        </div>
      </div>
    )
  }

  if (quizComplete) {
    const isCorrect = quizSelectedAnswer === todayQuestion.correct
    return (
      <div className="p-4">
        <div className={`p-4 rounded-xl text-center ${isCorrect ? 'bg-green-500/20 border border-green-400/50' : 'bg-red-500/20 border border-red-500/50'}`}>
          {isCorrect ? (
            <>
              <Sparkles className="w-8 h-8 text-green-400 mx-auto mb-2" />
              <p className="text-green-300 font-bold">Правильно! +{todayQuestion.difficulty * 5} XP</p>
            </>
          ) : (
            <>
              <X className="w-8 h-8 text-red-400 mx-auto mb-2" />
              <p className="text-red-300">Неверно. Ответ: {todayQuestion.options[todayQuestion.correct]}</p>
            </>
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="p-4">
      <div className="flex items-center gap-2 mb-3">
        <Brain className="w-5 h-5 text-violet-400" />
        <span className="text-sm text-white font-medium">{todayQuestion.subject}</span>
        <div className="ml-auto flex items-center gap-1">
          {[1, 2, 3].map(l => (
            <Star key={l} className={`w-3 h-3 ${l <= todayQuestion.difficulty ? 'text-yellow-400 fill-yellow-400' : 'text-white/20'}`} />
          ))}
        </div>
      </div>
      
      <div className="bg-white/5 rounded-xl p-3 mb-4">
        <p className="text-white text-center font-medium">{todayQuestion.question}</p>
      </div>
      
      <div className="grid grid-cols-2 gap-2">
        {todayQuestion.options.map((opt, idx) => (
          <button key={idx} onClick={() => onAnswer(idx)}
            className="p-3 bg-white/10 hover:bg-white/20 rounded-xl text-white text-sm font-medium transition-all">
            {String.fromCharCode(65 + idx)}. {opt}
          </button>
        ))}
      </div>
    </div>
  )
}
