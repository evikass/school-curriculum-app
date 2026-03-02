'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw, Calendar } from 'lucide-react'

const DAYS = [
  { name: 'Понедельник', short: 'Пн', order: 1, emoji: '📖' },
  { name: 'Вторник', short: 'Вт', order: 2, emoji: '✏️' },
  { name: 'Среда', short: 'Ср', order: 3, emoji: '🎨' },
  { name: 'Четверг', short: 'Чт', order: 4, emoji: '⚽' },
  { name: 'Пятница', short: 'Пт', order: 5, emoji: '🎵' },
  { name: 'Суббота', short: 'Сб', order: 6, emoji: '🎮' },
  { name: 'Воскресенье', short: 'Вс', order: 7, emoji: '🌟' },
]

const MONTHS = [
  'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
  'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
]

const SEASONS = [
  { name: 'Зима', months: ['Декабрь', 'Январь', 'Февраль'], emoji: '❄️' },
  { name: 'Весна', months: ['Март', 'Апрель', 'Май'], emoji: '🌸' },
  { name: 'Лето', months: ['Июнь', 'Июль', 'Август'], emoji: '☀️' },
  { name: 'Осень', months: ['Сентябрь', 'Октябрь', 'Ноябрь'], emoji: '🍂' },
]

type GameMode = 'order' | 'yesterday' | 'month' | 'season'

