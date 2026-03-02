'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { FlaskConical, Star, Trophy, RotateCcw, Zap } from 'lucide-react'

type Difficulty = 'easy' | 'medium' | 'hard'

interface Question {
  q: string
  options: string[]
  correct: number
  difficulty: Difficulty
  fact?: string
}

const QUESTIONS: Question[] = [
  // Easy
  { q: 'Какой химический элемент обозначается символом H?', options: ['Гелий', 'Водород', 'Кислород', 'Азот'], correct: 1, difficulty: 'easy', fact: 'Водород — самый лёгкий элемент во Вселенной!' },
  { q: 'Какая формула у воды?', options: ['CO2', 'H2O', 'NaCl', 'O2'], correct: 1, difficulty: 'easy', fact: 'Вода покрывает 71% поверхности Земли.' },
  { q: 'Какой газ мы вдыхаем для дыхания?', options: ['Азот', 'Кислород', 'Углекислый газ', 'Водород'], correct: 1, difficulty: 'easy', fact: 'Кислород составляет 21% атмосферы Земли.' },
  { q: 'Какой элемент является основой органической химии?', options: ['Азот', 'Кислород', 'Углерод', 'Водород'], correct: 2, difficulty: 'easy', fact: 'Все живые организмы состоят из углеродных соединений.' },
  // Medium
  { q: 'Какой металл плавится при комнатной температуре?', options: ['Железо', 'Ртуть', 'Медь', 'Алюминий'], correct: 1, difficulty: 'medium', fact: 'Ртуть — единственный жидкий металл при комнатной температуре.' },
  { q: 'Чему равна атомная масса углерода?', options: ['6', '12', '14', '16'], correct: 1, difficulty: 'medium', fact: 'Атомная масса углерода равна 12 атомным единицам массы.' },
  { q: 'Какой элемент имеет символ Na?', options: ['Азот', 'Натрий', 'Неон', 'Никель'], correct: 1, difficulty: 'medium', fact: 'Натрий — мягкий серебристый металл, reacts vigorously с водой.' },
  { q: 'Какое вещество образуется при горении водорода?', options: ['Углекислый газ', 'Вода', 'Азот', 'Метан'], correct: 1, difficulty: 'medium', fact: 'При горении водорода выделяется много энергии и образуется вода.' },
  // Hard
  { q: 'Сколько электронов на внешнем уровне у кислорода?', options: ['4', '6', '8', '2'], correct: 1, difficulty: 'hard', fact: 'Кислород имеет 6 валентных электронов.' },
  { q: 'Какая группа элементов называется галогенами?', options: ['Щелочные металлы', 'Благородные газы', 'Галогены', 'Переходные металлы'], correct: 2, difficulty: 'hard', fact: 'Галогены — это фтор, хлор, бром, йод и астат.' },
  { q: 'Чему равно число Авогадро?', options: ['6.02 × 10²³', '3.14 × 10²³', '9.81 × 10²³', '1.60 × 10²³'], correct: 0, difficulty: 'hard', fact: 'Число Авогадро показывает количество частиц в одном моле вещества.' },
  { q: 'Какой оксид называется сухим льдом?', options: ['CO2', 'N2O', 'SO2', 'NO2'], correct: 0, difficulty: 'hard', fact: 'Сухой лёд — это твёрдый углекислый газ, который сублимирует при -78°C.' },
]

const DIFFICULTY_CONFIG = {
  easy: { xp: 10, color: 'from-green-500/20 to-emerald-500/20', border: 'border-green-500/30', badge: 'bg-green-500/20 text-green-300' },
  medium: { xp: 15, color: 'from-yellow-500/20 to-orange-500/20', border: 'border-yellow-500/30', badge: 'bg-yellow-500/20 text-yellow-300' },
  hard: { xp: 25, color: 'from-red-500/20 to-rose-500/20', border: 'border-red-500/30', badge: 'bg-red-500/20 text-red-300' },
}

const DIFFICULTY_LABELS = {
  easy: 'Легко',
  medium: 'Средне',
  hard: 'Сложно',
}

