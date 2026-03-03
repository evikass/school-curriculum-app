'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { Hash, RotateCcw, Trophy, Target, Zap, Info } from 'lucide-react'

interface PrimeQuestion {
  number: number
  isPrime: boolean
  factors?: number[]
}

// Функция проверки простого числа
const isPrimeNumber = (n: number): boolean => {
  if (n < 2) return false
  if (n === 2) return true
  if (n % 2 === 0) return false
  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    if (n % i === 0) return false
  }
  return true
}

// Получить делители числа
const getFactors = (n: number): number[] => {
  if (n < 2) return []
  const factors: number[] = []
  for (let i = 2; i <= n; i++) {
    if (n % i === 0) factors.push(i)
  }
  return factors
}

// Генерация вопросов
const generateQuestions = (difficulty: 'easy' | 'medium' | 'hard'): PrimeQuestion[] => {
  const questions: PrimeQuestion[] = []
  
  if (difficulty === 'easy') {
    // Числа от 2 до 30
    for (let i = 2; i <= 30; i++) {
      const prime = isPrimeNumber(i)
      questions.push({
        number: i,
        isPrime: prime,
        factors: prime ? undefined : getFactors(i)
      })
    }
  } else if (difficulty === 'medium') {
    // Числа от 2 до 100
    const numbers = new Set<number>()
    while (numbers.size < 20) {
      const n = Math.floor(Math.random() * 99) + 2
      numbers.add(n)
    }
    Array.from(numbers).forEach(n => {
      const prime = isPrimeNumber(n)
      questions.push({
        number: n,
        isPrime: prime,
        factors: prime ? undefined : getFactors(n)
      })
    })
  } else {
    // Числа до 500 + проверка делителей
    const numbers = new Set<number>()
    while (numbers.size < 20) {
      const n = Math.floor(Math.random() * 499) + 2
      numbers.add(n)
    }
    Array.from(numbers).forEach(n => {
      const prime = isPrimeNumber(n)
      questions.push({
        number: n,
        isPrime: prime,
        factors: prime ? undefined : getFactors(n)
      })
    })
  }
  
  return questions
}

// Первые простые числа для справки
const FIRST_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

