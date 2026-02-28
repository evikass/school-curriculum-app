'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Calendar, X, Plus, AlertCircle, ChevronLeft, ChevronRight, Sun, Moon, CloudSun, Coffee } from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'
import { AddScheduleForm, ScheduleListItem, ScheduleNotification, useSchedule, subjects, dayNames, dayNamesFull } from './studySchedule'

export default function StudySchedule() {
  const { selectedClass } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [currentDay, setCurrentDay] = useState(new Date().getDay())
  const [showAddForm, setShowAddForm] = useState(false)
  const [newItem, setNewItem] = useState({
    subject: subjects[0].name,
    time: '12:00',
    duration: 30,
    days: [1, 2, 3, 4, 5]
  })

  const { schedule, notification, addItem, removeItem, toggleItemActive, dismissNotification } = useSchedule()

  const todaySchedule = schedule
    .filter(item => item.active && item.days.includes(currentDay))
    .sort((a, b) => a.time.localeCompare(b.time))

  const getTimeOfDay = () => {
    const hour = new Date().getHours()
    if (hour < 12) return { icon: Sun, text: 'Утро', color: 'text-yellow-400' }
    if (hour < 17) return { icon: CloudSun, text: 'День', color: 'text-orange-400' }
    if (hour < 21) return { icon: Coffee, text: 'Вечер', color: 'text-purple-400' }
    return { icon: Moon, text: 'Ночь', color: 'text-blue-400' }
  }

  const addScheduleItem = () => {
    addItem(newItem)
    setShowAddForm(false)
    setNewItem({ subject: subjects[0].name, time: '12:00', duration: 30, days: [1, 2, 3, 4, 5] })
  }

  const timeOfDay = getTimeOfDay()
  const TimeIcon = timeOfDay.icon

  return (
    <>
      {!isOpen && (
        <motion.button
          initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}
          onClick={() => setIsOpen(true)}
          className="fixed right-4 top-1/2 -translate-y-1/2 z-40 bg-gradient-to-r from-blue-500 to-cyan-500 p-4 rounded-full shadow-lg shadow-blue-500/30 border-2 border-white/20 group"
        >
          <Calendar className="w-6 h-6 text-white" />
          <span className="absolute -right-2 -top-2 bg-green-400 text-green-900 text-xs font-bold px-2 py-1 rounded-full">
            {todaySchedule.length}
          </span>
          <span className="absolute right-full mr-3 bg-gray-900/90 text-white px-3 py-2 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity">
            Расписание занятий
          </span>
        </motion.button>
      )}

      <ScheduleNotification show={notification.show} item={notification.item} onClose={dismissNotification} />

      <AnimatePresence>
        {isOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="bg-gradient-to-br from-slate-900 to-slate-800 rounded-3xl p-6 max-w-lg w-full max-h-[80vh] overflow-hidden shadow-2xl border-2 border-white/10 flex flex-col">

            {/* Header */}
            <div className="flex justify-between items-center mb-6">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-blue-500/30 rounded-xl">
                  <Calendar className="w-6 h-6 text-blue-300" />
                </div>
                <div>
                  <h3 className="text-xl font-bold text-white">Расписание</h3>
                  <p className="text-blue-300 text-sm flex items-center gap-2">
                    <TimeIcon className={`w-4 h-4 ${timeOfDay.color}`} />
                    {timeOfDay.text} • {dayNamesFull[currentDay]}
                  </p>
                </div>
              </div>
              <button onClick={() => setIsOpen(false)} className="text-white/50 hover:text-white">
                <X className="w-6 h-6" />
              </button>
            </div>

            {/* Day selector */}
            <div className="flex items-center justify-between mb-4">
              <button onClick={() => setCurrentDay(d => (d - 1 + 7) % 7)} className="p-2 hover:bg-white/10 rounded-lg transition-colors">
                <ChevronLeft className="w-5 h-5 text-white" />
              </button>
              <div className="flex gap-1">
                {dayNames.map((day, idx) => (
                  <button key={idx} onClick={() => setCurrentDay(idx)}
                    className={`w-10 h-10 rounded-xl font-medium transition-all
                      ${currentDay === idx ? 'bg-blue-500 text-white' : 'bg-white/5 text-white/50 hover:bg-white/10'}`}>
                    {day}
                  </button>
                ))}
              </div>
              <button onClick={() => setCurrentDay(d => (d + 1) % 7)} className="p-2 hover:bg-white/10 rounded-lg transition-colors">
                <ChevronRight className="w-5 h-5 text-white" />
              </button>
            </div>

            {/* Schedule list */}
            <div className="flex-1 overflow-y-auto space-y-2 mb-4">
              {todaySchedule.length === 0 ? (
                <div className="text-center py-8">
                  <AlertCircle className="w-12 h-12 text-white/20 mx-auto mb-3" />
                  <p className="text-white/50">Нет занятий на этот день</p>
                  <button onClick={() => setShowAddForm(true)} className="mt-3 text-blue-400 hover:text-blue-300 text-sm">
                    Добавить занятие
                  </button>
                </div>
              ) : (
                todaySchedule.map((item, idx) => (
                  <ScheduleListItem key={item.id} item={item} index={idx} onToggle={toggleItemActive} onRemove={removeItem} />
                ))
              )}
            </div>

            {/* Add form */}
            <AnimatePresence>
              {showAddForm && (
                <AddScheduleForm show={showAddForm} newItem={newItem} setNewItem={setNewItem} onAdd={addScheduleItem} onCancel={() => setShowAddForm(false)} />
              )}
            </AnimatePresence>

            {/* Add button */}
            {!showAddForm && (
              <button onClick={() => setShowAddForm(true)}
                className="w-full py-3 bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600 text-white rounded-xl font-medium transition-all flex items-center justify-center gap-2">
                <Plus className="w-5 h-5" />
                Добавить занятие
              </button>
            )}
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}
