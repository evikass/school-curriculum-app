'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useBonusMultiplier } from './ActivityBonus'
import { GameLesson } from '@/data/types'
import { ArrowLeft, Gamepad2, Star, Play, Trophy, CheckCircle, Circle, Sparkles, PartyPopper } from 'lucide-react'
import { useSound } from '@/lib/sounds'

// Confetti component for celebration
function Confetti() {
  const [particles, setParticles] = useState<Array<{ id: number; x: number; color: string; delay: number; rotation: number }>>([])

  useEffect(() => {
    const colors = ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']
    const newParticles = Array.from({ length: 50 }, (_, i) => ({
      id: i,
      x: Math.random() * 100,
      color: colors[Math.floor(Math.random() * colors.length)],
      delay: Math.random() * 0.5,
      rotation: Math.random() * 360
    }))
    setParticles(newParticles)
  }, [])

  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden z-50">
      {particles.map((p) => (
        <div
          key={p.id}
          className="absolute animate-confetti"
          style={{
            left: `${p.x}%`,
            top: '-20px',
            width: '10px',
            height: '10px',
            backgroundColor: p.color,
            borderRadius: Math.random() > 0.5 ? '50%' : '0',
            animationDelay: `${p.delay}s`,
            transform: `rotate(${p.rotation}deg)`
          }}
        />
      ))}
    </div>
  )
}

