'use client'

import { ChevronLeft, Star, Lightbulb, ArrowRight, Trophy } from 'lucide-react'
import { GameLesson } from '@/data/types'
import { useGameState, calculateStars, QuizTask, FindTask, FillTask, OrderTask, GameFinishedScreen, ResultFeedback } from './gamePlayer'

interface GamePlayerProps {
  game: GameLesson
  onBack: () => void
  onComplete: (stars: number) => void
}

export default function GamePlayer({ game, onBack, onComplete }: GamePlayerProps) {
  const { state, setAnswer, toggleFindItem, moveOrderedItem, nextTask, restartGame, showHint, setFilledAnswer } = useGameState(game)

  if (!game.tasks || game.tasks.length === 0) {
    return (
      <div className="min-h-[60vh] flex items-center justify-center">
        <div className="bg-slate-800/80 backdrop-blur-xl rounded-3xl p-8 text-center max-w-md w-full border border-slate-700/50 shadow-2xl">
          <h2 className="text-2xl font-bold text-white mb-4">{game.title}</h2>
          <p className="text-slate-300 mb-6">Для этой игры пока нет заданий</p>
          <button onClick={onBack} className="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-500 hover:opacity-90 rounded-xl text-white font-medium transition-opacity">
            Вернуться
          </button>
        </div>
      </div>
    )
  }

  const task = game.tasks[state.currentTask]
  const progress = (state.currentTask / game.tasks.length) * 100

  const handleQuizAnswer = (answer: string) => setAnswer(answer, answer === task.correctAnswer)

  const handleFillAnswer = () => setAnswer(state.filledAnswer, state.filledAnswer.toUpperCase() === (task.correctAnswer as string).toUpperCase())

  const handleFindCheck = () => {
    const correct = task.correctAnswer as string[]
    const isCorrect = correct.length === state.selectedItems.length && correct.every(item => state.selectedItems.includes(item))
    setAnswer(state.selectedItems.join(', '), isCorrect)
  }

  const handleOrderCheck = () => {
    const isCorrect = state.orderedItems.join(', ') === (task.correctAnswer as string)
    setAnswer(state.orderedItems.join(', '), isCorrect)
  }

  const handleNextTask = () => {
    if (state.currentTask >= game.tasks!.length - 1) {
      const stars = calculateStars(state.score, game.tasks!.length)
      onComplete(stars)
    }
    nextTask()
  }

  // Game finished screen
  if (state.gameFinished) {
    const stars = calculateStars(state.score, game.tasks.length)
    return (
      <GameFinishedScreen
        score={state.score}
        totalTasks={game.tasks.length}
        stars={stars}
        rewardMessage={game.reward.message}
        onRestart={restartGame}
        onBack={onBack}
      />
    )
  }

  return (
    <div className="animate-fadeIn">
      {/* Back button */}
      <button onClick={onBack} className="mb-6 flex items-center gap-2 text-slate-300 hover:text-white transition-colors group">
        <ChevronLeft className="w-5 h-5 group-hover:-translate-x-1 transition-transform" />
        <span>Назад к урокам</span>
      </button>

      {/* Game header */}
      <div className="bg-slate-800/60 backdrop-blur-xl rounded-2xl p-6 mb-6 border border-slate-700/50">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-bold text-white">{game.title}</h2>
          <div className="flex items-center gap-2">
            <Star className="w-6 h-6 text-yellow-400 fill-yellow-400" />
            <span className="text-xl font-bold text-yellow-400">{state.score}/{game.tasks.length}</span>
          </div>
        </div>
        <div className="h-3 bg-slate-700 rounded-full overflow-hidden">
          <div className="h-full bg-gradient-to-r from-purple-500 to-blue-500 transition-all duration-500" style={{ width: `${progress}%` }} />
        </div>
        <p className="text-slate-400 text-sm mt-2">Задание {state.currentTask + 1} из {game.tasks.length}</p>
      </div>

      {/* Task content */}
      <div className="bg-slate-800/60 backdrop-blur-xl rounded-2xl p-6 border border-slate-700/50">
        <div className="mb-6">
          <h3 className="text-xl font-semibold text-white mb-2">{task.question}</h3>

          {/* Hint button */}
          {state.result === 'none' && !state.showHint && (
            <button onClick={showHint} className="flex items-center gap-2 text-purple-400 hover:text-purple-300 transition-colors">
              <Lightbulb className="w-5 h-5" />
              Показать подсказку
            </button>
          )}

          {state.showHint && (
            <div className="mt-3 p-4 bg-purple-500/20 rounded-xl border border-purple-500/30">
              <p className="text-purple-300 flex items-center gap-2">
                <Lightbulb className="w-5 h-5" />
                {task.hint}
              </p>
            </div>
          )}
        </div>

        {/* Task types */}
        {(task.type === 'quiz' || task.type === 'match') && (
          <QuizTask task={task} result={state.result} selectedAnswer={state.selectedAnswer} onAnswer={handleQuizAnswer} />
        )}

        {task.type === 'find' && (
          <FindTask task={task} result={state.result} selectedItems={state.selectedItems} onToggleItem={toggleFindItem} onCheck={handleFindCheck} />
        )}

        {task.type === 'fill' && (
          <FillTask task={task} result={state.result} filledAnswer={state.filledAnswer} onFillChange={setFilledAnswer} onCheck={handleFillAnswer} />
        )}

        {task.type === 'order' && (
          <OrderTask items={state.orderedItems} result={state.result} onMove={moveOrderedItem} onCheck={handleOrderCheck} />
        )}

        {/* Result feedback */}
        <ResultFeedback result={state.result} correctAnswer={task.correctAnswer} />

        {/* Next button */}
        {state.result !== 'none' && (
          <button onClick={handleNextTask} className="mt-6 w-full py-4 bg-gradient-to-r from-purple-600 to-blue-500 hover:opacity-90 rounded-xl text-white font-medium text-lg transition-opacity flex items-center justify-center gap-2">
            {state.currentTask < game.tasks.length - 1 ? (
              <>Следующее задание <ArrowRight className="w-5 h-5" /></>
            ) : (
              <>Завершить игру <Trophy className="w-5 h-5" /></>
            )}
          </button>
        )}
      </div>
    </div>
  )
}
