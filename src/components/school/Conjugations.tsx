'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { PenTool, RotateCcw, Trophy, Target, BookOpen } from 'lucide-react'

type ConjugationType = 'present' | 'past' | 'future'

interface VerbData {
  infinitive: string
  conjugation: 1 | 2
  present: Record<string, string>
  past: Record<string, string>
  future: Record<string, string>
  difficulty: 'easy' | 'medium' | 'hard'
}

const VERBS: VerbData[] = [
  // Лёгкий уровень - 1 и 2 спряжение
  { 
    infinitive: 'читать', conjugation: 1, difficulty: 'easy',
    present: { 'я': 'читаю', 'ты': 'читаешь', 'он/она': 'читает', 'мы': 'читаем', 'вы': 'читаете', 'они': 'читают' },
    past: { 'я': 'читал', 'ты': 'читал', 'он': 'читал', 'она': 'читала', 'мы': 'читали', 'вы': 'читали', 'они': 'читали' },
    future: { 'я': 'буду читать', 'ты': 'будешь читать', 'он/она': 'будет читать', 'мы': 'будем читать', 'вы': 'будете читать', 'они': 'будут читать' }
  },
  { 
    infinitive: 'писать', conjugation: 1, difficulty: 'easy',
    present: { 'я': 'пишу', 'ты': 'пишешь', 'он/она': 'пишет', 'мы': 'пишем', 'вы': 'пишете', 'они': 'пишут' },
    past: { 'я': 'писал', 'ты': 'писал', 'он': 'писал', 'она': 'писала', 'мы': 'писали', 'вы': 'писали', 'они': 'писали' },
    future: { 'я': 'буду писать', 'ты': 'будешь писать', 'он/она': 'будет писать', 'мы': 'будем писать', 'вы': 'будете писать', 'они': 'будут писать' }
  },
  { 
    infinitive: 'говорить', conjugation: 2, difficulty: 'easy',
    present: { 'я': 'говорю', 'ты': 'говоришь', 'он/она': 'говорит', 'мы': 'говорим', 'вы': 'говорите', 'они': 'говорят' },
    past: { 'я': 'говорил', 'ты': 'говорил', 'он': 'говорил', 'она': 'говорила', 'мы': 'говорили', 'вы': 'говорили', 'они': 'говорили' },
    future: { 'я': 'буду говорить', 'ты': 'будешь говорить', 'он/она': 'будет говорить', 'мы': 'будем говорить', 'вы': 'будете говорить', 'они': 'будут говорить' }
  },
  { 
    infinitive: 'делать', conjugation: 1, difficulty: 'easy',
    present: { 'я': 'делаю', 'ты': 'делаешь', 'он/она': 'делает', 'мы': 'делаем', 'вы': 'делаете', 'они': 'делают' },
    past: { 'я': 'делал', 'ты': 'делал', 'он': 'делал', 'она': 'делала', 'мы': 'делали', 'вы': 'делали', 'они': 'делали' },
    future: { 'я': 'буду делать', 'ты': 'будешь делать', 'он/она': 'будет делать', 'мы': 'будем делать', 'вы': 'будете делать', 'они': 'будут делать' }
  },
  { 
    infinitive: 'сидеть', conjugation: 2, difficulty: 'easy',
    present: { 'я': 'сижу', 'ты': 'сидишь', 'он/она': 'сидит', 'мы': 'сидим', 'вы': 'сидите', 'они': 'сидят' },
    past: { 'я': 'сидел', 'ты': 'сидел', 'он': 'сидел', 'она': 'сидела', 'мы': 'сидели', 'вы': 'сидели', 'они': 'сидели' },
    future: { 'я': 'буду сидеть', 'ты': 'будешь сидеть', 'он/она': 'будет сидеть', 'мы': 'будем сидеть', 'вы': 'будете сидеть', 'они': 'будут сидеть' }
  },
  
  // Средний уровень
  { 
    infinitive: 'бежать', conjugation: 1, difficulty: 'medium',
    present: { 'я': 'бегу', 'ты': 'бежишь', 'он/она': 'бежит', 'мы': 'бежим', 'вы': 'бежите', 'они': 'бегут' },
    past: { 'я': 'бежал', 'ты': 'бежал', 'он': 'бежал', 'она': 'бежала', 'мы': 'бежали', 'вы': 'бежали', 'они': 'бежали' },
    future: { 'я': 'буду бежать', 'ты': 'будешь бежать', 'он/она': 'будет бежать', 'мы': 'будем бежать', 'вы': 'будете бежать', 'они': 'будут бежать' }
  },
  { 
    infinitive: 'хотеть', conjugation: 1, difficulty: 'medium',
    present: { 'я': 'хочу', 'ты': 'хочешь', 'он/она': 'хочет', 'мы': 'хотим', 'вы': 'хотите', 'они': 'хотят' },
    past: { 'я': 'хотел', 'ты': 'хотел', 'он': 'хотел', 'она': 'хотела', 'мы': 'хотели', 'вы': 'хотели', 'они': 'хотели' },
    future: { 'я': 'буду хотеть', 'ты': 'будешь хотеть', 'он/она': 'будет хотеть', 'мы': 'будем хотеть', 'вы': 'будете хотеть', 'они': 'будут хотеть' }
  },
  { 
    infinitive: 'смотреть', conjugation: 2, difficulty: 'medium',
    present: { 'я': 'смотрю', 'ты': 'смотришь', 'он/она': 'смотрит', 'мы': 'смотрим', 'вы': 'смотрите', 'они': 'смотрят' },
    past: { 'я': 'смотрел', 'ты': 'смотрел', 'он': 'смотрел', 'она': 'смотрела', 'мы': 'смотрели', 'вы': 'смотрели', 'они': 'смотрели' },
    future: { 'я': 'буду смотреть', 'ты': 'будешь смотреть', 'он/она': 'будет смотреть', 'мы': 'будем смотреть', 'вы': 'будете смотреть', 'они': 'будут смотреть' }
  },
  { 
    infinitive: 'видеть', conjugation: 2, difficulty: 'medium',
    present: { 'я': 'вижу', 'ты': 'видишь', 'он/она': 'видит', 'мы': 'видим', 'вы': 'видите', 'они': 'видят' },
    past: { 'я': 'видел', 'ты': 'видел', 'он': 'видел', 'она': 'видела', 'мы': 'видели', 'вы': 'видели', 'они': 'видели' },
    future: { 'я': 'буду видеть', 'ты': 'будешь видеть', 'он/она': 'будет видеть', 'мы': 'будем видеть', 'вы': 'будете видеть', 'они': 'будут видеть' }
  },
  { 
    infinitive: 'слышать', conjugation: 2, difficulty: 'medium',
    present: { 'я': 'слышу', 'ты': 'слышишь', 'он/она': 'слышит', 'мы': 'слышим', 'вы': 'слышите', 'они': 'слышат' },
    past: { 'я': 'слышал', 'ты': 'слышал', 'он': 'слышал', 'она': 'слышала', 'мы': 'слышали', 'вы': 'слышали', 'они': 'слышали' },
    future: { 'я': 'буду слышать', 'ты': 'будешь слышать', 'он/она': 'будет слышать', 'мы': 'будем слышать', 'вы': 'будете слышать', 'они': 'будут слышать' }
  },
  
  // Сложный уровень - разноспрягаемые и особые
  { 
    infinitive: 'дать', conjugation: 1, difficulty: 'hard',
    present: { 'я': 'дам', 'ты': 'дашь', 'он/она': 'даст', 'мы': 'дадим', 'вы': 'дадите', 'они': 'дадут' },
    past: { 'я': 'дал', 'ты': 'дал', 'он': 'дал', 'она': 'дала', 'мы': 'дали', 'вы': 'дали', 'они': 'дали' },
    future: { 'я': 'дам', 'ты': 'дашь', 'он/она': 'даст', 'мы': 'дадим', 'вы': 'дадите', 'они': 'дадут' }
  },
  { 
    infinitive: 'есть', conjugation: 1, difficulty: 'hard',
    present: { 'я': 'ем', 'ты': 'ешь', 'он/она': 'ест', 'мы': 'едим', 'вы': 'едите', 'они': 'едят' },
    past: { 'я': 'ел', 'ты': 'ел', 'он': 'ел', 'она': 'ела', 'мы': 'ели', 'вы': 'ели', 'они': 'ели' },
    future: { 'я': 'буду есть', 'ты': 'будешь есть', 'он/она': 'будет есть', 'мы': 'будем есть', 'вы': 'будете есть', 'они': 'будут есть' }
  },
  { 
    infinitive: 'хотеть', conjugation: 1, difficulty: 'hard',
    present: { 'я': 'хочу', 'ты': 'хочешь', 'он/она': 'хочет', 'мы': 'хотим', 'вы': 'хотите', 'они': 'хотят' },
    past: { 'я': 'хотел', 'ты': 'хотел', 'он': 'хотел', 'она': 'хотела', 'мы': 'хотели', 'вы': 'хотели', 'они': 'хотели' },
    future: { 'я': 'захочу', 'ты': 'захочешь', 'он/она': 'захочет', 'мы': 'захотим', 'вы': 'захотите', 'они': 'захотят' }
  },
  { 
    infinitive: 'брить', conjugation: 1, difficulty: 'hard',
    present: { 'я': 'брею', 'ты': 'бреешь', 'он/она': 'бреет', 'мы': 'бреем', 'вы': 'бреете', 'они': 'бреют' },
    past: { 'я': 'брил', 'ты': 'брил', 'он': 'брил', 'она': 'брила', 'мы': 'брили', 'вы': 'брили', 'они': 'брили' },
    future: { 'я': 'буду брить', 'ты': 'будешь брить', 'он/она': 'будет брить', 'мы': 'будем брить', 'вы': 'будете брить', 'они': 'будут брить' }
  },
  { 
    infinitive: 'стелить', conjugation: 1, difficulty: 'hard',
    present: { 'я': 'стелю', 'ты': 'стелешь', 'он/она': 'стелет', 'мы': 'стелем', 'вы': 'стелете', 'они': 'стелют' },
    past: { 'я': 'стелил', 'ты': 'стелил', 'он': 'стелил', 'она': 'стелила', 'мы': 'стелили', 'вы': 'стелили', 'они': 'стелили' },
    future: { 'я': 'буду стелить', 'ты': 'будешь стелить', 'он/она': 'будет стелить', 'мы': 'будем стелить', 'вы': 'будете стелить', 'они': 'будут стелить' }
  },
]

