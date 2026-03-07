'use client'

import React, { useMemo, useState } from 'react'
import { 
  Lightbulb, BookOpen, CheckCircle, Star, AlertTriangle, 
  Sparkles, Target, HelpCircle, Info, Award, ExternalLink
} from 'lucide-react'

interface LessonContentRendererProps {
  content: string
  onOpenLiteraryWork?: (workId: string) => void
}

// Парсер контента урока с расширенным форматированием
export default function LessonContentRenderer({ content, onOpenLiteraryWork }: LessonContentRendererProps) {
  const parsedContent = useMemo(() => {
    if (!content) return []
    
    const lines = content.split('\n')
    const elements: React.ReactElement[] = []
    
    let currentList: { type: 'bullet' | 'numbered' | 'none', items: string[] } = { type: 'none', items: [] }
    let inCodeBlock = false
    let codeLines: string[] = []
    
    const flushList = () => {
      if (currentList.items.length > 0 && currentList.type !== 'none') {
        if (currentList.type === 'bullet') {
          elements.push(
            <div key={`list-${elements.length}`} className="my-4 space-y-2">
              {currentList.items.map((item, idx) => (
                <div key={idx} className="flex items-start gap-3 p-3 bg-white/5 rounded-xl border border-white/10 hover:bg-white/10 transition-all">
                  <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-white text-sm flex-shrink-0 mt-0.5">
                    {idx + 1}
                  </div>
                  <span className="text-white/90 text-base leading-relaxed">{parseInlineFormatting(item)}</span>
                </div>
              ))}
            </div>
          )
        } else if (currentList.type === 'numbered') {
          elements.push(
            <div key={`list-${elements.length}`} className="my-4 space-y-2">
              {currentList.items.map((item, idx) => (
                <div key={idx} className="flex items-start gap-3 p-3 bg-gradient-to-r from-blue-500/20 to-cyan-500/20 rounded-xl border border-blue-400/30 hover:border-blue-400/50 transition-all">
                  <div className="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-cyan-400 flex items-center justify-center text-white text-xs flex-shrink-0 mt-0.5 font-bold">
                    {idx + 1}
                  </div>
                  <span className="text-white/90 text-base leading-relaxed">{parseInlineFormatting(item)}</span>
                </div>
              ))}
            </div>
          )
        }
      }
      currentList = { type: 'none', items: [] }
    }
    
    const parseInlineFormatting = (text: string): React.ReactNode => {
      // Bold text **text**
      const parts = text.split(/(\*\*.+?\*\*)/g)
      return parts.map((part, idx) => {
        if (part.startsWith('**') && part.endsWith('**')) {
          return <strong key={idx} className="text-yellow-300 font-bold">{part.slice(2, -2)}</strong>
        }
        return part
      })
    }
    
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim()
      const originalLine = lines[i]
      
      // Detect code blocks
      if (line.startsWith('```')) {
        if (inCodeBlock) {
          // End code block
          if (codeLines.length > 0) {
            elements.push(
              <div key={`code-${elements.length}`} className="my-4 bg-slate-900/80 rounded-xl p-4 border border-cyan-500/30 font-mono text-sm overflow-x-auto">
                <pre className="text-cyan-300 whitespace-pre-wrap">{codeLines.join('\n')}</pre>
              </div>
            )
          }
          codeLines = []
          inCodeBlock = false
        } else {
          // Start code block
          flushList()
          inCodeBlock = true
        }
        continue
      }
      
      if (inCodeBlock) {
        codeLines.push(originalLine)
        continue
      }
      
      // Skip empty lines but create spacing
      if (!line) {
        flushList()
        if (elements.length > 0) {
          elements.push(<div key={`space-${i}`} className="h-3" />)
        }
        continue
      }
      
      // Main header (## Title)
      if (line.startsWith('## ')) {
        flushList()
        elements.push(
          <div key={`h2-${i}`} className="mt-6 mb-4 flex items-center gap-3">
            <div className="h-1 w-8 bg-gradient-to-r from-yellow-400 to-orange-500 rounded-full"></div>
            <h2 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-orange-300 to-red-400">
              {line.replace('## ', '')}
            </h2>
            <div className="flex-1 h-1 bg-gradient-to-r from-yellow-400/50 to-transparent rounded-full"></div>
          </div>
        )
        continue
      }
      
      // Sub-header (# Title)
      if (line.startsWith('# ')) {
        flushList()
        elements.push(
          <div key={`h3-${i}`} className="mt-5 mb-3 flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-yellow-400 flex-shrink-0" />
            <h3 className="text-xl font-bold text-yellow-200">
              {line.replace('# ', '')}
            </h3>
          </div>
        )
        continue
      }
      
      // Important block with border (!!! text)
      if (line.startsWith('!!! ')) {
        flushList()
        elements.push(
          <div key={`important-${i}`} className="my-4 p-4 bg-gradient-to-r from-amber-500/20 to-orange-500/20 rounded-2xl border-2 border-amber-400/50 shadow-lg">
            <div className="flex items-center gap-3 mb-2">
              <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0" />
              <span className="text-amber-300 font-bold text-lg">Важно!</span>
            </div>
            <p className="text-white/90 text-base">{parseInlineFormatting(line.replace('!!! ', ''))}</p>
          </div>
        )
        continue
      }
      
      // Tip block with icon (!! text)
      if (line.startsWith('!! ')) {
        flushList()
        elements.push(
          <div key={`tip-${i}`} className="my-4 p-4 bg-gradient-to-r from-cyan-500/20 to-blue-500/20 rounded-2xl border border-cyan-400/30">
            <div className="flex items-center gap-3 mb-2">
              <Lightbulb className="w-5 h-5 text-cyan-400 flex-shrink-0" />
              <span className="text-cyan-300 font-bold">💡 Подсказка</span>
            </div>
            <p className="text-white/90 text-base">{parseInlineFormatting(line.replace('!! ', ''))}</p>
          </div>
        )
        continue
      }
      
      // Note/Info block (! text)
      if (line.startsWith('! ')) {
        flushList()
        elements.push(
          <div key={`note-${i}`} className="my-3 p-4 bg-gradient-to-r from-violet-500/20 to-purple-500/20 rounded-xl border border-violet-400/30">
            <div className="flex items-center gap-3">
              <Info className="w-5 h-5 text-violet-400 flex-shrink-0" />
              <p className="text-white/90 text-base">{parseInlineFormatting(line.replace('! ', ''))}</p>
            </div>
          </div>
        )
        continue
      }
      
      // Example block (> text)
      if (line.startsWith('> ')) {
        flushList()
        elements.push(
          <div key={`example-${i}`} className="my-3 p-4 bg-gradient-to-r from-green-500/20 to-emerald-500/20 rounded-xl border border-green-400/30">
            <div className="flex items-center gap-3">
              <Target className="w-5 h-5 text-green-400 flex-shrink-0" />
              <span className="text-green-300 font-medium">Пример:</span>
            </div>
            <p className="text-white/90 text-base mt-1">{parseInlineFormatting(line.replace('> ', ''))}</p>
          </div>
        )
        continue
      }
      
      // Warning block (? text)
      if (line.startsWith('? ')) {
        flushList()
        elements.push(
          <div key={`warning-${i}`} className="my-3 p-4 bg-gradient-to-r from-rose-500/20 to-pink-500/20 rounded-xl border border-rose-400/30">
            <div className="flex items-center gap-3">
              <HelpCircle className="w-5 h-5 text-rose-400 flex-shrink-0" />
              <span className="text-rose-300 font-medium">⚠️ Внимание!</span>
            </div>
            <p className="text-white/90 text-base mt-1">{parseInlineFormatting(line.replace('? ', ''))}</p>
          </div>
        )
        continue
      }
      
      // Success/Check block (+ text)
      if (line.startsWith('+ ')) {
        flushList()
        elements.push(
          <div key={`check-${i}`} className="my-3 p-4 bg-gradient-to-r from-emerald-500/20 to-teal-500/20 rounded-xl border border-emerald-400/30">
            <div className="flex items-center gap-3">
              <CheckCircle className="w-5 h-5 text-emerald-400 flex-shrink-0" />
              <p className="text-white/90 text-base">{parseInlineFormatting(line.replace('+ ', ''))}</p>
            </div>
          </div>
        )
        continue
      }
      
      // Award/Achievement block (* text)
      if (line.startsWith('* ')) {
        flushList()
        elements.push(
          <div key={`award-${i}`} className="my-3 p-4 bg-gradient-to-r from-yellow-500/20 to-amber-500/20 rounded-xl border border-yellow-400/30">
            <div className="flex items-center gap-3">
              <Award className="w-5 h-5 text-yellow-400 flex-shrink-0" />
              <p className="text-white/90 text-base">{parseInlineFormatting(line.replace('* ', ''))}</p>
            </div>
          </div>
        )
        continue
      }
      
      // Definition block (:- text)
      if (line.startsWith(':- ')) {
        flushList()
        elements.push(
          <div key={`def-${i}`} className="my-3 p-4 bg-gradient-to-r from-indigo-500/20 to-violet-500/20 rounded-xl border-l-4 border-indigo-400/50">
            <div className="flex items-center gap-3">
              <BookOpen className="w-5 h-5 text-indigo-400 flex-shrink-0" />
              <span className="text-indigo-300 font-medium">📖 Определение:</span>
            </div>
            <p className="text-white/90 text-base mt-2 font-medium">{parseInlineFormatting(line.replace(':- ', ''))}</p>
          </div>
        )
        continue
      }
      
      // Literary work link [[work-id|text]]
      const literaryMatch = line.match(/\[\[(.+?)\|(.+?)\]\]/)
      if (literaryMatch) {
        flushList()
        const workId = literaryMatch[1]
        const linkText = literaryMatch[2]
        elements.push(
          <div key={`literary-${i}`} className="my-4 p-4 bg-gradient-to-r from-amber-500/20 to-orange-500/20 rounded-2xl border-2 border-amber-400/40 cursor-pointer hover:border-amber-400/60 transition-all"
                   onClick={() => onOpenLiteraryWork?.(workId)}>
            <div className="flex items-center gap-3">
              <BookOpen className="w-6 h-6 text-amber-400 flex-shrink-0" />
              <div>
                <p className="text-amber-200 font-medium">Читать полный текст:</p>
                <p className="text-white font-bold text-lg">{linkText}</p>
              </div>
              <ExternalLink className="w-5 h-5 text-amber-400 ml-auto flex-shrink-0" />
            </div>
          </div>
        )
        continue
      }
      
      // Bullet list item (- text)
      if (line.startsWith('- ')) {
        if (currentList.type !== 'bullet') {
          flushList()
          currentList = { type: 'bullet', items: [] }
        }
        currentList.items.push(line.substring(2))
        continue
      }
      
      // Numbered list item (1. text)
      if (/^\d+\.\s/.test(line)) {
        if (currentList.type !== 'numbered') {
          flushList()
          currentList = { type: 'numbered', items: [] }
        }
        currentList.items.push(line.replace(/^\d+\.\s/, ''))
        continue
      }
      
      // Bold header (**text**)
      if (line.startsWith('**') && line.endsWith('**') && !line.slice(2, -2).includes('**')) {
        flushList()
        elements.push(
          <div key={`bold-${i}`} className="mt-5 mb-3 p-3 bg-gradient-to-r from-purple-500/30 to-pink-500/30 rounded-xl border border-purple-400/40">
            <h4 className="text-lg font-bold text-white flex items-center gap-2">
              <Star className="w-5 h-5 text-yellow-400 flex-shrink-0" />
              {line.replace(/\*\*/g, '')}
            </h4>
          </div>
        )
        continue
      }
      
      // Regular text with inline formatting
      flushList()
      
      // Check if line starts with bold text
      const boldMatch = line.match(/^\*\*(.+?)\*\*:?/)
      if (boldMatch) {
        const restOfLine = line.replace(/^\*\*.+?\*\*:?\s*/, '')
        elements.push(
          <div key={`text-${i}`} className="my-2 flex items-start gap-2">
            <span className="px-3 py-1 bg-gradient-to-r from-orange-500/40 to-amber-500/40 rounded-lg text-amber-200 font-bold text-base">
              {boldMatch[1]}:
            </span>
            <span className="text-white/90 text-base leading-relaxed flex-1">{parseInlineFormatting(restOfLine)}</span>
          </div>
        )
        continue
      }
      
      // Regular paragraph
      elements.push(
        <p key={`p-${i}`} className="text-white/90 text-base leading-relaxed my-1">
          {parseInlineFormatting(line)}
        </p>
      )
    }
    
    // Flush remaining list
    flushList()
    
    return elements
  }, [content, onOpenLiteraryWork])
  
  if (!content) return null
  
  return (
    <div className="lesson-content">
      {parsedContent}
    </div>
  )
}
