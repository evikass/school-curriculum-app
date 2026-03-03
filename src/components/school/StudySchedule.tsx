'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  Calendar, Clock, Bell, X, Plus, Trash2, BookOpen, 
  CheckCircle, AlertCircle, ChevronLeft, ChevronRight,
  Sun, Moon, CloudSun, Coffee
} from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'

interface ScheduleItem {
  id: string
  subject: string
  time: string
  duration: number // минуты
  days: number[] // 0-6 (вс-сб)
  active: boolean
}

const defaultSchedule: ScheduleItem[] = [
  { id: '1', subject: 'Русский язык', time: '09:00', duration: 30, days: [1, 3, 5], active: true },
  { id: '2', subject: 'Математика', time: '10:00', duration: 30, days: [1, 2, 4], active: true },
  { id: '3', subject: 'Окружающий мир', time: '11:00', duration: 20, days: [2, 4], active: true },
  { id: '4', subject: 'Литература', time: '15:00', duration: 25, days: [1, 3, 5], active: true },
]

const subjects = [
  { name: 'Русский язык', icon: '📖', color: 'bg-red-500' },
  { name: 'Математика', icon: '🔢', color: 'bg-blue-500' },
  { name: 'Литература', icon: '📚', color: 'bg-purple-500' },
  { name: 'Окружающий мир', icon: '🌍', color: 'bg-green-500' },
  { name: 'Иностранный язык', icon: '🌐', color: 'bg-pink-500' },
  { name: 'История', icon: '🏛️', color: 'bg-amber-500' },
  { name: 'Биология', icon: '🔬', color: 'bg-emerald-500' },
  { name: 'География', icon: '🗺️', color: 'bg-teal-500' },
]

const dayNames = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']
const dayNamesFull = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

