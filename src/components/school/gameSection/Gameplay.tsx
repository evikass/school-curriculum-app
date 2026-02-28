'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useBonusMultiplier } from '../ActivityBonus'
import { useSound } from '@/lib/sounds'
import { ArrowLeft, Gamepad2, Star, Trophy, CheckCircle, Circle, Sparkles, PartyPopper } from 'lucide-react'
import { Confetti } from '../kid-games/Confetti'

export function Gameplay() {
  const { selectedGame, selectGame, addPoints, recordGameResult, unlockAchievement } = useSchool()
  const { playCorrect, playAchievement, playLevelUp } = useSound()
  const { multiplier } = useBonusMultiplier()
  const [currentIndex, setCurrentIndex] = useState(0)
  const [answers, setAnswers] = useState<Record<number, string | string[]>>({})
  const [showResults, setShowResults] = useState(false)
  const [showCelebration, setShowCelebration] = useState(false)

  if (!selectedGame || !selectedGame.tasks) return null

  const task = selectedGame.tasks[currentIndex]
  const totalTasks = selectedGame.tasks.length

  const handleAnswerSelect = (answer: string) => setAnswers({ ...answers, [currentIndex]: answer })

  const handleMultiAnswerSelect = (answer: string) => {
    const currentAnswers = (answers[currentIndex] as string[]) || []
    const newAnswers = currentAnswers.includes(answer) ? currentAnswers.filter(a => a !== answer) : [...currentAnswers, answer]
    setAnswers({ ...answers, [currentIndex]: newAnswers })
  }

  const calculateScore = () => {
    let correct = 0
    selectedGame.tasks.forEach((task, index) => {
      const userAnswer = answers[index]
      if (task.type === 'find' && Array.isArray(userAnswer) && Array.isArray(task.correctAnswer)) {
        if (JSON.stringify([...userAnswer].sort()) === JSON.stringify([...task.correctAnswer].sort())) correct++
      } else if (userAnswer === task.correctAnswer) correct++
    })
    return correct
  }

  const handleFinish = () => {
    const score = calculateScore()
    addPoints(Math.round(score * 5 * multiplier))
    recordGameResult(score, totalTasks, selectedGame.subject)
    setShowResults(true)
    // Звуки и конфетти для хороших результатов
    if (score >= totalTasks * 0.7) {
      setShowCelebration(true)
      if (score === totalTasks) {
        playAchievement()
      } else {
        playLevelUp()
      }
    } else {
      playCorrect()
    }
    if (score === totalTasks) unlockAchievement('perfect_game')
  }

  if (showResults) {
    return <ResultsScreen score={calculateScore()} totalTasks={totalTasks} game={selectedGame} multiplier={multiplier} showCelebration={showCelebration} onRestart={() => { setCurrentIndex(0); setAnswers({}); setShowResults(false); setShowCelebration(false) }} onExit={() => { selectGame(null); setShowCelebration(false) }} />
  }

  return (
    <div className="w-full max-w-2xl mx-auto animate-fadeIn">
      <button onClick={() => selectGame(null)} className="mb-6 flex items-center gap-2 text-white/80 hover:text-white text-xl font-medium bg-white/10 hover:bg-white/20 px-6 py-3 rounded-2xl transition-all">
        <ArrowLeft className="w-6 h-6" />Выйти из игры
      </button>

      {/* Progress dots */}
      <div className="flex items-center justify-center gap-2 mb-6">
        {Array.from({ length: totalTasks }).map((_, i) => (
          <div key={i} className={`w-4 h-4 rounded-full transition-all ${i < currentIndex ? 'bg-green-400 scale-110' : i === currentIndex ? 'bg-purple-400 scale-125' : 'bg-white/30'}`} />
        ))}
      </div>

      <div className="p-8 rounded-3xl bg-gradient-to-br from-gray-800/80 to-gray-900/80 border-4 border-white/10">
        <div className="flex items-center gap-3 mb-4">
          <Gamepad2 className="w-8 h-8 text-purple-400" />
          <h2 className="text-2xl font-bold text-white">{selectedGame.title}</h2>
        </div>
        <p className="text-purple-200 mb-6">Задание {currentIndex + 1} из {totalTasks}</p>
        <h3 className="text-2xl font-bold text-white mb-8">{task.question}</h3>

        {task.type === 'quiz' && task.options && <QuizOptions options={task.options} selectedAnswer={answers[currentIndex] as string} onSelect={handleAnswerSelect} />}
        {task.type === 'fill' && <FillInput value={(answers[currentIndex] as string) || ''} onChange={handleAnswerSelect} />}
        {task.type === 'find' && task.options && <FindOptions options={task.options} selectedAnswers={(answers[currentIndex] as string[]) || []} onSelect={handleMultiAnswerSelect} />}

        {task.hint && <p className="text-purple-300 mt-6 italic">💡 Подсказка: {task.hint}</p>}

        <Navigation currentIndex={currentIndex} totalTasks={totalTasks}
          onPrev={() => setCurrentIndex(Math.max(0, currentIndex - 1))}
          onNext={() => setCurrentIndex(currentIndex + 1)}
          onFinish={handleFinish} />
      </div>
    </div>
  )
}

