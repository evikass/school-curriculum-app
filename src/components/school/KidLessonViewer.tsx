'use client'

import { useSchool, LessonData } from '@/context/SchoolContext'
import { useState } from 'react'
import {
  ArrowLeft, Star, BookOpen, ChevronDown, ChevronRight, Gamepad2, Play,
  Calculator, Palette, Music, Dumbbell, Globe, BookOpenText,
  Languages, Ruler, Shield, Map, Leaf, Atom, FlaskConical, Sigma, Shapes,
  Landmark, Users, Monitor, Hammer, HeartHandshake, Lightbulb, Cpu, Brush,
  MapPin, Blocks, MessageSquare, Wallet, Smartphone, Bug, Pencil, MessageCircle, Code, X
} from 'lucide-react'
import { generateLessonQuiz } from '@/lib/lessonQuizGenerator'
import LessonAnimatedSVG from './LessonAnimatedSVG'
import PeriodicTable from './PeriodicTable'
import { LessonTopic, LessonItem } from '@/data/types'

// Цвета для смысловых блоков
const blockColors = [
  { bg: 'bg-pink-500/15', border: 'border-pink-400/30', accent: 'text-pink-300' },
  { bg: 'bg-cyan-500/15', border: 'border-cyan-400/30', accent: 'text-cyan-300' },
  { bg: 'bg-amber-500/15', border: 'border-amber-400/30', accent: 'text-amber-300' },
  { bg: 'bg-emerald-500/15', border: 'border-emerald-400/30', accent: 'text-emerald-300' },
  { bg: 'bg-purple-500/15', border: 'border-purple-400/30', accent: 'text-purple-300' },
  { bg: 'bg-rose-500/15', border: 'border-rose-400/30', accent: 'text-rose-300' },
]

// Цвета для выделения слов в примерах
const highlightColors = [
  'text-yellow-300',
  'text-cyan-300',
  'text-pink-300',
  'text-lime-300',
  'text-orange-300',
  'text-sky-300',
]

// Цвета для заголовков-подзаголовков
const titleColors = [
  'text-cyan-300',
  'text-pink-300',
  'text-lime-300',
  'text-orange-300',
  'text-purple-300',
  'text-rose-300',
  'text-amber-300',
  'text-emerald-300',
]

// Типы важных фраз с их цветами и эмодзи
const importantPhrases: { pattern: string; color: string; bg: string; emoji: string }[] = [
  { pattern: 'важно', color: 'text-yellow-300', bg: 'bg-yellow-500/25', emoji: '⭐' },
  { pattern: 'запомни', color: 'text-pink-300', bg: 'bg-pink-500/25', emoji: '💡' },
  { pattern: 'обрати внимание', color: 'text-orange-300', bg: 'bg-orange-500/25', emoji: '👁️' },
  { pattern: 'правило', color: 'text-cyan-300', bg: 'bg-cyan-500/25', emoji: '📏' },
  { pattern: 'определение', color: 'text-purple-300', bg: 'bg-purple-500/25', emoji: '📖' },
  { pattern: 'итак', color: 'text-lime-300', bg: 'bg-lime-500/25', emoji: '✅' },
  { pattern: 'главное', color: 'text-rose-300', bg: 'bg-rose-500/25', emoji: '🎯' },
  { pattern: 'помни', color: 'text-amber-300', bg: 'bg-amber-500/25', emoji: '🧠' },
  { pattern: 'нужно', color: 'text-sky-300', bg: 'bg-sky-500/25', emoji: '✨' },
  { pattern: 'надо', color: 'text-emerald-300', bg: 'bg-emerald-500/25', emoji: '💪' },
  { pattern: 'можно', color: 'text-indigo-300', bg: 'bg-indigo-500/25', emoji: '✅' },
  { pattern: 'нельзя', color: 'text-red-300', bg: 'bg-red-500/25', emoji: '❌' },
  { pattern: 'как', color: 'text-teal-300', bg: 'bg-teal-500/25', emoji: '❓' },
  { pattern: 'чтобы', color: 'text-fuchsia-300', bg: 'bg-fuchsia-500/25', emoji: '🎯' },
]