export default function DaysOfWeek() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('order')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)

  // Mode: order
  const [shuffledDays, setShuffledDays] = useState<typeof DAYS>([])
  const [selectedDays, setSelectedDays] = useState<typeof DAYS>([])

  // Mode: yesterday/tomorrow
  const [currentDayQuestion, setCurrentDayQuestion] = useState<{ day: typeof DAYS[0]; question: 'вчера' | 'завтра' } | null>(null)

  // Mode: month
  const [monthQuestion, setMonthQuestion] = useState<{ month: string; type: 'number' | 'season' } | null>(null)

  // Mode: season
  const [seasonQuestion, setSeasonQuestion] = useState<{ months: string[]; answer: string } | null>(null)

  const shuffleArray = <T,>(arr: T[]): T[] => [...arr].sort(() => Math.random() - 0.5)

  useEffect(() => {
    if (mode === 'order') {
      setShuffledDays(shuffleArray(DAYS))
      setSelectedDays([])
    } else if (mode === 'yesterday') {
      generateDayQuestion()
    } else if (mode === 'month') {
      generateMonthQuestion()
    } else if (mode === 'season') {
      generateSeasonQuestion()
    }
  }, [mode])

  const generateDayQuestion = () => {
    const day = DAYS[Math.floor(Math.random() * DAYS.length)]
    const question: 'вчера' | 'завтра' = Math.random() > 0.5 ? 'вчера' : 'завтра'
    setCurrentDayQuestion({ day, question })
  }

  const generateMonthQuestion = () => {
    const month = MONTHS[Math.floor(Math.random() * MONTHS.length)]
    const type: 'number' | 'season' = Math.random() > 0.5 ? 'number' : 'season'
    setMonthQuestion({ month, type })
  }

  const generateSeasonQuestion = () => {
    const season = SEASONS[Math.floor(Math.random() * SEASONS.length)]
    setSeasonQuestion({ months: shuffleArray(season.months), answer: season.name })
  }

  const handleDaySelect = (day: typeof DAYS[0]) => {
    if (selectedDays.length >= 7) return
    const newSelected = [...selectedDays, day]
    setSelectedDays(newSelected)
    setShuffledDays(shuffledDays.filter(d => d.name !== day.name))

    if (newSelected.length === 7) {
      const isCorrect = newSelected.every((d, i) => d.order === i + 1)
      if (isCorrect) {
        playCorrect()
        setScore(s => s + 30)
        setStreak(s => s + 1)
        setFeedback('correct')
        addXP(15 + streak)
      } else {
        playWrong()
        setStreak(0)
        setFeedback('wrong')
      }
      setTimeout(() => {
        setFeedback(null)
        setShuffledDays(shuffleArray(DAYS))
        setSelectedDays([])
      }, 1500)
    }
  }

  const handleYesterdayAnswer = (answer: string) => {
    if (!currentDayQuestion) return
    const dayIndex = DAYS.findIndex(d => d.name === currentDayQuestion.day.name)
    let correctAnswer: string
    
    if (currentDayQuestion.question === 'вчера') {
      correctAnswer = dayIndex === 0 ? DAYS[6].name : DAYS[dayIndex - 1].name
    } else {
      correctAnswer = dayIndex === 6 ? DAYS[0].name : DAYS[dayIndex + 1].name
    }

    if (answer === correctAnswer) {
      playCorrect()
      setScore(s => s + 15)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(8 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateDayQuestion()
    }, 1000)
  }

  const handleMonthAnswer = (answer: number | string) => {
    if (!monthQuestion) return
    let correct: boolean
    
    if (monthQuestion.type === 'number') {
      correct = answer === MONTHS.indexOf(monthQuestion.month) + 1
    } else {
      const season = SEASONS.find(s => s.months.includes(monthQuestion.month))
      correct = answer === season?.name
    }

    if (correct) {
      playCorrect()
      setScore(s => s + 15)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(8 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateMonthQuestion()
    }, 1000)
  }

  const handleSeasonAnswer = (answer: string) => {
    if (!seasonQuestion) return
    
    if (answer === seasonQuestion.answer) {
      playCorrect()
      setScore(s => s + 20)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(10 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateSeasonQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'order') {
      setShuffledDays(shuffleArray(DAYS))
      setSelectedDays([])
    } else if (mode === 'yesterday') {
      generateDayQuestion()
    } else if (mode === 'month') {
      generateMonthQuestion()
    } else {
      generateSeasonQuestion()
    }
  }

  return (
    <div className="bg-gradient-to-br from-amber-500/20 to-orange-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">📅</span> Дни недели и месяцы
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4 flex-wrap">
        {(['order', 'yesterday', 'month', 'season'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-amber-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'order' ? '🗓️ Порядок' : m === 'yesterday' ? '⬅️ Вчера/Завтра' : m === 'month' ? '📆 Месяцы' : '🍂 Сезоны'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'order' && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Расставь дни недели по порядку:</div>
            
            <div className="flex flex-wrap gap-2 justify-center mb-4 min-h-[60px] p-3 bg-white/5 rounded-lg">
              {selectedDays.map((d, i) => (
                <span key={d.name} className="px-3 py-2 bg-amber-500 rounded-lg text-white font-medium flex items-center gap-1">
                  <span className="text-lg">{d.emoji}</span> {d.short}
                </span>
              ))}
              {selectedDays.length < 7 && (
                <span className="text-white/30 animate-pulse">Выбери следующий день...</span>
              )}
            </div>

            <div className="flex flex-wrap gap-2 justify-center">
              {shuffledDays.map(d => (
                <button
                  key={d.name}
                  onClick={() => handleDaySelect(d)}
                  disabled={selectedDays.length >= 7}
                  className="px-4 py-2 bg-white/10 hover:bg-white/20 rounded-lg text-white font-medium transition-all hover:scale-105 disabled:opacity-50 flex items-center gap-1"
                >
                  <span className="text-lg">{d.emoji}</span> {d.short}
                </button>
              ))}
            </div>

            {feedback && (
              <div className={`mt-4 p-3 rounded-lg ${feedback === 'correct' ? 'bg-green-500/20 text-green-300' : 'bg-red-500/20 text-red-300'}`}>
                {feedback === 'correct' ? '🎉 Отлично! Все дни в правильном порядке!' : '❌ Попробуй ещё раз!'}
              </div>
            )}
          </div>
        )}

        {mode === 'yesterday' && currentDayQuestion && (
          <div className="text-center">
            <div className="mb-2 text-white/60">
              Какой день был <strong className="text-amber-300">{currentDayQuestion.question}</strong>?
            </div>
            <div className="text-5xl mb-2">{currentDayQuestion.day.emoji}</div>
            <div className="text-3xl font-bold text-white mb-6">{currentDayQuestion.day.name}</div>
            
            <div className="grid grid-cols-4 gap-2">
              {DAYS.map(d => (
                <button
                  key={d.name}
                  onClick={() => handleYesterdayAnswer(d.name)}
                  className="p-3 bg-white/10 hover:bg-amber-500/30 rounded-lg text-white font-medium transition-all hover:scale-105"
                >
                  <div className="text-2xl mb-1">{d.emoji}</div>
                  <div className="text-xs">{d.short}</div>
                </button>
              ))}
            </div>

            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                {currentDayQuestion.question === 'вчера' 
                  ? `Вчера был: ${DAYS[(DAYS.findIndex(d => d.name === currentDayQuestion.day.name) + 6) % 7].name}`
                  : `Завтра будет: ${DAYS[(DAYS.findIndex(d => d.name === currentDayQuestion.day.name) + 1) % 7].name}`}
              </div>
            )}
          </div>
        )}

        {mode === 'month' && monthQuestion && (
          <div className="text-center">
            {monthQuestion.type === 'number' ? (
              <>
                <div className="mb-2 text-white/60">Какой по счёту месяц?</div>
                <div className="text-4xl font-bold text-white mb-6">{monthQuestion.month}</div>
                <div className="grid grid-cols-6 gap-2">
                  {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map(n => (
                    <button
                      key={n}
                      onClick={() => handleMonthAnswer(n)}
                      className="p-3 bg-white/10 hover:bg-amber-500/30 rounded-lg text-white font-bold text-xl transition-all hover:scale-105"
                    >
                      {n}
                    </button>
                  ))}
                </div>
              </>
            ) : (
              <>
                <div className="mb-2 text-white/60">К какому сезону относится?</div>
                <div className="text-4xl font-bold text-white mb-6">{monthQuestion.month}</div>
                <div className="grid grid-cols-2 gap-3">
                  {SEASONS.map(s => (
                    <button
                      key={s.name}
                      onClick={() => handleMonthAnswer(s.name)}
                      className="p-4 bg-white/10 hover:bg-amber-500/30 rounded-lg text-white font-medium transition-all hover:scale-105 flex items-center justify-center gap-2"
                    >
                      <span className="text-2xl">{s.emoji}</span> {s.name}
                    </button>
                  ))}
                </div>
              </>
            )}
          </div>
        )}

        {mode === 'season' && seasonQuestion && (
          <div className="text-center">
            <div className="mb-2 text-white/60">К какому сезону относятся эти месяцы?</div>
            <div className="flex justify-center gap-3 mb-6">
              {seasonQuestion.months.map(m => (
                <span key={m} className="px-4 py-2 bg-white/10 rounded-lg text-white font-medium">{m}</span>
              ))}
            </div>
            <div className="grid grid-cols-2 gap-3">
              {SEASONS.map(s => (
                <button
                  key={s.name}
                  onClick={() => handleSeasonAnswer(s.name)}
                  className="p-4 bg-white/10 hover:bg-amber-500/30 rounded-lg text-white font-medium transition-all hover:scale-105 flex items-center justify-center gap-2"
                >
                  <span className="text-2xl">{s.emoji}</span> {s.name}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>

      <div className="flex justify-center mt-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>

      <div className="mt-4 p-3 bg-white/5 rounded-lg">
        <div className="text-white/60 text-sm mb-2">📅 Дни недели:</div>
        <div className="flex justify-between text-xs">
          {DAYS.map(d => (
            <span key={d.name} className="text-center">
              <span className="text-lg block">{d.emoji}</span>
              <span className="text-white/70">{d.short}</span>
            </span>
          ))}
        </div>
      </div>
    </div>
  )
}
