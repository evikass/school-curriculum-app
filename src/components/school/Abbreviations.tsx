'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { Abbreviate, RotateCcw, Trophy, Target, BookOpen } from 'lucide-react'

interface AbbreviationData {
  abbr: string
  full: string
  category: string
  difficulty: 'easy' | 'medium' | 'hard'
}

const ABBREVIATIONS: AbbreviationData[] = [
  // Лёгкий уровень - общеизвестные
  { abbr: 'США', full: 'Соединённые Штаты Америки', category: 'География', difficulty: 'easy' },
  { abbr: 'ООН', full: 'Организация Объединённых Наций', category: 'Организации', difficulty: 'easy' },
  { abbr: 'КНР', full: 'Китайская Народная Республика', category: 'География', difficulty: 'easy' },
  { abbr: 'РФ', full: 'Российская Федерация', category: 'География', difficulty: 'easy' },
  { abbr: 'ООО', full: 'Общество с ограниченной ответственностью', category: 'Бизнес', difficulty: 'easy' },
  { abbr: 'ИП', full: 'Индивидуальный предприниматель', category: 'Бизнес', difficulty: 'easy' },
  { abbr: 'НДС', full: 'Налог на добавленную стоимость', category: 'Бизнес', difficulty: 'easy' },
  { abbr: 'ПДД', full: 'Правила дорожного движения', category: 'Транспорт', difficulty: 'easy' },
  { abbr: 'ГИБДД', full: 'Государственная инспекция безопасности дорожного движения', category: 'Транспорт', difficulty: 'easy' },
  { abbr: 'ЗП', full: 'Заработная плата', category: 'Бизнес', difficulty: 'easy' },
  { abbr: 'ТЦ', full: 'Торговый центр', category: 'Места', difficulty: 'easy' },
  { abbr: 'ТК', full: 'Трудовой кодекс', category: 'Закон', difficulty: 'easy' },
  
  // Средний уровень
  { abbr: 'МИД', full: 'Министерство иностранных дел', category: 'Государство', difficulty: 'medium' },
  { abbr: 'МВД', full: 'Министерство внутренних дел', category: 'Государство', difficulty: 'medium' },
  { abbr: 'МО', full: 'Министерство обороны', category: 'Государство', difficulty: 'medium' },
  { abbr: 'МЧС', full: 'Министерство по чрезвычайным ситуациям', category: 'Государство', difficulty: 'medium' },
  { abbr: 'ФСБ', full: 'Федеральная служба безопасности', category: 'Государство', difficulty: 'medium' },
  { abbr: 'ЦБ', full: 'Центральный банк', category: 'Финансы', difficulty: 'medium' },
  { abbr: 'СМИ', full: 'Средства массовой информации', category: 'Медиа', difficulty: 'medium' },
  { abbr: 'ИТ', full: 'Информационные технологии', category: 'Технологии', difficulty: 'medium' },
  { abbr: 'ГД', full: 'Государственная Дума', category: 'Государство', difficulty: 'medium' },
  { abbr: 'СФ', full: 'Совет Федерации', category: 'Государство', difficulty: 'medium' },
  { abbr: 'РЖД', full: 'Российские железные дороги', category: 'Транспорт', difficulty: 'medium' },
  { abbr: 'ГУМ', full: 'Главный универсальный магазин', category: 'Места', difficulty: 'medium' },
  { abbr: 'ВУЗ', full: 'Высшее учебное заведение', category: 'Образование', difficulty: 'medium' },
  { abbr: 'СУЗ', full: 'Среднее учебное заведение', category: 'Образование', difficulty: 'medium' },
  
  // Сложный уровень
  { abbr: 'ЕГЭ', full: 'Единый государственный экзамен', category: 'Образование', difficulty: 'hard' },
  { abbr: 'ОГЭ', full: 'Основной государственный экзамен', category: 'Образование', difficulty: 'hard' },
  { abbr: 'ВПР', full: 'Всероссийские проверочные работы', category: 'Образование', difficulty: 'hard' },
  { abbr: 'ГИА', full: 'Государственная итоговая аттестация', category: 'Образование', difficulty: 'hard' },
  { abbr: 'ОСАГО', full: 'Обязательное страхование автогражданской ответственности', category: 'Страхование', difficulty: 'hard' },
  { abbr: 'КАСКО', full: 'Комплексное автомобильное страхование кроме ответственности', category: 'Страхование', difficulty: 'hard' },
  { abbr: 'ЖКХ', full: 'Жилищно-коммунальное хозяйство', category: 'Услуги', difficulty: 'hard' },
  { abbr: 'УК', full: 'Управляющая компания', category: 'Услуги', difficulty: 'hard' },
  { abbr: 'НКО', full: 'Некоммерческая организация', category: 'Организации', difficulty: 'hard' },
  { abbr: 'АО', full: 'Акционерное общество', category: 'Бизнес', difficulty: 'hard' },
  { abbr: 'ПАО', full: 'Публичное акционерное общество', category: 'Бизнес', difficulty: 'hard' },
  { abbr: 'ФНС', full: 'Федеральная налоговая служба', category: 'Государство', difficulty: 'hard' },
  { abbr: 'Росреестр', full: 'Федеральная служба государственной регистрации, кадастра и картографии', category: 'Государство', difficulty: 'hard' },
  { abbr: 'Роспотребнадзор', full: 'Федеральная служба по надзору в сфере защиты прав потребителей', category: 'Государство', difficulty: 'hard' },
  { abbr: 'РИА', full: 'Российское информационное агентство', category: 'Медиа', difficulty: 'hard' },
  { abbr: 'ТАСС', full: 'Телеграфное агентство Советского Союза', category: 'Медиа', difficulty: 'hard' },
]

