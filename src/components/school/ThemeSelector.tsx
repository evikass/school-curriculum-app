'use client'

import { useState, createContext, useContext } from 'react'
import { Palette } from 'lucide-react'

const ThemeContext = createContext({ theme: 'default', setTheme: (t: string) => {} })

export const useTheme = () => useContext(ThemeContext)

export default function ThemeSelector() {
  const [theme, setTheme] = useState('default')

  return (
    <button
      onClick={() => setTheme(theme === 'default' ? 'dark' : 'default')}
      className="text-pink-400 text-xs bg-pink-400/20 px-3 py-1 rounded-full hover:bg-pink-400/30 transition-colors"
    >
      <Palette className="w-3 h-3 inline" /> Тема
    </button>
  )
}
