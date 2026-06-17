'use client'

import { createPortal } from 'react-dom'
import { useEffect, useRef, useCallback } from 'react'

interface ImageLightboxProps {
  src: string
  alt?: string
  isOpen: boolean
  onClose: () => void
}

export default function ImageLightbox({ src, alt, isOpen, onClose }: ImageLightboxProps) {
  const imgRef = useRef<HTMLImageElement>(null)
  const containerRef = useRef<HTMLDivElement>(null)

  // Состояние трансформации
  const transformRef = useRef({ scale: 1, x: 0, y: 0 })
  // Активный пинч
  const pinchRef = useRef({
    active: false,
    startDistance: 0,
    startScale: 1,
  })
  // Свайп/перетаскивание одним пальцем при увеличении
  const dragRef = useRef({
    active: false,
    startX: 0,
    startY: 0,
    startTransX: 0,
    startTransY: 0,
  })

  const applyTransform = useCallback(() => {
    const img = imgRef.current
    if (!img) return
    const { scale, x, y } = transformRef.current
    img.style.transform = `translate(${x}px, ${y}px) scale(${scale})`
  }, [])

  const resetTransform = useCallback(() => {
    transformRef.current = { scale: 1, x: 0, y: 0 }
    applyTransform()
  }, [applyTransform])

  // Блокируем скролл когда открыт
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
      resetTransform()
    } else {
      document.body.style.overflow = ''
    }
    return () => {
      document.body.style.overflow = ''
    }
  }, [isOpen, resetTransform])

  // Закрытие по Escape
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isOpen) return
      if (e.key === 'Escape') {
        resetTransform()
        onClose()
      }
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [isOpen, onClose, resetTransform])

  // Получить расстояние между двумя тач-точками
  const getDistance = (touches: TouchList): number => {
    const dx = touches[0].clientX - touches[1].clientX
    const dy = touches[0].clientY - touches[1].clientY
    return Math.sqrt(dx * dx + dy * dy)
  }

  // --- Touch handlers ---

  const handleTouchStart = useCallback((e: React.TouchEvent) => {
    if (e.touches.length === 2) {
      // Начало пинча
      e.preventDefault()
      pinchRef.current = {
        active: true,
        startDistance: getDistance(e.touches),
        startScale: transformRef.current.scale,
      }
      // Отменяем активный драг
      dragRef.current.active = false
    } else if (e.touches.length === 1 && transformRef.current.scale > 1) {
      // Драг одним пальцем при увеличенном состоянии
      dragRef.current = {
        active: true,
        startX: e.touches[0].clientX,
        startY: e.touches[0].clientY,
        startTransX: transformRef.current.x,
        startTransY: transformRef.current.y,
      }
    }
  }, [])

  const handleTouchMove = useCallback((e: React.TouchEvent) => {
    if (e.touches.length === 2 && pinchRef.current.active) {
      e.preventDefault()
      const currentDistance = getDistance(e.touches)
      const ratio = currentDistance / pinchRef.current.startDistance
      let newScale = pinchRef.current.startScale * ratio
      // Ограничиваем зум от 1x до 5x
      newScale = Math.min(Math.max(newScale, 1), 5)
      transformRef.current.scale = newScale
      // При пинче сбрасываем смещение к центру
      transformRef.current.x = 0
      transformRef.current.y = 0
      applyTransform()
    } else if (e.touches.length === 1 && dragRef.current.active) {
      e.preventDefault()
      const dx = e.touches[0].clientX - dragRef.current.startX
      const dy = e.touches[0].clientY - dragRef.current.startY
      transformRef.current.x = dragRef.current.startTransX + dx
      transformRef.current.y = dragRef.current.startTransY + dy
      applyTransform()
    }
  }, [applyTransform])

  const handleTouchEnd = useCallback((e: React.TouchEvent) => {
    if (e.touches.length < 2) {
      pinchRef.current.active = false
    }
    if (e.touches.length === 0) {
      dragRef.current.active = false
      // Если зум вернулся к 1 — сбрасываем позицию
      if (transformRef.current.scale <= 1) {
        resetTransform()
      }
    }
  }, [resetTransform])

  // Тап по картинке: если увеличена — сбросить, если нет — закрыть
  const handleImageClick = useCallback((e: React.MouseEvent) => {
    e.stopPropagation()
    if (transformRef.current.scale > 1) {
      resetTransform()
    } else {
      onClose()
    }
  }, [onClose, resetTransform])

  // Тап по фону — закрыть
  const handleBgClick = useCallback(() => {
    resetTransform()
    onClose()
  }, [onClose, resetTransform])

  // Колёсико мыши для зума на десктопе
  const handleWheel = useCallback((e: React.WheelEvent) => {
    e.preventDefault()
    const delta = e.deltaY > 0 ? 0.9 : 1.1
    let newScale = transformRef.current.scale * delta
    newScale = Math.min(Math.max(newScale, 1), 5)
    transformRef.current.scale = newScale
    if (newScale <= 1) {
      transformRef.current.x = 0
      transformRef.current.y = 0
    }
    applyTransform()
  }, [applyTransform])

  if (!isOpen) return null

  return createPortal(
    <div
      ref={containerRef}
      className="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 animate-[fadeIn_150ms_ease-out]"
      onClick={handleBgClick}
      style={{ touchAction: 'none' }}
    >
      <img
        ref={imgRef}
        src={src}
        alt={alt || ''}
        className="max-h-[95vh] max-w-[95vw] object-contain rounded-lg 
                   animate-[scaleIn_200ms_ease-out] cursor-pointer
                   transition-transform duration-75 ease-out select-none"
        style={{ transformOrigin: 'center center' }}
        onClick={handleImageClick}
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onTouchEnd={handleTouchEnd}
        onWheel={handleWheel}
        draggable={false}
      />
    </div>,
    document.body
  )
}
