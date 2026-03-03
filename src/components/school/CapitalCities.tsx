'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { Building2 } from 'lucide-react'

const CITIES = [
  { country: 'Россия', capital: 'Москва' },
  { country: 'Франция', capital: 'Париж' },
  { country: 'Германия', capital: 'Берлин' },
  { country: 'Япония', capital: 'Токио' },
  { country: 'Великобритания', capital: 'Лондон' },
  { country: 'Италия', capital: 'Рим' },
  { country: 'США', capital: 'Вашингтон' },
  { country: 'Китай', capital: 'Пекин' },
]

export default function CapitalCities() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const city = CITIES[index]
  const options = CITIES.filter(c => c !== city).sort(() => Math.random() - 0.5).slice(0, 3).concat(city).sort(() => Math.random() - 0.5)

  const answer = (capital: string) => {
    if (capital === city.capital) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % CITIES.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-green-500/20 border-2 border-emerald-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <Building2 className="w-5 h-5" /> Столицы
      </h3>
      <p className="text-white mb-2">Столица страны:</p>
      <p className="text-3xl text-emerald-300 font-bold mb-6">{city.country}</p>
      <div className="grid grid-cols-2 gap-3">
        {options.map(opt => (
          <button
            key={opt.capital}
            onClick={() => answer(opt.capital)}
            className="p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            {opt.capital}
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
    </div>
  )
}
