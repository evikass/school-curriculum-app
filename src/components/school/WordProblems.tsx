'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Calculator, Star, Trophy, RotateCcw, Zap, BookOpen } from 'lucide-react'

interface Problem {
  problem: string
  options: string[]
  correct: number
  type: 'motion' | 'percent' | 'proportion' | 'work' | 'time'
  solution: string
}

const PROBLEMS: Problem[] = [
  // Задачи на движение
  {
    problem: 'Автомобиль едет со скоростью 60 км/ч. Какое расстояние он проедет за 3 часа?',
    options: ['120 км', '180 км', '200 км', '160 км'],
    correct: 1,
    type: 'motion',
    solution: 'S = v × t = 60 × 3 = 180 км'
  },
  {
    problem: 'Велосипедист проехал 45 км за 3 часа. С какой скоростью он ехал?',
    options: ['12 км/ч', '15 км/ч', '18 км/ч', '20 км/ч'],
    correct: 1,
    type: 'motion',
    solution: 'v = S ÷ t = 45 ÷ 3 = 15 км/ч'
  },
  {
    problem: 'Поезд идёт со скоростью 80 км/ч. За сколько часов он проедет 320 км?',
    options: ['3 часа', '4 часа', '5 часов', '6 часов'],
    correct: 1,
    type: 'motion',
    solution: 't = S ÷ v = 320 ÷ 80 = 4 часа'
  },
  // Задачи на проценты
  {
    problem: 'В классе 30 учеников. 40% из них — девочки. Сколько девочек в классе?',
    options: ['10', '12', '15', '18'],
    correct: 1,
    type: 'percent',
    solution: '30 × 40% = 30 × 0,4 = 12 девочек'
  },
  {
    problem: 'Цена товара 500 рублей. Скидка составляет 20%. Сколько стоит товар со скидкой?',
    options: ['350 руб', '380 руб', '400 руб', '420 руб'],
    correct: 2,
    type: 'percent',
    solution: '500 - (500 × 0,2) = 500 - 100 = 400 рублей'
  },
  {
    problem: 'В книге 200 страниц. Ученик прочитал 25% книги. Сколько страниц он прочитал?',
    options: ['40', '50', '60', '75'],
    correct: 1,
    type: 'percent',
    solution: '200 × 25% = 200 × 0,25 = 50 страниц'
  },
  // Задачи на пропорции
  {
    problem: 'За 4 кг яблок заплатили 200 рублей. Сколько стоят 7 кг яблок?',
    options: ['300 руб', '350 руб', '380 руб', '400 руб'],
    correct: 1,
    type: 'proportion',
    solution: '200 ÷ 4 × 7 = 50 × 7 = 350 рублей'
  },
  {
    problem: '5 рабочих выполняют работу за 10 дней. За сколько дней выполнят эту работу 10 рабочих?',
    options: ['3 дня', '4 дня', '5 дней', '6 дней'],
    correct: 2,
    type: 'proportion',
    solution: 'Чем больше рабочих, тем меньше времени: 10 дней × 5 ÷ 10 = 5 дней'
  },
  {
    problem: 'На карте расстояние между городами 6 см. Масштаб карты 1:1000000. Каково реальное расстояние?',
    options: ['6 км', '60 км', '600 км', '6000 км'],
    correct: 1,
    type: 'proportion',
    solution: '6 × 1000000 см = 6000000 см = 60 км'
  },
  // Задачи на работу
  {
    problem: 'Мастер делает 15 деталей в час, ученик — 10 деталей. За сколько часов они сделают 100 деталей вместе?',
    options: ['3 часа', '4 часа', '5 часов', '6 часов'],
    correct: 1,
    type: 'work',
    solution: 'Вместе: 15 + 10 = 25 деталей/час. 100 ÷ 25 = 4 часа'
  },
  {
    problem: 'Один насос наполняет бассейн за 6 часов, другой — за 3 часа. За сколько часов они наполнят бассейн вместе?',
    options: ['1 час', '2 часа', '3 часа', '4 часа'],
    correct: 1,
    type: 'work',
    solution: 'За 1 час: 1/6 + 1/3 = 1/2 бассейна. Значит, весь бассейн за 2 часа'
  },
  // Задачи на время
  {
    problem: 'Поезд вышел в 14:35 и прибыл в 19:20. Сколько времени он был в пути?',
    options: ['4 ч 35 мин', '4 ч 45 мин', '5 ч 15 мин', '5 ч 45 мин'],
    correct: 1,
    type: 'time',
    solution: 'От 14:35 до 19:20 = 4 часа 45 минут'
  },
  {
    problem: 'Урок длится 45 минут. Перемена — 15 минут. Уроки начинаются в 8:30. Во сколько закончится 4-й урок?',
    options: ['11:30', '12:00', '12:30', '13:00'],
    correct: 1,
    type: 'time',
    solution: '4 урока = 180 мин, 3 перемены = 45 мин. 8:30 + 225 мин = 12:00'
  },
]

