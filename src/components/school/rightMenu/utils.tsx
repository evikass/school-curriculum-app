'use client'

import { Star, Crown, Zap, Award, Target, Flame, Medal, BookOpen, Gamepad2, Heart, Rocket, Brain, Bolt, Trophy } from 'lucide-react'

export const getIcon = (icon: string) => {
  const iconClass = "w-5 h-5"
  switch (icon) {
    case 'star': return <Star className={iconClass} />
    case 'crown': return <Crown className={iconClass} />
    case 'zap': return <Zap className={iconClass} />
    case 'award': return <Award className={iconClass} />
    case 'target': return <Target className={iconClass} />
    case 'flame': return <Flame className={iconClass} />
    case 'medal': return <Medal className={iconClass} />
    case 'book': return <BookOpen className={iconClass} />
    case 'game': return <Gamepad2 className={iconClass} />
    case 'heart': return <Heart className={iconClass} />
    case 'rocket': return <Rocket className={iconClass} />
    case 'brain': return <Brain className={iconClass} />
    case 'lightning': return <Bolt className={iconClass} />
    case 'trophy': return <Trophy className={iconClass} />
    default: return <Star className={iconClass} />
  }
}
