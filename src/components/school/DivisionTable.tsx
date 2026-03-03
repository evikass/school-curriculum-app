'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { Divide, RotateCcw, Trophy, Zap, Target, Grid2X2 } from 'lucide-react'

interface DivisionProblem {
  a: number
  b: number
  answer: number
}

export default function DivisionTable() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentProblem, setCurrentProblem] = useState<DivisionProblem | null>(null)
  const [userAnswer, setUserAnswer] = useState('')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [correctAnswers, setCorrectAnswers] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [mode, setMode] = useState<'menu' | 'game' | 'table'>('menu')
  const [gameMode, setGameMode] = useState<'practice' | 'timed' | 'survival'>('practice')
  const [selectedNumber, setSelectedNumber] = useState<number | null>(null)
  const [timeLeft, setTimeLeft] = useState(60)
  const [lives, setLives] = useState(3)
  const [timer, setTimer] = useState(0)
  const [questionStart, setQuestionStart] = useState(0)

  const generateProblem = useCallback((number?: number): DivisionProblem => {
    if (number) {
      const b = Math.floor(Math.random() * 10) + 1
      const a = number * b
      return { a, b, answer: number }
    }
    const b = Math.floor(Math.random() * 9) + 2
    const answer = Math.floor(Math.random() * 9) + 2
    const a = b * answer
    return { a, b, answer }
  }, [])

  useEffect(() => {
    if (mode === 'game' && !currentProblem && !gameOver) {
      const problem = generateProblem(selectedNumber || undefined)
      setCurrentProblem(problem)
      setQuestionStart(Date.now())
    }
  }, [mode, currentProblem, gameOver, generateProblem, selectedNumber])

  useEffect(() => {
    if (mode === 'game' && gameMode === 'timed' && !showResult && !gameOver) {
      const interval = setInterval(() => {
        setTimeLeft(prev => {
          if (prev <= 1) {
            setGameOver(true)
            return 0
          }
          return prev - 1
        })
      }, 1000)
      return () => clearInterval(interval)
    }
  }, [mode, gameMode, showResult, gameOver])

  useEffect(() => {
    if (mode === 'game' && !showResult && !gameOver) {
      const interval = setInterval(() => {
        setTimer(Math.floor((Date.now() - questionStart) / 100) / 10)
      }, 100)
      return () => clearInterval(interval)
    }
  }, [mode, showResult, gameOver, questionStart])

  const startGame = (gMode: 'practice' | 'timed' | 'survival', number?: number) => {
    setGameMode(gMode)
    setSelectedNumber(number || null)
    setScore(0)
    setStreak(0)
    setTotalQuestions(0)
    setCorrectAnswers(0)
    setGameOver(false)
    setUserAnswer('')
    setShowResult(false)
    setTimeLeft(60)
    setLives(3)
    setMode('game')
    const problem = generateProblem(number)
    setCurrentProblem(problem)
    setQuestionStart(Date.now())
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!currentProblem || showResult) return
    
    const answer = parseInt(userAnswer)
    if (isNaN(answer)) return
    
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = answer === currentProblem.answer
    
    if (isCorrect) {
      playSound('correct')
      const newStreak = streak + 1
      setStreak(newStreak)
      setCorrectAnswers(prev => prev + 1)
      const timeBonus = Math.max(0, 5 - timer)
      const streakBonus = Math.floor(newStreak / 5) * 3
      const xp = 5 + timeBonus + streakBonus
      setScore(prev => prev + xp)
      addXP(xp)
    } else {
      playSound('wrong')
      setStreak(0)
      if (gameMode === 'survival') {
        setLives(prev => {
          if (prev <= 1) {
            setGameOver(true)
          }
          return prev - 1
        })
      }
    }
    
    const delay = isCorrect ? 1000 : 1500
    setTimeout(() => {
      setUserAnswer('')
      setShowResult(false)
      setTimer(0)
      setQuestionStart(Date.now())
      
      if (!gameOver && !(gameMode === 'survival' && lives <= 1)) {
        const problem = generateProblem(selectedNumber || undefined)
        setCurrentProblem(problem)
      }
    }, delay)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentProblem(null)
    setGameOver(false)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-emerald-900/50 to-green-900/50 rounded-2xl p-6 backdrop-blur-sm border border-emerald-500/30">
        <h2 className="text-2xl font-bold text-emerald-300 mb-6 flex items-center gap-2">
          <Divide className="w-7 h-7" />
          Таблица деления
        </h2>
        
        <p className="text-emerald-200 mb-6">
          Деление - это обратная операция умножению. Выберите число для практики!
        </p>
        
        <div className="grid grid-cols-5 gap-2 mb-6">
          {[2, 3, 4, 5, 6, 7, 8, 9].map((num) => (
            <button
              key={num}
              onClick={() => startGame('practice', num)}
              className="p-3 bg-white/10 hover:bg-emerald-500/30 border border-white/20 rounded-lg text-white font-bold transition-all hover:scale-105"
            >
              ÷{num}
            </button>
          ))}
          <button
            onClick={() => startGame('practice')}
            className="p-3 bg-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-400 rounded-lg text-emerald-300 font-bold transition-all hover:scale-105 col-span-2"
          >
            Все
          </button>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <button
            onClick={() => startGame('practice')}
            className="p-4 rounded-xl font-bold transition-all hover:scale-105 bg-green-500/20 border-green-500/50 hover:bg-green-500/30 text-green-300 border"
          >
            <Target className="w-6 h-6 mx-auto mb-2" />
            Практика
            <div className="text-xs opacity-75 mt-1">Без ограничений</div>
          </button>
          <button
            onClick={() => startGame('timed')}
            className="p-4 rounded-xl font-bold transition-all hover:scale-105 bg-yellow-500/20 border-yellow-500/50 hover:bg-yellow-500/30 text-yellow-300 border"
          >
            <Zap className="w-6 h-6 mx-auto mb-2" />
            На время
            <div className="text-xs opacity-75 mt-1">60 секунд</div>
          </button>
          <button
            onClick={() => startGame('survival')}
            className="p-4 rounded-xl font-bold transition-all hover:scale-105 bg-red-500/20 border-red-500/50 hover:bg-red-500/30 text-red-300 border"
          >
            <Divide className="w-6 h-6 mx-auto mb-2" />
            Выживание
            <div className="text-xs opacity-75 mt-1">3 жизни</div>
          </button>
        </div>

        <button
          onClick={() => setMode('table')}
          className="w-full p-4 rounded-xl font-bold transition-all hover:scale-[1.02] bg-emerald-500/20 border-emerald-500/50 hover:bg-emerald-500/30 text-emerald-300 border flex items-center justify-center gap-2"
        >
          <Grid2X2 className="w-5 h-5" />
          Показать таблицу деления
        </button>
      </div>
    )
  }

  if (mode === 'table') {
    return (
      <div className="bg-gradient-to-br from-emerald-900/50 to-green-900/50 rounded-2xl p-6 backdrop-blur-sm border border-emerald-500/30">
        <h2 className="text-2xl font-bold text-emerald-300 mb-4 flex items-center gap-2">
          <Grid2X2 className="w-7 h-7" />
          Таблица деления
        </h2>
        
        <div className="overflow-x-auto">
          <table className="w-full text-center">
            <thead>
              <tr>
                <th className="p-2 text-emerald-300">÷</th>
                {[2, 3, 4, 5, 6, 7, 8, 9, 10].map(n => (
                  <th key={n} className="p-2 text-emerald-300 font-bold">{n}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {[2, 4, 6, 8, 10, 12, 14, 16, 18].map(row => (
                <tr key={row}>
                  <td className="p-2 text-emerald-300 font-bold">{row}</td>
                  {[2, 3, 4, 5, 6, 7, 8, 9, 10].map(col => (
                    <td key={col} className={`p-2 text-white bg-white/5 border border-white/10 ${row % col === 0 ? '' : 'opacity-50'}`}>
                      {row % col === 0 ? row / col : '-'}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        
        <button
          onClick={() => setMode('menu')}
          className="mt-4 w-full py-3 bg-emerald-500 hover:bg-emerald-400 rounded-xl font-bold text-white transition-colors"
        >
          Назад
        </button>
      </div>
    )
  }

  if (gameOver) {
    const accuracy = totalQuestions > 0 ? Math.round((correctAnswers / totalQuestions) * 100) : 0
    return (
      <div className="bg-gradient-to-br from-emerald-900/50 to-green-900/50 rounded-2xl p-6 backdrop-blur-sm border border-emerald-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-emerald-300 mb-2">
          {gameMode === 'timed' ? 'Время вышло!' : 'Игра окончена!'}
        </h2>
        <p className="text-emerald-200 mb-2">
          Результат: {score} XP
        </p>
        <p className="text-emerald-300 text-sm mb-4">
          Правильных ответов: {correctAnswers} из {totalQuestions} ({accuracy}%)
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(gameMode, selectedNumber || undefined)}
            className="px-6 py-3 bg-emerald-500 hover:bg-emerald-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-emerald-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentProblem) return null

  return (
    <div className="bg-gradient-to-br from-emerald-900/50 to-green-900/50 rounded-2xl p-6 backdrop-blur-sm border border-emerald-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-emerald-300 text-sm">
          {gameMode === 'timed' && `⏱️ ${timeLeft} сек`}
          {gameMode === 'survival' && `❤️ ${lives}`}
          {gameMode === 'practice' && `Вопрос ${totalQuestions + 1}`}
        </div>
        <div className="flex items-center gap-4">
          <span className="text-emerald-300">Серия: {streak}🔥</span>
          <span className="text-emerald-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-8 mb-6 text-center">
        <p className="text-5xl font-bold text-white mb-4">
          {currentProblem.a} ÷ {currentProblem.b} = ?
        </p>
        {gameMode === 'practice' && (
          <p className="text-emerald-300 text-sm">⏱️ {timer.toFixed(1)} сек</p>
        )}
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="number"
          value={userAnswer}
          onChange={(e) => setUserAnswer(e.target.value)}
          placeholder="Ответ"
          className="w-full bg-white/10 border border-emerald-500/30 rounded-xl px-4 py-4 text-white placeholder-emerald-300 focus:outline-none focus:border-emerald-400 text-2xl text-center"
          autoFocus
        />
      </form>

      {showResult && (
        <div className={`mt-4 p-4 rounded-lg text-center ${
          parseInt(userAnswer) === currentProblem.answer
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          <p className="font-bold text-xl">
            {parseInt(userAnswer) === currentProblem.answer
              ? '✅ Правильно!'
              : `❌ Неправильно. ${currentProblem.a} ÷ ${currentProblem.b} = ${currentProblem.answer}`}
          </p>
        </div>
      )}

      <div className="mt-6 grid grid-cols-3 gap-2">
        {[1, 2, 3, 4, 5, 6, 7, 8, 9, null, 0, 'del'].map((num, i) => (
          <button
            key={i}
            onClick={() => {
              if (num === null) return
              if (num === 'del') {
                setUserAnswer(prev => prev.slice(0, -1))
              } else {
                setUserAnswer(prev => prev + num)
              }
            }}
            disabled={showResult}
            className={`p-3 rounded-lg font-bold text-xl transition-all ${
              num === null 
                ? 'invisible' 
                : num === 'del'
                  ? 'bg-red-500/20 text-red-300 hover:bg-red-500/30'
                  : 'bg-white/10 text-white hover:bg-white/20'
            }`}
          >
            {num === 'del' ? '⌫' : num}
          </button>
        ))}
      </div>

      <button
        onClick={() => handleSubmit({ preventDefault: () => {} } as React.FormEvent)}
        disabled={!userAnswer || showResult}
        className="mt-4 w-full py-3 bg-emerald-500 hover:bg-emerald-400 disabled:opacity-50 rounded-xl font-bold text-white transition-colors"
      >
        Проверить
      </button>

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-emerald-400">
          {selectedNumber ? `Таблица ÷${selectedNumber}` : 'Все таблицы'}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-emerald-400 hover:text-emerald-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
