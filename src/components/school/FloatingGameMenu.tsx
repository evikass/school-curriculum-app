'use client'

import { useState } from 'react'
import { Gamepad2, X, Zap } from 'lucide-react'

interface GameButton {
  id: string
  icon: React.ReactNode
  label: string
  color: string
}

const GAME_BUTTONS: GameButton[] = [
  { id: 'flashcards', icon: '📚', label: 'Карточки', color: 'teal' },
  { id: 'speedtest', icon: '⚡', label: 'Спид', color: 'yellow' },
  { id: 'typing', icon: '✏️', label: 'Печать', color: 'slate' },
  { id: 'spelling', icon: '📝', label: 'Орфо', color: 'pink' },
  { id: 'puzzle', icon: '🧮', label: 'Голов.', color: 'emerald' },
  { id: 'scramble', icon: '🔀', label: 'Слова', color: 'teal' },
  { id: 'racing', icon: '🏎️', label: 'Гонка', color: 'orange' },
  { id: 'trivia', icon: '⚔️', label: 'Битва', color: 'indigo' },
  { id: 'crossword', icon: '🔲', label: 'Кросс', color: 'blue' },
  { id: 'sentence', icon: '💬', label: 'Предл', color: 'emerald' },
  { id: 'colormatch', icon: '🎨', label: 'Цвета', color: 'pink' },
  { id: 'wordsearch', icon: '🔍', label: 'Поиск', color: 'cyan' },
  { id: 'sequence', icon: '🔢', label: 'Ряд', color: 'violet' },
  { id: 'emoji', icon: '😊', label: 'Эмодзи', color: 'amber' },
  { id: 'geography', icon: '🌍', label: 'Гео', color: 'emerald' },
  { id: 'hangman', icon: '🎮', label: 'Висел', color: 'slate' },
  { id: 'truefalse', icon: '✅', label: 'П/Л', color: 'rose' },
  { id: 'anagram', icon: '🔄', label: 'Анагр', color: 'fuchsia' },
  { id: 'oddoneout', icon: '🎯', label: 'Лишн', color: 'sky' },
  { id: 'soundquiz', icon: '🔊', label: 'Звук', color: 'orange' },
  { id: 'mathpuzzle', icon: '🧩', label: 'Гол', color: 'indigo' },
  { id: 'wordchain', icon: '🔗', label: 'Цепь', color: 'green' },
  { id: 'quickmath', icon: '⚡', label: 'Быстр', color: 'amber' },
  { id: 'multiply', icon: '✖️', label: 'ТабУ', color: 'blue' },
  { id: 'divide', icon: '➗', label: 'ТабД', color: 'emerald' },
  { id: 'alphabetsort', icon: '🔤', label: 'А-Я', color: 'teal' },
  { id: 'synonym', icon: '↔️', label: 'Син', color: 'purple' },
  { id: 'antonyms', icon: '↔️', label: 'Антон', color: 'fuchsia' },
  { id: 'homonyms', icon: '📖', label: 'Омон', color: 'orange' },
  { id: 'flags', icon: '🚩', label: 'Флаг', color: 'blue' },
  { id: 'timequiz', icon: '⏰', label: 'Часы', color: 'amber' },
  { id: 'riddles', icon: '❓', label: 'Загад', color: 'violet' },
  { id: 'proverbs', icon: '📜', label: 'Посл', color: 'rose' },
  { id: 'punctuation', icon: '✍️', label: 'Знак', color: 'cyan' },
  { id: 'capitals', icon: '🏛️', label: 'Стол', color: 'emerald' },
  { id: 'roman', icon: 'rome', label: 'Рим', color: 'stone' },
  { id: 'fraction', icon: '➗', label: 'Дроб', color: 'indigo' },
  { id: 'percent', icon: '%', label: '%', color: 'orange' },
  { id: 'geometry', icon: '📐', label: 'Фиг', color: 'lime' },
  { id: 'nature', icon: '🌿', label: 'Прир', color: 'green' },
  { id: 'history', icon: '📜', label: 'Ист', color: 'amber' },
  { id: 'science', icon: '🔬', label: 'Наук', color: 'violet' },
  { id: 'measurement', icon: '📏', label: 'Измер', color: 'teal' },
  { id: 'equation', icon: '📊', label: 'Урав', color: 'indigo' },
  { id: 'parts', icon: '📖', label: 'ЧРеч', color: 'rose' },
  { id: 'wordform', icon: '🧩', label: 'Сост', color: 'amber' },
  { id: 'syllables', icon: '🎵', label: 'Слог', color: 'cyan' },
  { id: 'stress', icon: '📢', label: 'Удар', color: 'red' },
  { id: 'cases', icon: '📋', label: 'Падеж', color: 'violet' },
  { id: 'conjugations', icon: '✍️', label: 'Спряг', color: 'pink' },
  { id: 'compare', icon: '⚖️', label: 'Сравн', color: 'sky' },
  { id: 'abbr', icon: '📝', label: 'Аббр', color: 'amber' },
  { id: 'prime', icon: '🔢', label: 'Прост', color: 'violet' },
  { id: 'vowels', icon: '🔤', label: 'Гл/Сог', color: 'pink' },
  { id: 'zhishi', icon: '✏️', label: 'ЖИ-ШИ', color: 'green' },
  { id: 'days', icon: '📅', label: 'Дни', color: 'amber' },
  { id: 'evenodd', icon: '🔢', label: 'Чёт', color: 'cyan' },
  { id: 'shapes', icon: '⬡', label: 'Фигуры', color: 'rose' },
  { id: 'simplemath', icon: '➕', label: '+/-', color: 'emerald' },
  { id: 'counting', icon: '🔵', label: 'Счёт', color: 'yellow' },
  { id: 'animals', icon: '🐾', label: 'Живот', color: 'green' },
  { id: 'professions', icon: '💼', label: 'Проф', color: 'indigo' },
  { id: 'periodic', icon: '⚗️', label: 'Химия', color: 'cyan' },
  { id: 'physics', icon: '⚛️', label: 'Физ', color: 'violet' },
  { id: 'chemistry', icon: '🧪', label: 'Хим', color: 'lime' },
  { id: 'biology', icon: '🧬', label: 'Био', color: 'green' },
  { id: 'astronomy', icon: '🌟', label: 'Космос', color: 'indigo' },
  { id: 'logic', icon: '🧠', label: 'Логика', color: 'purple' },
  { id: 'wordprob', icon: '📄', label: 'Задачи', color: 'amber' },
  { id: 'reading', icon: '📕', label: 'Чтение', color: 'teal' },
  { id: 'challenge', icon: '⏱️', label: 'Челлендж', color: 'red' },
  { id: 'memory', icon: '🧠', label: 'Память', color: 'purple' },
  { id: 'daily', icon: '🎁', label: 'Ежедн', color: 'amber' },
  { id: 'stats', icon: '📊', label: 'Стат', color: 'blue' },
]

