'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { Volume2, RotateCcw, Trophy, Target, AlertCircle, BookOpen } from 'lucide-react'

interface WordData {
  word: string
  stressedIndex: number
  stressedWord: string
  difficulty: 'easy' | 'medium' | 'hard'
  explanation?: string
}

const WORDS: WordData[] = [
  // Лёгкий уровень - простые слова
  { word: 'мама', stressedIndex: 0, stressedWord: 'мАма', difficulty: 'easy' },
  { word: 'папа', stressedIndex: 0, stressedWord: 'пАпа', difficulty: 'easy' },
  { word: 'вода', stressedIndex: 1, stressedWord: 'водА', difficulty: 'easy' },
  { word: 'рука', stressedIndex: 1, stressedWord: 'рукА', difficulty: 'easy' },
  { word: 'нога', stressedIndex: 1, stressedWord: 'ногА', difficulty: 'easy' },
  { word: 'луна', stressedIndex: 1, stressedWord: 'лунА', difficulty: 'easy' },
  { word: 'весна', stressedIndex: 0, stressedWord: 'вЕсна', difficulty: 'easy' },
  { word: 'река', stressedIndex: 0, stressedWord: 'рЕка', difficulty: 'easy' },
  { word: 'окно', stressedIndex: 1, stressedWord: 'окнО', difficulty: 'easy' },
  { word: 'море', stressedIndex: 0, stressedWord: 'мОре', difficulty: 'easy' },
  { word: 'лес', stressedIndex: 0, stressedWord: 'лЕс', difficulty: 'easy' },
  { word: 'кот', stressedIndex: 0, stressedWord: 'кОт', difficulty: 'easy' },
  { word: 'дом', stressedIndex: 0, stressedWord: 'дОм', difficulty: 'easy' },
  { word: 'сад', stressedIndex: 0, stressedWord: 'сАд', difficulty: 'easy' },
  { word: 'шар', stressedIndex: 0, stressedWord: 'шАр', difficulty: 'easy' },
  
  // Средний уровень - слова с особенностями
  { word: 'молоко', stressedIndex: 2, stressedWord: 'молокО', difficulty: 'medium' },
  { word: 'собака', stressedIndex: 1, stressedWord: 'собАка', difficulty: 'medium' },
  { word: 'машина', stressedIndex: 1, stressedWord: 'машИна', difficulty: 'medium' },
  { word: 'картина', stressedIndex: 1, stressedWord: 'картИна', difficulty: 'medium' },
  { word: 'работа', stressedIndex: 1, stressedWord: 'рабОта', difficulty: 'medium' },
  { word: 'погода', stressedIndex: 1, stressedWord: 'погОда', difficulty: 'medium' },
  { word: 'дорога', stressedIndex: 1, stressedWord: 'дорОга', difficulty: 'medium' },
  { word: 'хорошо', stressedIndex: 2, stressedWord: 'хорошО', difficulty: 'medium' },
  { word: 'ворона', stressedIndex: 1, stressedWord: 'ворОна', difficulty: 'medium' },
  { word: 'корова', stressedIndex: 1, stressedWord: 'корОва', difficulty: 'medium' },
  { word: 'берёза', stressedIndex: 1, stressedWord: 'берЁза', difficulty: 'medium' },
  { word: 'ягода', stressedIndex: 0, stressedWord: 'Ягода', difficulty: 'medium' },
  { word: 'телефон', stressedIndex: 2, stressedWord: 'телефОн', difficulty: 'medium' },
  { word: 'апельсин', stressedIndex: 2, stressedWord: 'апельсИн', difficulty: 'medium' },
  { word: 'магазин', stressedIndex: 2, stressedWord: 'магазИн', difficulty: 'medium' },
  
  // Сложный уровень - трудные случаи
  { word: 'звонит', stressedIndex: 1, stressedWord: 'звонИт', difficulty: 'hard', explanation: 'Глаголы на -ить имеют ударение на окончании' },
  { word: 'позвонишь', stressedIndex: 3, stressedWord: 'позвонИшь', difficulty: 'hard', explanation: 'В форме 2 лица ударение на окончании' },
  { word: 'красивее', stressedIndex: 2, stressedWord: 'красИвее', difficulty: 'hard', explanation: 'В сравнительной степени ударение на И' },
  { word: 'свёкла', stressedIndex: 0, stressedWord: 'свЁкла', difficulty: 'hard' },
  { word: 'торты', stressedIndex: 0, stressedWord: 'тОрты', difficulty: 'hard', explanation: 'Множественное число, ударение на первом слоге' },
  { word: 'шофёр', stressedIndex: 2, stressedWord: 'шофЁр', difficulty: 'hard' },
  { word: 'договор', stressedIndex: 2, stressedWord: 'договОр', difficulty: 'hard' },
  { word: 'каталог', stressedIndex: 2, stressedWord: 'каталОг', difficulty: 'hard' },
  { word: 'диалог', stressedIndex: 2, stressedWord: 'диалОг', difficulty: 'hard' },
  { word: 'столяр', stressedIndex: 2, stressedWord: 'столЯр', difficulty: 'hard' },
  { word: 'фарфор', stressedIndex: 2, stressedWord: 'фарфОр', difficulty: 'hard' },
  { word: 'цемент', stressedIndex: 2, stressedWord: 'цемЕнт', difficulty: 'hard' },
  { word: 'портфель', stressedIndex: 2, stressedWord: 'портфЕль', difficulty: 'hard' },
  { word: 'щавель', stressedIndex: 1, stressedWord: 'щавЕль', difficulty: 'hard' },
  { word: 'баловать', stressedIndex: 2, stressedWord: 'балОвать', difficulty: 'hard', explanation: 'Инфинитив, ударение на О' },
  { word: 'баловаться', stressedIndex: 2, stressedWord: 'балОваться', difficulty: 'hard' },
  { word: 'облегчить', stressedIndex: 2, stressedWord: 'облЕгчить', difficulty: 'hard' },
  { word: 'углубить', stressedIndex: 2, stressedWord: 'углУбить', difficulty: 'hard' },
  { word: 'украинский', stressedIndex: 1, stressedWord: 'укрАинский', difficulty: 'hard' },
  { word: 'христианин', stressedIndex: 2, stressedWord: 'христианИн', difficulty: 'hard' },
  { word: 'обеспечение', stressedIndex: 2, stressedWord: 'обеспЕчение', difficulty: 'hard' },
  { word: 'средства', stressedIndex: 0, stressedWord: 'срЕдства', difficulty: 'hard', explanation: 'Множественное число, ударение на первом слоге' },
  { word: 'ключевой', stressedIndex: 2, stressedWord: 'ключевОй', difficulty: 'hard' },
  { word: 'аэропорты', stressedIndex: 2, stressedWord: 'аэропОрты', difficulty: 'hard' },
  { word: 'заняла', stressedIndex: 1, stressedWord: 'занялА', difficulty: 'hard', explanation: 'Прошедшее время женского рода' },
  { word: 'поняла', stressedIndex: 1, stressedWord: 'понялА', difficulty: 'hard' },
  { word: 'создала', stressedIndex: 1, stressedWord: 'создалА', difficulty: 'hard' },
]

