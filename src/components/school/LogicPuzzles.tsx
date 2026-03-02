'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Brain, Lightbulb, Trophy, RotateCcw, Zap, HelpCircle } from 'lucide-react'

interface Puzzle {
  question: string
  answer: string
  hint: string
  type: 'sequence' | 'riddle' | 'math' | 'pattern'
}

const PUZZLES: Puzzle[] = [
  {
    question: 'Что идёт, но никогда не приходит?',
    answer: 'завтра',
    hint: 'Это слово часто говорят, когда откладывают дела...',
    type: 'riddle'
  },
  {
    question: 'Продолжи последовательность: 2, 4, 8, 16, ?',
    answer: '32',
    hint: 'Каждое следующее число в 2 раза больше предыдущего',
    type: 'sequence'
  },
  {
    question: 'В комнате 4 угла. В каждом углу сидит кошка. Напротив каждой кошки — 3 кошки. Сколько всего кошек?',
    answer: '4',
    hint: 'Каждая кошка видит трёх других...',
    type: 'math'
  },
  {
    question: 'Какой знак нужно поставить между 5 и 6, чтобы получилось число больше 5, но меньше 6?',
    answer: 'запятую',
    hint: 'В математике это разделитель...',
    type: 'riddle'
  },
  {
    question: 'Продолжи последовательность: 1, 1, 2, 3, 5, 8, ?',
    answer: '13',
    hint: 'Это знаменитая последовательность Фибоначчи',
    type: 'sequence'
  },
  {
    question: 'У семи братьев по сестре. Сколько всего детей в семье?',
    answer: '8',
    hint: 'Сестра одна на всех братьев',
    type: 'math'
  },
  {
    question: 'Что можно увидеть с закрытыми глазами?',
    answer: 'сон',
    hint: 'Это случается каждую ночь...',
    type: 'riddle'
  },
  {
    question: 'Найди лишнее: квадрат, круг, треугольник, прямоугольник, шар',
    answer: 'шар',
    hint: 'Подумай о размерности...',
    type: 'pattern'
  },
  {
    question: 'Продолжи: А, В, Г, Д, ?, ?',
    answer: 'Е, Ё',
    hint: 'Это русский алфавит без буквы Б',
    type: 'sequence'
  },
  {
    question: 'Три курицы несут три яйца за три дня. Сколько яиц снесут 12 куриц за 12 дней?',
    answer: '48',
    hint: 'Одна курица несёт одно яйцо за три дня',
    type: 'math'
  },
  {
    question: 'Что становится легче, когда его наполняют?',
    answer: 'воздушный шар',
    hint: 'Это летает в небе...',
    type: 'riddle'
  },
  {
    question: 'Какое число следующее: 1, 4, 9, 16, 25, ?',
    answer: '36',
    hint: 'Это квадраты натуральных чисел',
    type: 'sequence'
  },
]

const TYPE_CONFIG = {
  sequence: { label: 'Последовательность', color: 'from-blue-500/20 to-cyan-500/20', border: 'border-blue-500/30' },
  riddle: { label: 'Загадка', color: 'from-purple-500/20 to-pink-500/20', border: 'border-purple-500/30' },
  math: { label: 'Задача', color: 'from-green-500/20 to-emerald-500/20', border: 'border-green-500/30' },
  pattern: { label: 'Закономерность', color: 'from-orange-500/20 to-yellow-500/20', border: 'border-orange-500/30' },
}

