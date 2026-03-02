'use client'

import { useState } from 'react'
import { Volume2, VolumeX } from 'lucide-react'

export default function SoundToggle() {
  const [isMuted, setIsMuted] = useState(false)

  return (
    <button
      onClick={() => setIsMuted(!isMuted)}
      className="text-purple-400 text-xs bg-purple-400/20 px-3 py-1 rounded-full hover:bg-purple-400/30 transition-colors"
    >
      {isMuted ? <VolumeX className="w-3 h-3 inline" /> : <Volume2 className="w-3 h-3 inline" />}
      {isMuted ? ' Выкл' : ' Звук'}
    </button>
  )
}
