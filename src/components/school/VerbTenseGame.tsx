'use client'

import { useState, useEffect } from 'react'
import { Volume2, Star, Trophy, RotateCcw } from 'lucide-react'

interface VerbTense {
  verb: string
  present: string
  past: string
  future: string
  context: string
}

const VERB_TENSES: VerbTense[] = [
  { verb: 'читать', present: 'читает', past: 'читал', future: 'будет читать', context: 'Мама ___ книгу.' },
  { verb: 'писать', present: 'пишет', past: 'писал', future: 'будет писать', context: 'Ученик ___ упражнение.' },
  { verb: 'бежать', present: 'бежит', past: 'бежал', future: 'будет бежать', context: 'Мальчик ___ быстро.' },
  { verb: 'говорить', present: 'говорит', past: 'говорил', future: 'будет говорить', context: 'Учитель ___ громко.' },
  { verb: 'рисовать', present: 'рисует', past: 'рисовал', future: 'будет рисовать', context: 'Художник ___ картину.' },
  { verb: 'петь', present: 'поёт', past: 'пел', future: 'будет петь', context: 'Певец ___ песню.' },
  { verb: 'спать', present: 'спит', past: 'спал', future: 'будет спать', context: 'Ребёнок ___ в кроватке.' },
  { verb: 'играть', present: 'играет', past: 'играл', future: 'будет играть', context: 'Кошка ___ с мячом.' },
  { verb: 'лететь', present: 'летит', past: 'летел', future: 'будет лететь', context: 'Самолёт ___ высоко.' },
  { verb: 'смотреть', present: 'смотрит', past: 'смотрел', future: 'будет смотреть', context: 'Мы ___ фильм.' },
  { verb: 'слушать', present: 'слушает', past: 'слушал', future: 'будет слушать', context: 'Я ___ музыку.' },
  { verb: 'танцевать', present: 'танцует', past: 'танцевал', future: 'будет танцевать', context: 'Девочка ___ на сцене.' },
]

const TIME_MARKERS = {
  present: ['сейчас', 'в данный момент', 'сегодня', 'обычно', 'каждый день'],
  past: ['вчера', 'на прошлой неделе', 'в прошлом году', 'раньше', 'тогда'],
  future: ['завтра', 'на следующей неделе', 'в будущем году', 'потом', 'скоро']
}

type TenseType = 'present' | 'past' | 'future'

