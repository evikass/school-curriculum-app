'use client'

import { useEffect, useState } from 'react'

export default function Confetti() {
  const [pieces, setPieces] = useState<{ id: number; x: number; color: string; delay: number }[]>([])

  useEffect(() => {
    const colors = ['#FFD700', '#FF69B4', '#00CED1', '#32CD32', '#FF6347', '#9370DB']
    const newPieces = Array.from({ length: 100 }, (_, i) => ({
      id: i,
      x: Math.random() * 100,
      color: colors[Math.floor(Math.random() * colors.length)],
      delay: Math.random() * 2
    }))
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setPieces(newPieces)
  }, [])

  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden z-50">
      {pieces.map(piece => (
        <div
          key={piece.id}
          className="absolute w-3 h-3 animate-bounce"
          style={{
            left: `${piece.x}%`,
            top: '-20px',
            backgroundColor: piece.color,
            animation: `fall 3s linear ${piece.delay}s forwards`
          }}
        />
      ))}
      <style jsx>{`
        @keyframes fall {
          to {
            transform: translateY(100vh) rotate(720deg);
          }
        }
      `}</style>
    </div>
  )
}
