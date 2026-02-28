'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Sparkles, X, Lock, CheckCircle, Star, Crown } from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'
import { Sticker, allStickers, rarityColors, rarityLabels } from './stickerAlbum/data'

const glowStyles = {
  common: 'shadow-gray-500/30',
  rare: 'shadow-blue-500/30',
  epic: 'shadow-purple-500/30',
  legendary: 'shadow-yellow-500/50'
}

const bgStyles = {
  common: 'from-gray-500 to-gray-600',
  rare: 'from-blue-500 to-cyan-500',
  epic: 'from-purple-500 to-pink-500',
  legendary: 'from-yellow-400 to-orange-500'
}

export default function StickerAlbum() {
  const { totalStars, streak } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [stickers, setStickers] = useState<Sticker[]>(() => {
    if (typeof window === 'undefined') return []
    const saved = localStorage.getItem('stickerAlbum')
    return saved ? JSON.parse(saved) : allStickers
  })
  const [selectedSticker, setSelectedSticker] = useState<Sticker | null>(null)
  const [filter, setFilter] = useState<'all' | 'unlocked' | 'locked'>('all')

  useEffect(() => {
    const updated = stickers.map(s => {
      if (s.unlocked) return s
      let shouldUnlock = false
      if (s.id === 's9' && totalStars >= 50) shouldUnlock = true
      if (s.id === 's10' && streak >= 7) shouldUnlock = true
      if (s.id === 's15' && streak >= 30) shouldUnlock = true
      if (s.id === 's18' && totalStars >= 1000) shouldUnlock = true
      if (s.id === 's20' && streak >= 100) shouldUnlock = true
      return shouldUnlock ? { ...s, unlocked: true, unlockedAt: new Date().toISOString() } : s
    })
    if (JSON.stringify(updated) !== JSON.stringify(stickers)) {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setStickers(updated)
      localStorage.setItem('stickerAlbum', JSON.stringify(updated))
    }
  }, [totalStars, streak, stickers])

  const filteredStickers = stickers.filter(s => filter === 'unlocked' ? s.unlocked : filter === 'locked' ? !s.unlocked : true)
  const unlockedCount = stickers.filter(s => s.unlocked).length
  const progress = (unlockedCount / stickers.length) * 100
  const rarityOrder = { legendary: 0, epic: 1, rare: 2, common: 3 }
  const sortedStickers = [...filteredStickers].sort((a, b) => a.unlocked !== b.unlocked ? (a.unlocked ? -1 : 1) : rarityOrder[a.rarity] - rarityOrder[b.rarity])

  return (
    <>
      {!isOpen && (
        <motion.button initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}
          onClick={() => setIsOpen(true)}
          className="fixed left-4 bottom-20 z-40 bg-gradient-to-r from-amber-500 to-yellow-500 p-4 rounded-full shadow-lg shadow-amber-500/30 border-2 border-white/20 group">
          <Sparkles className="w-6 h-6 text-white" />
          <span className="absolute -right-2 -top-2 bg-purple-500 text-white text-xs font-bold px-2 py-1 rounded-full">{unlockedCount}/{stickers.length}</span>
          <span className="absolute left-full ml-3 bg-gray-900/90 text-white px-3 py-2 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity">Альбом наклеек</span>
        </motion.button>
      )}

      <AnimatePresence>
        {isOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="bg-gradient-to-br from-amber-900 to-orange-900 rounded-3xl max-w-lg w-full max-h-[85vh] overflow-hidden shadow-2xl border-2 border-white/10 flex flex-col">

            {/* Header */}
            <div className="p-4 border-b border-white/10">
              <div className="flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-yellow-500/30 rounded-xl"><Sparkles className="w-6 h-6 text-yellow-300" /></div>
                  <div>
                    <h3 className="text-xl font-bold text-white">Альбом наклеек</h3>
                    <p className="text-yellow-300 text-sm">{unlockedCount} из {stickers.length} собрано</p>
                  </div>
                </div>
                <button onClick={() => setIsOpen(false)} className="text-white/50 hover:text-white"><X className="w-6 h-6" /></button>
              </div>
              <div className="mt-3 h-3 bg-white/10 rounded-full overflow-hidden">
                <motion.div className="h-full bg-gradient-to-r from-yellow-400 to-orange-500" initial={{ width: 0 }} animate={{ width: `${progress}%` }} />
              </div>
              <div className="flex gap-2 mt-3">
                {[{ id: 'all', label: 'Все' }, { id: 'unlocked', label: 'Собраны' }, { id: 'locked', label: 'Не собраны' }].map(f => (
                  <button key={f.id} onClick={() => setFilter(f.id as typeof filter)}
                    className={`px-4 py-1.5 rounded-xl text-sm font-medium transition-all ${filter === f.id ? 'bg-yellow-500 text-white' : 'bg-white/10 text-white/50 hover:bg-white/20'}`}>{f.label}</button>
                ))}
              </div>
            </div>

            {/* Stickers grid */}
            <div className="flex-1 overflow-y-auto p-4">
              <div className="grid grid-cols-4 gap-3">
                {sortedStickers.map((sticker, idx) => (
                  <motion.button key={sticker.id} initial={{ opacity: 0, scale: 0.5 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: idx * 0.02 }}
                    onClick={() => sticker.unlocked && setSelectedSticker(sticker)} disabled={!sticker.unlocked}
                    className={`aspect-square rounded-2xl p-3 flex flex-col items-center justify-center transition-all relative overflow-hidden
                      ${sticker.unlocked ? `bg-gradient-to-br ${bgStyles[sticker.rarity]} ${glowStyles[sticker.rarity]} shadow-lg cursor-pointer hover:scale-105` : 'bg-white/5 border border-white/10 cursor-not-allowed'}`}>
                    {sticker.unlocked ? (
                      <>
                        <span className="text-3xl mb-1">{sticker.emoji}</span>
                        <span className="text-[10px] text-white/80 font-medium text-center line-clamp-1">{sticker.name}</span>
                        <div className={`absolute top-1 right-1 w-2 h-2 rounded-full ${sticker.rarity === 'legendary' ? 'bg-yellow-300 animate-pulse' : sticker.rarity === 'epic' ? 'bg-purple-300' : sticker.rarity === 'rare' ? 'bg-blue-300' : 'bg-gray-300'}`} />
                      </>
                    ) : <Lock className="w-6 h-6 text-white/20" />}
                  </motion.button>
                ))}
              </div>
            </div>

            {/* Legend */}
            <div className="p-3 border-t border-white/10 flex justify-center gap-4">
              {Object.entries(rarityLabels).map(([rarity, label]) => (
                <div key={rarity} className="flex items-center gap-1.5">
                  <div className={`w-3 h-3 rounded-full bg-gradient-to-br ${bgStyles[rarity as keyof typeof bgStyles]}`} />
                  <span className="text-xs text-white/50">{label}</span>
                </div>
              ))}
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>

    {/* Sticker detail */}
    <AnimatePresence>
      {selectedSticker && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
          className="fixed inset-0 z-60 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm" onClick={() => setSelectedSticker(null)}>
          <motion.div initial={{ scale: 0.5, rotate: -10 }} animate={{ scale: 1, rotate: 0 }} exit={{ scale: 0.5, rotate: 10 }}
            className={`p-8 rounded-3xl text-center bg-gradient-to-br ${bgStyles[selectedSticker.rarity]} shadow-2xl ${glowStyles[selectedSticker.rarity]}`}>
            <motion.div animate={{ y: [0, -10, 0] }} transition={{ duration: 2, repeat: Infinity }}>
              <span className="text-8xl block mb-4">{selectedSticker.emoji}</span>
            </motion.div>
            <h4 className="text-2xl font-bold text-white mb-2">{selectedSticker.name}</h4>
            <p className="text-white/80 mb-3">{selectedSticker.description}</p>
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/20 text-white text-sm font-medium">
              {selectedSticker.rarity === 'legendary' && <Crown className="w-4 h-4" />}
              {selectedSticker.rarity === 'epic' && <Star className="w-4 h-4" />}
              {selectedSticker.rarity === 'rare' && <Sparkles className="w-4 h-4" />}
              {selectedSticker.rarity === 'common' && <CheckCircle className="w-4 h-4" />}
              {rarityLabels[selectedSticker.rarity]}
            </div>
            {selectedSticker.unlockedAt && <p className="text-white/50 text-sm mt-3">Получено: {new Date(selectedSticker.unlockedAt).toLocaleDateString('ru-RU')}</p>}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
    </>
  )
}
