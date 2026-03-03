'use client'

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
    </div>
  )
}
