'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Users, X, Calendar, BookOpen, BarChart3, Printer, Download } from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'
import { useSessions, OverviewTab, HistoryTab, SubjectsTab } from './parentDashboard'

export default function ParentDashboard() {
  const { totalPoints, totalStars, selectedClass, progress } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [activeTab, setActiveTab] = useState<'overview' | 'history' | 'subjects'>('overview')

  const { sessions, stats } = useSessions()

  return (
    <>
      {/* Open button */}
      {!isOpen && (
        <motion.button
          initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}
          onClick={() => setIsOpen(true)}
          className="fixed left-4 bottom-4 z-40 bg-gradient-to-r from-emerald-500 to-teal-500 p-4 rounded-full shadow-lg shadow-emerald-500/30 border-2 border-white/20 group"
        >
          <Users className="w-6 h-6 text-white" />
          <span className="absolute left-full ml-3 bg-gray-900/90 text-white px-3 py-2 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity">
            Для родителей
          </span>
        </motion.button>
      )}

      {/* Modal */}
      <AnimatePresence>
        {isOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="bg-gradient-to-br from-slate-900 to-slate-800 rounded-3xl max-w-2xl w-full max-h-[85vh] overflow-hidden shadow-2xl border-2 border-white/10 flex flex-col">

            {/* Header */}
            <div className="p-6 border-b border-white/10">
              <div className="flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-emerald-500/30 rounded-xl">
                    <Users className="w-6 h-6 text-emerald-300" />
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-white">Родительская панель</h3>
                    <p className="text-emerald-300 text-sm">
                      {selectedClass !== null ? `${selectedClass} класс` : 'Класс не выбран'}
                    </p>
                  </div>
                </div>
                <button onClick={() => setIsOpen(false)} className="text-white/50 hover:text-white">
                  <X className="w-6 h-6" />
                </button>
              </div>

              {/* Tabs */}
              <div className="flex gap-2 mt-4">
                {[
                  { id: 'overview' as const, label: 'Обзор', icon: BarChart3 },
                  { id: 'history' as const, label: 'История', icon: Calendar },
                  { id: 'subjects' as const, label: 'Предметы', icon: BookOpen }
                ].map(tab => (
                  <button key={tab.id} onClick={() => setActiveTab(tab.id)}
                    className={`flex-1 py-2 px-4 rounded-xl font-medium transition-all flex items-center justify-center gap-2
                      ${activeTab === tab.id ? 'bg-emerald-500 text-white' : 'bg-white/5 text-white/50 hover:bg-white/10'}`}>
                    <tab.icon className="w-4 h-4" />
                    {tab.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Content */}
            <div className="flex-1 overflow-y-auto p-6">
              {activeTab === 'overview' && (
                <OverviewTab stats={stats} sessions={sessions} totalStars={totalStars} totalPoints={totalPoints} achievements={progress.achievements} />
              )}
              {activeTab === 'history' && <HistoryTab sessions={sessions} />}
              {activeTab === 'subjects' && <SubjectsTab stats={stats} />}
            </div>

            {/* Footer */}
            <div className="p-4 border-t border-white/10 flex gap-2">
              <button className="flex-1 py-2 bg-white/5 hover:bg-white/10 text-white rounded-xl transition-colors flex items-center justify-center gap-2">
                <Printer className="w-4 h-4" />
                Печать
              </button>
              <button className="flex-1 py-2 bg-white/5 hover:bg-white/10 text-white rounded-xl transition-colors flex items-center justify-center gap-2">
                <Download className="w-4 h-4" />
                Экспорт
              </button>
            </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}
