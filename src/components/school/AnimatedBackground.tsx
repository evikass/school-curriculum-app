'use client'

<<<<<<< HEAD
import { useEffect, useState } from 'react'

interface Star {
  id: number
  x: number
  y: number
  size: number
  opacity: number
  duration: number
  delay: number
}

export default function AnimatedBackground() {
  const [stars, setStars] = useState<Star[]>([])

  useEffect(() => {
    const newStars: Star[] = Array.from({ length: 50 }, (_, i) => ({
      id: i,
      x: Math.random() * 100,
      y: Math.random() * 100,
      size: 1 + Math.random() * 3,
      opacity: 0.2 + Math.random() * 0.5,
      duration: 2 + Math.random() * 3,
      delay: Math.random() * 3
    }))
    setStars(newStars)
  }, [])

  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden z-0">
      {/* Gradient orbs */}
      <div className="absolute top-0 left-1/4 w-[500px] h-[500px] bg-purple-500/20 rounded-full blur-[128px] animate-pulse" />
      <div className="absolute bottom-0 right-1/4 w-[400px] h-[400px] bg-pink-500/20 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }} />
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-indigo-500/10 rounded-full blur-[120px]" />
      
      {/* Twinkling stars */}
      {stars.map((star) => (
        <div
          key={star.id}
          className="absolute rounded-full bg-white animate-sparkle"
          style={{
            left: `${star.x}%`,
            top: `${star.y}%`,
            width: `${star.size}px`,
            height: `${star.size}px`,
            opacity: star.opacity,
            animationDuration: `${star.duration}s`,
            animationDelay: `${star.delay}s`
          }}
        />
      ))}

      {/* Floating particles */}
      <div className="absolute top-1/4 left-1/3 w-2 h-2 bg-yellow-300/40 rounded-full animate-float" style={{ animationDuration: '6s' }} />
      <div className="absolute top-1/3 right-1/4 w-3 h-3 bg-pink-300/30 rounded-full animate-float" style={{ animationDuration: '8s', animationDelay: '1s' }} />
      <div className="absolute bottom-1/4 left-1/5 w-2 h-2 bg-purple-300/40 rounded-full animate-float" style={{ animationDuration: '7s', animationDelay: '2s' }} />
      <div className="absolute bottom-1/3 right-1/3 w-4 h-4 bg-blue-300/20 rounded-full animate-float" style={{ animationDuration: '9s', animationDelay: '0.5s' }} />
=======
import { useMemo } from 'react'

// Pre-generate deterministic stars for SSR
const generateStars = (seed: number) => {
  const stars = []
  for (let i = 0; i < 50; i++) {
    // Use seeded random for deterministic output
    const rand1 = Math.sin(seed + i * 0.1) * 10000 % 100
    const rand2 = Math.sin(seed + i * 0.2 + 1000) * 10000 % 100
    const rand3 = Math.sin(seed + i * 0.3 + 1000) * 10000 % 4
    const rand4 = Math.sin(seed + i * 0.4 + 1000) * 10000 % 0.5 + 0.3
    stars.push({
      id: i,
      x: Math.abs(rand1),
      y: Math.abs(rand2),
      size: Math.abs(rand3) + 1,
      opacity: Math.abs(rand4)
    })
  }
  return stars
}

export default function AnimatedBackground() {
  // Use useMemo with a fixed seed for SSR consistency
  const stars = useMemo(() => generateStars(42), [])

  return (
    <div className="fixed inset-0 overflow-hidden pointer-events-none" suppressHydrationWarning>
      {stars.map(star => (
        <div
          key={star.id}
          className="absolute rounded-full bg-white animate-pulse"
          style={{
            left: `${star.x}%`,
            top: `${star.y}%`,
            width: star.size,
            height: star.size,
            opacity: star.opacity,
            animationDelay: `${star.id * 0.1}s`
          }}
        />
      ))}
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
    </div>
  )
}
