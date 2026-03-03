'use client'

import { useState, useEffect, useCallback } from 'react'
import { Star, Trophy, RotateCcw, Shuffle, Lightbulb } from 'lucide-react'

interface WordPuzzle {
  word: string
  hint: string
  category: string
}

const WORDS: WordPuzzle[] = [
  { word: 'КРАСИВЫЙ', hint: 'Тот, кто нравится', category: 'Прилагательное' },
  { word: 'БЕЖАТЬ', hint: 'Быстрое движение', category: 'Глагол' },
  { word: 'СОЛНЦЕ', hint: 'Светит на небе', category: 'Существительное' },
  { word: 'ПРИРОДА', hint: 'Мир вокруг нас', category: 'Существительное' },
  { word: 'УЧЕНИК', hint: 'Тот, кто учится', category: 'Существительное' },
  { word: 'ТЕТРАДЬ', hint: 'Для записей', category: 'Существительное' },
  { word: 'КАРАНДАШ', hint: 'Для рисования', category: 'Существительное' },
  { word: 'ПЕРЕМЕН', hint: 'Отдых между уроками', category: 'Существительное' },
  { word: 'УРОЖАЙ', hint: 'Собирают осенью', category: 'Существительное' },
  { word: 'РАДОСТЬ', hint: 'Чувство счастья', category: 'Существительное' },
  { word: 'ВЕСЁЛЫЙ', hint: 'Любит смеяться', category: 'Прилагательное' },
  { word: 'ДРУЖБА', hint: 'Отношения друзей', category: 'Существительное' },
  { word: 'МОРОЗ', hint: 'Холод зимой', category: 'Существительное' },
  { word: 'МЕТЕЛЬ', hint: 'Снежная буря', category: 'Существительное' },
  { word: 'ЛЕСТНИЦ', hint: 'Для подъёма', category: 'Существительное' },
  { word: 'РЕЧЕНИЕ', hint: 'Ответ на задачу', category: 'Существительное' },
  { word: 'ЗДОРОВЫ', hint: 'Не болеет', category: 'Прилагательное' },
  { word: 'ГОРОДСК', hint: 'В городе', category: 'Прилагательное' },
  { word: 'ПЛАВАТЬ', hint: 'В воде', category: 'Глагол' },
  { word: 'САЖАТЬ', hint: 'Растения в землю', category: 'Глагол' },
]