export default function PrimeNumbers() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [questions, setQuestions] = useState<PrimeQuestion[]>([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [currentQuestion, setCurrentQuestion] = useState<PrimeQuestion | null>(null)
  const [selectedAnswer, setSelectedAnswer] = useState<boolean | null>(null)
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [mode, setMode] = useState<'menu' | 'game' | 'learn'>('menu')
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('easy')
  const [timer, setTimer] = useState(0)
  const [questionStart, setQuestionStart] = useState(0)

  useEffect(() => {
    if (mode === 'game' && questions.length > 0 && currentIndex < questions.length) {
      setCurrentQuestion(questions[currentIndex])
      setQuestionStart(Date.now())
    }
  }, [mode, questions, currentIndex])

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
    setCurrentIndex(0)
    setGameOver(false)
    setSelectedAnswer(null)
    setShowResult(false)
    setMode('game')
    const newQuestions = generateQuestions(diff)
    setQuestions(newQuestions)
    setCurrentQuestion(newQuestions[0])
    setQuestionStart(Date.now())
  }

  const handleSelect = (isPrime: boolean) => {
    if (!currentQuestion || showResult) return
    
    setSelectedAnswer(isPrime)
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = isPrime === currentQuestion.isPrime
    
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
      setSelectedAnswer(null)
      setShowResult(false)
      setTimer(0)
      
      if (currentIndex + 1 >= questions.length) {
        setGameOver(true)
      } else {
        setCurrentIndex(prev => prev + 1)
        setQuestionStart(Date.now())
      }
    }, 2000)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentQuestion(null)
    setGameOver(false)
    setQuestions([])
    setCurrentIndex(0)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-purple-900/50 to-violet-900/50 rounded-2xl p-6 backdrop-blur-sm border border-purple-500/30">
        <h2 className="text-2xl font-bold text-purple-300 mb-6 flex items-center gap-2">
          <Hash className="w-7 h-7" />
          Простые числа
        </h2>
        
        <p className="text-purple-200 mb-6">
          Простое число делится только на 1 и на себя. Определите, является ли число простым!
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
                {diff === 'easy' ? 'Числа 2-30' : diff === 'medium' ? 'Числа 2-100' : 'Числа до 500'}
              </div>
            </button>
          ))}
        </div>

        <button
          onClick={() => setMode('learn')}
          className="w-full p-4 rounded-xl font-bold transition-all hover:scale-[1.02] bg-purple-500/20 border-purple-500/50 hover:bg-purple-500/30 text-purple-300 border flex items-center justify-center gap-2"
        >
          <Info className="w-5 h-5" />
          Теория простых чисел
        </button>
      </div>
    )
  }

  if (mode === 'learn') {
    return (
      <div className="bg-gradient-to-br from-purple-900/50 to-violet-900/50 rounded-2xl p-6 backdrop-blur-sm border border-purple-500/30">
        <h2 className="text-2xl font-bold text-purple-300 mb-6 flex items-center gap-2">
          <Info className="w-7 h-7" />
          Теория: Простые числа
        </h2>
        
        <div className="space-y-4 text-purple-200">
          <div className="bg-white/10 rounded-lg p-4">
            <h3 className="font-bold text-purple-300 mb-2">Что такое простое число?</h3>
            <p>Простое число — это натуральное число больше 1, которое делится только на 1 и на себя.</p>
          </div>
          
          <div className="bg-white/10 rounded-lg p-4">
            <h3 className="font-bold text-purple-300 mb-2">Примеры:</h3>
            <ul className="list-disc list-inside space-y-1">
              <li><strong>2</strong> — простое (делится только на 1 и 2)</li>
              <li><strong>7</strong> — простое (делится только на 1 и 7)</li>
              <li><strong>4</strong> — НЕ простое (делится на 1, 2, 4)</li>
              <li><strong>9</strong> — НЕ простое (делится на 1, 3, 9)</li>
            </ul>
          </div>
          
          <div className="bg-white/10 rounded-lg p-4">
            <h3 className="font-bold text-purple-300 mb-2">Первые 25 простых чисел:</h3>
            <p className="text-2xl font-mono text-white">{FIRST_PRIMES.join(', ')}</p>
          </div>
          
          <div className="bg-white/10 rounded-lg p-4">
            <h3 className="font-bold text-purple-300 mb-2">Интересные факты:</h3>
            <ul className="list-disc list-inside space-y-1">
              <li>2 — единственное чётное простое число</li>
              <li>1 — НЕ простое число</li>
              <li>Простых чисел бесконечно много</li>
            </ul>
          </div>
        </div>
        
        <button
          onClick={() => setMode('menu')}
          className="mt-6 w-full py-3 bg-purple-500 hover:bg-purple-400 rounded-xl font-bold text-white transition-colors"
        >
          Назад
        </button>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-purple-900/50 to-violet-900/50 rounded-2xl p-6 backdrop-blur-sm border border-purple-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-purple-300 mb-2">Отлично!</h2>
        <p className="text-purple-200 mb-4">
          Результат: {score} XP за {totalQuestions} вопросов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-purple-500 hover:bg-purple-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-purple-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentQuestion) return null

  return (
    <div className="bg-gradient-to-br from-purple-900/50 to-violet-900/50 rounded-2xl p-6 backdrop-blur-sm border border-purple-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-purple-300 text-sm flex items-center gap-2">
          <Target className="w-4 h-4" />
          Простое или составное?
        </div>
        <div className="flex items-center gap-4">
          <span className="text-purple-300 text-sm">{timer.toFixed(1)}с</span>
          <span className="text-purple-300">Серия: {streak}🔥</span>
          <span className="text-purple-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-8 mb-6 text-center">
        <p className="text-purple-300 text-sm mb-2">Число:</p>
        <p className="text-6xl font-bold text-white">{currentQuestion.number}</p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <button
          onClick={() => handleSelect(true)}
          disabled={showResult}
          className={`p-6 rounded-xl font-bold border-2 transition-all ${
            showResult
              ? currentQuestion.isPrime
                ? 'bg-green-500/30 border-green-400 text-green-300'
                : selectedAnswer === true
                  ? 'bg-red-500/30 border-red-400 text-red-300'
                  : 'bg-white/10 border-white/20 text-white/50'
              : 'bg-white/10 hover:bg-green-500/20 border-white/20 hover:border-green-400 text-white'
          }`}
        >
          <span className="text-2xl block mb-2">✓</span>
          Простое
          <div className="text-xs opacity-75 mt-1">Делится только на 1 и себя</div>
        </button>
        
        <button
          onClick={() => handleSelect(false)}
          disabled={showResult}
          className={`p-6 rounded-xl font-bold border-2 transition-all ${
            showResult
              ? !currentQuestion.isPrime
                ? 'bg-green-500/30 border-green-400 text-green-300'
                : selectedAnswer === false
                  ? 'bg-red-500/30 border-red-400 text-red-300'
                  : 'bg-white/10 border-white/20 text-white/50'
              : 'bg-white/10 hover:bg-red-500/20 border-white/20 hover:border-red-400 text-white'
          }`}
        >
          <span className="text-2xl block mb-2">✗</span>
          Составное
          <div className="text-xs opacity-75 mt-1">Имеет другие делители</div>
        </button>
      </div>

      {showResult && (
        <div className={`mt-4 p-4 rounded-lg ${
          selectedAnswer === currentQuestion.isPrime
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          <p className="font-bold mb-1">
            {selectedAnswer === currentQuestion.isPrime
              ? '✅ Правильно!'
              : '❌ Неправильно!'}
          </p>
          <p className="text-sm">
            {currentQuestion.number} — {currentQuestion.isPrime 
              ? 'простое число (делится только на 1 и себя)' 
              : `составное число (делится на ${currentQuestion.factors?.join(', ')})`}
          </p>
        </div>
      )}

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-purple-400">
          Вопрос {currentIndex + 1} из {questions.length}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-purple-400 hover:text-purple-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
