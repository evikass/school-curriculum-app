'use client'

import { useSchool } from '@/context/SchoolContext'
<<<<<<< HEAD
import { GameLesson } from '@/data/types'
import { ArrowLeft, Gamepad2, Star, Play } from 'lucide-react'

export default function GameSection() {
  const { games, selectedClass, selectGame, goBack } = useSchool()
  
  const safeGames = Array.isArray(games) ? games : []
  const gradeName = selectedClass === 0 ? 'Подготовишки' : selectedClass ? `${selectedClass} класс` : 'Класс'

  return (
    <div className="w-full">
      <button onClick={goBack}
        className="mb-6 flex items-center gap-2 text-white/80 hover:text-white text-xl font-medium bg-white/10 hover:bg-white/20 px-6 py-3 rounded-2xl transition-all">
        <ArrowLeft className="w-6 h-6" /> Назад к предметам
      </button>

      <div className="text-center mb-8">
        <div className="inline-flex items-center gap-4 mb-4">
          <Gamepad2 className="w-16 h-16 text-purple-400" />
        </div>
        <h2 className="text-3xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-3">
          Игры и викторины!
        </h2>
        <p className="text-xl text-purple-200">{gradeName} • {safeGames.length} игр</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {safeGames.map((game: GameLesson, index: number) => (
          <button key={index} onClick={() => selectGame(game)}
            className="group relative overflow-hidden p-6 rounded-3xl bg-gradient-to-br from-purple-600/60 to-pink-600/60 border-4 border-white/20 hover:border-yellow-400/50 shadow-xl hover:shadow-2xl hover:scale-[1.02] transition-all duration-300 text-left">
            <div className="p-4 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 inline-block mb-4 group-hover:scale-110 transition-transform">
              <Gamepad2 className="w-10 h-10 text-white" />
            </div>
            <h3 className="text-2xl font-bold text-white mb-2">{game.title}</h3>
            <p className="text-purple-200 mb-4">{game.subject}</p>
            <div className="flex items-center gap-4 mb-4">
              <span className="text-white/80 bg-white/10 px-3 py-1 rounded-xl">{game.tasks?.length || 0} заданий</span>
              <span className="flex items-center gap-1 text-yellow-400">
                <Star className="w-5 h-5 fill-yellow-400" />{game.reward?.stars || 0}
              </span>
            </div>
            <div className="flex items-center gap-2 text-white font-bold">
              <Play className="w-6 h-6 group-hover:scale-110 transition-transform" />Начать игру!
            </div>
          </button>
        ))}
=======
import { useBonusMultiplier } from './ActivityBonus'
import { GameLesson } from '@/data/types'
import { ArrowLeft, Gamepad2, Star, Play, Trophy, CheckCircle, Circle } from 'lucide-react'
import { useState } from 'react'

function SafeGameCard({ game, onSelect }: { game: GameLesson; onSelect: (g: GameLesson) => void }) {
  try {
    return (
      <button
        onClick={() => onSelect(game)}
        className="group relative overflow-hidden p-6 rounded-3xl
                   bg-gradient-to-br from-purple-600/60 to-pink-600/60
                   border-4 border-white/20 hover:border-yellow-400/50
                   shadow-xl hover:shadow-2xl hover:scale-[1.02]
                   transition-all duration-300 text-left"
      >
        {/* Icon */}
        <div className="p-4 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 inline-block mb-4
                        group-hover:scale-110 transition-transform">
          <Gamepad2 className="w-10 h-10 text-white" />
        </div>

        {/* Content */}
        <h3 className="text-2xl font-bold text-white mb-2">{game.title || 'Без названия'}</h3>
        <p className="text-purple-200 mb-4">{game.subject || 'Предмет'}</p>

        {/* Stats */}
        <div className="flex items-center gap-4 mb-4">
          <span className="text-white/80 bg-white/10 px-3 py-1 rounded-xl">
            {game.tasks?.length || 0} заданий
          </span>
          <span className="flex items-center gap-1 text-yellow-400">
            <Star className="w-5 h-5 fill-yellow-400" />
            {game.reward?.stars || 0}
          </span>
        </div>

        {/* Play button */}
        <div className="flex items-center gap-2 text-white font-bold">
          <Play className="w-6 h-6 group-hover:scale-110 transition-transform" />
          Начать игру!
        </div>
      </button>
    )
  } catch (e) {
    console.error('SafeGameCard error:', e)
    return null
  }
}

export default function GameSection() {
  try {
    const { games, selectedClass, selectGame, goBack } = useSchool()
    
    // Safety check - ensure games is always an array
    const safeGames = Array.isArray(games) ? games : (games ? [games] : [])
    const gamesCount = safeGames.length

    return (
      <div className="w-full animate-fadeIn">
        {/* Back button */}
        <button
          onClick={goBack}
          className="mb-6 flex items-center gap-2 text-white/80 hover:text-white text-xl font-medium 
                     bg-white/10 hover:bg-white/20 px-6 py-3 rounded-2xl transition-all"
        >
          <ArrowLeft className="w-6 h-6" /> 
          Назад к предметам
        </button>

        {/* Title */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-4 mb-4">
            <Gamepad2 className="w-16 h-16 text-purple-400" />
          </div>
          <h2 className="text-3xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-3">
            Игры и викторины!
          </h2>
          <p className="text-xl text-purple-200">
            {selectedClass === 0 ? 'Подготовишки' : `${selectedClass} класс`} • {gamesCount} игр
          </p>
        </div>

        {/* Games grid */}
        {gamesCount === 0 ? (
          <div className="text-center p-8 bg-white/10 rounded-2xl">
            <p className="text-purple-200 text-xl">Игр для этого класса пока нет 😔</p>
            <p className="text-purple-300 mt-2">Попробуйте другой класс!</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {safeGames.map((game: GameLesson, index: number) => (
              <SafeGameCard key={index} game={game} onSelect={selectGame} />
            ))}
          </div>
        )}
      </div>
    )
  } catch (error) {
    console.error('GameSection render error:', error)
    return (
      <div className="p-6 bg-red-500/20 border-2 border-red-500 rounded-2xl text-white">
        <h2 className="text-2xl font-bold mb-2">Ошибка загрузки игр</h2>
        <p>{error instanceof Error ? error.message : 'Неизвестная ошибка'}</p>
      </div>
    )
  }
}

// Gameplay component for playing a game
export function Gameplay() {
  const { selectedGame, selectGame, addPoints, goBack, recordGameResult, unlockAchievement } = useSchool()
  const { multiplier } = useBonusMultiplier()
  const [currentIndex, setCurrentIndex] = useState(0)
  const [answers, setAnswers] = useState<Record<number, string | string[]>>({})
  const [showResults, setShowResults] = useState(false)

  if (!selectedGame) return null
  
  // Safety checks
  const tasks = selectedGame.tasks || []
  const totalTasks = tasks.length
  
  if (totalTasks === 0) {
    return (
      <div className="w-full max-w-2xl mx-auto animate-fadeIn">
        <div className="text-center p-8 bg-white/10 rounded-2xl">
          <p className="text-purple-200 text-xl">В этой игре нет заданий 😔</p>
          <button
            onClick={() => selectGame(null)}
            className="mt-4 px-6 py-3 bg-purple-500 text-white rounded-2xl"
          >
            Назад
          </button>
        </div>
      </div>
    )
  }

  const task = tasks[currentIndex]
  
  // Safety check for task
  if (!task) {
    return (
      <div className="w-full max-w-2xl mx-auto animate-fadeIn">
        <div className="text-center p-8 bg-white/10 rounded-2xl">
          <p className="text-purple-200 text-xl">Задание не найдено 😔</p>
          <button
            onClick={() => selectGame(null)}
            className="mt-4 px-6 py-3 bg-purple-500 text-white rounded-2xl"
          >
            Назад
          </button>
        </div>
      </div>
    )
  }

  const handleAnswerSelect = (answer: string) => {
    setAnswers({ ...answers, [currentIndex]: answer })
  }

  const handleMultiAnswerSelect = (answer: string) => {
    const currentAnswers = (answers[currentIndex] as string[]) || []
    const newAnswers = currentAnswers.includes(answer)
      ? currentAnswers.filter(a => a !== answer)
      : [...currentAnswers, answer]
    setAnswers({ ...answers, [currentIndex]: newAnswers })
  }

  const calculateScore = () => {
    let correct = 0
    tasks.forEach((task, index) => {
      const userAnswer = answers[index]
      if (task.type === 'find' && Array.isArray(userAnswer) && Array.isArray(task.correctAnswer)) {
        if (JSON.stringify([...userAnswer].sort()) === JSON.stringify([...task.correctAnswer].sort())) {
          correct++
        }
      } else if (userAnswer === task.correctAnswer) {
        correct++
      }
    })
    return correct
  }

  // Results screen
  if (showResults) {
    const score = calculateScore()
    const percentage = Math.round((score / totalTasks) * 100)

    return (
      <div className="w-full max-w-2xl mx-auto animate-fadeIn">
        <div className="text-center p-8 rounded-3xl bg-gradient-to-br from-purple-600/60 to-pink-600/60 
                        border-4 border-white/20">
          <Trophy className="w-20 h-20 text-yellow-400 mx-auto mb-6" />
          <h2 className="text-4xl font-black text-white mb-4">Результаты!</h2>
          
          <div className="flex justify-center gap-8 mb-8">
            <div className="text-center">
              <div className="text-5xl font-black text-green-400">{score}</div>
              <div className="text-white/70">Правильно</div>
            </div>
            <div className="text-center">
              <div className="text-5xl font-black text-purple-300">{percentage}%</div>
              <div className="text-white/70">Результат</div>
            </div>
            <div className="text-center">
              <div className="text-5xl font-black text-yellow-400">{Math.round(score * 5 * multiplier)}</div>
              <div className="text-white/70">Баллов {multiplier > 1 ? `(x${multiplier})` : ''}</div>
            </div>
          </div>

          {/* Stars */}
          <div className="flex justify-center gap-2 mb-6">
            {Array.from({ length: selectedGame.reward?.stars || 3 }).map((_, i) => (
              <Star key={i} className="w-10 h-10 text-yellow-400 fill-yellow-400" />
            ))}
          </div>

          <p className="text-xl text-white/90 mb-8">{selectedGame.reward?.message || 'Отличная работа!'}</p>

          <div className="flex justify-center gap-4">
            <button
              onClick={() => { setCurrentIndex(0); setAnswers({}); setShowResults(false) }}
              className="px-6 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-2xl 
                         font-bold hover:scale-105 transition-transform"
            >
              Играть снова
            </button>
            <button
              onClick={() => { selectGame(null); setShowResults(false); }}
              className="px-6 py-3 bg-white/20 text-white rounded-2xl font-bold hover:bg-white/30 transition-colors"
            >
              К играм
            </button>
          </div>
        </div>
      </div>
    )
  }

  // Game screen
  return (
    <div className="w-full max-w-2xl mx-auto animate-fadeIn">
      {/* Back */}
      <button
        onClick={() => selectGame(null)}
        className="mb-6 flex items-center gap-2 text-white/80 hover:text-white text-xl font-medium 
                   bg-white/10 hover:bg-white/20 px-6 py-3 rounded-2xl transition-all"
      >
        <ArrowLeft className="w-6 h-6" /> 
        Выйти из игры
      </button>

      {/* Progress dots */}
      <div className="flex items-center justify-center gap-2 mb-6">
        {Array.from({ length: totalTasks }).map((_, i) => (
          <div
            key={i}
            className={`w-4 h-4 rounded-full transition-all ${
              i < currentIndex ? 'bg-green-400 scale-110' :
              i === currentIndex ? 'bg-purple-400 scale-125' : 'bg-white/30'
            }`}
          />
        ))}
      </div>

      {/* Game card */}
      <div className="p-8 rounded-3xl bg-gradient-to-br from-gray-800/80 to-gray-900/80 border-4 border-white/10">
        <div className="flex items-center gap-3 mb-4">
          <Gamepad2 className="w-8 h-8 text-purple-400" />
          <h2 className="text-2xl font-bold text-white">{selectedGame.title}</h2>
        </div>
        <p className="text-purple-200 mb-6">Задание {currentIndex + 1} из {totalTasks}</p>

        {/* Question */}
        <h3 className="text-2xl font-bold text-white mb-8">{task.question}</h3>

        {/* Quiz type */}
        {task.type === 'quiz' && task.options && (
          <div className="space-y-4">
            {task.options.map((option, index) => (
              <button
                key={index}
                onClick={() => handleAnswerSelect(option)}
                className={`w-full p-5 rounded-2xl text-left text-lg font-medium transition-all
                  ${answers[currentIndex] === option
                    ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white border-4 border-white/40'
                    : 'bg-white/10 text-white border-4 border-white/20 hover:border-purple-400'
                  }`}
              >
                {option}
              </button>
            ))}
          </div>
        )}

        {/* Fill type */}
        {task.type === 'fill' && (
          <input
            type="text"
            value={(answers[currentIndex] as string) || ''}
            onChange={(e) => handleAnswerSelect(e.target.value)}
            className="w-full p-5 bg-white/10 border-4 border-white/20 rounded-2xl text-white text-xl
                       focus:border-purple-400 focus:outline-none"
            placeholder="Введи ответ..."
          />
        )}

        {/* Find type */}
        {task.type === 'find' && task.options && (
          <div className="space-y-4">
            <p className="text-purple-300 mb-4">Выбери все правильные варианты:</p>
            {task.options.map((option, index) => {
              const selectedAnswers = (answers[currentIndex] as string[]) || []
              const isSelected = selectedAnswers.includes(option)
              return (
                <button
                  key={index}
                  onClick={() => handleMultiAnswerSelect(option)}
                  className={`w-full p-5 rounded-2xl text-left text-lg font-medium transition-all flex items-center gap-4
                    ${isSelected
                      ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white border-4 border-white/40'
                      : 'bg-white/10 text-white border-4 border-white/20 hover:border-purple-400'
                    }`}
                >
                  {isSelected ? (
                    <CheckCircle className="w-6 h-6 text-green-300" />
                  ) : (
                    <Circle className="w-6 h-6 text-white/50" />
                  )}
                  {option}
                </button>
              )
            })}
          </div>
        )}

        {/* Hint */}
        {task.hint && (
          <p className="text-purple-300 mt-6 italic">
            💡 Подсказка: {task.hint}
          </p>
        )}

        {/* Navigation */}
        <div className="flex justify-between mt-8">
          <button
            onClick={() => setCurrentIndex(Math.max(0, currentIndex - 1))}
            disabled={currentIndex === 0}
            className="px-6 py-3 bg-white/10 text-white rounded-2xl font-bold 
                       hover:bg-white/20 disabled:opacity-30 transition-all"
          >
            ← Назад
          </button>
          
          {currentIndex === totalTasks - 1 ? (
            <button
              onClick={() => {
                const score = calculateScore()
                setShowResults(true)
                addPoints(Math.round(score * 5 * multiplier))
                recordGameResult(score, totalTasks, selectedGame.subject)
                if (score === totalTasks) {
                  unlockAchievement('perfect_game')
                }
              }}
              className="px-8 py-3 bg-gradient-to-r from-green-500 to-emerald-500 text-white rounded-2xl 
                         font-bold hover:scale-105 transition-transform"
            >
              Завершить! 🎉
            </button>
          ) : (
            <button
              onClick={() => setCurrentIndex(currentIndex + 1)}
              className="px-8 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-2xl 
                         font-bold hover:scale-105 transition-transform"
            >
              Далее →
            </button>
          )}
        </div>
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
      </div>
    </div>
  )
}
