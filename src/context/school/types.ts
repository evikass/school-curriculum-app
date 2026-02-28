export type ViewType = 'classes' | 'subjects' | 'lessons' | 'games' | 'gameplay'

export interface DailyProgress {
  lessonsCompleted: number
  gamesPlayed: number
  pointsEarned: number
}

export interface Progress {
  totalPoints: number
  completedTopics: Record<string, boolean>
  achievements: string[]
  streak: number
  lastActiveDate: string
  gamesPlayed: number
  correctAnswers: number
  totalAnswers: number
  favoriteSubject: string | null
  dailyProgress: Record<string, DailyProgress>
  todayLessons: number
  todayGames: number
  todayPoints: number
}

export interface SchoolContextType {
  selectedClass: number | null
  view: ViewType
  selectedSubject: any | null
  selectedGame: any | null
  progress: Progress
  subjects: any[]
  games: any[]

  goToClass: (cls: number) => void
  goToSubject: (subject: any) => void
  goToGames: () => void
  goBack: () => void
  selectGame: (game: any | null) => void
  addPoints: (points: number) => void
  completeTopic: (topicKey: string) => void
  recordGameResult: (correct: number, total: number, subject: string) => void
  unlockAchievement: (achievementId: string) => void
  resetProgress: () => void
  setView: (view: ViewType) => void

  isKidMode: boolean
  totalPoints: number
  totalStars: number
  streak: number
}
