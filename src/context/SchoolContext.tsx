'use client'

import { createContext, useContext, useState, useMemo, ReactNode } from 'react'
import { getSubjectsForGrade, allGames } from '@/data'
import { SubjectData, GameLesson } from '@/data/types'
import { ViewType, Progress, getInitialProgress, getTodayString, calculateStreak, saveProgressToStorage, getDefaultProgress } from './school'

interface SchoolContextType {
  selectedClass: number | null
  view: ViewType
  selectedSubject: SubjectData | null
  selectedGame: GameLesson | null
  progress: Progress
  subjects: SubjectData[]
  games: GameLesson[]
  goToClass: (cls: number) => void
  goToSubject: (subject: SubjectData) => void
  goToGames: () => void
  goBack: () => void
  selectGame: (game: GameLesson | null) => void
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

const SchoolContext = createContext<SchoolContextType | null>(null)

export function useSchool() {
  const context = useContext(SchoolContext)
  if (!context) throw new Error('useSchool must be used within SchoolProvider')
  return context
}

export function SchoolProvider({ children }: { children: ReactNode }) {
  const [selectedClass, setSelectedClass] = useState<number | null>(null)
  const [view, setView] = useState<ViewType>('classes')
  const [selectedSubject, setSelectedSubject] = useState<SubjectData | null>(null)
  const [selectedGame, setSelectedGame] = useState<GameLesson | null>(null)
  const [progress, setProgress] = useState<Progress>(getInitialProgress)

  const subjects = useMemo(() => selectedClass !== null ? getSubjectsForGrade(selectedClass) : [], [selectedClass])
  const games = useMemo(() => {
    if (selectedClass === null) return []
    return allGames[selectedClass] || []
  }, [selectedClass])
  const isKidMode = selectedClass !== null && selectedClass <= 2

  const updateProgress = (updates: Partial<Progress>) => {
    const newProgress = { ...progress, ...updates }
    setProgress(newProgress)
    saveProgressToStorage(newProgress)
  }

  const addPoints = (points: number) => {
    const today = getTodayString()
    const newStreak = calculateStreak(progress.lastActiveDate, progress.streak)
    updateProgress({
      totalPoints: progress.totalPoints + points,
      streak: newStreak,
      lastActiveDate: today,
      todayPoints: progress.lastActiveDate === today ? progress.todayPoints + points : points
    })
  }

  const completeTopic = (topicKey: string) => {
    if (!progress.completedTopics[topicKey]) {
      const today = getTodayString()
      const newStreak = calculateStreak(progress.lastActiveDate, progress.streak)
      updateProgress({
        completedTopics: { ...progress.completedTopics, [topicKey]: true },
        totalPoints: progress.totalPoints + 10,
        streak: newStreak,
        lastActiveDate: today,
        todayLessons: progress.lastActiveDate === today ? progress.todayLessons + 1 : 1,
        todayPoints: progress.lastActiveDate === today ? progress.todayPoints + 10 : 10
      })
    }
  }

  const recordGameResult = (correct: number, total: number, subject: string) => {
    const today = getTodayString()
    const newStreak = calculateStreak(progress.lastActiveDate, progress.streak)
    updateProgress({
      gamesPlayed: progress.gamesPlayed + 1,
      correctAnswers: progress.correctAnswers + correct,
      totalAnswers: progress.totalAnswers + total,
      streak: newStreak,
      lastActiveDate: today,
      favoriteSubject: progress.favoriteSubject || subject,
      todayGames: progress.lastActiveDate === today ? progress.todayGames + 1 : 1
    })
  }

  const unlockAchievement = (achievementId: string) => {
    if (!progress.achievements.includes(achievementId)) {
      updateProgress({ achievements: [...progress.achievements, achievementId] })
    }
  }

  const goToClass = (cls: number) => { setSelectedClass(cls); setView('subjects'); setSelectedSubject(null) }
  const goToSubject = (subject: SubjectData) => { setSelectedSubject(subject); setView('lessons') }
  const goToGames = () => { setView('games'); setSelectedGame(null) }

  const goBack = () => {
    if (view === 'lessons') { setView('subjects'); setSelectedSubject(null) }
    else if (view === 'subjects') { setView('classes'); setSelectedClass(null) }
    else if (view === 'games') { setView('subjects') }
    else if (view === 'gameplay') { setView('games'); setSelectedGame(null) }
  }

  const selectGame = (game: GameLesson | null) => {
    setSelectedGame(game)
    setView(game ? 'gameplay' : 'games')
  }

  const resetProgress = () => {
    setProgress(getDefaultProgress())
    saveProgressToStorage(getDefaultProgress())
    setSelectedClass(null)
    setView('classes')
    setSelectedSubject(null)
    setSelectedGame(null)
  }

  return (
    <SchoolContext.Provider value={{
      selectedClass, view, selectedSubject, selectedGame, progress, subjects, games,
      goToClass, goToSubject, goToGames, goBack, selectGame,
      addPoints, completeTopic, recordGameResult, unlockAchievement, resetProgress, setView,
      isKidMode,
      totalPoints: progress.totalPoints,
      totalStars: Math.floor(progress.totalPoints / 10),
      streak: progress.streak
    }}>
      {children}
    </SchoolContext.Provider>
  )
}
