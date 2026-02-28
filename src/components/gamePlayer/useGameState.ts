'use client'

import { useState, useCallback } from 'react'
import { GameLesson } from '@/data/types'
import { GameState, GameResult } from './types'

export function useGameState(game: GameLesson) {
  const [state, setState] = useState<GameState>(() => ({
    currentTask: 0,
    score: 0,
    selectedAnswer: null,
    result: 'none' as GameResult,
    showHint: false,
    gameFinished: false,
    orderedItems: game.tasks?.[0]?.type === 'order' && game.tasks[0].options
      ? [...game.tasks[0].options].sort(() => Math.random() - 0.5)
      : [],
    filledAnswer: '',
    selectedItems: []
  }))

  const setAnswer = useCallback((answer: string, isCorrect: boolean) => {
    setState(prev => ({
      ...prev,
      selectedAnswer: answer,
      result: isCorrect ? 'correct' : 'wrong',
      score: isCorrect ? prev.score + 1 : prev.score,
      showHint: false
    }))
  }, [])

  const toggleFindItem = useCallback((item: string) => {
    setState(prev => ({
      ...prev,
      selectedItems: prev.selectedItems.includes(item)
        ? prev.selectedItems.filter(i => i !== item)
        : [...prev.selectedItems, item]
    }))
  }, [])

  const moveOrderedItem = useCallback((index: number, direction: 'up' | 'down') => {
    setState(prev => {
      const newItems = [...prev.orderedItems]
      const newIndex = direction === 'up' ? index - 1 : index + 1
      if (newIndex >= 0 && newIndex < newItems.length) {
        [newItems[index], newItems[newIndex]] = [newItems[newIndex], newItems[index]]
      }
      return { ...prev, orderedItems: newItems }
    })
  }, [])

  const nextTask = useCallback(() => {
    setState(prev => {
      if (!game.tasks || prev.currentTask >= game.tasks.length - 1) {
        return { ...prev, gameFinished: true }
      }
      const nextIdx = prev.currentTask + 1
      const nextTaskData = game.tasks[nextIdx]
      return {
        ...prev,
        currentTask: nextIdx,
        selectedAnswer: null,
        result: 'none',
        showHint: false,
        filledAnswer: '',
        selectedItems: [],
        orderedItems: nextTaskData?.type === 'order' && nextTaskData.options
          ? [...nextTaskData.options].sort(() => Math.random() - 0.5)
          : prev.orderedItems
      }
    })
  }, [game.tasks])

  const restartGame = useCallback(() => {
    const firstTask = game.tasks?.[0]
    setState({
      currentTask: 0,
      score: 0,
      selectedAnswer: null,
      result: 'none',
      showHint: false,
      gameFinished: false,
      filledAnswer: '',
      selectedItems: [],
      orderedItems: firstTask?.type === 'order' && firstTask.options
        ? [...firstTask.options].sort(() => Math.random() - 0.5)
        : []
    })
  }, [game.tasks])

  const showHint = useCallback(() => {
    setState(prev => ({ ...prev, showHint: true }))
  }, [])

  const setFilledAnswer = useCallback((answer: string) => {
    setState(prev => ({ ...prev, filledAnswer: answer }))
  }, [])

  return {
    state,
    setAnswer,
    toggleFindItem,
    moveOrderedItem,
    nextTask,
    restartGame,
    showHint,
    setFilledAnswer
  }
}

export function calculateStars(score: number, total: number): number {
  if (score >= total * 0.9) return 3
  if (score >= total * 0.6) return 2
  return 1
}
