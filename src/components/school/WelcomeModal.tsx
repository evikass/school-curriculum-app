'use client'

import { useState, useEffect } from 'react'
import { School, BookOpen, Gamepad2, Trophy, ChevronRight, X, Volume2, VolumeX, Sparkles, Star, Zap } from 'lucide-react'
import { useSound } from '@/lib/sounds'

interface WelcomeSlide {
  title: string
  description: string
  icon: React.ReactNode
  color: string
  bgColor: string
}

const slides: WelcomeSlide[] = [
  {
    title: "Добро пожаловать в ИНЕТШКОЛА! 🎉",
    description: "Здесь ты можешь учиться и играть! Выбирай свой класс и начинай приключение в мире знаний!",
    icon: <School className="w-16 h-16 md:w-20 md:h-20 text-white drop-shadow-lg" />,
    color: "from-violet-500 via-purple-500 to-fuchsia-500",
    bgColor: "from-purple-600/30 to-pink-600/30"
  },
  {
    title: "Уроки и темы 📚",
    description: "Изучай интересные темы по школьным предметам. Каждый урок помогает узнать что-то новое и полезное!",
    icon: <BookOpen className="w-16 h-16 md:w-20 md:h-20 text-white drop-shadow-lg" />,
    color: "from-blue-500 via-cyan-500 to-teal-500",
    bgColor: "from-blue-600/30 to-cyan-600/30"
  },
  {
    title: "Игры и викторины 🎮",
    description: "Закрепляй знания в весёлых играх! Зарабатывай звёзды и открывай новые достижения!",
    icon: <Gamepad2 className="w-16 h-16 md:w-20 md:h-20 text-white drop-shadow-lg" />,
    color: "from-emerald-500 via-green-500 to-lime-500",
    bgColor: "from-green-600/30 to-emerald-600/30"
  },
  {
    title: "Достижения и награды 🏆",
    description: "Выполняй задания, собирай баллы и становись лучше каждый день! Ты справишься! ✨",
    icon: <Trophy className="w-16 h-16 md:w-20 md:h-20 text-white drop-shadow-lg" />,
    color: "from-amber-500 via-yellow-500 to-orange-500",
    bgColor: "from-yellow-600/30 to-orange-600/30"
  }
]

