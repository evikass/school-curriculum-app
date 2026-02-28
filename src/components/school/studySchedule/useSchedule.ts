'use client'

import { useState, useEffect, useCallback } from 'react'
import { ScheduleItem } from './types'
import { defaultSchedule } from './constants'

export function useSchedule() {
  const [schedule, setSchedule] = useState<ScheduleItem[]>(() => {
    if (typeof window === 'undefined') return []
    const saved = localStorage.getItem('studySchedule')
    if (saved) return JSON.parse(saved)
    localStorage.setItem('studySchedule', JSON.stringify(defaultSchedule))
    return defaultSchedule
  })
  const [notification, setNotification] = useState<{ show: boolean; item: ScheduleItem | null }>({
    show: false,
    item: null
  })

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
        if (navigator.vibrate) {
          navigator.vibrate([200, 100, 200])
        }
      }
    }

    const interval = setInterval(checkNotification, 60000)
    return () => clearInterval(interval)
  }, [schedule, notification.show])

  const addItem = useCallback((item: Omit<ScheduleItem, 'id' | 'active'>) => {
    const newItem: ScheduleItem = {
      id: Date.now().toString(),
      ...item,
      active: true
    }
    setSchedule(prev => [...prev, newItem])
  }, [])

  const removeItem = useCallback((id: string) => {
    setSchedule(prev => prev.filter(item => item.id !== id))
  }, [])

  const toggleItemActive = useCallback((id: string) => {
    setSchedule(prev => prev.map(item =>
      item.id === id ? { ...item, active: !item.active } : item
    ))
  }, [])

  const dismissNotification = useCallback(() => {
    setNotification({ show: false, item: null })
  }, [])

  return {
    schedule,
    notification,
    addItem,
    removeItem,
    toggleItemActive,
    dismissNotification
  }
}
