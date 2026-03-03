'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { BookCopy, RotateCcw, Trophy, Target, HelpCircle } from 'lucide-react'

interface HomonymData {
  word: string
  meanings: string[]
  examples: string[]
  difficulty: 'easy' | 'medium' | 'hard'
}

const HOMONYMS: HomonymData[] = [
  // Лёгкий уровень
  { word: 'коса', meanings: ['причёска', 'инструмент', 'берег реки'], examples: ['длинная коса', 'острая коса', 'песчаная коса'], difficulty: 'easy' },
  { word: 'лук', meanings: ['овощ', 'оружие'], examples: ['горький лук', 'тугой лук'], difficulty: 'easy' },
  { word: 'ключ', meanings: ['инструмент', 'родник', 'шифр'], examples: ['гаечный ключ', 'горный ключ', 'ключ к шифру'], difficulty: 'easy' },
  { word: 'мир', meanings: ['отсутствие войны', 'вселенная'], examples: ['мир во всём мире', 'мироздание'], difficulty: 'easy' },
  { word: 'клетка', meanings: ['место для животных', 'единица ткани', 'квадрат'], examples: ['клетка для птиц', 'кровяная клетка', 'клетка на рубашке'], difficulty: 'easy' },
  { word: 'лист', meanings: ['часть растения', 'бумага'], examples: ['зелёный лист', 'лист бумаги'], difficulty: 'easy' },
  { word: 'шляпка', meanings: ['головной убор', 'часть гриба', 'деталь'], examples: ['новая шляпка', 'шляпка гриба', 'шляпка гвоздя'], difficulty: 'easy' },
  { word: 'глава', meanings: ['голова', 'раздел книги', 'руководитель'], examples: ['глава семьи', 'глава романа', 'глава государства'], difficulty: 'easy' },
  
  // Средний уровень
  { word: 'бор', meanings: ['сосновый лес', 'химический элемент', 'зубной врач'], examples: ['густой бор', 'химический бор', 'зубной бор'], difficulty: 'medium' },
  { word: 'гребень', meanings: ['для волос', 'часть петуха', 'вершина горы'], examples: ['расчёска-гребень', 'гребень петуха', 'гребень горы'], difficulty: 'medium' },
  { word: 'клуб', meanings: ['организация', 'дымовое облако'], examples: ['спортивный клуб', 'клуб дыма'], difficulty: 'medium' },
  { word: 'лавка', meanings: ['магазин', 'скамья'], examples: ['овощная лавка', 'деревянная лавка'], difficulty: 'medium' },
  { word: 'лампа', meanings: ['осветительный прибор', 'электронный прибор'], examples: ['настольная лампа', 'электронная лампа'], difficulty: 'medium' },
  { word: 'лопатка', meanings: ['инструмент', 'кость', 'часть растения'], examples: ['садовая лопатка', 'лопатка плеча', 'лопатка листа'], difficulty: 'medium' },
  { word: 'наконечник', meanings: ['окончание предмета', 'снаряжение'], examples: ['наконечник стрелы', 'наконечник копья'], difficulty: 'medium' },
  { word: 'опушка', meanings: ['край леса', 'меховая отделка'], examples: ['опушка леса', 'опушка шубы'], difficulty: 'medium' },
  { word: 'плита', meanings: ['каменная плита', 'кухонная плита'], examples: ['мраморная плита', 'газовая плита'], difficulty: 'medium' },
  { word: 'почта', meanings: ['учреждение', 'здание', 'переписка'], examples: ['работать на почте', 'идти на почту', 'получить почту'], difficulty: 'medium' },
  
  // Сложный уровень
  { word: 'балка', meanings: ['бревно', 'овраг'], examples: ['несущая балка', 'глубокая балка'], difficulty: 'hard' },
  { word: 'блок', meanings: ['устройство', 'объединение', 'часть здания'], examples: ['блок питания', 'политический блок', 'жилой блок'], difficulty: 'hard' },
  { word: 'вяз', meanings: ['дерево', 'действие'], examples: ['старый вяз', 'вяз узлов'], difficulty: 'hard' },
  { word: 'звено', meanings: ['часть цепи', 'единица организации', 'элемент системы'], examples: ['звено цепи', 'звено пионеров', 'звено механизма'], difficulty: 'hard' },
  { word: 'карьер', meanings: ['место добычи', 'продвижение по службе'], examples: ['каменный карьер', 'успешная карьера'], difficulty: 'hard' },
  { word: 'клиент', meanings: ['покупатель', 'зависимый человек'], examples: ['постоянный клиент', 'клиент банка'], difficulty: 'hard' },
  { word: 'код', meanings: ['шифр', 'программа', 'правила'], examples: ['секретный код', 'код программы', 'кодекс чести'], difficulty: 'hard' },
  { word: 'кора', meanings: ['кожица дерева', 'вещество мозга'], examples: ['кора дуба', 'кора головного мозга'], difficulty: 'hard' },
  { word: 'кухня', meanings: ['помещение', 'культура питания'], examples: ['большая кухня', 'французская кухня'], difficulty: 'hard' },
  { word: 'линия', meanings: ['черта', 'направление', 'транспорт'], examples: 'прямая линия, линия метро, линия поведения', difficulty: 'hard' },
  { word: 'объём', meanings: ['величина', 'содержание'], examples: ['объём куба', 'объём знаний'], difficulty: 'hard' },
  { word: 'пропись', meanings: ['образец письма', 'правило'], examples: ['прописи для детей', 'пропись в документе'], difficulty: 'hard' },
]

