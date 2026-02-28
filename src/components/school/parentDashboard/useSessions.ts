'use client'

import { useState, useEffect, useMemo } from 'react'
import { StudySession, SessionStats } from './types'

const generateDemoSessions = (): StudySession[] => {
  const sessions: StudySession[] = []
  const subjects = ['Русский язык', 'Математика', 'Окружающий мир', 'Литература']
  const today = new Date()

  for (let i = 0; i < 14; i++) {
    const date = new Date(today)
    date.setDate(date.getDate() - i)
    sessions.push({
      date: date.toISOString().split('T')[0],
      subject: subjects[Math.floor(Math.random() * subjects.length)],
      duration: Math.floor(Math.random() * 30) + 10,
      lessonsCompleted: Math.floor(Math.random() * 3) + 1,
      gamesPlayed: Math.floor(Math.random() * 2),
      pointsEarned: Math.floor(Math.random() * 50) + 10
    })
  }
  return sessions
}

export function useSessions() {
  const [sessions, setSessions] = useState<StudySession[]>(() => {
    if (typeof window === 'undefined') return []
    const saved = localStorage.getItem('studySessions')
    if (saved) return JSON.parse(saved)
    const demo = generateDemoSessions()
    localStorage.setItem('studySessions', JSON.stringify(demo))
    return demo
  })

  const stats: SessionStats = useMemo(() => {
    const totalDuration = sessions.reduce((sum, s) => sum + s.duration, 0)
    const totalLessons = sessions.reduce((sum, s) => sum + s.lessonsCompleted, 0)
    const totalGames = sessions.reduce((sum, s) => sum + s.gamesPlayed, 0)
    const avgDuration = sessions.length > 0 ? Math.round(totalDuration / sessions.length) : 0

    const weekAgo = new Date()
    weekAgo.setDate(weekAgo.getDate() - 7)
    const weekSessions = sessions.filter(s => new Date(s.date) >= weekAgo)
    const weekDuration = weekSessions.reduce((sum, s) => sum + s.duration, 0)

    const bySubject: Record<string, { duration: number; lessons: number }> = {}
    sessions.forEach(s => {
      if (!bySubject[s.subject]) {
        bySubject[s.subject] = { duration: 0, lessons: 0 }
      }
      bySubject[s.subject].duration += s.duration
      bySubject[s.subject].lessons += s.lessonsCompleted
    })

    return { totalDuration, totalLessons, totalGames, avgDuration, weekDuration, weekSessions: weekSessions.length, bySubject }
  }, [sessions])

  return { sessions, stats }
}
