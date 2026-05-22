'use client'

import { useState, useMemo } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { GameLesson } from '@/data/types'
import { ArrowLeft, Gamepad2, Star, Play, BookOpen, ChevronRight } from 'lucide-react'

// Маппинг иконок предметов
const subjectIconMap: Record<string, string> = {
  'Математика': '🔢',
  'Алгебра': '📐',
  'Геометрия': '📏',
  'Русский язык': '📖',
  'Литература': '📚',
  'История': '🏛️',
  'Обществознание': '👥',
  'Физика': '⚛️',
  'Химия': '🧪',
  'Биология': '🧬',
  'География': '🌍',
  'Английский': '🇬🇧',
  'Информатика': '💻',
  'Программирование': '💻',
  'Окружающий мир': '🌿',
  'Музыка': '🎵',
  'Изобразительное искусство': '🎨',
  'Физическая культура': '⚽',
  'Технология': '🔧',
  'Основы безопасности': '🛡️',
  'Экономика': '📊',
  'Право': '⚖️',
  'Астрономия': '🔭',
  'Экология': '🌱',
  'Робототехника': '🤖',
  'Этика': '💝',
  'Религия': '🕊️',
  'Проекты': '📋',
  'Чтение': '📖',
  'Развитие речи': '🗣️',
  'Лепка': '🏺',
  'Финансы': '💰',
  'Цифровая грамотность': '📱',
  'Краеведение': '🗺️',
  'Психология': '🧠',
  'Карьера': '💼',
  'ОГЭ': '📝',
  'ЕГЭ': '📝',
  'Философия': '💭',
  'Бизнес': '💼',
  'Лаборатория': '🔬',
}

// Цвета предметов для карточек
const subjectColorMap: Record<string, string> = {
  'Математика': 'from-blue-500 to-cyan-500',
  'Алгебра': 'from-indigo-500 to-blue-500',
  'Геометрия': 'from-cyan-500 to-teal-500',
  'Русский язык': 'from-red-500 to-rose-500',
  'Литература': 'from-purple-500 to-pink-500',
  'История': 'from-amber-500 to-orange-500',
  'Обществознание': 'from-violet-500 to-purple-500',
  'Физика': 'from-violet-500 to-indigo-500',
  'Химия': 'from-emerald-500 to-green-500',
  'Биология': 'from-green-500 to-lime-500',
  'География': 'from-teal-500 to-emerald-500',
  'Английский': 'from-pink-500 to-rose-500',
  'Информатика': 'from-sky-500 to-blue-500',
  'Программирование': 'from-cyan-500 to-sky-500',
  'Окружающий мир': 'from-green-500 to-emerald-500',
  'Музыка': 'from-cyan-400 to-sky-400',
  'Изобразительное искусство': 'from-rose-500 to-pink-500',
  'Физическая культура': 'from-orange-500 to-amber-500',
  'Технология': 'from-yellow-500 to-orange-500',
  'Основы безопасности': 'from-slate-500 to-gray-500',
  'Экономика': 'from-amber-500 to-yellow-500',
  'Право': 'from-rose-500 to-red-500',
  'Астрономия': 'from-indigo-600 to-purple-600',
  'Экология': 'from-lime-500 to-green-500',
  'Робототехника': 'from-violet-500 to-fuchsia-500',
  'Этика': 'from-pink-400 to-rose-400',
  'Религия': 'from-amber-400 to-yellow-400',
  'Проекты': 'from-gray-500 to-slate-500',
  'Чтение': 'from-teal-400 to-cyan-400',
  'Развитие речи': 'from-teal-500 to-cyan-500',
  'Лепка': 'from-amber-400 to-orange-400',
  'Финансы': 'from-yellow-500 to-amber-500',
  'Цифровая грамотность': 'from-sky-400 to-blue-400',
  'Краеведение': 'from-emerald-400 to-teal-400',
  'Психология': 'from-fuchsia-500 to-purple-500',
  'Карьера': 'from-orange-400 to-amber-400',
  'ОГЭ': 'from-red-500 to-orange-500',
  'ЕГЭ': 'from-red-600 to-rose-600',
  'Философия': 'from-purple-500 to-violet-500',
  'Бизнес': 'from-amber-500 to-orange-500',
  'Лаборатория': 'from-emerald-400 to-cyan-400',
}

