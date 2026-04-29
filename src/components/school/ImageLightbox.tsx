'use client'

import { createPortal } from 'react-dom'
import { useEffect, useState } from 'react'
import { motion, AnimePresence } from 'framer-motion'
import { X } from 'lucide-react'

interface ImageLightboxProps {
  src: string
  alt: string
  isOpen: boolean
  onClose: () => void
}

export default function ImageLightbox({ src, alt, isOpen, onClose }: ImageLightboxProps) {
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)
  }, [])

  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
    return () => { document.body.style.overflow = '' }
  }, [isOpen])

  if (!mounted) return null

  return createPortal(
    isOpen ? (
      <div
        className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/90"
        onClick={onClose}
      >
        <button
          onClick={onClose}
          className="absolute top-4 right-4 z-10 p-2 bg-white/10 hover:bg-white/20 
                     rounded-full text-white transition-colors"
        >
          <X className="w-7 h-7" />
        </button>

        <img
          src={src}
          alt={alt}
          style={{ width: '95vw', maxHeight: '92vh', objectFit: 'contain', cursor: 'pointer' }}
          onClick={onClose}
        />
      </div>
    ) : null,
    document.body
  )
}
