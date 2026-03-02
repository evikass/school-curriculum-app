'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw, Zap } from 'lucide-react'

type GameMode = 'classify' | 'count' | 'sequence'

export default function EvenOdd() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('classify')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  
  // Mode: classify
  const [currentNumber, setCurrentNumber] = useState(0)
  
  // Mode: count
  const [groupNumbers, setGroupNumbers] = useState<number[]>([])
  const [countAnswer, setCountAnswer] = useState<{ even: number | null; odd: number | null }>({ even: null, odd: null })
  
  // Mode: sequence
  const [sequence, setSequence] = useState<number[]>([])
  const [missingIndex, setMissingIndex] = useState(0)
  const [correctAnswer, setCorrectAnswer] = useState(0)

  const generateClassifyQuestion = () => {
    setCurrentNumber(Math.floor(Math.random() * 100) + 1)
  }

  const generateCountQuestion = () => {
    const count = Math.floor(Math.random() * 5) + 4 // 4-8 numbers
    const nums: number[] = []
    for (let i = 0; i < count; i++) {
      nums.push(Math.floor(Math.random() * 20) + 1)
    }
    setGroupNumbers(nums)
    setCountAnswer({ even: null, odd: null })
  }

  const generateSequenceQuestion = () => {
    const start = Math.floor(Math.random() * 10) + 1
    const isEven = Math.random() > 0.5
    const seq: number[] = []
    for (let i = 0; i < 5; i++) {
      seq.push(start + (isEven ? i * 2 : i * 2 + 1))
    }
    const missing = Math.floor(Math.random() * 5)
    setCorrectAnswer(seq[missing])
    seq[missing] = 0
    setSequence(seq)
    setMissingIndex(missing)
  }

  useEffect(() => {
    if (mode === 'classify') generateClassifyQuestion()
    else if (mode === 'count') generateCountQuestion()
    else generateSequenceQuestion()
  }, [mode])

  const handleClassifyAnswer = (isEven: boolean) => {
    const correct = (currentNumber % 2 === 0) === isEven
    
    if (correct) {
      playCorrect()
      setScore(s => s + 10)
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
      generateClassifyQuestion()
    }, 800)
  }

  const handleCountSubmit = () => {
    const evenCount = groupNumbers.filter(n => n % 2 === 0).length
    const oddCount = groupNumbers.filter(n => n % 2 !== 0).length
    
    if (countAnswer.even === evenCount && countAnswer.odd === oddCount) {
      playCorrect()
      setScore(s => s + 25)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(12 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateCountQuestion()
    }, 1200)
  }

  const handleSequenceAnswer = (answer: number) => {
    if (answer === correctAnswer) {
      playCorrect()
      setScore(s => s + 20)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(10 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateSequenceQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'classify') generateClassifyQuestion()
    else if (mode === 'count') generateCountQuestion()
    else generateSequenceQuestion()
  }

  return (
    <div className="bg-gradient-to-br from-cyan-500/20 to-blue-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">🔢</span> Чётные и Нечётные
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4">
        {(['classify', 'count', 'sequence'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-cyan-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'classify' ? '🎯 Определи' : m === 'count' ? '📊 Посчитай' : '➡️ Продолжи ряд'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'classify' && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Это число чётное или нечётное?</div>
            <div className={`text-8xl font-black mb-6 ${feedback === 'correct' ? 'text-green-400' : feedback === 'wrong' ? 'text-red-400' : 'text-white'}`}>
              {currentNumber}
            </div>
            <div className="flex justify-center gap-4">
              <button
                onClick={() => handleClassifyAnswer(true)}
                className="px-10 py-5 bg-gradient-to-r from-green-400 to-emerald-500 rounded-xl text-white font-bold text-2xl hover:scale-105 transition-transform shadow-lg"
              >
                Чётное
              </button>
              <button
                onClick={() => handleClassifyAnswer(false)}
                className="px-10 py-5 bg-gradient-to-r from-orange-400 to-red-500 rounded-xl text-white font-bold text-2xl hover:scale-105 transition-transform shadow-lg"
              >
                Нечётное
              </button>
            </div>
          </div>
        )}

        {mode === 'count' && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Сколько чётных и нечётных чисел?</div>
            <div className="flex flex-wrap gap-3 justify-center mb-6">
              {groupNumbers.map((n, i) => (
                <span
                  key={i}
                  className={`w-12 h-12 flex items-center justify-center rounded-lg text-xl font-bold ${n % 2 === 0 ? 'bg-green-500/30 text-green-300' : 'bg-orange-500/30 text-orange-300'}`}
                >
                  {n}
                </span>
              ))}
            </div>
            <div className="flex justify-center gap-6 mb-4">
              <div className="flex flex-col items-center gap-2">
                <span className="text-green-300">Чётных:</span>
                <div className="flex gap-1">
                  {[0, 1, 2, 3, 4, 5, 6, 7, 8].map(n => (
                    <button
                      key={n}
                      onClick={() => setCountAnswer({ ...countAnswer, even: n })}
                      className={`w-8 h-8 rounded text-sm font-bold transition-all ${countAnswer.even === n ? 'bg-green-500 text-white' : 'bg-green-500/20 text-green-300 hover:bg-green-500/40'}`}
                    >
                      {n}
                    </button>
                  ))}
                </div>
              </div>
              <div className="flex flex-col items-center gap-2">
                <span className="text-orange-300">Нечётных:</span>
                <div className="flex gap-1">
                  {[0, 1, 2, 3, 4, 5, 6, 7, 8].map(n => (
                    <button
                      key={n}
                      onClick={() => setCountAnswer({ ...countAnswer, odd: n })}
                      className={`w-8 h-8 rounded text-sm font-bold transition-all ${countAnswer.odd === n ? 'bg-orange-500 text-white' : 'bg-orange-500/20 text-orange-300 hover:bg-orange-500/40'}`}
                    >
                      {n}
                    </button>
                  ))}
                </div>
              </div>
            </div>
            <button
              onClick={handleCountSubmit}
              disabled={countAnswer.even === null || countAnswer.odd === null}
              className="px-8 py-3 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-xl text-white font-bold hover:scale-105 transition-transform disabled:opacity-50"
            >
              Проверить
            </button>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                Правильно: {groupNumbers.filter(n => n % 2 === 0).length} чётных, {groupNumbers.filter(n => n % 2 !== 0).length} нечётных
              </div>
            )}
          </div>
        )}

        {mode === 'sequence' && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Какое число пропущено?</div>
            <div className="flex justify-center gap-2 mb-6">
              {sequence.map((n, i) => (
                <div
                  key={i}
                  className={`w-16 h-16 flex items-center justify-center rounded-lg text-2xl font-bold ${i === missingIndex ? 'bg-yellow-500/30 border-2 border-yellow-400 border-dashed text-yellow-400' : 'bg-white/10 text-white'}`}
                >
                  {n === 0 ? '?' : n}
                </div>
              ))}
            </div>
            <div className="flex justify-center gap-2 flex-wrap">
              {[correctAnswer - 4, correctAnswer - 2, correctAnswer - 1, correctAnswer, correctAnswer + 1, correctAnswer + 2, correctAnswer + 4]
                .filter(n => n > 0 && !sequence.includes(n))
                .sort(() => Math.random() - 0.5)
                .slice(0, 5)
                .map(n => (
                  <button
                    key={n}
                    onClick={() => handleSequenceAnswer(n)}
                    className="w-14 h-14 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-lg text-white text-xl font-bold hover:scale-110 transition-transform"
                  >
                    {n}
                  </button>
                ))}
              <button
                onClick={() => handleSequenceAnswer(correctAnswer)}
                className="w-14 h-14 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-lg text-white text-xl font-bold hover:scale-110 transition-transform"
              >
                {correctAnswer}
              </button>
            </div>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                Правильный ответ: {correctAnswer}
              </div>
            )}
          </div>
        )}
      </div>

      <div className="flex justify-center mt-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>

      <div className="mt-4 p-3 bg-white/5 rounded-lg">
        <div className="text-white/60 text-sm mb-2">💡 Запомни:</div>
        <div className="grid grid-cols-2 gap-3 text-sm">
          <div className="text-center p-2 bg-green-500/20 rounded-lg">
            <div className="font-bold text-green-300">Чётные (÷2)</div>
            <div className="text-white/70">2, 4, 6, 8, 10...</div>
          </div>
          <div className="text-center p-2 bg-orange-500/20 rounded-lg">
            <div className="font-bold text-orange-300">Нечётные</div>
            <div className="text-white/70">1, 3, 5, 7, 9...</div>
          </div>
        </div>
      </div>
    </div>
  )
}