function QuizOptions({ options, selectedAnswer, onSelect }: { options: string[]; selectedAnswer: string; onSelect: (a: string) => void }) {
  return (
    <div className="space-y-4">
      {options.map((option, idx) => (
        <button key={idx} onClick={() => onSelect(option)}
          className={`w-full p-5 rounded-2xl text-left text-lg font-medium transition-all
            ${selectedAnswer === option ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white border-4 border-white/40' : 'bg-white/10 text-white border-4 border-white/20 hover:border-purple-400'}`}>
          {option}
        </button>
      ))}
    </div>
  )
}

function FillInput({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  return (
    <input type="text" value={value} onChange={(e) => onChange(e.target.value)}
      className="w-full p-5 bg-white/10 border-4 border-white/20 rounded-2xl text-white text-xl focus:border-purple-400 focus:outline-none" placeholder="Введи ответ..." />
  )
}

function FindOptions({ options, selectedAnswers, onSelect }: { options: string[]; selectedAnswers: string[]; onSelect: (a: string) => void }) {
  return (
    <div className="space-y-4">
      <p className="text-purple-300 mb-4">Выбери все правильные варианты:</p>
      {options.map((option, idx) => {
        const isSelected = selectedAnswers.includes(option)
        return (
          <button key={idx} onClick={() => onSelect(option)}
            className={`w-full p-5 rounded-2xl text-left text-lg font-medium transition-all flex items-center gap-4
              ${isSelected ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white border-4 border-white/40' : 'bg-white/10 text-white border-4 border-white/20 hover:border-purple-400'}`}>
            {isSelected ? <CheckCircle className="w-6 h-6 text-green-300" /> : <Circle className="w-6 h-6 text-white/50" />}
            {option}
          </button>
        )
      })}
    </div>
  )
}

function Navigation({ currentIndex, totalTasks, onPrev, onNext, onFinish }: { currentIndex: number; totalTasks: number; onPrev: () => void; onNext: () => void; onFinish: () => void }) {
  return (
    <div className="flex justify-between mt-8">
      <button onClick={onPrev} disabled={currentIndex === 0}
        className="px-6 py-3 bg-white/10 text-white rounded-2xl font-bold hover:bg-white/20 disabled:opacity-30 transition-all">← Назад</button>
      {currentIndex === totalTasks - 1 ? (
        <button onClick={onFinish} className="px-8 py-3 bg-gradient-to-r from-green-500 to-emerald-500 text-white rounded-2xl font-bold hover:scale-105 transition-transform flex items-center gap-2">
          <Sparkles className="w-5 h-5" />Завершить!
        </button>
      ) : (
        <button onClick={onNext} className="px-8 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-2xl font-bold hover:scale-105 transition-transform">Далее →</button>
      )}
    </div>
  )
}

function ResultsScreen({ score, totalTasks, game, multiplier, showCelebration, onRestart, onExit }: { score: number; totalTasks: number; game: any; multiplier: number; showCelebration: boolean; onRestart: () => void; onExit: () => void }) {
  const percentage = Math.round((score / totalTasks) * 100)
  const isGood = percentage >= 70

  return (
    <div className="w-full max-w-2xl mx-auto animate-fadeIn">
      {showCelebration && <Confetti />}
      <div className={`text-center p-8 rounded-3xl border-4 border-white/20 ${isGood ? 'bg-gradient-to-br from-green-600/60 to-teal-600/60' : 'bg-gradient-to-br from-purple-600/60 to-pink-600/60'}`}>
        <div className="mb-6">
          {isGood ? (
            <div className="inline-flex p-4 rounded-full bg-yellow-400 animate-wiggle">
              <PartyPopper className="w-16 h-16 text-purple-900" />
            </div>
          ) : (
            <Trophy className="w-20 h-20 text-yellow-400 mx-auto" />
          )}
        </div>
        <h2 className="text-4xl font-black text-white mb-4">{isGood ? 'Отлично! 🎉' : 'Результаты!'}</h2>
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
            <div className="text-white/70">Баллов {multiplier > 1 ? `🔥x${multiplier}` : ''}</div>
          </div>
        </div>
        <div className="flex justify-center gap-2 mb-6">
          {Array.from({ length: game.reward.stars }).map((_, i) => <Star key={i} className="w-10 h-10 text-yellow-400 fill-yellow-400 animate-sparkle" style={{ animationDelay: `${i * 0.2}s` }} />)}
        </div>
        <p className="text-xl text-white/90 mb-8">{game.reward.message}</p>
        <div className="flex justify-center gap-4">
          <button onClick={onRestart} className="px-6 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-2xl font-bold hover:scale-105 transition-transform">Играть снова</button>
          <button onClick={onExit} className="px-6 py-3 bg-white/20 text-white rounded-2xl font-bold hover:bg-white/30 transition-colors">К играм</button>
        </div>
      </div>
    </div>
  )
}
