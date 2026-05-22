'use client'

import { useSchool } from '@/context/SchoolContext'
import { GameLesson } from '@/data/types'
import { useState, useMemo } from 'react'
import { ArrowLeft, Gamepad2, Star, Play, Sparkles, PartyPopper, Brain, Calculator, BookOpen, Zap, Puzzle, Target, Trophy, X, ChevronRight } from 'lucide-react'
import MemoryGame from './MemoryGame'
import QuickMath from './QuickMath'
import MathRacing from './MathRacing'
import NumberPuzzle from './NumberPuzzle'
import SpellingGame from './SpellingGame'
import HangmanGame from './HangmanGame'
import SequenceGame from './SequenceGame'
import ChallengeMode from './ChallengeMode'

type MiniGameId = 'memory' | 'quickmath' | 'racing' | 'puzzle' | 'spelling' | 'hangman' | 'sequence' | 'challenge' | null

interface MiniGame {
  id: MiniGameId
  title: string
  icon: React.ReactNode
  subject: string
  description: string
  colorClass: string
  minGrade?: number
  maxGrade?: number
}

// Эмодзи для предметов
const subjectEmojiMap: Record<string, string> = {
  'Математика': '🔢',
  'Алгебра': '📐',
  'Геометрия': '📏',
  'Русский язык': '📝',
  'Литература': '📚',
  'История': '🏛️',
  'Обществознание': '👥',
  'Физика': '⚛️',
  'Химия': '🧪',
  'Биология': '🧬',
  'География': '🌍',
  'Английский': '🇬🇧',
  'Информатика': '💻',
  'Окружающий мир': '🌿',
  'Музыка': '🎵',
  'Изобразительное искусство': '🎨',
  'Физическая культура': '⚽',
  'Технология': '🔧',
  'Основы безопасности': '🛡️',
  'Чтение': '📖',
  'Развитие речи': '🗣️',
  'Лепка': '🏺',
  'Проекты': '📋',
  'Память': '🧠',
  'Логика': '🧩',
  'Слова': '💬',
  'Разное': '🎲',
}

// Яркие градиенты для карточек предметов (детский стиль)
const subjectColorMap: Record<string, string> = {
  'Математика': 'from-blue-400 to-cyan-400',
  'Алгебра': 'from-indigo-400 to-blue-400',
  'Геометрия': 'from-cyan-400 to-teal-400',
  'Русский язык': 'from-red-400 to-rose-400',
  'Литература': 'from-purple-400 to-pink-400',
  'История': 'from-amber-400 to-orange-400',
  'Физика': 'from-violet-400 to-indigo-400',
  'Химия': 'from-emerald-400 to-green-400',
  'Биология': 'from-green-400 to-lime-400',
  'География': 'from-teal-400 to-emerald-400',
  'Английский': 'from-pink-400 to-rose-400',
  'Информатика': 'from-sky-400 to-blue-400',
  'Окружающий мир': 'from-green-400 to-emerald-400',
  'Музыка': 'from-cyan-300 to-sky-300',
  'Изобразительное искусство': 'from-rose-400 to-pink-400',
  'Физическая культура': 'from-orange-400 to-amber-400',
  'Технология': 'from-yellow-400 to-orange-400',
  'Основы безопасности': 'from-slate-400 to-gray-400',
  'Чтение': 'from-teal-300 to-cyan-300',
  'Развитие речи': 'from-teal-400 to-cyan-400',
  'Лепка': 'from-amber-300 to-orange-300',
  'Проекты': 'from-gray-400 to-slate-400',
  'Память': 'from-pink-400 to-rose-400',
  'Логика': 'from-purple-400 to-violet-400',
  'Слова': 'from-amber-400 to-yellow-400',
  'Разное': 'from-yellow-400 to-amber-400',
}

