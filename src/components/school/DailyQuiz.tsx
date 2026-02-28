'use client'

import { useState, useEffect, useMemo, useCallback } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { Brain, Sparkles, Trophy, X, Clock, Star, Zap } from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'
import { quizQuestions } from './dailyQuiz/questions'

export default function DailyQuiz() {
  const { addPoints, selectedClass } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [showResult, setShowResult] = useState(false)
  const [isComplete, setIsComplete] = useState(false)
  const [timeLeft, setTimeLeft] = useState(15)
  const [answeredToday, setAnsweredToday] = useState(() => {
    if (typeof window === 'undefined') return false
    return localStorage.getItem('lastQuizDate') === new Date().toDateString()
  })

  const todayQuestion = useMemo(() => {
    const today = new Date()
    const dayOfYear = Math.floor((today.getTime() - new Date(today.getFullYear(), 0, 0).getTime()) / 86400000)
    const grade = selectedClass || 1
    const maxDifficulty = grade <= 2 ? 1 : grade <= 4 ? 2 : 3
    const filtered = quizQuestions.filter(q => q.difficulty <= maxDifficulty)
    return filtered[dayOfYear % filtered.length]
  }, [selectedClass])

  const handleAnswer = useCallback((answerIndex: number) => {
    if (showResult) return
    setSelectedAnswer(answerIndex)
    setShowResult(true)
    if (answerIndex === todayQuestion.correct) {
      addPoints(todayQuestion.difficulty * 5)
    }
    setTimeout(() => {
      localStorage.setItem('lastQuizDate', new Date().toDateString())
      setAnsweredToday(true)
      setIsComplete(true)
    }, 2000)
  }, [showResult, todayQuestion, addPoints])

  useEffect(() => {
    if (isOpen && !showResult && !isComplete && timeLeft > 0) {
      const timer = setTimeout(() => setTimeLeft(t => t - 1), 1000)
      return () => clearTimeout(timer)
    } else if (timeLeft === 0 && !showResult) {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      handleAnswer(-1)
    }
  }, [isOpen, showResult, isComplete, timeLeft, handleAnswer])

  if (!isOpen && answeredToday) return null

  return (
    <>
      {!isOpen && (
        <motion.button initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}
          onClick={() => setIsOpen(true)}
          className="fixed left-4 top-1/2 -translate-y-1/2 z-40 bg-gradient-to-r from-violet-500 to-purple-600 p-4 rounded-full shadow-lg shadow-purple-500/30 border-2 border-white/20 group">
          <Brain className="w-6 h-6 text-white" />
          <span className="absolute -right-2 -top-2 bg-yellow-400 text-purple-900 text-xs font-bold px-2 py-1 rounded-full animate-bounce">
            +{todayQuestion.difficulty * 5} XP
          </span>
          <span className="absolute left-full ml-3 bg-gray-900/90 text-white px-3 py-2 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity">
            Викторина дня!
          </span>
        </motion.button>
      )}

      <AnimatePresence>
        {isOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="bg-gradient-to-br from-violet-900 to-indigo-900 rounded-3xl p-6 max-w-lg w-full shadow-2xl border-2 border-white/10">

            {/* Header */}
            <div className="flex justify-between items-center mb-6">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-violet-500/30 rounded-xl"><Brain className="w-6 h-6 text-violet-300" /></div>
                <div>
                  <h3 className="text-xl font-bold text-white">Викторина дня</h3>
                  <p className="text-violet-300 text-sm">{todayQuestion.subject}</p>
                </div>
              </div>
              <button onClick={() => setIsOpen(false)} className="text-white/50 hover:text-white"><X className="w-6 h-6" /></button>
            </div>

            {/* Timer */}
            {!isComplete && <TimerBar timeLeft={timeLeft} />}

            {/* Content */}
            {!isComplete ? (
              <QuestionContent question={todayQuestion} selectedAnswer={selectedAnswer} showResult={showResult} onAnswer={handleAnswer} />
            ) : (
              <CompletionScreen question={todayQuestion} selectedAnswer={selectedAnswer} onClose={() => setIsOpen(false)} />
            )}

            {/* Difficulty */}
            {!isComplete && <DifficultyIndicator difficulty={todayQuestion.difficulty} />}
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}

function TimerBar({ timeLeft }: { timeLeft: number }) {
  return (
    <div className="flex items-center gap-2 mb-4">
      <Clock className={`w-5 h-5 ${timeLeft <= 5 ? 'text-red-400 animate-pulse' : 'text-white/50'}`} />
      <div className="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
        <motion.div className={`h-full ${timeLeft <= 5 ? 'bg-red-500' : 'bg-violet-500'}`}
          initial={{ width: '100%' }} animate={{ width: `${(timeLeft / 15) * 100}%` }} />
      </div>
      <span className={`font-mono ${timeLeft <= 5 ? 'text-red-400' : 'text-white'}`}>{timeLeft}с</span>
    </div>
  )
}

function QuestionContent({ question, selectedAnswer, showResult, onAnswer }: { question: typeof quizQuestions[0]; selectedAnswer: number | null; showResult: boolean; onAnswer: (idx: number) => void }) {
  return (
    <>
      <div className="bg-white/5 rounded-2xl p-4 mb-6">
        <p className="text-white text-lg font-medium text-center">{question.question}</p>
      </div>
      <div className="grid grid-cols-2 gap-3">
        {question.options.map((option, idx) => (
          <motion.button key={idx} whileHover={{ scale: showResult ? 1 : 1.02 }} whileTap={{ scale: showResult ? 1 : 0.98 }}
            onClick={() => onAnswer(idx)} disabled={showResult}
            className={`p-4 rounded-xl text-left font-medium transition-all
              ${showResult ? idx === question.correct ? 'bg-green-500 text-white' : idx === selectedAnswer ? 'bg-red-500/50 text-white' : 'bg-white/5 text-white/50'
                : 'bg-white/10 text-white hover:bg-white/20'}`}>
            <span className="flex items-center gap-2">
              <span className="w-6 h-6 rounded-full bg-white/10 flex items-center justify-center text-sm">{String.fromCharCode(65 + idx)}</span>
              {option}
            </span>
          </motion.button>
        ))}
      </div>
      {showResult && (
        <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}
          className={`mt-4 p-3 rounded-xl text-center ${selectedAnswer === question.correct ? 'bg-green-500/20 border border-green-500/30' : 'bg-red-500/20 border border-red-500/30'}`}>
          {selectedAnswer === question.correct ? (
            <span className="text-green-300 flex items-center justify-center gap-2"><Sparkles className="w-5 h-5" />Правильно! +{question.difficulty * 5} XP</span>
          ) : selectedAnswer === -1 ? (
            <span className="text-red-300">Время вышло!</span>
          ) : (
            <span className="text-red-300">Неверно. Правильный ответ: {question.options[question.correct]}</span>
          )}
        </motion.div>
      )}
    </>
  )
}

