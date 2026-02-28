'use client'

import { Crown, Medal, Award } from 'lucide-react'

export const getChallengeIconColor = (icon: string): string => {
  switch (icon) {
    case 'lessons': return 'from-blue-400 to-cyan-500'
    case 'games': return 'from-green-400 to-emerald-500'
    case 'streak': return 'from-orange-400 to-red-500'
    case 'points': return 'from-yellow-400 to-amber-500'
    default: return 'from-purple-400 to-pink-500'
  }
}

export const getRankIcon = (rank: number) => {
  switch (rank) {
    case 1: return <Crown className="w-5 h-5 text-yellow-400" />
    case 2: return <Medal className="w-5 h-5 text-gray-300" />
    case 3: return <Award className="w-5 h-5 text-amber-600" />
    default: return <span className="text-sm font-bold text-gray-400">#{rank}</span>
  }
}