export default function StudySchedule() {
  const { selectedGrade } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [schedule, setSchedule] = useState<ScheduleItem[]>([])
  const [currentDay, setCurrentDay] = useState(new Date().getDay())
  const [showAddForm, setShowAddForm] = useState(false)
  const [newItem, setNewItem] = useState({
    subject: subjects[0].name,
    time: '12:00',
    duration: 30,
    days: [1, 2, 3, 4, 5]
  })
  const [notification, setNotification] = useState<{ show: boolean; item: ScheduleItem | null }>({
    show: false,
    item: null
  })
  
  // Загрузка расписания
  useEffect(() => {
    const saved = localStorage.getItem('studySchedule')
    if (saved) {
<<<<<<< HEAD
      setSchedule(JSON.parse(saved))
    } else {
=======
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setSchedule(JSON.parse(saved))
    } else {
      // eslint-disable-next-line react-hooks/set-state-in-effect
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
      setSchedule(defaultSchedule)
      localStorage.setItem('studySchedule', JSON.stringify(defaultSchedule))
    }
  }, [])
  
  // Сохранение расписания
  useEffect(() => {
    if (schedule.length > 0) {
      localStorage.setItem('studySchedule', JSON.stringify(schedule))
    }
  }, [schedule])
  
  // Проверка напоминаний
  useEffect(() => {
    const checkNotification = () => {
      const now = new Date()
      const currentTime = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`
      const currentDayOfWeek = now.getDay()
      
      const upcoming = schedule.find(item => 
        item.active && 
        item.days.includes(currentDayOfWeek) &&
        item.time === currentTime
      )
      
      if (upcoming && !notification.show) {
        setNotification({ show: true, item: upcoming })
        // Вибрация на мобильных
        if (navigator.vibrate) {
          navigator.vibrate([200, 100, 200])
        }
      }
    }
    
    const interval = setInterval(checkNotification, 60000) // каждую минуту
    return () => clearInterval(interval)
  }, [schedule, notification.show])
  
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
    const newItemData: ScheduleItem = {
      id: Date.now().toString(),
      subject: newItem.subject,
      time: newItem.time,
      duration: newItem.duration,
      days: newItem.days,
      active: true
    }
    setSchedule([...schedule, newItemData])
    setShowAddForm(false)
    setNewItem({ subject: subjects[0].name, time: '12:00', duration: 30, days: [1, 2, 3, 4, 5] })
  }
  
  const removeItem = (id: string) => {
    setSchedule(schedule.filter(item => item.id !== id))
  }
  
  const toggleItemActive = (id: string) => {
    setSchedule(schedule.map(item => 
      item.id === id ? { ...item, active: !item.active } : item
    ))
  }
  
  const toggleDay = (day: number) => {
    const newDays = newItem.days.includes(day)
      ? newItem.days.filter(d => d !== day)
      : [...newItem.days, day]
    setNewItem({ ...newItem, days: newDays.sort() })
  }
  
  const timeOfDay = getTimeOfDay()
  const TimeIcon = timeOfDay.icon
  
  return (
    <>
      {/* Кнопка открытия */}
      {!isOpen && (
        <motion.button
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={() => setIsOpen(true)}
          className="fixed right-4 top-1/2 -translate-y-1/2 z-40
                     bg-gradient-to-r from-blue-500 to-cyan-500
                     p-4 rounded-full shadow-lg shadow-blue-500/30
                     border-2 border-white/20 group"
        >
          <Calendar className="w-6 h-6 text-white" />
          <span className="absolute -right-2 -top-2 bg-green-400 text-green-900 
                          text-xs font-bold px-2 py-1 rounded-full">
            {todaySchedule.length}
          </span>
          <span className="absolute right-full mr-3 bg-gray-900/90 text-white 
                          px-3 py-2 rounded-lg text-sm whitespace-nowrap
                          opacity-0 group-hover:opacity-100 transition-opacity">
            Расписание занятий
          </span>
        </motion.button>
      )}
      
      {/* Напоминание */}
      <AnimatePresence>
        {notification.show && notification.item && (
          <motion.div
            initial={{ y: -100, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            exit={{ y: -100, opacity: 0 }}
            className="fixed top-4 left-1/2 -translate-x-1/2 z-50
                       bg-gradient-to-r from-green-500 to-emerald-500
                       rounded-2xl p-4 shadow-xl max-w-md w-full mx-4
                       border-2 border-white/20"
          >
            <div className="flex items-center gap-4">
              <div className="p-3 bg-white/20 rounded-xl">
                <Bell className="w-6 h-6 text-white animate-bounce" />
              </div>
              <div className="flex-1">
                <h4 className="text-white font-bold">Пора заниматься!</h4>
                <p className="text-white/80">{notification.item.subject} в {notification.item.time}</p>
              </div>
              <button 
                onClick={() => setNotification({ show: false, item: null })}
                className="p-2 hover:bg-white/10 rounded-lg transition-colors"
              >
                <X className="w-5 h-5 text-white" />
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
      
      {/* Модальное окно */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4
                       bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}
          >
            <motion.div
              initial={{ scale: 0.8, opacity: 0, y: 50 }}
              animate={{ scale: 1, opacity: 1, y: 0 }}
              exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="bg-gradient-to-br from-slate-900 to-slate-800
                         rounded-3xl p-6 max-w-lg w-full max-h-[80vh] overflow-hidden
                         shadow-2xl border-2 border-white/10 flex flex-col"
            >
              {/* Заголовок */}
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
              
              {/* Выбор дня */}
              <div className="flex items-center justify-between mb-4">
                <button 
                  onClick={() => setCurrentDay(d => (d - 1 + 7) % 7)}
                  className="p-2 hover:bg-white/10 rounded-lg transition-colors"
                >
                  <ChevronLeft className="w-5 h-5 text-white" />
                </button>
                <div className="flex gap-1">
                  {dayNames.map((day, idx) => (
                    <button
                      key={idx}
                      onClick={() => setCurrentDay(idx)}
                      className={`w-10 h-10 rounded-xl font-medium transition-all
                                ${currentDay === idx 
                                  ? 'bg-blue-500 text-white' 
                                  : 'bg-white/5 text-white/50 hover:bg-white/10'
                                }`}
                    >
                      {day}
                    </button>
                  ))}
                </div>
                <button 
                  onClick={() => setCurrentDay(d => (d + 1) % 7)}
                  className="p-2 hover:bg-white/10 rounded-lg transition-colors"
                >
                  <ChevronRight className="w-5 h-5 text-white" />
                </button>
              </div>
              
              {/* Список занятий */}
              <div className="flex-1 overflow-y-auto space-y-2 mb-4">
                {todaySchedule.length === 0 ? (
                  <div className="text-center py-8">
                    <AlertCircle className="w-12 h-12 text-white/20 mx-auto mb-3" />
                    <p className="text-white/50">Нет занятий на этот день</p>
                    <button
                      onClick={() => setShowAddForm(true)}
                      className="mt-3 text-blue-400 hover:text-blue-300 text-sm"
                    >
                      Добавить занятие
                    </button>
                  </div>
                ) : (
                  todaySchedule.map((item, idx) => {
                    const subjectInfo = subjects.find(s => s.name === item.subject) || subjects[0]
                    return (
                      <motion.div
                        key={item.id}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: idx * 0.05 }}
                        className={`flex items-center gap-3 p-3 rounded-xl
                                  ${item.active ? 'bg-white/5' : 'bg-white/5 opacity-50'}`}
                      >
                        <span className="text-2xl">{subjectInfo.icon}</span>
                        <div className="flex-1">
                          <p className="text-white font-medium">{item.subject}</p>
                          <p className="text-white/50 text-sm flex items-center gap-2">
                            <Clock className="w-3 h-3" />
                            {item.time} • {item.duration} мин
                          </p>
                        </div>
                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => toggleItemActive(item.id)}
                            className={`p-2 rounded-lg transition-colors
                                      ${item.active 
                                        ? 'bg-green-500/20 text-green-400' 
                                        : 'bg-white/5 text-white/30'}`}
                          >
                            <CheckCircle className="w-4 h-4" />
                          </button>
                          <button
                            onClick={() => removeItem(item.id)}
                            className="p-2 hover:bg-red-500/20 rounded-lg text-white/30 hover:text-red-400 transition-colors"
                          >
                            <Trash2 className="w-4 h-4" />
                          </button>
                        </div>
                      </motion.div>
                    )
                  })
                )}
              </div>
              
              {/* Форма добавления */}
              <AnimatePresence>
                {showAddForm && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    className="border-t border-white/10 pt-4 overflow-hidden"
                  >
                    <div className="space-y-3">
                      <select
                        value={newItem.subject}
                        onChange={(e) => setNewItem({ ...newItem, subject: e.target.value })}
                        className="w-full bg-white/10 text-white rounded-xl p-3 border border-white/10"
                      >
                        {subjects.map(s => (
                          <option key={s.name} value={s.name} className="bg-slate-800">
                            {s.icon} {s.name}
                          </option>
                        ))}
                      </select>
                      
                      <div className="flex gap-2">
                        <input
                          type="time"
                          value={newItem.time}
                          onChange={(e) => setNewItem({ ...newItem, time: e.target.value })}
                          className="flex-1 bg-white/10 text-white rounded-xl p-3 border border-white/10"
                        />
                        <input
                          type="number"
                          value={newItem.duration}
                          onChange={(e) => setNewItem({ ...newItem, duration: parseInt(e.target.value) || 30 })}
                          min={10}
                          max={120}
                          className="w-24 bg-white/10 text-white rounded-xl p-3 border border-white/10"
                        />
                        <span className="flex items-center text-white/50 text-sm">мин</span>
                      </div>
                      
                      <div className="flex gap-1">
                        {dayNames.map((day, idx) => (
                          <button
                            key={idx}
                            onClick={() => toggleDay(idx)}
                            className={`flex-1 py-2 rounded-lg text-sm font-medium transition-all
                                      ${newItem.days.includes(idx)
                                        ? 'bg-blue-500 text-white'
                                        : 'bg-white/5 text-white/50 hover:bg-white/10'
                                      }`}
                          >
                            {day}
                          </button>
                        ))}
                      </div>
                      
                      <div className="flex gap-2">
                        <button
                          onClick={() => setShowAddForm(false)}
                          className="flex-1 py-3 bg-white/5 hover:bg-white/10 text-white rounded-xl transition-colors"
                        >
                          Отмена
                        </button>
                        <button
                          onClick={addScheduleItem}
                          className="flex-1 py-3 bg-blue-500 hover:bg-blue-600 text-white rounded-xl transition-colors flex items-center justify-center gap-2"
                        >
                          <Plus className="w-4 h-4" />
                          Добавить
                        </button>
                      </div>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
              
              {/* Кнопка добавления */}
              {!showAddForm && (
                <button
                  onClick={() => setShowAddForm(true)}
                  className="w-full py-3 bg-gradient-to-r from-blue-500 to-cyan-500
                            hover:from-blue-600 hover:to-cyan-600
                            text-white rounded-xl font-medium transition-all
                            flex items-center justify-center gap-2"
                >
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
