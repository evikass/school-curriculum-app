'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw, Triangle, Square, Circle, Hexagon, Pentagon, Star } from 'lucide-react'

const SHAPES = [
  { name: 'Круг', sides: 0, emoji: '⭕', color: 'red', icon: Circle },
  { name: 'Треугольник', sides: 3, emoji: '🔺', color: 'yellow', icon: Triangle },
  { name: 'Квадрат', sides: 4, emoji: '🟧', color: 'orange', icon: Square },
  { name: 'Прямоугольник', sides: 4, emoji: '🟦', color: 'blue', icon: Square },
  { name: 'Ромб', sides: 4, emoji: '🔷', color: 'cyan', icon: Square },
  { name: 'Пятиугольник', sides: 5, emoji: '⬠', color: 'purple', icon: Pentagon },
  { name: 'Шестиугольник', sides: 6, emoji: '⬡', color: 'green', icon: Hexagon },
  { name: 'Звезда', sides: 5, emoji: '⭐', color: 'amber', icon: Star },
]

const REAL_OBJECTS = [
  { object: 'Мяч', shape: 'Круг' },
  { object: 'Дверь', shape: 'Прямоугольник' },
  { object: 'Окно', shape: 'Квадрат' },
  { object: 'Дорожный знак (Стоп)', shape: 'Восьмиугольник' },
  { object: 'Книга', shape: 'Прямоугольник' },
  { object: 'Часы', shape: 'Круг' },
  { object: 'Пицца', shape: 'Круг' },
  { object: 'Треугольник музыкальный', shape: 'Треугольник' },
  { object: 'Солнце', shape: 'Круг' },
  { object: 'Подушка', shape: 'Квадрат' },
  { object: 'Экран телевизора', shape: 'Прямоугольник' },
  { object: 'Колесо', shape: 'Круг' },
  { object: 'Открытка', shape: 'Прямоугольник' },
  { object: 'Лист бумаги', shape: 'Прямоугольник' },
  { object: 'Сотовый телефон', shape: 'Прямоугольник' },
  { object: 'Медаль', shape: 'Круг' },
  { object: 'Сэндвич', shape: 'Треугольник' },
  { object: 'Флажок', shape: 'Треугольник' },
]

type GameMode = 'name' | 'sides' | 'objects' | 'count'

