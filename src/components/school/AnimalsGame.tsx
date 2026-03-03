'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw } from 'lucide-react'

const ANIMALS = {
  domestic: [
    { name: 'Собака', emoji: '🐶', category: 'домашнее' },
    { name: 'Кошка', emoji: '🐱', category: 'домашнее' },
    { name: 'Корова', emoji: '🐄', category: 'домашнее' },
    { name: 'Лошадь', emoji: '🐴', category: 'домашнее' },
    { name: 'Свинья', emoji: '🐷', category: 'домашнее' },
    { name: 'Овца', emoji: '🐑', category: 'домашнее' },
    { name: 'Коза', emoji: '🐐', category: 'домашнее' },
    { name: 'Курица', emoji: '🐔', category: 'домашнее' },
    { name: 'Утка', emoji: '🦆', category: 'домашнее' },
    { name: 'Гусь', emoji: '🦢', category: 'домашнее' },
    { name: 'Кролик', emoji: '🐰', category: 'домашнее' },
    { name: 'Хомяк', emoji: '🐹', category: 'домашнее' },
  ],
  wild: [
    { name: 'Волк', emoji: '🐺', category: 'дикое' },
    { name: 'Лиса', emoji: '🦊', category: 'дикое' },
    { name: 'Медведь', emoji: '🐻', category: 'дикое' },
    { name: 'Заяц', emoji: '🐰', category: 'дикое' },
    { name: 'Олень', emoji: '🦌', category: 'дикое' },
    { name: 'Ёж', emoji: '🦔', category: 'дикое' },
    { name: 'Белка', emoji: '🐿️', category: 'дикое' },
    { name: 'Лось', emoji: '🫎', category: 'дикое' },
    { name: 'Кабан', emoji: '🐗', category: 'дикое' },
    { name: 'Бобр', emoji: '🦫', category: 'дикое' },
    { name: 'Рысь', emoji: '🐱', category: 'дикое' },
    { name: 'Тигр', emoji: '🐯', category: 'дикое' },
  ],
  forest: [
    { name: 'Медведь', emoji: '🐻', habitat: 'лес' },
    { name: 'Волк', emoji: '🐺', habitat: 'лес' },
    { name: 'Лиса', emoji: '🦊', habitat: 'лес' },
    { name: 'Заяц', emoji: '🐰', habitat: 'лес' },
    { name: 'Белка', emoji: '🐿️', habitat: 'лес' },
    { name: 'Ёж', emoji: '🦔', habitat: 'лес' },
    { name: 'Олень', emoji: '🦌', habitat: 'лес' },
    { name: 'Лось', emoji: '🫎', habitat: 'лес' },
  ],
  farm: [
    { name: 'Корова', emoji: '🐄', habitat: 'ферма' },
    { name: 'Свинья', emoji: '🐷', habitat: 'ферма' },
    { name: 'Овца', emoji: '🐑', habitat: 'ферма' },
    { name: 'Коза', emoji: '🐐', habitat: 'ферма' },
    { name: 'Лошадь', emoji: '🐴', habitat: 'ферма' },
    { name: 'Курица', emoji: '🐔', habitat: 'ферма' },
    { name: 'Утка', emoji: '🦆', habitat: 'ферма' },
    { name: 'Гусь', emoji: '🦢', habitat: 'ферма' },
  ],
  water: [
    { name: 'Рыба', emoji: '🐟', habitat: 'вода' },
    { name: 'Дельфин', emoji: '🐬', habitat: 'вода' },
    { name: 'Кит', emoji: '🐋', habitat: 'вода' },
    { name: 'Акула', emoji: '🦈', habitat: 'вода' },
    { name: 'Краб', emoji: '🦀', habitat: 'вода' },
    { name: 'Осьминог', emoji: '🐙', habitat: 'вода' },
    { name: 'Черепаха', emoji: '🐢', habitat: 'вода' },
    { name: 'Лягушка', emoji: '🐸', habitat: 'вода' },
  ],
}

const ANIMAL_SOUNDS: { name: string; sound: string }[] = [
  { name: 'Собака', sound: 'Гав-гав' },
  { name: 'Кошка', sound: 'Мяу-мяу' },
  { name: 'Корова', sound: 'Му-у' },
  { name: 'Свинья', sound: 'Хрю-хрю' },
  { name: 'Овца', sound: 'Бе-е' },
  { name: 'Коза', sound: 'Ме-е' },
  { name: 'Курица', sound: 'Ко-ко-ко' },
  { name: 'Утка', sound: 'Кря-кря' },
  { name: 'Гусь', sound: 'Га-га-га' },
  { name: 'Лошадь', sound: 'Иго-го' },
  { name: 'Волк', sound: 'У-у-у' },
  { name: 'Лягушка', sound: 'Ква-ква' },
]

