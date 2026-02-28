'use client'

import { useState, useEffect, useCallback } from 'react'
import { Star } from 'lucide-react'

// ===== MATH GAME =====
export function MathGame({ onComplete }: { onComplete: (score: number) => void }) {
  const [num1, setNum1] = useState(0)
  const [num2, setNum2] = useState(0)
  const [operator, setOperator] = useState<'+' | '-' | '×'>('+')
  const [options, setOptions] = useState<number[]>([])
  const [correct, setCorrect] = useState(0)
  const [score, setScore] = useState(0)
  const [round, setRound] = useState(1)
  const totalRounds = 5
  
  const generateProblem = useCallback(() => {
    const ops: ('+' | '-' | '×')[] = ['+', '-', '×']
    const op = ops[Math.floor(Math.random() * 3)]
    let n1, n2, answer
    
    if (op === '×') {
      n1 = Math.floor(Math.random() * 9) + 2
      n2 = Math.floor(Math.random() * 9) + 2
      answer = n1 * n2
    } else if (op === '+') {
      n1 = Math.floor(Math.random() * 50) + 10
      n2 = Math.floor(Math.random() * 50) + 10
      answer = n1 + n2
    } else {
      n1 = Math.floor(Math.random() * 50) + 30
      n2 = Math.floor(Math.random() * 30) + 1
      answer = n1 - n2
    }
    
    setNum1(n1)
    setNum2(n2)
    setOperator(op)
    setCorrect(answer)
    
    const opts = [answer]
    while (opts.length < 4) {
      const wrong = answer + Math.floor(Math.random() * 20) - 10
      if (wrong !== answer && wrong > 0 && !opts.includes(wrong)) opts.push(wrong)
    }
    setOptions(opts.sort(() => Math.random() - 0.5))
  }, [])

  // eslint-disable-next-line react-hooks/set-state-in-effect
  useEffect(() => { generateProblem() }, [generateProblem])
  
  const handleAnswer = (answer: number) => {
    const newScore = answer === correct ? score + 10 : score
    setScore(newScore)
    
    if (round < totalRounds) {
      setRound(r => r + 1)
      generateProblem()
    } else {
      onComplete(newScore)
    }
  }
  
  return (
    <div className="text-center">
      <div className="mb-3 flex justify-between items-center">
        <span className="text-white/50 text-sm">Раунд {round}/{totalRounds}</span>
        <span className="text-yellow-400 font-bold flex items-center gap-1 text-sm">
          <Star className="w-4 h-4" /> {score}
        </span>
      </div>
      <div className="text-4xl font-black text-white mb-6">{num1} {operator} {num2} = ?</div>
      <div className="grid grid-cols-2 gap-2">
        {options.map((opt, idx) => (
          <button key={idx} onClick={() => handleAnswer(opt)}
            className="py-3 px-4 bg-white/10 hover:bg-white/20 rounded-xl text-xl font-bold text-white border border-white/20 transition-all">
            {opt}
          </button>
        ))}
      </div>
    </div>
  )
}

// ===== MEMORY GAME =====
export function MemoryGame({ onComplete }: { onComplete: (score: number) => void }) {
  const [sequence, setSequence] = useState<number[]>([])
  const [playerSeq, setPlayerSeq] = useState<number[]>([])
  const [showingSeq, setShowingSeq] = useState(true)
  const [activeTile, setActiveTile] = useState<number | null>(null)
  const [score, setScore] = useState(0)
  const [level, setLevel] = useState(1)
  
  useEffect(() => {
    const newSeq = [...sequence, Math.floor(Math.random() * 9)]
    setSequence(newSeq)
    setPlayerSeq([])
    
    let idx = 0
    const showInterval = setInterval(() => {
      if (idx < newSeq.length) {
        setActiveTile(newSeq[idx])
        setTimeout(() => setActiveTile(null), 400)
        idx++
      } else {
        setShowingSeq(false)
        clearInterval(showInterval)
      }
    }, 600)
    
    return () => clearInterval(showInterval)
  }, [level])
  
  const handleTileClick = (tile: number) => {
    if (showingSeq) return
    
    const newPlayerSeq = [...playerSeq, tile]
    setPlayerSeq(newPlayerSeq)
    
    if (newPlayerSeq[newPlayerSeq.length - 1] !== sequence[newPlayerSeq.length - 1]) {
      onComplete(score)
      return
    }
    
    if (newPlayerSeq.length === sequence.length) {
      const newScore = score + level * 10
      setScore(newScore)
      if (level < 5) {
        setLevel(l => l + 1)
        setShowingSeq(true)
      } else {
        onComplete(newScore + level * 10)
      }
    }
  }
  
  return (
    <div className="text-center">
      <div className="mb-3 flex justify-between items-center">
        <span className="text-white/50 text-sm">Уровень {level}/5</span>
        <span className="text-yellow-400 font-bold text-sm">Очки: {score}</span>
      </div>
      <p className="text-white mb-3 text-sm">{showingSeq ? 'Запомни...' : 'Повтори!'}</p>
      <div className="grid grid-cols-3 gap-2">
        {Array.from({ length: 9 }, (_, i) => (
          <button key={i} onClick={() => handleTileClick(i)} disabled={showingSeq}
            className={`aspect-square rounded-xl transition-all ${activeTile === i ? 'bg-yellow-400' : 'bg-white/10 hover:bg-white/20 border border-white/20'}`}>
            <span className={`text-lg font-bold ${activeTile === i ? 'text-purple-900' : 'text-white/30'}`}>{i + 1}</span>
          </button>
        ))}
      </div>
    </div>
  )
}