export default function KidGameSection() {
  const { games, selectedClass, selectGame, goBack } = useSchool()
  const [activeMiniGame, setActiveMiniGame] = useState<MiniGameId>(null)
  const [selectedSubject, setSelectedSubject] = useState<string | null>(null)

  // Настоящие мини-игры для детей
  const miniGames: MiniGame[] = useMemo(() => {
    const baseGames: MiniGame[] = [
      {
        id: 'memory',
        title: 'Найди пару',
        icon: <Brain className="w-10 h-10" />,
        subject: 'Память',
        description: selectedClass <= 2 ? 'Найди одинаковые карточки!' : 'Найди пары понятий!',
        colorClass: 'from-pink-500 to-rose-500',
        minGrade: 0,
        maxGrade: 11
      },
      {
        id: 'quickmath',
        title: 'Быстрый счёт',
        icon: <Calculator className="w-10 h-10" />,
        subject: 'Математика',
        description: selectedClass <= 4 ? 'Реши примеры за время!' : 'Реши сложные примеры!',
        colorClass: 'from-blue-500 to-cyan-500',
        minGrade: 0,
        maxGrade: 11
      },
      {
        id: 'racing',
        title: 'Математические гонки',
        icon: <Zap className="w-10 h-10" />,
        subject: 'Математика',
        description: selectedClass <= 2 ? 'Гонки с примерами!' : 'Соревнование по математике!',
        colorClass: 'from-green-500 to-emerald-500',
        minGrade: 1,
        maxGrade: 9
      },
      {
        id: 'puzzle',
        title: 'Числовые головоломки',
        icon: <Puzzle className="w-10 h-10" />,
        subject: 'Логика',
        description: 'Реши числовые задачки!',
        colorClass: 'from-purple-500 to-violet-500',
        minGrade: 2,
        maxGrade: 11
      },
      {
        id: 'spelling',
        title: 'Правописание',
        icon: <BookOpen className="w-10 h-10" />,
        subject: 'Русский язык',
        description: selectedClass <= 4 ? 'Напиши слова правильно!' : 'Проверь орфографию!',
        colorClass: 'from-red-500 to-orange-500',
        minGrade: 1,
        maxGrade: 11
      },
      {
        id: 'hangman',
        title: 'Угадай слово',
        icon: <Target className="w-10 h-10" />,
        subject: 'Слова',
        description: 'Угадай слово по буквам!',
        colorClass: 'from-amber-500 to-yellow-500',
        minGrade: 1,
        maxGrade: 7
      },
      {
        id: 'sequence',
        title: 'Закономерности',
        icon: <Brain className="w-10 h-10" />,
        subject: 'Логика',
        description: 'Продолжи последовательность!',
        colorClass: 'from-indigo-500 to-purple-500',
        minGrade: 0,
        maxGrade: 6
      },
      {
        id: 'challenge',
        title: 'Челлендж дня',
        icon: <Trophy className="w-10 h-10" />,
        subject: 'Разное',
        description: 'Ежедневное задание!',
        colorClass: 'from-yellow-500 to-amber-500',
        minGrade: 0,
        maxGrade: 11
      },
    ]

    return baseGames.filter(game => 
      (game.minGrade === undefined || selectedClass >= game.minGrade) &&
      (game.maxGrade === undefined || selectedClass <= game.maxGrade)
    )
  }, [selectedClass])

  const safeGames = Array.isArray(games) ? games : []
  
  // Эмодзи и название класса
  const gradeEmoji = selectedClass === 0 ? '🎈' : selectedClass === 1 ? '🌟' : selectedClass <= 4 ? '🌈' : selectedClass <= 7 ? '🎯' : '🏆'
  const gradeName = selectedClass === 0 ? 'Подготовительный' : 
                    selectedClass === 1 ? '1 класс' : 
                    selectedClass === 2 ? '2 класс' : 
                    selectedClass === 3 ? '3 класс' : 
                    selectedClass === 4 ? '4 класс' : 
                    selectedClass === 5 ? '5 класс' :
                    selectedClass === 6 ? '6 класс' :
                    selectedClass === 7 ? '7 класс' :
                    selectedClass === 8 ? '8 класс' :
                    selectedClass === 9 ? '9 класс' :
                    selectedClass === 10 ? '10 класс' : '11 класс'

  // Объединяем мини-игры и обучающие задания по предметам
  const allItemsBySubject = useMemo(() => {
    const grouped: Record<string, { miniGames: MiniGame[]; eduGames: GameLesson[] }> = {}
    
    // Мини-игры по предметам
    for (const mg of miniGames) {
      const subject = mg.subject || 'Разное'
      if (!grouped[subject]) grouped[subject] = { miniGames: [], eduGames: [] }
      grouped[subject].miniGames.push(mg)
    }
    
    // Обучающие задания по предметам
    for (const eg of safeGames) {
      const subject = eg.subject || 'Другое'
      if (!grouped[subject]) grouped[subject] = { miniGames: [], eduGames: [] }
      grouped[subject].eduGames.push(eg)
    }
    
    return grouped
  }, [miniGames, safeGames])

  const subjectNames = Object.keys(allItemsBySubject).sort((a, b) => {
    const order = ['Математика', 'Алгебра', 'Русский язык', 'Литература', 'Окружающий мир', 'Память', 'Логика', 'Слова', 'Разное']
    const aIdx = order.indexOf(a)
    const bIdx = order.indexOf(b)
    if (aIdx !== -1 && bIdx !== -1) return aIdx - bIdx
    if (aIdx !== -1) return -1
    if (bIdx !== -1) return 1
    return a.localeCompare(b)
  })

  // Если активна мини-игра — показываем её
  if (activeMiniGame) {
    return (
      <div className="w-full relative">
        <button 
          onClick={() => setActiveMiniGame(null)}
          className="mb-6 flex items-center gap-3 text-white text-xl font-bold bg-red-500/80 hover:bg-red-600
            px-6 py-3 rounded-2xl transition-all hover:scale-105 active:scale-95"
        >
          <X className="w-6 h-6" />
          <span>Закрыть игру</span>
        </button>
        {(() => {
          switch (activeMiniGame) {
            case 'memory': return <MemoryGame />
            case 'quickmath': return <QuickMath />
            case 'racing': return <MathRacing />
            case 'puzzle': return <NumberPuzzle />
            case 'spelling': return <SpellingGame />
            case 'hangman': return <HangmanGame />
            case 'sequence': return <SequenceGame />
            case 'challenge': return <ChallengeMode />
            default: return null
          }
        })()}
      </div>
    )
  }

  // ===== Если выбран предмет — показываем его игры =====
  if (selectedSubject) {
    const subjectData = allItemsBySubject[selectedSubject]
    const subjectMiniGames = subjectData?.miniGames || []
    const subjectEduGames = subjectData?.eduGames || []
    const totalGames = subjectMiniGames.length + subjectEduGames.length
    const emoji = subjectEmojiMap[selectedSubject] || '📚'

    return (
      <div className="w-full">
        <button onClick={goBack}
          className="mb-6 flex items-center gap-3 text-white text-2xl font-black bg-white/10 hover:bg-white/20
            px-8 py-4 rounded-3xl transition-all hover:scale-105 active:scale-95">
          <ArrowLeft className="w-8 h-8" />
          <span>Назад</span>
        </button>

        <button
          onClick={() => setSelectedSubject(null)}
          className="mb-6 flex items-center gap-2 text-purple-300 hover:text-purple-200 text-lg font-medium transition-colors"
        >
          <ArrowLeft className="w-5 h-5" /> Все предметы
        </button>

        <div className="text-center mb-8">
          <div className="text-5xl mb-3">{emoji}</div>
          <h2 className="text-3xl md:text-4xl font-black text-transparent bg-clip-text
            bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-2">
            {selectedSubject}
          </h2>
          <p className="text-xl text-purple-200">
            <PartyPopper className="w-5 h-5 inline" /> {totalGames} {totalGames === 1 ? 'игра' : totalGames < 5 ? 'игры' : 'игр'} для {gradeName}
          </p>
        </div>

        {/* Мини-игры предмета */}
        {subjectMiniGames.length > 0 && (
          <div className="mb-8">
            <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
              <Sparkles className="w-6 h-6 text-yellow-400" />
              Мини-игры
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {subjectMiniGames.map((game) => (
                <button
                  key={game.id}
                  onClick={() => setActiveMiniGame(game.id)}
                  className="group relative overflow-hidden p-5 rounded-2xl
                    bg-gradient-to-br border-2 border-white/20 hover:border-yellow-400
                    shadow-lg hover:shadow-xl hover:scale-[1.02] active:scale-95 
                    transition-all duration-200 text-left"
                >
                  <div className={`p-3 rounded-xl bg-gradient-to-br ${game.colorClass} inline-block mb-3 group-hover:scale-110 transition-transform text-white`}>
                    {game.icon}
                  </div>
                  <h3 className="text-lg font-bold text-white mb-1">{game.title}</h3>
                  <p className="text-sm text-purple-200 mb-2">{game.description}</p>
                  <div className={`flex items-center gap-2 text-white text-sm font-medium
                    bg-white/20 px-3 py-1.5 rounded-lg group-hover:bg-white/30 transition-colors`}>
                    <Play className="w-4 h-4" />
                    <span>Играть</span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Обучающие задания предмета */}
        {subjectEduGames.length > 0 && (
          <div className="mb-8">
            <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
              <BookOpen className="w-6 h-6 text-purple-400" />
              Обучающие задания
              <Star className="w-6 h-6 text-yellow-400" />
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {subjectEduGames.map((game: GameLesson, index: number) => (
                <button
                  key={index}
                  onClick={() => selectGame(game)}
                  className="group relative overflow-hidden p-4 rounded-2xl
                    bg-gradient-to-br from-indigo-500/30 to-purple-500/30
                    border-2 border-white/20 hover:border-yellow-400
                    shadow-lg hover:shadow-xl hover:scale-[1.02] active:scale-95 
                    transition-all duration-200 text-left"
                >
                  <div className="p-3 rounded-xl bg-gradient-to-br from-yellow-400 to-orange-500
                    inline-block mb-3 group-hover:scale-110 transition-transform">
                    <Gamepad2 className="w-6 h-6 text-white" />
                  </div>
                  <h3 className="text-base font-bold text-white mb-1">{game.title}</h3>
                  <div className="flex items-center gap-2">
                    <span className="text-xs text-white/80 bg-white/20 px-2 py-0.5 rounded">
                      {game.tasks?.length || 0} заданий
                    </span>
                    <span className="flex items-center gap-1 text-sm text-yellow-400">
                      <Star className="w-4 h-4 fill-yellow-400" />
                      {game.reward?.stars || 0}
                    </span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    )
  }

  // ===== Главная страница — выбор предмета =====
  return (
    <div className="w-full">
      <button onClick={goBack}
        className="mb-6 flex items-center gap-3 text-white text-2xl font-black bg-white/10 hover:bg-white/20
          px-8 py-4 rounded-3xl transition-all hover:scale-105 active:scale-95">
        <ArrowLeft className="w-8 h-8" />
        <span>Назад</span>
      </button>

      {/* Header with animation */}
      <div className="text-center mb-10">
        <div className="inline-flex items-center gap-4 mb-6">
          <Sparkles className="w-12 h-12 text-yellow-400 animate-pulse" />
          <Gamepad2 className="w-20 h-20 text-purple-400 animate-bounce" />
          <Sparkles className="w-12 h-12 text-yellow-400 animate-pulse" />
        </div>

        <h2 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text
          bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-4">
          {gradeEmoji} Игры: {gradeName} {gradeEmoji}
        </h2>

        <p className="text-2xl text-purple-200 flex items-center justify-center gap-2">
          <PartyPopper className="w-6 h-6" />
          {subjectNames.length} предметов · {miniGames.length + safeGames.length} игр
          <PartyPopper className="w-6 h-6" />
        </p>
      </div>

      {/* Предметы */}
      <p className="text-center text-white/60 mb-6 text-lg">Выбери предмет и играй!</p>
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
        {subjectNames.map((subject) => {
          const data = allItemsBySubject[subject]
          const total = (data.miniGames?.length || 0) + (data.eduGames?.length || 0)
          const emoji = subjectEmojiMap[subject] || '📚'
          const gradient = subjectColorMap[subject] || 'from-gray-400 to-slate-400'
          const hasMiniGames = (data.miniGames?.length || 0) > 0
          
          return (
            <button
              key={subject}
              onClick={() => setSelectedSubject(subject)}
              className="group relative overflow-hidden p-4 sm:p-5 rounded-2xl
                bg-gradient-to-br from-white/10 to-white/5
                border-2 border-white/10 hover:border-white/30
                shadow-lg hover:shadow-xl hover:scale-[1.03] active:scale-95
                transition-all duration-300 text-center"
            >
              <div className={`absolute inset-0 bg-gradient-to-br ${gradient} opacity-15 group-hover:opacity-25 transition-opacity rounded-2xl`} />
              <div className="relative z-10">
                <div className="text-3xl sm:text-4xl mb-2">{emoji}</div>
                <h3 className="text-sm sm:text-base font-bold text-white mb-1 leading-tight">{subject}</h3>
                <p className="text-white/50 text-xs sm:text-sm">
                  {total} {total === 1 ? 'игра' : total < 5 ? 'игры' : 'игр'}
                  {hasMiniGames && <Sparkles className="w-3 h-3 inline text-yellow-400 ml-1" />}
                </p>
                <ChevronRight className="w-4 h-4 text-white/30 mx-auto mt-1 group-hover:text-white/60 transition-colors" />
              </div>
            </button>
          )
        })}
      </div>

      {/* Fun footer */}
      <div className="mt-10 text-center">
        <p className="text-xl text-white/60">
          Выбери предмет и получи звёздочки! ⭐
        </p>
      </div>
    </div>
  )
}
