'use client'

import { useState, useRef, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { useSchool } from '@/context/SchoolContext'
import { X, Trophy, Star, Zap, Flame, Sparkles, Home, RotateCcw, ChevronUp } from 'lucide-react'
import { allAchievements, allStickers, Achievement, Sticker, rarityColors } from './rightMenu/constants'
import { getIcon } from './rightMenu/utils'
import AchievementsTab from './rightMenu/AchievementsTab'
import GamesTab from './rightMenu/GamesTab'

export default function RightSideMenu() {
  const { progress, setView, selectedClass, totalPoints, totalStars, streak, resetProgress, addPoints } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [activeTab, setActiveTab] = useState<'achievements' | 'actions' | 'games' | 'stickers'>('achievements')
  const [showResetConfirm, setShowResetConfirm] = useState(false)
  const [newAchievement, setNewAchievement] = useState<Achievement | null>(null)
  const prevAchievementsRef = useRef<string[]>(progress.achievements)
  const [selectedGame, setSelectedGame] = useState<'math' | 'memory' | null>(null)
  const [finalScore, setFinalScore] = useState<number | null>(null)
  const [stickers, setStickers] = useState<Sticker[]>(() => {
    if (typeof window === 'undefined') return []
    const saved = localStorage.getItem('stickerAlbum')
    return saved ? JSON.parse(saved) : allStickers
  })
  const [stickerFilter, setStickerFilter] = useState<'all' | 'unlocked' | 'locked'>('all')

  const unlockedCount = allAchievements.filter(a => a.condition(progress)).length
  const totalCount = allAchievements.length

  // Achievement notification
  useEffect(() => {
    const prevCount = prevAchievementsRef.current.length
    const currentCount = progress.achievements.length
    if (currentCount > prevCount) {
      const newId = progress.achievements.find(id => !prevAchievementsRef.current.includes(id))
      if (newId) {
        const achievement = allAchievements.find(a => a.id === newId)
        if (achievement) {
          setNewAchievement(achievement)
          setTimeout(() => setNewAchievement(null), 3000)
        }
      }
    }
    prevAchievementsRef.current = progress.achievements
  }, [progress.achievements])

  // Update stickers based on progress
  useEffect(() => {
    const updated = stickers.map(s => {
      if (s.unlocked) return s
      let shouldUnlock = false
      if (s.id === 's9' && totalStars >= 50) shouldUnlock = true
      if (s.id === 's10' && streak >= 7) shouldUnlock = true
      if (s.id === 's18' && totalStars >= 1000) shouldUnlock = true
      return shouldUnlock ? { ...s, unlocked: true } : s
    })
    if (JSON.stringify(updated) !== JSON.stringify(stickers)) {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setStickers(updated)
      localStorage.setItem('stickerAlbum', JSON.stringify(updated))
    }
  }, [totalStars, streak, stickers])

  const handleReset = () => {
    resetProgress()
    setShowResetConfirm(false)
    setIsOpen(false)
    setView('classes')
  }

  const quickActions = [
    { id: 'home', label: 'Главная', icon: <Home className="w-5 h-5" />, color: 'from-blue-500 to-cyan-500', action: () => { setView('classes'); setIsOpen(false) } },
    { id: 'lessons', label: 'Уроки', icon: <Star className="w-5 h-5" />, color: 'from-green-500 to-emerald-500', action: () => { if (selectedClass !== null) { setView('subjects'); setIsOpen(false) } } },
    { id: 'games', label: 'Игры', icon: <Trophy className="w-5 h-5" />, color: 'from-purple-500 to-pink-500', action: () => { if (selectedClass !== null) { setView('games'); setIsOpen(false) } } },
    { id: 'reset', label: 'Сброс', icon: <RotateCcw className="w-5 h-5" />, color: 'from-red-500 to-rose-500', action: () => setShowResetConfirm(true) },
  ]

  const unlockedStickers = stickers.filter(s => s.unlocked).length
  const filteredStickers = stickers.filter(s => {
    if (stickerFilter === 'unlocked') return s.unlocked
    if (stickerFilter === 'locked') return !s.unlocked
    return true
  })

  return (
    <>
      {/* Floating button */}
      <motion.button initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }}
        onClick={() => setIsOpen(true)}
        className="fixed right-4 bottom-4 z-40 p-4 rounded-full bg-gradient-to-br from-yellow-400 to-orange-500 shadow-xl shadow-orange-500/30 hover:shadow-2xl hover:shadow-orange-500/40 transition-all">
        <Trophy className="w-6 h-6 text-purple-900" />
        <span className="absolute -top-1 -right-1 px-2 py-0.5 bg-purple-600 text-white rounded-full text-xs font-bold">{unlockedCount}/{totalCount}</span>
      </motion.button>

      {/* Achievement notification */}
      {newAchievement && (
        <motion.div initial={{ y: -50, opacity: 0 }} animate={{ y: 0, opacity: 1 }} className="fixed top-6 left-1/2 -translate-x-1/2 z-50">
          <div className="px-6 py-3 rounded-2xl bg-gradient-to-r from-yellow-400 to-orange-500 shadow-2xl flex items-center gap-3 text-purple-900">
            {getIcon(newAchievement.icon)}
            <div><p className="font-bold">{newAchievement.name}</p><p className="text-sm opacity-80">{newAchievement.desc}</p></div>
            <Sparkles className="w-5 h-5 animate-pulse" />
          </div>
        </motion.div>
      )}

      {/* Modal */}
      <AnimatePresence>
        {isOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="w-full max-w-lg max-h-[90vh] overflow-hidden bg-gradient-to-br from-gray-900 to-orange-900 rounded-3xl border-2 border-orange-500/30 shadow-2xl">
              
              {/* Header */}
              <div className="bg-gradient-to-r from-yellow-500 to-orange-500 p-3">
                <div className="flex justify-between items-center mb-3">
                  <h2 className="text-lg font-black text-purple-900 flex items-center gap-2"><Trophy className="w-5 h-5" />Меню</h2>
                  <button onClick={() => setIsOpen(false)} className="p-1.5 rounded-xl hover:bg-white/20"><X className="w-5 h-5 text-purple-900" /></button>
                </div>
                <div className="flex items-center justify-center gap-6 py-2 mb-2 bg-white/20 rounded-xl">
                  <div className="flex items-center gap-1 text-purple-900"><Star className="w-5 h-5" /><span className="font-bold">{totalStars}</span></div>
                  <div className="flex items-center gap-1 text-purple-900"><Flame className="w-5 h-5" /><span className="font-bold">{streak}</span></div>
                  <div className="flex items-center gap-1 text-purple-900"><Zap className="w-5 h-5" /><span className="font-bold">{totalPoints}</span></div>
                </div>
                <div className="flex gap-1 overflow-x-auto pb-1">
                  {[
                    { id: 'achievements', label: '🏆 Достижения' },
                    { id: 'stickers', label: '✨ Наклейки' },
                    { id: 'games', label: '🎮 Мини-игры' },
                    { id: 'actions', label: '⚡ Действия' },
                  ].map(tab => (
                    <button key={tab.id} onClick={() => { setActiveTab(tab.id as typeof activeTab); setSelectedGame(null); setFinalScore(null); }}
                      className={`relative px-3 py-1.5 rounded-lg font-medium text-xs transition-all whitespace-nowrap ${activeTab === tab.id ? 'bg-white text-orange-600' : 'bg-white/20 text-purple-900 hover:bg-white/30'}`}>
                      {tab.label}
                    </button>
                  ))}
                </div>
              </div>

              {/* Content */}
              <div className="overflow-y-auto max-h-[65vh]">
                {activeTab === 'achievements' && <AchievementsTab progress={progress} />}
                
                {activeTab === 'stickers' && (
                  <div className="p-4">
                    <div className="flex justify-between items-center mb-3">
                      <p className="text-orange-300 text-sm">{unlockedStickers} из {stickers.length} собрано</p>
                      <div className="flex gap-1">
                        {['all', 'unlocked', 'locked'].map(f => (
                          <button key={f} onClick={() => setStickerFilter(f as typeof stickerFilter)}
                            className={`px-2 py-1 rounded-lg text-xs font-medium ${stickerFilter === f ? 'bg-yellow-500 text-white' : 'bg-white/10 text-white/50'}`}>
                            {f === 'all' ? 'Все' : f === 'unlocked' ? 'Собраны' : 'Нет'}
                          </button>
                        ))}
                      </div>
                    </div>
                    <div className="grid grid-cols-4 gap-2">
                      {filteredStickers.map(sticker => {
                        const colors = rarityColors[sticker.rarity]
                        return (
                          <div key={sticker.id} className={`aspect-square rounded-xl p-2 flex flex-col items-center justify-center ${sticker.unlocked ? `bg-gradient-to-br ${colors.bg} ${colors.glow} shadow-lg` : 'bg-white/5 border border-white/10'}`}>
                            {sticker.unlocked ? (
                              <><span className="text-2xl">{sticker.emoji}</span><span className="text-[8px] text-white/80 text-center mt-1">{sticker.name}</span></>
                            ) : <span className="text-white/20">🔒</span>}
                          </div>
                        )
                      })}
                    </div>
                  </div>
                )}

                {activeTab === 'games' && <GamesTab selectedGame={selectedGame} setSelectedGame={setSelectedGame} finalScore={finalScore} setFinalScore={setFinalScore} addPoints={addPoints} onClose={() => setIsOpen(false)} />}
                
                {activeTab === 'actions' && (
                  <div className="p-4">
                    <div className="grid grid-cols-2 gap-2">
                      {quickActions.map(action => (
                        <button key={action.id} onClick={action.action}
                          className={`p-3 rounded-xl bg-gradient-to-br ${action.color} text-white font-medium flex flex-col items-center gap-2 shadow-lg`}>
                          {action.icon}<span className="text-sm">{action.label}</span>
                        </button>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Reset confirmation */}
      <AnimatePresence>
        {showResetConfirm && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setShowResetConfirm(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1 }}
              className="bg-slate-900 rounded-2xl p-6 max-w-sm w-full border border-white/10 shadow-xl">
              <div className="text-center">
                <div className="w-16 h-16 bg-red-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
                  <RotateCcw className="w-8 h-8 text-red-400" />
                </div>
                <h3 className="text-xl font-bold text-white mb-2">Сбросить прогресс?</h3>
                <p className="text-white/60 mb-6 text-sm">Все достижения, звёзды и очки будут удалены.</p>
                <div className="flex gap-3">
                  <button onClick={() => setShowResetConfirm(false)} className="flex-1 py-2 bg-white/10 text-white rounded-xl">Отмена</button>
                  <button onClick={handleReset} className="flex-1 py-2 bg-red-500 text-white rounded-xl">Сбросить</button>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Scroll to top */}
      <motion.button initial={{ opacity: 0 }} animate={{ opacity: isOpen ? 0 : 1 }} whileHover={{ scale: 1.1 }}
        onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
        className="fixed right-4 bottom-20 z-30 p-3 rounded-full bg-white/10 hover:bg-white/20 text-white/50 hover:text-white transition-colors">
        <ChevronUp className="w-5 h-5" />
      </motion.button>
    </>
  )
}