export default function GameSection() {
  const { games, selectedClass, selectGame, goBack } = useSchool()
  const [selectedSubject, setSelectedSubject] = useState<string | null>(null)
  
  const safeGames = Array.isArray(games) ? games : []
  const gradeName = selectedClass === 0 ? 'Подготовишки' : selectedClass ? `${selectedClass} класс` : 'Класс'

  // Группируем игры по предметам
  const gamesBySubject = useMemo(() => {
    const grouped: Record<string, GameLesson[]> = {}
    for (const game of safeGames) {
      const subject = game.subject || 'Другое'
      if (!grouped[subject]) {
        grouped[subject] = []
      }
      grouped[subject].push(game)
    }
    return grouped
  }, [safeGames])

  const subjectNames = Object.keys(gamesBySubject).sort((a, b) => {
    // Сортировка: основные предметы первыми
    const order = ['Математика', 'Алгебра', 'Геометрия', 'Русский язык', 'Литература', 'Физика', 'Химия', 'Биология', 'История', 'Обществознание', 'География', 'Английский', 'Информатика', 'Программирование']
    const aIdx = order.indexOf(a)
    const bIdx = order.indexOf(b)
    if (aIdx !== -1 && bIdx !== -1) return aIdx - bIdx
    if (aIdx !== -1) return -1
    if (bIdx !== -1) return 1
    return a.localeCompare(b)
  })

  // Если выбран предмет — показываем его игры
  const currentSubjectGames = selectedSubject ? gamesBySubject[selectedSubject] || [] : []

  return (
    <div className="w-full">
      <button onClick={goBack}
        className="mb-6 flex items-center gap-2 text-white/80 hover:text-white text-xl font-medium bg-white/10 hover:bg-white/20 px-6 py-3 rounded-2xl transition-all">
        <ArrowLeft className="w-6 h-6" /> Назад к предметам
      </button>

      <div className="text-center mb-8">
        <div className="inline-flex items-center gap-4 mb-4">
          <Gamepad2 className="w-16 h-16 text-purple-400" />
        </div>
        <h2 className="text-3xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-3">
          Игры и викторины!
        </h2>
        <p className="text-xl text-purple-200">{gradeName} • {safeGames.length} игр по {subjectNames.length} предметам</p>
      </div>

      {!selectedSubject ? (
        /* ===== Выбор предмета ===== */
        <div>
          <p className="text-center text-white/60 mb-6 text-lg">Выберите предмет для игр и викторин</p>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
            {subjectNames.map((subject) => {
              const gamesCount = gamesBySubject[subject].length
              const emoji = subjectIconMap[subject] || '📚'
              const gradient = subjectColorMap[subject] || 'from-gray-500 to-slate-500'
              
              return (
                <button
                  key={subject}
                  onClick={() => setSelectedSubject(subject)}
                  className="group relative overflow-hidden p-4 sm:p-5 rounded-2xl bg-gradient-to-br from-white/10 to-white/5 border-2 border-white/10 hover:border-white/30 shadow-lg hover:shadow-xl hover:scale-[1.03] transition-all duration-300 text-center"
                >
                  <div className={`absolute inset-0 bg-gradient-to-br ${gradient} opacity-10 group-hover:opacity-20 transition-opacity`} />
                  <div className="relative z-10">
                    <div className="text-3xl sm:text-4xl mb-2">{emoji}</div>
                    <h3 className="text-sm sm:text-base font-bold text-white mb-1 leading-tight">{subject}</h3>
                    <p className="text-white/50 text-xs sm:text-sm">{gamesCount} {gamesCount === 1 ? 'игра' : gamesCount < 5 ? 'игры' : 'игр'}</p>
                    <ChevronRight className="w-4 h-4 text-white/30 mx-auto mt-1 group-hover:text-white/60 transition-colors" />
                  </div>
                </button>
              )
            })}
          </div>
        </div>
      ) : (
        /* ===== Игры выбранного предмета ===== */
        <div>
          <button
            onClick={() => setSelectedSubject(null)}
            className="mb-6 flex items-center gap-2 text-purple-300 hover:text-purple-200 text-lg font-medium transition-colors"
          >
            <ArrowLeft className="w-5 h-5" /> Все предметы
          </button>

          <div className="flex items-center gap-3 mb-6">
            <span className="text-3xl">{subjectIconMap[selectedSubject] || '📚'}</span>
            <h3 className="text-2xl font-bold text-white">{selectedSubject}</h3>
            <span className="text-white/50 text-sm ml-2">{currentSubjectGames.length} {currentSubjectGames.length === 1 ? 'игра' : currentSubjectGames.length < 5 ? 'игры' : 'игр'}</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {currentSubjectGames.map((game: GameLesson, index: number) => (
              <button key={index} onClick={() => selectGame(game)}
                className="group relative overflow-hidden p-6 rounded-3xl bg-gradient-to-br from-purple-600/60 to-pink-600/60 border-4 border-white/20 hover:border-yellow-400/50 shadow-xl hover:shadow-2xl hover:scale-[1.02] transition-all duration-300 text-left">
                <div className="p-4 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 inline-block mb-4 group-hover:scale-110 transition-transform">
                  <Gamepad2 className="w-10 h-10 text-white" />
                </div>
                <h3 className="text-2xl font-bold text-white mb-2">{game.title}</h3>
                <p className="text-purple-200 mb-4">{game.subject}</p>
                <div className="flex items-center gap-4 mb-4">
                  <span className="text-white/80 bg-white/10 px-3 py-1 rounded-xl">{game.tasks?.length || 0} заданий</span>
                  <span className="flex items-center gap-1 text-yellow-400">
                    <Star className="w-5 h-5 fill-yellow-400" />{game.reward?.stars || 0}
                  </span>
                </div>
                <div className="flex items-center gap-2 text-white font-bold">
                  <Play className="w-6 h-6 group-hover:scale-110 transition-transform" />Начать игру!
                </div>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
