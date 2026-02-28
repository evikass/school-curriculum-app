'use client'

import { useState, useEffect } from 'react'

export function Confetti() {
  const [particles, setParticles] = useState<Array<{ id: number; x: number; color: string; delay: number; rotation: number }>>([])

  useEffect(() => {
    const colors = ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']
    setParticles(Array.from({ length: 50 }, (_, i) => ({
      id: i,
      x: Math.random() * 100,
      color: colors[Math.floor(Math.random() * colors.length)],
      delay: Math.random() * 0.5,
      rotation: Math.random() * 360
    })))
  }, [])

  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden z-50">
      {particles.map((p) => (
        <div key={p.id} className="absolute animate-confetti"
          style={{ left: `${p.x}%`, top: '-20px', width: '10px', height: '10px', backgroundColor: p.color,
            borderRadius: Math.random() > 0.5 ? '50%' : '0', animationDelay: `${p.delay}s`, transform: `rotate(${p.rotation}deg)` }} />
      ))}
    </div>
  )
}
