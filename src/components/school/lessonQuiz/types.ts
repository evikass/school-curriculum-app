export interface QuestionItem {
  type: string
  question: string
  options: string[]
  correct: number
  hint: string
}

export interface QuizState {
  currentQuestion: number
  selectedAnswer: number | null
  showResult: boolean
  score: number
  isComplete: boolean
  wrongAnswers: number[]
}
