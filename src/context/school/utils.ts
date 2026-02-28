import { Progress } from './types'

export function getTodayString(): string {
  return new Date().toISOString().split('T')[0]
}

export function calculateStreak(lastDate: string, currentStreak: number): number {
  const today = getTodayString()
  if (lastDate === today) return currentStreak

  const yesterday = new Date()
  yesterday.setDate(yesterday.getDate() - 1)
  const yesterdayString = yesterday.toISOString().split('T')[0]

  if (lastDate === yesterdayString) return currentStreak + 1
  return 1
}

export function getDefaultProgress(): Progress {
  return {
    totalPoints: 0,
    completedTopics: {},
    achievements: [],
    streak: 0,
    lastActiveDate: '',
    gamesPlayed: 0,
    correctAnswers: 0,
    totalAnswers: 0,
    favoriteSubject: null,
    dailyProgress: {},
    todayLessons: 0,
    todayGames: 0,
    todayPoints: 0
  }
}

export function getInitialProgress(): Progress {
  const defaultProgress = getDefaultProgress()

  if (typeof window === 'undefined') return defaultProgress

  try {
    const saved = localStorage.getItem('schoolProgress')
    if (saved) {
      return { ...defaultProgress, ...JSON.parse(saved) }
    }
  } catch {
    // ignore
  }
  return defaultProgress
}

export function saveProgressToStorage(progress: Progress): void {
  if (typeof window !== 'undefined') {
    localStorage.setItem('schoolProgress', JSON.stringify(progress))
  }
}
