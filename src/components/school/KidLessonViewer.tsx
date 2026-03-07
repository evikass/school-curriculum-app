'use client'

import { useSchool, LessonData } from '@/context/SchoolContext'
import { useState } from 'react'
import { ArrowLeft, Star, BookOpen, ChevronDown, ChevronRight, Gamepad2, Play, Sparkles } from 'lucide-react'
import { generateLessonQuiz } from '@/lib/lessonQuizGenerator'
import LessonContentRenderer from './LessonContentRenderer'

interface Lesson {
  title: string
  description: string
  tasks: string[]
}

interface TopicSection {
  topic: string
  lessons: Lesson[]
}

export default function KidLessonViewer() {
  const { selectedSubject, goBack, completeTopic, addPoints, selectGame, selectGameFromLesson, games: contextGames, selectedLesson, selectLesson } = useSchool()
  const [selectedTopicIndex, setSelectedTopicIndex] = useState<number | null>(null)
  const [showGames, setShowGames] = useState(false)
  const [completedLessons, setCompletedLessons] = useState<Set<string>>(new Set())

  if (!selectedSubject) return null

  const topics = selectedSubject.detailedTopics || []
  const games = contextGames || []

  // Если выбран урок - показываем его содержимое
  if (selectedLesson) {
    return (
      <div className="w-full animate-slideIn">
        <button
          onClick={() => selectLesson(null)}
          className="mb-6 flex items-center gap-3 text-white text-xl font-bold 
                     bg-white/20 hover:bg-white/30 px-6 py-3 rounded-2xl transition-all
                     hover:scale-105 active:scale-95 border border-white/20"
        >
          <ArrowLeft className="w-6 h-6" /> 
          <span>Назад к урокам</span>
        </button>

        <div className="max-w-3xl mx-auto">
          {/* Красивый заголовок урока */}
          <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-purple-600/40 via-pink-600/30 to-blue-600/40 
                          border-2 border-white/20 p-6 md:p-8 shadow-2xl">
            {/* Декоративные элементы */}
            <div className="absolute top-0 right-0 w-40 h-40 bg-yellow-400/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
            <div className="absolute bottom-0 left-0 w-32 h-32 bg-purple-400/10 rounded-full blur-2xl translate-y-1/2 -translate-x-1/2"></div>
            
            <div className="relative z-10">
              {/* Иконка предмета */}
              <div className="flex items-center gap-4 mb-4">
                <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 
                                flex items-center justify-center text-3xl shadow-lg">
                  📖
                </div>
                <div>
                  <h2 className="text-2xl md:text-3xl font-black text-white">
                    {selectedLesson.title}
                  </h2>
                  <p className="text-purple-200 text-sm">{selectedSubject.title}</p>
                </div>
              </div>
              
              {/* Содержимое урока с новым форматированием */}
              <div className="mt-6">
                <LessonContentRenderer content={selectedLesson.description} />
              </div>

              {/* Задания */}
              {selectedLesson.tasks && selectedLesson.tasks.length > 0 && (
                <div className="mt-8 p-5 bg-gradient-to-r from-indigo-500/20 to-purple-500/20 rounded-2xl border-2 border-indigo-400/30">
                  <h4 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-emerald-400 to-teal-500 flex items-center justify-center">
                      <BookOpen className="w-5 h-5 text-white" />
                    </div>
                    <span className="text-emerald-300">Задания для закрепления:</span>
                  </h4>
                  <div className="space-y-2">
                    {selectedLesson.tasks.map((task, i) => (
                      <div key={i} className="flex items-start gap-3 p-3 bg-white/5 rounded-xl border border-white/10 hover:bg-white/10 transition-all">
                        <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-blue-400 to-cyan-500 flex items-center justify-center text-white text-xs font-bold flex-shrink-0 mt-0.5">
                          {i + 1}
                        </div>
                        <span className="text-white/90 text-base">{task}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Кнопки действий */}
              <div className="mt-8 flex flex-wrap gap-3 justify-center">
                <button
                  onClick={() => {
                    const subjectGames = games.filter(g =>
                      g.subject === selectedSubject.title ||
                      selectedSubject.title.toLowerCase().includes(g.subject.toLowerCase()) ||
                      g.subject.toLowerCase().includes(selectedSubject.title.toLowerCase())
                    )

                    if (subjectGames.length > 0) {
                      const randomGame = subjectGames[Math.floor(Math.random() * subjectGames.length)]
                      selectGameFromLesson(randomGame)
                    } else {
                      const generatedGame = generateLessonQuiz(
                        selectedLesson.title,
                        selectedLesson.description,
                        selectedSubject.title
                      )
                      if (generatedGame) {
                        selectGameFromLesson(generatedGame)
                      } else if (games.length > 0) {
                        const randomGame = games[Math.floor(Math.random() * games.length)]
                        selectGameFromLesson(randomGame)
                      }
                    }
                  }}
                  className="px-6 py-3 text-lg font-bold bg-gradient-to-r from-purple-500 to-pink-500 
                             hover:from-purple-400 hover:to-pink-400
                             text-white rounded-2xl transition-all hover:scale-105 active:scale-95 
                             flex items-center gap-2 shadow-lg border border-white/20"
                >
                  <Gamepad2 className="w-5 h-5" />
                  <span>🎮 Тест-игра</span>
                </button>
                
                <button
                  onClick={() => {
                    setCompletedLessons(new Set([...completedLessons, selectedLesson.title]))
                    completeTopic(selectedLesson.title)
                    addPoints(5)
                    selectLesson(null)
                  }}
                  className="px-6 py-3 text-lg font-bold bg-gradient-to-r from-green-500 to-emerald-500 
                             hover:from-green-400 hover:to-emerald-400
                             text-white rounded-2xl transition-all hover:scale-105 active:scale-95 
                             flex items-center gap-2 shadow-lg border border-white/20"
                >
                  <Star className="w-5 h-5" />
                  <span>✅ Понял! +5 ⭐</span>
                </button>
                
                <button
                  onClick={() => selectLesson(null)}
                  className="px-6 py-3 text-lg font-bold bg-white/20 hover:bg-white/30 
                             text-white rounded-2xl transition-all hover:scale-105 active:scale-95 
                             flex items-center gap-2 border border-white/10"
                >
                  <BookOpen className="w-5 h-5" />
                  <span>📚 Другие уроки</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  // Если показываем игры
  if (showGames) {
    return (
      <div className="w-full animate-slideIn">
        <button
          onClick={() => setShowGames(false)}
          className="mb-8 flex items-center gap-3 text-white text-xl font-bold 
                     bg-white/20 hover:bg-white/30 px-6 py-3 rounded-2xl transition-all"
        >
          <ArrowLeft className="w-6 h-6" /> Назад к урокам
        </button>

        <div className="text-center mb-8">
          <div className="text-6xl mb-4">🎮</div>
          <h2 className="text-3xl font-black text-white">Игры и задания</h2>
          <p className="text-purple-200 mt-2">{games.length} игр для закрепления!</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-4xl mx-auto">
          {games.map((game, index) => (
            <button
              key={index}
              onClick={() => selectGame(game)}
              className="p-5 rounded-2xl bg-gradient-to-br from-purple-600/50 to-pink-600/50 
                         border-2 border-white/20 hover:border-yellow-400
                         text-left transition-all hover:scale-[1.02] group shadow-xl"
            >
              <div className="flex items-center gap-4 mb-3">
                <div className="p-3 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 shadow-lg">
                  <Gamepad2 className="w-7 h-7 text-white" />
                </div>
                <div>
                  <h4 className="text-lg font-bold text-white">{game.title}</h4>
                  <p className="text-purple-200 text-sm">{game.tasks.length} заданий</p>
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
      </div>
    )
  }

  // Основной вид - список тем и уроков
  return (
    <div className="w-full animate-slideIn">
      <button
        onClick={goBack}
        className="mb-8 flex items-center gap-3 text-white text-xl font-bold 
                   bg-white/20 hover:bg-white/30 px-6 py-3 rounded-2xl transition-all"
      >
        <ArrowLeft className="w-6 h-6" /> Назад
      </button>

      <div className="text-center mb-10">
        <div className="relative inline-block">
          <div className="absolute inset-0 blur-xl bg-gradient-to-r from-yellow-400/30 to-pink-400/30 rounded-full scale-150"></div>
          <div className="relative text-7xl mb-4">{selectedSubject.icon}</div>
        </div>
        <h2 className="text-3xl md:text-4xl font-black text-transparent bg-clip-text 
                   bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-4">
          {selectedSubject.title}
        </h2>
        <p className="text-lg text-purple-200">
          {topics.reduce((acc, t) => acc + (t.lessons?.length || 0), 0)} уроков для изучения! 📚
        </p>
      </div>

      {/* Кнопка игр */}
      {games.length > 0 && (
        <div className="text-center mb-6">
          <button
            onClick={() => setShowGames(true)}
            className="px-8 py-4 text-xl font-bold bg-gradient-to-r from-green-500 to-teal-500 
                       hover:from-green-400 hover:to-teal-400
                       text-white rounded-2xl transition-all hover:scale-105 active:scale-95 
                       flex items-center gap-3 mx-auto shadow-xl border border-white/20"
          >
            <Gamepad2 className="w-6 h-6" />
            <span>🎮 Игры ({games.length})</span>
          </button>
        </div>
      )}

      <div className="space-y-4 max-w-4xl mx-auto">
        {topics.map((topicBlock: TopicSection, topicIndex: number) => {
          const isExpanded = selectedTopicIndex === topicIndex
          const lessonsCount = topicBlock.lessons?.length || 0
          const completedCount = topicBlock.lessons?.filter(l => completedLessons.has(l.title)).length || 0

          return (
            <div key={topicIndex} 
                 className="rounded-2xl overflow-hidden bg-gradient-to-br from-indigo-500/30 to-purple-500/30 
                            border-2 border-white/20 shadow-xl">
              {/* Topic header */}
              <button
                onClick={() => setSelectedTopicIndex(isExpanded ? null : topicIndex)}
                className="w-full px-5 py-4 flex items-center justify-between text-left
                           hover:bg-white/5 transition-colors"
              >
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-yellow-400 to-orange-500 
                                  flex items-center justify-center text-white font-black text-xl shadow-lg">
                    {topicIndex + 1}
                  </div>
                  <div>
                    <span className="text-lg md:text-xl font-bold text-white">{topicBlock.topic}</span>
                    <div className="text-sm text-purple-300">
                      {completedCount > 0 ? (
                        <span className="text-green-400">✓ {completedCount}/{lessonsCount} пройдено</span>
                      ) : (
                        <span>{lessonsCount} уроков</span>
                      )}
                    </div>
                  </div>
                </div>
                {isExpanded ? (
                  <ChevronDown className="w-6 h-6 text-yellow-400" />
                ) : (
                  <ChevronRight className="w-6 h-6 text-yellow-400" />
                )}
              </button>

              {/* Expanded lessons */}
              {isExpanded && topicBlock.lessons && (
                <div className="px-5 pb-5 space-y-2 bg-gray-900/30">
                  {topicBlock.lessons.map((lesson, lessonIndex) => {
                    const isCompleted = completedLessons.has(lesson.title)
                    
                    return (
                      <button
                        key={lessonIndex}
                        onClick={() => selectLesson(lesson)}
                        className={`w-full p-4 rounded-xl text-left transition-all hover:scale-[1.01]
                                   ${isCompleted 
                                     ? 'bg-gradient-to-r from-green-500/30 to-emerald-500/30 border-2 border-green-400/50'
                                     : 'bg-white/10 border-2 border-white/10 hover:border-yellow-400/50'
                                   }`}
                      >
                        <div className="flex items-center gap-3">
                          <div className={`w-10 h-10 rounded-xl flex items-center justify-center text-xl
                                          ${isCompleted ? 'bg-green-500' : 'bg-gradient-to-br from-purple-400 to-pink-400'} shadow-lg`}>
                            {isCompleted ? '✅' : '📖'}
                          </div>
                          <div className="flex-1 min-w-0">
                            <h4 className="text-base font-bold text-white truncate">{lesson.title}</h4>
                            <p className="text-xs text-purple-300 truncate">
                              {lesson.description.substring(0, 60)}...
                            </p>
                          </div>
                          <div className="flex items-center gap-2 text-yellow-400 font-bold flex-shrink-0">
                            <Star className="w-5 h-5 fill-yellow-400" />
                            <span className="text-sm">+10</span>
                          </div>
                        </div>
                      </button>
                    )
                  })}
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
