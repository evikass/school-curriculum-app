'use client'

import { SchoolProvider, useSchool } from '@/context/SchoolContext'
import { 
  GradeSelector, SubjectGrid, LessonViewer, 
  GameSection, Gameplay,
  KidGameSection, KidGameplay, KidSubjectGrid, KidLessonViewer,
  SideButtons
} from '@/components/school'
import { School } from 'lucide-react'

function AppContent() {
  const { view, isKidMode } = useSchool()

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 p-4 md:p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <header className="text-center mb-8">
          <h1 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text 
                         bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 
                         flex items-center justify-center gap-4 mb-2">
            <School className="w-12 h-12 text-purple-300" />
            ИНЕТШКОЛА
          </h1>
          <p className="text-xl text-purple-200">
            Интерактивная школьная программа
          </p>
        </header>

        {/* Main content */}
        <main>
          {view === 'classes' && <GradeSelector />}
          {view === 'subjects' && (isKidMode ? <KidSubjectGrid /> : <SubjectGrid />)}
          {view === 'lessons' && (isKidMode ? <KidLessonViewer /> : <LessonViewer />)}
          {view === 'games' && (isKidMode ? <KidGameSection /> : <GameSection />)}
          {view === 'gameplay' && (isKidMode ? <KidGameplay /> : <Gameplay />)}
        </main>

        {/* Footer */}
        <footer className="text-center mt-12 text-purple-300/50 text-sm">
          ИНЕТШКОЛА © 2025 • Сделано с любовью для учеников
          <span className="ml-2 text-xs opacity-50">v2.1-2025-01-16</span>
        </footer>
      </div>

      {/* Side Buttons - Мультимодальные кнопки по бокам */}
      <SideButtons />
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
