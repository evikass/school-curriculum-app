'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Leaf, Star, Trophy, RotateCcw, Zap, Heart, Bug, Flower2 } from 'lucide-react'

interface Question {
  q: string
  options: string[]
  correct: number
  category: 'animals' | 'plants' | 'human'
  fact: string
}

const QUESTIONS: Question[] = [
  // Животные
  { 
    q: 'Какое животное является самым большим на Земле?', 
    options: ['Слон', 'Синий кит', 'Жираф', 'Белая акула'], 
    correct: 1, 
    category: 'animals',
    fact: 'Синий кит может достигать длины 30 метров и весить до 200 тонн!'
  },
  { 
    q: 'Сколько ног у паука?', 
    options: ['6', '8', '10', '4'], 
    correct: 1, 
    category: 'animals',
    fact: 'Пауки — это не насекомые, а паукообразные. У насекомых 6 ног.'
  },
  { 
    q: 'Какое животное может поворачивать голову на 360 градусов?', 
    options: ['Орёл', 'Сова', 'Голубь', 'Сокол'], 
    correct: 1, 
    category: 'animals',
    fact: 'Сова может поворачивать голову на 270 градусов в каждую сторону!'
  },
  { 
    q: 'Какое животное спит вверх ногами?', 
    options: ['Летучая мышь', 'Белка', 'Енот', 'Кошка'], 
    correct: 0, 
    category: 'animals',
    fact: 'Летучие мыши спят вниз головой, чтобы легко взлететь.'
  },
  // Растения
  { 
    q: 'Какой процесс позволяет растениям производить кислород?', 
    options: ['Дыхание', 'Фотосинтез', 'Испарение', 'Гниение'], 
    correct: 1, 
    category: 'plants',
    fact: 'Во время фотосинтеза растения поглощают CO2 и выделяют кислород.'
  },
  { 
    q: 'Какая часть растения поглощает воду из почвы?', 
    options: ['Листья', 'Стебель', 'Корень', 'Цветок'], 
    correct: 2, 
    category: 'plants',
    fact: 'Корни растений могут проникать в почву на глубину десятков метров!'
  },
  { 
    q: 'Какое растение является хищником?', 
    options: ['Роза', 'Росянка', 'Одуванчик', 'Подсолнух'], 
    correct: 1, 
    category: 'plants',
    fact: 'Росянка ловит насекомых с помощью липких капель на листьях.'
  },
  { 
    q: 'Что образуется из цветка после опыления?', 
    options: ['Лист', 'Плод', 'Корень', 'Стебель'], 
    correct: 1, 
    category: 'plants',
    fact: 'Плод защищает семена и помогает их распространению.'
  },
  // Человек
  { 
    q: 'Сколько костей в теле взрослого человека?', 
    options: ['106', '156', '206', '306'], 
    correct: 2, 
    category: 'human',
    fact: 'У новорождённого около 270 костей, но некоторые срастаются.'
  },
  { 
    q: 'Какой орган перекачивает кровь по организму?', 
    options: ['Лёгкие', 'Печень', 'Сердце', 'Почки'], 
    correct: 2, 
    category: 'human',
    fact: 'Сердце делает около 100 000 ударов в день!'
  },
  { 
    q: 'Сколько зубов у взрослого человека?', 
    options: ['24', '28', '32', '36'], 
    correct: 2, 
    category: 'human',
    fact: 'Зубы — самая твёрдая часть человеческого тела.'
  },
  { 
    q: 'Какой орган отвечает за зрение?', 
    options: ['Ухо', 'Глаз', 'Нос', 'Кожа'], 
    correct: 1, 
    category: 'human',
    fact: 'Глаз может различать около 10 миллионов цветов!'
  },
]

const CATEGORY_CONFIG = {
  animals: { icon: Bug, color: 'from-amber-500/20 to-orange-500/20', border: 'border-amber-500/30', label: 'Животные' },
  plants: { icon: Flower2, color: 'from-green-500/20 to-emerald-500/20', border: 'border-green-500/30', label: 'Растения' },
  human: { icon: Heart, color: 'from-rose-500/20 to-pink-500/20', border: 'border-rose-500/30', label: 'Человек' },
}

