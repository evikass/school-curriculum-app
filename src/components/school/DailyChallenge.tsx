'use client'

import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Gift, RotateCcw } from 'lucide-react'

const CHALLENGES = [
  { task: 'Реши 3 примера', reward: 30 },
  { task: 'Пройди тест', reward: 50 },
  { task: 'Собери пазл', reward: 40 },
]

export default function DailyChallenge() {
  const { addXP } = useSchool()
  const [completed, setCompleted] = useState(false)
  const [challenge, setChallenge] = useState<typeof CHALLENGES[0] | null>(null)

  useEffect(() => {
    // Only select challenge on client side
    setChallenge(CHALLENGES[Math.floor(Math.random() * CHALLENGES.length)])
  }, [])

  if (!challenge) return null

  const complete = () => {
    addXP(challenge.reward)
    setCompleted(true)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-amber-500/20 to-yellow-500/20 border-2 border-amber-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Gift className="w-5 h-5" /> Ежедневный челлендж
      </h3>
      {completed ? (
        <div className="text-center">
          <div className="text-4xl mb-4">🎉</div>
          <p className="text-green-400 font-bold">Выполнено! +{challenge.reward} XP</p>
        </div>
      ) : (
        <>
          <p className="text-white mb-4">{challenge.task}</p>
          <p className="text-amber-300 mb-4">Награда: {challenge.reward} XP</p>
          <button onClick={complete} className="w-full py-3 bg-amber-500 text-white rounded-xl font-bold">
            Выполнить
          </button>
        </>
      )}
    </div>
  )
}
