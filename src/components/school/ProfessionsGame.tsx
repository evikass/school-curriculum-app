'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw } from 'lucide-react'

const PROFESSIONS = [
  { name: 'Врач', emoji: '👨‍⚕️', description: 'Лечит людей', actions: ['лечит', 'осматривает', 'выписывает лекарства'] },
  { name: 'Учитель', emoji: '👩‍🏫', description: 'Учит детей', actions: ['учит', 'объясняет', 'проверяет'] },
  { name: 'Повар', emoji: '👨‍🍳', description: 'Готовит еду', actions: ['готовит', 'режет', 'варит'] },
  { name: 'Пожарный', emoji: '🧑‍🚒', description: 'Тушит пожары', actions: ['тушит', 'спасает', 'помогает'] },
  { name: 'Полицейский', emoji: '👮', description: 'Охраняет порядок', actions: ['охраняет', 'ловит', 'защищает'] },
  { name: 'Водитель', emoji: '🚗', description: 'Управляет транспортом', actions: ['водит', 'перевозит', 'управляет'] },
  { name: 'Строитель', emoji: '👷', description: 'Строит дома', actions: ['строит', 'кладёт', 'возводит'] },
  { name: 'Парикмахер', emoji: '💇', description: 'Стрижёт людей', actions: ['стрижёт', 'укладывает', 'красит'] },
  { name: 'Продавец', emoji: '🧑‍💼', description: 'Продаёт товары', actions: ['продаёт', 'обслуживает', 'считает'] },
  { name: 'Художник', emoji: '🎨', description: 'Рисует картины', actions: ['рисует', 'пишет', 'творит'] },
  { name: 'Музыкант', emoji: '🎵', description: 'Играет на инструментах', actions: ['играет', 'поёт', 'сочиняет'] },
  { name: 'Спортсмен', emoji: '⚽', description: 'Занимается спортом', actions: ['тренируется', 'соревнуется', 'побеждает'] },
  { name: 'Космонавт', emoji: '👨‍🚀', description: 'Летает в космос', actions: ['летает', 'исследует', 'открывает'] },
  { name: 'Лётчик', emoji: '✈️', description: 'Управляет самолётом', actions: ['летает', 'перевозит', 'управляет'] },
  { name: 'Моряк', emoji: '⚓', description: 'Плавает на кораблях', actions: ['плавает', 'управляет', 'несёт вахту'] },
  { name: 'Фермер', emoji: '🧑‍🌾', description: 'Выращивает растения и животных', actions: ['выращивает', 'сеет', 'ухаживает'] },
  { name: 'Пекарь', emoji: '🥖', description: 'Выпекает хлеб', actions: ['печёт', 'замешивает', 'выпекает'] },
  { name: 'Почтальон', emoji: '📬', description: 'Доставляет почту', actions: ['доставляет', 'разносит', 'приносит'] },
  { name: 'Библиотекарь', emoji: '📚', description: 'Работает с книгами', actions: ['выдаёт', 'принимает', 'хранит'] },
  { name: 'Доктор', emoji: '🩺', description: 'Лечит больных', actions: ['лечит', 'ставит диагноз', 'назначает'] },
]

type GameMode = 'what' | 'who' | 'action' | 'items'

const PROFESSION_ITEMS: { profession: string; items: string[] }[] = [
  { profession: 'Врач', items: ['стетоскоп', 'градусник', 'лекарства'] },
  { profession: 'Учитель', items: ['доска', 'мел', 'учебники'] },
  { profession: 'Повар', items: ['кастрюля', 'сковорода', 'нож'] },
  { profession: 'Пожарный', items: ['шланг', 'каска', 'огнетушитель'] },
  { profession: 'Полицейский', items: ['свиток', 'свисток', 'жезл'] },
  { profession: 'Художник', items: ['кисти', 'краски', 'холст'] },
  { profession: 'Музыкант', items: ['инструмент', 'ноты', 'пюпитр'] },
  { profession: 'Парикмахер', items: ['ножницы', 'расчёска', 'фен'] },
]

