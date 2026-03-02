'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw } from 'lucide-react'

const OBJECTS = {
  animals: ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🦁', '🐯', '🐮', '🐷', '🐸', '🐵'],
  fruits: ['🍎', '🍐', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🫐', '🍑', '🍒', '🥝', '🍍', '🥭', '🍈'],
  objects: ['⭐', '🌟', '🎈', '🎁', '🎀', '🎯', '🔮', '💎', '🌸', '🌺', '🌻', '🍀', '🌈', '❤️', '💜'],
  school: ['📚', '✏️', '🖊️', '📐', '📏', '🎨', '🎵', '🎹', '🏀', '⚽', '🎾', '🏆', '🏅', '🥇', '🎒'],
}

type Category = keyof typeof OBJECTS
type GameMode = 'count' | 'compare' | 'more'

export default function CountingGame() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('count')
  const [category, setCategory] = useState<Category>('animals')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  
  // Mode: count
  const [items, setItems] = useState<string[]>([])
  const [correctCount, setCorrectCount] = useState(0)
  
  // Mode: compare
  const [group1, setGroup1] = useState<string[]>([])
  const [group2, setGroup2] = useState<string[]>([])
  const [correctCompare, setCorrectCompare] = useState<'left' | 'right' | 'equal'>('equal')
  
  // Mode: more
  const [moreItems, setMoreItems] = useState<{ items: string[]; target: number } | null>(null)

  const shuffleArray = <T,>(arr: T[]): T[] => [...arr].sort(() => Math.random() - 0.5)

  const generateCountQuestion = () => {
    const count = Math.floor(Math.random() * 10) + 1
    const object = OBJECTS[category][Math.floor(Math.random() * OBJECTS[category].length)]
    setItems(Array(count).fill(object))
    setCorrectCount(count)
  }

  const generateCompareQuestion = () => {
    const obj1 = OBJECTS[category][Math.floor(Math.random() * OBJECTS[category].length)]
    const obj2 = OBJECTS[category].filter(o => o !== obj1)[Math.floor(Math.random() * (OBJECTS[category].length - 1))]
    const count1 = Math.floor(Math.random() * 8) + 1
    const count2 = Math.floor(Math.random() * 8) + 1
    
    setGroup1(Array(count1).fill(obj1))
    setGroup2(Array(count2).fill(obj2))
    
    if (count1 > count2) setCorrectCompare('left')
    else if (count2 > count1) setCorrectCompare('right')
    else setCorrectCompare('equal')
  }

  const generateMoreQuestion = () => {
    const object = OBJECTS[category][Math.floor(Math.random() * OBJECTS[category].length)]
    const count = Math.floor(Math.random() * 5) + 3
    setMoreItems({ items: Array(count).fill(object), target: count })
  }

  useEffect(() => {
    if (mode === 'count') generateCountQuestion()
    else if (mode === 'compare') generateCompareQuestion()
    else generateMoreQuestion()
  }, [mode, category])

  const handleCountAnswer = (answer: number) => {
    const correct = answer === correctCount
    
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
      generateCountQuestion()
    }, 1000)
  }

  const handleCompareAnswer = (answer: 'left' | 'right' | 'equal') => {
    const correct = answer === correctCompare
    
    if (correct) {
      playCorrect()
      setScore(s => s + 15)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(8 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateCompareQuestion()
    }, 1000)
  }

  const handleMoreAnswer = (answer: number) => {
    if (!moreItems) return
    const correct = answer === moreItems.target
    
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
      generateMoreQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'count') generateCountQuestion()
    else if (mode === 'compare') generateCompareQuestion()
    else generateMoreQuestion()
  }

  return (
    <div className="bg-gradient-to-br from-yellow-500/20 to-orange-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">🔢</span> Счёт предметов
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-3">
        {(['count', 'compare', 'more'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-yellow-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'count' ? '🎯 Посчитай' : m === 'compare' ? '⚖️ Сравни' : '➕ Сколько ещё?'}
          </button>
        ))}
      </div>

      <div className="flex gap-2 mb-4">
        {(['animals', 'fruits', 'objects', 'school'] as Category[]).map(c => (
          <button
            key={c}
            onClick={() => { setCategory(c); reset() }}
            className={`flex-1 py-1 rounded-lg text-xs font-medium transition-all ${category === c ? 'bg-orange-500 text-white' : 'bg-white/10 text-white/50 hover:bg-white/20'}`}
          >
            {c === 'animals' ? '🐾 Животные' : c === 'fruits' ? '🍎 Фрукты' : c === 'objects' ? '✨ Разное' : '🎒 Школа'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'count' && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Сколько предметов?</div>
            <div className="flex flex-wrap justify-center gap-2 mb-6 min-h-[100px] p-4 bg-white/5 rounded-xl">
              {items.map((item, i) => (
                <span key={i} className="text-4xl animate-bounce" style={{ animationDelay: `${i * 50}ms` }}>{item}</span>
              ))}
            </div>
            <div className="grid grid-cols-5 gap-2">
              {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(n => (
                <button
                  key={n}
                  onClick={() => handleCountAnswer(n)}
                  className={`p-3 rounded-lg text-2xl font-bold transition-all ${feedback && n === correctCount ? 'bg-green-500 text-white' : 'bg-white/10 hover:bg-yellow-500/30 text-white hover:scale-110'}`}
                >
                  {n}
                </button>
              ))}
            </div>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                Правильный ответ: {correctCount}
              </div>
            )}
          </div>
        )}

        {mode === 'compare' && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Где больше предметов?</div>
            <div className="grid grid-cols-3 gap-4 mb-6">
              <div className={`p-4 rounded-xl ${feedback === 'correct' && correctCompare === 'left' ? 'bg-green-500/30 ring-2 ring-green-400' : 'bg-blue-500/20'}`}>
                <div className="text-blue-300 mb-2">Слева</div>
                <div className="flex flex-wrap justify-center gap-1">
                  {group1.map((item, i) => (
                    <span key={i} className="text-3xl">{item}</span>
                  ))}
                </div>
                <div className="text-white font-bold mt-2">{group1.length}</div>
              </div>
              <div className="flex flex-col items-center justify-center">
                <button
                  onClick={() => handleCompareAnswer('equal')}
                  className={`p-3 rounded-lg text-lg font-bold transition-all ${feedback === 'correct' && correctCompare === 'equal' ? 'bg-green-500 text-white' : 'bg-white/10 hover:bg-yellow-500/30 text-white'}`}
                >
                  =
                </button>
              </div>
              <div className={`p-4 rounded-xl ${feedback === 'correct' && correctCompare === 'right' ? 'bg-green-500/30 ring-2 ring-green-400' : 'bg-pink-500/20'}`}>
                <div className="text-pink-300 mb-2">Справа</div>
                <div className="flex flex-wrap justify-center gap-1">
                  {group2.map((item, i) => (
                    <span key={i} className="text-3xl">{item}</span>
                  ))}
                </div>
                <div className="text-white font-bold mt-2">{group2.length}</div>
              </div>
            </div>
            <div className="flex justify-center gap-4">
              <button
                onClick={() => handleCompareAnswer('left')}
                className={`px-8 py-3 rounded-xl font-bold transition-all ${feedback === 'correct' && correctCompare === 'left' ? 'bg-green-500 text-white' : 'bg-gradient-to-r from-blue-500 to-cyan-500 text-white hover:scale-105'}`}
              >
                ⬅️ Слева больше
              </button>
              <button
                onClick={() => handleCompareAnswer('right')}
                className={`px-8 py-3 rounded-xl font-bold transition-all ${feedback === 'correct' && correctCompare === 'right' ? 'bg-green-500 text-white' : 'bg-gradient-to-r from-pink-500 to-rose-500 text-white hover:scale-105'}`}
              >
                Справа больше ➡️
              </button>
            </div>
          </div>
        )}

        {mode === 'more' && moreItems && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Сколько нужно добавить, чтобы стало {moreItems.target + Math.floor(Math.random() * 3) + 1}?</div>
            <div className="flex flex-wrap justify-center gap-2 mb-6 p-4 bg-white/5 rounded-xl">
              {moreItems.items.map((item, i) => (
                <span key={i} className="text-4xl">{item}</span>
              ))}
              {Array(Math.floor(Math.random() * 3) + 1).fill(0).map((_, i) => (
                <span key={`q${i}`} className="text-4xl opacity-30">❓</span>
              ))}
            </div>
            <div className="grid grid-cols-5 gap-2">
              {[0, 1, 2, 3, 4, 5].map(n => (
                <button
                  key={n}
                  onClick={() => handleMoreAnswer(n)}
                  className={`p-3 rounded-lg text-2xl font-bold transition-all ${'bg-white/10 hover:bg-yellow-500/30 text-white hover:scale-110'}`}
                >
                  {n}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>

      <div className="flex justify-center mt-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>

      <div className="mt-4 p-3 bg-white/5 rounded-lg">
        <div className="text-white/60 text-sm">💡 Считай внимательно! Наведи мышкой на каждый предмет.</div>
      </div>
    </div>
  )
}
