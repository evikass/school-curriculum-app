'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw, Zap } from 'lucide-react'

const ELEMENTS = [
  { symbol: 'H', name: 'Водород', number: 1, mass: 1 },
  { symbol: 'He', name: 'Гелий', number: 2, mass: 4 },
  { symbol: 'Li', name: 'Литий', number: 3, mass: 7 },
  { symbol: 'Be', name: 'Бериллий', number: 4, mass: 9 },
  { symbol: 'B', name: 'Бор', number: 5, mass: 11 },
  { symbol: 'C', name: 'Углерод', number: 6, mass: 12 },
  { symbol: 'N', name: 'Азот', number: 7, mass: 14 },
  { symbol: 'O', name: 'Кислород', number: 8, mass: 16 },
  { symbol: 'F', name: 'Фтор', number: 9, mass: 19 },
  { symbol: 'Ne', name: 'Неон', number: 10, mass: 20 },
  { symbol: 'Na', name: 'Натрий', number: 11, mass: 23 },
  { symbol: 'Mg', name: 'Магний', number: 12, mass: 24 },
  { symbol: 'Al', name: 'Алюминий', number: 13, mass: 27 },
  { symbol: 'Si', name: 'Кремний', number: 14, mass: 28 },
  { symbol: 'P', name: 'Фосфор', number: 15, mass: 31 },
  { symbol: 'S', name: 'Сера', number: 16, mass: 32 },
  { symbol: 'Cl', name: 'Хлор', number: 17, mass: 35 },
  { symbol: 'Ar', name: 'Аргон', number: 18, mass: 40 },
  { symbol: 'K', name: 'Калий', number: 19, mass: 39 },
  { symbol: 'Ca', name: 'Кальций', number: 20, mass: 40 },
  { symbol: 'Fe', name: 'Железо', number: 26, mass: 56 },
  { symbol: 'Cu', name: 'Медь', number: 29, mass: 64 },
  { symbol: 'Zn', name: 'Цинк', number: 30, mass: 65 },
  { symbol: 'Ag', name: 'Серебро', number: 47, mass: 108 },
  { symbol: 'Au', name: 'Золото', number: 79, mass: 197 },
]

const GROUPS: Record<string, string[]> = {
  'Щелочные металлы': ['Li', 'Na', 'K'],
  'Щёлочноземельные металлы': ['Be', 'Mg', 'Ca'],
  'Галогены': ['F', 'Cl'],
  'Благородные газы': ['He', 'Ne', 'Ar'],
  'Металлы': ['Fe', 'Cu', 'Zn', 'Ag', 'Au'],
  'Неметаллы': ['H', 'C', 'N', 'O', 'P', 'S'],
}

type GameMode = 'symbol' | 'number' | 'name' | 'group'

