'use client'

import { CheckCircle, Star, ChevronRight } from 'lucide-react'
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
    <button onClick={() => onOpenDetail(lesson)} className={`w-full p-6 rounded-3xl border-4 transition-all text-left group
      ${isCompleted ? 'bg-green-500/20 border-green-400/50 hover:bg-green-500/30' : 'bg-white/5 border-white/20 hover:border-purple-400/50 hover:bg-white/10'}`}>
      <div className="flex items-center gap-4">
        {isCompleted ? (
          <div className="p-2 rounded-full bg-green-400 group-hover:scale-110 transition-transform">
            <CheckCircle className="w-6 h-6 text-white" />
          </div>
        ) : (
          <div className="p-2 rounded-xl bg-gradient-to-br from-yellow-400 to-orange-500 group-hover:scale-110 transition-transform">
            <Star className="w-6 h-6 text-white" />
          </div>
        )}
        <div className="flex-1">
          <h4 className="text-xl font-bold text-white mb-1 group-hover:text-purple-300 transition-colors">{lesson.title}</h4>
          <p className="text-base text-gray-400 line-clamp-2">{lesson.description}</p>
        </div>
        <div className="text-purple-400 group-hover:translate-x-2 transition-transform">
          <ChevronRight className="w-8 h-8" />
        </div>
      </div>
      {lesson.tasks && lesson.tasks.length > 0 && (
        <div className="mt-3 ml-14 p-3 rounded-xl bg-purple-500/20 border border-purple-400/30">
          <p className="text-purple-200 text-lg font-medium">📝 {lesson.tasks.length} заданий</p>
        </div>
      )}
    </button>
  )
}