export default function WordBuilderGame() {
  const [currentPuzzle, setCurrentPuzzle] = useState<WordPuzzle | null>(null)
  const [shuffledLetters, setShuffledLetters] = useState<string[]>([])
  const [userLetters, setUserLetters] = useState<string[]>([])
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [bestStreak, setBestStreak] = useState(0)
  const [round, setRound] = useState(0)
  const [totalRounds] = useState(10)
  const [showResult, setShowResult] = useState(false)
  const [isCorrect, setIsCorrect] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [showHint, setShowHint] = useState(false)
  const [hintsUsed, setHintsUsed] = useState(0)

  const shuffleArray = <T,>(array: T[]): T[] => {
    const newArray = [...array]
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[newArray[i], newArray[j]] = [newArray[j], newArray[i]]
    }
    return newArray
  }

  const generatePuzzle = useCallback(() => {
    const puzzle = WORDS[Math.floor(Math.random() * WORDS.length)]
    const letters = puzzle.word.split('')
    const shuffled = shuffleArray(letters)
    
    setCurrentPuzzle(puzzle)
    setShuffledLetters(shuffled)
    setUserLetters([])
    setShowResult(false)
    setShowHint(false)
  }, [])

  useEffect(() => {
    generatePuzzle()
  }, [generatePuzzle])

  const handleLetterClick = (letter: string, index: number) => {
    if (showResult) return
    setUserLetters([...userLetters, { letter, index }])
    setShuffledLetters(shuffledLetters.filter((_, i) => i !== index))
  }

  const handleUserLetterClick = (index: number) => {
    if (showResult) return
    const letter = userLetters[index]
    setUserLetters(userLetters.filter((_, i) => i !== index))
    setShuffledLetters([...shuffledLetters, letter.letter])
  }

  const checkAnswer = () => {
    if (!currentPuzzle) return

    const answer = userLetters.map(l => l.letter).join('')
    const correct = answer === currentPuzzle.word

    setIsCorrect(correct)
    setShowResult(true)

    if (correct) {
      const bonus = showHint ? 0 : 5
      setScore(score + 10 + streak * 2 + bonus)
      setStreak(streak + 1)
      if (streak + 1 > bestStreak) setBestStreak(streak + 1)
    } else {
      setStreak(0)
    }

    setTimeout(() => {
      if (round + 1 >= totalRounds) {
        setGameOver(true)
      } else {
        setRound(round + 1)
        generatePuzzle()
      }
    }, 2000)
  }

  const useHint = () => {
    if (showHint || !currentPuzzle) return
    
    setShowHint(true)
    setHintsUsed(hintsUsed + 1)
    
    // Reveal first letter
    const firstLetterIndex = shuffledLetters.findIndex(l => l === currentPuzzle.word[0])
    if (firstLetterIndex !== -1) {
      handleLetterClick(currentPuzzle.word[0], firstLetterIndex)
    }
  }

  const restartGame = () => {
    setScore(0)
    setStreak(0)
    setRound(0)
    setHintsUsed(0)
    setGameOver(false)
    generatePuzzle()
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-emerald-900/80 to-teal-900/80 rounded-2xl p-6 backdrop-blur-xl border border-white/20">
        <div className="text-center">
          <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-white mb-2">Молодец!</h2>
          <div className="space-y-2 mb-6">
            <p className="text-3xl font-bold text-yellow-400">{score} очков</p>
            <p className="text-white/80">Лучшая серия: {bestStreak} 🔥</p>
            <p className="text-white/60">Подсказок использовано: {hintsUsed}</p>
          </div>
          <button
            onClick={restartGame}
            className="px-6 py-3 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl text-white font-bold hover:from-green-600 hover:to-emerald-600 transition-all flex items-center gap-2 mx-auto"
          >
            <RotateCcw className="w-5 h-5" />
            Играть снова
          </button>
        </div>
      </div>
    )
  }

  if (!currentPuzzle) return null

  return (
    <div className="bg-gradient-to-br from-emerald-900/80 to-teal-900/80 rounded-2xl p-6 backdrop-blur-xl border border-white/20">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <span className="text-2xl">🔤</span>
          <h2 className="text-xl font-bold text-white">Собери слово</h2>
        </div>
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-1 text-yellow-400">
            <Star className="w-5 h-5 fill-current" />
            <span className="font-bold">{score}</span>
          </div>
          <div className="text-white/60 text-sm">
            {round + 1}/{totalRounds}
          </div>
        </div>
      </div>

      {/* Category & Hint */}
      <div className="bg-white/10 rounded-xl p-4 mb-6">
        <div className="flex items-center justify-between mb-2">
          <span className="px-3 py-1 bg-teal-500/20 text-teal-300 rounded-full text-sm">
            {currentPuzzle.category}
          </span>
          <button
            onClick={useHint}
            disabled={showHint || showResult}
            className="flex items-center gap-1 px-3 py-1 bg-yellow-500/20 text-yellow-300 rounded-full text-sm hover:bg-yellow-500/30 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <Lightbulb className="w-4 h-4" />
            Подсказка
          </button>
        </div>
        <p className="text-white/80">{currentPuzzle.hint}</p>
      </div>

      {/* User's answer area */}
      <div className="mb-6">
        <p className="text-white/60 text-sm mb-2">Твой ответ:</p>
        <div className="min-h-[60px] bg-white/5 rounded-xl p-4 flex flex-wrap gap-2 justify-center">
          {userLetters.length === 0 ? (
            <span className="text-white/40">Нажми на буквы ниже</span>
          ) : (
            userLetters.map((letter, index) => (
              <button
                key={index}
                onClick={() => handleUserLetterClick(index)}
                className="w-12 h-12 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl text-white text-xl font-bold 
                           hover:from-purple-600 hover:to-pink-600 transition-all shadow-lg"
              >
                {letter.letter}
              </button>
            ))
          )}
        </div>
      </div>

      {/* Shuffled letters */}
      <div className="mb-6">
        <p className="text-white/60 text-sm mb-2">Доступные буквы:</p>
        <div className="flex flex-wrap gap-2 justify-center min-h-[60px] bg-white/5 rounded-xl p-4">
          {shuffledLetters.map((letter, index) => (
            <button
              key={index}
              onClick={() => handleLetterClick(letter, index)}
              disabled={showResult}
              className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-500 rounded-xl text-white text-xl font-bold 
                         hover:from-indigo-600 hover:to-purple-600 transition-all shadow-lg disabled:opacity-50"
            >
              {letter}
            </button>
          ))}
        </div>
      </div>

      {/* Action buttons */}
      <div className="flex gap-3 mb-4">
        <button
          onClick={() => {
            setShuffledLetters([...shuffledLetters, ...userLetters.map(l => l.letter)])
            setUserLetters([])
          }}
          disabled={userLetters.length === 0 || showResult}
          className="flex-1 py-3 bg-white/10 rounded-xl text-white font-medium hover:bg-white/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
        >
          <RotateCcw className="w-5 h-5" />
          Сброс
        </button>
        <button
          onClick={() => setShuffledLetters(shuffleArray(shuffledLetters))}
          disabled={shuffledLetters.length === 0 || showResult}
          className="flex-1 py-3 bg-white/10 rounded-xl text-white font-medium hover:bg-white/20 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
        >
          <Shuffle className="w-5 h-5" />
          Перемешать
        </button>
      </div>

      <button
        onClick={checkAnswer}
        disabled={userLetters.length !== currentPuzzle.word.length || showResult}
        className="w-full py-3 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl text-white font-bold
                   hover:from-green-600 hover:to-emerald-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
      >
        Проверить
      </button>

      {/* Result */}
      {showResult && (
        <div className={`mt-4 p-4 rounded-xl ${isCorrect ? 'bg-green-500/20' : 'bg-red-500/20'}`}>
          <div className="flex items-center gap-2">
            {isCorrect ? (
              <>
                <span className="text-2xl">✅</span>
                <div>
                  <p className="text-green-300 font-bold">Правильно!</p>
                  <p className="text-white/60 text-sm">
                    +{10 + streak * 2 + (showHint ? 0 : 5)} очков
                  </p>
                </div>
              </>
            ) : (
              <>
                <span className="text-2xl">❌</span>
                <div>
                  <p className="text-red-300 font-bold">Неверно</p>
                  <p className="text-white">
                    Правильный ответ: <span className="font-bold">{currentPuzzle.word}</span>
                  </p>
                </div>
              </>
            )}
          </div>
        </div>
      )}

      {/* Streak indicator */}
      {streak > 0 && !showResult && (
        <div className="mt-4 text-center">
          <span className="px-3 py-1 bg-orange-500/20 text-orange-300 rounded-full text-sm font-medium">
            🔥 Серия: {streak}
          </span>
        </div>
      )}
    </div>
  )
}
