'use client'

import { useState, useMemo } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  X, CheckCircle, XCircle, Trophy, Star, Sparkles, 
  RotateCcw, ChevronRight, HelpCircle
} from 'lucide-react'

interface LessonQuizProps {
  lessonTitle: string
  lessonDescription: string
  isOpen: boolean
  onClose: () => void
  onComplete: (score: number) => void
}

// Генерация вопросов на основе урока
function generateQuestions(title: string, description: string) {
  // Базовые вопросы на основе названия и описания
  const questions = []
  
  // Вопрос 1: Основной термин из названия
  const keyTerms = title.match(/([А-ЯЁ][а-яё]+(?:\s+[а-яё]+)?)/g) || []
  if (keyTerms.length > 0) {
    questions.push({
      type: 'understanding',
      question: `Что означает термин "${keyTerms[0]}" в контексте данного урока?`,
      options: [
        description.slice(0, 50) + '...',
        'Научное понятие из учебника',
        'Непонятное слово',
        'Простое выражение'
      ],
      correct: 0,
      hint: 'Внимательно прочитай описание урока'
    })
  }
  
  // Вопрос 2: Проверка понимания
  questions.push({
    type: 'comprehension',
    question: `Какое утверждение правильно описывает тему "${title}"?`,
    options: [
      description.slice(0, 60) + '...',
      'Это сложная тема для взрослых',
      'Это не важно для изучения',
      'Это просто теория без практики'
    ],
    correct: 0,
    hint: 'Ответ находится в описании урока'
  })
  
  // Вопрос 3: Применение знаний
  questions.push({
    type: 'application',
    question: 'Для чего нужно изучать эту тему?',
    options: [
      'Чтобы лучше понимать мир вокруг',
      'Это не нужно в жизни',
      'Только для сдачи экзамена',
      'Чтобы получить хорошую оценку'
    ],
    correct: 0,
    hint: 'Знания помогают нам развиваться'
  })
  
  // Вопрос 4: Верно/неверно
  questions.push({
    type: 'truefalse',
    question: `Верно ли, что "${title}" является важной темой для изучения?`,
    options: ['Верно', 'Неверно'],
    correct: 0,
    hint: 'Все темы в учебнике важны'
  })
  
  return questions
}