export default function Abbreviations() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentAbbr, setCurrentAbbr] = useState<AbbreviationData | null>(null)
  const [options, setOptions] = useState<string[]>([])
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null)
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('easy')
  const [usedItems, setUsedItems] = useState<Set<string>>(new Set())
  const [mode, setMode] = useState<'menu' | 'game'>('menu')

  const getFilteredAbbrs = useCallback(() => {
    return ABBREVIATIONS.filter(a => a.difficulty === difficulty)
  }, [difficulty])

  const generateOptions = useCallback((abbr: AbbreviationData) => {
    const allFull = ABBREVIATIONS.filter(a => a.difficulty === difficulty).map(a => a.full)
    const wrongAnswers = allFull
      .filter(f => f !== abbr.full)
      .sort(() => Math.random() - 0.5)
      .slice(0, 3)
    
    const allOptions = [...wrongAnswers, abbr.full].sort(() => Math.random() - 0.5)
    setOptions(allOptions)
  }, [difficulty])

  const getNextAbbr = useCallback(() => {
    const filtered = getFilteredAbbrs()
    const available = filtered.filter(a => !usedItems.has(a.abbr))
    
    if (available.length === 0) {
      setGameOver(true)
      return null
    }
    
    const randomIndex = Math.floor(Math.random() * available.length)
    return available[randomIndex]
  }, [getFilteredAbbrs, usedItems])

  useEffect(() => {
    if (mode === 'game' && !currentAbbr && !gameOver) {
      const next = getNextAbbr()
      if (next) {
        setCurrentAbbr(next)
        generateOptions(next)
      }
    }
  }, [mode, currentAbbr, gameOver, getNextAbbr, generateOptions])

  const startGame = (diff: 'easy' | 'medium' | 'hard') => {
    setDifficulty(diff)
    setScore(0)
    setStreak(0)
    setTotalQuestions(0)
    setUsedItems(new Set())
    setGameOver(false)
    setSelectedAnswer(null)
    setShowResult(false)
    setMode('game')
    const filtered = ABBREVIATIONS.filter(a => a.difficulty === diff)
    const randomIndex = Math.floor(Math.random() * filtered.length)
    const abbr = filtered[randomIndex]
    setCurrentAbbr(abbr)
    setUsedItems(new Set([abbr.abbr]))
    generateOptions(abbr)
  }

  const handleSelect = (answer: string) => {
    if (!currentAbbr || showResult) return
    
    setSelectedAnswer(answer)
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = answer === currentAbbr.full
    
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
      const newUsed = new Set(usedItems).add(currentAbbr.abbr)
      setUsedItems(newUsed)
      setSelectedAnswer(null)
      setShowResult(false)
      
      const filtered = ABBREVIATIONS.filter(a => a.difficulty === difficulty)
      const available = filtered.filter(a => !newUsed.has(a.abbr))
      
      if (available.length === 0) {
        setGameOver(true)
      } else {
        const nextA = available[Math.floor(Math.random() * available.length)]
        setCurrentAbbr(nextA)
        generateOptions(nextA)
      }
    }, 2500)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentAbbr(null)
    setGameOver(false)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-amber-900/50 to-yellow-900/50 rounded-2xl p-6 backdrop-blur-sm border border-amber-500/30">
        <h2 className="text-2xl font-bold text-amber-300 mb-6 flex items-center gap-2">
          <Abbreviate className="w-7 h-7" />
          Аббревиатуры
        </h2>
        
        <p className="text-amber-200 mb-6">
          Расшифруйте аббревиатуры! Это сокращённые названия организаций, учреждений и понятий.
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
                {diff === 'easy' ? 'Известные' : diff === 'medium' ? 'Государственные' : 'Специальные'}
              </div>
            </button>
          ))}
        </div>
        
        <div className="bg-white/10 rounded-lg p-4">
          <p className="text-amber-300 text-sm text-center">
            Примеры: <strong>США</strong> = Соединённые Штаты Америки, <strong>ООН</strong> = Организация Объединённых Наций
          </p>
        </div>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-amber-900/50 to-yellow-900/50 rounded-2xl p-6 backdrop-blur-sm border border-amber-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-amber-300 mb-2">Отлично!</h2>
        <p className="text-amber-200 mb-4">
          Результат: {score} XP за {totalQuestions} вопросов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-amber-500 hover:bg-amber-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-amber-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentAbbr) return null

  return (
    <div className="bg-gradient-to-br from-amber-900/50 to-yellow-900/50 rounded-2xl p-6 backdrop-blur-sm border border-amber-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-amber-300 text-sm flex items-center gap-2">
          <Target className="w-4 h-4" />
          {currentAbbr.category}
        </div>
        <div className="flex items-center gap-4">
          <span className="text-amber-300">Серия: {streak}🔥</span>
          <span className="text-amber-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-6 mb-6 text-center">
        <p className="text-amber-300 text-sm mb-2">Расшифруйте аббревиатуру:</p>
        <p className="text-5xl font-bold text-white">{currentAbbr.abbr}</p>
      </div>

      <div className="grid grid-cols-1 gap-3">
        {options.map((option, index) => {
          const isSelected = selectedAnswer === option
          const isCorrect = option === currentAbbr.full
          
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
              className={`p-4 rounded-xl font-bold border transition-all text-left ${buttonClass}`}
            >
              {option}
            </button>
          )
        })}
      </div>

      {showResult && (
        <div className={`mt-4 p-3 rounded-lg ${
          selectedAnswer === currentAbbr.full
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          {selectedAnswer === currentAbbr.full ? (
            <p className="font-bold">✅ Правильно! {currentAbbr.abbr} = {currentAbbr.full}</p>
          ) : (
            <p className="font-bold">❌ {currentAbbr.abbr} = {currentAbbr.full}</p>
          )}
        </div>
      )}

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-amber-400">
          Вопрос {totalQuestions + 1} из {getFilteredAbbrs().length}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-amber-400 hover:text-amber-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
