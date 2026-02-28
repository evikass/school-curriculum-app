'use client'

import { useState } from 'react'
import { Search, UserPlus } from 'lucide-react'
import { SearchResult } from './types'
import { demoSearchResults } from './constants'

interface SearchTabProps {
  onAddFriend: (user: SearchResult) => void
}

export function SearchTab({ onAddFriend }: SearchTabProps) {
  const [searchQuery, setSearchQuery] = useState('')

  return (
    <div className="space-y-4">
      {/* Search input */}
      <div className="relative">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-white/30" />
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Поиск друзей..."
          className="w-full bg-white/5 text-white rounded-xl py-3 pl-10 pr-4 border border-white/10 focus:border-pink-500/50 outline-none"
        />
      </div>

      {/* Results */}
      <div className="space-y-2">
        <p className="text-white/50 text-sm">Рекомендации</p>
        {demoSearchResults.map((user) => (
          <div key={user.id} className="bg-white/5 rounded-xl p-3 flex items-center gap-3">
            <span className="text-2xl">{user.avatar}</span>
            <div className="flex-1">
              <p className="text-white">{user.name}</p>
              <p className="text-white/50 text-sm">{user.grade} класс</p>
            </div>
            <button
              onClick={() => onAddFriend(user)}
              className="px-3 py-1.5 bg-pink-500 hover:bg-pink-600 text-white rounded-lg text-sm font-medium flex items-center gap-1"
            >
              <UserPlus className="w-4 h-4" />
              Добавить
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}
