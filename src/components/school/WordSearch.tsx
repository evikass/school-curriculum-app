'use client'

<<<<<<< HEAD
import { useState, useCallback, useEffect } from 'react'
import { Search, Check, RotateCcw, Trophy, Eye } from 'lucide-react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from './SoundToggle'

interface WordSearchPuzzle {
  grid: string[][]
  words: string[]
  category: string
  difficulty: 'easy' | 'medium' | 'hard'
}

const puzzles: WordSearchPuzzle[] = [
  {
    difficulty: 'easy',
    category: 'Животные',
    words: ['КОТ', 'СОБАКА', 'ЛИСА'],
    grid: [
      ['К', 'О', 'Т', 'А', 'Б'],
      ['С', 'О', 'Л', 'И', 'С'],
      ['А', 'Б', 'И', 'К', 'А'],
      ['К', 'А', 'С', 'А', 'Л'],
      ['А', 'Н', 'А', 'П', 'И'],
    ]
  },
  {
    difficulty: 'easy',
    category: 'Фрукты',
    words: ['ЯБЛОКО', 'ГРУША', 'СЛИВА'],
    grid: [
      ['Я', 'Б', 'Л', 'О', 'К', 'О'],
      ['Г', 'Р', 'У', 'Ш', 'А', 'Н'],
      ['С', 'Л', 'И', 'В', 'А', 'Т'],
      ['К', 'О', 'Р', 'А', 'Б', 'Л'],
      ['Я', 'Г', 'О', 'Д', 'А', 'М'],
      ['Ф', 'Р', 'У', 'К', 'Т', 'Ы'],
    ]
  },
  {
    difficulty: 'medium',
    category: 'Школа',
    words: ['УРОК', 'ПАРТА', 'ДОСКА', 'МЕЛ', 'КНИГА'],
    grid: [
      ['У', 'Р', 'О', 'К', 'А', 'Б', 'В'],
      ['П', 'А', 'Р', 'Т', 'А', 'Г', 'Д'],
      ['Д', 'О', 'С', 'К', 'А', 'Е', 'Ж'],
      ['М', 'Е', 'Л', 'О', 'Н', 'И', 'З'],
      ['К', 'Н', 'И', 'Г', 'А', 'К', 'И'],
      ['Р', 'У', 'Ч', 'К', 'А', 'И', 'Й'],
      ['Т', 'Е', 'Т', 'Р', 'А', 'Д', 'Ь'],
    ]
  },
  {
    difficulty: 'hard',
    category: 'Природа',
    words: ['СОЛНЦЕ', 'ЗВЕЗДЫ', 'ОБЛАКА', 'ГОРА', 'РЕКА', 'ЛЕС'],
    grid: [
      ['С', 'О', 'Л', 'Н', 'Ц', 'Е', 'А', 'Б'],
      ['З', 'В', 'Е', 'З', 'Д', 'Ы', 'Г', 'В'],
      ['О', 'Б', 'Л', 'А', 'К', 'А', 'Д', 'Е'],
      ['Г', 'О', 'Р', 'А', 'Н', 'И', 'Ж', 'З'],
      ['Р', 'Е', 'К', 'А', 'Т', 'О', 'И', 'К'],
      ['Л', 'Е', 'С', 'О', 'К', 'Л', 'Й', 'Л'],
      ['М', 'О', 'Р', 'Е', 'П', 'М', 'М', 'М'],
      ['Н', 'Е', 'Б', 'О', 'Р', 'У', 'Н', 'О'],
    ]
  }
=======
import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Search } from 'lucide-react'

const PUZZLES = [
  { word: 'КОТ', grid: ['КОТКА', 'ПОЛЕТ', 'ТОЧКА', 'КНИГА', 'ОКНО'], positions: [[0,0], [0,1], [0,2]] },
  { word: 'МИР', grid: ['МИРРА', 'ИКРАН', 'РЫБАК', 'МОРЕ'], positions: [[0,0], [0,1], [0,2]] },
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
]