export default function ProfessionsGame() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('what')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)

  // Mode: what
  const [whatQuestion, setWhatQuestion] = useState<{ profession: typeof PROFESSIONS[0]; type: 'description' | 'action' } | null>(null)

  // Mode: who
  const [whoQuestion, setWhoQuestion] = useState<{ description: string; answer: string } | null>(null)

  // Mode: action
  const [actionQuestion, setActionQuestion] = useState<{ profession: string; emoji: string; actions: string[] } | null>(null)

  // Mode: items
  const [itemsQuestion, setItemsQuestion] = useState<{ items: string[]; answer: string } | null>(null)

  const shuffleArray = <T,>(arr: T[]): T[] => [...arr].sort(() => Math.random() - 0.5)

  const generateWhatQuestion = () => {
    const prof = PROFESSIONS[Math.floor(Math.random() * PROFESSIONS.length)]
    const type: 'description' | 'action' = Math.random() > 0.5 ? 'description' : 'action'
    setWhatQuestion({ profession: prof, type })
  }

  const generateWhoQuestion = () => {
    const prof = PROFESSIONS[Math.floor(Math.random() * PROFESSIONS.length)]
    const description = prof.description
    setWhoQuestion({ description, answer: prof.name })
  }

  const generateActionQuestion = () => {
    const prof = PROFESSIONS[Math.floor(Math.random() * PROFESSIONS.length)]
    setActionQuestion({ profession: prof.name, emoji: prof.emoji, actions: prof.actions })
  }

  const generateItemsQuestion = () => {
    const item = PROFESSION_ITEMS[Math.floor(Math.random() * PROFESSION_ITEMS.length)]
    setItemsQuestion({ items: item.items, answer: item.profession })
  }

  useEffect(() => {
    if (mode === 'what') generateWhatQuestion()
    else if (mode === 'who') generateWhoQuestion()
    else if (mode === 'action') generateActionQuestion()
    else generateItemsQuestion()
  }, [mode])

  const handleWhatAnswer = (answer: string) => {
    if (!whatQuestion) return
    const correct = answer === whatQuestion.profession.name

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
      generateWhatQuestion()
    }, 1000)
  }

  const handleWhoAnswer = (answer: string) => {
    if (!whoQuestion) return
    const correct = answer === whoQuestion.answer

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
      generateWhoQuestion()
    }, 1000)
  }

  const handleActionAnswer = (isCorrect: boolean) => {
    if (!actionQuestion) return

    if (isCorrect) {
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
      generateActionQuestion()
    }, 800)
  }

  const handleItemsAnswer = (answer: string) => {
    if (!itemsQuestion) return
    const correct = answer === itemsQuestion.answer

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
      generateItemsQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'what') generateWhatQuestion()
    else if (mode === 'who') generateWhoQuestion()
    else if (mode === 'action') generateActionQuestion()
    else generateItemsQuestion()
  }

  const getWrongActions = (correct: string[]): string[] => {
    const all = ['бежит', 'спит', 'ест', 'смотрит', 'гуляет', 'читает', 'пишет', 'считает']
    return shuffleArray(all.filter(a => !correct.includes(a))).slice(0, 2)
  }

  return (
    <div className="bg-gradient-to-br from-indigo-500/20 to-violet-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">👨‍💼</span> Профессии
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4 flex-wrap">
        {(['what', 'who', 'action', 'items'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-indigo-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'what' ? '📋 Что делает?' : m === 'who' ? '👤 Кто это?' : m === 'action' ? '✅ Правильно?' : '🔧 Предметы'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'what' && whatQuestion && (
          <div className="text-center">
            <div className="text-6xl mb-4">{whatQuestion.profession.emoji}</div>
            <div className="mb-4">
              {whatQuestion.type === 'description' ? (
                <div className="text-white/60">Кто {whatQuestion.profession.description.toLowerCase()}?</div>
              ) : (
                <div className="text-white/60">
                  Кто {whatQuestion.profession.actions[0]}?
                </div>
              )}
            </div>
            <div className="grid grid-cols-2 gap-3">
              {shuffleArray([...PROFESSIONS.slice(0, 3), whatQuestion.profession]).map(p => (
                <button
                  key={p.name}
                  onClick={() => handleWhatAnswer(p.name)}
                  className="p-4 bg-gradient-to-r from-indigo-400 to-violet-500 rounded-xl text-white font-bold hover:scale-105 transition-transform"
                >
                  <div className="text-3xl mb-1">{p.emoji}</div>
                  {p.name}
                </button>
              ))}
            </div>
          </div>
        )}

        {mode === 'who' && whoQuestion && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Кто это?</div>
            <div className="text-2xl font-bold text-white mb-6 p-4 bg-white/10 rounded-xl">
              {whoQuestion.description}
            </div>
            <div className="grid grid-cols-2 gap-3">
              {shuffleArray([...PROFESSIONS.slice(0, 3), PROFESSIONS.find(p => p.name === whoQuestion.answer)!]).map(p => (
                <button
                  key={p.name}
                  onClick={() => handleWhoAnswer(p.name)}
                  className="p-4 bg-gradient-to-r from-indigo-400 to-violet-500 rounded-xl text-white font-bold hover:scale-105 transition-transform"
                >
                  <div className="text-3xl mb-1">{p.emoji}</div>
                  {p.name}
                </button>
              ))}
            </div>
          </div>
        )}

        {mode === 'action' && actionQuestion && (
          <div className="text-center">
            <div className="text-6xl mb-2">{actionQuestion.emoji}</div>
            <div className="text-2xl font-bold text-white mb-4">{actionQuestion.profession}</div>
            <div className="mb-6 text-white/60">Правильно ли: "{actionQuestion.actions[0]}"?</div>
            <div className="flex justify-center gap-4">
              <button
                onClick={() => handleActionAnswer(true)}
                className="px-10 py-4 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
              >
                ✅ Да
              </button>
              <button
                onClick={() => handleActionAnswer(false)}
                className="px-10 py-4 bg-gradient-to-r from-red-500 to-pink-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
              >
                ❌ Нет
              </button>
            </div>
          </div>
        )}

        {mode === 'items' && itemsQuestion && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Кому нужны эти предметы?</div>
            <div className="flex justify-center gap-3 mb-6">
              {itemsQuestion.items.map((item, i) => (
                <span key={i} className="px-4 py-2 bg-white/10 rounded-lg text-white font-medium">
                  {item}
                </span>
              ))}
            </div>
            <div className="grid grid-cols-2 gap-3">
              {shuffleArray([...PROFESSION_ITEMS.slice(0, 3), itemsQuestion]).map(item => {
                const prof = PROFESSIONS.find(p => p.name === (item.answer || item.profession))
                return (
                  <button
                    key={prof?.name}
                    onClick={() => handleItemsAnswer(prof?.name || '')}
                    className="p-4 bg-gradient-to-r from-indigo-400 to-violet-500 rounded-xl text-white font-bold hover:scale-105 transition-transform"
                  >
                    <div className="text-3xl mb-1">{prof?.emoji}</div>
                    {prof?.name}
                  </button>
                )
              })}
            </div>
          </div>
        )}
      </div>

      <div className="flex justify-center mt-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>

      <div className="mt-4 p-3 bg-white/5 rounded-lg">
        <div className="text-white/60 text-sm">
          💼 Профессия — это работа, которой человек занимается большую часть жизни
        </div>
      </div>
    </div>
  )
}
