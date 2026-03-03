'use client'

<<<<<<< HEAD
import { useState, useEffect } from 'react'
import { Volume2, VolumeX } from 'lucide-react'
import { soundManager } from '@/lib/sounds'

export default function SoundToggle() {
  const [enabled, setEnabled] = useState(true)

  useEffect(() => {
    setEnabled(soundManager.isEnabled())
  }, [])

  const toggleSound = () => {
    const newState = !enabled
    setEnabled(newState)
    soundManager.setEnabled(newState)
  }

  return (
    <button
      onClick={toggleSound}
      className={`p-2 rounded-xl transition-all ${
        enabled 
          ? 'bg-white/10 text-white hover:bg-white/20' 
          : 'bg-red-500/20 text-red-400 hover:bg-red-500/30'
      }`}
      title={enabled ? 'Выключить звуки' : 'Включить звуки'}
    >
      {enabled ? (
        <Volume2 className="w-5 h-5" />
      ) : (
        <VolumeX className="w-5 h-5" />
      )}
=======
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
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
    </button>
  )
}
