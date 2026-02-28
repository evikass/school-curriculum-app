'use client'

import { useState, useEffect, useMemo } from 'react'
import { Friend, SearchResult } from './types'
import { demoFriends, demoSearchResults } from './constants'

export function useFriends(totalPoints: number, totalStars: number, streak: number, selectedClass: number | null) {
  const [friends, setFriends] = useState<Friend[]>(() => {
    if (typeof window === 'undefined') return []
    const saved = localStorage.getItem('friendsList')
    if (saved) return JSON.parse(saved)
    localStorage.setItem('friendsList', JSON.stringify(demoFriends))
    return demoFriends
  })
  const [sentGifts, setSentGifts] = useState<string[]>(() => {
    if (typeof window === 'undefined') return []
    const gifts = localStorage.getItem('sentGifts')
    return gifts ? JSON.parse(gifts) : []
  })

  useEffect(() => {
    localStorage.setItem('friendsList', JSON.stringify(friends))
  }, [friends])

  const sendGift = (friendId: string) => {
    if (sentGifts.includes(friendId)) return
    const newGifts = [...sentGifts, friendId]
    setSentGifts(newGifts)
    localStorage.setItem('sentGifts', JSON.stringify(newGifts))
  }

  const addFriend = (user: SearchResult) => {
    const newFriend: Friend = {
      ...user,
      points: Math.floor(Math.random() * 1000),
      stars: Math.floor(Math.random() * 50),
      streak: Math.floor(Math.random() * 10),
      lastActive: 'только что',
      isOnline: true
    }
    setFriends(prev => [...prev, newFriend])
  }

  const removeFriend = (friendId: string) => {
    setFriends(prev => prev.filter(f => f.id !== friendId))
  }

  const ranking = useMemo(() => {
    return [...friends, {
      id: 'me',
      name: 'Ты',
      avatar: '😎',
      points: totalPoints,
      stars: totalStars,
      streak: streak,
      grade: selectedClass || 1,
      lastActive: 'сейчас',
      isOnline: true
    }].sort((a, b) => b.points - a.points)
  }, [friends, totalPoints, totalStars, streak, selectedClass])

  const myRank = ranking.findIndex(f => f.id === 'me') + 1

  return {
    friends,
    sentGifts,
    ranking,
    myRank,
    sendGift,
    addFriend,
    removeFriend
  }
}
