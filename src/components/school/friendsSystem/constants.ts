import { Friend, SearchResult } from './types'

export const demoFriends: Friend[] = [
  { id: '1', name: 'Алиса', avatar: '👧', points: 1250, stars: 45, streak: 7, grade: 3, lastActive: '5 мин', isOnline: true },
  { id: '2', name: 'Максим', avatar: '👦', points: 980, stars: 32, streak: 3, grade: 4, lastActive: '1 час', isOnline: true },
  { id: '3', name: 'София', avatar: '👧', points: 1580, stars: 58, streak: 12, grade: 2, lastActive: '2 часа', isOnline: false },
  { id: '4', name: 'Артём', avatar: '👦', points: 890, stars: 28, streak: 5, grade: 5, lastActive: '1 день', isOnline: false },
  { id: '5', name: 'Вика', avatar: '👧', points: 2100, stars: 72, streak: 15, grade: 3, lastActive: '3 часа', isOnline: true },
]

export const demoSearchResults: SearchResult[] = [
  { id: '6', name: 'Даниил', avatar: '👦', grade: 4 },
  { id: '7', name: 'Полина', avatar: '👧', grade: 2 },
  { id: '8', name: 'Кирилл', avatar: '👦', grade: 5 },
]
