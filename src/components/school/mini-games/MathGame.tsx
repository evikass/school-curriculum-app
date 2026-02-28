'use client'

import { useState, useEffect, useCallback } from 'react'
import { motion } from 'framer-motion'
import { Star } from 'lucide-react'

export function MathGame({ onComplete }: { onComplete: (score: number) => void }) {
  const [num1, setNum1] = useState(0)
  const [num2, setNum2] = useState(0)
  const [operator, setOperator] = useState<'+' | '-' | '×'>('+')
  const [options, setOptions] = useState<number[]>([])
  const [correct, setCorrect] = useState(0)
  const [score, setScore] = useState(0)
  const [round, setRound] = useState(1)
  const totalRounds = 10
  
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
      <div className="mb-4 flex justify-between items-center">
        <span className="text-white/50">Раунд {round}/{totalRounds}</span>
        <span className="text-yellow-400 font-bold flex items-center gap-1">
          <Star className="w-4 h-4" /> {score}
        </span>
      </div>
      
      <div className="text-5xl font-black text-white mb-8">
        {num1} {operator} {num2} = ?
      </div>
      
      <div className="grid grid-cols-2 gap-3">
        {options.map((opt, idx) => (
          <motion.button
            key={idx}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => handleAnswer(opt)}
            className="py-4 px-6 bg-white/10 hover:bg-white/20 rounded-2xl text-2xl font-bold text-white border-2 border-white/20 transition-all"
          >
            {opt}
          </motion.button>
        ))}
      </div>
    </div>
  )
}
