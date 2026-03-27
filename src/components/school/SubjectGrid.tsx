'use client'

import { useSchool } from '@/context/SchoolContext'
import { SubjectData } from '@/data/types'
import {
  BookOpen, Calculator, Palette, Music, Dumbbell, Globe, BookOpenText,
  Languages, Ruler, Shield, Map, Leaf, Atom, FlaskConical, Sigma, Shapes,
  Landmark, Users, Monitor, Hammer, HeartHandshake, Lightbulb, Cpu, Brush,
  MapPin, Blocks, MessageSquare, Wallet, Smartphone, Bug, Pencil, MessageCircle, Code,
  Gamepad2, ArrowLeft, Sparkles
} from 'lucide-react'

const iconMap: Record<string, React.ComponentType<{ className?: string }>> = {
  BookOpen, Calculator, Palette, Music, Dumbbell, Globe, BookOpenText, Languages, Ruler,
  Shield, Map, Leaf, Atom, FlaskConical, Sigma, Shapes, Landmark, Users, Monitor, Hammer,
  HeartHandshake, Lightbulb, Cpu, Brush, MapPin, Blocks, MessageSquare, Wallet, Smartphone, Bug,
  Pencil, MessageCircle, Code
}

const subjectEmojis: Record<string, string> = {
  'Математика': '🔢',
  'Русский язык': '📝',
  'Литература': '📚',
  'Окружающий мир': '🌍',
  'Английский': '🇬🇧',
  'Музыка': '🎵',
  'Физкультура': '⚽',
  'ИЗО': '🎨',
  'Технология': '🔧',
  'ОБЖ': '🛡️',
  'История': '📜',
  'Биология': '🧬',
  'География': '🗺️',
  'Физика': '⚛️',
  'Химия': '🧪',
  'Обществознание': '👥',
  'Информатика': '💻',
  'Алгебра': '📐',
  'Геометрия': '📏',
  'Экология': '🌿',
  'Робототехника': '🤖',
  'Кодирование': '👨‍💻',
  'Чтение': '📖',
  'Речь': '💬',
  'Письмо': '✍️',
  'Окр. мир': '🌏',
  'Ручной труд': '✂️',
}

export default function SubjectGrid() {
  const { selectedClass, subjects, games, goToSubject, goToGames, goBack, isKidMode } = useSchool()

  const getIconComponent = (iconName: string) => iconMap[iconName] || BookOpen
  const getEmoji = (title: string) => subjectEmojis[title] || '📖'

  return (
    <div className="w-full animate-slideIn">
      {/* Title */}
      <div className="text-center mb-4">
        <h2 className="text-3xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-3">
          {selectedClass === 0 ? '🎒 Подготовишки' : `📚 ${selectedClass} класс`}
        </h2>
        <p className="text-xl text-purple-200">
          Выбери предмет для изучения! ✨
        </p>
      </div>

      {/* Back button */}
      <div className="flex justify-start mb-6">
        <button
          onClick={goBack}
          className="flex items-center gap-2 text-white/80 hover:text-white text-lg font-medium 
                     bg-white/10 hover:bg-white/20 px-5 py-2 rounded-xl transition-all"
        >
          <ArrowLeft className="w-5 h-5" /> 
          Назад к классам
        </button>
      </div>

      {/* Games button */}
      {games.length > 0 && (
        <button
          onClick={goToGames}
          className="w-full mb-8 p-6 bg-gradient-to-r from-purple-500 via-pink-500 to-orange-500 
                     rounded-3xl shadow-xl hover:shadow-2xl transition-all hover:scale-[1.02] 
                     border-4 border-white/20 group"
        >
          <div className="flex items-center justify-center gap-4">
            <Gamepad2 className="w-12 h-12 text-white group-hover:rotate-12 transition-transform" />
            <div className="text-left">
              <div className="text-2xl font-black text-white">Игры и викторины!</div>
              <div className="text-white/80">{games.length} игр доступно</div>
            </div>
            <Sparkles className="w-10 h-10 text-yellow-300 animate-pulse" />
          </div>
        </button>
      )}

      {/* Subjects grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
        {subjects.map((subject: SubjectData, index: number) => {
          const IconComponent = getIconComponent(subject.icon)
          const emoji = getEmoji(subject.title)
          const lessonsCount = subject.detailedTopics?.reduce((acc, t) => acc + (t.subtopics?.reduce((a, s) => a + s.lessons.length, 0) || t.lessons?.length || 0), 0) || 0
          const gamesCount = subject.games?.length || 0

          return (
            <button
              key={index}
              onClick={() => goToSubject(subject)}
              className="group relative overflow-hidden p-6 rounded-3xl
                         bg-gradient-to-br from-gray-800/80 to-gray-900/80
                         border-4 border-white/10 hover:border-white/30
                         shadow-xl hover:shadow-2xl hover:scale-[1.02]
                         transition-all duration-300 text-left"
            >
              {/* Icon/Emoji */}
              <div className="flex items-start gap-4 mb-4">
                <div className={`p-4 rounded-2xl bg-gradient-to-br ${subject.color || 'from-purple-500 to-blue-500'} 
                                shadow-lg group-hover:scale-110 transition-transform`}>
                  <span className="text-4xl">{emoji}</span>
                </div>
                <div className="flex-1">
                  <h3 className="text-xl md:text-2xl font-bold text-white mb-1">
                    {subject.title}
                  </h3>
                  <div className="flex flex-wrap gap-2">
                    {lessonsCount > 0 && (
                      <span className="text-sm text-blue-300 bg-blue-500/20 px-2 py-1 rounded-lg">
                        📚 {lessonsCount} уроков
                      </span>
                    )}
                    {gamesCount > 0 && (
                      <span className="text-sm text-green-300 bg-green-500/20 px-2 py-1 rounded-lg">
                        🎮 {gamesCount} игр
                      </span>
                    )}
                  </div>
                </div>
              </div>

              {/* Topics preview */}
              {subject.topics && subject.topics.length > 0 && (
                <div className="flex flex-wrap gap-2 mb-4">
                  {subject.topics.slice(0, 3).map((topic, i) => (
                    <span key={i} className="text-sm text-purple-200 bg-purple-500/20 px-3 py-1 rounded-xl">
                      {topic}
                    </span>
                  ))}
                  {subject.topics.length > 3 && (
                    <span className="text-sm text-purple-300">+{subject.topics.length - 3}</span>
                  )}
                </div>
              )}

              {/* CTA */}
              <div className="flex items-center gap-2 text-purple-400 group-hover:text-purple-300 transition-colors">
                <span className="font-medium">Открыть</span>
                <span className="group-hover:translate-x-2 transition-transform">→</span>
              </div>
            </button>
          )
        })}
      </div>
    </div>
  )
}
