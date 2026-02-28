'use client'

import { useMemo } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { X, CheckCircle, XCircle, Trophy, Star, Sparkles, RotateCcw, ChevronRight, HelpCircle } from 'lucide-react'
import { generateQuestions, useQuizState, getScoreMessage, QuestionItem } from './lessonQuiz'

interface LessonQuizProps {
  lessonTitle: string
  lessonDescription: string
  isOpen: boolean
  onClose: () => void
  onComplete: (score: number) => void
}

export default function LessonQuiz({ lessonTitle, lessonDescription, isOpen, onClose, onComplete }: LessonQuizProps) {
  const questions = useMemo(() => generateQuestions(lessonTitle, lessonDescription), [lessonTitle, lessonDescription])
  const { state, handleAnswer, nextQuestion, resetQuiz } = useQuizState(questions)

  if (!isOpen) return null

  const question = questions[state.currentQuestion]
  const scoreInfo = getScoreMessage(state.score, questions.length)

  return (
    <AnimatePresence>
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
        className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm"
        onClick={(e) => e.target === e.currentTarget && onClose()}>
        <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
          className="bg-gradient-to-br from-blue-900 to-indigo-900 rounded-3xl max-w-lg w-full max-h-[85vh] overflow-hidden shadow-2xl border-2 border-white/10 flex flex-col">

        {/* Header */}
        <div className="p-4 border-b border-white/10">
          <div className="flex justify-between items-center">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-blue-500/30 rounded-xl"><HelpCircle className="w-5 h-5 text-blue-300" /></div>
              <div>
                <h3 className="text-lg font-bold text-white">Тест: {lessonTitle}</h3>
                {!state.isComplete && <p className="text-blue-300 text-sm">Вопрос {state.currentQuestion + 1} из {questions.length}</p>}
              </div>
            </div>
            <button onClick={onClose} className="text-white/50 hover:text-white p-2"><X className="w-5 h-5" /></button>
          </div>
          {!state.isComplete && (
            <div className="mt-3 h-2 bg-white/10 rounded-full overflow-hidden">
              <motion.div className="h-full bg-gradient-to-r from-blue-500 to-cyan-500" initial={{ width: 0 }}
                animate={{ width: `${((state.currentQuestion + 1) / questions.length) * 100}%` }} />
            </div>
          )}
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-6">
          {!state.isComplete ? (
            <QuestionContent question={question} selectedAnswer={state.selectedAnswer} showResult={state.showResult} onAnswer={handleAnswer} />
          ) : (
            <ResultsScreen score={state.score} total={questions.length} wrongAnswers={state.wrongAnswers} questions={questions}
              scoreInfo={scoreInfo} onReset={resetQuiz} onClose={onClose} />
          )}
        </div>

        {/* Footer */}
        {!state.isComplete && state.showResult && (
          <div className="p-4 border-t border-white/10">
            <button onClick={nextQuestion}
              className="w-full py-3 bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600 text-white rounded-xl font-medium flex items-center justify-center gap-2">
              {state.currentQuestion < questions.length - 1 ? <>Следующий вопрос <ChevronRight className="w-5 h-5" /></> : <>Показать результат <Trophy className="w-5 h-5" /></>}
            </button>
          </div>
        )}
        </motion.div>
      </motion.div>
    </AnimatePresence>
  )
}

function QuestionContent({ question, selectedAnswer, showResult, onAnswer }: { question: QuestionItem; selectedAnswer: number | null; showResult: boolean; onAnswer: (idx: number) => void }) {
  return (
    <div className="space-y-6">
      <div className="bg-white/5 rounded-2xl p-4 border border-white/10">
        <p className="text-white text-lg font-medium">{question.question}</p>
      </div>
      <div className="space-y-3">
        {question.options.map((option, idx) => (
          <motion.button key={idx} whileHover={{ scale: showResult ? 1 : 1.02 }} whileTap={{ scale: showResult ? 1 : 0.98 }}
            onClick={() => onAnswer(idx)} disabled={showResult}
            className={`w-full p-4 rounded-xl text-left font-medium transition-all
              ${showResult ? idx === question.correct ? 'bg-green-500/30 border-2 border-green-500 text-white'
                : idx === selectedAnswer ? 'bg-red-500/30 border-2 border-red-500 text-white' : 'bg-white/5 text-white/50'
                : 'bg-white/10 text-white hover:bg-white/20 border-2 border-transparent'}`}>
            <span className="flex items-center gap-3">
              <span className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold
                ${showResult ? idx === question.correct ? 'bg-green-500 text-white' : idx === selectedAnswer ? 'bg-red-500 text-white' : 'bg-white/10 text-white/50' : 'bg-white/10 text-white'}`}>
                {showResult ? idx === question.correct ? <CheckCircle className="w-5 h-5" /> : idx === selectedAnswer ? <XCircle className="w-5 h-5" /> : String.fromCharCode(65 + idx) : String.fromCharCode(65 + idx)}
              </span>
              {option}
            </span>
          </motion.button>
        ))}
      </div>
      {showResult && (
        <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4">
          <p className="text-blue-300 text-sm">💡 {question.hint}</p>
        </motion.div>
      )}
    </div>
  )
}

function ResultsScreen({ score, total, wrongAnswers, questions, scoreInfo, onReset, onClose }: { score: number; total: number; wrongAnswers: number[]; questions: QuestionItem[]; scoreInfo: { message: string; color: string }; onReset: () => void; onClose: () => void }) {
  return (
    <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="text-center py-8">
      <motion.div animate={{ rotate: [0, 360] }} transition={{ duration: 2, repeat: Infinity, ease: 'linear' }} className="inline-block mb-4">
        <Trophy className={`w-20 h-20 ${score === total ? 'text-yellow-400' : 'text-blue-400'}`} />
      </motion.div>
      <h4 className="text-2xl font-bold text-white mb-2">Результат: {score} из {total}</h4>
      <p className={`text-lg mb-6 ${scoreInfo.color}`}>{scoreInfo.message}</p>
      <div className="flex items-center justify-center gap-2 mb-6">
        {[...Array(total)].map((_, idx) => <Star key={idx} className={`w-8 h-8 ${idx < score ? 'text-yellow-400 fill-yellow-400' : 'text-white/20'}`} />)}
      </div>
      {wrongAnswers.length > 0 && (
        <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 mb-6 text-left">
          <p className="text-red-400 font-medium mb-2">Вопросы для повторения:</p>
          {wrongAnswers.map(idx => <p key={idx} className="text-red-300 text-sm">• {questions[idx].question}</p>)}
        </div>
      )}
      <div className="flex gap-3">
        <button onClick={onReset} className="flex-1 py-3 bg-white/10 hover:bg-white/20 text-white rounded-xl font-medium flex items-center justify-center gap-2">
          <RotateCcw className="w-5 h-5" />Ещё раз
        </button>
        <button onClick={onClose} className="flex-1 py-3 bg-gradient-to-r from-green-500 to-emerald-500 text-white rounded-xl font-medium flex items-center justify-center gap-2">
          <Sparkles className="w-5 h-5" />Готово!
        </button>
      </div>
    </motion.div>
  )
}