const TYPE_CONFIG = {
  motion: { label: 'На движение', icon: '🚗', color: 'from-blue-500/20 to-cyan-500/20', border: 'border-blue-500/30' },
  percent: { label: 'На проценты', icon: '📊', color: 'from-green-500/20 to-emerald-500/20', border: 'border-green-500/30' },
  proportion: { label: 'На пропорции', icon: '⚖️', color: 'from-orange-500/20 to-yellow-500/20', border: 'border-orange-500/30' },
  work: { label: 'На работу', icon: '🔧', color: 'from-purple-500/20 to-pink-500/20', border: 'border-purple-500/30' },
  time: { label: 'На время', icon: '⏰', color: 'from-rose-500/20 to-red-500/20', border: 'border-rose-500/30' },
}

export default function WordProblems() {
  const { addPoints } = useSchool()
  const [currentIndex, setCurrentIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [answered, setAnswered] = useState(false)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [showSolution, setShowSolution] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [problems] = useState(() => [...PROBLEMS].sort(() => Math.random() - 0.5))

  const currentProblem = problems[currentIndex]

  const handleAnswer = (idx: number) => {
    if (answered) return
    setAnswered(true)
    setSelectedAnswer(idx)
    
    if (idx === currentProblem.correct) {
      addPoints(25)
      setScore(s => s + 1)
    }
    setShowSolution(true)
  }

  const nextProblem = () => {
    if (currentIndex < problems.length - 1) {
      setCurrentIndex(i => i + 1)
      setAnswered(false)
      setSelectedAnswer(null)
      setShowSolution(false)
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
    setShowSolution(false)
  }

  if (gameOver) {
    const percentage = Math.round((score / problems.length) * 100)
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-teal-500/20 to-cyan-500/20 border-2 border-teal-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-white mb-2">Результат</h3>
        <p className="text-4xl font-bold text-teal-300 mb-2">{score} / {problems.length}</p>
        <p className="text-lg text-teal-200 mb-4">
          {percentage >= 80 ? 'Отличный математик! 📐' : percentage >= 60 ? 'Хорошие вычисления! 🔢' : 'Продолжай практиковаться! ✏️'}
        </p>
        <p className="text-teal-300 mb-4">Заработано XP: {score * 25}</p>
        <button
          onClick={resetGame}
          className="px-6 py-3 bg-teal-500 hover:bg-teal-600 rounded-xl text-white font-bold transition-colors flex items-center gap-2 mx-auto"
        >
          <RotateCcw className="w-4 h-4" /> Новые задачи
        </button>
      </div>
    )
  }

  const typeConfig = TYPE_CONFIG[currentProblem.type]

  return (
    <div className={`p-6 rounded-2xl bg-gradient-to-br ${typeConfig.color} border-2 ${typeConfig.border}`}>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-bold text-white flex items-center gap-2">
          <Calculator className="w-5 h-5 text-teal-400" />
          Текстовые задачи
        </h3>
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 rounded-full text-sm bg-teal-500/20 text-teal-300">
            {typeConfig.icon} {typeConfig.label}
          </span>
          <span className="text-teal-300 text-sm">
            {currentIndex + 1}/{problems.length}
          </span>
        </div>
      </div>

      <div className="bg-white/5 rounded-xl p-4 mb-4">
        <div className="flex items-start gap-2">
          <BookOpen className="w-5 h-5 text-teal-400 flex-shrink-0 mt-0.5" />
          <p className="text-white leading-relaxed">{currentProblem.problem}</p>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {currentProblem.options.map((opt, i) => {
          const isCorrect = i === currentProblem.correct
          const isSelected = i === selectedAnswer
          
          let buttonClass = 'p-4 rounded-xl text-white font-bold transition-all '
          
          if (!answered) {
            buttonClass += 'bg-white/10 hover:bg-white/20 hover:scale-[1.02]'
          } else if (isCorrect) {
            buttonClass += 'bg-teal-500/50 border-2 border-teal-400'
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

      {showSolution && (
        <div className="mt-4 p-3 bg-teal-500/20 rounded-xl border border-teal-500/30">
          <p className="text-teal-200 text-sm font-medium mb-1">📐 Решение:</p>
          <p className="text-white">{currentProblem.solution}</p>
        </div>
      )}

      {answered && (
        <button
          onClick={nextProblem}
          className="mt-4 w-full p-3 bg-teal-500 hover:bg-teal-600 rounded-xl text-white font-bold transition-colors"
        >
          {currentIndex < problems.length - 1 ? 'Следующая задача →' : 'Показать результат'}
        </button>
      )}

      <div className="flex items-center justify-between mt-4 text-teal-300 text-sm">
        <span className="flex items-center gap-1"><Star className="w-4 h-4" /> Решено: {score}</span>
        <span className="flex items-center gap-1"><Zap className="w-4 h-4" /> XP: {score * 25}</span>
      </div>
    </div>
  )
}