// Проверка, это заголовок в markdown формате **Текст:** или просто Текст:
const isHeading = (text: string): boolean => {
  // Убираем markdown звёздочки для проверки
  const cleaned = text.replace(/\*\*/g, '')
  return cleaned.endsWith(':') && cleaned.length > 2 && cleaned.length < 60
}

// Извлечь текст заголовка без звёздочек и двоеточия
const extractHeadingText = (text: string): string => {
  return text.replace(/\*\*/g, '').replace(/:$/, '')
}

// Проверка, это подзаголовок в формате **Текст** или **Текст эмодзи**
const isSubheading = (text: string): boolean => {
  // Паттерн: **Текст** или **Текст эмодзи** - начинается и заканчивается **
  const match = text.match(/^\*\*(.+)\*\*$/)
  if (match) {
    const content = match[1].trim()
    // Это подзаголовок если: начинается с заглавной буквы и не слишком длинный
    const startsWithCapital = /^[А-ЯЁA-Z]/.test(content)
    const isReasonableLength = content.length > 1 && content.length < 50
    // Не считаем подзаголовком если это вся строка с важными словами
    const lower = content.toLowerCase()
    const hasImportantWord = ['вопросы', 'упражнения', 'задания'].some(w => lower.includes(w))
    return startsWithCapital && isReasonableLength && !hasImportantWord
  }
  return false
}

// Извлечь текст подзаголовка без звёздочек
const extractSubheadingText = (text: string): string => {
  return text.replace(/\*\*/g, '')
}

// Проверка, содержит ли строка числа
const hasNumbers = (text: string): boolean => /\d/.test(text)

// Найти тип важной фразы
const findImportantType = (text: string): { color: string; bg: string; emoji: string } | null => {
  const lower = text.toLowerCase()
  for (const phrase of importantPhrases) {
    if (lower.includes(phrase.pattern)) {
      return { color: phrase.color, bg: phrase.bg, emoji: phrase.emoji }
    }
  }
  return null
}

// Форматирование строки примера с выделением слова
const formatExampleLine = (text: string, colorIndex: number) => {
  // Убираем markdown звёздочки
  const cleaned = text.replace(/\*\*/g, '')

  // Паттерн: "- ДОМ — ..." или "ДОМ — ..." или "- МА-МА — ..."
  const match = cleaned.match(/^(-\s*)?([А-ЯЁа-яёA-Za-z\-]+)\s*[—–-]\s*(.+)$/)
  if (match) {
    const [, dash, word, rest] = match
    const highlightColor = highlightColors[colorIndex % highlightColors.length]
    return (
      <>
        {dash && <span className="text-white/60">{dash}</span>}
        <span className={`${highlightColor} font-bold`}>{word}</span>
        <span className="text-white/70"> — </span>
        <span className="text-white/90">{rest}</span>
      </>
    )
  }
  return cleaned
}

// Убрать markdown звёздочки из текста
const cleanMarkdown = (text: string): string => {
  return text.replace(/\*\*/g, '')
}

