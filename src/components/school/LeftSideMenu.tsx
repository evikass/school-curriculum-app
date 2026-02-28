'use client'

import { useState, useMemo, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { useSchool } from '@/context/SchoolContext'
import { X, Target } from 'lucide-react'
import { dailyRewards, quizQuestions, getWeekNumber, getWeekChallenges, getLevel } from './leftMenu/constants'
import { getChallengeIconColor, getRankIcon } from './leftMenu/utils'
import TasksTab from './leftMenu/TasksTab'
import BonusTab from './leftMenu/BonusTab'
import ChallengesTab from './leftMenu/ChallengesTab'
import StatsTab from './leftMenu/StatsTab'
import QuizTab from './leftMenu/QuizTab'

interface DailyTask {
  id: string
  title: string
  description: string
  points: number
  progress: number
  total: number
  type: 'lessons' | 'games' | 'points' | 'streak'
  icon: 'book' | 'game' | 'zap' | 'flame'
}

function getInitialClaimedState(today: string): boolean {
  if (typeof window === 'undefined') return false
  return localStorage.getItem('lastBonusClaim') === today
}

export default function LeftSideMenu() {
  const { progress, addPoints, selectedClass } = useSchool()
  const [isOpen, setIsOpen] = useState(false)
  const [activeTab, setActiveTab] = useState<'tasks' | 'bonus' | 'challenges' | 'stats' | 'quiz'>('tasks')
  const [taskBonusClaimed, setTaskBonusClaimed] = useState(false)
  const [showClaimAnimation, setShowClaimAnimation] = useState(false)
  const [quizAnswered, setQuizAnswered] = useState(() => {
    if (typeof window === 'undefined') return false
    return localStorage.getItem('lastQuizDate') === new Date().toDateString()
  })
  const [quizSelectedAnswer, setQuizSelectedAnswer] = useState<number | null>(null)
  const [quizComplete, setQuizComplete] = useState(false)

  const today = new Date().toISOString().split('T')[0]
  const [claimedToday, setClaimedToday] = useState(() => getInitialClaimedState(today))

  // Progress data
  const todayLessons = progress.todayLessons || 0
  const todayGames = progress.todayGames || 0
  const todayPoints = progress.todayPoints || 0
  const streak = progress.streak || 0
  const completedLessons = Object.keys(progress.completedTopics).length
  const gamesPlayed = progress.gamesPlayed
  const totalPoints = progress.totalPoints
  const achievements = progress.achievements.length
  const correctAnswers = progress.correctAnswers
  const totalAnswers = progress.totalAnswers
  const accuracy = totalAnswers > 0 ? Math.round((correctAnswers / totalAnswers) * 100) : 0

  // Daily Tasks
  const tasks: DailyTask[] = useMemo(() => [
    { id: 'complete_lesson', title: '📚 Пройди урок', description: 'Заверши один урок сегодня', points: 15, progress: Math.min(todayLessons, 1), total: 1, type: 'lessons', icon: 'book' },
    { id: 'play_game', title: '🎮 Сыграй в игру', description: 'Заверши одну игру сегодня', points: 20, progress: Math.min(todayGames, 1), total: 1, type: 'games', icon: 'game' },
    { id: 'earn_points', title: '⭐ Набери 30 баллов', description: 'Заработай баллы за сегодня', points: 25, progress: Math.min(todayPoints, 30), total: 30, type: 'points', icon: 'zap' },
    { id: 'streak_bonus', title: '🔥 Занимайся подряд', description: `Твоя серия: ${streak} дней`, points: streak >= 3 ? 30 : 0, progress: streak >= 3 ? 1 : 0, total: 1, type: 'streak', icon: 'flame' }
  ], [todayLessons, todayGames, todayPoints, streak])

  const completedTasks = tasks.filter(t => t.progress >= t.total).length
  const totalTasks = tasks.filter(t => t.points > 0).length
  const allCompleted = completedTasks === totalTasks && totalTasks > 0
  const totalReward = tasks.reduce((sum, t) => sum + (t.progress >= t.total ? t.points : 0), 0)

  // Daily Bonus
  const consecutiveDays = useMemo(() => {
    if (typeof window === 'undefined') return 0
    const lastClaimDate = localStorage.getItem('lastBonusClaim')
    const savedStreak = parseInt(localStorage.getItem('bonusStreak') || '0', 10)
    if (!lastClaimDate) return 0
    const yesterday = new Date()
    yesterday.setDate(yesterday.getDate() - 1)
    const yesterdayStr = yesterday.toISOString().split('T')[0]
    if (lastClaimDate === yesterdayStr || lastClaimDate === today) return savedStreak
    return 0
  }, [today])

  const currentDay = (consecutiveDays % 7) + 1
  const currentReward = dailyRewards[currentDay - 1]

  const claimBonus = () => {
    if (claimedToday) return
    const newStreak = consecutiveDays + 1
    localStorage.setItem('lastBonusClaim', today)
    localStorage.setItem('bonusStreak', newStreak.toString())
    addPoints(currentReward.reward)
    setShowClaimAnimation(true)
    setClaimedToday(true)
    setTimeout(() => setShowClaimAnimation(false), 2000)
  }

  // Weekly Challenges
  const weekNum = getWeekNumber()
  const challenges = useMemo(() => getWeekChallenges(weekNum), [weekNum])
  const getChallengeProgress = (icon: string): number => {
    switch (icon) {
      case 'lessons': return Math.min(completedLessons, 5)
      case 'games': return Math.min(gamesPlayed, 7)
      case 'streak': return Math.min(streak, 5)
      case 'points': return Math.min(totalPoints, 200)
      default: return 0
    }
  }
  const completedChallenges = challenges.filter(c => getChallengeProgress(c.icon) >= c.target).length

  // Quiz
  const todayQuestion = useMemo(() => {
    const dayOfYear = Math.floor((new Date().getTime() - new Date(new Date().getFullYear(), 0, 0).getTime()) / 86400000)
    const grade = selectedClass || 1
    const maxDifficulty = grade <= 2 ? 1 : grade <= 4 ? 2 : 3
    const filtered = quizQuestions.filter(q => q.difficulty <= maxDifficulty)
    return filtered[dayOfYear % filtered.length]
  }, [selectedClass])

  const handleQuizAnswer = (answerIndex: number) => {
    if (quizComplete) return
    setQuizSelectedAnswer(answerIndex)
    setQuizComplete(true)
    if (answerIndex === todayQuestion.correct) addPoints(todayQuestion.difficulty * 5 + 10)
    setTimeout(() => {
      localStorage.setItem('lastQuizDate', new Date().toDateString())
      setQuizAnswered(true)
    }, 2000)
  }

  const hasUnclaimedBonus = !claimedToday
  const notificationCount = (hasUnclaimedBonus ? 1 : 0) + (!quizAnswered ? 1 : 0)

  return (
    <>
      {/* Floating button */}
      <motion.button
        initial={{ scale: 0 }} animate={{ scale: 1 }} whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }}
        onClick={() => setIsOpen(true)}
        className="fixed left-4 bottom-4 z-40 p-4 rounded-full bg-gradient-to-br from-green-400 to-teal-500 shadow-xl shadow-teal-500/30 hover:shadow-2xl hover:shadow-teal-500/40 transition-all duration-300"
      >
        <Target className="w-6 h-6 text-white" />
        {notificationCount > 0 && (
          <span className="absolute -top-1 -right-1 w-5 h-5 bg-red-500 text-white rounded-full text-xs font-bold flex items-center justify-center animate-pulse">
            {notificationCount}
          </span>
        )}
      </motion.button>

      {/* Modal */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm"
            onClick={(e) => e.target === e.currentTarget && setIsOpen(false)}
          >
            <motion.div
              initial={{ scale: 0.8, opacity: 0, y: 50 }} animate={{ scale: 1, opacity: 1, y: 0 }} exit={{ scale: 0.8, opacity: 0, y: 50 }}
              className="w-full max-w-lg max-h-[90vh] overflow-hidden bg-gradient-to-br from-gray-900 to-teal-900 rounded-3xl border-2 border-teal-500/30 shadow-2xl"
            >
              {/* Header */}
              <div className="bg-teal-600 p-3">
                <div className="flex justify-between items-center mb-3">
                  <h2 className="text-lg font-black text-white flex items-center gap-2">
                    <Target className="w-5 h-5" /> Меню
                  </h2>
                  <button onClick={() => setIsOpen(false)} className="p-1.5 rounded-xl hover:bg-white/20 transition-colors">
                    <X className="w-5 h-5 text-white" />
                  </button>
                </div>
                
                {/* Tabs */}
                <div className="flex gap-1 overflow-x-auto pb-1">
                  {[
                    { id: 'tasks', label: '📋 Задания', notif: completedTasks < totalTasks },
                    { id: 'bonus', label: '🎁 Бонус', notif: hasUnclaimedBonus },
                    { id: 'challenges', label: '🗓️ Челленджи', notif: false },
                    { id: 'stats', label: '📊 Статистика', notif: false },
                    { id: 'quiz', label: '🧠 Викторина', notif: !quizAnswered },
                  ].map(tab => (
                    <button key={tab.id} onClick={() => setActiveTab(tab.id as typeof activeTab)}
                      className={`relative px-3 py-1.5 rounded-lg font-medium text-xs transition-all whitespace-nowrap ${activeTab === tab.id ? 'bg-white text-teal-600' : 'bg-white/20 text-white hover:bg-white/30'}`}>
                      {tab.label}
                      {tab.notif && <span className="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full" />}
                    </button>
                  ))}
                </div>
              </div>

              {/* Content */}
              <div className="overflow-y-auto max-h-[65vh]">
                {activeTab === 'tasks' && <TasksTab tasks={tasks} todayLessons={todayLessons} todayGames={todayGames} todayPoints={todayPoints} allCompleted={allCompleted} totalReward={totalReward} taskBonusClaimed={taskBonusClaimed} onClaimBonus={() => setTaskBonusClaimed(true)} />}
                {activeTab === 'bonus' && <BonusTab currentDay={currentDay} currentReward={currentReward} claimedToday={claimedToday} consecutiveDays={consecutiveDays} onClaim={claimBonus} />}
                {activeTab === 'challenges' && <ChallengesTab challenges={challenges} completedChallenges={completedChallenges} weekNum={weekNum} getChallengeProgress={getChallengeProgress} />}
                {activeTab === 'stats' && <StatsTab totalPoints={totalPoints} completedLessons={completedLessons} gamesPlayed={gamesPlayed} streak={streak} achievements={achievements} accuracy={accuracy} />}
                {activeTab === 'quiz' && <QuizTab quizAnswered={quizAnswered} quizComplete={quizComplete} quizSelectedAnswer={quizSelectedAnswer} todayQuestion={todayQuestion} onAnswer={handleQuizAnswer} />}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Claim animation */}
      {showClaimAnimation && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center pointer-events-none">
          <motion.div initial={{ scale: 0.5, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="text-center">
            <div className="text-6xl mb-4">{currentReward.icon}</div>
            <div className="px-6 py-3 rounded-2xl bg-gradient-to-r from-yellow-400 to-amber-500 text-purple-900">
              <p className="text-xl font-black">+{currentReward.reward} баллов!</p>
            </div>
          </motion.div>
        </div>
      )}
    </>
  )
}
