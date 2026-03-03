'use client'

import { useState, useEffect, useCallback } from 'react'
import { useSchool } from '@/context/SchoolContext'
import useSound from '@/hooks/useSound'
import { BookOpen, RotateCcw, Trophy, Target, HelpCircle } from 'lucide-react'

type CaseType = 'nominative' | 'genitive' | 'dative' | 'accusative' | 'instrumental' | 'prepositional'

interface WordCase {
  word: string
  cases: Record<CaseType, string>
  difficulty: 'easy' | 'medium' | 'hard'
  gender: 'm' | 'f' | 'n'
}

const WORD_CASES: WordCase[] = [
  // Лёгкий уровень - простые существительные
  { word: 'дом', gender: 'm', difficulty: 'easy', cases: { nominative: 'дом', genitive: 'дома', dative: 'дому', accusative: 'дом', instrumental: 'домом', prepositional: 'доме' } },
  { word: 'кот', gender: 'm', difficulty: 'easy', cases: { nominative: 'кот', genitive: 'кота', dative: 'коту', accusative: 'кота', instrumental: 'котом', prepositional: 'коте' } },
  { word: 'стол', gender: 'm', difficulty: 'easy', cases: { nominative: 'стол', genitive: 'стола', dative: 'столу', accusative: 'стол', instrumental: 'столом', prepositional: 'столе' } },
  { word: 'лес', gender: 'm', difficulty: 'easy', cases: { nominative: 'лес', genitive: 'леса', dative: 'лесу', accusative: 'лес', instrumental: 'лесом', prepositional: 'лесе' } },
  { word: 'сад', gender: 'm', difficulty: 'easy', cases: { nominative: 'сад', genitive: 'сада', dative: 'саду', accusative: 'сад', instrumental: 'садом', prepositional: 'саде' } },
  { word: 'вода', gender: 'f', difficulty: 'easy', cases: { nominative: 'вода', genitive: 'воды', dative: 'воде', accusative: 'воду', instrumental: 'водой', prepositional: 'воде' } },
  { word: 'рука', gender: 'f', difficulty: 'easy', cases: { nominative: 'рука', genitive: 'руки', dative: 'руке', accusative: 'руку', instrumental: 'рукой', prepositional: 'руке' } },
  { word: 'книга', gender: 'f', difficulty: 'easy', cases: { nominative: 'книга', genitive: 'книги', dative: 'книге', accusative: 'книгу', instrumental: 'книгой', prepositional: 'книге' } },
  { word: 'мама', gender: 'f', difficulty: 'easy', cases: { nominative: 'мама', genitive: 'мамы', dative: 'маме', accusative: 'маму', instrumental: 'мамой', prepositional: 'маме' } },
  { word: 'окно', gender: 'n', difficulty: 'easy', cases: { nominative: 'окно', genitive: 'окна', dative: 'окну', accusative: 'окно', instrumental: 'окном', prepositional: 'окне' } },
  
  // Средний уровень
  { word: 'учитель', gender: 'm', difficulty: 'medium', cases: { nominative: 'учитель', genitive: 'учителя', dative: 'учителю', accusative: 'учителя', instrumental: 'учителем', prepositional: 'учителе' } },
  { word: 'ученик', gender: 'm', difficulty: 'medium', cases: { nominative: 'ученик', genitive: 'ученика', dative: 'ученику', accusative: 'ученика', instrumental: 'учеником', prepositional: 'ученике' } },
  { word: 'песня', gender: 'f', difficulty: 'medium', cases: { nominative: 'песня', genitive: 'песни', dative: 'песне', accusative: 'песню', instrumental: 'песней', prepositional: 'песне' } },
  { word: 'земля', gender: 'f', difficulty: 'medium', cases: { nominative: 'земля', genitive: 'земли', dative: 'земле', accusative: 'землю', instrumental: 'землёй', prepositional: 'земле' } },
  { word: 'море', gender: 'n', difficulty: 'medium', cases: { nominative: 'море', genitive: 'моря', dative: 'морю', accusative: 'море', instrumental: 'морем', prepositional: 'море' } },
  { word: 'поле', gender: 'n', difficulty: 'medium', cases: { nominative: 'поле', genitive: 'поля', dative: 'полю', accusative: 'поле', instrumental: 'полем', prepositional: 'поле' } },
  { word: 'деревня', gender: 'f', difficulty: 'medium', cases: { nominative: 'деревня', genitive: 'деревни', dative: 'деревне', accusative: 'деревню', instrumental: 'деревней', prepositional: 'деревне' } },
  { word: 'город', gender: 'm', difficulty: 'medium', cases: { nominative: 'город', genitive: 'города', dative: 'городу', accusative: 'город', instrumental: 'городом', prepositional: 'городе' } },
  { word: 'друг', gender: 'm', difficulty: 'medium', cases: { nominative: 'друг', genitive: 'друга', dative: 'другу', accusative: 'друга', instrumental: 'другом', prepositional: 'друге' } },
  { word: 'сестра', gender: 'f', difficulty: 'medium', cases: { nominative: 'сестра', genitive: 'сестры', dative: 'сестре', accusative: 'сестру', instrumental: 'сестрой', prepositional: 'сестре' } },
  
  // Сложный уровень - слова с особенностями
  { word: 'отец', gender: 'm', difficulty: 'hard', cases: { nominative: 'отец', genitive: 'отца', dative: 'отцу', accusative: 'отца', instrumental: 'отцом', prepositional: 'отце' } },
  { word: 'конь', gender: 'm', difficulty: 'hard', cases: { nominative: 'конь', genitive: 'коня', dative: 'коню', accusative: 'коня', instrumental: 'конём', prepositional: 'коне' } },
  { word: 'день', gender: 'm', difficulty: 'hard', cases: { nominative: 'день', genitive: 'дня', dative: 'дню', accusative: 'день', instrumental: 'днём', prepositional: 'дне' } },
  { word: 'путь', gender: 'm', difficulty: 'hard', cases: { nominative: 'путь', genitive: 'пути', dative: 'пути', accusative: 'путь', instrumental: 'путём', prepositional: 'пути' } },
  { word: 'имя', gender: 'n', difficulty: 'hard', cases: { nominative: 'имя', genitive: 'имени', dative: 'имени', accusative: 'имя', instrumental: 'именем', prepositional: 'имени' } },
  { word: 'время', gender: 'n', difficulty: 'hard', cases: { nominative: 'время', genitive: 'времени', dative: 'времени', accusative: 'время', instrumental: 'временем', prepositional: 'времени' } },
  { word: 'дочь', gender: 'f', difficulty: 'hard', cases: { nominative: 'дочь', genitive: 'дочери', dative: 'дочери', accusative: 'дочь', instrumental: 'дочерью', prepositional: 'дочери' } },
  { word: 'мать', gender: 'f', difficulty: 'hard', cases: { nominative: 'мать', genitive: 'матери', dative: 'матери', accusative: 'мать', instrumental: 'матерью', prepositional: 'матери' } },
  { word: 'нож', gender: 'm', difficulty: 'hard', cases: { nominative: 'нож', genitive: 'ножа', dative: 'ножу', accusative: 'нож', instrumental: 'ножом', prepositional: 'ноже' } },
  { word: 'карандаш', gender: 'm', difficulty: 'hard', cases: { nominative: 'карандаш', genitive: 'карандаша', dative: 'карандашу', accusative: 'карандаш', instrumental: 'карандашом', prepositional: 'карандаше' } },
]

