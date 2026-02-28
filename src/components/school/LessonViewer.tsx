'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { LessonTopic, TopicSection, GameLesson } from '@/data/types'
import {
  ArrowLeft, ChevronDown, ChevronRight, BookOpen, Gamepad2, HelpCircle, Play,
  CheckCircle, Star, Sparkles, FileText, ClipboardList
} from 'lucide-react'
import LessonDetailModal from './LessonDetailModal'
import LessonQuiz from './LessonQuiz'

interface SelectedLesson {
  title: string
  description: string
  tasks: string[]
  image?: string
  content?: string
  examples?: string[]
  facts?: string[]
}

export default function LessonViewer() {
  const { selectedSubject, selectedClass, completeTopic, goBack, selectGame, isKidMode } = useSchool()
  const [expandedTopics, setExpandedTopics] = useState<Set<string>>(new Set())
  const [currentTab, setCurrentTab] = useState<'lessons' | 'games'>('lessons')
  
  // Для модального окна подробного урока
  const [detailLesson, setDetailLesson] = useState<SelectedLesson | null>(null)
  const [isDetailOpen, setIsDetailOpen] = useState(false)
  
  // Для теста
  const [quizLesson, setQuizLesson] = useState<SelectedLesson | null>(null)
  const [isQuizOpen, setIsQuizOpen] = useState(false)
  const [completedQuizzes, setCompletedQuizzes] = useState<Set<string>>(new Set())

  if (!selectedSubject) return null

  const toggleTopic = (topicName: string) => {
    const newExpanded = new Set(expandedTopics)
    if (newExpanded.has(topicName)) {
      newExpanded.delete(topicName)
    } else {
      newExpanded.add(topicName)
    }
    setExpandedTopics(newExpanded)
  }
  
  const openDetail = (lesson: SelectedLesson) => {
    setDetailLesson(lesson)
    setIsDetailOpen(true)
  }
  
  const openQuiz = (lesson: SelectedLesson, lessonKey: string) => {
    setQuizLesson({ ...lesson, title: `${lesson.title}` })
    setIsQuizOpen(true)
  }
  
  const handleQuizComplete = (score: number) => {
    if (quizLesson) {
      setCompletedQuizzes(new Set([...completedQuizzes, quizLesson.title]))
    }
  }
  
  const handleDetailComplete = () => {
    if (detailLesson) {
      // Отметить урок как пройденный
    }
  }

  return (
    <div className="w-full animate-fadeIn">
      {/* Back button */}
      <button
        onClick={goBack}
        className="mb-6 flex items-center gap-2 text-white/80 hover:text-white text-xl font-medium 
                   bg-white/10 hover:bg-white/20 px-6 py-3 rounded-2xl transition-all"
      >
        <ArrowLeft className="w-6 h-6" /> 
        Назад к предметам
      </button>

      {/* Title */}
      <div className="flex items-center gap-4 mb-8">
        <div className="p-4 rounded-2xl bg-gradient-to-br from-purple-500 to-blue-500">
          <BookOpen className="w-10 h-10 text-white" />
        </div>
        <div>
          <h2 className="text-3xl md:text-4xl font-black text-white">
            {selectedSubject.title}
          </h2>
          <p className="text-purple-200">
            {selectedSubject.detailedTopics?.reduce((acc, t) => 
              acc + (t.subtopics?.reduce((a, s) => a + s.lessons.length, 0) || t.lessons?.length || 0), 0
            ) || 0} уроков доступно
          </p>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
        <button
          onClick={() => setCurrentTab('lessons')}
          className={`px-6 py-3 rounded-2xl font-bold text-lg transition-all whitespace-nowrap
            ${currentTab === 'lessons' 
              ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg' 
              : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
        >
          📘 Уроки
        </button>
        {selectedSubject.games && selectedSubject.games.length > 0 && (
          <button
            onClick={() => setCurrentTab('games')}
            className={`px-6 py-3 rounded-2xl font-bold text-lg transition-all whitespace-nowrap
              ${currentTab === 'games' 
                ? 'bg-gradient-to-r from-green-500 to-teal-500 text-white shadow-lg' 
                : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            🎮 Игры ({selectedSubject.games.length})
          </button>
        )}
      </div>

      {/* Content */}
      {currentTab === 'lessons' && selectedSubject.detailedTopics && (
        <div className="space-y-4">
          {selectedSubject.detailedTopics.map((topicBlock: LessonTopic, topicIndex: number) => {
            const topicKey = topicBlock.topic
            const isExpanded = expandedTopics.has(topicKey)
            const totalLessons = topicBlock.subtopics 
              ? topicBlock.subtopics.reduce((acc, st) => acc + st.lessons.length, 0)
              : (topicBlock.lessons?.length || 0)

            return (
              <div key={topicIndex} 
                   className="rounded-3xl overflow-hidden bg-gradient-to-br from-gray-800/80 to-gray-900/80 
                              border-2 border-white/10">
                {/* Topic header */}
                <button
                  onClick={() => toggleTopic(topicKey)}
                  className="w-full px-6 py-5 flex items-center justify-between text-left
                             hover:bg-white/5 transition-colors"
                >
                  <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-500 
                                    flex items-center justify-center text-white font-black text-xl">
                      {topicIndex + 1}
                    </div>
                    <div>
                      <span className="text-xl font-bold text-white">{topicBlock.topic}</span>
                      <div className="text-sm text-purple-300">{totalLessons} уроков</div>
                    </div>
                  </div>
                  {isExpanded ? (
                    <ChevronDown className="w-6 h-6 text-purple-400" />
                  ) : (
                    <ChevronRight className="w-6 h-6 text-purple-400" />
                  )}
                </button>

                {/* Expanded content */}
                {isExpanded && (
                  <div className="px-6 pb-6 space-y-6 bg-gray-900/30">
                    {/* Subtopics */}
                    {topicBlock.subtopics ? (
                      topicBlock.subtopics.map((subtopic: TopicSection, subtopicIndex: number) => (
                        <div key={subtopicIndex} className="mt-4">
                          <h4 className="text-lg font-bold text-cyan-300 mb-4 flex items-center gap-3">
                            <span className="w-8 h-8 rounded-xl bg-cyan-500/20 flex items-center justify-center text-cyan-300">
                              {subtopicIndex + 1}
                            </span>
                            {subtopic.title}
                          </h4>
                          <div className="space-y-4 pl-4">
                            {subtopic.lessons.map((lesson, lessonIndex) => {
                              const lessonKey = `${topicKey}-${subtopicIndex}-${lessonIndex}`
                              const isQuizCompleted = completedQuizzes.has(lesson.title)
                              
                              return (
                                <div key={lessonIndex} 
                                     className="p-5 rounded-2xl bg-white/5 border border-white/10 hover:border-purple-400/50 transition-all">
                                  <div className="flex items-start justify-between gap-4">
                                    <div className="flex-1">
                                      <h5 className="text-lg font-bold text-purple-300 mb-2 flex items-center gap-2">
                                        <Star className="w-5 h-5 text-yellow-400" />
                                        {lesson.title}
                                      </h5>
                                      <p className="text-gray-400 text-sm line-clamp-2">
                                        {lesson.description}
                                      </p>
                                    </div>
                                    
                                    {/* Кнопки действий */}
                                    <div className="flex gap-2 flex-shrink-0">
                                      <button
                                        onClick={() => openDetail(lesson)}
                                        className="px-4 py-2 bg-gradient-to-r from-blue-500 to-cyan-500
                                                   hover:from-blue-600 hover:to-cyan-600
                                                   text-white rounded-xl font-medium text-sm
                                                   flex items-center gap-2 transition-all hover:scale-105"
                                      >
                                        <FileText className="w-4 h-4" />
                                        Урок
                                      </button>
                                      <button
                                        onClick={() => openQuiz(lesson, lessonKey)}
                                        className={`px-4 py-2 rounded-xl font-medium text-sm
                                                   flex items-center gap-2 transition-all hover:scale-105
                                                   ${isQuizCompleted 
                                                     ? 'bg-green-500 text-white'
                                                     : 'bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white'
                                                   }`}
                                      >
                                        <ClipboardList className="w-4 h-4" />
                                        {isQuizCompleted ? '✓ Тест' : 'Тест'}
                                      </button>
                                    </div>
                                  </div>
                                  
                                  {/* Превью заданий */}
                                  {lesson.tasks && lesson.tasks.length > 0 && (
                                    <div className="mt-3 p-3 rounded-xl bg-purple-500/10 border border-purple-400/20">
                                      <p className="text-purple-300 text-sm font-medium mb-1">
                                        📝 Заданий: {lesson.tasks.length}
                                      </p>
                                      <p className="text-purple-200/60 text-xs">
                                        {lesson.tasks.slice(0, 2).join(' • ')}...
                                      </p>
                                    </div>
                                  )}
                                </div>
                              )
                            })}
                          </div>
                        </div>
                      ))
                    ) : (
                      /* Old structure */
                      topicBlock.lessons?.map((lesson, lessonIndex) => {
                        const lessonKey = `${topicKey}-${lessonIndex}`
                        const isQuizCompleted = completedQuizzes.has(lesson.title)
                        
                        return (
                          <div key={lessonIndex} 
                               className="p-5 rounded-2xl bg-white/5 border border-white/10 hover:border-purple-400/50">
                            <div className="flex items-start justify-between gap-4">
                              <div className="flex-1">
                                <h4 className="text-xl font-bold text-purple-300 mb-2">{lesson.title}</h4>
                                <p className="text-gray-400 text-sm line-clamp-2">
                                  {lesson.description}
                                </p>
                              </div>
                              
                              {/* Кнопки действий */}
                              <div className="flex gap-2 flex-shrink-0">
                                <button
                                  onClick={() => openDetail(lesson)}
                                  className="px-4 py-2 bg-gradient-to-r from-blue-500 to-cyan-500
                                             hover:from-blue-600 hover:to-cyan-600
                                             text-white rounded-xl font-medium text-sm
                                             flex items-center gap-2 transition-all hover:scale-105"
                                >
                                  <FileText className="w-4 h-4" />
                                  Урок
                                </button>
                                <button
                                  onClick={() => openQuiz(lesson, lessonKey)}
                                  className={`px-4 py-2 rounded-xl font-medium text-sm
                                             flex items-center gap-2 transition-all hover:scale-105
                                             ${isQuizCompleted 
                                               ? 'bg-green-500 text-white'
                                               : 'bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white'
                                             }`}
                                >
                                  <ClipboardList className="w-4 h-4" />
                                  {isQuizCompleted ? '✓ Тест' : 'Тест'}
                                </button>
                              </div>
                            </div>
                            
                            {lesson.tasks && lesson.tasks.length > 0 && (
                              <div className="mt-4 p-4 rounded-xl bg-purple-500/10 border border-purple-400/20">
                                <p className="text-purple-300 font-medium mb-2">📝 Задания:</p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-1">
                                  {lesson.tasks.map((task, i) => (
                                    <li key={i}>{task}</li>
                                  ))}
                                </ul>
                              </div>
                            )}
                          </div>
                        )
                      })
                    )}
                  </div>
                )}
              </div>
            )
          })}
        </div>
      )}

      {/* Games tab */}
      {currentTab === 'games' && selectedSubject.games && (
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {selectedSubject.games.map((game: GameLesson, index: number) => (
            <button
              key={index}
              onClick={() => selectGame(game)}
              className="p-6 rounded-3xl bg-gradient-to-br from-purple-600/50 to-pink-600/50 
                         border-2 border-white/20 hover:border-white/40
                         text-left transition-all hover:scale-[1.02] group"
            >
              <div className="flex items-center gap-4 mb-3">
                <div className="p-3 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500">
                  <Gamepad2 className="w-8 h-8 text-white" />
                </div>
                <div>
                  <h4 className="text-xl font-bold text-white">{game.title}</h4>
                  <p className="text-purple-200">{game.tasks.length} заданий</p>
                </div>
              </div>
              <div className="flex items-center gap-2 text-yellow-400">
                <Star className="w-5 h-5 fill-yellow-400" />
                <span className="font-medium">{game.reward.stars} звёзд</span>
                <Play className="w-5 h-5 ml-auto group-hover:scale-110 transition-transform" />
              </div>
            </button>
          ))}
        </div>
      )}
      
      {/* Модальные окна */}
      <LessonDetailModal
        lesson={detailLesson}
        isOpen={isDetailOpen}
        onClose={() => setIsDetailOpen(false)}
        onComplete={handleDetailComplete}
      />
      
      <LessonQuiz
        lessonTitle={quizLesson?.title || ''}
        lessonDescription={quizLesson?.description || ''}
        isOpen={isQuizOpen}
        onClose={() => setIsQuizOpen(false)}
        onComplete={handleQuizComplete}
      />
    </div>
  )
}