type GameMode = 'classify' | 'habitat' | 'sounds' | 'babies'

const BABY_ANIMALS: { mother: string; baby: string; emoji: string }[] = [
  { mother: 'Собака', baby: 'Щенок', emoji: '🐶' },
  { mother: 'Кошка', baby: 'Котёнок', emoji: '🐱' },
  { mother: 'Корова', baby: 'Теленок', emoji: '🐄' },
  { mother: 'Лошадь', baby: 'Жеребёнок', emoji: '🐴' },
  { mother: 'Свинья', baby: 'Поросёнок', emoji: '🐷' },
  { mother: 'Овца', baby: 'Ягнёнок', emoji: '🐑' },
  { mother: 'Коза', baby: 'Козлёнок', emoji: '🐐' },
  { mother: 'Курица', baby: 'Цыплёнок', emoji: '🐔' },
  { mother: 'Утка', baby: 'Утёнок', emoji: '🦆' },
  { mother: 'Гусь', baby: 'Гусёнок', emoji: '🦢' },
]

export default function AnimalsGame() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('classify')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)

  // Mode: classify
  const [classifyAnimal, setClassifyAnimal] = useState<{ name: string; emoji: string; category: string } | null>(null)

  // Mode: habitat
  const [habitatAnimal, setHabitatAnimal] = useState<{ name: string; emoji: string; habitat: string } | null>(null)

  // Mode: sounds
  const [soundQuestion, setSoundQuestion] = useState<{ sound: string; answer: string } | null>(null)

  // Mode: babies
  const [babyQuestion, setBabyQuestion] = useState<{ mother: string; baby: string; emoji: string; type: 'mother' | 'baby' } | null>(null)

  const allAnimals = [...ANIMALS.domestic, ...ANIMALS.wild]
  const habitatAnimals = [...ANIMALS.forest, ...ANIMALS.farm, ...ANIMALS.water]

  const generateClassifyQuestion = () => {
    const animal = allAnimals[Math.floor(Math.random() * allAnimals.length)]
    setClassifyAnimal(animal)
  }

  const generateHabitatQuestion = () => {
    const animal = habitatAnimals[Math.floor(Math.random() * habitatAnimals.length)]
    setHabitatAnimal(animal)
  }

  const generateSoundQuestion = () => {
    const item = ANIMAL_SOUNDS[Math.floor(Math.random() * ANIMAL_SOUNDS.length)]
    setSoundQuestion({ sound: item.sound, answer: item.name })
  }

  const generateBabyQuestion = () => {
    const item = BABY_ANIMALS[Math.floor(Math.random() * BABY_ANIMALS.length)]
    const type: 'mother' | 'baby' = Math.random() > 0.5 ? 'mother' : 'baby'
    setBabyQuestion({ ...item, type })
  }

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    if (mode === 'classify') generateClassifyQuestion()
    else if (mode === 'habitat') generateHabitatQuestion()
    else if (mode === 'sounds') generateSoundQuestion()
    else generateBabyQuestion()
  }, [mode])

  const handleClassifyAnswer = (isDomestic: boolean) => {
    if (!classifyAnimal) return
    const correct = (classifyAnimal.category === 'домашнее') === isDomestic

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
      generateClassifyQuestion()
    }, 800)
  }

  const handleHabitatAnswer = (habitat: string) => {
    if (!habitatAnimal) return
    const correct = habitatAnimal.habitat === habitat

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
      generateHabitatQuestion()
    }, 800)
  }

  const handleSoundAnswer = (answer: string) => {
    if (!soundQuestion) return
    const correct = answer === soundQuestion.answer

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
      generateSoundQuestion()
    }, 800)
  }

  const handleBabyAnswer = (answer: string) => {
    if (!babyQuestion) return
    const correctAnswer = babyQuestion.type === 'mother' ? babyQuestion.baby : babyQuestion.mother
    const correct = answer === correctAnswer

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
      generateBabyQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'classify') generateClassifyQuestion()
    else if (mode === 'habitat') generateHabitatQuestion()
    else if (mode === 'sounds') generateSoundQuestion()
    else generateBabyQuestion()
  }

  const shuffleArray = <T,>(arr: T[]): T[] => [...arr].sort(() => Math.random() - 0.5)

  return (
    <div className="bg-gradient-to-br from-green-500/20 to-lime-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">🐾</span> Животные
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4 flex-wrap">
        {(['classify', 'habitat', 'sounds', 'babies'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-green-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'classify' ? '🏠 Дом/Дикие' : m === 'habitat' ? '🌳 Среда' : m === 'sounds' ? '🔊 Голоса' : '👶 Детёныши'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'classify' && classifyAnimal && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Это животное домашнее или дикое?</div>
            <div className="text-8xl mb-4">{classifyAnimal.emoji}</div>
            <div className={`text-3xl font-bold mb-6 ${feedback === 'correct' ? 'text-green-400' : feedback === 'wrong' ? 'text-red-400' : 'text-white'}`}>
              {classifyAnimal.name}
            </div>
            <div className="flex justify-center gap-4">
              <button
                onClick={() => handleClassifyAnswer(true)}
                className="px-8 py-4 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
              >
                🏠 Домашнее
              </button>
              <button
                onClick={() => handleClassifyAnswer(false)}
                className="px-8 py-4 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
              >
                🌲 Дикое
              </button>
            </div>
          </div>
        )}

        {mode === 'habitat' && habitatAnimal && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Где живёт это животное?</div>
            <div className="text-8xl mb-4">{habitatAnimal.emoji}</div>
            <div className="text-3xl font-bold text-white mb-6">{habitatAnimal.name}</div>
            <div className="grid grid-cols-3 gap-3">
              {[
                { id: 'лес', label: '🌲 Лес', emoji: '🌲' },
                { id: 'ферма', label: '🌾 Ферма', emoji: '🌾' },
                { id: 'вода', label: '🌊 Вода', emoji: '🌊' },
              ].map(h => (
                <button
                  key={h.id}
                  onClick={() => handleHabitatAnswer(h.id)}
                  className={`p-4 rounded-xl font-bold transition-all hover:scale-105 ${feedback === 'correct' && habitatAnimal.habitat === h.id ? 'bg-green-500 text-white' : 'bg-white/10 hover:bg-green-500/30 text-white'}`}
                >
                  <div className="text-3xl mb-1">{h.emoji}</div>
                  <div>{h.label}</div>
                </button>
              ))}
            </div>
          </div>
        )}

        {mode === 'sounds' && soundQuestion && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Кто издаёт этот звук?</div>
            <div className="text-4xl font-bold text-yellow-300 mb-6 p-4 bg-white/10 rounded-xl">
              "{soundQuestion.sound}"
            </div>
            <div className="grid grid-cols-4 gap-3">
              {shuffleArray(ANIMAL_SOUNDS).slice(0, 4).map(item => (
                <button
                  key={item.name}
                  onClick={() => handleSoundAnswer(item.name)}
                  className="p-4 bg-white/10 hover:bg-green-500/30 rounded-xl transition-all hover:scale-105"
                >
                  <div className="text-4xl mb-2">
                    {ANIMALS.domestic.find(a => a.name === item.name)?.emoji || ANIMALS.wild.find(a => a.name === item.name)?.emoji || '🐾'}
                  </div>
                  <div className="text-white text-sm">{item.name}</div>
                </button>
              ))}
              <button
                onClick={() => handleSoundAnswer(soundQuestion.answer)}
                className="p-4 bg-white/10 hover:bg-green-500/30 rounded-xl transition-all hover:scale-105"
              >
                <div className="text-4xl mb-2">
                  {ANIMALS.domestic.find(a => a.name === soundQuestion.answer)?.emoji || '🐾'}
                </div>
                <div className="text-white text-sm">{soundQuestion.answer}</div>
              </button>
            </div>
          </div>
        )}

        {mode === 'babies' && babyQuestion && (
          <div className="text-center">
            <div className="mb-4 text-white/60">
              {babyQuestion.type === 'mother' ? 'Как называется детёныш?' : 'Кто мама этого детёныша?'}
            </div>
            <div className="text-6xl mb-4">{babyQuestion.emoji}</div>
            <div className="text-3xl font-bold text-white mb-6">
              {babyQuestion.type === 'mother' ? babyQuestion.mother : babyQuestion.baby}
            </div>
            <div className="grid grid-cols-2 gap-3">
              {shuffleArray(BABY_ANIMALS).slice(0, 3).map(item => (
                <button
                  key={item.baby}
                  onClick={() => handleBabyAnswer(babyQuestion.type === 'mother' ? item.baby : item.mother)}
                  className="p-4 bg-gradient-to-r from-pink-500 to-rose-500 rounded-xl text-white font-bold hover:scale-105 transition-transform"
                >
                  {babyQuestion.type === 'mother' ? item.baby : item.mother}
                </button>
              ))}
              <button
                onClick={() => handleBabyAnswer(babyQuestion.type === 'mother' ? babyQuestion.baby : babyQuestion.mother)}
                className="p-4 bg-gradient-to-r from-pink-500 to-rose-500 rounded-xl text-white font-bold hover:scale-105 transition-transform"
              >
                {babyQuestion.type === 'mother' ? babyQuestion.baby : babyQuestion.mother}
              </button>
            </div>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                Правильный ответ: {babyQuestion.type === 'mother' ? babyQuestion.baby : babyQuestion.mother}
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
        <div className="text-white/60 text-sm">
          🐾 Домашние животные живут с человеком, а дикие — в природе
        </div>
      </div>
    </div>
  )
}
