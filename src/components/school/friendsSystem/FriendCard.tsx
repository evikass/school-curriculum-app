'use client'

import { motion } from 'framer-motion'
import { Star, Trophy, Flame, Gift, MessageCircle } from 'lucide-react'
import { Friend } from './types'

interface FriendCardProps {
  friend: Friend
  index: number
  hasSentGift: boolean
  onSendGift: (id: string) => void
}

export function FriendCard({ friend, index, hasSentGift, onSendGift }: FriendCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.05 }}
      className="bg-white/5 rounded-xl p-3"
    >
      <div className="flex items-center gap-3">
        <div className="relative">
          <span className="text-2xl">{friend.avatar}</span>
          {friend.isOnline && (
            <span className="absolute bottom-0 right-0 w-3 h-3 bg-green-500 rounded-full border-2 border-slate-800" />
          )}
        </div>
        <div className="flex-1">
          <div className="flex items-center gap-2">
            <p className="text-white font-medium">{friend.name}</p>
            <span className="text-white/30 text-xs">{friend.grade} кл</span>
          </div>
          <div className="flex items-center gap-3 text-xs">
            <span className="text-yellow-400 flex items-center gap-1">
              <Star className="w-3 h-3" /> {friend.stars}
            </span>
            <span className="text-purple-400">{friend.points} XP</span>
            <span className="text-white/30">{friend.lastActive}</span>
          </div>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => onSendGift(friend.id)}
            disabled={hasSentGift}
            className={`p-2 rounded-lg transition-colors
              ${hasSentGift ? 'bg-white/5 text-white/20' : 'bg-pink-500/20 text-pink-400 hover:bg-pink-500/30'}`}
          >
            <Gift className="w-4 h-4" />
          </button>
          <button className="p-2 bg-blue-500/20 text-blue-400 hover:bg-blue-500/30 rounded-lg">
            <MessageCircle className="w-4 h-4" />
          </button>
        </div>
      </div>
    </motion.div>
  )
}