const COLOR_MAP: Record<string, string> = {
  teal: 'bg-teal-500/20 hover:bg-teal-500/40 text-teal-300',
  yellow: 'bg-yellow-500/20 hover:bg-yellow-500/40 text-yellow-300',
  slate: 'bg-slate-500/20 hover:bg-slate-500/40 text-slate-300',
  pink: 'bg-pink-500/20 hover:bg-pink-500/40 text-pink-300',
  emerald: 'bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-300',
  orange: 'bg-orange-500/20 hover:bg-orange-500/40 text-orange-300',
  indigo: 'bg-indigo-500/20 hover:bg-indigo-500/40 text-indigo-300',
  blue: 'bg-blue-500/20 hover:bg-blue-500/40 text-blue-300',
  cyan: 'bg-cyan-500/20 hover:bg-cyan-500/40 text-cyan-300',
  violet: 'bg-violet-500/20 hover:bg-violet-500/40 text-violet-300',
  amber: 'bg-amber-500/20 hover:bg-amber-500/40 text-amber-300',
  rose: 'bg-rose-500/20 hover:bg-rose-500/40 text-rose-300',
  fuchsia: 'bg-fuchsia-500/20 hover:bg-fuchsia-500/40 text-fuchsia-300',
  sky: 'bg-sky-500/20 hover:bg-sky-500/40 text-sky-300',
  green: 'bg-green-500/20 hover:bg-green-500/40 text-green-300',
  purple: 'bg-purple-500/20 hover:bg-purple-500/40 text-purple-300',
  lime: 'bg-lime-500/20 hover:bg-lime-500/40 text-lime-300',
  red: 'bg-red-500/20 hover:bg-red-500/40 text-red-300',
  stone: 'bg-stone-500/20 hover:bg-stone-500/40 text-stone-300',
}