export default function ShapesQuiz() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('name')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  
  // Mode: name
  const [currentShape, setCurrentShape] = useState<typeof SHAPES[0] | null>(null)
  const [shapeOptions, setShapeOptions] = useState<string[]>([])
  
  // Mode: sides
  const [sidesQuestion, setSidesQuestion] = useState<{ shape: typeof SHAPES[0]; type: 'name' | 'sides' } | null>(null)
  
  // Mode: objects
  const [objectQuestion, setObjectQuestion] = useState<{ object: string; correct: string } | null>(null)
  
  // Mode: count
  const [countShapes, setCountShapes] = useState<{ emoji: string; count: number }[]>([])
  const [countTarget, setCountTarget] = useState<{ emoji: string; answer: number } | null>(null)
  const [selectedCount, setSelectedCount] = useState<number | null>(null)

  const shuffleArray = <T,>(arr: T[]): T[] => [...arr].sort(() => Math.random() - 0.5)

  const generateNameQuestion = () => {
    const shape = SHAPES[Math.floor(Math.random() * SHAPES.length)]
    setCurrentShape(shape)
    const options = shuffleArray([shape.name, ...shuffleArray(SHAPES.filter(s => s.name !== shape.name)).slice(0, 3).map(s => s.name)])
    setShapeOptions(options)
  }

  const generateSidesQuestion = () => {
    const shape = SHAPES.filter(s => s.sides > 0)[Math.floor(Math.random() * (SHAPES.length - 1))]
    const type: 'name' | 'sides' = Math.random() > 0.5 ? 'name' : 'sides'
    setSidesQuestion({ shape, type })
  }

  const generateObjectQuestion = () => {
    const obj = REAL_OBJECTS[Math.floor(Math.random() * REAL_OBJECTS.length)]
    setObjectQuestion({ object: obj.object, correct: obj.shape })
  }

  const generateCountQuestion = () => {
    const shapes = shuffleArray(SHAPES.slice(0, 4))
    const counts = shapes.map(s => ({
      emoji: s.emoji,
      count: Math.floor(Math.random() * 5) + 1
    }))
    setCountShapes(counts)
    const target = counts[Math.floor(Math.random() * counts.length)]
    setCountTarget(target)
    setSelectedCount(null)
  }

  useEffect(() => {
    if (mode === 'name') generateNameQuestion()
    else if (mode === 'sides') generateSidesQuestion()
    else if (mode === 'objects') generateObjectQuestion()
    else generateCountQuestion()
  }, [mode])

  const handleNameAnswer = (answer: string) => {
    if (!currentShape) return
    const correct = answer === currentShape.name
    
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
      generateNameQuestion()
    }, 800)
  }

  const handleSidesAnswer = (answer: number | string) => {
    if (!sidesQuestion) return
    let correct: boolean
    
    if (sidesQuestion.type === 'sides') {
      correct = answer === sidesQuestion.shape.sides
    } else {
      correct = answer === sidesQuestion.shape.name
    }

    if (correct) {
      playCorrect()
      setScore(s => s + 15)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(8 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateSidesQuestion()
    }, 1000)
  }

  const handleObjectAnswer = (answer: string) => {
    if (!objectQuestion) return
    
    if (answer === objectQuestion.correct) {
      playCorrect()
      setScore(s => s + 15)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(8 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateObjectQuestion()
    }, 1000)
  }

  const handleCountAnswer = () => {
    if (!countTarget || selectedCount === null) return
    
    if (selectedCount === countTarget.answer) {
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
      generateCountQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'name') generateNameQuestion()
    else if (mode === 'sides') generateSidesQuestion()
    else if (mode === 'objects') generateObjectQuestion()
    else generateCountQuestion()
  }

  return (
    <div className="bg-gradient-to-br from-rose-500/20 to-pink-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">🔷</span> Геометрические фигуры
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4 flex-wrap">
        {(['name', 'sides', 'objects', 'count'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-rose-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'name' ? '📛 Название' : m === 'sides' ? '📐 Углы' : m === 'objects' ? '🏠 Предметы' : '🔢 Счёт'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'name' && currentShape && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Как называется эта фигура?</div>
            <div className="text-9xl mb-6">{currentShape.emoji}</div>
            <div className="grid grid-cols-2 gap-3">
              {shapeOptions.map(opt => (
                <button
                  key={opt}
                  onClick={() => handleNameAnswer(opt)}
                  className="px-6 py-4 bg-gradient-to-r from-rose-400 to-pink-500 rounded-xl text-white font-bold text-lg hover:scale-105 transition-transform shadow-lg"
                >
                  {opt}
                </button>
              ))}
            </div>
          </div>
        )}

        {mode === 'sides' && sidesQuestion && (
          <div className="text-center">
            {sidesQuestion.type === 'sides' ? (
              <>
                <div className="mb-4 text-white/60">Сколько углов/сторон?</div>
                <div className="text-9xl mb-6">{sidesQuestion.shape.emoji}</div>
                <div className="flex justify-center gap-2 flex-wrap">
                  {[0, 3, 4, 5, 6, 7, 8].map(n => (
                    <button
                      key={n}
                      onClick={() => handleSidesAnswer(n)}
                      className="w-14 h-14 bg-gradient-to-r from-rose-400 to-pink-500 rounded-lg text-white text-2xl font-bold hover:scale-110 transition-transform"
                    >
                      {n}
                    </button>
                  ))}
                </div>
              </>
            ) : (
              <>
                <div className="mb-4 text-white/60">Какая фигура имеет {sidesQuestion.shape.sides} углов?</div>
                <div className="grid grid-cols-4 gap-2">
                  {shuffleArray(SHAPES.filter(s => s.sides > 0)).slice(0, 4).map(s => (
                    <button
                      key={s.name}
                      onClick={() => handleSidesAnswer(s.name)}
                      className="p-4 bg-white/10 hover:bg-rose-500/30 rounded-xl transition-all hover:scale-105"
                    >
                      <div className="text-5xl mb-2">{s.emoji}</div>
                      <div className="text-white/70 text-xs">{s.name}</div>
                    </button>
                  ))}
                </div>
              </>
            )}
          </div>
        )}

        {mode === 'objects' && objectQuestion && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Какую форму имеет этот предмет?</div>
            <div className="text-5xl mb-2">🏠</div>
            <div className="text-3xl font-bold text-white mb-6">{objectQuestion.object}</div>
            <div className="grid grid-cols-2 gap-3">
              {shuffleArray([...new Set(REAL_OBJECTS.map(o => o.shape))]).slice(0, 4).map(shape => (
                <button
                  key={shape}
                  onClick={() => handleObjectAnswer(shape)}
                  className="px-6 py-4 bg-gradient-to-r from-rose-400 to-pink-500 rounded-xl text-white font-bold hover:scale-105 transition-transform shadow-lg"
                >
                  {shape}
                </button>
              ))}
              <button
                onClick={() => handleObjectAnswer(objectQuestion.correct)}
                className="px-6 py-4 bg-gradient-to-r from-rose-400 to-pink-500 rounded-xl text-white font-bold hover:scale-105 transition-transform shadow-lg"
              >
                {objectQuestion.correct}
              </button>
            </div>
          </div>
        )}

        {mode === 'count' && countTarget && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Сколько {countTarget.emoji} на картинке?</div>
            <div className="flex flex-wrap justify-center gap-2 mb-6 p-4 bg-white/5 rounded-xl">
              {countShapes.flatMap(s => Array(s.count).fill(s.emoji)).sort(() => Math.random() - 0.5).map((emoji, i) => (
                <span key={i} className="text-4xl">{emoji}</span>
              ))}
            </div>
            <div className="flex justify-center gap-2 mb-4">
              {[1, 2, 3, 4, 5, 6, 7, 8].map(n => (
                <button
                  key={n}
                  onClick={() => setSelectedCount(n)}
                  className={`w-12 h-12 rounded-lg text-xl font-bold transition-all ${selectedCount === n ? 'bg-rose-500 text-white' : 'bg-white/10 text-white hover:bg-white/20'}`}
                >
                  {n}
                </button>
              ))}
            </div>
            <button
              onClick={handleCountAnswer}
              disabled={selectedCount === null}
              className="px-8 py-3 bg-gradient-to-r from-rose-500 to-pink-500 rounded-xl text-white font-bold hover:scale-105 transition-transform disabled:opacity-50"
            >
              Проверить
            </button>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                Правильный ответ: {countTarget.answer}
              </div>
            )}
          </div>
        )}
      </div>

      <div className="flex justify-center mt-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>

      <div className="mt-4 p-3 bg-white/5 rounded-lg">
        <div className="text-white/60 text-sm mb-2">📐 Фигуры и углы:</div>
        <div className="grid grid-cols-4 gap-2 text-xs">
          {SHAPES.slice(0, 8).map(s => (
            <div key={s.name} className="text-center p-1 bg-white/5 rounded">
              <span className="text-xl">{s.emoji}</span>
              <div className="text-white/70">{s.sides === 0 ? '0' : s.sides} угл.</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