// Функция форматирования текста с цветовыми блоками для групп
const formatKidText = (text: string) => {
  const paragraphs = text.split(/\n\n+/)
  let blockIndex = 0
  let titleColorIndex = 0

  return paragraphs.map((paragraph, pIdx) => {
    const lines = paragraph.split('\n').filter(l => l.trim())
    if (lines.length === 0) return null

    const color = blockColors[blockIndex % blockColors.length]
    blockIndex++

    let exampleIndex = 0

    const content = lines.map((line, lIdx) => {
      const trimmed = line.trim()
      if (!trimmed) return null

      // Заголовок (типа "**Примеры:**", "**Правило:**", и т.д.) - крупно, ярко, без звёздочек
      if (isHeading(trimmed)) {
        return (
          <h3 key={lIdx} className="text-2xl md:text-3xl font-black mb-3 mt-5 first:mt-0 text-yellow-300 drop-shadow-lg">
            {extractHeadingText(trimmed)}
          </h3>
        )
      }

      // Подзаголовок (типа "**Зима ❄️**", "**Весна 🌸**", "**Собака 🐕**")
      if (isSubheading(trimmed)) {
        const titleColor = titleColors[titleColorIndex % titleColors.length]
        titleColorIndex++
        return (
          <h4 key={lIdx} className={`text-xl md:text-2xl font-bold mb-2 mt-4 first:mt-0 ${titleColor} drop-shadow`}>
            {extractSubheadingText(trimmed)}
          </h4>
        )
      }

      // Важная фраза с цветным фоном
      const importantType = findImportantType(trimmed)
      if (importantType) {
        return (
          <p key={lIdx} className={`text-lg md:text-xl font-bold ${importantType.color} my-2 ${importantType.bg} px-4 py-3 rounded-xl border border-white/10`}>
            {importantType.emoji} {cleanMarkdown(trimmed)}
          </p>
        )
      }

      // Строка с примером (содержит "—" тире и слово в начале)
      if (trimmed.includes('—') || trimmed.includes('–')) {
        const formatted = formatExampleLine(trimmed, exampleIndex)
        exampleIndex++
        return (
          <p key={lIdx} className="text-lg md:text-xl my-2 leading-relaxed text-white/90">
            {formatted}
          </p>
        )
      }

      // Строка с числами
      if (hasNumbers(trimmed)) {
        return (
          <p key={lIdx} className="text-lg md:text-xl text-cyan-200 my-2">
            {cleanMarkdown(trimmed)}
          </p>
        )
      }

      // Строка с ! или ?
      if (trimmed.includes('!') || trimmed.includes('?')) {
        return (
          <p key={lIdx} className="text-lg md:text-xl text-white/95 my-2 font-medium">
            {cleanMarkdown(trimmed)}
          </p>
        )
      }

      // Обычная строка
      return (
        <p key={lIdx} className="text-lg md:text-xl text-white/85 my-2">
          {cleanMarkdown(trimmed)}
        </p>
      )
    })

    return (
      <div key={pIdx} className={`${color.bg} ${color.border} border-2 rounded-3xl p-5 md:p-6 mb-4 last:mb-0`}>
        {content}
      </div>
    )
  })
}

const subjectEmojis: Record<string, string> = {
  'Математика': '🔢',
  'Русский язык': '📝',
  'Литература': '📚',
  'Литературное чтение': '📖',
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
  'Основы счёта': '🔢',
  'Подготовка к письму': '✏️',
  'Развитие речи': '💬',
}

interface Lesson {
  title: string
  description: string
  tasks: string[]
}