export default function ChemistryQuiz() {
  const { addPoints } = useSchool()
  const [selectedDifficulty, setSelectedDifficulty] = useState<Difficulty | null>(null)
  const [currentIndex, setCurrentIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [answered, setAnswered] = useState(false)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [showFact, setShowFact] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [questions, setQuestions] = useState<Question[]>([])

  const startGame = (diff: Difficulty) => {
    setSelectedDifficulty(diff)
    const filtered = QUESTIONS.filter(q => q.difficulty === diff)
    // Перемешиваем вопросы
    const shuffled = [...filtered].sort(() => Math.random() - 0.5)
    setQuestions(shuffled)
    setCurrentIndex(0)
    setScore(0)
    setGameOver(false)
    setAnswered(false)
    setSelectedAnswer(null)
    setShowFact(false)
  }

  const currentQuestion = questions[currentIndex]

  const handleAnswer = (idx: number) => {
    if (answered) return
    setAnswered(true)
    setSelectedAnswer(idx)
    
    if (idx === currentQuestion.correct) {
      const xp = DIFFICULTY_CONFIG[currentQuestion.difficulty].xp
      addPoints(xp)
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
    setSelectedDifficulty(null)
    setQuestions([])
    setCurrentIndex(0)
    setScore(0)
    setGameOver(false)
    setAnswered(false)
    setSelectedAnswer(null)
    setShowFact(false)
  }

  // Выбор сложности
  if (!selectedDifficulty) {
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 border-2 border-purple-500/30">
        <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <FlaskConical className="w-6 h-6 text-purple-400" />
          Викторина по химии
        </h3>
        <p className="text-purple-200 mb-6">Выберите уровень сложности:</p>
        <div className="space-y-3">
          {(Object.keys(DIFFICULTY_CONFIG) as Difficulty[]).map(diff => (
            <button
              key={diff}
              onClick={() => startGame(diff)}
              className={`w-full p-4 rounded-xl bg-gradient-to-r ${DIFFICULTY_CONFIG[diff].color} border-2 ${DIFFICULTY_CONFIG[diff].border} hover:scale-[1.02] transition-all flex items-center justify-between`}
            >
              <span className="text-white font-bold">{DIFFICULTY_LABELS[diff]}</span>
              <span className={`px-3 py-1 rounded-full text-sm ${DIFFICULTY_CONFIG[diff].badge} flex items-center gap-1`}>
                <Zap className="w-3 h-3" /> +{DIFFICULTY_CONFIG[diff].xp} XP
              </span>
            </button>
          ))}
        </div>
      </div>
    )
  }

  // Результаты
  if (gameOver) {
    const percentage = Math.round((score / questions.length) * 100)
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 border-2 border-purple-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-white mb-2">Результат</h3>
        <p className="text-4xl font-bold text-purple-300 mb-2">{score} / {questions.length}</p>
        <p className="text-lg text-purple-200 mb-4">
          {percentage >= 80 ? 'Отлично! 🎉' : percentage >= 60 ? 'Хорошо! 👍' : 'Продолжай учиться! 📚'}
        </p>
        <p className="text-purple-300 mb-4">Заработано XP: {score * DIFFICULTY_CONFIG[selectedDifficulty].xp}</p>
        <div className="flex gap-3 justify-center">
          <button
            onClick={() => startGame(selectedDifficulty)}
            className="px-6 py-3 bg-purple-500 hover:bg-purple-600 rounded-xl text-white font-bold transition-colors flex items-center gap-2"
          >
            <RotateCcw className="w-4 h-4" /> Ещё раз
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            Другая сложность
          </button>
        </div>
      </div>
    )
  }

  if (!currentQuestion) return null

  const config = DIFFICULTY_CONFIG[currentQuestion.difficulty]

  return (
    <div className={`p-6 rounded-2xl bg-gradient-to-br ${config.color} border-2 ${config.border}`}>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-bold text-white flex items-center gap-2">
          <FlaskConical className="w-5 h-5 text-purple-400" />
          Химия
        </h3>
        <div className="flex items-center gap-2">
          <span className={`px-3 py-1 rounded-full text-sm ${config.badge}`}>
            {DIFFICULTY_LABELS[currentQuestion.difficulty]}
          </span>
          <span className="text-purple-300 text-sm">
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

      {showFact && currentQuestion.fact && (
        <div className="mt-4 p-3 bg-purple-500/20 rounded-xl border border-purple-500/30">
          <p className="text-purple-200 text-sm">💡 {currentQuestion.fact}</p>
        </div>
      )}

      {answered && (
        <button
          onClick={nextQuestion}
          className="mt-4 w-full p-3 bg-purple-500 hover:bg-purple-600 rounded-xl text-white font-bold transition-colors"
        >
          {currentIndex < questions.length - 1 ? 'Следующий вопрос →' : 'Показать результат'}
        </button>
      )}

      <div className="flex items-center justify-between mt-4 text-purple-300 text-sm">
        <span className="flex items-center gap-1"><Star className="w-4 h-4" /> Счёт: {score}</span>
        <span className="flex items-center gap-1"><Zap className="w-4 h-4" /> XP: {score * config.xp}</span>
      </div>
    </div>
  )
}
