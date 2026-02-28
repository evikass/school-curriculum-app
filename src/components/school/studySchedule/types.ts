export interface ScheduleItem {
  id: string
  subject: string
  time: string
  duration: number // минуты
  days: number[] // 0-6 (вс-сб)
  active: boolean
}

export interface SubjectInfo {
  name: string
  icon: string
  color: string
}

export interface StudySession {
  date: string
  subject: string
  duration: number
  lessonsCompleted: number
  gamesPlayed: number
  pointsEarned: number
}
