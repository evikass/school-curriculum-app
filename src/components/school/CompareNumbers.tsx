'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { ArrowLeftRight, RotateCcw, Trophy, Target, Zap } from 'lucide-react'

interface CompareQuestion {
  left: number | { a: number; op: string; b: number }
  right: number | { a: number; op: string; b: number }
  answer: '<' | '=' | '>'
  difficulty: 'easy' | 'medium' | 'hard'
}

const QUESTIONS: CompareQuestion[] = [
  // Лёгкий уровень - сравнение чисел
  { left: 5, right: 8, answer: '<', difficulty: 'easy' },
  { left: 12, right: 7, answer: '>', difficulty: 'easy' },
  { left: 15, right: 15, answer: '=', difficulty: 'easy' },
  { left: 23, right: 32, answer: '<', difficulty: 'easy' },
  { left: 100, right: 99, answer: '>', difficulty: 'easy' },
  { left: 45, right: 54, answer: '<', difficulty: 'easy' },
  { left: 78, right: 78, answer: '=', difficulty: 'easy' },
  { left: 9, right: 11, answer: '<', difficulty: 'easy' },
  { left: 50, right: 49, answer: '>', difficulty: 'easy' },
  { left: 33, right: 33, answer: '=', difficulty: 'easy' },
  { left: 67, right: 76, answer: '<', difficulty: 'easy' },
  { left: 200, right: 199, answer: '>', difficulty: 'easy' },
  
  // Средний уровень - сравнение результатов выражений
  { left: { a: 5, op: '+', b: 3 }, right: { a: 10, op: '-', b: 2 }, answer: '=', difficulty: 'medium' },
  { left: { a: 4, op: '×', b: 5 }, right: { a: 3, op: '×', b: 7 }, answer: '<', difficulty: 'medium' },
  { left: { a: 24, op: '÷', b: 6 }, right: { a: 18, op: '÷', b: 3 }, answer: '<', difficulty: 'medium' },
  { left: { a: 7, op: '+', b: 8 }, right: { a: 6, op: '+', b: 9 }, answer: '=', difficulty: 'medium' },
  { left: { a: 15, op: '-', b: 7 }, right: { a: 20, op: '-', b: 10 }, answer: '<', difficulty: 'medium' },
  { left: { a: 6, op: '×', b: 4 }, right: { a: 5, op: '×', b: 5 }, answer: '<', difficulty: 'medium' },
  { left: { a: 36, op: '÷', b: 4 }, right: { a: 45, op: '÷', b: 5 }, answer: '=', difficulty: 'medium' },
  { left: { a: 12, op: '+', b: 12 }, right: { a: 5, op: '×', b: 5 }, answer: '<', difficulty: 'medium' },
  { left: { a: 100, op: '-', b: 25 }, right: { a: 8, op: '×', b: 10 }, answer: '<', difficulty: 'medium' },
  { left: { a: 9, op: '×', b: 3 }, right: { a: 10, op: '×', b: 3 }, answer: '<', difficulty: 'medium' },
  { left: { a: 72, op: '÷', b: 8 }, right: { a: 56, op: '÷', b: 7 }, answer: '=', difficulty: 'medium' },
  { left: { a: 25, op: '+', b: 15 }, right: { a: 50, op: '-', b: 10 }, answer: '=', difficulty: 'medium' },
  
  // Сложный уровень - смешанные операции и большие числа
  { left: { a: 15, op: '×', b: 4 }, right: { a: 12, op: '×', b: 5 }, answer: '=', difficulty: 'hard' },
  { left: { a: 144, op: '÷', b: 12 }, right: { a: 156, op: '÷', b: 13 }, answer: '=', difficulty: 'hard' },
  { left: { a: 7, op: '×', b: 8 }, right: { a: 9, op: '×', b: 6 }, answer: '>', difficulty: 'hard' },
  { left: { a: 1000, op: '÷', b: 8 }, right: { a: 125, op: '×', b: 1 }, answer: '=', difficulty: 'hard' },
  { left: { a: 23, op: '+', b: 45 }, right: { a: 8, op: '×', b: 9 }, answer: '=', difficulty: 'hard' },
  { left: { a: 17, op: '×', b: 3 }, right: { a: 25, op: '×', b: 2 }, answer: '>', difficulty: 'hard' },
  { left: { a: 225, op: '÷', b: 15 }, right: { a: 196, op: '÷', b: 14 }, answer: '=', difficulty: 'hard' },
  { left: { a: 6, op: '×', b: 7 }, right: { a: 5, op: '×', b: 8 }, answer: '>', difficulty: 'hard' },
  { left: { a: 11, op: '×', b: 11 }, right: { a: 12, op: '×', b: 10 }, answer: '>', difficulty: 'hard' },
  { left: { a: 81, op: '÷', b: 9 }, right: { a: 64, op: '÷', b: 8 }, answer: '=', difficulty: 'hard' },
  { left: { a: 13, op: '×', b: 4 }, right: { a: 15, op: '×', b: 3 }, answer: '>', difficulty: 'hard' },
  { left: { a: 256, op: '÷', b: 16 }, right: { a: 16, op: '×', b: 1 }, answer: '=', difficulty: 'hard' },
]

