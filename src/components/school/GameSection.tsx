'use client'

import { useSchool } from '@/context/SchoolContext'
import { GameLesson } from '@/data/types'
import { ArrowLeft, Gamepad2, Star, Play, BookOpen, Atom, Calculator, Globe, Languages, Landmark, Leaf, Map, FlaskConical, Monitor, Code, Music, Palette, Dumbbell, Users, Shapes, Sigma, TrendingUp, Shield, Ruler } from 'lucide-react'
import { useState } from 'react'

// Маппинг иконок
const iconMap: Record<string, React.ReactNode> = {
  "BookOpen": <BookOpen className="w-5 h-5" />,
  "BookOpenText": <BookOpen className="w-5 h-5" />,
  "Atom": <Atom className="w-5 h-5" />,
  "Calculator": <Calculator className="w-5 h-5" />,
  "Globe": <Globe className="w-5 h-5" />,
  "Languages": <Languages className="w-5 h-5" />,
  "Landmark": <Landmark className="w-5 h-5" />,
  "Leaf": <Leaf className="w-5 h-5" />,
  "Map": <Map className="w-5 h-5" />,
  "FlaskConical": <FlaskConical className="w-5 h-5" />,
  "Monitor": <Monitor className="w-5 h-5" />,
  "Code": <Code className="w-5 h-5" />,
  "Music": <Music className="w-5 h-5" />,
  "Palette": <Palette className="w-5 h-5" />,
  "Dumbbell": <Dumbbell className="w-5 h-5" />,
  "Users": <Users className="w-5 h-5" />,
  "Shapes": <Shapes className="w-5 h-5" />,
  "Sigma": <Sigma className="w-5 h-5" />,
  "TrendingUp": <TrendingUp className="w-5 h-5" />,
  "Shield": <Shield className="w-5 h-5" />,
  "Ruler": <Ruler className="w-5 h-5" />,
  "Gamepad2": <Gamepad2 className="w-5 h-5" />,
}

// Маппинг цветов для предметов
const subjectColors: Record<string, string> = {
  "Русский язык": "from-red-500 to-rose-600",
  "Литература": "from-purple-500 to-violet-600",
  "Математика": "from-blue-500 to-indigo-600",
  "Алгебра": "from-indigo-500 to-blue-600",
  "Геометрия": "from-cyan-500 to-teal-600",
  "Окружающий мир": "from-green-500 to-emerald-600",
  "Иностранный язык": "from-pink-500 to-rose-600",
  "Английский": "from-pink-500 to-rose-600",
  "История": "from-amber-500 to-orange-600",
  "Биология": "from-green-500 to-lime-600",
  "География": "from-teal-500 to-cyan-600",
  "Физика": "from-purple-500 to-violet-600",
  "Химия": "from-emerald-500 to-green-600",
  "Обществознание": "from-violet-500 to-purple-600",
  "Информатика": "from-sky-500 to-blue-600",
  "Основы программирования": "from-cyan-500 to-teal-600",
  "Робототехника": "from-violet-500 to-indigo-600",
  "Экономика": "from-amber-500 to-yellow-600",
  "Основы права": "from-rose-500 to-red-600",
  "Технология": "from-yellow-500 to-amber-600",
  "Изобразительное искусство": "from-rose-500 to-pink-600",
  "Музыка": "from-cyan-500 to-blue-600",
  "Физическая культура": "from-orange-500 to-red-600",
  "Основы безопасности": "from-slate-500 to-gray-600",
  "Карьерное консультирование": "from-teal-500 to-emerald-600",
  "Психология": "from-pink-500 to-purple-600",
}

export default function GameSection() {
  const { games, selectedClass, selectGame, goBack } = useSchool()
  const [selectedSubject, setSelectedSubject] = useState<string | null>(null)
  
  const safeGames = Array.isArray(games) ? games : []
  const gradeName = selectedClass === 0 ? 'Подготовишки' : selectedClass ? `${selectedClass} класс` : 'Класс'

  // Группируем игры по предметам
  const gamesBySubject = safeGames.reduce((acc, game) => {
    const subject = game.subject || 'Другое'
    if (!acc[subject]) {
      acc[subject] = []
    }
    acc[subject].push(game)
    return acc
  }, {} as Record<string, GameLesson[]>)

  const subjects = Object.keys(gamesBySubject).sort()
  
  // Фильтрованные игры
  const displayedGames = selectedSubject 
    ? gamesBySubject[selectedSubject] || []
    : safeGames

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
        <p className="text-xl text-purple-200">{gradeName} • {safeGames.length} игр</p>
      </div>

      {/* Вкладки предметов */}
      {subjects.length > 1 && (
        <div className="mb-6 flex flex-wrap gap-2 justify-center">
          <button
            onClick={() => setSelectedSubject(null)}
            className={`px-4 py-2 rounded-xl font-medium transition-all flex items-center gap-2 ${
              selectedSubject === null 
                ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg' 
                : 'bg-white/10 text-white/80 hover:bg-white/20 hover:text-white'
            }`}
          >
            <Gamepad2 className="w-4 h-4" />
            Все игры ({safeGames.length})
          </button>
          {subjects.map(subject => (
            <button
              key={subject}
              onClick={() => setSelectedSubject(subject)}
              className={`px-4 py-2 rounded-xl font-medium transition-all flex items-center gap-2 ${
                selectedSubject === subject 
                  ? `bg-gradient-to-r ${subjectColors[subject] || 'from-purple-500 to-pink-500'} text-white shadow-lg` 
                  : 'bg-white/10 text-white/80 hover:bg-white/20 hover:text-white'
              }`}
            >
              {iconMap[gamesBySubject[subject][0]?.icon] || <Gamepad2 className="w-4 h-4" />}
              {subject} ({gamesBySubject[subject].length})
            </button>
          ))}
        </div>
      )}

      {/* Заголовок выбранной категории */}
      {selectedSubject && (
        <div className="mb-6 text-center">
          <h3 className="text-2xl font-bold text-white mb-1">{selectedSubject}</h3>
          <p className="text-purple-200">{displayedGames.length} игр</p>
        </div>
      )}

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {displayedGames.map((game: GameLesson, index: number) => (
          <button key={index} onClick={() => selectGame(game)}
            className="group relative overflow-hidden p-6 rounded-3xl bg-gradient-to-br from-purple-600/60 to-pink-600/60 border-4 border-white/20 hover:border-yellow-400/50 shadow-xl hover:shadow-2xl hover:scale-[1.02] transition-all duration-300 text-left">
            <div className={`p-4 rounded-2xl bg-gradient-to-br ${subjectColors[game.subject] || 'from-yellow-400 to-orange-500'} inline-block mb-4 group-hover:scale-110 transition-transform`}>
              {iconMap[game.icon] || <Gamepad2 className="w-10 h-10 text-white" />}
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

      {displayedGames.length === 0 && (
        <div className="text-center py-12">
          <Gamepad2 className="w-16 h-16 text-purple-400/50 mx-auto mb-4" />
          <p className="text-purple-200 text-xl">Нет игр в этой категории</p>
        </div>
      )}
    </div>
  )
}