export default function VerbTenseGame() {
  const [currentVerb, setCurrentVerb] = useState<VerbTense | null>(null)
  const [currentTense, setCurrentTense] = useState<TenseType>('present')
  const [marker, setMarker] = useState('')
  const [userAnswer, setUserAnswer] = useState('')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [bestStreak, setBestStreak] = useState(0)
  const [round, setRound] = useState(0)
  const [totalRounds] = useState(10)
  const [showResult, setShowResult] = useState(false)
  const [isCorrect, setIsCorrect] = useState(false)
  const [gameOver, setGameOver] = useState(false)

  const generateQuestion = () => {
    const verb = VERB_TENSES[Math.floor(Math.random() * VERB_TENSES.length)]
    const tenses: TenseType[] = ['present', 'past', 'future']
    const tense = tenses[Math.floor(Math.random() * tenses.length)]
    const markers = TIME_MARKERS[tense]
    const timeMarker = markers[Math.floor(Math.random() * markers.length)]
    
    setCurrentVerb(verb)
    setCurrentTense(tense)
    setMarker(timeMarker)
    setUserAnswer('')
    setShowResult(false)
  }

  useEffect(() => {
    generateQuestion()
  }, [])

  const checkAnswer = () => {
    if (!currentVerb) return

    const correctAnswer = currentVerb[currentTense].toLowerCase().trim()
    const userAnswerNormalized = userAnswer.toLowerCase().trim()
    const correct = userAnswerNormalized === correctAnswer || 
                    userAnswerNormalized.includes(correctAnswer) ||
                    correctAnswer.includes(userAnswerNormalized)

    setIsCorrect(correct)
    setShowResult(true)

    if (correct) {
      setScore(score + 10 + streak * 2)
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
        generateQuestion()
      }
    }, 1500)
  }

  const restartGame = () => {
    setScore(0)
    setStreak(0)
    setRound(0)
    setGameOver(false)
    generateQuestion()
  }

  const getTenseName = (tense: TenseType) => {
    switch (tense) {
      case 'present': return 'Настоящее'
      case 'past': return 'Прошедшее'
      case 'future': return 'Будущее'
    }
  }

  const getTenseColor = (tense: TenseType) => {
    switch (tense) {
      case 'present': return 'text-green-400 bg-green-500/20'
      case 'past': return 'text-blue-400 bg-blue-500/20'
      case 'future': return 'text-purple-400 bg-purple-500/20'
    }
  }

  if (gameOver) {
    return (
      <div className="bg-gradient-to-br from-indigo-900/80 to-purple-900/80 rounded-2xl p-6 backdrop-blur-xl border border-white/20">
        <div className="text-center">
          <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-white mb-2">Игра окончена!</h2>
          <div className="space-y-2 mb-6">
            <p className="text-3xl font-bold text-yellow-400">{score} очков</p>
            <p className="text-white/80">Лучшая серия: {bestStreak} 🔥</p>
          </div>
          <div className="flex justify-center gap-4">
            <button
              onClick={restartGame}
              className="px-6 py-3 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl text-white font-bold hover:from-green-600 hover:to-emerald-600 transition-all flex items-center gap-2"
            >
              <RotateCcw className="w-5 h-5" />
              Играть снова
            </button>
          </div>
        </div>
      </div>
    )
  }

  if (!currentVerb) return null

  return (
    <div className="bg-gradient-to-br from-indigo-900/80 to-purple-900/80 rounded-2xl p-6 backdrop-blur-xl border border-white/20">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <span className="text-2xl">⏰</span>
          <h2 className="text-xl font-bold text-white">Времена глаголов</h2>
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

      {/* Streak indicator */}
      {streak > 0 && (
        <div className="mb-4 text-center">
          <span className="px-3 py-1 bg-orange-500/20 text-orange-300 rounded-full text-sm font-medium">
            🔥 Серия: {streak}
          </span>
        </div>
      )}

      {/* Question */}
      <div className="bg-white/10 rounded-xl p-4 mb-6">
        <div className="flex items-center gap-2 mb-3">
          <span className={`px-3 py-1 rounded-full text-sm font-medium ${getTenseColor(currentTense)}`}>
            {getTenseName(currentTense)} время
          </span>
          <span className="text-white/60 text-sm">({marker})</span>
        </div>
        
        <p className="text-white text-lg leading-relaxed">
          {currentVerb.context.replace('___', 
            <span key="blank" className="inline-block border-b-2 border-yellow-400 min-w-[100px]">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          )}
        </p>
        
        <p className="text-white/60 text-sm mt-2">
          Глагол: <span className="text-white font-medium">{currentVerb.verb}</span>
        </p>
      </div>

      {/* Input */}
      <div className="mb-4">
        <input
          type="text"
          value={userAnswer}
          onChange={(e) => setUserAnswer(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && userAnswer && !showResult && checkAnswer()}
          placeholder="Введите форму глагола..."
          className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded-xl text-white text-lg
                     placeholder-white/40 focus:outline-none focus:ring-2 focus:ring-purple-500"
          disabled={showResult}
          autoFocus
        />
      </div>

      {/* Check button */}
      {!showResult && (
        <button
          onClick={checkAnswer}
          disabled={!userAnswer}
          className="w-full py-3 bg-gradient-to-r from-purple-500 to-pink-500 rounded-xl text-white font-bold
                     hover:from-purple-600 hover:to-pink-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Проверить
        </button>
      )}

      {/* Result */}
      {showResult && (
        <div className={`p-4 rounded-xl ${isCorrect ? 'bg-green-500/20' : 'bg-red-500/20'}`}>
          <div className="flex items-center gap-2">
            {isCorrect ? (
              <>
                <span className="text-2xl">✅</span>
                <div>
                  <p className="text-green-300 font-bold">Правильно!</p>
                  <p className="text-white/60 text-sm">+{10 + streak * 2} очков</p>
                </div>
              </>
            ) : (
              <>
                <span className="text-2xl">❌</span>
                <div>
                  <p className="text-red-300 font-bold">Неверно</p>
                  <p className="text-white/60">Правильный ответ: <span className="text-white font-medium">{currentVerb[currentTense]}</span></p>
                </div>
              </>
            )}
          </div>
        </div>
      )}

      {/* Tips */}
      <div className="mt-6 p-4 bg-white/5 rounded-xl">
        <h3 className="text-white font-medium mb-2">💡 Подсказка</h3>
        <ul className="text-white/70 text-sm space-y-1">
          <li>• <span className="text-green-400">Настоящее</span>: сейчас, сегодня, обычно</li>
          <li>• <span className="text-blue-400">Прошедшее</span>: вчера, раньше, в прошлом году</li>
          <li>• <span className="text-purple-400">Будущее</span>: завтра, потом, в будущем</li>
        </ul>
      </div>
    </div>
  )
}
