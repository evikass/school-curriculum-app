'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { ArrowRightLeft, RotateCcw, Trophy, Target, Zap } from 'lucide-react'

interface AntonymPair {
  word: string
  antonym: string
  difficulty: 'easy' | 'medium' | 'hard'
  category: string
}

const ANTONYMS: AntonymPair[] = [
  // Лёгкий уровень
  { word: 'большой', antonym: 'маленький', difficulty: 'easy', category: 'Размер' },
  { word: 'высокий', antonym: 'низкий', difficulty: 'easy', category: 'Размер' },
  { word: 'длинный', antonym: 'короткий', difficulty: 'easy', category: 'Размер' },
  { word: 'широкий', antonym: 'узкий', difficulty: 'easy', category: 'Размер' },
  { word: 'толстый', antonym: 'тонкий', difficulty: 'easy', category: 'Размер' },
  { word: 'горячий', antonym: 'холодный', difficulty: 'easy', category: 'Температура' },
  { word: 'тёплый', antonym: 'прохладный', difficulty: 'easy', category: 'Температура' },
  { word: 'добрый', antonym: 'злой', difficulty: 'easy', category: 'Характер' },
  { word: 'весёлый', antonym: 'грустный', difficulty: 'easy', category: 'Эмоции' },
  { word: 'быстрый', antonym: 'медленный', difficulty: 'easy', category: 'Скорость' },
  { word: 'светлый', antonym: 'тёмный', difficulty: 'easy', category: 'Цвет' },
  { word: 'белый', antonym: 'чёрный', difficulty: 'easy', category: 'Цвет' },
  { word: 'старый', antonym: 'новый', difficulty: 'easy', category: 'Возраст' },
  { word: 'молодой', antonym: 'старый', difficulty: 'easy', category: 'Возраст' },
  { word: 'тяжёлый', antonym: 'лёгкий', difficulty: 'easy', category: 'Вес' },
  
  // Средний уровень
  { word: 'труд', antonym: 'отдых', difficulty: 'medium', category: 'Деятельность' },
  { word: 'работать', antonym: 'отдыхать', difficulty: 'medium', category: 'Деятельность' },
  { word: 'начало', antonym: 'конец', difficulty: 'medium', category: 'Время' },
  { word: 'утро', antonym: 'вечер', difficulty: 'medium', category: 'Время' },
  { word: 'день', antonym: 'ночь', difficulty: 'medium', category: 'Время' },
  { word: 'лето', antonym: 'зима', difficulty: 'medium', category: 'Время' },
  { word: 'радость', antonym: 'горе', difficulty: 'medium', category: 'Эмоции' },
  { word: 'счастье', antonym: 'несчастье', difficulty: 'medium', category: 'Эмоции' },
  { word: 'любить', antonym: 'ненавидеть', difficulty: 'medium', category: 'Эмоции' },
  { word: 'друг', antonym: 'враг', difficulty: 'medium', category: 'Отношения' },
  { word: 'мир', antonym: 'война', difficulty: 'medium', category: 'Отношения' },
  { word: 'правда', antonym: 'ложь', difficulty: 'medium', category: 'Отношения' },
  { word: 'говорить', antonym: 'молчать', difficulty: 'medium', category: 'Действие' },
  { word: 'покупать', antonym: 'продавать', difficulty: 'medium', category: 'Действие' },
  { word: 'брать', antonym: 'давать', difficulty: 'medium', category: 'Действие' },
  
  // Сложный уровень
  { word: 'восход', antonym: 'закат', difficulty: 'hard', category: 'Природа' },
  { word: 'земной', antonym: 'небесный', difficulty: 'hard', category: 'Природа' },
  { word: 'глубокий', antonym: 'мелкий', difficulty: 'hard', category: 'Размер' },
  { word: 'полнота', antonym: 'пустота', difficulty: 'hard', category: 'Состояние' },
  { word: 'щедрый', antonym: 'скупой', difficulty: 'hard', category: 'Характер' },
  { word: 'смелый', antonym: 'трусливый', difficulty: 'hard', category: 'Характер' },
  { word: 'мудрый', antonym: 'глупый', difficulty: 'hard', category: 'Характер' },
  { word: 'ленивый', antonym: 'трудолюбивый', difficulty: 'hard', category: 'Характер' },
  { word: 'скучный', antonym: 'интересный', difficulty: 'hard', category: 'Свойства' },
  { word: 'полезный', antonym: 'вредный', difficulty: 'hard', category: 'Свойства' },
  { word: 'аккуратный', antonym: 'неряшливый', difficulty: 'hard', category: 'Свойства' },
  { word: 'бедный', antonym: 'богатый', difficulty: 'hard', category: 'Состояние' },
  { word: 'здоровый', antonym: 'больной', difficulty: 'hard', category: 'Состояние' },
  { word: 'сильный', antonym: 'слабый', difficulty: 'hard', category: 'Свойства' },
  { word: 'победа', antonym: 'поражение', difficulty: 'hard', category: 'События' },
  { word: 'находить', antonym: 'терять', difficulty: 'hard', category: 'Действие' },
  { word: 'строить', antonym: 'разрушать', difficulty: 'hard', category: 'Действие' },
  { word: 'соединять', antonym: 'разделять', difficulty: 'hard', category: 'Действие' },
  { word: 'подниматься', antonym: 'опускаться', difficulty: 'hard', category: 'Движение' },
  { word: 'входить', antonym: 'выходить', difficulty: 'hard', category: 'Движение' },
]