interface FloatingGameMenuProps {
  activeGame: string | null
  onSelectGame: (gameId: string | null) => void
}

export default function FloatingGameMenu({ activeGame, onSelectGame }: FloatingGameMenuProps) {
  const [isOpen, setIsOpen] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')

  const filteredGames = GAME_BUTTONS.filter(game => 
    game.label.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <>
      {/* Floating button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={`fixed right-4 bottom-4 z-50 w-14 h-14 rounded-full shadow-2xl 
                    flex items-center justify-center transition-all duration-300
                    ${isOpen 
                      ? 'bg-red-500 hover:bg-red-600 rotate-90' 
                      : 'bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600'
                    }
                    ${activeGame ? 'ring-4 ring-yellow-400/50 animate-pulse' : ''}`}
      >
        {isOpen ? (
          <X className="w-7 h-7 text-white" />
        ) : (
          <Gamepad2 className="w-7 h-7 text-white" />
        )}
      </button>

      {/* Menu panel */}
      {isOpen && (
        <div className="fixed right-4 bottom-20 z-40 w-80 max-h-[70vh] 
                        bg-gray-900/95 backdrop-blur-xl rounded-2xl shadow-2xl
                        border border-white/10 overflow-hidden animate-slideIn">
          {/* Header */}
          <div className="p-4 border-b border-white/10">
            <h3 className="text-lg font-bold text-white flex items-center gap-2">
              <Zap className="w-5 h-5 text-yellow-400" />
              Мини-игры
            </h3>
            {/* Search */}
            <input
              type="text"
              placeholder="Поиск..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="mt-2 w-full px-3 py-2 bg-white/10 rounded-xl text-white text-sm
                         placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-purple-500"
            />
          </div>

          {/* Games grid */}
          <div className="p-3 overflow-y-auto max-h-[calc(70vh-100px)]">
            <div className="grid grid-cols-3 gap-2">
              {filteredGames.map((game) => (
                <button
                  key={game.id}
                  onClick={() => {
                    onSelectGame(activeGame === game.id ? null : game.id)
                    setIsOpen(false)
                  }}
                  className={`p-2 rounded-xl text-xs font-medium transition-all
                              flex flex-col items-center gap-1 min-h-[60px]
                              ${activeGame === game.id 
                                ? 'bg-white/30 ring-2 ring-yellow-400' 
                                : COLOR_MAP[game.color] || 'bg-white/10 hover:bg-white/20 text-white'
                              }`}
                >
                  <span className="text-lg">{game.icon}</span>
                  <span className="text-white/90 leading-tight text-center">{game.label}</span>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Active game indicator */}
      {activeGame && !isOpen && (
        <div className="fixed right-4 bottom-20 z-40 px-3 py-2 
                        bg-gray-900/90 backdrop-blur rounded-xl shadow-lg
                        text-white text-sm flex items-center gap-2">
          <span className="text-green-400">●</span>
          Игра активна
          <button
            onClick={() => onSelectGame(null)}
            className="ml-2 text-red-400 hover:text-red-300"
          >
            ✕
          </button>
        </div>
      )}
    </>
  )
}
