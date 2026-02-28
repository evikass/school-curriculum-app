'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { LessonTopic, TopicSection, GameLesson } from '@/data/types'
import { ArrowLeft, ChevronDown, ChevronRight, BookOpen } from 'lucide-react'
import LessonDetailModal from './LessonDetailModal'
import LessonQuiz from './LessonQuiz'
import { SelectedLesson, LessonCard, GameCard } from './kidLessonViewer'

export default function KidLessonViewer() {
  const { selectedSubject, selectedClass, completeTopic, goBack, selectGame } = useSchool()
  const [expandedTopic, setExpandedTopic] = useState<string | null>(null)
  const [currentTab, setCurrentTab] = useState<'lessons' | 'games'>('lessons')
  const [completedLessons, setCompletedLessons] = useState<Set<string>>(new Set())
  const [completedQuizzes, setCompletedQuizzes] = useState<Set<string>>(new Set())
  const [detailLesson, setDetailLesson] = useState<SelectedLesson | null>(null)
  const [isDetailOpen, setIsDetailOpen] = useState(false)
  const [quizLesson, setQuizLesson] = useState<SelectedLesson | null>(null)
  const [isQuizOpen, setIsQuizOpen] = useState(false)

  if (!selectedSubject) return null

  const toggleTopic = (topicName: string) => {
    // Если тема уже открыта - закрываем, иначе открываем новую (и закрываем предыдущую)
    setExpandedTopic(expandedTopic === topicName ? null : topicName)
  }

  const handleCompleteLesson = (lessonKey: string) => {
    if (!completedLessons.has(lessonKey)) {
      setCompletedLessons(new Set([...completedLessons, lessonKey]))
      completeTopic(lessonKey)
    }
  }

  const openDetail = (lesson: SelectedLesson) => { setDetailLesson(lesson); setIsDetailOpen(true) }
  const openQuiz = (lesson: SelectedLesson) => { setQuizLesson(lesson); setIsQuizOpen(true) }
  const handleQuizComplete = () => { if (quizLesson) setCompletedQuizzes(new Set([...completedQuizzes, quizLesson.title])) }

  const getGradeEmoji = () => selectedClass === 0 ? '🎒' : selectedClass === 1 ? '🌟' : '🦋'

  return (
    <div className="w-full animate-bounceIn">
      {/* Back button */}
      <button onClick={goBack} className="mb-8 flex items-center gap-3 text-white text-2xl font-bold bg-white/20 hover:bg-white/30 px-8 py-4 rounded-3xl transition-all border-4 border-white/30 hover:border-white/50">
        <ArrowLeft className="w-8 h-8" />Назад
      </button>

      {/* Title */}
      <div className="flex items-center gap-5 mb-8">
        <div className="p-5 rounded-3xl bg-gradient-to-br from-yellow-400 to-orange-500">
          <BookOpen className="w-12 h-12 text-white" />
        </div>
        <div>
          <h2 className="text-3xl md:text-5xl font-black text-white">{selectedSubject.title}</h2>
          <p className="text-xl text-purple-200 mt-1">{getGradeEmoji()} Уроки и игры</p>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-4 mb-8 overflow-x-auto pb-2">
        <button onClick={() => setCurrentTab('lessons')}
          className={`px-8 py-5 rounded-3xl font-black text-2xl transition-all whitespace-nowrap flex items-center gap-3
            ${currentTab === 'lessons' ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg scale-105' : 'bg-white/20 text-white hover:bg-white/30'}`}>
          📘 Уроки
        </button>
        {selectedSubject.games && selectedSubject.games.length > 0 && (
          <button onClick={() => setCurrentTab('games')}
            className={`px-8 py-5 rounded-3xl font-black text-2xl transition-all whitespace-nowrap flex items-center gap-3
              ${currentTab === 'games' ? 'bg-gradient-to-r from-green-500 to-teal-500 text-white shadow-lg scale-105' : 'bg-white/20 text-white hover:bg-white/30'}`}>
            🎮 Игры ({selectedSubject.games.length})
          </button>
        )}
      </div>

      {/* Lessons content */}
      {currentTab === 'lessons' && selectedSubject.detailedTopics && (
        <div className="space-y-6">
          <div className="flex items-start gap-4 p-6 rounded-3xl bg-gradient-to-r from-yellow-400/20 to-orange-400/20 border-4 border-yellow-400/30 mb-6">
            <div className="text-5xl animate-wiggle">🦉</div>
            <div>
              <p className="text-xl text-white font-bold mb-2">Мудрая Сова</p>
              <p className="text-lg text-purple-200">Нажми на урок, чтобы начать! Внутри ты найдёшь теорию и тест. 📚✨</p>
            </div>
          </div>

          {selectedSubject.detailedTopics.map((topicBlock: LessonTopic, topicIndex: number) => (
            <TopicBlock key={topicIndex} topicBlock={topicBlock} topicIndex={topicIndex} selectedClass={selectedClass} subjectTitle={selectedSubject.title}
              expandedTopic={expandedTopic} completedLessons={completedLessons} completedQuizzes={completedQuizzes}
              onToggleTopic={toggleTopic} onOpenDetail={openDetail} />
          ))}
        </div>
      )}

      {/* Games content */}
      {currentTab === 'games' && selectedSubject.games && (
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
          {selectedSubject.games.map((game: GameLesson, index: number) => (
            <GameCard key={index} game={game} onSelect={selectGame} />
          ))}
        </div>
      )}

      {/* Modals */}
      <LessonDetailModal 
        lesson={detailLesson} 
        isOpen={isDetailOpen} 
        onClose={() => setIsDetailOpen(false)} 
        onComplete={() => handleCompleteLesson(`${selectedClass}-${selectedSubject.title}-${detailLesson?.title}`)} 
        onStartQuiz={() => { 
          setQuizLesson(detailLesson)
          setIsDetailOpen(false)
          setIsQuizOpen(true)
        }}
      />
      <LessonQuiz lessonTitle={quizLesson?.title || ''} lessonDescription={quizLesson?.description || ''} isOpen={isQuizOpen} onClose={() => setIsQuizOpen(false)} onComplete={handleQuizComplete} />
    </div>
  )
}