export default function WordSearch() {
  const { addXP } = useSchool()
<<<<<<< HEAD
  const { playSound } = useSound()
  
  const [currentPuzzle, setCurrentPuzzle] = useState<WordSearchPuzzle | null>(null)
  const [selectedCells, setSelectedCells] = useState<Set<string>>(new Set())
  const [foundWords, setFoundWords] = useState<Set<string>>(new Set())
  const [isSelecting, setIsSelecting] = useState(false)
  const [startCell, setStartCell] = useState<{ row: number; col: number } | null>(null)
  const [completed, setCompleted] = useState(false)
  const [showHint, setShowHint] = useState(false)

  const startPuzzle = useCallback((puzzle: WordSearchPuzzle) => {
    setCurrentPuzzle(puzzle)
    setSelectedCells(new Set())
    setFoundWords(new Set())
    setIsSelecting(false)
    setStartCell(null)
    setCompleted(false)
    setShowHint(false)
  }, [])

  const handleCellMouseDown = useCallback((row: number, col: number) => {
    setIsSelecting(true)
    setStartCell({ row, col })
    setSelectedCells(new Set([`${row}-${col}`]))
  }, [])

  const handleCellMouseEnter = useCallback((row: number, col: number) => {
    if (!isSelecting || !startCell) return
    
    const newSelected = new Set<string>()
    
    // Determine direction and fill cells
    const dRow = Math.sign(row - startCell.row)
    const dCol = Math.sign(col - startCell.col)
    
    // Only allow horizontal, vertical, or diagonal
    if (dRow !== 0 && dCol !== 0 && Math.abs(row - startCell.row) !== Math.abs(col - startCell.col)) {
      return
    }
    
    let r = startCell.row
    let c = startCell.col
    
    while (true) {
      newSelected.add(`${r}-${c}`)
      if (r === row && c === col) break
      r += dRow
      c += dCol
    }
    
    setSelectedCells(newSelected)
  }, [isSelecting, startCell])

  const handleMouseUp = useCallback(() => {
    if (!currentPuzzle || selectedCells.size === 0) return
    
    // Get selected word
    const cells = Array.from(selectedCells).sort((a, b) => {
      const [aRow, aCol] = a.split('-').map(Number)
      const [bRow, bCol] = b.split('-').map(Number)
      return aRow !== bRow ? aRow - bRow : aCol - bCol
    })
    
    const word = cells.map(cell => {
      const [row, col] = cell.split('-').map(Number)
      return currentPuzzle.grid[row][col]
    }).join('')
    
    const reversedWord = word.split('').reverse().join('')
    
    // Check if word is valid
    if (currentPuzzle.words.includes(word) && !foundWords.has(word)) {
      playSound?.('success')
      setFoundWords(prev => new Set([...prev, word]))
      addXP(currentPuzzle.difficulty === 'easy' ? 8 : currentPuzzle.difficulty === 'medium' ? 12 : 18)
    } else if (currentPuzzle.words.includes(reversedWord) && !foundWords.has(reversedWord)) {
      playSound?.('success')
      setFoundWords(prev => new Set([...prev, reversedWord]))
      addXP(currentPuzzle.difficulty === 'easy' ? 8 : currentPuzzle.difficulty === 'medium' ? 12 : 18)
    }
    
    setIsSelecting(false)
    setStartCell(null)
    setSelectedCells(new Set())
  }, [currentPuzzle, selectedCells, foundWords, playSound, addXP])

  // Check for completion
  useEffect(() => {
    if (currentPuzzle && foundWords.size === currentPuzzle.words.length) {
      setCompleted(true)
    }
  }, [foundWords, currentPuzzle])

  if (!currentPuzzle) {
    return (
      <div className="bg-gradient-to-br from-cyan-900/90 to-blue-900/90 rounded-2xl p-6 backdrop-blur-sm border border-cyan-500/30">
        <h2 className="text-2xl font-bold text-cyan-200 mb-4 flex items-center gap-2">
          <Search className="w-6 h-6" />
          Поиск слов
        </h2>
        <p className="text-cyan-100/80 mb-6">
          Найди все скрытые слова в сетке букв! Выбирай буквы, перетаскивая мышкой.
        </p>
        <div className="flex flex-col gap-3">
          {puzzles.map((puzzle, index) => (
            <button
              key={index}
              onClick={() => startPuzzle(puzzle)}
              className={`p-4 rounded-xl text-left transition-all hover:scale-[1.02] ${
                puzzle.difficulty === 'easy' 
                  ? 'bg-green-500/30 hover:bg-green-500/40 text-green-200'
                  : puzzle.difficulty === 'medium'
                  ? 'bg-yellow-500/30 hover:bg-yellow-500/40 text-yellow-200'
                  : 'bg-red-500/30 hover:bg-red-500/40 text-red-200'
              }`}
            >
              <div className="font-bold">
                {puzzle.category} ({puzzle.difficulty === 'easy' ? 'Легко' : puzzle.difficulty === 'medium' ? 'Средне' : 'Сложно'})
              </div>
              <div className="text-sm opacity-70">
                {puzzle.words.length} слов • {puzzle.grid.length}×{puzzle.grid[0].length}
              </div>
            </button>
          ))}
        </div>
      </div>
    )
  }

  if (completed) {
    const xpGained = currentPuzzle.words.length * (currentPuzzle.difficulty === 'easy' ? 8 : currentPuzzle.difficulty === 'medium' ? 12 : 18)
    return (
      <div className="bg-gradient-to-br from-cyan-900/90 to-blue-900/90 rounded-2xl p-6 backdrop-blur-sm border border-cyan-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-cyan-200 mb-2">Отлично!</h2>
        <p className="text-cyan-100 mb-4">Все слова найдены!</p>
        <p className="text-2xl font-bold text-yellow-400 mb-2">{foundWords.size}/{currentPuzzle.words.length} слов</p>
        <p className="text-xl text-green-400 mb-6">+{xpGained} XP</p>
        <button
          onClick={() => setCurrentPuzzle(null)}
          className="px-6 py-3 bg-cyan-500 hover:bg-cyan-400 text-white font-bold rounded-xl transition-all"
        >
          Новый поиск
        </button>
      </div>
    )
  }

  return (
    <div className="bg-gradient-to-br from-cyan-900/90 to-blue-900/90 rounded-2xl p-6 backdrop-blur-sm border border-cyan-500/30"
      onMouseUp={handleMouseUp}
      onMouseLeave={handleMouseUp}
    >
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-cyan-200 flex items-center gap-2">
          <Search className="w-5 h-5" />
          Поиск слов
        </h2>
        <span className="text-cyan-300 text-sm">{currentPuzzle.category}</span>
      </div>

      {/* Words to find */}
      <div className="mb-4 flex flex-wrap gap-2 justify-center">
        {currentPuzzle.words.map(word => (
          <span
            key={word}
            className={`px-3 py-1 rounded-full text-sm font-medium ${
              foundWords.has(word) 
                ? 'bg-green-500/30 text-green-300 line-through' 
                : 'bg-cyan-800/50 text-cyan-200'
            }`}
          >
            {word}
          </span>
        ))}
      </div>

      {/* Grid */}
      <div className="flex justify-center mb-4">
        <div className="inline-grid gap-1 bg-cyan-950 p-2 rounded-lg select-none">
          {currentPuzzle.grid.map((row, rowIndex) => (
            <div key={rowIndex} className="flex gap-1">
              {row.map((cell, colIndex) => {
                const isSelected = selectedCells.has(`${rowIndex}-${colIndex}`)
                const isPartOfFound = Array.from(foundWords).some(word => {
                  // Check if this cell is part of a found word
                  return false // Simplified for now
                })
                
                return (
                  <div
                    key={colIndex}
                    onMouseDown={() => handleCellMouseDown(rowIndex, colIndex)}
                    onMouseEnter={() => handleCellMouseEnter(rowIndex, colIndex)}
                    className={`w-8 h-8 flex items-center justify-center font-bold text-sm cursor-pointer rounded transition-colors ${
                      isSelected
                        ? 'bg-yellow-500 text-gray-900'
                        : isPartOfFound
                        ? 'bg-green-500/50 text-white'
                        : 'bg-cyan-800/50 text-cyan-100 hover:bg-cyan-700/50'
                    }`}
                  >
                    {cell}
                  </div>
                )
              })}
            </div>
          ))}
        </div>
      </div>

      {/* Progress */}
      <div className="text-center mb-4">
        <span className="text-cyan-200">
          Найдено: {foundWords.size} / {currentPuzzle.words.length}
        </span>
      </div>

      {/* Controls */}
      <div className="flex flex-wrap gap-2 justify-center">
        <button
          onClick={() => setShowHint(!showHint)}
          className="px-4 py-2 bg-cyan-700/50 hover:bg-cyan-600/50 text-cyan-200 rounded-lg transition-all flex items-center gap-2"
        >
          <Eye className="w-4 h-4" />
          {showHint ? 'Скрыть' : 'Подсказка'}
        </button>
        <button
          onClick={() => startPuzzle(currentPuzzle)}
          className="px-4 py-2 bg-cyan-700/50 hover:bg-cyan-600/50 text-cyan-200 rounded-lg transition-all flex items-center gap-2"
        >
          <RotateCcw className="w-4 h-4" />
          Заново
        </button>
        <button
          onClick={() => setCurrentPuzzle(null)}
          className="px-4 py-2 bg-cyan-600/50 hover:bg-cyan-600 text-cyan-200 rounded-lg transition-all"
        >
          Назад
        </button>
      </div>

      {/* Hint */}
      {showHint && (
        <div className="mt-4 text-center text-cyan-300 text-sm">
          Слова могут быть расположены горизонтально, вертикально или по диагонали
        </div>
      )}
=======
  const [index, setIndex] = useState(0)
  const [found, setFound] = useState<Set<string>>(new Set())
  const [score, setScore] = useState(0)

  const puzzle = PUZZLES[index]
  const wordFound = puzzle.word.split('').every((_, i) => found.has(`${puzzle.positions[i][0]}-${puzzle.positions[i][1]}`))

  const toggle = (r: number, c: number) => {
    const key = `${r}-${c}`
    const newFound = new Set(found)
    if (newFound.has(key)) {
      newFound.delete(key)
    } else {
      newFound.add(key)
    }
    setFound(newFound)
  }

  const checkWord = () => {
    if (wordFound) {
      addXP(20)
      setScore(s => s + 1)
    }
    setFound(new Set())
    setIndex(i => (i + 1) % PUZZLES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-teal-500/20 border-2 border-cyan-500/30">
      <h3 className="text-xl font-bold text-white mb-2">🔍 Поиск слов</h3>
      <p className="text-cyan-300 mb-4">Найди слово: <span className="font-bold">{puzzle.word}</span></p>
      <div className="flex flex-col gap-1 mb-4">
        {puzzle.grid.map((row, r) => (
          <div key={r} className="flex gap-1">
            {row.split('').map((char, c) => (
              <button
                key={c}
                onClick={() => toggle(r, c)}
                className={`w-10 h-10 rounded-lg font-bold transition-all ${
                  found.has(`${r}-${c}`)
                    ? 'bg-cyan-500 text-white'
                    : 'bg-white/10 text-white hover:bg-white/20'
                }`}
              >
                {char}
              </button>
            ))}
          </div>
        ))}
      </div>
      <button onClick={checkWord} className="w-full py-3 bg-cyan-500 text-white rounded-xl font-bold">
        Проверить
      </button>
      <p className="text-center text-purple-300 mt-4">Найдено: {score}</p>
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
    </div>
  )
}
