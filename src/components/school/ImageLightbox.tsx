'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { X, ZoomIn, ZoomOut, RotateCw } from 'lucide-react'

interface ImageLightboxProps {
  src: string
  alt: string
  isOpen: boolean
  onClose: () => void
}

export default function ImageLightbox({ src, alt, isOpen, onClose }: ImageLightboxProps) {
  const [zoom, setZoom] = useState(1)
  const [rotation, setRotation] = useState(0)

  const handleZoomIn = () => setZoom(prev => Math.min(prev + 0.5, 4))
  const handleZoomOut = () => setZoom(prev => Math.max(prev - 0.5, 0.5))
  const handleRotate = () => setRotation(prev => (prev + 90) % 360)
  const handleReset = () => {
    setZoom(1)
    setRotation(0)
  }

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          className="fixed inset-0 z-[100] flex items-center justify-center
                     bg-black/90 backdrop-blur-md"
          onClick={(e) => {
            if (e.target === e.currentTarget) {
              onClose()
              handleReset()
            }
          }}
        >
          {/* Toolbar */}
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="absolute top-4 right-4 z-10 flex items-center gap-2"
          >
            <button
              onClick={handleZoomOut}
              className="p-3 bg-white/10 hover:bg-white/20 rounded-xl transition-colors
                         text-white backdrop-blur-sm border border-white/10"
              title="Уменьшить"
            >
              <ZoomOut className="w-5 h-5" />
            </button>
            <span className="text-white/70 text-sm font-mono min-w-[3rem] text-center select-none">
              {Math.round(zoom * 100)}%
            </span>
            <button
              onClick={handleZoomIn}
              className="p-3 bg-white/10 hover:bg-white/20 rounded-xl transition-colors
                         text-white backdrop-blur-sm border border-white/10"
              title="Увеличить"
            >
              <ZoomIn className="w-5 h-5" />
            </button>
            <button
              onClick={handleRotate}
              className="p-3 bg-white/10 hover:bg-white/20 rounded-xl transition-colors
                         text-white backdrop-blur-sm border border-white/10"
              title="Повернуть"
            >
              <RotateCw className="w-5 h-5" />
            </button>
            <div className="w-px h-6 bg-white/20 mx-1" />
            <button
              onClick={() => {
                onClose()
                handleReset()
              }}
              className="p-3 bg-red-500/80 hover:bg-red-500 rounded-xl transition-colors
                         text-white backdrop-blur-sm"
              title="Закрыть"
            >
              <X className="w-5 h-5" />
            </button>
          </motion.div>

          {/* Hint at bottom */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="absolute bottom-4 left-1/2 -translate-x-1/2 z-10
                       text-white/40 text-sm select-none"
          >
            Нажмите на фон, чтобы закрыть
          </motion.div>

          {/* Image */}
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.8, opacity: 0 }}
            transition={{ type: 'spring', damping: 25, stiffness: 300 }}
            className="max-w-[95vw] max-h-[90vh] overflow-auto flex items-center justify-center"
          >
            <img
              src={src}
              alt={alt}
              style={{
                transform: `scale(${zoom}) rotate(${rotation}deg)`,
                transition: 'transform 0.3s ease',
              }}
              className="max-w-full max-h-[85vh] object-contain rounded-lg shadow-2xl select-none"
              draggable={false}
            />
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