const TENSE_NAMES: Record<ConjugationType, string> = {
  present: 'Настоящее время',
  past: 'Прошедшее время',
  future: 'Будущее время'
}

const PRONOUNS = ['я', 'ты', 'он/она', 'мы', 'вы', 'они']

export default function Conjugations() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentVerb, setCurrentVerb] = useState<VerbData | null>(null)
  const [currentTense, setCurrentTense] = useState<ConjugationType>('present')
  const [currentPronoun, setCurrentPronoun] = useState('')
  const [userAnswer, setUserAnswer] = useState('')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('easy')
  const [usedItems, setUsedItems] = useState<Set<string>>(new Set())
  const [mode, setMode] = useState<'menu' | 'game'>('menu')

  const getFilteredVerbs = useCallback(() => {
    return VERBS.filter(v => v.difficulty === difficulty)
  }, [difficulty])

  const getNextQuestion = useCallback(() => {
    const filtered = getFilteredVerbs()
    const available = filtered.filter(v => !usedItems.has(v.infinitive))
    
    if (available.length === 0) {
      setGameOver(true)
      return null
    }
    
    const randomIndex = Math.floor(Math.random() * available.length)
    const verb = available[randomIndex]
    const tenses: ConjugationType[] = ['present', 'past', 'future']
    const randomTense = tenses[Math.floor(Math.random() * tenses.length)]
    const pronounKeys = Object.keys(verb[randomTense])
    const randomPronoun = pronounKeys[Math.floor(Math.random() * pronounKeys.length)]
    
    return { verb, tense: randomTense, pronoun: randomPronoun }
  }, [getFilteredVerbs, usedItems])

  useEffect(() => {
    if (mode === 'game' && !currentVerb && !gameOver) {
      const next = getNextQuestion()
      if (next) {
        setCurrentVerb(next.verb)
        setCurrentTense(next.tense)
        setCurrentPronoun(next.pronoun)
      }
    }
  }, [mode, currentVerb, gameOver, getNextQuestion])

  const startGame = (diff: 'easy' | 'medium' | 'hard') => {
    setDifficulty(diff)
    setScore(0)
    setStreak(0)
    setTotalQuestions(0)
    setUsedItems(new Set())
    setGameOver(false)
    setUserAnswer('')
    setShowResult(false)
    setMode('game')
    const filtered = VERBS.filter(v => v.difficulty === diff)
    const randomIndex = Math.floor(Math.random() * filtered.length)
    const verb = filtered[randomIndex]
    setCurrentVerb(verb)
    setUsedItems(new Set([verb.infinitive]))
    const tenses: ConjugationType[] = ['present', 'past', 'future']
    const randomTense = tenses[Math.floor(Math.random() * tenses.length)]
    setCurrentTense(randomTense)
    const pronounKeys = Object.keys(verb[randomTense])
    setCurrentPronoun(pronounKeys[Math.floor(Math.random() * pronounKeys.length)])
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!currentVerb || showResult) return
    
    const answer = userAnswer.trim().toLowerCase()
    const correct = currentVerb[currentTense][currentPronoun].toLowerCase()
    
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = answer === correct
    
    if (isCorrect) {
      playSound('correct')
      const newStreak = streak + 1
      setStreak(newStreak)
      const bonus = Math.floor(newStreak / 3) * 2
      const xp = 15 + bonus
      setScore(prev => prev + xp)
      addXP(xp)
    } else {
      playSound('wrong')
      setStreak(0)
    }
    
    setTimeout(() => {
      const newUsed = new Set(usedItems).add(currentVerb.infinitive)
      setUsedItems(newUsed)
      setUserAnswer('')
      setShowResult(false)
      
      const filtered = VERBS.filter(v => v.difficulty === difficulty)
      const available = filtered.filter(v => !newUsed.has(v.infinitive))
      
      if (available.length === 0) {
        setGameOver(true)
      } else {
        const nextV = available[Math.floor(Math.random() * available.length)]
        setCurrentVerb(nextV)
        const tenses: ConjugationType[] = ['present', 'past', 'future']
        const randomTense = tenses[Math.floor(Math.random() * tenses.length)]
        setCurrentTense(randomTense)
        const pronounKeys = Object.keys(nextV[randomTense])
        setCurrentPronoun(pronounKeys[Math.floor(Math.random() * pronounKeys.length)])
      }
    }, 2500)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentVerb(null)
    setGameOver(false)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-pink-900/50 to-rose-900/50 rounded-2xl p-6 backdrop-blur-sm border border-pink-500/30">
        <h2 className="text-2xl font-bold text-pink-300 mb-6 flex items-center gap-2">
          <PenTool className="w-7 h-7" />
          Спряжение глаголов
        </h2>
        
        <p className="text-pink-200 mb-6">
          Проспрягайте глаголы по лицам и числам. В русском языке два спряжения и особые формы!
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
                {diff === 'easy' ? 'Обычные глаголы' : diff === 'medium' ? 'Чередование' : 'Особые формы'}
              </div>
            </button>
          ))}
        </div>
        
        <div className="bg-white/10 rounded-lg p-4">
          <p className="text-pink-300 text-sm text-center">
            I спряжение: -ешь, -ет, -ем, -ете, -ут/-ют | II спряжение: -ишь, -ит, -им, -ите, -ат/-ят
          </p>
        </div>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-pink-900/50 to-rose-900/50 rounded-2xl p-6 backdrop-blur-sm border border-pink-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-pink-300 mb-2">Отлично!</h2>
        <p className="text-pink-200 mb-4">
          Результат: {score} XP за {totalQuestions} вопросов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-pink-500 hover:bg-pink-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-pink-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentVerb) return null

  const correctAnswer = currentVerb[currentTense][currentPronoun]

  return (
    <div className="bg-gradient-to-br from-pink-900/50 to-rose-900/50 rounded-2xl p-6 backdrop-blur-sm border border-pink-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-pink-300 text-sm">
          {currentVerb.conjugation} спряжение
        </div>
        <div className="flex items-center gap-4">
          <span className="text-pink-300">Серия: {streak}🔥</span>
          <span className="text-pink-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-6 mb-6 text-center">
        <p className="text-pink-300 text-sm mb-2">Глагол:</p>
        <p className="text-3xl font-bold text-white mb-4">{currentVerb.infinitive}</p>
        <div className="flex justify-center gap-4">
          <div className="bg-pink-500/20 rounded-lg px-4 py-2">
            <p className="text-pink-300 text-xs">Время</p>
            <p className="text-white font-bold">{TENSE_NAMES[currentTense]}</p>
          </div>
          <div className="bg-rose-500/20 rounded-lg px-4 py-2">
            <p className="text-rose-300 text-xs">Местоимение</p>
            <p className="text-white font-bold">{currentPronoun}</p>
          </div>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          value={userAnswer}
          onChange={(e) => setUserAnswer(e.target.value)}
          placeholder={`Форма глагола для "${currentPronoun}"`}
          className="w-full bg-white/10 border border-pink-500/30 rounded-xl px-4 py-3 text-white placeholder-pink-300 focus:outline-none focus:border-pink-400 text-xl text-center"
          autoFocus
        />
      </form>

      {showResult && (
        <div className={`mt-4 p-4 rounded-lg text-center ${
          userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          <p className="font-bold mb-1">
            {userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()
              ? '✅ Правильно!'
              : `❌ Правильно: ${correctAnswer}`}
          </p>
          <p className="text-sm opacity-75">
            {currentPronoun} {correctAnswer}
          </p>
        </div>
      )}

      <button
        onClick={() => handleSubmit({ preventDefault: () => {} } as React.FormEvent)}
        disabled={!userAnswer.trim() || showResult}
        className="mt-4 w-full py-3 bg-pink-500 hover:bg-pink-400 disabled:opacity-50 rounded-xl font-bold text-white transition-colors"
      >
        Проверить
      </button>

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-pink-400">
          Вопрос {totalQuestions + 1}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-pink-400 hover:text-pink-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