export default function Homonyms() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentHomonym, setCurrentHomonym] = useState<HomonymData | null>(null)
  const [currentMeaningIndex, setCurrentMeaningIndex] = useState(0)
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

  const getFilteredHomonyms = useCallback(() => {
    return HOMONYMS.filter(h => h.difficulty === difficulty)
  }, [difficulty])

  const generateOptions = useCallback((homonym: HomonymData, correctMeaning: string) => {
    const allMeanings = HOMONYMS.flatMap(h => h.meanings)
    const wrongAnswers = allMeanings
      .filter(m => m !== correctMeaning)
      .sort(() => Math.random() - 0.5)
      .slice(0, 3)
    
    const allOptions = [...wrongAnswers, correctMeaning].sort(() => Math.random() - 0.5)
    setOptions(allOptions)
  }, [])

  const getNextQuestion = useCallback(() => {
    const filtered = getFilteredHomonyms()
    const available = filtered.filter(h => !usedItems.has(h.word))
    
    if (available.length === 0) {
      setGameOver(true)
      return null
    }
    
    const randomIndex = Math.floor(Math.random() * available.length)
    const homonym = available[randomIndex]
    const meaningIndex = Math.floor(Math.random() * homonym.meanings.length)
    
    return { homonym, meaningIndex }
  }, [getFilteredHomonyms, usedItems])

  useEffect(() => {
    if (mode === 'game' && !currentHomonym && !gameOver) {
      const next = getNextQuestion()
      if (next) {
        setCurrentHomonym(next.homonym)
        setCurrentMeaningIndex(next.meaningIndex)
        generateOptions(next.homonym, next.homonym.meanings[next.meaningIndex])
      }
    }
  }, [mode, currentHomonym, gameOver, getNextQuestion, generateOptions])

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
    const filtered = HOMONYMS.filter(h => h.difficulty === diff)
    const randomIndex = Math.floor(Math.random() * filtered.length)
    const homonym = filtered[randomIndex]
    setCurrentHomonym(homonym)
    setUsedItems(new Set([homonym.word]))
    const meaningIndex = Math.floor(Math.random() * homonym.meanings.length)
    setCurrentMeaningIndex(meaningIndex)
    generateOptions(homonym, homonym.meanings[meaningIndex])
  }

  const handleSelect = (answer: string) => {
    if (!currentHomonym || showResult) return
    
    setSelectedAnswer(answer)
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = answer === currentHomonym.meanings[currentMeaningIndex]
    
    if (isCorrect) {
      playSound('correct')
      const newStreak = streak + 1
      setStreak(newStreak)
      const bonus = Math.floor(newStreak / 3) * 2
      const xp = 12 + bonus
      setScore(prev => prev + xp)
      addXP(xp)
    } else {
      playSound('wrong')
      setStreak(0)
    }
    
    setTimeout(() => {
      const newUsed = new Set(usedItems).add(currentHomonym.word)
      setUsedItems(newUsed)
      setSelectedAnswer(null)
      setShowResult(false)
      
      const filtered = HOMONYMS.filter(h => h.difficulty === difficulty)
      const available = filtered.filter(h => !newUsed.has(h.word))
      
      if (available.length === 0) {
        setGameOver(true)
      } else {
        const nextH = available[Math.floor(Math.random() * available.length)]
        setCurrentHomonym(nextH)
        const meaningIdx = Math.floor(Math.random() * nextH.meanings.length)
        setCurrentMeaningIndex(meaningIdx)
        generateOptions(nextH, nextH.meanings[meaningIdx])
      }
    }, 2500)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentHomonym(null)
    setGameOver(false)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-orange-900/50 to-amber-900/50 rounded-2xl p-6 backdrop-blur-sm border border-orange-500/30">
        <h2 className="text-2xl font-bold text-orange-300 mb-6 flex items-center gap-2">
          <BookCopy className="w-7 h-7" />
          Омонимы
        </h2>
        
        <p className="text-orange-200 mb-6">
          Омонимы - слова, которые пишутся одинаково, но имеют разное значение. Определите значение слова по контексту!
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
                {diff === 'easy' ? '8 слов' : diff === 'medium' ? '10 слов' : '12 слов'}
              </div>
            </button>
          ))}
        </div>
        
        <div className="bg-white/10 rounded-lg p-4">
          <p className="text-orange-300 text-sm text-center">
            Пример: <strong>коса</strong> - причёска, инструмент для покоса, отмель реки
          </p>
        </div>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-orange-900/50 to-amber-900/50 rounded-2xl p-6 backdrop-blur-sm border border-orange-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-orange-300 mb-2">Отлично!</h2>
        <p className="text-orange-200 mb-4">
          Результат: {score} XP за {totalQuestions} вопросов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-orange-500 hover:bg-orange-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-orange-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentHomonym) return null

  const correctMeaning = currentHomonym.meanings[currentMeaningIndex]
  const example = currentHomonym.examples[currentMeaningIndex] || currentHomonym.examples[0]

  return (
    <div className="bg-gradient-to-br from-orange-900/50 to-amber-900/50 rounded-2xl p-6 backdrop-blur-sm border border-orange-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className="text-orange-300 text-sm flex items-center gap-2">
          <Target className="w-4 h-4" />
          Определите значение
        </div>
        <div className="flex items-center gap-4">
          <span className="text-orange-300">Серия: {streak}🔥</span>
          <span className="text-orange-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-6 mb-6 text-center">
        <p className="text-orange-300 text-sm mb-2">Слово-омоним:</p>
        <p className="text-4xl font-bold text-white mb-4">{currentHomonym.word}</p>
        <div className="bg-orange-500/20 rounded-lg p-3">
          <p className="text-orange-300 text-sm">Пример употребления:</p>
          <p className="text-white font-medium">{example}</p>
        </div>
      </div>

      <p className="text-orange-300 text-sm mb-3 text-center">Что означает это слово в данном контексте?</p>

      <div className="grid grid-cols-1 gap-3">
        {options.map((option, index) => {
          const isSelected = selectedAnswer === option
          const isCorrect = option === correctMeaning
          
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
        <div className={`mt-4 p-3 rounded-lg ${
          selectedAnswer === correctMeaning
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          {selectedAnswer === correctMeaning ? (
            <p className="font-bold">✅ Правильно! &quot;{currentHomonym.word}&quot; = {correctMeaning}</p>
          ) : (
            <p className="font-bold">❌ Правильный ответ: {correctMeaning}</p>
          )}
          {currentHomonym.meanings.length > 1 && (
            <p className="text-sm mt-1 opacity-75">
              Другие значения: {currentHomonym.meanings.filter(m => m !== correctMeaning).join(', ')}
            </p>
          )}
        </div>
      )}

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-orange-400">
          Вопрос {totalQuestions + 1}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-orange-400 hover:text-orange-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
