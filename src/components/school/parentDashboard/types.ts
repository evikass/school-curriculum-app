export interface StudySession {
  date: string
  subject: string
  duration: number // минуты
  lessonsCompleted: number
  gamesPlayed: number
  pointsEarned: number
}

export interface SessionStats {
  totalDuration: number
  totalLessons: number
  totalGames: number
  avgDuration: number
  weekDuration: number
  weekSessions: number
  bySubject: Record<string, { duration: number; lessons: number }>
}