const evaluateExpression = (expr: number | { a: number; op: string; b: number }): number => {
  if (typeof expr === 'number') return expr
  const { a, op, b } = expr
  switch (op) {
    case '+': return a + b
    case '-': return a - b
    case '×': return a * b
    case '÷': return a / b
    default: return 0
  }
}

const formatExpression = (expr: number | { a: number; op: string; b: number }): string => {
  if (typeof expr === 'number') return expr.toString()
  return `${expr.a} ${expr.op} ${expr.b}`
}

export default function CompareNumbers() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentQuestion, setCurrentQuestion] = useState<CompareQuestion | null>(null)
  const [selectedAnswer, setSelectedAnswer] = useState<'<' | '=' | '>' | null>(null)
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('easy')
  const [usedQuestions, setUsedQuestions] = useState<Set<number>>(new Set())
  const [mode, setMode] = useState<'menu' | 'game'>('menu')
  const [timer, setTimer] = useState(0)
  const [questionStart, setQuestionStart] = useState(0)

  const getFilteredQuestions = useCallback(() => {
    return QUESTIONS.filter(q => q.difficulty === difficulty)
  }, [difficulty])

  const getNextQuestion = useCallback(() => {
    const filtered = getFilteredQuestions()
    const available = filtered
      .map((q, i) => ({ q, originalIndex: QUESTIONS.indexOf(q) }))
      .filter(item => !usedQuestions.has(item.originalIndex))
    
    if (available.length === 0) {
      setGameOver(true)
      return null
    }
    
    const randomIndex = Math.floor(Math.random() * available.length)
    return available[randomIndex].q
  }, [getFilteredQuestions, usedQuestions])

  useEffect(() => {
    if (mode === 'game' && !currentQuestion && !gameOver) {
      const q = getNextQuestion()
      if (q) setCurrentQuestion(q)
    }
  }, [mode, currentQuestion, gameOver, getNextQuestion])

  useEffect(() => {
    if (mode === 'game' && !showResult) {
      const interval = setInterval(() => {
        setTimer(Math.floor((Date.now() - questionStart) / 100) / 10)
      }, 100)
      return () => clearInterval(interval)
    }
  }, [mode, showResult, questionStart])

  const startGame = (diff: 'easy' | 'medium' | 'hard') => {
    setDifficulty(diff)
    setScore(0)
    setStreak(0)
    setTotalQuestions(0)
    setUsedQuestions(new Set())
    setGameOver(false)
    setSelectedAnswer(null)
    setShowResult(false)
    setMode('game')
    setQuestionStart(Date.now())
    const filtered = QUESTIONS.filter(q => q.difficulty === diff)
    const randomIndex = Math.floor(Math.random() * filtered.length)
    setCurrentQuestion(filtered[randomIndex])
    setUsedQuestions(new Set([QUESTIONS.indexOf(filtered[randomIndex])]))
  }

  const handleSelect = (answer: '<' | '=' | '>') => {
    if (!currentQuestion || showResult) return
    
    setSelectedAnswer(answer)
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = answer === currentQuestion.answer
    
    if (isCorrect) {
      playSound('correct')
      const newStreak = streak + 1
      setStreak(newStreak)
      const timeBonus = Math.max(0, 10 - timer)
      const streakBonus = Math.floor(newStreak / 3) * 2
      const xp = 10 + timeBonus + streakBonus
      setScore(prev => prev + xp)
      addXP(xp)
    } else {
      playSound('wrong')
      setStreak(0)
    }
    
    setTimeout(() => {
      const originalIndex = QUESTIONS.indexOf(currentQuestion)
      const newUsed = new Set(usedQuestions).add(originalIndex)
      setUsedQuestions(newUsed)
      setSelectedAnswer(null)
      setShowResult(false)
      setTimer(0)
      setQuestionStart(Date.now())
      
      const filtered = QUESTIONS.filter(q => q.difficulty === difficulty)
      const available = filtered.filter(q => !newUsed.has(QUESTIONS.indexOf(q)))
      
      if (available.length === 0) {
        setGameOver(true)
      } else {
        const nextQ = available[Math.floor(Math.random() * available.length)]
        setCurrentQuestion(nextQ)
      }
    }, 2000)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentQuestion(null)
    setGameOver(false)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-sky-900/50 to-blue-900/50 rounded-2xl p-6 backdrop-blur-sm border border-sky-500/30">
        <h2 className="text-2xl font-bold text-sky-300 mb-6 flex items-center gap-2">
          <ArrowLeftRight className="w-7 h-7" />
          Сравнение чисел
        </h2>
        
        <p className="text-sky-200 mb-6">
          Сравните числа или результаты выражений. Выберите правильный знак: меньше, равно или больше!
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          {(['easy', 'medium', 'hard'] as const).map((diff) => (
            <button
              key={diff}
              onClick={() => startGame(diff)}
              className={`p-4 rounded-xl font-bold transition-all hover:scale-105 ${
                diff === 'easy' 
                  ? 'bg-green-500/20 border-green-500/50 hover:bg-green-500/30 text-green-300' 
                  : diff === 'medium'
                    ? 'bg-yellow-500/20 border-yellow-500/50 hover:bg-yellow-500/30 text-yellow-300'
                    : 'bg-red-500/20 border-red-500/50 hover:bg-red-500/30 text-red-300'
              } border`}
            >
              {diff === 'easy' ? 'Легко' : diff === 'medium' ? 'Средне' : 'Сложно'}
              <div className="text-xs opacity-75 mt-1">
                {diff === 'easy' ? 'Числа' : diff === 'medium' ? 'Выражения' : 'Сложные'}
              </div>
            </button>
          ))}
        </div>
        
        <div className="grid grid-cols-3 gap-4">
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-3xl text-white mb-1">&lt;</div>
            <div className="text-xs text-sky-300">Меньше</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-3xl text-white mb-1">=</div>
            <div className="text-xs text-sky-300">Равно</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-3xl text-white mb-1">&gt;</div>
            <div className="text-xs text-sky-300">Больше</div>
          </div>
        </div>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-sky-900/50 to-blue-900/50 rounded-2xl p-6 backdrop-blur-sm border border-sky-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-sky-300 mb-2">Отлично!</h2>
        <p className="text-sky-200 mb-4">
          Результат: {score} XP за {totalQuestions} вопросов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-sky-500 hover:bg-sky-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-sky-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentQuestion) return null

  const leftValue = evaluateExpression(currentQuestion.left)
  const rightValue = evaluateExpression(currentQuestion.right)

  return (
    <div className="bg-gradient-to-br from-sky-900/50 to-blue-900/50 rounded-2xl p-6 backdrop-blur-sm border border-sky-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-sky-300 text-sm flex items-center gap-2">
          <Target className="w-4 h-4" />
          Сравните значения
        </div>
        <div className="flex items-center gap-4">
          <span className="text-sky-300 text-sm">{timer.toFixed(1)}с</span>
          <span className="text-sky-300">Серия: {streak}🔥</span>
          <span className="text-sky-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-6 mb-6">
        <div className="flex items-center justify-center gap-4">
          <div className="text-center">
            <p className="text-3xl font-bold text-white mb-2">
              {formatExpression(currentQuestion.left)}
            </p>
            {typeof currentQuestion.left !== 'number' && (
              <p className="text-sky-300 text-sm">= {leftValue}</p>
            )}
          </div>
          
          <div className="text-4xl text-sky-400 font-bold">?</div>
          
          <div className="text-center">
            <p className="text-3xl font-bold text-white mb-2">
              {formatExpression(currentQuestion.right)}
            </p>
            {typeof currentQuestion.right !== 'number' && (
              <p className="text-sky-300 text-sm">= {rightValue}</p>
            )}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-4">
        {(['<', '=', '>'] as const).map((symbol) => {
          const isSelected = selectedAnswer === symbol
          const isCorrect = symbol === currentQuestion.answer
          
          let buttonClass = 'bg-white/10 hover:bg-white/20 border-white/20 text-white'
          if (showResult) {
            if (isCorrect) {
              buttonClass = 'bg-green-500/30 border-green-400 text-green-300'
            } else if (isSelected && !isCorrect) {
              buttonClass = 'bg-red-500/30 border-red-400 text-red-300'
            }
          }
          
          return (
            <button
              key={symbol}
              onClick={() => handleSelect(symbol)}
              disabled={showResult}
              className={`p-6 rounded-xl font-bold border-2 transition-all ${buttonClass}`}
            >
              <span className="text-4xl">{symbol}</span>
              <div className="text-xs mt-2 opacity-75">
                {symbol === '<' ? 'Меньше' : symbol === '=' ? 'Равно' : 'Больше'}
              </div>
            </button>
          )
        })}
      </div>

      {showResult && (
        <div className={`mt-4 p-3 rounded-lg text-center ${
          selectedAnswer === currentQuestion.answer
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          <p className="font-bold">
            {selectedAnswer === currentQuestion.answer
              ? '✅ Правильно!'
              : `❌ Правильный ответ: ${currentQuestion.answer}`}
          </p>
          <p className="text-sm opacity-75">
            {leftValue} {currentQuestion.answer} {rightValue}
          </p>
        </div>
      )}

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-sky-400">
          Вопрос {totalQuestions + 1} из {getFilteredQuestions().length}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-sky-400 hover:text-sky-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
