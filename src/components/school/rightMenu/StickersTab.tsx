'use client'

import { Lock } from 'lucide-react'
import { Sticker, rarityColors } from './constants'

interface StickersTabProps {
  stickers: Sticker[]
  stickerFilter: 'all' | 'unlocked' | 'locked'
  setStickerFilter: (f: 'all' | 'unlocked' | 'locked') => void
}

export default function StickersTab({ stickers, stickerFilter, setStickerFilter }: StickersTabProps) {
  const unlockedStickers = stickers.filter(s => s.unlocked).length
  const filteredStickers = stickers.filter(s => {
    if (stickerFilter === 'unlocked') return s.unlocked
    if (stickerFilter === 'locked') return !s.unlocked
    return true
  })

  return (
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
                <>
                  <span className="text-2xl">{sticker.emoji}</span>
                  <span className="text-[8px] text-white/80 text-center mt-1">{sticker.name}</span>
                </>
              ) : (
                <Lock className="w-5 h-5 text-white/20" />
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
