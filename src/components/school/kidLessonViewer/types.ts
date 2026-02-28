import { LessonItem } from '@/data/types'

export type SelectedLesson = LessonItem & {
  tasks: string[]
  description: string
}

export interface LessonViewerState {
  expandedTopics: Set<string>
  currentTab: 'lessons' | 'games'
  completedLessons: Set<string>
  completedQuizzes: Set<string>
  detailLesson: SelectedLesson | null
  isDetailOpen: boolean
  quizLesson: SelectedLesson | null
  isQuizOpen: boolean
}
