'use client'

import { SchoolProvider, useSchool } from '@/context/SchoolContext'
import { GradeSelector, SubjectGrid, LessonViewer, KidSubjectGrid, KidLessonViewer } from '@/components/school'

function AppContent() {
  const { view, isKidMode, selectedClass, games } = useSchool()

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 p-4 md:p-8">
      <div className="max-w-7xl mx-auto">
        <header className="text-center mb-8">
          <h1 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text
                         bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-2">
            ИНЕТШКОЛА
          </h1>
          <p className="text-xl text-purple-200">Интерактивная школьная программа</p>
          <p className="text-green-400 text-xs mt-2">v2.17-nogames</p>
        </header>

        <main>
          {view === 'classes' && <GradeSelector />}
          {view === 'subjects' && (isKidMode ? <KidSubjectGrid /> : <SubjectGrid />)}
          {view === 'lessons' && (isKidMode ? <KidLessonViewer /> : <LessonViewer />)}
          {view === 'games' && (
            <div className="text-center text-white p-8">
              <h2 className="text-3xl font-bold mb-4">Игры и викторины</h2>
              <p className="text-purple-200">Класс: {selectedClass} | Игр: {games?.length || 0}</p>
              <p className="text-yellow-300 mt-4">Секция игр временно недоступна</p>
            </div>
          )}
          {view === 'gameplay' && (
            <div className="text-center text-white p-8">
              <p>Gameplay view</p>
            </div>
          )}
        </main>
      </div>
    </div>
  )
}

export default function Home() {
  return (
    <SchoolProvider>
      <AppContent />
    </SchoolProvider>
  )
}