export default function PeriodicTableGame() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('symbol')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  
  const [currentElement, setCurrentElement] = useState<typeof ELEMENTS[0] | null>(null)
  const [questionType, setQuestionType] = useState<'symbol' | 'name' | 'number'>('symbol')

  const shuffleArray = <T,>(arr: T[]): T[] => [...arr].sort(() => Math.random() - 0.5)

  const generateQuestion = () => {
    const element = ELEMENTS[Math.floor(Math.random() * ELEMENTS.length)]
    setCurrentElement(element)
    const types: ('symbol' | 'name' | 'number')[] = ['symbol', 'name', 'number']
    setQuestionType(types[Math.floor(Math.random() * types.length)])
  }

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    generateQuestion()
  }, [mode])

  const handleSymbolAnswer = (answer: string) => {
    if (!currentElement) return
    const correct = answer === currentElement.symbol

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
      generateQuestion()
    }, 1000)
  }

  const handleGroupAnswer = (group: string) => {
    if (!currentElement) return
    const correct = GROUPS[group]?.includes(currentElement.symbol)

    if (correct) {
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
      generateQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    generateQuestion()
  }

  const getOptions = () => {
    if (!currentElement) return []
    const correct = questionType === 'symbol' ? currentElement.symbol :
                    questionType === 'name' ? currentElement.name : 
                    currentElement.number.toString()
    
    const allOptions = questionType === 'symbol' ? ELEMENTS.map(e => e.symbol) :
                       questionType === 'name' ? ELEMENTS.map(e => e.name) :
                       ELEMENTS.map(e => e.number.toString())
    
    const wrongOptions = allOptions.filter(o => o !== correct)
    const selected = shuffleArray(wrongOptions).slice(0, 3)
    return shuffleArray([correct, ...selected])
  }

  return (
    <div className="bg-gradient-to-br from-cyan-500/20 to-blue-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">⚛️</span> Таблица Менделеева
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4">
        {(['symbol', 'number', 'name', 'group'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-cyan-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'symbol' ? '🔣 Символ' : m === 'number' ? '🔢 Номер' : m === 'name' ? '📝 Название' : '🏷️ Группа'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode !== 'group' && currentElement && (
          <div className="text-center">
            {questionType === 'symbol' && (
              <>
                <div className="mb-4 text-white/60">Какой символ у элемента?</div>
                <div className="text-4xl font-bold text-white mb-6 p-4 bg-white/10 rounded-xl">
                  {currentElement.name}
                </div>
              </>
            )}
            {questionType === 'name' && (
              <>
                <div className="mb-4 text-white/60">Как называется этот элемент?</div>
                <div className={`text-6xl font-black mb-6 ${feedback === 'correct' ? 'text-green-400' : feedback === 'wrong' ? 'text-red-400' : 'text-yellow-300'}`}>
                  {currentElement.symbol}
                </div>
              </>
            )}
            {questionType === 'number' && (
              <>
                <div className="mb-4 text-white/60">Какой порядковый номер?</div>
                <div className="text-4xl font-bold text-white mb-6">
                  {currentElement.symbol} ({currentElement.name})
                </div>
              </>
            )}
            
            <div className="grid grid-cols-2 gap-3">
              {getOptions().map((opt, i) => (
                <button
                  key={i}
                  onClick={() => handleSymbolAnswer(opt.toString())}
                  className="p-4 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform"
                >
                  {opt}
                </button>
              ))}
            </div>
          </div>
        )}

        {mode === 'group' && currentElement && (
          <div className="text-center">
            <div className="mb-4 text-white/60">К какой группе относится?</div>
            <div className={`text-6xl font-black mb-6 ${feedback === 'correct' ? 'text-green-400' : feedback === 'wrong' ? 'text-red-400' : 'text-yellow-300'}`}>
              {currentElement.symbol}
            </div>
            <div className="text-xl text-white mb-6">{currentElement.name}</div>
            <div className="grid grid-cols-2 gap-3">
              {Object.keys(GROUPS).map(group => (
                <button
                  key={group}
                  onClick={() => handleGroupAnswer(group)}
                  className="p-4 bg-gradient-to-r from-purple-500 to-pink-500 rounded-xl text-white font-bold hover:scale-105 transition-transform"
                >
                  {group}
                </button>
              ))}
            </div>
          </div>
        )}

        {feedback === 'wrong' && currentElement && mode === 'group' && (
          <div className="mt-4 text-yellow-300">
            {currentElement.symbol} — {Object.entries(GROUPS).find(([, v]) => v.includes(currentElement.symbol))?.[0] || 'Не в группе'}
          </div>
        )}
      </div>

      <div className="flex justify-center mt-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>

      <div className="mt-4 p-3 bg-white/5 rounded-lg overflow-x-auto">
        <div className="text-white/60 text-sm mb-2">⚛️ Периодическая таблица (первые 20):</div>
        <div className="flex gap-1 flex-wrap text-xs">
          {ELEMENTS.slice(0, 20).map(e => (
            <span key={e.symbol} className="px-2 py-1 bg-white/10 rounded text-white">
              {e.symbol}
            </span>
          ))}
        </div>
      </div>
    </div>
  )
}