function CompletionScreen({ question, selectedAnswer, onClose }: { question: typeof quizQuestions[0]; selectedAnswer: number | null; onClose: () => void }) {
  return (
    <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="text-center py-8">
      <motion.div animate={{ rotate: 360 }} transition={{ duration: 1, repeat: Infinity, ease: 'linear' }} className="inline-block">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
      </motion.div>
      <h4 className="text-2xl font-bold text-white mb-2">{selectedAnswer === question.correct ? 'Отлично!' : 'Попробуй завтра!'}</h4>
      <p className="text-violet-300 mb-4">
        {selectedAnswer === question.correct ? `Ты заработал ${question.difficulty * 5} XP и 1 звезду!` : 'Заходи завтра за новой викториной!'}
      </p>
      <div className="flex items-center justify-center gap-4">
        <div className="flex items-center gap-1 text-yellow-400"><Zap className="w-5 h-5" /><span>{question.difficulty * 5} XP</span></div>
        <div className="flex items-center gap-1 text-orange-400"><Star className="w-5 h-5" /><span>{selectedAnswer === question.correct ? 1 : 0}</span></div>
      </div>
      <button onClick={onClose} className="mt-6 px-6 py-3 bg-violet-500 hover:bg-violet-600 text-white rounded-xl font-medium transition-colors">Закрыть</button>
    </motion.div>
  )
}

function DifficultyIndicator({ difficulty }: { difficulty: number }) {
  return (
    <div className="flex items-center gap-1 mt-4 justify-center">
      {[1, 2, 3].map(level => (
        <Star key={level} className={`w-4 h-4 ${level <= difficulty ? 'text-yellow-400 fill-yellow-400' : 'text-white/20'}`} />
      ))}
      <span className="text-white/50 text-sm ml-2">Сложность: {difficulty}/3</span>
    </div>
  )
}