export default function BiologyQuiz() {
  const { addPoints } = useSchool()
  const [currentIndex, setCurrentIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [answered, setAnswered] = useState(false)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [showFact, setShowFact] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [questions] = useState(() => [...QUESTIONS].sort(() => Math.random() - 0.5))

  const currentQuestion = questions[currentIndex]

  const handleAnswer = (idx: number) => {
    if (answered) return
    setAnswered(true)
    setSelectedAnswer(idx)
    
    if (idx === currentQuestion.correct) {
      addPoints(15)
      setScore(s => s + 1)
    }
    setShowFact(true)
  }

  const nextQuestion = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(i => i + 1)
      setAnswered(false)
      setSelectedAnswer(null)
      setShowFact(false)
    } else {
      setGameOver(true)
    }
  }

  const resetGame = () => {
    setCurrentIndex(0)
    setScore(0)
    setGameOver(false)
    setAnswered(false)
    setSelectedAnswer(null)
    setShowFact(false)
  }

  if (gameOver) {
    const percentage = Math.round((score / questions.length) * 100)
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-green-500/20 to-teal-500/20 border-2 border-green-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-white mb-2">Результат</h3>
        <p className="text-4xl font-bold text-green-300 mb-2">{score} / {questions.length}</p>
        <p className="text-lg text-green-200 mb-4">
          {percentage >= 80 ? 'Отлично! Ты настоящий биолог! 🧬' : percentage >= 60 ? 'Хорошие знания! 🌿' : 'Продолжай изучать природу! 🌱'}
        </p>
        <p className="text-green-300 mb-4">Заработано XP: {score * 15}</p>
        <button
          onClick={resetGame}
          className="px-6 py-3 bg-green-500 hover:bg-green-600 rounded-xl text-white font-bold transition-colors flex items-center gap-2 mx-auto"
        >
          <RotateCcw className="w-4 h-4" /> Играть снова
        </button>
      </div>
    )
  }

  const CategoryIcon = CATEGORY_CONFIG[currentQuestion.category].icon

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-green-500/20 to-teal-500/20 border-2 border-green-500/30">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-bold text-white flex items-center gap-2">
          <Leaf className="w-5 h-5 text-green-400" />
          Биология
        </h3>
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 rounded-full text-sm bg-green-500/20 text-green-300 flex items-center gap-1">
            <CategoryIcon className="w-3 h-3" />
            {CATEGORY_CONFIG[currentQuestion.category].label}
          </span>
          <span className="text-green-300 text-sm">
            {currentIndex + 1}/{questions.length}
          </span>
        </div>
      </div>

      <div className="bg-white/5 rounded-xl p-4 mb-4">
        <p className="text-lg text-white">{currentQuestion.q}</p>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {currentQuestion.options.map((opt, i) => {
          const isCorrect = i === currentQuestion.correct
          const isSelected = i === selectedAnswer
          
          let buttonClass = 'p-4 rounded-xl text-white font-bold transition-all '
          
          if (!answered) {
            buttonClass += 'bg-white/10 hover:bg-white/20 hover:scale-[1.02]'
          } else if (isCorrect) {
            buttonClass += 'bg-green-500/50 border-2 border-green-400'
          } else if (isSelected && !isCorrect) {
            buttonClass += 'bg-red-500/50 border-2 border-red-400'
          } else {
            buttonClass += 'bg-white/5 opacity-50'
          }
          
          return (
            <button
              key={i}
              onClick={() => handleAnswer(i)}
              disabled={answered}
              className={buttonClass}
            >
              <span className="flex items-center justify-center gap-2">
                {opt}
                {answered && isCorrect && <Star className="w-4 h-4 text-yellow-300" />}
              </span>
            </button>
          )
        })}
      </div>

      {showFact && (
        <div className="mt-4 p-3 bg-green-500/20 rounded-xl border border-green-500/30">
          <p className="text-green-200 text-sm">🔬 Интересный факт: {currentQuestion.fact}</p>
        </div>
      )}

      {answered && (
        <button
          onClick={nextQuestion}
          className="mt-4 w-full p-3 bg-green-500 hover:bg-green-600 rounded-xl text-white font-bold transition-colors"
        >
          {currentIndex < questions.length - 1 ? 'Следующий вопрос →' : 'Показать результат'}
        </button>
      )}

      <div className="flex items-center justify-between mt-4 text-green-300 text-sm">
        <span className="flex items-center gap-1"><Star className="w-4 h-4" /> Счёт: {score}</span>
        <span className="flex items-center gap-1"><Zap className="w-4 h-4" /> XP: {score * 15}</span>
      </div>
    </div>
  )
}
