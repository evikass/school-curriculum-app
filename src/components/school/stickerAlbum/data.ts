export interface Sticker {
  id: string
  name: string
  emoji: string
  rarity: 'common' | 'rare' | 'epic' | 'legendary'
  description: string
  unlocked: boolean
  unlockedAt?: string
}

export const allStickers: Sticker[] = [
  // Common
  { id: 's1', name: 'Первоклашка', emoji: '🎒', rarity: 'common', description: 'Начал учёбу!', unlocked: false },
  { id: 's2', name: 'Читатель', emoji: '📖', rarity: 'common', description: 'Прочитал первый урок', unlocked: false },
  { id: 's3', name: 'Счётовод', emoji: '🔢', rarity: 'common', description: 'Решил 10 примеров', unlocked: false },
  { id: 's4', name: 'Художник', emoji: '🎨', rarity: 'common', description: 'Открыл урок ИЗО', unlocked: false },
  { id: 's5', name: 'Музыкант', emoji: '🎵', rarity: 'common', description: 'Открыл урок музыки', unlocked: false },
  { id: 's6', name: 'Спортсмен', emoji: '⚽', rarity: 'common', description: 'Занятия физкультурой', unlocked: false },

  // Rare
  { id: 's7', name: 'Отличник', emoji: '⭐', rarity: 'rare', description: '5 уроков подряд', unlocked: false },
  { id: 's8', name: 'Геймер', emoji: '🎮', rarity: 'rare', description: 'Выиграл 10 игр', unlocked: false },
  { id: 's9', name: 'Звезда', emoji: '🌟', rarity: 'rare', description: 'Собрал 50 звёзд', unlocked: false },
  { id: 's10', name: 'Серия 7', emoji: '🔥', rarity: 'rare', description: 'Занимался 7 дней подряд', unlocked: false },
  { id: 's11', name: 'Книголюб', emoji: '📚', rarity: 'rare', description: 'Прочитал 20 уроков', unlocked: false },
  { id: 's12', name: 'Математик', emoji: '🧮', rarity: 'rare', description: 'Решил 50 примеров', unlocked: false },

  // Epic
  { id: 's13', name: 'Мудрец', emoji: '🦉', rarity: 'epic', description: 'Прошёл 50 уроков', unlocked: false },
  { id: 's14', name: 'Чемпион', emoji: '🏆', rarity: 'epic', description: '100 побед в играх', unlocked: false },
  { id: 's15', name: 'Серия 30', emoji: '💎', rarity: 'epic', description: '30 дней подряд!', unlocked: false },
  { id: 's16', name: 'Гений', emoji: '🧠', rarity: 'epic', description: '500 XP за день', unlocked: false },
  { id: 's17', name: 'Исследователь', emoji: '🔍', rarity: 'epic', description: 'Открыл все предметы', unlocked: false },

  // Legendary
  { id: 's18', name: 'Легенда', emoji: '👑', rarity: 'legendary', description: '1000 звёзд!', unlocked: false },
  { id: 's19', name: 'Мастер', emoji: '🎯', rarity: 'legendary', description: 'Все достижения', unlocked: false },
  { id: 's20', name: 'Серия 100', emoji: '💫', rarity: 'legendary', description: '100 дней подряд!', unlocked: false },
]

export const rarityColors = {
  common: { bg: 'from-gray-500 to-gray-600', border: 'border-gray-400', glow: 'shadow-gray-500/30' },
  rare: { bg: 'from-blue-500 to-cyan-500', border: 'border-blue-400', glow: 'shadow-blue-500/30' },
  epic: { bg: 'from-purple-500 to-pink-500', border: 'border-purple-400', glow: 'shadow-purple-500/30' },
  legendary: { bg: 'from-yellow-400 to-orange-500', border: 'border-yellow-400', glow: 'shadow-yellow-500/50' }
}

export const rarityLabels = {
  common: 'Обычная',
  rare: 'Редкая',
  epic: 'Эпическая',
  legendary: 'Легендарная'
}
