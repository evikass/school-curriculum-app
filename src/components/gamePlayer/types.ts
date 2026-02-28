export type GameResult = 'none' | 'correct' | 'wrong'

export interface GameState {
  currentTask: number
  score: number
  selectedAnswer: string | null
  result: GameResult
  showHint: boolean
  gameFinished: boolean
  orderedItems: string[]
  filledAnswer: string
  selectedItems: string[]
}

export type GameAction =
  | { type: 'SET_ANSWER'; answer: string; isCorrect: boolean }
  | { type: 'SET_FILL_ANSWER'; answer: string; isCorrect: boolean }
  | { type: 'TOGGLE_FIND_ITEM'; item: string }
  | { type: 'SET_FIND_RESULT'; isCorrect: boolean; answer: string }
  | { type: 'SET_ORDER_ITEMS'; items: string[] }
  | { type: 'SET_ORDER_RESULT'; isCorrect: boolean; answer: string }
  | { type: 'NEXT_TASK'; orderedItems: string[] }
  | { type: 'RESTART'; orderedItems: string[] }
  | { type: 'SHOW_HINT' }
  | { type: 'FINISH_GAME' }