export default function StressMark() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentWord, setCurrentWord] = useState<WordData | null>(null)
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null)
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('easy')
  const [wordsUsed, setWordsUsed] = useState<Set<number>>(new Set())
  const [mode, setMode] = useState<'menu' | 'game'>('menu')

  const getFilteredWords = useCallback(() => {
    return WORDS.filter(w => w.difficulty === difficulty)
  }, [difficulty])

  const getNextWord = useCallback(() => {
    const filtered = getFilteredWords()
    const available = filtered
      .map((w, i) => ({ w, originalIndex: WORDS.indexOf(w) }))
      .filter(item => !wordsUsed.has(item.originalIndex))
    
    if (available.length === 0) {
      setGameOver(true)
      return null
    }
    
    const randomIndex = Math.floor(Math.random() * available.length)
    return available[randomIndex].w
  }, [getFilteredWords, wordsUsed])

  useEffect(() => {
    if (mode === 'game' && !currentWord && !gameOver) {
      const w = getNextWord()
      if (w) setCurrentWord(w)
    }
  }, [mode, currentWord, gameOver, getNextWord])

  const startGame = (diff: 'easy' | 'medium' | 'hard') => {
    setDifficulty(diff)
    setScore(0)
    setStreak(0)
    setTotalQuestions(0)
    setWordsUsed(new Set())
    setGameOver(false)
    setSelectedIndex(null)
    setShowResult(false)
    setMode('game')
    const filtered = WORDS.filter(w => w.difficulty === diff)
    const randomIndex = Math.floor(Math.random() * filtered.length)
    setCurrentWord(filtered[randomIndex])
    setWordsUsed(new Set([WORDS.indexOf(filtered[randomIndex])]))
  }

  const handleLetterClick = (index: number) => {
    if (!currentWord || showResult) return
    setSelectedIndex(index)
  }

  const checkAnswer = () => {
    if (!currentWord || selectedIndex === null) return
    
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = selectedIndex === currentWord.stressedIndex
    
    if (isCorrect) {
      playSound('correct')
      const newStreak = streak + 1
      setStreak(newStreak)
      const bonus = Math.floor(newStreak / 3) * 2
      const xp = 10 + bonus
      setScore(prev => prev + xp)
      addXP(xp)
    } else {
      playSound('wrong')
      setStreak(0)
    }
    
    setTimeout(() => {
      const originalIndex = WORDS.indexOf(currentWord)
      const newUsed = new Set(wordsUsed).add(originalIndex)
      setWordsUsed(newUsed)
      setSelectedIndex(null)
      setShowResult(false)
      
      const filtered = WORDS.filter(w => w.difficulty === difficulty)
      const available = filtered.filter(w => !newUsed.has(WORDS.indexOf(w)))
      
      if (available.length === 0) {
        setGameOver(true)
      } else {
        const nextW = available[Math.floor(Math.random() * available.length)]
        setCurrentWord(nextW)
      }
    }, 2500)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentWord(null)
    setGameOver(false)
  }

  const getVowelIndices = (word: string): number[] => {
    const vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return word.split('').reduce((acc, char, i) => {
      if (vowels.includes(char)) acc.push(i)
      return acc
    }, [] as number[])
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-red-900/50 to-rose-900/50 rounded-2xl p-6 backdrop-blur-sm border border-red-500/30">
        <h2 className="text-2xl font-bold text-red-300 mb-6 flex items-center gap-2">
          <Volume2 className="w-7 h-7" />
          Ударения
        </h2>
        
        <p className="text-red-200 mb-6">
          Поставьте ударение в слове. Правильная расстановка ударения - признак грамотной речи!
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
                {diff === 'easy' ? 'Простые слова' : diff === 'medium' ? 'Обычные' : 'Трудные случаи'}
              </div>
            </button>
          ))}
        </div>
        
        <div className="bg-white/10 rounded-lg p-4 text-center">
          <AlertCircle className="w-6 h-6 mx-auto text-red-400 mb-2" />
          <p className="text-red-200 text-sm">
            Нажмите на гласную букву, чтобы поставить ударение
          </p>
        </div>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-red-900/50 to-rose-900/50 rounded-2xl p-6 backdrop-blur-sm border border-red-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-red-300 mb-2">Отлично!</h2>
        <p className="text-red-200 mb-4">
          Результат: {score} XP за {totalQuestions} слов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-red-500 hover:bg-red-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-red-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentWord) return null

  const vowels = getVowelIndices(currentWord.word)
  const letters = currentWord.word.split('')

  return (
    <div className="bg-gradient-to-br from-red-900/50 to-rose-900/50 rounded-2xl p-6 backdrop-blur-sm border border-red-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-red-300 text-sm flex items-center gap-2">
          <Target className="w-4 h-4" />
          Поставьте ударение
        </div>
        <div className="flex items-center gap-4">
          <span className="text-red-300">Серия: {streak}🔥</span>
          <span className="text-red-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-6 mb-6">
        <p className="text-center mb-2 text-red-300 text-sm">Выберите букву для ударения:</p>
        <div className="flex justify-center gap-1 flex-wrap">
          {letters.map((letter, index) => {
            const isVowel = vowels.includes(index)
            const isSelected = selectedIndex === index
            const isCorrect = showResult && index === currentWord.stressedIndex
            const isWrong = showResult && isSelected && !isCorrect
            
            return (
              <button
                key={index}
                onClick={() => isVowel && handleLetterClick(index)}
                disabled={!isVowel || showResult}
                className={`relative px-3 py-2 text-3xl font-bold transition-all ${
                  isVowel 
                    ? isSelected
                      ? 'text-red-300'
                      : 'text-white hover:text-red-300 cursor-pointer'
                    : 'text-white cursor-default'
                }`}
              >
                {isSelected && !showResult && (
                  <span className="absolute -top-2 left-1/2 transform -translate-x-1/2 text-red-400 text-xl">́</span>
                )}
                {isCorrect && (
                  <span className="absolute -top-2 left-1/2 transform -translate-x-1/2 text-green-400 text-xl">́</span>
                )}
                {isWrong && (
                  <span className="absolute -top-2 left-1/2 transform -translate-x-1/2 text-red-400 text-xl">́</span>
                )}
                <span className={isCorrect ? 'text-green-400' : isWrong ? 'text-red-400 line-through' : ''}>
                  {letter}
                </span>
              </button>
            )
          })}
        </div>
      </div>

      {showResult && (
        <div className={`mb-4 p-3 rounded-lg ${
          selectedIndex === currentWord.stressedIndex
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          <p className="font-bold mb-1">
            {selectedIndex === currentWord.stressedIndex
              ? '✅ Правильно!'
              : `❌ Правильно: ${currentWord.stressedWord}`}
          </p>
          {currentWord.explanation && (
            <p className="text-sm opacity-75">{currentWord.explanation}</p>
          )}
        </div>
      )}

      <button
        onClick={checkAnswer}
        disabled={showResult || selectedIndex === null}
        className="w-full py-3 bg-red-500 hover:bg-red-400 disabled:opacity-50 rounded-xl font-bold text-white transition-colors"
      >
        Проверить
      </button>

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-red-400">
          Слово {totalQuestions + 1} из {getFilteredWords().length}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-red-400 hover:text-red-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