export default function KidLessonViewer() {
  const { selectedSubject, goBack, completeTopic, addPoints, selectGame, selectGameFromLesson, games: contextGames, selectedLesson, selectLesson } = useSchool()
  const [selectedTopicIndex, setSelectedTopicIndex] = useState<number | null>(null)
  const [showGames, setShowGames] = useState(false)
  const [completedLessons, setCompletedLessons] = useState<Set<string>>(new Set())
  const [showPeriodicTable, setShowPeriodicTable] = useState(false)

  const getEmoji = (title: string) => subjectEmojis[title] || '📖'
  
  const isChemistryOrPhysics = selectedSubject && (
    selectedSubject.title.toLowerCase().includes('химия') ||
    selectedSubject.title.toLowerCase().includes('физика')
  )
  
  const showPeriodicTableButton = isChemistryOrPhysics

  if (!selectedSubject) return null

  const topics = selectedSubject.detailedTopics || []
  const games = contextGames || []

  // Если выбран урок - показываем его содержимое
  if (selectedLesson) {
    return (
      <div className="w-full animate-slideIn">
        <div className="max-w-3xl mx-auto mb-6">
          <button
            onClick={() => selectLesson(null)}
            className="flex items-center gap-2 text-white text-lg font-bold 
                       bg-white/20 hover:bg-white/30 px-5 py-3 rounded-2xl transition-all"
          >
            <ArrowLeft className="w-5 h-5" /> Назад к урокам
          </button>
        </div>

        <div className="max-w-3xl mx-auto">
          {/* ОБЩИЙ БЛОК УРОКА */}
          <div className="bg-gradient-to-br from-indigo-500/30 via-purple-500/30 to-pink-500/30 
                          rounded-3xl p-6 md:p-10 border-4 border-white/20 shadow-2xl">
            
            {/* Заголовок урока */}
            <div className="text-center mb-8">
              <div className="text-6xl md:text-7xl mb-4">{getEmoji(selectedSubject?.title || '')}</div>
              
              <h2 className="text-2xl md:text-4xl font-black text-transparent bg-clip-text 
                             bg-gradient-to-r from-yellow-300 via-pink-300 to-cyan-300 mb-3">
                {selectedLesson.title}
              </h2>
              
              <div className="inline-block bg-purple-500/30 px-6 py-2 rounded-full">
                <span className="text-lg text-purple-200">{selectedSubject?.title}</span>
              </div>
            </div>

            {/* Изображение урока из SVG файла (приоритет) */}
            {'image' in selectedLesson && selectedLesson.image ? (
              <div className="flex justify-center mb-6">
                <div className="relative rounded-3xl overflow-hidden border-4 border-purple-400/30 shadow-2xl max-w-2xl w-full">
                  <img 
                    src={selectedLesson.image as string} 
                    alt={selectedLesson.title}
                    className="w-full h-auto"
                    onError={(e) => {
                      const target = e.target as HTMLImageElement;
                      target.style.display = 'none';
                    }}
                  />
                </div>
              </div>
            ) : (
              /* Анимированный SVG - только если нет внешней картинки */
              <div className="flex justify-center mb-6">
                <LessonAnimatedSVG 
                  lessonTitle={selectedLesson.title} 
                  subject={selectedSubject?.title || ''}
                  size="medium" 
                />
              </div>
            )}
            
            {/* Контент урока */}
            <div className="space-y-0">
              {formatKidText(selectedLesson.description)}
            </div>

            {/* Блок с заданиями */}
            {selectedLesson.tasks && selectedLesson.tasks.length > 0 && (
              <div className="mt-8 bg-amber-500/20 rounded-3xl p-6 border-2 border-amber-400/30">
                <h4 className="text-xl md:text-2xl font-bold text-amber-300 mb-4">
                  Задания:
                </h4>
                <div className="space-y-3">
                  {selectedLesson.tasks.map((task, i) => (
                    <div key={i} className="flex items-start gap-4 text-white/90 text-lg">
                      <span className="w-8 h-8 rounded-full bg-amber-400 flex items-center justify-center text-sm font-bold text-amber-900 flex-shrink-0 mt-1">
                        {i + 1}
                      </span>
                      <span>{task}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Кнопки действий */}
            <div className="mt-8 flex gap-4 justify-center flex-wrap">
              <button
                onClick={() => {
                  const subjectGames = games.filter(g =>
                    g.subject === selectedSubject.title ||
                    selectedSubject.title.toLowerCase().includes(g.subject.toLowerCase()) ||
                    g.subject.toLowerCase().includes(selectedSubject.title.toLowerCase())
                  )
                  if (subjectGames.length > 0) {
                    const randomGame = subjectGames[Math.floor(Math.random() * subjectGames.length)]
                    selectGameFromLesson(randomGame)
                  } else {
                    const generatedGame = generateLessonQuiz(
                      selectedLesson.title,
                      selectedLesson.description,
                      selectedSubject.title
                    )
                    if (generatedGame) {
                      selectGameFromLesson(generatedGame)
                    } else if (games.length > 0) {
                      const randomGame = games[Math.floor(Math.random() * games.length)]
                      selectGameFromLesson(randomGame)
                    }
                  }
                }}
                className="px-8 py-4 text-xl font-bold 
                           bg-gradient-to-r from-purple-500 to-pink-500 
                           hover:from-purple-400 hover:to-pink-400
                           text-white rounded-2xl transition-all hover:scale-105 
                           flex items-center gap-3 shadow-xl"
              >
                🎮 Игра-тест
              </button>
              <button
                onClick={() => {
                  setCompletedLessons(new Set([...completedLessons, selectedLesson.title]))
                  completeTopic(selectedLesson.title)
                  addPoints(5)
                  selectLesson(null)
                }}
                className="px-8 py-4 text-xl font-bold 
                           bg-gradient-to-r from-green-500 to-emerald-500 
                           hover:from-green-400 hover:to-emerald-400
                           text-white rounded-2xl transition-all hover:scale-105 
                           flex items-center gap-3 shadow-xl"
              >
                ✅ Понял! +5⭐
              </button>
              <button
                onClick={() => selectLesson(null)}
                className="px-8 py-4 text-xl font-bold 
                           bg-white/20 hover:bg-white/30 
                           text-white rounded-2xl transition-all shadow-xl"
              >
                📚 Другие уроки
              </button>
            </div>
          </div>
        </div>
        
        {showPeriodicTable && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm overflow-y-auto">
            <div className="w-full max-w-7xl my-8 relative">
              <button
                onClick={() => setShowPeriodicTable(false)}
                className="absolute -top-2 -right-2 z-10 p-3 bg-red-500 hover:bg-red-600 rounded-full text-white shadow-lg"
              >
                <X className="w-6 h-6" />
              </button>
              <PeriodicTable onClose={() => setShowPeriodicTable(false)} />
            </div>
          </div>
        )}
      </div>
    )
  }

  // Если показываем игры
  if (showGames) {
    return (
      <div className="w-full animate-slideIn">
        <div className="max-w-4xl mx-auto mb-6">
          <button
            onClick={() => setShowGames(false)}
            className="flex items-center gap-2 text-white text-lg font-bold 
                       bg-white/20 hover:bg-white/30 px-5 py-3 rounded-2xl transition-all"
          >
            <ArrowLeft className="w-5 h-5" /> Назад к урокам
          </button>
        </div>

        <div className="text-center mb-10">
          <div className="text-6xl mb-4">🎮</div>
          <h2 className="text-3xl md:text-4xl font-black text-white">Игры и задания</h2>
          <p className="text-xl text-purple-200 mt-2">{games.length} игр!</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-4xl mx-auto">
          {games.map((game, index) => (
            <button
              key={index}
              onClick={() => selectGame(game)}
              className="p-6 rounded-3xl bg-gradient-to-br from-purple-600/50 to-pink-600/50 
                         border-4 border-white/20 hover:border-yellow-400
                         text-left transition-all hover:scale-[1.02] group"
            >
              <div className="flex items-center gap-4 mb-3">
                <div className="p-4 rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500">
                  <Gamepad2 className="w-8 h-8 text-white" />
                </div>
                <div>
                  <h4 className="text-xl font-bold text-white">{game.title}</h4>
                  <p className="text-lg text-purple-200">{game.tasks.length} заданий</p>
                </div>
              </div>
              <div className="flex items-center gap-2 text-yellow-400">
                <Star className="w-5 h-5 fill-yellow-400" />
                <span className="font-medium">{game.reward.stars} звёзд</span>
                <Play className="w-5 h-5 ml-auto group-hover:scale-110 transition-transform" />
              </div>
            </button>
          ))}
        </div>
      </div>
    )
  }

  // Основной вид - список тем и уроков
  return (
    <div className="w-full animate-slideIn">
      <div className="text-center mb-10">
        <div className="text-7xl md:text-8xl mb-4">{getEmoji(selectedSubject.title)}</div>
        <h2 className="text-3xl md:text-5xl font-black text-transparent bg-clip-text 
                       bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-3">
          {selectedSubject.title}
        </h2>
        <p className="text-xl text-purple-200">
          {topics.reduce((acc, t) => acc + (t.lessons?.length || 0), 0)} уроков 📚
        </p>
      </div>

      {/* Кнопка Назад слева, Игры справа */}
      <div className="flex justify-center mb-8">
        <div className="w-full max-w-4xl px-4 flex items-center gap-4">
          <button
            onClick={goBack}
            className="flex items-center gap-2 text-white text-base md:text-lg font-bold 
                       bg-white/20 hover:bg-white/30 px-4 md:px-5 py-2.5 md:py-3 rounded-2xl transition-all"
          >
            <ArrowLeft className="w-4 h-4 md:w-5 md:h-5" /> Назад
          </button>
          
          {games.length > 0 && (
            <button
              onClick={() => setShowGames(true)}
              className="px-4 md:px-5 py-2.5 md:py-3 text-base md:text-lg font-bold 
                         bg-gradient-to-r from-green-500 to-teal-500 
                         hover:from-green-400 hover:to-teal-400
                         text-white rounded-2xl transition-all hover:scale-105 
                         flex items-center gap-2"
            >
              <Gamepad2 className="w-4 h-4 md:w-5 md:h-5" />
              Игры ({games.length})
            </button>
          )}
        </div>
      </div>

      <div className="space-y-4 max-w-4xl mx-auto">
        {topics.map((topicBlock: LessonTopic, topicIndex: number) => {
          const isExpanded = selectedTopicIndex === topicIndex
          const lessonsCount = topicBlock.lessons?.length || 0
          const completedCount = topicBlock.lessons?.filter(l => completedLessons.has(l.title)).length || 0

          return (
            <div key={topicIndex} 
                 className="rounded-3xl overflow-hidden bg-gradient-to-br from-indigo-500/30 to-purple-500/30 
                            border-4 border-white/20">
              <button
                onClick={() => setSelectedTopicIndex(isExpanded ? null : topicIndex)}
                className="w-full px-6 py-5 flex items-center justify-between text-left
                           hover:bg-white/5 transition-colors"
              >
                <div className="flex items-center gap-4">
                  <div className="w-14 h-14 rounded-2xl 
                                  bg-gradient-to-br from-yellow-400 to-orange-500 
                                  flex items-center justify-center text-white font-black text-2xl shadow-lg">
                    {topicIndex + 1}
                  </div>
                  <div>
                    <span className="text-xl md:text-2xl font-bold text-white">{topicBlock.topic}</span>
                    <div className="text-base text-purple-300">
                      {completedCount > 0 ? (
                        <span className="text-green-400">✓ {completedCount}/{lessonsCount}</span>
                      ) : (
                        <span>{lessonsCount} уроков</span>
                      )}
                    </div>
                  </div>
                </div>
                {isExpanded ? (
                  <ChevronDown className="w-7 h-7 text-yellow-400" />
                ) : (
                  <ChevronRight className="w-7 h-7 text-yellow-400" />
                )}
              </button>

              {isExpanded && topicBlock.lessons && (
                <div className="px-6 pb-6 space-y-3 bg-black/20">
                  {topicBlock.lessons.map((lesson, lessonIndex) => {
                    const isCompleted = completedLessons.has(lesson.title)
                    
                    return (
                      <button
                        key={lessonIndex}
                        onClick={() => selectLesson(lesson)}
                        className={`w-full p-5 rounded-2xl text-left transition-all hover:scale-[1.01]
                                   ${isCompleted 
                                     ? 'bg-green-500/20 border-2 border-green-400/40'
                                     : 'bg-white/5 border-2 border-white/10 hover:border-pink-400/40'
                                   }`}
                      >
                        <div className="flex items-center gap-4">
                          <div className={`w-12 h-12 rounded-xl flex items-center justify-center text-2xl
                                          ${isCompleted ? 'bg-green-500' : 'bg-gradient-to-br from-purple-400 to-pink-400'}`}>
                            {isCompleted ? '✅' : '📖'}
                          </div>
                          <div className="flex-1 min-w-0">
                            <h4 className="text-lg font-bold text-white truncate">{lesson.title}</h4>
                            <p className="text-sm text-purple-300 truncate">
                              {String(lesson.description || '').substring(0, 50)}...
                            </p>
                          </div>
                          <div className="text-yellow-400 font-bold flex items-center gap-1">
                            <Star className="w-5 h-5 fill-yellow-400" />
                            <span>+10</span>
                          </div>
                        </div>
                      </button>
                    )
                  })}
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
