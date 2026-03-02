'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { Volume2, RefreshCw, Star } from 'lucide-react'

const VOWELS = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
const CONSONANTS = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
const LETTERS = [...VOWELS, ...CONSONANTS]

const HARD_MODE_WORDS = [
  { word: 'ЯБЛОКО', vowelCount: 3, consonantCount: 3 },
  { word: 'МОЛОКО', vowelCount: 3, consonantCount: 3 },
  { word: 'СОЛНЦЕ', vowelCount: 2, consonantCount: 4 },
  { word: 'МЕДВЕДЬ', vowelCount: 2, consonantCount: 4 },
  { word: 'УЧЕНИК', vowelCount: 3, consonantCount: 3 },
  { word: 'ТЕТРАДЬ', vowelCount: 3, consonantCount: 4 },
  { word: 'КАРАНДАШ', vowelCount: 3, consonantCount: 5 },
  { word: 'ПЕНАЛ', vowelCount: 2, consonantCount: 3 },
  { word: 'РУЧКА', vowelCount: 2, consonantCount: 3 },
  { word: 'КНИГА', vowelCount: 2, consonantCount: 3 },
  { word: 'ПАРТА', vowelCount: 2, consonantCount: 3 },
  { word: 'ДОСКА', vowelCount: 2, consonantCount: 3 },
  { word: 'ШКОЛА', vowelCount: 2, consonantCount: 3 },
  { word: 'ВЕСНА', vowelCount: 2, consonantCount: 3 },
  { word: 'ЗИМА', vowelCount: 2, consonantCount: 2 },
  { word: 'ЛЕТО', vowelCount: 2, consonantCount: 2 },
  { word: 'ОСЕНЬ', vowelCount: 2, consonantCount: 3 },
  { word: 'ДЕТИ', vowelCount: 2, consonantCount: 2 },
  { word: 'МАМА', vowelCount: 2, consonantCount: 2 },
  { word: 'ПАПА', vowelCount: 2, consonantCount: 2 },
]

type GameMode = 'sort' | 'count'

