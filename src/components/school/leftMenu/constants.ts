// ===== DAILY BONUS =====
export const dailyRewards = [
  { day: 1, reward: 5, icon: '⭐' },
  { day: 2, reward: 10, icon: '🌟' },
  { day: 3, reward: 15, icon: '💫' },
  { day: 4, reward: 20, icon: '✨' },
  { day: 5, reward: 30, icon: '🔮' },
  { day: 6, reward: 40, icon: '💎' },
  { day: 7, reward: 100, icon: '🎁' },
]

// ===== DAILY QUIZ =====
export const quizQuestions = [
  { id: 1, question: "Сколько будет 15 + 27?", options: ["42", "41", "43", "40"], correct: 0, subject: "Математика", difficulty: 1 },
  { id: 2, question: "Сколько букв в русском алфавите?", options: ["30", "33", "32", "31"], correct: 1, subject: "Русский язык", difficulty: 1 },
  { id: 3, question: "Какое время года идёт после зимы?", options: ["Лето", "Осень", "Весна", "Зима"], correct: 2, subject: "Окружающий мир", difficulty: 1 },
  { id: 4, question: "Сколько планет в Солнечной системе?", options: ["8", "9", "7", "10"], correct: 0, subject: "Окружающий мир", difficulty: 1 },
  { id: 5, question: "Столица России?", options: ["Санкт-Петербург", "Москва", "Казань", "Новосибирск"], correct: 1, subject: "География", difficulty: 1 },
  { id: 6, question: "Сколько минут в часе?", options: ["60", "100", "24", "30"], correct: 0, subject: "Математика", difficulty: 1 },
  { id: 7, question: "Какой океан самый большой?", options: ["Атлантический", "Тихий", "Индийский", "Северный Ледовитый"], correct: 1, subject: "География", difficulty: 1 },
  { id: 8, question: "Сколько дней в неделе?", options: ["5", "6", "7", "8"], correct: 2, subject: "Окружающий мир", difficulty: 1 },
]

// ===== WEEKLY CHALLENGES =====
export const getWeekNumber = (): number => {
  const now = new Date()
  const start = new Date(now.getFullYear(), 0, 1)
  const diff = now.getTime() - start.getTime()
  const oneWeek = 604800000
  return Math.ceil(diff / oneWeek)
}

export const getWeekChallenges = (weekNum: number) => [
  { id: `week_${weekNum}_lessons`, title: 'Книжный червь', description: 'Пройди 5 уроков за неделю', icon: 'lessons', target: 5, reward: 50 },
  { id: `week_${weekNum}_games`, title: 'Игроман', description: 'Сыграй 7 игр за неделю', icon: 'games', target: 7, reward: 60 },
  { id: `week_${weekNum}_streak`, title: 'Марафонец', description: 'Занимайся 5 дней подряд', icon: 'streak', target: 5, reward: 70 },
  { id: `week_${weekNum}_points`, title: 'Охотник за баллами', description: 'Набери 200 баллов за неделю', icon: 'points', target: 200, reward: 100 }
]

// ===== LEVELS =====
export const getLevel = (totalPoints: number) => {
  if (totalPoints >= 1000) return { name: 'Легенда', icon: '🌟', color: 'from-amber-400 to-yellow-500' }
  if (totalPoints >= 500) return { name: 'Эксперт', icon: '👑', color: 'from-rose-400 to-red-500' }
  if (totalPoints >= 300) return { name: 'Мастер', icon: '🏆', color: 'from-purple-400 to-pink-500' }
  if (totalPoints >= 150) return { name: 'Знаток', icon: '⭐', color: 'from-yellow-400 to-orange-500' }
  if (totalPoints >= 50) return { name: 'Ученик', icon: '📚', color: 'from-blue-400 to-cyan-500' }
  return { name: 'Новичок', icon: '🌱', color: 'from-green-400 to-emerald-500' }
}

// ===== LEADERBOARD =====
export const getLeaderboard = (totalPoints: number, streak: number, gamesPlayed: number) => [
  { name: 'Ты', points: totalPoints, streak, games: gamesPlayed, isPlayer: true },
  { name: 'Алексей', points: 2450, streak: 12, games: 45, isPlayer: false },
  { name: 'Мария', points: 1890, streak: 8, games: 32, isPlayer: false },
  { name: 'Дмитрий', points: 1450, streak: 15, games: 28, isPlayer: false },
  { name: 'Анна', points: 1200, streak: 5, games: 22, isPlayer: false },
].sort((a, b) => b.points - a.points)
