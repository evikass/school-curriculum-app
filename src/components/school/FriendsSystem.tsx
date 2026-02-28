'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Users, X, Crown, Star, Trophy, Flame } from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'
import { useFriends, FriendCard, SearchTab, RequestsTab } from './friendsSystem'

export default function FriendsSystem() {
  const { totalPoints, totalStars, streak, selectedClass } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [activeTab, setActiveTab] = useState<'friends' | 'search' | 'requests'>('friends')

  const { friends, sentGifts, ranking, myRank, sendGift, addFriend } = useFriends(totalPoints, totalStars, streak, selectedClass)

  return (
    <>
      {/* Open button */}
      {!isOpen && (
        <motion.button
          initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}
          onClick={() => setIsOpen(true)}
          className="fixed right-4 top-1/2 translate-y-16 z-40 bg-gradient-to-r from-pink-500 to-rose-500 p-4 rounded-full shadow-lg shadow-pink-500/30 border-2 border-white/20 group"
        >
          <Users className="w-6 h-6 text-white" />
          <span className="absolute -right-2 -top-2 bg-green-400 text-green-900 text-xs font-bold px-2 py-1 rounded-full">
            {friends.filter(f => f.isOnline).length}
          </span>
          <span className="absolute right-full mr-3 bg-gray-900/90 text-white px-3 py-2 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity">
            Друзья • #{myRank} в рейтинге
          </span>
        </motion.button>
      )}

      {/* Modal */}
      <AnimatePresence>
        {isOpen && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}>
            <motion.div initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="bg-gradient-to-br from-slate-900 to-slate-800 rounded-3xl max-w-md w-full max-h-[85vh] overflow-hidden shadow-2xl border-2 border-white/10 flex flex-col">

            {/* Header */}
            <div className="p-4 border-b border-white/10">
              <div className="flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-pink-500/30 rounded-xl">
                    <Users className="w-5 h-5 text-pink-300" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-white">Друзья</h3>
                    <p className="text-pink-300 text-sm">Твой рейтинг: #{myRank}</p>
                  </div>
                </div>
                <button onClick={() => setIsOpen(false)} className="text-white/50 hover:text-white">
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Tabs */}
              <div className="flex gap-2 mt-3">
                {[
                  { id: 'friends' as const, label: 'Друзья', count: friends.length },
                  { id: 'search' as const, label: 'Поиск' },
                  { id: 'requests' as const, label: 'Заявки', count: 2 }
                ].map(tab => (
                  <button key={tab.id} onClick={() => setActiveTab(tab.id)}
                    className={`flex-1 py-2 px-3 rounded-xl font-medium transition-all flex items-center justify-center gap-1 text-sm
                      ${activeTab === tab.id ? 'bg-pink-500 text-white' : 'bg-white/5 text-white/50 hover:bg-white/10'}`}>
                    {tab.label}
                    {tab.count !== undefined && (
                      <span className="bg-white/20 px-1.5 py-0.5 rounded-full text-xs">{tab.count}</span>
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* Content */}
            <div className="flex-1 overflow-y-auto p-4">
              {activeTab === 'friends' && (
                <div className="space-y-3">
                  {/* Your position */}
                  <div className="bg-gradient-to-r from-pink-500/20 to-purple-500/20 rounded-2xl p-3 border border-pink-500/30">
                    <div className="flex items-center gap-3">
                      <div className="relative">
                        <span className="text-3xl">😎</span>
                        <span className="absolute -bottom-1 -right-1 bg-pink-500 text-white text-xs font-bold w-5 h-5 rounded-full flex items-center justify-center">
                          {myRank}
                        </span>
                      </div>
                      <div className="flex-1">
                        <p className="text-white font-bold">Ты</p>
                        <div className="flex items-center gap-3 text-sm">
                          <span className="text-yellow-400 flex items-center gap-1"><Star className="w-3 h-3" /> {totalStars}</span>
                          <span className="text-purple-400 flex items-center gap-1"><Trophy className="w-3 h-3" /> {totalPoints}</span>
                          <span className="text-orange-400 flex items-center gap-1"><Flame className="w-3 h-3" /> {streak}</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Friends list */}
                  {friends.map((friend, idx) => (
                    <FriendCard key={friend.id} friend={friend} index={idx} hasSentGift={sentGifts.includes(friend.id)} onSendGift={sendGift} />
                  ))}
                </div>
              )}

              {activeTab === 'search' && <SearchTab onAddFriend={addFriend} />}
              {activeTab === 'requests' && <RequestsTab />}
            </div>

            {/* Ranking footer */}
            <div className="p-3 border-t border-white/10">
              <div className="flex items-center justify-center gap-4">
                {ranking.slice(0, 3).map((player, idx) => (
                  <div key={player.id} className="text-center">
                    <div className="relative inline-block">
                      <span className="text-2xl">{player.avatar}</span>
                      {idx === 0 && <Crown className="absolute -top-2 left-1/2 -translate-x-1/2 w-4 h-4 text-yellow-400" />}
                    </div>
                    <p className="text-xs text-white/70 mt-1">{player.name}</p>
                    <p className="text-xs text-purple-400">{player.points} XP</p>
                  </div>
                ))}
              </div>
            </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}
