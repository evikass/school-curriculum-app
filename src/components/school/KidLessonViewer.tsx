'use client'

import { useSchool } from '@/context/SchoolContext'
import { useState } from 'react'
import { ArrowLeft, Star, CheckCircle, XCircle } from 'lucide-react'

export default function KidLessonViewer() {
  const { selectedSubject, goBack, completeTopic, addPoints } = useSchool()
  const [selectedTopic, setSelectedTopic] = useState<string | null>(null)
  const [showQuiz, setShowQuiz] = useState(false)
  const [quizAnswer, setQuizAnswer] = useState<string | null>(null)
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null)

  if (!selectedSubject) return null

  const topics = selectedSubject.topics || []
  const lessons = selectedSubject.detailedTopics?.flatMap(t => t.lessons || []) || []

  if (showQuiz && selectedTopic) {
    return (
      <div className="w-full animate-bounceIn">
        <button
          onClick={() => { setShowQuiz(false); setQuizAnswer(null); setIsCorrect(null) }}
          className="mb-8 flex items-center gap-3 text-white text-2xl font-bold 
                     bg-white/20 px-8 py-4 rounded-3xl"
        >
          <ArrowLeft className="w-8 h-8" /> Назад
        </button>

        <div className="max-w-xl mx-auto text-center p-8 rounded-3xl bg-white/10 border-4 border-white/20">
          <div className="text-6xl mb-6">❓</div>
          <h2 className="text-3xl font-black text-white mb-8">
            Ты запомнил тему "{selectedTopic}"?
          </h2>

          {isCorrect === null ? (
            <div className="space-y-4">
              <button
                onClick={() => { 
                  setIsCorrect(true); 
                  completeTopic(selectedTopic); 
                  addPoints(10);
                }}
                className="w-full p-6 text-2xl font-bold bg-green-500 hover:bg-green-400 
                           text-white rounded-2xl transition-all"
              >
                ✅ Да, понял!
              </button>
              <button
                onClick={() => setIsCorrect(false)}
                className="w-full p-6 text-2xl font-bold bg-orange-500 hover:bg-orange-400 
                           text-white rounded-2xl transition-all"
              >
                🔄 Ещё разок
              </button>
            </div>
          ) : isCorrect ? (
            <div className="animate-bounceIn">
              <div className="text-8xl mb-6">🎉</div>
              <h3 className="text-2xl font-bold text-white mb-4">Отлично!</h3>
              <p className="text-xl text-purple-200 mb-6">
                Ты заработал <span className="text-yellow-400 font-bold">+10 ⭐</span>
              </p>
              <button
                onClick={() => { setShowQuiz(false); setSelectedTopic(null) }}
                className="px-8 py-4 text-xl font-bold bg-gradient-to-r from-purple-500 to-pink-500 
                           text-white rounded-2xl"
              >
                К другим темам
              </button>
            </div>
          ) : (
            <div className="animate-bounceIn">
              <div className="text-6xl mb-6">💪</div>
              <h3 className="text-2xl font-bold text-white mb-4">Ничего!</h3>
              <p className="text-xl text-purple-200 mb-6">
                Попробуй перечитать и вернись снова!
              </p>
              <button
                onClick={() => { setShowQuiz(false); setSelectedTopic(null) }}
                className="px-8 py-4 text-xl font-bold bg-white/20 text-white rounded-2xl"
              >
                Понятно
              </button>
            </div>
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="w-full animate-slideIn">
      <button
        onClick={goBack}
        className="mb-8 flex items-center gap-3 text-white text-2xl font-bold 
                   bg-white/20 hover:bg-white/30 px-8 py-4 rounded-3xl transition-all"
      >
        <ArrowLeft className="w-8 h-8" /> Назад
      </button>

      <div className="text-center mb-10">
        <div className="text-7xl mb-4">{selectedSubject.icon}</div>
        <h2 className="text-4xl md:text-5xl font-black text-transparent bg-clip-text 
                       bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-4">
          {selectedSubject.title}
        </h2>
        <p className="text-xl text-purple-200">
          {topics.length} тем для изучения! 📚
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {topics.map((topic, index) => {
          const isCompleted = Math.random() > 0.7 // Demo - should use actual progress
          return (
            <button
              key={index}
              onClick={() => { setSelectedTopic(topic); setShowQuiz(true) }}
              className={`group relative overflow-hidden p-8 rounded-3xl
                         ${isCompleted 
                           ? 'bg-gradient-to-br from-green-500/40 to-emerald-500/40 border-4 border-green-400/50'
                           : 'bg-gradient-to-br from-indigo-500/40 to-purple-500/40 border-4 border-white/20 hover:border-yellow-400'
                         }
                         shadow-xl hover:shadow-2xl hover:scale-[1.02]
                         transition-all duration-300 text-left`}
            >
              <div className="flex items-start gap-5">
                <div className={`p-4 rounded-2xl ${isCompleted ? 'bg-green-500' : 'bg-gradient-to-br from-yellow-400 to-orange-500'}
                                shadow-lg group-hover:scale-110 transition-transform`}>
                  <span className="text-4xl">{isCompleted ? '✅' : '📖'}</span>
                </div>
                <div className="flex-1">
                  <h3 className="text-2xl font-black text-white mb-2">{topic}</h3>
                  <div className="flex items-center gap-2">
                    {isCompleted ? (
                      <span className="text-green-300 font-bold">✓ Изучено</span>
                    ) : (
                      <span className="text-purple-300">Нажми, чтобы изучить →</span>
                    )}
                  </div>
                </div>
              </div>
            </button>
          )
        })}
      </div>
    </div>
  )
}