function TopicBlock({ topicBlock, topicIndex, selectedClass, subjectTitle, expandedTopic, completedLessons, completedQuizzes, onToggleTopic, onOpenDetail }: {
  topicBlock: LessonTopic
  topicIndex: number
  selectedClass: number | null
  subjectTitle: string
  expandedTopic: string | null
  completedLessons: Set<string>
  completedQuizzes: Set<string>
  onToggleTopic: (name: string) => void
  onOpenDetail: (lesson: SelectedLesson) => void
}) {
  const topicKey = topicBlock.topic
  const isExpanded = expandedTopic === topicKey
  const totalLessons = topicBlock.subtopics ? topicBlock.subtopics.reduce((acc, st) => acc + st.lessons.length, 0) : (topicBlock.lessons?.length || 0)

  return (
    <div className="rounded-3xl overflow-hidden bg-gradient-to-br from-indigo-600/40 to-purple-600/40 border-4 border-white/20">
      <button onClick={() => onToggleTopic(topicKey)} className="w-full px-8 py-6 flex items-center justify-between text-left hover:bg-white/10 transition-colors">
        <div className="flex items-center gap-5">
          <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-cyan-400 to-blue-500 flex items-center justify-center text-white font-black text-2xl shadow-lg">
            {topicIndex + 1}
          </div>
          <div>
            <span className="text-2xl md:text-3xl font-bold text-white">{topicBlock.topic}</span>
            <div className="text-lg text-purple-200 mt-1">{totalLessons} уроков</div>
          </div>
        </div>
        {isExpanded ? <ChevronDown className="w-8 h-8 text-purple-300" /> : <ChevronRight className="w-8 h-8 text-purple-300" />}
      </button>

      {isExpanded && (
        <div className="px-8 pb-8 space-y-8 bg-purple-900/30">
          {topicBlock.subtopics ? topicBlock.subtopics.map((subtopic: TopicSection, subtopicIndex: number) => (
            <div key={subtopicIndex} className="mt-6">
              <h4 className="text-xl font-bold text-cyan-300 mb-5 flex items-center gap-3">
                <span className="w-10 h-10 rounded-xl bg-cyan-400/20 flex items-center justify-center text-cyan-300">{subtopicIndex + 1}</span>
                {subtopic.title}
              </h4>
              <div className="space-y-5 pl-4">
                {subtopic.lessons.map((lesson, lessonIndex) => {
                  const lessonKey = `${selectedClass}-${subjectTitle}-${topicKey}-${subtopicIndex}-${lessonIndex}`
                  return <LessonCard key={lessonIndex} lesson={lesson} lessonKey={lessonKey} isCompleted={completedLessons.has(lessonKey)} isQuizCompleted={completedQuizzes.has(lesson.title)} onOpenDetail={onOpenDetail} />
                })}
              </div>
            </div>
          )) : topicBlock.lessons?.map((lesson, lessonIndex) => {
            const lessonKey = `${selectedClass}-${subjectTitle}-${topicKey}-${lessonIndex}`
            return <LessonCard key={lessonIndex} lesson={lesson} lessonKey={lessonKey} isCompleted={completedLessons.has(lessonKey)} isQuizCompleted={completedQuizzes.has(lesson.title)} onOpenDetail={onOpenDetail} />
          })}
        </div>
      )}
    </div>
  )
}
