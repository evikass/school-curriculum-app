'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { LessonTopic, TopicSection, GameLesson } from '@/data/types'
import {
  ArrowLeft, ChevronDown, ChevronRight, BookOpen, Gamepad2, Play,
  CheckCircle, Star, Sparkles, Smile, FileText, ClipboardList
} from 'lucide-react'
import LessonDetailModal from './LessonDetailModal'
import LessonQuiz from './LessonQuiz'

interface SelectedLesson {
  title: string
  description: string
  tasks: string[]
}

export default function KidLessonViewer() {
  const { selectedSubject, selectedClass, completeTopic, goBack, selectGame } = useSchool()
  const [expandedTopics, setExpandedTopics] = useState<Set<string>>(new Set())
  const [currentTab, setCurrentTab] = useState<'lessons' | 'games'>('lessons')
  const [completedLessons, setCompletedLessons] = useState<Set<string>>(new Set())
  
  // Для модальных окон
  const [detailLesson, setDetailLesson] = useState<SelectedLesson | null>(null)
  const [isDetailOpen, setIsDetailOpen] = useState(false)
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

  const handleCompleteLesson = (lessonKey: string) => {
    if (!completedLessons.has(lessonKey)) {
      setCompletedLessons(new Set([...completedLessons, lessonKey]))
      completeTopic(lessonKey)
    }
  }
  
  const openDetail = (lesson: SelectedLesson) => {
    setDetailLesson(lesson)
    setIsDetailOpen(true)
  }
  
  const openQuiz = (lesson: SelectedLesson) => {
    setQuizLesson(lesson)
    setIsQuizOpen(true)
  }
  
  const handleQuizComplete = (score: number) => {
    if (quizLesson) {
      setCompletedQuizzes(new Set([...completedQuizzes, quizLesson.title]))
    }
  }

  const getGradeEmoji = () => {
    if (selectedClass === 0) return '🎒'
    if (selectedClass === 1) return '🌟'
    return '🦋'
  }

  return (
    <div className="w-full animate-bounceIn">
      {/* Back button - BIG for kids */}
      <button
        onClick={goBack}
        className="mb-8 flex items-center gap-3 text-white text-2xl font-bold 
                   bg-white/20 hover:bg-white/30 px-8 py-4 rounded-3xl transition-all
                   border-4 border-white/30 hover:border-white/50"
      >
        <ArrowLeft className="w-8 h-8" /> 
        Назад
      </button>

      {/* Title with emoji */}
      <div className="flex items-center gap-5 mb-8">
        <div className="p-5 rounded-3xl bg-gradient-to-br from-yellow-400 to-orange-500">
          <BookOpen className="w-12 h-12 text-white" />
        </div>
        <div>
          <h2 className="text-3xl md:text-5xl font-black text-white">
            {selectedSubject.title}
          </h2>
          <p className="text-xl text-purple-200 mt-1">
            {getGradeEmoji()} Уроки и игры
          </p>
        </div>
      </div>

      {/* Tabs - BIG BUTTONS */}
      <div className="flex gap-4 mb-8 overflow-x-auto pb-2">
        <button
          onClick={() => setCurrentTab('lessons')}
          className={`px-8 py-5 rounded-3xl font-black text-2xl transition-all whitespace-nowrap flex items-center gap-3
            ${currentTab === 'lessons' 
              ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg scale-105' 
              : 'bg-white/20 text-white hover:bg-white/30'}`}
        >
          📘 Уроки
        </button>
        {selectedSubject.games && selectedSubject.games.length > 0 && (
          <button
            onClick={() => setCurrentTab('games')}
            className={`px-8 py-5 rounded-3xl font-black text-2xl transition-all whitespace-nowrap flex items-center gap-3
              ${currentTab === 'games' 
                ? 'bg-gradient-to-r from-green-500 to-teal-500 text-white shadow-lg scale-105' 
                : 'bg-white/20 text-white hover:bg-white/30'}`}
          >
            🎮 Игры ({selectedSubject.games.length})
          </button>
        )}
      </div>

      {/* Content */}
      {currentTab === 'lessons' && selectedSubject.detailedTopics && (
        <div className="space-y-6">
          {/* Helper character */}
          <div className="flex items-start gap-4 p-6 rounded-3xl bg-gradient-to-r from-yellow-400/20 to-orange-400/20 
                          border-4 border-yellow-400/30 mb-6">
            <div className="text-5xl animate-wiggle">🦉</div>
            <div>
              <p className="text-xl text-white font-bold mb-2">Мудрая Сова</p>
              <p className="text-lg text-purple-200">
                Нажми «Урок» чтобы прочитать, или «Тест» чтобы проверить знания! 📚✨
              </p>
            </div>
          </div>

          {selectedSubject.detailedTopics.map((topicBlock: LessonTopic, topicIndex: number) => {
            const topicKey = topicBlock.topic
            const isExpanded = expandedTopics.has(topicKey)
            const totalLessons = topicBlock.subtopics 
              ? topicBlock.subtopics.reduce((acc, st) => acc + st.lessons.length, 0)
              : (topicBlock.lessons?.length || 0)

            return (
              <div key={topicIndex} 
                   className="rounded-3xl overflow-hidden bg-gradient-to-br from-indigo-600/40 to-purple-600/40 
                              border-4 border-white/20">
                {/* Topic header - BIG */}
                <button
                  onClick={() => toggleTopic(topicKey)}
                  className="w-full px-8 py-6 flex items-center justify-between text-left
                             hover:bg-white/10 transition-colors"
                >
                  <div className="flex items-center gap-5">
                    <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-cyan-400 to-blue-500 
                                    flex items-center justify-center text-white font-black text-2xl shadow-lg">
                      {topicIndex + 1}
                    </div>
                    <div>
                      <span className="text-2xl md:text-3xl font-bold text-white">{topicBlock.topic}</span>
                      <div className="text-lg text-purple-200 mt-1">{totalLessons} уроков</div>
                    </div>
                  </div>
                  {isExpanded ? (
                    <ChevronDown className="w-8 h-8 text-purple-300" />
                  ) : (
                    <ChevronRight className="w-8 h-8 text-purple-300" />
                  )}
                </button>

                {/* Expanded content */}
                {isExpanded && (
                  <div className="px-8 pb-8 space-y-8 bg-purple-900/30">
                    {/* Subtopics */}
                    {topicBlock.subtopics ? (
                      topicBlock.subtopics.map((subtopic: TopicSection, subtopicIndex: number) => (
                        <div key={subtopicIndex} className="mt-6">
                          <h4 className="text-xl font-bold text-cyan-300 mb-5 flex items-center gap-3">
                            <span className="w-10 h-10 rounded-xl bg-cyan-400/20 flex items-center justify-center text-cyan-300">
                              {subtopicIndex + 1}
                            </span>
                            {subtopic.title}
                          </h4>
                          <div className="space-y-5 pl-4">
                            {subtopic.lessons.map((lesson, lessonIndex) => {
                              const lessonKey = `${selectedClass}-${selectedSubject.title}-${topicKey}-${subtopicIndex}-${lessonIndex}`
                              const isCompleted = completedLessons.has(lessonKey)
                              const isQuizCompleted = completedQuizzes.has(lesson.title)

                              return (
                                <div key={lessonIndex} 
                                     className={`p-6 rounded-3xl border-4 transition-all
                                       ${isCompleted 
                                         ? 'bg-green-500/20 border-green-400/50' 
                                         : 'bg-white/5 border-white/20 hover:border-purple-400/50'}`}>
                                  <div className="flex items-start gap-4">
                                    {isCompleted ? (
                                      <div className="p-2 rounded-full bg-green-400">
                                        <CheckCircle className="w-6 h-6 text-white" />
                                      </div>
                                    ) : (
                                      <Star className="w-8 h-8 text-yellow-400 flex-shrink-0 mt-1" />
                                    )}
                                    <div className="flex-1">
                                      <h5 className="text-xl font-bold text-purple-200 mb-2">
                                        {lesson.title}
                                      </h5>
                                      <p className="text-base text-gray-400 line-clamp-2 mb-3">
                                        {lesson.description}
                                      </p>
                                      
                                      {/* BIG BUTTONS for kids */}
                                      <div className="flex gap-3 mt-4">
                                        <button
                                          onClick={() => openDetail(lesson)}
                                          className="flex-1 py-4 px-6 bg-gradient-to-r from-blue-500 to-cyan-500
                                                     hover:from-blue-600 hover:to-cyan-600
                                                     text-white rounded-2xl font-bold text-lg
                                                     flex items-center justify-center gap-3
                                                     transition-all hover:scale-105"
                                        >
                                          <FileText className="w-6 h-6" />
                                          Урок 📖
                                        </button>
                                        <button
                                          onClick={() => openQuiz(lesson)}
                                          className={`flex-1 py-4 px-6 rounded-2xl font-bold text-lg
                                                     flex items-center justify-center gap-3
                                                     transition-all hover:scale-105
                                                     ${isQuizCompleted 
                                                       ? 'bg-green-500 text-white'
                                                       : 'bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white'
                                                     }`}
                                        >
                                          <ClipboardList className="w-6 h-6" />
                                          {isQuizCompleted ? '✓ Тест' : 'Тест 🎯'}
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              )
                            })}
                          </div>
                        </div>
                      ))
                    ) : (
                      /* Old structure */
                      topicBlock.lessons?.map((lesson, lessonIndex) => {
                        const lessonKey = `${selectedClass}-${selectedSubject.title}-${topicKey}-${lessonIndex}`
                        const isCompleted = completedLessons.has(lessonKey)
                        const isQuizCompleted = completedQuizzes.has(lesson.title)

                        return (
                          <div key={lessonIndex} 
                               className={`p-6 rounded-3xl border-4 transition-all
                                 ${isCompleted 
                                   ? 'bg-green-500/20 border-green-400/50' 
                                   : 'bg-white/5 border-white/20 hover:border-purple-400/50'}`}>
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
                                <p className="text-base text-gray-400 line-clamp-2 mb-3">
                                  {lesson.description}
                                </p>
                                
                                {/* BIG BUTTONS for kids */}
                                <div className="flex gap-3">
                                  <button
                                    onClick={() => openDetail(lesson)}
                                    className="flex-1 py-4 px-6 bg-gradient-to-r from-blue-500 to-cyan-500
                                               hover:from-blue-600 hover:to-cyan-600
                                               text-white rounded-2xl font-bold text-lg
                                               flex items-center justify-center gap-3
                                               transition-all hover:scale-105"
                                  >
                                    <FileText className="w-6 h-6" />
                                    Урок 📖
                                  </button>
                                  <button
                                    onClick={() => openQuiz(lesson)}
                                    className={`flex-1 py-4 px-6 rounded-2xl font-bold text-lg
                                               flex items-center justify-center gap-3
                                               transition-all hover:scale-105
                                               ${isQuizCompleted 
                                                 ? 'bg-green-500 text-white'
                                                 : 'bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white'
                                               }`}
                                  >
                                    <ClipboardList className="w-6 h-6" />
                                    {isQuizCompleted ? '✓ Тест' : 'Тест 🎯'}
                                  </button>
                                </div>
                              </div>
                            </div>
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
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
          {selectedSubject.games.map((game: GameLesson, index: number) => (
            <button
              key={index}
              onClick={() => selectGame(game)}
              className="p-8 rounded-3xl bg-gradient-to-br from-purple-500/60 to-pink-500/60 
                         border-4 border-white/20 hover:border-yellow-400
                         text-left transition-all hover:scale-[1.02] group relative"
            >
              {/* Star badge */}
              <div className="absolute top-4 right-4 bg-yellow-400 text-purple-900 
                             px-4 py-2 rounded-2xl font-black text-lg flex items-center gap-2">
                <Star className="w-5 h-5 fill-purple-900" />
                {game.reward.stars}
              </div>

              <div className="flex items-center gap-4 mb-4">
                <div className="p-4 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500
                                group-hover:scale-110 transition-transform">
                  <Gamepad2 className="w-10 h-10 text-white" />
                </div>
                <div>
                  <h4 className="text-2xl font-bold text-white">{game.title}</h4>
                  <p className="text-lg text-purple-200">{game.tasks.length} заданий</p>
                </div>
              </div>
              
              <div className="flex items-center gap-3 text-yellow-300 text-xl font-bold">
                <Play className="w-6 h-6" />
                ИГРАТЬ!
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
        onComplete={() => setIsDetailOpen(false)}
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