export default function WelcomeModal() {
  const [state, setState] = useState<{ isOpen: boolean; hasSeenWelcome: boolean }>({ isOpen: false, hasSeenWelcome: false })

  // Check localStorage only on client
  useEffect(() => {
    const hasSeenWelcome = localStorage.getItem('hasSeenWelcome') === 'true'
    if (!hasSeenWelcome) {
      setState({ isOpen: true, hasSeenWelcome: false })
    }
  }, [])
  const [currentSlide, setCurrentSlide] = useState(0)
  const [isAnimating, setIsAnimating] = useState(false)
  const { isEnabled, setEnabled, playClick } = useSound()

  const handleClose = () => {
    setIsAnimating(true)
    setTimeout(() => {
      setState({ isOpen: false, hasSeenWelcome: true })
      localStorage.setItem('hasSeenWelcome', 'true')
    }, 300)
  }

  const handleNext = () => {
    playClick()
    if (currentSlide < slides.length - 1) {
      setIsAnimating(true)
      setTimeout(() => {
        setCurrentSlide(currentSlide + 1)
        setIsAnimating(false)
      }, 200)
    } else {
      handleClose()
    }
  }

  const toggleSound = () => {
    setEnabled(!isEnabled())
    playClick()
  }

  if (!state.isOpen) return null

  const slide = slides[currentSlide]
  const isLastSlide = currentSlide === slides.length - 1

  return (
    <div className={`fixed inset-0 z-[100] flex items-center justify-center p-4 
                    bg-black/80 backdrop-blur-md transition-opacity duration-300
                    ${isAnimating ? 'opacity-0' : 'opacity-100'}`}>
      <div className={`w-full max-w-lg relative overflow-hidden
                      bg-gradient-to-br from-gray-900 via-purple-900/95 to-pink-900/95
                      rounded-3xl border-4 border-white/20 shadow-2xl
                      transform transition-all duration-300
                      ${isAnimating ? 'scale-95 opacity-0' : 'scale-100 opacity-100'}`}>
        
        {/* Animated background */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className={`absolute inset-0 bg-gradient-to-br ${slide.bgColor} transition-all duration-500`} />
          <div className="absolute -top-20 -left-20 w-40 h-40 bg-purple-500/20 rounded-full blur-3xl animate-pulse" />
          <div className="absolute -bottom-20 -right-20 w-40 h-40 bg-pink-500/20 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
        </div>

        {/* Sound toggle button */}
        <button
          onClick={toggleSound}
          className="absolute top-4 left-4 z-10 p-3 rounded-xl bg-white/10 hover:bg-white/20 
                     transition-colors group"
          title={isEnabled() ? 'Выключить звук' : 'Включить звук'}
        >
          {isEnabled() ? (
            <Volume2 className="w-5 h-5 text-white group-hover:scale-110 transition-transform" />
          ) : (
            <VolumeX className="w-5 h-5 text-white/50 group-hover:scale-110 transition-transform" />
          )}
        </button>

        {/* Close button */}
        <button
          onClick={handleClose}
          className="absolute top-4 right-4 z-10 p-3 rounded-xl bg-white/10 hover:bg-white/20 
                     transition-colors"
        >
          <X className="w-5 h-5 text-white" />
        </button>

        {/* Content */}
        <div className="relative p-8 pt-16 text-center">
          {/* Animated icon */}
          <div className={`mb-8 inline-flex p-6 rounded-3xl bg-gradient-to-br ${slide.color} 
                          shadow-2xl transform hover:scale-105 transition-transform
                          animate-bounceIn`}>
            {slide.icon}
            {/* Sparkles around icon */}
            <Sparkles className="absolute -top-2 -right-2 w-6 h-6 text-yellow-300 animate-ping" />
            <Sparkles className="absolute -bottom-1 -left-2 w-5 h-5 text-yellow-200 animate-ping" style={{ animationDelay: '0.5s' }} />
          </div>

          {/* Title */}
          <h2 className="text-2xl md:text-3xl font-black text-white mb-4 
                         drop-shadow-lg animate-fadeIn">
            {slide.title}
          </h2>

          {/* Description */}
          <p className="text-lg text-purple-100 mb-8 leading-relaxed 
                        animate-fadeIn" style={{ animationDelay: '0.1s' }}>
            {slide.description}
          </p>

          {/* Progress dots */}
          <div className="flex justify-center gap-3 mb-8">
            {slides.map((s, i) => (
              <button
                key={i}
                onClick={() => {
                  playClick()
                  setIsAnimating(true)
                  setTimeout(() => {
                    setCurrentSlide(i)
                    setIsAnimating(false)
                  }, 200)
                }}
                className={`transition-all duration-300 rounded-full
                  ${i === currentSlide 
                    ? 'bg-yellow-400 w-8 h-3' 
                    : i < currentSlide 
                      ? 'bg-green-400 w-3 h-3' 
                      : 'bg-white/30 w-3 h-3 hover:bg-white/50'
                  }`}
              />
            ))}
          </div>

          {/* Button */}
          <button
            onClick={handleNext}
            className={`px-10 py-4 rounded-2xl font-bold text-xl transition-all
                       hover:scale-105 active:scale-95 flex items-center gap-3 mx-auto
                       bg-gradient-to-r ${slide.color} text-white shadow-lg
                       hover:shadow-xl animate-fadeIn`}
            style={{ animationDelay: '0.2s' }}
          >
            {isLastSlide ? (
              <>
                <Zap className="w-6 h-6" />
                Начать учиться!
                <Star className="w-6 h-6" />
              </>
            ) : (
              <>
                Далее
                <ChevronRight className="w-6 h-6" />
              </>
            )}
          </button>
        </div>

        {/* Decorative stars */}
        <div className="absolute top-20 left-4 text-4xl opacity-30 animate-float">⭐</div>
        <div className="absolute bottom-16 right-6 text-3xl opacity-30 animate-float" style={{ animationDelay: '0.5s' }}>✨</div>
        <div className="absolute top-1/3 right-8 text-2xl opacity-20 animate-float" style={{ animationDelay: '1s' }}>🌟</div>
        <div className="absolute bottom-1/3 left-8 text-2xl opacity-20 animate-float" style={{ animationDelay: '1.5s' }}>💫</div>
      </div>
    </div>
  )
}
