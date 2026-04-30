'use client'

import { createPortal } from 'react-dom'
import { useState, useEffect } from 'react'
import { X, ZoomIn, ZoomOut } from 'lucide-react'

interface ImageLightboxProps {
  src: string
  alt?: string
  isOpen: boolean
  onClose: () => void
}

export default function ImageLightbox({ src, alt, isOpen, onClose }: ImageLightboxProps) {
  const [zoomed, setZoomed] = useState(false)

  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
    return () => {
      document.body.style.overflow = ''
    }
  }, [isOpen])

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isOpen) return
      if (e.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [isOpen, onClose])

  if (!isOpen) return null

  return createPortal(
    <div
      className="fixed inset-0 z-[100] flex items-center justify-center bg-black/90 backdrop-blur-sm"
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose()
      }}
    >
      {/* Close button */}
      <button
        onClick={onClose}
        className="absolute top-4 right-4 z-[101] p-3 bg-black/50 hover:bg-black/70 
                   rounded-full text-white transition-colors"
      >
        <X className="w-6 h-6" />
      </button>

      {/* Zoom toggle button */}
      <button
        onClick={() => setZoomed(!zoomed)}
        className="absolute top-4 left-4 z-[101] p-3 bg-black/50 hover:bg-black/70 
                   rounded-full text-white transition-colors"
      >
        {zoomed ? <ZoomOut className="w-6 h-6" /> : <ZoomIn className="w-6 h-6" />}
      </button>

      {/* Image */}
      <div
        className={`transition-transform duration-300 ease-in-out ${
          zoomed ? 'cursor-zoom-out' : 'cursor-zoom-in'
        }`}
        onClick={() => setZoomed(!zoomed)}
      >
        <img
          src={src}
          alt={alt || ''}
          className={`max-h-[90vh] max-w-[95vw] object-contain transition-transform duration-300 ease-in-out ${
            zoomed ? 'scale-[2.5]' : 'scale-100'
          }`}
          style={{ transformOrigin: 'center center' }}
        />
      </div>
    </div>,
    document.body
  )
}