const CASE_NAMES: Record<CaseType, { name: string; question: string }> = {
  nominative: { name: 'Именительный', question: 'кто? что?' },
  genitive: { name: 'Родительный', question: 'кого? чего?' },
  dative: { name: 'Дательный', question: 'кому? чему?' },
  accusative: { name: 'Винительный', question: 'кого? что?' },
  instrumental: { name: 'Творительный', question: 'кем? чем?' },
  prepositional: { name: 'Предложный', question: 'о ком? о чём?' }
}

const CASE_COLORS: Record<CaseType, string> = {
  nominative: 'bg-blue-500/20 border-blue-400 text-blue-300',
  genitive: 'bg-green-500/20 border-green-400 text-green-300',
  dative: 'bg-yellow-500/20 border-yellow-400 text-yellow-300',
  accusative: 'bg-red-500/20 border-red-400 text-red-300',
  instrumental: 'bg-purple-500/20 border-purple-400 text-purple-300',
  prepositional: 'bg-cyan-500/20 border-cyan-400 text-cyan-300'
}

export default function WordCases() {
  const { addXP } = useSchool()
  const { playSound } = useSound()
  const [currentWord, setCurrentWord] = useState<WordCase | null>(null)
  const [targetCase, setTargetCase] = useState<CaseType | null>(null)
  const [userAnswer, setUserAnswer] = useState('')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)
  const [showResult, setShowResult] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('easy')
  const [usedWords, setUsedWords] = useState<Set<number>>(new Set())
  const [mode, setMode] = useState<'menu' | 'game'>('menu')

  const getFilteredWords = useCallback(() => {
    return WORD_CASES.filter(w => w.difficulty === difficulty)
  }, [difficulty])

  const getNextWord = useCallback(() => {
    const filtered = getFilteredWords()
    const available = filtered
      .map((w, i) => ({ w, originalIndex: WORD_CASES.indexOf(w) }))
      .filter(item => !usedWords.has(item.originalIndex))
    
    if (available.length === 0) {
      setGameOver(true)
      return null
    }
    
    const randomIndex = Math.floor(Math.random() * available.length)
    const word = available[randomIndex].w
    
    const cases: CaseType[] = ['nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional']
    const randomCase = cases[Math.floor(Math.random() * cases.length)]
    
    return { word, targetCase: randomCase }
  }, [getFilteredWords, usedWords])

  useEffect(() => {
    if (mode === 'game' && !currentWord && !gameOver) {
      const next = getNextWord()
      if (next) {
        setCurrentWord(next.word)
        setTargetCase(next.targetCase)
      }
    }
  }, [mode, currentWord, gameOver, getNextWord])

  const startGame = (diff: 'easy' | 'medium' | 'hard') => {
    setDifficulty(diff)
    setScore(0)
    setStreak(0)
    setTotalQuestions(0)
    setUsedWords(new Set())
    setGameOver(false)
    setUserAnswer('')
    setShowResult(false)
    setMode('game')
    const filtered = WORD_CASES.filter(w => w.difficulty === diff)
    const randomIndex = Math.floor(Math.random() * filtered.length)
    const word = filtered[randomIndex]
    setCurrentWord(word)
    setUsedWords(new Set([WORD_CASES.indexOf(word)]))
    const cases: CaseType[] = ['nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional']
    setTargetCase(cases[Math.floor(Math.random() * cases.length)])
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!currentWord || !targetCase || showResult) return
    
    const answer = userAnswer.trim().toLowerCase()
    const correct = currentWord.cases[targetCase].toLowerCase()
    
    setShowResult(true)
    setTotalQuestions(prev => prev + 1)
    
    const isCorrect = answer === correct
    
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
      const originalIndex = WORD_CASES.indexOf(currentWord)
      const newUsed = new Set(usedWords).add(originalIndex)
      setUsedWords(newUsed)
      setUserAnswer('')
      setShowResult(false)
      
      const filtered = WORD_CASES.filter(w => w.difficulty === difficulty)
      const available = filtered.filter(w => !newUsed.has(WORD_CASES.indexOf(w)))
      
      if (available.length === 0) {
        setGameOver(true)
      } else {
        const nextW = available[Math.floor(Math.random() * available.length)]
        setCurrentWord(nextW)
        const cases: CaseType[] = ['nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional']
        setTargetCase(cases[Math.floor(Math.random() * cases.length)])
      }
    }, 2500)
  }

  const resetGame = () => {
    setMode('menu')
    setCurrentWord(null)
    setGameOver(false)
  }

  if (mode === 'menu') {
    return (
      <div className="bg-gradient-to-br from-violet-900/50 to-purple-900/50 rounded-2xl p-6 backdrop-blur-sm border border-violet-500/30">
        <h2 className="text-2xl font-bold text-violet-300 mb-6 flex items-center gap-2">
          <BookOpen className="w-7 h-7" />
          Падежи
        </h2>
        
        <p className="text-violet-200 mb-6">
          Измените форму слова в нужном падеже. Запомните 6 падежей русского языка!
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
                {diff === 'easy' ? 'Простые слова' : diff === 'medium' ? 'Обычные' : 'Особые формы'}
              </div>
            </button>
          ))}
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
          {Object.entries(CASE_NAMES).map(([key, value]) => (
            <div key={key} className={`${CASE_COLORS[key as CaseType]} rounded-lg p-2 border`}>
              <div className="text-xs font-bold">{value.name}</div>
              <div className="text-xs opacity-75">{value.question}</div>
            </div>
          ))}
        </div>
      </div>
    )
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-violet-900/50 to-purple-900/50 rounded-2xl p-6 backdrop-blur-sm border border-violet-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-violet-300 mb-2">Отлично!</h2>
        <p className="text-violet-200 mb-4">
          Результат: {score} XP за {totalQuestions} вопросов
        </p>
        <div className="flex gap-4 justify-center">
          <button
            onClick={() => startGame(difficulty)}
            className="px-6 py-3 bg-violet-500 hover:bg-violet-400 rounded-xl font-bold text-white transition-colors"
          >
            Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl font-bold text-violet-200 transition-colors"
          >
            Меню
          </button>
        </div>
      </div>
    )
  }

  if (!currentWord || !targetCase) return null

  return (
    <div className="bg-gradient-to-br from-violet-900/50 to-purple-900/50 rounded-2xl p-6 backdrop-blur-sm border border-violet-500/30">
      <div className="flex justify-between items-center mb-4">
        <div className={`${CASE_COLORS[targetCase]} px-3 py-1 rounded-lg border text-sm`}>
          {CASE_NAMES[targetCase].name}
        </div>
        <div className="flex items-center gap-4">
          <span className="text-violet-300">Серия: {streak}🔥</span>
          <span className="text-violet-300">Очки: {score}</span>
        </div>
      </div>

      <div className="bg-white/10 rounded-xl p-6 mb-6 text-center">
        <p className="text-violet-300 text-sm mb-2">Слово в именительном падеже:</p>
        <p className="text-3xl font-bold text-white mb-4">{currentWord.word}</p>
        <div className={`${CASE_COLORS[targetCase]} rounded-lg p-3 border`}>
          <p className="text-sm">Поставьте в {CASE_NAMES[targetCase].name.toLowerCase()} падеж</p>
          <p className="text-xs opacity-75">({CASE_NAMES[targetCase].question})</p>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          value={userAnswer}
          onChange={(e) => setUserAnswer(e.target.value)}
          placeholder="Введите форму слова"
          className="w-full bg-white/10 border border-violet-500/30 rounded-xl px-4 py-3 text-white placeholder-violet-300 focus:outline-none focus:border-violet-400 text-xl text-center"
          autoFocus
        />
      </form>

      {showResult && (
        <div className={`mt-4 p-4 rounded-lg text-center ${
          userAnswer.trim().toLowerCase() === currentWord.cases[targetCase].toLowerCase()
            ? 'bg-green-500/20 text-green-300'
            : 'bg-red-500/20 text-red-300'
        }`}>
          <p className="font-bold mb-1">
            {userAnswer.trim().toLowerCase() === currentWord.cases[targetCase].toLowerCase()
              ? '✅ Правильно!'
              : `❌ Неправильно`}
          </p>
          <p className="text-sm">
            {currentWord.word} → {currentWord.cases[targetCase]}
          </p>
          <p className="text-xs opacity-75 mt-1">
            {CASE_NAMES[targetCase].name}: {CASE_NAMES[targetCase].question}
          </p>
        </div>
      )}

      <button
        onClick={() => handleSubmit({ preventDefault: () => {} } as React.FormEvent)}
        disabled={!userAnswer.trim() || showResult}
        className="mt-4 w-full py-3 bg-violet-500 hover:bg-violet-400 disabled:opacity-50 rounded-xl font-bold text-white transition-colors"
      >
        Проверить
      </button>

      <div className="mt-4 flex justify-between items-center">
        <div className="text-sm text-violet-400">
          Вопрос {totalQuestions + 1} из {getFilteredWords().length}
        </div>
        <button
          onClick={resetGame}
          className="flex items-center gap-2 text-violet-400 hover:text-violet-300 transition-colors"
        >
          <RotateCcw className="w-4 h-4" />
          Меню
        </button>
      </div>
    </div>
  )
}
