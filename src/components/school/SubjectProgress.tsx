'use client'

<<<<<<< HEAD
import { useSchool } from '@/context/SchoolContext'
import { useState } from 'react'
import { ChevronDown, ChevronUp, CheckCircle, Circle, Play, Star } from 'lucide-react'

interface SubjectProgressProps {
  subjectTitle: string
  subjectIcon: string
  subjectColor: string
  topics: string[]
  completedTopics: Record<string, boolean>
}

export default function SubjectProgress({ 
  subjectTitle, 
  subjectIcon, 
  subjectColor, 
  topics, 
  completedTopics 
}: SubjectProgressProps) {
  const [expanded, setExpanded] = useState(false)
  
  const totalTopics = topics.length
  const completedCount = Object.keys(completedTopics).filter(key => 
    key.startsWith(subjectTitle) && completedTopics[key]
  ).length
  
  const progressPercent = totalTopics > 0 ? (completedCount / totalTopics) * 100 : 0

  return (
    <div className="bg-white/5 rounded-2xl border border-white/10 overflow-hidden">
      {/* Header */}
      <button 
        onClick={() => setExpanded(!expanded)}
        className="w-full p-4 flex items-center justify-between hover:bg-white/5 transition-colors"
      >
        <div className="flex items-center gap-3">
          <div className={`w-10 h-10 rounded-xl bg-gradient-to-br ${subjectColor} flex items-center justify-center`}>
            <span className="text-xl">{subjectIcon}</span>
          </div>
          <div className="text-left">
            <h3 className="font-bold text-white">{subjectTitle}</h3>
            <p className="text-sm text-white/60">{completedCount}/{totalTopics} тем</p>
          </div>
        </div>
        
        <div className="flex items-center gap-3">
          {/* Progress bar */}
          <div className="w-24 h-2 bg-white/10 rounded-full overflow-hidden">
            <div 
              className={`h-full bg-gradient-to-r ${subjectColor} transition-all duration-500`}
              style={{ width: `${progressPercent}%` }}
            />
          </div>
          
          {expanded ? (
            <ChevronUp className="w-5 h-5 text-white/60" />
          ) : (
            <ChevronDown className="w-5 h-5 text-white/60" />
          )}
        </div>
      </button>

      {/* Expanded content */}
      {expanded && (
        <div className="border-t border-white/10 p-4 space-y-2">
          {topics.map((topic, index) => {
            const topicKey = `${subjectTitle}-${topic}`
            const isCompleted = completedTopics[topicKey]
            
            return (
              <div 
                key={index}
                className={`flex items-center gap-3 p-3 rounded-xl transition-all ${
                  isCompleted 
                    ? 'bg-green-500/10 border border-green-500/30' 
                    : 'bg-white/5 border border-white/10'
                }`}
              >
                {isCompleted ? (
                  <CheckCircle className="w-5 h-5 text-green-400" />
                ) : (
                  <Circle className="w-5 h-5 text-white/30" />
                )}
                
                <span className={`flex-1 ${isCompleted ? 'text-green-300' : 'text-white/80'}`}>
                  {topic}
                </span>
                
                {isCompleted && (
                  <Star className="w-4 h-4 text-yellow-400 fill-yellow-400" />
                )}
              </div>
            )
          })}
        </div>
      )}
=======
import { TrendingUp } from 'lucide-react'

export default function SubjectProgress() {
  const subjects = [
    { name: 'Математика', progress: 75, color: 'from-blue-500 to-cyan-500' },
    { name: 'Русский язык', progress: 60, color: 'from-pink-500 to-rose-500' },
    { name: 'Окружающий мир', progress: 45, color: 'from-green-500 to-emerald-500' },
  ]

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-violet-500/20 to-purple-500/20 border-2 border-violet-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <TrendingUp className="w-5 h-5" /> Прогресс по предметам
      </h3>
      <div className="space-y-4">
        {subjects.map(s => (
          <div key={s.name}>
            <div className="flex justify-between mb-1">
              <span className="text-white">{s.name}</span>
              <span className="text-violet-300">{s.progress}%</span>
            </div>
            <div className="h-2 bg-white/20 rounded-full overflow-hidden">
              <div className={`h-full bg-gradient-to-r ${s.color} transition-all`} style={{ width: `${s.progress}%` }} />
            </div>
          </div>
        ))}
      </div>
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
    </div>
  )
}