export default function Antonyms() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentPair, setCurrentPair] = useState<AntonymPair | null>(null)
  const [options, setOptions] = useState<string[]>([])
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null)
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('easy')
  const [usedPairs, setUsedPairs] = useState<Set<number>>(new Set())
  const [mode, setMode] = useState<'menu' | 'game'>('menu')
  const [timer, setTimer] = useState(0)
  const [questionStart, setQuestionStart] = useState(0)

  const getFilteredPairs = useCallback(() => {
    return ANTONYMS.filter(p => p.difficulty === difficulty)
  }, [difficulty])

  const generateOptions = useCallback((pair: AntonymPair) => {
    const filtered = getFilteredPairs()
    const wrongAnswers = filtered
      .filter(p => p.antonym !== pair.antonym)
      .map(p => p.antonym)
      .sort(() => Math.random() - 0.5)
      .slice(0, 3)
    
    const allOptions = [...wrongAnswers, pair.antonym].sort(() => Math.random() - 0.5)
    setOptions(allOptions)
  }, [getFilteredPairs])

  const getNextPair = useCallback(() => {
    const filtered = getFilteredPairs()
    const available = filtered
      .map((p, i) => ({ p, originalIndex: ANTONYMS.indexOf(p) }))
      .filter(item => !usedPairs.has(item.originalIndex))
    
    if (available.length === 0) {
      setGameOver(true)
      return null
    }
    
    const randomIndex = Math.floor(Math.random() * available.length)
    return available[randomIndex].p
  }, [getFilteredPairs, usedPairs])

  useEffect(() => {
    if (mode === 'game' && !currentPair && !gameOver) {
      const pair = getNextPair()
      if (pair) {
        setCurrentPair(pair)
        generateOptions(pair)
        setQuestionStart(Date.now())
      }
    }
  }, [mode, currentPair, gameOver, getNextPair, generateOptions])

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
    setUsedPairs(new Set())
    setGameOver(false)
    setSelectedAnswer(null)
    setShowResult(false)
    setMode('game')
    const filtered = ANTONYMS.filter(p => p.difficulty === diff)
    const randomIndex = Math.floor(Math.random() * filtered.length)
    const pair = filtered[randomIndex]
    setCurrentPair(pair)
    setUsedPairs(new Set([ANTONYMS.indexOf(pair)]))
    generateOptions(pair)
    setQuestionStart(Date.now())
  }

  const handleSelect = (answer: string) => {
    if (!currentPair || showResult) return
    
    setSelectedAnswer(answer)
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = answer === currentPair.antonym
    
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
      const originalIndex = ANTONYMS.indexOf(currentPair)
      const newUsed = new Set(usedPairs).add(originalIndex)
      setUsedPairs(newUsed)
      setSelectedAnswer(null)
      setShowResult(false)
      setTimer(0)
      
      const filtered = ANTONYMS.filter(p => p.difficulty === difficulty)
      const available = filtered.filter(p => !newUsed.has(ANTONYMS.indexOf(p)))
      
      if (available.length === 0) {
        setGameOver(true)
      } else {
        const nextPair = available[Math.floor(Math.random() * available.length)]
        setCurrentPair(nextPair)
        generateOptions(nextPair)
        setQuestionStart(Date.now())
      }
    }, 2000)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentPair(null)
    setGameOver(false)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-fuchsia-900/50 to-pink-900/50 rounded-2xl p-6 backdrop-blur-sm border border-fuchsia-500/30">
        <h2 className="text-2xl font-bold text-fuchsia-300 mb-6 flex items-center gap-2">
          <ArrowRightLeft className="w-7 h-7" />
          Антонимы
        </h2>
        
        <p className="text-fuchsia-200 mb-6">
          Найдите слово с противоположным значением! Антонимы - это слова с противоположным смыслом.
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
                {diff === 'easy' ? '15 пар' : diff === 'medium' ? '15 пар' : '20 пар'}
              </div>
            </button>
          ))}
        </div>
        
        <div className="bg-white/10 rounded-lg p-4">
          <p className="text-fuchsia-300 text-sm text-center">
            Пример: большой ↔ маленький, горячий ↔ холодный
          </p>
        </div>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-fuchsia-900/50 to-pink-900/50 rounded-2xl p-6 backdrop-blur-sm border border-fuchsia-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-fuchsia-300 mb-2">Отлично!</h2>
        <p className="text-fuchsia-200 mb-4">
          Результат: {score} XP за {totalQuestions} вопросов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-fuchsia-500 hover:bg-fuchsia-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-fuchsia-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentPair) return null

  return (
    <div className="bg-gradient-to-br from-fuchsia-900/50 to-pink-900/50 rounded-2xl p-6 backdrop-blur-sm border border-fuchsia-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-fuchsia-300 text-sm flex items-center gap-2">
          <Target className="w-4 h-4" />
          {currentPair.category}
        </div>
        <div className="flex items-center gap-4">
          <span className="text-fuchsia-300 text-sm">{timer.toFixed(1)}с</span>
          <span className="text-fuchsia-300">Серия: {streak}🔥</span>
          <span className="text-fuchsia-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-6 mb-6 text-center">
        <p className="text-fuchsia-300 text-sm mb-2">Найдите антоним к слову:</p>
        <p className="text-3xl font-bold text-white">{currentPair.word}</p>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {options.map((option, index) => {
          const isSelected = selectedAnswer === option
          const isCorrect = option === currentPair.antonym
          
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
              key={index}
              onClick={() => handleSelect(option)}
              disabled={showResult}
              className={`p-4 rounded-xl font-bold border transition-all ${buttonClass}`}
            >
              {option}
            </button>
          )
        })}
      </div>

      {showResult && (
        <div className={`mt-4 p-3 rounded-lg text-center ${
          selectedAnswer === currentPair.antonym
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          {selectedAnswer === currentPair.antonym ? (
            <p className="font-bold">✅ {currentPair.word} ↔ {currentPair.antonym}</p>
          ) : (
            <p className="font-bold">❌ Правильно: {currentPair.word} ↔ {currentPair.antonym}</p>
          )}
        </div>
      )}

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-fuchsia-400">
          Вопрос {totalQuestions + 1} из {getFilteredPairs().length}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-fuchsia-400 hover:text-fuchsia-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