export default function LessonQuiz({ 
  lessonTitle, 
  lessonDescription, 
  isOpen, 
  onClose, 
  onComplete 
}: LessonQuizProps) {
  const [currentQuestion, setCurrentQuestion] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [showResult, setShowResult] = useState(false)
  const [score, setScore] = useState(0)
  const [isComplete, setIsComplete] = useState(false)
  const [wrongAnswers, setWrongAnswers] = useState<number[]>([])
  
  const questions = useMemo(() => 
    generateQuestions(lessonTitle, lessonDescription), 
    [lessonTitle, lessonDescription]
  )
  
  const handleAnswer = (answerIndex: number) => {
    if (showResult) return
    
    setSelectedAnswer(answerIndex)
    setShowResult(true)
    
    const isCorrect = answerIndex === questions[currentQuestion].correct
    if (isCorrect) {
      setScore(s => s + 1)
    } else {
      setWrongAnswers([...wrongAnswers, currentQuestion])
    }
  }
  
  const nextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1)
      setSelectedAnswer(null)
      setShowResult(false)
    } else {
      setIsComplete(true)
      onComplete(score + (selectedAnswer === questions[currentQuestion].correct ? 1 : 0))
    }
  }
  
  const resetQuiz = () => {
    setCurrentQuestion(0)
    setSelectedAnswer(null)
    setShowResult(false)
    setScore(0)
    setIsComplete(false)
    setWrongAnswers([])
  }
  
  const getScoreMessage = () => {
    const percentage = (score / questions.length) * 100
    if (percentage >= 100) return { message: 'Превосходно! Идеальный результат! 🎉', color: 'text-yellow-400' }
    if (percentage >= 75) return { message: 'Отлично! Ты хорошо усвоил материал! 🌟', color: 'text-green-400' }
    if (percentage >= 50) return { message: 'Хорошо! Но есть над чем поработать! 💪', color: 'text-blue-400' }
    return { message: 'Попробуй ещё раз! Ты справишься! 📚', color: 'text-orange-400' }
  }
  
  if (!isOpen) return null
  
  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="fixed inset-0 z-50 flex items-center justify-center p-4
                   bg-black/70 backdrop-blur-sm"
        onClick={(e) => e.target === e.currentTarget && onClose()}
      >
        <motion.div
          initial={{ scale: 0.8, opacity: 0, y: 50 }}
          animate={{ scale: 1, opacity: 1, y: 0 }}
          exit={{ scale: 0.8, opacity: 0, y: 50 }}
          className="bg-gradient-to-br from-blue-900 to-indigo-900
                     rounded-3xl max-w-lg w-full max-h-[85vh] overflow-hidden
                     shadow-2xl border-2 border-white/10 flex flex-col"
        >
          {/* Header */}
          <div className="p-4 border-b border-white/10">
            <div className="flex justify-between items-center">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-blue-500/30 rounded-xl">
                  <HelpCircle className="w-5 h-5 text-blue-300" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-white">Тест: {lessonTitle}</h3>
                  {!isComplete && (
                    <p className="text-blue-300 text-sm">
                      Вопрос {currentQuestion + 1} из {questions.length}
                    </p>
                  )}
                </div>
              </div>
              <button onClick={onClose} className="text-white/50 hover:text-white p-2">
                <X className="w-5 h-5" />
              </button>
            </div>
            
            {/* Progress bar */}
            {!isComplete && (
              <div className="mt-3 h-2 bg-white/10 rounded-full overflow-hidden">
                <motion.div
                  className="h-full bg-gradient-to-r from-blue-500 to-cyan-500"
                  initial={{ width: 0 }}
                  animate={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
                />
              </div>
            )}
          </div>
          
          {/* Content */}
          <div className="flex-1 overflow-y-auto p-6">
            {!isComplete ? (
              <div className="space-y-6">
                {/* Question */}
                <div className="bg-white/5 rounded-2xl p-4 border border-white/10">
                  <p className="text-white text-lg font-medium">
                    {questions[currentQuestion].question}
                  </p>
                </div>
                
                {/* Options */}
                <div className="space-y-3">
                  {questions[currentQuestion].options.map((option, idx) => (
                    <motion.button
                      key={idx}
                      whileHover={{ scale: showResult ? 1 : 1.02 }}
                      whileTap={{ scale: showResult ? 1 : 0.98 }}
                      onClick={() => handleAnswer(idx)}
                      disabled={showResult}
                      className={`w-full p-4 rounded-xl text-left font-medium transition-all
                                ${showResult 
                                  ? idx === questions[currentQuestion].correct
                                    ? 'bg-green-500/30 border-2 border-green-500 text-white'
                                    : idx === selectedAnswer
                                      ? 'bg-red-500/30 border-2 border-red-500 text-white'
                                      : 'bg-white/5 text-white/50'
                                  : 'bg-white/10 text-white hover:bg-white/20 border-2 border-transparent'
                                }`}
                    >
                      <span className="flex items-center gap-3">
                        <span className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold
                                        ${showResult 
                                          ? idx === questions[currentQuestion].correct
                                            ? 'bg-green-500 text-white'
                                            : idx === selectedAnswer
                                              ? 'bg-red-500 text-white'
                                              : 'bg-white/10 text-white/50'
                                          : 'bg-white/10 text-white'
                                        }`}>
                          {showResult ? (
                            idx === questions[currentQuestion].correct ? (
                              <CheckCircle className="w-5 h-5" />
                            ) : idx === selectedAnswer ? (
                              <XCircle className="w-5 h-5" />
                            ) : (
                              String.fromCharCode(65 + idx)
                            )
                          ) : (
                            String.fromCharCode(65 + idx)
                          )}
                        </span>
                        {option}
                      </span>
                    </motion.button>
                  ))}
                </div>
                
                {/* Hint */}
                {showResult && (
                  <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4"
                  >
                    <p className="text-blue-300 text-sm">
                      💡 {questions[currentQuestion].hint}
                    </p>
                  </motion.div>
                )}
              </div>
            ) : (
              /* Results */
              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                className="text-center py-8"
              >
                <motion.div
                  animate={{ rotate: [0, 360] }}
                  transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}
                  className="inline-block mb-4"
                >
                  <Trophy className={`w-20 h-20 ${
                    score === questions.length ? 'text-yellow-400' : 'text-blue-400'
                  }`} />
                </motion.div>
                
                <h4 className="text-2xl font-bold text-white mb-2">
                  Результат: {score} из {questions.length}
                </h4>
                
                <p className={`text-lg mb-6 ${getScoreMessage().color}`}>
                  {getScoreMessage().message}
                </p>
                
                {/* Stars earned — 5-star rating */}
                <div className="flex items-center justify-center gap-2 mb-6">
                  {[0, 1, 2, 3, 4].map((idx) => {
                    const starsEarned = Math.round((score / questions.length) * 5)
                    return (
                      <Star
                        key={idx}
                        className={`w-8 h-8 ${
                          idx < starsEarned 
                            ? 'text-yellow-400 fill-yellow-400' 
                            : 'text-white/20'
                        }`}
                      />
                    )
                  })}
                </div>
                
                {/* Wrong answers review */}
                {wrongAnswers.length > 0 && (
                  <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 mb-6 text-left">
                    <p className="text-red-400 font-medium mb-2">
                      Вопросы для повторения:
                    </p>
                    {wrongAnswers.map((idx) => (
                      <p key={idx} className="text-red-300 text-sm">
                        • {questions[idx].question}
                      </p>
                    ))}
                  </div>
                )}
                
                <div className="flex gap-3">
                  <button
                    onClick={resetQuiz}
                    className="flex-1 py-3 bg-white/10 hover:bg-white/20
                              text-white rounded-xl font-medium transition-colors
                              flex items-center justify-center gap-2"
                  >
                    <RotateCcw className="w-5 h-5" />
                    Ещё раз
                  </button>
                  <button
                    onClick={onClose}
                    className="flex-1 py-3 bg-gradient-to-r from-green-500 to-emerald-500 
                              text-white rounded-xl font-medium transition-colors
                              flex items-center justify-center gap-2"
                  >
                    <Sparkles className="w-5 h-5" />
                    Готово!
                  </button>
                </div>
              </motion.div>
            )}
          </div>
          
          {/* Footer */}
          {!isComplete && showResult && (
            <div className="p-4 border-t border-white/10">
              <button
                onClick={nextQuestion}
                className="w-full py-3 bg-gradient-to-r from-blue-500 to-cyan-500 
                          hover:from-blue-600 hover:to-cyan-600
                          text-white rounded-xl font-medium transition-colors
                          flex items-center justify-center gap-2"
              >
                {currentQuestion < questions.length - 1 ? (
                  <>
                    Следующий вопрос
                    <ChevronRight className="w-5 h-5" />
                  </>
                ) : (
                  <>
                    Показать результат
                    <Trophy className="w-5 h-5" />
                  </>
                )}
              </button>
            </div>
          )}
        </motion.div>
      </motion.div>
    </AnimatePresence>
  )
}
