'use client'

import { createPortal } from 'react-dom'
import { useEffect } from 'react'

interface ImageLightboxProps {
  src: string
  alt?: string
  isOpen: boolean
  onClose: () => void
}

export default function ImageLightbox({ src, alt, isOpen, onClose }: ImageLightboxProps) {
  // Блокируем скролл когда открыт
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

  // Закрытие по Escape
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
      className="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 animate-[fadeIn_150ms_ease-out]"
      onClick={onClose}
    >
      {/* Картинка — тап по ней тоже закрывает (повторный тап = сворачивание) */}
      <img
        src={src}
        alt={alt || ''}
        className="max-h-[95vh] max-w-[95vw] object-contain rounded-lg 
                   animate-[scaleIn_200ms_ease-out] cursor-pointer"
        onClick={onClose}
      />
    </div>,
    document.body
  )
}
