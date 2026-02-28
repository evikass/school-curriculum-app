// ===== ACHIEVEMENTS DATA =====
export interface Achievement {
  id: string
  name: string
  desc: string
  icon: string
  condition: (p: { 
    totalPoints: number
    completedTopics: Record<string, boolean>
    achievements: string[]
    streak: number
    gamesPlayed: number
    correctAnswers: number
    totalAnswers: number
  }) => boolean
  points: number
}

export const allAchievements: Achievement[] = [
  { id: 'first_lesson', name: 'Первый шаг', desc: 'Пройди первый урок', icon: 'book', condition: (p) => Object.keys(p.completedTopics).length >= 1, points: 10 },
  { id: 'first_game', name: 'Игрок', desc: 'Сыграй первую игру', icon: 'game', condition: (p) => p.gamesPlayed >= 1, points: 10 },
  { id: 'five_lessons', name: 'Ученик', desc: 'Пройди 5 уроков', icon: 'star', condition: (p) => Object.keys(p.completedTopics).length >= 5, points: 20 },
  { id: 'points_50', name: 'Коллекционер', desc: 'Набери 50 баллов', icon: 'zap', condition: (p) => p.totalPoints >= 50, points: 15 },
  { id: 'points_100', name: 'Богач', desc: 'Набери 100 баллов', icon: 'zap', condition: (p) => p.totalPoints >= 100, points: 25 },
  { id: 'points_250', name: 'Тысяча', desc: 'Набери 250 баллов', icon: 'zap', condition: (p) => p.totalPoints >= 250, points: 50 },
  { id: 'points_500', name: 'Миллионер', desc: 'Набери 500 баллов', icon: 'crown', condition: (p) => p.totalPoints >= 500, points: 100 },
  { id: 'ten_lessons', name: 'Отличник', desc: 'Пройди 10 уроков', icon: 'medal', condition: (p) => Object.keys(p.completedTopics).length >= 10, points: 30 },
  { id: 'twenty_lessons', name: 'Знаток', desc: 'Пройди 20 уроков', icon: 'target', condition: (p) => Object.keys(p.completedTopics).length >= 20, points: 50 },
  { id: 'streak_3', name: 'На волне', desc: 'Занимайся 3 дня подряд', icon: 'flame', condition: (p) => p.streak >= 3, points: 30 },
  { id: 'streak_7', name: 'Недельный марафон', desc: 'Занимайся 7 дней подряд', icon: 'flame', condition: (p) => p.streak >= 7, points: 70 },
  { id: 'games_5', name: 'Любитель игр', desc: 'Сыграй 5 игр', icon: 'game', condition: (p) => p.gamesPlayed >= 5, points: 25 },
  { id: 'games_10', name: 'Геймер', desc: 'Сыграй 10 игр', icon: 'game', condition: (p) => p.gamesPlayed >= 10, points: 50 },
  { id: 'accuracy_80', name: 'Меткий', desc: '80% правильных ответов', icon: 'target', condition: (p) => p.totalAnswers > 0 && (p.correctAnswers / p.totalAnswers) >= 0.8, points: 75 },
]

// ===== STICKERS DATA =====
export interface Sticker {
  id: string
  name: string
  emoji: string
  rarity: 'common' | 'rare' | 'epic' | 'legendary'
  description: string
  unlocked: boolean
}

export const allStickers: Sticker[] = [
  { id: 's1', name: 'Первоклашка', emoji: '🎒', rarity: 'common', description: 'Начал учёбу!', unlocked: false },
  { id: 's2', name: 'Читатель', emoji: '📖', rarity: 'common', description: 'Прочитал первый урок', unlocked: false },
  { id: 's3', name: 'Счётовод', emoji: '🔢', rarity: 'common', description: 'Решил 10 примеров', unlocked: false },
  { id: 's4', name: 'Художник', emoji: '🎨', rarity: 'common', description: 'Открыл урок ИЗО', unlocked: false },
  { id: 's7', name: 'Отличник', emoji: '⭐', rarity: 'rare', description: '5 уроков подряд', unlocked: false },
  { id: 's8', name: 'Геймер', emoji: '🎮', rarity: 'rare', description: 'Выиграл 10 игр', unlocked: false },
  { id: 's9', name: 'Звезда', emoji: '🌟', rarity: 'rare', description: 'Собрал 50 звёзд', unlocked: false },
  { id: 's10', name: 'Серия 7', emoji: '🔥', rarity: 'rare', description: '7 дней подряд', unlocked: false },
  { id: 's13', name: 'Мудрец', emoji: '🦉', rarity: 'epic', description: 'Прошёл 50 уроков', unlocked: false },
  { id: 's14', name: 'Чемпион', emoji: '🏆', rarity: 'epic', description: '100 побед', unlocked: false },
  { id: 's18', name: 'Легенда', emoji: '👑', rarity: 'legendary', description: '1000 звёзд!', unlocked: false },
  { id: 's19', name: 'Мастер', emoji: '🎯', rarity: 'legendary', description: 'Все достижения', unlocked: false },
]

export const rarityColors = {
  common: { bg: 'from-gray-500 to-gray-600', glow: 'shadow-gray-500/30' },
  rare: { bg: 'from-blue-500 to-cyan-500', glow: 'shadow-blue-500/30' },
  epic: { bg: 'from-purple-500 to-pink-500', glow: 'shadow-purple-500/30' },
  legendary: { bg: 'from-yellow-400 to-orange-500', glow: 'shadow-yellow-500/50' }
}
