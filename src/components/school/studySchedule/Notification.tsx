'use client'

import { motion, AnimatePresence } from 'framer-motion'
import { Bell, X } from 'lucide-react'
import { ScheduleItem } from './types'

interface ScheduleNotificationProps {
  show: boolean
  item: ScheduleItem | null
  onClose: () => void
}

export function ScheduleNotification({ show, item, onClose }: ScheduleNotificationProps) {
  return (
    <AnimatePresence>
      {show && item && (
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
              <p className="text-white/80">{item.subject} в {item.time}</p>
            </div>
            <button
              onClick={onClose}
              className="p-2 hover:bg-white/10 rounded-lg transition-colors"
            >
              <X className="w-5 h-5 text-white" />
            </button>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