export default function LogicPuzzles() {
  const { addPoints } = useSchool()
  const [currentIndex, setCurrentIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [userAnswer, setUserAnswer] = useState('')
  const [showHint, setShowHint] = useState(false)
  const [showResult, setShowResult] = useState(false)
  const [isCorrect, setIsCorrect] = useState(false)
  const [gameOver, setGameOver] = useState(false)
  const [hintsUsed, setHintsUsed] = useState(0)
  const [puzzles] = useState(() => [...PUZZLES].sort(() => Math.random() - 0.5))

  const currentPuzzle = puzzles[currentIndex]

  const checkAnswer = () => {
    const correct = userAnswer.toLowerCase().trim() === currentPuzzle.answer.toLowerCase().trim()
    setIsCorrect(correct)
    setShowResult(true)
    
    if (correct) {
      const bonus = showHint ? 10 : 20 // Меньше XP если использовал подсказку
      addPoints(bonus)
      setScore(s => s + 1)
    }
  }

  const useHint = () => {
    setShowHint(true)
    setHintsUsed(h => h + 1)
  }

  const nextPuzzle = () => {
    if (currentIndex < puzzles.length - 1) {
      setCurrentIndex(i => i + 1)
      setUserAnswer('')
      setShowHint(false)
      setShowResult(false)
      setIsCorrect(false)
    } else {
      setGameOver(true)
    }
  }

  const resetGame = () => {
    setCurrentIndex(0)
    setScore(0)
    setUserAnswer('')
    setShowHint(false)
    setShowResult(false)
    setIsCorrect(false)
    setGameOver(false)
    setHintsUsed(0)
  }

  if (gameOver) {
    const percentage = Math.round((score / puzzles.length) * 100)
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-violet-500/20 to-purple-500/20 border-2 border-violet-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-white mb-2">Отличная работа!</h3>
        <p className="text-4xl font-bold text-violet-300 mb-2">{score} / {puzzles.length}</p>
        <p className="text-lg text-violet-200 mb-2">
          {percentage >= 80 ? 'Ты настоящий мыслитель! 🧠' : percentage >= 60 ? 'Хорошая логика! 💪' : 'Продолжай тренировать ум! 🎯'}
        </p>
        <p className="text-violet-300 mb-1">Подсказок использовано: {hintsUsed}</p>
        <p className="text-violet-300 mb-4">Заработано XP: {score * 20 - hintsUsed * 10}</p>
        <button
          onClick={resetGame}
          className="px-6 py-3 bg-violet-500 hover:bg-violet-600 rounded-xl text-white font-bold transition-colors flex items-center gap-2 mx-auto"
        >
          <RotateCcw className="w-4 h-4" /> Новые загадки
        </button>
      </div>
    )
  }

  const typeConfig = TYPE_CONFIG[currentPuzzle.type]

  return (
    <div className={`p-6 rounded-2xl bg-gradient-to-br ${typeConfig.color} border-2 ${typeConfig.border}`}>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-bold text-white flex items-center gap-2">
          <Brain className="w-5 h-5 text-violet-400" />
          Логические задачи
        </h3>
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 rounded-full text-sm bg-violet-500/20 text-violet-300">
            {typeConfig.label}
          </span>
          <span className="text-violet-300 text-sm">
            {currentIndex + 1}/{puzzles.length}
          </span>
        </div>
      </div>

      <div className="bg-white/5 rounded-xl p-4 mb-4">
        <p className="text-lg text-white">{currentPuzzle.question}</p>
      </div>

      {!showResult ? (
        <>
          <div className="flex gap-2 mb-4">
            <input
              type="text"
              value={userAnswer}
              onChange={(e) => setUserAnswer(e.target.value)}
              placeholder="Введи ответ..."
              className="flex-1 p-3 bg-white/10 border border-white/20 rounded-xl text-white placeholder-white/50 focus:outline-none focus:border-violet-400"
              onKeyPress={(e) => e.key === 'Enter' && checkAnswer()}
            />
            <button
              onClick={checkAnswer}
              disabled={!userAnswer.trim()}
              className="px-6 py-3 bg-violet-500 hover:bg-violet-600 disabled:bg-violet-500/50 disabled:cursor-not-allowed rounded-xl text-white font-bold transition-colors"
            >
              Ответить
            </button>
          </div>

          {!showHint && (
            <button
              onClick={useHint}
              className="w-full p-3 bg-white/5 hover:bg-white/10 rounded-xl text-violet-300 font-medium transition-colors flex items-center justify-center gap-2 border border-white/10"
            >
              <HelpCircle className="w-4 h-4" /> Использовать подсказку (-10 XP)
            </button>
          )}

          {showHint && (
            <div className="p-3 bg-yellow-500/20 rounded-xl border border-yellow-500/30 flex items-start gap-2">
              <Lightbulb className="w-5 h-5 text-yellow-400 flex-shrink-0 mt-0.5" />
              <p className="text-yellow-200 text-sm">{currentPuzzle.hint}</p>
            </div>
          )}
        </>
      ) : (
        <div className={`p-4 rounded-xl ${isCorrect ? 'bg-green-500/20 border border-green-500/30' : 'bg-red-500/20 border border-red-500/30'}`}>
          <p className={`text-lg font-bold ${isCorrect ? 'text-green-300' : 'text-red-300'}`}>
            {isCorrect ? '✅ Правильно!' : '❌ Неправильно'}
          </p>
          {!isCorrect && (
            <p className="text-white mt-1">Правильный ответ: <span className="font-bold text-green-300">{currentPuzzle.answer}</span></p>
          )}
          <p className="text-violet-200 mt-2">
            Заработано XP: {isCorrect ? (showHint ? 10 : 20) : 0}
          </p>
        </div>
      )}

      {showResult && (
        <button
          onClick={nextPuzzle}
          className="mt-4 w-full p-3 bg-violet-500 hover:bg-violet-600 rounded-xl text-white font-bold transition-colors"
        >
          {currentIndex < puzzles.length - 1 ? 'Следующая задача →' : 'Показать результат'}
        </button>
      )}

      <div className="flex items-center justify-between mt-4 text-violet-300 text-sm">
        <span className="flex items-center gap-1"><Brain className="w-4 h-4" /> Решено: {score}</span>
        <span className="flex items-center gap-1"><Zap className="w-4 h-4" /> XP: {score * 20 - hintsUsed * 10}</span>
      </div>
    </div>
  )
}