export default function KidGameSection() {
  const { games, selectedClass, selectGame, goBack } = useSchool()

  const gradeEmoji = selectedClass === 0 ? '🎒' : selectedClass === 1 ? '🌟' : '🦋'

  return (
    <div className="w-full animate-bounceIn">
      {/* Back button - BIG for kids */}
      <button
        onClick={goBack}
        className="mb-8 flex items-center gap-3 text-white text-2xl font-bold 
                   bg-white/20 hover:bg-white/30 px-8 py-4 rounded-3xl transition-all
                   border-4 border-white/30 hover:border-white/50"
      >
        <ArrowLeft className="w-8 h-8" /> 
        Назад
      </button>

      {/* Title - HUGE and colorful */}
      <div className="text-center mb-10">
        <div className="text-8xl mb-4 animate-float">{gradeEmoji}</div>
        <h2 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text 
                       bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-4">
          ИГРЫ!
        </h2>
        <p className="text-2xl text-purple-200">
          Выбери игру и играй! 🎮
        </p>
      </div>

      {/* Games grid - BIG CARDS */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {games.map((game: GameLesson, index: number) => (
          <button
            key={index}
            onClick={() => selectGame(game)}
            className="group relative overflow-hidden p-8 rounded-3xl
                       bg-gradient-to-br from-purple-500/60 to-pink-500/60
                       border-4 border-white/30 hover:border-yellow-400
                       shadow-2xl hover:shadow-yellow-400/20
                       transition-all duration-300 hover:scale-[1.03] text-left"
          >
            {/* Star badge */}
            <div className="absolute top-4 right-4 bg-yellow-400 text-purple-900 
                           px-4 py-2 rounded-2xl font-black text-lg flex items-center gap-2">
              <Star className="w-6 h-6 fill-purple-900" />
              {game.reward.stars}
            </div>

            {/* Icon */}
            <div className="p-5 rounded-3xl bg-gradient-to-br from-yellow-400 to-orange-500 
                           inline-block mb-5 group-hover:scale-110 transition-transform">
              <Gamepad2 className="w-14 h-14 text-white" />
            </div>

            {/* Content */}
            <h3 className="text-3xl font-black text-white mb-3">{game.title}</h3>
            <p className="text-xl text-purple-200 mb-4">{game.subject}</p>

            <div className="text-white/80 text-lg">
              {game.tasks.length} заданий
            </div>

            {/* Play button */}
            <div className="mt-6 flex items-center gap-3 text-yellow-300 text-xl font-bold">
              <Play className="w-8 h-8" />
              ИГРАТЬ!
            </div>
          </button>
        ))}
      </div>
    </div>
  )
}

// Kid-friendly gameplay component
export function KidGameplay() {
  const { selectedGame, selectGame, addPoints, recordGameResult, unlockAchievement } = useSchool()
  const { playCorrect, playAchievement, playLevelUp } = useSound()
  const { multiplier } = useBonusMultiplier()
  const [currentIndex, setCurrentIndex] = useState(0)
  const [answers, setAnswers] = useState<Record<number, string | string[]>>({})
  const [showResults, setShowResults] = useState(false)
  const [showCelebration, setShowCelebration] = useState(false)

  if (!selectedGame) return null

  const task = selectedGame.tasks[currentIndex]
  const totalTasks = selectedGame.tasks.length

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
    selectedGame.tasks.forEach((task, index) => {
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

  const handleFinish = () => {
    const score = calculateScore()
    addPoints(Math.round(score * 10 * multiplier))
    recordGameResult(score, totalTasks, selectedGame.subject)
    setShowResults(true)
    
    if (score >= totalTasks * 0.7) {
      setShowCelebration(true)
      if (score === totalTasks) {
        // Perfect score!
        playAchievement()
      } else {
        playLevelUp()
      }
    } else {
      playCorrect()
    }
    
    // Track perfect game for achievements
    if (score === totalTasks) {
      unlockAchievement('perfect_game')
    }
  }

  // Results screen
  if (showResults) {
    const score = calculateScore()
    const percentage = Math.round((score / totalTasks) * 100)
    const isGood = percentage >= 70

    return (
      <div className="w-full max-w-2xl mx-auto animate-bounceIn">
        {showCelebration && <Confetti />}
        
        <div className="text-center p-10 rounded-3xl bg-gradient-to-br 
                        ${isGood ? 'from-green-500/60 to-teal-500/60' : 'from-purple-600/60 to-pink-600/60'}
                        border-4 border-white/30 shadow-2xl">
          
          {/* Big icon */}
          <div className="mb-6">
            {isGood ? (
              <div className="inline-flex p-6 rounded-full bg-yellow-400 animate-wiggle">
                <PartyPopper className="w-20 h-20 text-purple-900" />
              </div>
            ) : (
              <Trophy className="w-24 h-24 text-yellow-400 mx-auto" />
            )}
          </div>

          <h2 className="text-5xl font-black text-white mb-6">
            {isGood ? 'УРА! 🎉' : 'Результаты'}
          </h2>
          
          <div className="flex justify-center gap-10 mb-8">
            <div className="text-center">
              <div className="text-7xl font-black text-white">{score}</div>
              <div className="text-xl text-white/80">Правильно</div>
            </div>
            <div className="text-center">
              <div className="text-7xl font-black text-yellow-300">{percentage}%</div>
              <div className="text-xl text-white/80">Результат</div>
            </div>
            <div className="text-center">
              <div className="text-7xl font-black text-green-300">{Math.round(score * 10 * multiplier)}</div>
              <div className="text-xl text-white/80">Баллов {multiplier > 1 ? `🔥x${multiplier}` : ''}</div>
            </div>
          </div>

          {/* Stars */}
          <div className="flex justify-center gap-3 mb-8">
            {Array.from({ length: selectedGame.reward.stars }).map((_, i) => (
              <Star key={i} className="w-14 h-14 text-yellow-400 fill-yellow-400 animate-sparkle" 
                    style={{ animationDelay: `${i * 0.2}s` }} />
            ))}
          </div>

          <p className="text-2xl text-white mb-10">{selectedGame.reward.message}</p>

          <div className="flex flex-col sm:flex-row justify-center gap-4">
            <button
              onClick={() => { 
                setCurrentIndex(0); 
                setAnswers({}); 
                setShowResults(false);
                setShowCelebration(false);
              }}
              className="px-10 py-5 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-3xl 
                         text-2xl font-bold hover:scale-105 transition-transform"
            >
              Ещё раз! 🔄
            </button>
            <button
              onClick={() => { 
                selectGame(null); 
                setShowResults(false);
                setShowCelebration(false);
              }}
              className="px-10 py-5 bg-white/20 text-white rounded-3xl text-2xl font-bold 
                         hover:bg-white/30 transition-colors"
            >
              К играм 🎮
            </button>
          </div>
        </div>
      </div>
    )
  }

  // Game screen
  return (
    <div className="w-full max-w-3xl mx-auto animate-fadeIn">
      {/* Back */}
      <button
        onClick={() => selectGame(null)}
        className="mb-8 flex items-center gap-3 text-white text-2xl font-bold 
                   bg-white/20 hover:bg-white/30 px-8 py-4 rounded-3xl transition-all
                   border-4 border-white/30"
      >
        <ArrowLeft className="w-8 h-8" /> 
        Выйти
      </button>

      {/* Progress - BIG DOTS */}
      <div className="flex items-center justify-center gap-4 mb-8">
        {Array.from({ length: totalTasks }).map((_, i) => (
          <div
            key={i}
            className={`w-6 h-6 rounded-full transition-all ${
              i < currentIndex ? 'bg-green-400 scale-110' :
              i === currentIndex ? 'bg-yellow-400 scale-150 ring-4 ring-yellow-400/30' : 'bg-white/30'
            }`}
          />
        ))}
      </div>

      {/* Game card */}
      <div className="p-8 md:p-10 rounded-3xl bg-gradient-to-br from-indigo-600/60 to-purple-600/60 
                      border-4 border-white/20 shadow-2xl">
        
        {/* Title */}
        <div className="flex items-center gap-4 mb-6">
          <Gamepad2 className="w-10 h-10 text-purple-300" />
          <h2 className="text-3xl font-black text-white">{selectedGame.title}</h2>
        </div>
        <p className="text-xl text-purple-200 mb-8">
          Задание {currentIndex + 1} из {totalTasks}
        </p>

        {/* Question - BIG TEXT */}
        <h3 className="text-2xl md:text-3xl font-bold text-white mb-10 leading-relaxed">
          {task.question}
        </h3>

        {/* Quiz type - BIG BUTTONS */}
        {task.type === 'quiz' && task.options && (
          <div className="space-y-5">
            {task.options.map((option, index) => (
              <button
                key={index}
                onClick={() => handleAnswerSelect(option)}
                className={`w-full p-6 md:p-8 rounded-3xl text-left text-xl md:text-2xl font-bold transition-all
                  ${answers[currentIndex] === option
                    ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white border-4 border-yellow-400 scale-[1.02]'
                    : 'bg-white/10 text-white border-4 border-white/30 hover:border-purple-400 hover:bg-white/20'
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
            className="w-full p-6 md:p-8 bg-white/10 border-4 border-white/30 rounded-3xl text-white text-2xl
                       focus:border-yellow-400 focus:outline-none placeholder-white/50"
            placeholder="Напиши ответ..."
          />
        )}

        {/* Find type */}
        {task.type === 'find' && task.options && (
          <div className="space-y-5">
            <p className="text-xl text-purple-200 mb-4">Выбери все правильные:</p>
            {task.options.map((option, index) => {
              const selectedAnswers = (answers[currentIndex] as string[]) || []
              const isSelected = selectedAnswers.includes(option)
              return (
                <button
                  key={index}
                  onClick={() => handleMultiAnswerSelect(option)}
                  className={`w-full p-6 md:p-8 rounded-3xl text-left text-xl md:text-2xl font-bold transition-all flex items-center gap-4
                    ${isSelected
                      ? 'bg-gradient-to-r from-green-500 to-teal-500 text-white border-4 border-yellow-400'
                      : 'bg-white/10 text-white border-4 border-white/30 hover:border-purple-400'
                    }`}
                >
                  {isSelected ? (
                    <CheckCircle className="w-8 h-8 text-white flex-shrink-0" />
                  ) : (
                    <Circle className="w-8 h-8 text-white/50 flex-shrink-0" />
                  )}
                  <span>{option}</span>
                </button>
              )
            })}
          </div>
        )}

        {/* Hint */}
        {task.hint && (
          <div className="mt-8 p-5 rounded-2xl bg-yellow-400/20 border-2 border-yellow-400/40">
            <p className="text-xl text-yellow-200">
              💡 Подсказка: {task.hint}
            </p>
          </div>
        )}

        {/* Navigation - BIG BUTTONS */}
        <div className="flex justify-between mt-10 gap-4">
          <button
            onClick={() => setCurrentIndex(Math.max(0, currentIndex - 1))}
            disabled={currentIndex === 0}
            className="px-8 py-5 bg-white/10 text-white rounded-3xl text-xl font-bold 
                       hover:bg-white/20 disabled:opacity-30 transition-all border-4 border-white/20"
          >
            ← Назад
          </button>
          
          {currentIndex === totalTasks - 1 ? (
            <button
              onClick={handleFinish}
              className="px-10 py-5 bg-gradient-to-r from-green-500 to-emerald-500 text-white rounded-3xl 
                         text-2xl font-bold hover:scale-105 transition-transform flex items-center gap-3"
            >
              <Sparkles className="w-8 h-8" />
              ГОТОВО!
            </button>
          ) : (
            <button
              onClick={() => setCurrentIndex(currentIndex + 1)}
              className="px-10 py-5 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-3xl 
                         text-2xl font-bold hover:scale-105 transition-transform"
            >
              Далее →
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
