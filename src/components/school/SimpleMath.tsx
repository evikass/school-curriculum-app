'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw, Plus, Minus } from 'lucide-react'

type Operation = 'add' | 'subtract' | 'mixed'
type Difficulty = 'easy' | 'medium' | 'hard'

interface Problem {
  num1: number
  num2: number
  operation: 'add' | 'subtract'
  answer: number
}

export default function SimpleMath() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [operation, setOperation] = useState<Operation>('add')
  const [difficulty, setDifficulty] = useState<Difficulty>('easy')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  const [problem, setProblem] = useState<Problem | null>(null)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [showVisual, setShowVisual] = useState(true)

  const getRange = () => {
    switch (difficulty) {
      case 'easy': return { min: 1, max: 10 }
      case 'medium': return { min: 5, max: 20 }
      case 'hard': return { min: 10, max: 50 }
    }
  }

  const generateProblem = () => {
    const range = getRange()
    const op: 'add' | 'subtract' = operation === 'mixed' 
      ? (Math.random() > 0.5 ? 'add' : 'subtract')
      : operation
    
    let num1 = Math.floor(Math.random() * (range.max - range.min + 1)) + range.min
    let num2 = Math.floor(Math.random() * (range.max - range.min + 1)) + range.min
    
    if (op === 'subtract' && num1 < num2) {
      [num1, num2] = [num2, num1]
    }
    
    const answer = op === 'add' ? num1 + num2 : num1 - num2
    setProblem({ num1, num2, operation: op, answer })
    setSelectedAnswer(null)
  }

  useEffect(() => {
    generateProblem()
  }, [operation, difficulty])

  const handleAnswer = (answer: number) => {
    if (!problem) return
    
    setSelectedAnswer(answer)
    const correct = answer === problem.answer
    
    if (correct) {
      playCorrect()
      const points = difficulty === 'easy' ? 10 : difficulty === 'medium' ? 15 : 20
      setScore(s => s + points)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(5 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateProblem()
    }, 1200)
  }

  const generateOptions = () => {
    if (!problem) return []
    const options = new Set([problem.answer])
    while (options.size < 4) {
      const offset = Math.floor(Math.random() * 10) - 5
      const opt = problem.answer + offset
      if (opt >= 0 && opt !== problem.answer) {
        options.add(opt)
      }
    }
    return Array.from(options).sort(() => Math.random() - 0.5)
  }

  const renderVisual = () => {
    if (!problem || !showVisual) return null
    
    const items = ['🍎', '🍊', '🍋', '🍇', '🍓', '🌟', '🔵', '🟢', '🟡', '🟣']
    const item = items[Math.floor(Math.random() * items.length)]
    
    if (problem.operation === 'add') {
      return (
        <div className="flex flex-col items-center gap-2 mb-4">
          <div className="flex flex-wrap justify-center gap-1 max-w-xs">
            {Array(problem.num1).fill(0).map((_, i) => (
              <span key={`a${i}`} className="text-2xl animate-bounce" style={{ animationDelay: `${i * 50}ms` }}>{item}</span>
            ))}
          </div>
          <span className="text-3xl text-white">+</span>
          <div className="flex flex-wrap justify-center gap-1 max-w-xs">
            {Array(problem.num2).fill(0).map((_, i) => (
              <span key={`b${i}`} className="text-2xl animate-bounce" style={{ animationDelay: `${i * 50}ms` }}>{item}</span>
            ))}
          </div>
        </div>
      )
    } else {
      const crossed = problem.num1 - problem.answer
      return (
        <div className="flex flex-col items-center gap-2 mb-4">
          <div className="flex flex-wrap justify-center gap-1 max-w-xs">
            {Array(problem.num1).fill(0).map((_, i) => (
              <span 
                key={i} 
                className={`text-2xl ${i < crossed ? 'line-through opacity-30' : ''}`}
              >
                {item}
              </span>
            ))}
          </div>
          <div className="text-white/60 text-sm">Забрали: {crossed} {item}</div>
        </div>
      )
    }
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    generateProblem()
  }

  return (
    <div className="bg-gradient-to-br from-emerald-500/20 to-green-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">➕➖</span> Сложение и Вычитание
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-3">
        {(['add', 'subtract', 'mixed'] as Operation[]).map(op => (
          <button
            key={op}
            onClick={() => { setOperation(op); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all flex items-center justify-center gap-1 ${operation === op ? 'bg-emerald-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {op === 'add' ? <><Plus className="w-4 h-4" /> Сложение</> : op === 'subtract' ? <><Minus className="w-4 h-4" /> Вычитание</> : '🔢 Всё вместе'}
          </button>
        ))}
      </div>

      <div className="flex gap-2 mb-4">
        {(['easy', 'medium', 'hard'] as Difficulty[]).map(d => (
          <button
            key={d}
            onClick={() => { setDifficulty(d); reset() }}
            className={`flex-1 py-1 rounded-lg text-xs font-medium transition-all ${difficulty === d ? 'bg-green-500 text-white' : 'bg-white/10 text-white/50 hover:bg-white/20'}`}
          >
            {d === 'easy' ? 'Легко (1-10)' : d === 'medium' ? 'Средне (5-20)' : 'Сложно (10-50)'}
          </button>
        ))}
      </div>

      {problem && (
        <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
          <div className="text-center">
            {showVisual && renderVisual()}
            
            <div className="flex items-center justify-center gap-4 mb-6">
              <span className="text-5xl font-black text-white">{problem.num1}</span>
              <span className="text-4xl text-yellow-400">{problem.operation === 'add' ? '+' : '-'}</span>
              <span className="text-5xl font-black text-white">{problem.num2}</span>
              <span className="text-4xl text-white">=</span>
              <span className={`text-5xl font-black ${feedback === 'correct' ? 'text-green-400' : feedback === 'wrong' ? 'text-red-400' : 'text-yellow-400'}`}>
                {feedback ? problem.answer : '?'}
              </span>
            </div>

            <div className="grid grid-cols-4 gap-3">
              {generateOptions().map(opt => (
                <button
                  key={opt}
                  onClick={() => handleAnswer(opt)}
                  disabled={feedback !== null}
                  className={`p-4 rounded-xl text-white text-3xl font-bold transition-all hover:scale-110 ${selectedAnswer === opt ? (feedback === 'correct' ? 'bg-green-500' : 'bg-red-500') : 'bg-gradient-to-r from-emerald-400 to-green-500 hover:from-emerald-500 hover:to-green-600'} disabled:opacity-50 shadow-lg`}
                >
                  {opt}
                </button>
              ))}
            </div>

            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300 text-xl">
                Правильный ответ: {problem.answer}
              </div>
            )}
          </div>
        </div>
      )}

      <div className="flex justify-center mt-4 gap-4">
        <button
          onClick={() => setShowVisual(!showVisual)}
          className={`text-xs px-3 py-1 rounded-full transition-colors ${showVisual ? 'bg-purple-400/30 text-purple-300' : 'bg-white/10 text-white/50 hover:bg-white/20'}`}
        >
          {showVisual ? '🎨 С картинками' : '📝 Без картинок'}
        </button>
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>
    </div>
  )
}
