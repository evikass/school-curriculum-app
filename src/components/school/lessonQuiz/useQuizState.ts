'use client'

import { useState, useCallback } from 'react'
import { QuestionItem, QuizState } from './types'

export function useQuizState(questions: QuestionItem[]) {
  const [state, setState] = useState<QuizState>({
    currentQuestion: 0,
    selectedAnswer: null,
    showResult: false,
    score: 0,
    isComplete: false,
    wrongAnswers: []
  })

  const handleAnswer = useCallback((answerIndex: number) => {
    if (state.showResult) return

    const isCorrect = answerIndex === questions[state.currentQuestion].correct
    setState(prev => ({
      ...prev,
      selectedAnswer: answerIndex,
      showResult: true,
      score: isCorrect ? prev.score + 1 : prev.score,
      wrongAnswers: isCorrect ? prev.wrongAnswers : [...prev.wrongAnswers, prev.currentQuestion]
    }))
  }, [state.showResult, state.currentQuestion, questions])

  const nextQuestion = useCallback(() => {
    setState(prev => {
      if (prev.currentQuestion < questions.length - 1) {
        return { ...prev, currentQuestion: prev.currentQuestion + 1, selectedAnswer: null, showResult: false }
      }
      return { ...prev, isComplete: true }
    })
  }, [questions.length])

  const resetQuiz = useCallback(() => {
    setState({ currentQuestion: 0, selectedAnswer: null, showResult: false, score: 0, isComplete: false, wrongAnswers: [] })
  }, [])

  return { state, handleAnswer, nextQuestion, resetQuiz }
}

export function getScoreMessage(score: number, total: number) {
  const percentage = (score / total) * 100
  if (percentage >= 100) return { message: 'Превосходно! Идеальный результат! 🎉', color: 'text-yellow-400' }
  if (percentage >= 75) return { message: 'Отлично! Ты хорошо усвоил материал! 🌟', color: 'text-green-400' }
  if (percentage >= 50) return { message: 'Хорошо! Но есть над чем поработать! 💪', color: 'text-blue-400' }
  return { message: 'Попробуй ещё раз! Ты справишься! 📚', color: 'text-orange-400' }
}