export default function VowelsConsonants() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('sort')
  const [currentLetter, setCurrentLetter] = useState('')
  const [currentWord, setCurrentWord] = useState<typeof HARD_MODE_WORDS[0] | null>(null)
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  const [usedLetters, setUsedLetters] = useState<string[]>([])
  const [usedWords, setUsedWords] = useState<number[]>([])

  const getRandomLetter = () => {
    const available = LETTERS.filter(l => !usedLetters.includes(l))
    if (available.length === 0) {
      setUsedLetters([])
      return LETTERS[Math.floor(Math.random() * LETTERS.length)]
    }
    return available[Math.floor(Math.random() * available.length)]
  }

  const getRandomWord = () => {
    const availableIndices = HARD_MODE_WORDS.map((_, i) => i).filter(i => !usedWords.includes(i))
    if (availableIndices.length === 0) {
      setUsedWords([])
      return HARD_MODE_WORDS[Math.floor(Math.random() * HARD_MODE_WORDS.length)]
    }
    return HARD_MODE_WORDS[availableIndices[Math.floor(Math.random() * availableIndices.length)]]
  }

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    if (mode === 'sort') {
      setCurrentLetter(getRandomLetter())
    } else {
      setCurrentWord(getRandomWord())
    }
  }, [mode])

  const handleLetterAnswer = (isVowel: boolean) => {
    const correct = isVowel ? VOWELS.includes(currentLetter) : CONSONANTS.includes(currentLetter)
    
    if (correct) {
      playCorrect()
      setScore(s => s + 10)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(5 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      const letter = getRandomLetter()
      setCurrentLetter(letter)
      setUsedLetters(u => [...u, currentLetter])
    }, 800)
  }

  const handleWordAnswer = (vowelAnswer: number, consonantAnswer: number) => {
    if (!currentWord) return
    
    const correct = vowelAnswer === currentWord.vowelCount && consonantAnswer === currentWord.consonantCount
    
    if (correct) {
      playCorrect()
      setScore(s => s + 20)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(10 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      const word = getRandomWord()
      setCurrentWord(word)
      setUsedWords(u => [...u, HARD_MODE_WORDS.indexOf(currentWord)])
    }, 1200)
  }

  const reset = () => {
    if (mode === 'sort') {
      setUsedLetters([])
      setCurrentLetter(getRandomLetter())
    } else {
      setUsedWords([])
      setCurrentWord(getRandomWord())
    }
    setScore(0)
    setStreak(0)
  }

  return (
    <div className="bg-gradient-to-br from-pink-500/20 to-purple-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">🔤</span> Гласные и Согласные
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4">
        <button
          onClick={() => { setMode('sort'); reset() }}
          className={`flex-1 py-2 rounded-lg font-medium transition-all ${mode === 'sort' ? 'bg-pink-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
        >
          🎯 Раздели буквы
        </button>
        <button
          onClick={() => { setMode('count'); reset() }}
          className={`flex-1 py-2 rounded-lg font-medium transition-all ${mode === 'count' ? 'bg-purple-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
        >
          📊 Посчитай в слове
        </button>
      </div>

      {mode === 'sort' ? (
        <div className="text-center">
          <div className={`text-9xl font-black mb-6 transition-transform ${feedback === 'correct' ? 'scale-125 text-green-400' : feedback === 'wrong' ? 'scale-75 text-red-400' : 'text-white'}`}>
            {currentLetter}
          </div>
          
          <div className="flex justify-center gap-4 mb-4">
            <button
              onClick={() => handleLetterAnswer(true)}
              className="px-8 py-4 bg-gradient-to-r from-pink-500 to-red-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
            >
              Гласная
            </button>
            <button
              onClick={() => handleLetterAnswer(false)}
              className="px-8 py-4 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
            >
              Согласная
            </button>
          </div>

          <div className="flex justify-center gap-4 text-sm">
            <div className="bg-pink-500/20 rounded-lg px-4 py-2">
              <div className="text-pink-300">Гласные (10)</div>
              <div className="text-white font-mono text-xs">А Е Ё И О У Ы Э Ю Я</div>
            </div>
            <div className="bg-blue-500/20 rounded-lg px-4 py-2">
              <div className="text-blue-300">Согласные (21)</div>
              <div className="text-white font-mono text-xs">Б В Г Д Ж З Й К Л М Н П Р С Т Ф Х Ц Ч Ш Щ</div>
            </div>
          </div>
        </div>
      ) : (
        <div className="text-center">
          {currentWord && (
            <>
              <div className="mb-2 text-white/60">Сколько гласных и согласных в слове?</div>
              <div className={`text-5xl font-black mb-6 tracking-wider ${feedback === 'correct' ? 'text-green-400' : feedback === 'wrong' ? 'text-red-400' : 'text-white'}`}>
                {currentWord.word}
              </div>
              
              <div className="flex justify-center gap-4 mb-4">
                <div className="flex flex-col items-center gap-2">
                  <span className="text-pink-300">Гласных:</span>
                  <div className="flex gap-2">
                    {[0, 1, 2, 3, 4, 5].map(n => (
                      <button
                        key={`v${n}`}
                        onClick={() => handleWordAnswer(n, currentWord.consonantCount)}
                        className="w-10 h-10 rounded-lg bg-pink-500/30 text-white font-bold hover:bg-pink-500/50 transition-colors"
                      >
                        {n}
                      </button>
                    ))}
                  </div>
                </div>
                <div className="flex flex-col items-center gap-2">
                  <span className="text-blue-300">Согласных:</span>
                  <div className="flex gap-2">
                    {[0, 1, 2, 3, 4, 5].map(n => (
                      <button
                        key={`c${n}`}
                        onClick={() => handleWordAnswer(currentWord.vowelCount, n)}
                        className="w-10 h-10 rounded-lg bg-blue-500/30 text-white font-bold hover:bg-blue-500/50 transition-colors"
                      >
                        {n}
                      </button>
                    ))}
                  </div>
                </div>
              </div>

              {feedback === 'wrong' && (
                <div className="text-yellow-300">
                  Правильно: {currentWord.vowelCount} гласных, {currentWord.consonantCount} согласных
                </div>
              )}
            </>
          )}
        </div>
      )}

      <div className="flex justify-center mt-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>
    </div>
  )
}
