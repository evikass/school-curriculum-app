'use client'

import { CheckCircle, Star, FileText } from 'lucide-react'
import { SelectedLesson } from './types'

interface LessonCardProps {
  lesson: SelectedLesson
  lessonKey: string
  isCompleted: boolean
  isQuizCompleted: boolean
  onOpenDetail: (lesson: SelectedLesson) => void
}

export function LessonCard({ lesson, lessonKey, isCompleted, isQuizCompleted, onOpenDetail }: LessonCardProps) {
  return (
    <div className={`p-6 rounded-3xl border-4 transition-all
      ${isCompleted ? 'bg-green-500/20 border-green-400/50' : 'bg-white/5 border-white/20 hover:border-purple-400/50'}`}>
      <div className="flex items-start gap-4">
        {isCompleted ? (
          <div className="p-2 rounded-full bg-green-400">
            <CheckCircle className="w-6 h-6 text-white" />
          </div>
        ) : (
          <Star className="w-8 h-8 text-yellow-400 flex-shrink-0 mt-1" />
        )}
        <div className="flex-1">
          <h4 className="text-xl font-bold text-purple-200 mb-2">{lesson.title}</h4>
          <p className="text-base text-gray-400 line-clamp-2 mb-3">{lesson.description}</p>
          <button onClick={() => onOpenDetail(lesson)}
            className="w-full py-4 px-6 bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600 text-white rounded-2xl font-bold text-lg flex items-center justify-center gap-3 transition-all hover:scale-105">
            <FileText className="w-6 h-6" />Урок 📖
          </button>
        </div>
      </div>
    </div>
  )
}
