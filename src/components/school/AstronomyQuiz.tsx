'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Sparkles, Star, Trophy, RotateCcw, Zap, Moon, Sun, Rocket } from 'lucide-react'

interface Question {
  q: string
  options: string[]
  correct: number
  fact: string
}

const QUESTIONS: Question[] = [
  { 
    q: 'Какая планета ближе всех к Солнцу?', 
    options: ['Венера', 'Меркурий', 'Земля', 'Марс'], 
    correct: 1,
    fact: 'Меркурий находится на расстоянии около 58 млн км от Солнца.'
  },
  { 
    q: 'Сколько планет в Солнечной системе?', 
    options: ['7', '8', '9', '10'], 
    correct: 1,
    fact: 'Плутон был исключён из списка планет в 2006 году.'
  },
  { 
    q: 'Какая самая большая планета Солнечной системы?', 
    options: ['Сатурн', 'Юпитер', 'Нептун', 'Уран'], 
    correct: 1,
    fact: 'Юпитер настолько велик, что в него поместится 1300 Земель!'
  },
  { 
    q: 'Какая планета известна своими кольцами?', 
    options: ['Юпитер', 'Уран', 'Сатурн', 'Нептун'], 
    correct: 2,
    fact: 'Кольца Сатурна состоят из льда и камней.'
  },
  { 
    q: 'Как называется наша галактика?', 
    options: ['Андромеда', 'Млечный Путь', 'Треугольник', 'Большая Медведица'], 
    correct: 1,
    fact: 'Млечный Путь содержит от 200 до 400 миллиардов звёзд!'
  },
  { 
    q: 'Какая планета называется "красной"?', 
    options: ['Венера', 'Юпитер', 'Марс', 'Меркурий'], 
    correct: 2,
    fact: 'Красный цвет Марса обусловлен оксидом железа (ржавчиной) на его поверхности.'
  },
  { 
    q: 'Что такое Солнце?', 
    options: ['Планета', 'Звезда', 'Спутник', 'Астероид'], 
    correct: 1,
    fact: 'Солнце — это жёлтый карлик, возраст которого около 4.6 млрд лет.'
  },
  { 
    q: 'Сколько спутников у Земли?', 
    options: ['0', '1', '2', '3'], 
    correct: 1,
    fact: 'Луна — единственный естественный спутник Земли.'
  },
  { 
    q: 'Какая планета вращается "лёжа на боку"?', 
    options: ['Нептун', 'Сатурн', 'Уран', 'Юпитер'], 
    correct: 2,
    fact: 'Ось вращения Урана наклонена на 98 градусов!'
  },
  { 
    q: 'Как называется ближайшая к Земле звезда?', 
    options: ['Полярная', 'Сириус', 'Солнце', 'Альфа Центавра'], 
    correct: 2,
    fact: 'Солнце — ближайшая к Земле звезда, следующая — Проксима Центавра.'
  },
  { 
    q: 'Какой космический объект имеет "хвост"?', 
    options: ['Астероид', 'Комета', 'Метеор', 'Планета'], 
    correct: 1,
    fact: 'Хвост кометы образуется при приближении к Солнцу из газов и пыли.'
  },
  { 
    q: 'Что такое чёрная дыра?', 
    options: ['Тёмная планета', 'Область с огромной гравитацией', 'Тёмная туманность', 'Пустота в космосе'], 
    correct: 1,
    fact: 'Гравитация чёрной дыры настолько сильна, что даже свет не может её покинуть.'
  },
]

export default function AstronomyQuiz() {
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
      addPoints(20)
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
      <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-900/40 via-purple-900/40 to-blue-900/40 border-2 border-indigo-500/30 text-center relative overflow-hidden">
        {/* Декоративные звёзды */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          {[...Array(20)].map((_, i) => (
            <Star
              key={i}
              className="absolute w-2 h-2 text-yellow-300/30 animate-pulse"
              style={{
                top: `${Math.random() * 100}%`,
                left: `${Math.random() * 100}%`,
                animationDelay: `${Math.random() * 2}s`
              }}
            />
          ))}
        </div>
        
        <div className="relative z-10">
          <Rocket className="w-16 h-16 text-indigo-400 mx-auto mb-4" />
          <h3 className="text-2xl font-bold text-white mb-2">Миссия завершена!</h3>
          <p className="text-4xl font-bold text-indigo-300 mb-2">{score} / {questions.length}</p>
          <p className="text-lg text-indigo-200 mb-4">
            {percentage >= 80 ? 'Ты настоящий космонавт! 🚀' : percentage >= 60 ? 'Хороший полёт! 🌟' : 'Продолжай исследовать космос! 🌌'}
          </p>
          <p className="text-indigo-300 mb-4">Заработано XP: {score * 20}</p>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white font-bold transition-colors flex items-center gap-2 mx-auto"
          >
            <RotateCcw className="w-4 h-4" /> Новый полёт
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-900/40 via-purple-900/40 to-blue-900/40 border-2 border-indigo-500/30 relative overflow-hidden">
      {/* Декоративные звёзды */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        {[...Array(15)].map((_, i) => (
          <Sparkles
            key={i}
            className="absolute w-1 h-1 text-yellow-200/40 animate-pulse"
            style={{
              top: `${Math.random() * 100}%`,
              left: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 2}s`
            }}
          />
        ))}
      </div>

      <div className="relative z-10">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-bold text-white flex items-center gap-2">
            <Moon className="w-5 h-5 text-indigo-300" />
            Астрономия
          </h3>
          <div className="flex items-center gap-2">
            <span className="px-3 py-1 rounded-full text-sm bg-indigo-500/20 text-indigo-300 flex items-center gap-1">
              <Sun className="w-3 h-3" />
              Космос
            </span>
            <span className="text-indigo-300 text-sm">
              {currentIndex + 1}/{questions.length}
            </span>
          </div>
        </div>

        <div className="bg-white/5 rounded-xl p-4 mb-4 backdrop-blur-sm">
          <p className="text-lg text-white">{currentQuestion.q}</p>
        </div>

        <div className="grid grid-cols-2 gap-3">
          {currentQuestion.options.map((opt, i) => {
            const isCorrect = i === currentQuestion.correct
            const isSelected = i === selectedAnswer
            
            let buttonClass = 'p-4 rounded-xl text-white font-bold transition-all backdrop-blur-sm '
            
            if (!answered) {
              buttonClass += 'bg-white/10 hover:bg-white/20 hover:scale-[1.02] border border-white/10'
            } else if (isCorrect) {
              buttonClass += 'bg-indigo-500/50 border-2 border-indigo-400'
            } else if (isSelected && !isCorrect) {
              buttonClass += 'bg-rose-500/50 border-2 border-rose-400'
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
          <div className="mt-4 p-3 bg-indigo-500/20 rounded-xl border border-indigo-500/30 backdrop-blur-sm">
            <p className="text-indigo-200 text-sm">🌌 Факт: {currentQuestion.fact}</p>
          </div>
        )}

        {answered && (
          <button
            onClick={nextQuestion}
            className="mt-4 w-full p-3 bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white font-bold transition-colors"
          >
            {currentIndex < questions.length - 1 ? 'Следующий вопрос →' : 'Завершить миссию'}
          </button>
        )}

        <div className="flex items-center justify-between mt-4 text-indigo-300 text-sm">
          <span className="flex items-center gap-1"><Star className="w-4 h-4" /> Счёт: {score}</span>
          <span className="flex items-center gap-1"><Zap className="w-4 h-4" /> XP: {score * 20}</span>
        </div>
      </div>
    </div>
  )
}
