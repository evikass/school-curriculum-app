'use client'

import { useState, useEffect } from 'react'
import { X } from 'lucide-react'

const tips = [
  { emoji: '🦉', message: 'Мудрая Сова говорит: Читай внимательно задание! 📖' },
  { emoji: '🐱', message: 'Кот Учёный подсказывает: Не торопись, думай! 🤔' },
  { emoji: '🦊', message: 'Лиса советует: Если сложно - посмотри подсказку! 💡' },
  { emoji: '🐼', message: 'Панда напоминает: Делай перерывы! 🌿' },
  { emoji: '🦄', message: 'Единорог верит в тебя! Ты справишься! ✨' },
  { emoji: '🐸', message: 'Лягушка-путешественница: Каждый урок - приключение! 🗺️' },
]

export default function MascotHelper() {
  const [isVisible, setIsVisible] = useState(false)
  const [isDismissed, setIsDismissed] = useState(false)
  const [currentTip, setCurrentTip] = useState(tips[0])

  useEffect(() => {
    // Load dismissed state and pick a random tip only on client
    const dismissed = localStorage.getItem('mascotDismissed') === 'true'
    if (dismissed) {
      setIsDismissed(true)
      return
    }
    setCurrentTip(tips[Math.floor(Math.random() * tips.length)])
  }, [])

  useEffect(() => {
    if (isDismissed) return

    const timer = setTimeout(() => {
      setIsVisible(true)
    }, 30000)

    return () => clearTimeout(timer)
  }, [isDismissed])

  const handleDismiss = () => {
    setIsVisible(false)
    setIsDismissed(true)
    localStorage.setItem('mascotDismissed', 'true')
  }

  if (!isVisible) return null

  return (
    <div className="fixed bottom-72 left-6 z-30 animate-bounceIn">
      <div className="relative max-w-xs bg-white/95 rounded-3xl p-4 shadow-2xl 
                      border-2 border-purple-300 overflow-hidden">
        {/* Close button */}
        <button
          onClick={handleDismiss}
          className="absolute top-2 right-2 p-1.5 rounded-full bg-purple-100 
                     hover:bg-purple-200 transition-colors"
        >
          <X className="w-4 h-4 text-purple-600" />
        </button>

        {/* Content */}
        <div className="flex items-start gap-3">
          {/* Mascot */}
          <div className="flex-shrink-0 text-4xl animate-wiggle">
            {currentTip.emoji}
          </div>
          
          {/* Message */}
          <div className="pt-1">
            <p className="text-gray-700 text-sm leading-relaxed">
              {currentTip.message}
            </p>
          </div>
        </div>

        {/* Button */}
        <button
          onClick={handleDismiss}
          className="mt-3 w-full py-2 bg-purple-100 hover:bg-purple-200 
                     rounded-xl text-purple-700 text-sm font-medium transition-colors"
        >
          Понятно! 👍
        </button>
      </div>
    </div>
  )
}

// Floating mascot button when dismissed
export function MascotButton() {
  const [showTip, setShowTip] = useState(false)
  const [currentTip, setCurrentTip] = useState(tips[0])

  const handleShowTip = () => {
    const randomTip = tips[Math.floor(Math.random() * tips.length)]
    setCurrentTip(randomTip)
    setShowTip(!showTip)
  }

  return (
    <div className="fixed bottom-80 left-6 z-30">
      <button
        onClick={handleShowTip}
        className="w-14 h-14 rounded-full bg-gradient-to-br from-amber-400 to-orange-500
                   shadow-lg hover:scale-110 transition-transform animate-float
                   flex items-center justify-center text-3xl border-2 border-white/50"
      >
        🦉
      </button>

      {showTip && (
        <div className="absolute bottom-16 left-0 max-w-xs bg-white/95 rounded-2xl p-4 
                       shadow-2xl border-2 border-purple-200 animate-bounceIn">
          <div className="flex items-center gap-3">
            <span className="text-3xl">{currentTip.emoji}</span>
            <p className="text-gray-700 text-sm">{currentTip.message}</p>
          </div>
          <button
            onClick={() => setShowTip(false)}
            className="mt-2 w-full py-2 bg-purple-100 hover:bg-purple-200 
                       rounded-xl text-purple-700 text-sm font-medium transition-colors"
          >
            Спасибо! 😊
          </button>
        </div>
      )}
    </div>
  )
}
