'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw, Lightbulb } from 'lucide-react'

const FORMULAS = [
  { name: 'Скорость', formula: 'v = s/t', description: 'Скорость равна расстоянию, делённому на время', variables: ['v — скорость', 's — расстояние', 't — время'] },
  { name: 'Путь', formula: 's = v × t', description: 'Расстояние равно скорости, умноженной на время', variables: ['s — расстояние', 'v — скорость', 't — время'] },
  { name: 'Плотность', formula: 'ρ = m/V', description: 'Плотность равна массе, делённой на объём', variables: ['ρ — плотность', 'm — масса', 'V — объём'] },
  { name: 'Масса', formula: 'm = ρ × V', description: 'Масса равна плотности, умноженной на объём', variables: ['m — масса', 'ρ — плотность', 'V — объём'] },
  { name: 'Сила тяжести', formula: 'F = m × g', description: 'Сила тяжести равна массе, умноженной на ускорение свободного падения', variables: ['F — сила', 'm — масса', 'g ≈ 10 Н/кг'] },
  { name: 'Вес', formula: 'P = m × g', description: 'Вес равен массе, умноженной на ускорение свободного падения', variables: ['P — вес', 'm — масса', 'g ≈ 10 Н/кг'] },
  { name: 'Давление', formula: 'p = F/S', description: 'Давление равно силе, делённой на площадь', variables: ['p — давление', 'F — сила', 'S — площадь'] },
  { name: 'Работа', formula: 'A = F × s', description: 'Работа равна силе, умноженной на путь', variables: ['A — работа', 'F — сила', 's — путь'] },
  { name: 'Мощность', formula: 'N = A/t', description: 'Мощность равна работе, делённой на время', variables: ['N — мощность', 'A — работа', 't — время'] },
  { name: 'Кинетическая энергия', formula: 'Eк = mv²/2', description: 'Кинетическая энергия зависит от массы и скорости', variables: ['Eк — энергия', 'm — масса', 'v — скорость'] },
  { name: 'Потенциальная энергия', formula: 'Eп = mgh', description: 'Потенциальная энергия зависит от массы и высоты', variables: ['Eп — энергия', 'm — масса', 'g — ускорение', 'h — высота'] },
  { name: 'Закон Ома', formula: 'I = U/R', description: 'Сила тока равна напряжению, делённому на сопротивление', variables: ['I — сила тока', 'U — напряжение', 'R — сопротивление'] },
  { name: 'Закон Гука', formula: 'F = kx', description: 'Сила упругости пропорциональна удлинению', variables: ['F — сила', 'k — жёсткость', 'x — удлинение'] },
  { name: 'Архимедова сила', formula: 'FА = ρgV', description: 'Выталкивающая сила равна весу вытесненной жидкости', variables: ['FА — сила', 'ρ — плотность жидкости', 'V — объём тела'] },
]

type GameMode = 'formula' | 'variable' | 'calculate'

const CALCULATIONS = [
  { question: 'Автомобиль проехал 100 км за 2 часа. Найдите скорость.', answer: 50, unit: 'км/ч', hint: 'v = s/t' },
  { question: 'Плотность воды 1000 кг/м³. Какой объём занимает 2000 кг воды?', answer: 2, unit: 'м³', hint: 'V = m/ρ' },
  { question: 'Масса тела 5 кг. Найдите силу тяжести (g=10 Н/кг).', answer: 50, unit: 'Н', hint: 'F = mg' },
  { question: 'Сила 100 Н действует на площадь 2 м². Найдите давление.', answer: 50, unit: 'Па', hint: 'p = F/S' },
  { question: 'Тело массой 2 кг движется со скоростью 3 м/с. Найдите кинетическую энергию.', answer: 9, unit: 'Дж', hint: 'E = mv²/2' },
  { question: 'Тело массой 10 кг поднято на высоту 5 м. Найдите потенциальную энергию (g=10).', answer: 500, unit: 'Дж', hint: 'E = mgh' },
]

export default function PhysicsFormulas() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('formula')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)

  // Mode: formula
  const [currentFormula, setCurrentFormula] = useState<typeof FORMULAS[0] | null>(null)
  const [questionBy, setQuestionBy] = useState<'name' | 'description'>('name')

  // Mode: calculate
  const [currentCalc, setCurrentCalc] = useState<typeof CALCULATIONS[0] | null>(null)
  const [calcAnswer, setCalcAnswer] = useState('')

  const shuffleArray = <T,>(arr: T[]): T[] => [...arr].sort(() => Math.random() - 0.5)

  const generateFormulaQuestion = () => {
    const formula = FORMULAS[Math.floor(Math.random() * FORMULAS.length)]
    setCurrentFormula(formula)
    setQuestionBy(Math.random() > 0.5 ? 'name' : 'description')
  }

  const generateCalcQuestion = () => {
    const calc = CALCULATIONS[Math.floor(Math.random() * CALCULATIONS.length)]
    setCurrentCalc(calc)
    setCalcAnswer('')
  }

  useEffect(() => {
    if (mode === 'formula' || mode === 'variable') generateFormulaQuestion()
    else generateCalcQuestion()
  }, [mode])

  const handleFormulaAnswer = (formula: string) => {
    if (!currentFormula) return
    const correct = formula === currentFormula.formula

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
      generateFormulaQuestion()
    }, 1200)
  }

  const handleVariableAnswer = (variable: string) => {
    if (!currentFormula) return
    const correct = currentFormula.variables.includes(variable)

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
      generateFormulaQuestion()
    }, 1000)
  }

  const handleCalcSubmit = () => {
    if (!currentCalc) return
    const userAnswer = parseFloat(calcAnswer)
    const correct = userAnswer === currentCalc.answer

    if (correct) {
      playCorrect()
      setScore(s => s + 25)
      setStreak(s => s + 1)
      setFeedback('correct')
      addXP(12 + streak)
    } else {
      playWrong()
      setStreak(0)
      setFeedback('wrong')
    }

    setTimeout(() => {
      setFeedback(null)
      generateCalcQuestion()
    }, 1500)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'formula' || mode === 'variable') generateFormulaQuestion()
    else generateCalcQuestion()
  }

  return (
    <div className="bg-gradient-to-br from-indigo-500/20 to-violet-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">📐</span> Физические формулы
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-4">
        {(['formula', 'variable', 'calculate'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-xs font-medium transition-all ${mode === m ? 'bg-indigo-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'formula' ? '📝 Формула' : m === 'variable' ? '🔤 Переменные' : '🧮 Вычислить'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'formula' && currentFormula && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Какая формула?</div>
            {questionBy === 'name' ? (
              <div className="text-3xl font-bold text-white mb-6 p-4 bg-white/10 rounded-xl">
                {currentFormula.name}
              </div>
            ) : (
              <div className="text-lg text-white mb-6 p-4 bg-white/10 rounded-xl">
                {currentFormula.description}
              </div>
            )}
            <div className="grid grid-cols-2 gap-3">
              {shuffleArray([...FORMULAS.filter(f => f.formula !== currentFormula.formula).slice(0, 3), currentFormula]).map(f => (
                <button
                  key={f.formula}
                  onClick={() => handleFormulaAnswer(f.formula)}
                  className="p-4 bg-gradient-to-r from-indigo-500 to-violet-500 rounded-xl text-white font-mono text-xl hover:scale-105 transition-transform"
                >
                  {f.formula}
                </button>
              ))}
            </div>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300 font-mono">
                Правильно: {currentFormula.formula}
              </div>
            )}
          </div>
        )}

        {mode === 'variable' && currentFormula && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Что означает переменная в формуле?</div>
            <div className="text-4xl font-mono text-yellow-300 mb-6 p-4 bg-white/10 rounded-xl">
              {currentFormula.formula}
            </div>
            <div className="grid grid-cols-1 gap-2">
              {shuffleArray([...currentFormula.variables, ...FORMULAS.filter(f => f.formula !== currentFormula.formula).slice(0, 2).flatMap(f => f.variables.slice(0, 1))]).slice(0, 4).map((v, i) => (
                <button
                  key={i}
                  onClick={() => handleVariableAnswer(v)}
                  className={`p-3 rounded-xl text-white font-medium hover:scale-102 transition-transform ${
                    currentFormula.variables.includes(v) ? 'bg-gradient-to-r from-green-500 to-emerald-500' : 'bg-gradient-to-r from-red-500 to-pink-500'
                  }`}
                >
                  {v}
                </button>
              ))}
            </div>
          </div>
        )}

        {mode === 'calculate' && currentCalc && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Реши задачу:</div>
            <div className="text-lg text-white mb-4 p-4 bg-white/10 rounded-xl">
              {currentCalc.question}
            </div>
            <div className="text-sm text-cyan-300 mb-4 flex items-center justify-center gap-2">
              <Lightbulb className="w-4 h-4" /> Подсказка: {currentCalc.hint}
            </div>
            <div className="flex gap-2 justify-center mb-4">
              <input
                type="number"
                value={calcAnswer}
                onChange={(e) => setCalcAnswer(e.target.value)}
                placeholder="Ответ"
                className="w-32 px-4 py-3 rounded-xl bg-white/10 text-white text-xl text-center focus:outline-none focus:ring-2 focus:ring-indigo-400"
              />
              <span className="px-4 py-3 bg-white/10 rounded-xl text-white text-xl">
                {currentCalc.unit}
              </span>
            </div>
            <button
              onClick={handleCalcSubmit}
              disabled={!calcAnswer}
              className="px-8 py-3 bg-gradient-to-r from-indigo-500 to-violet-500 rounded-xl text-white font-bold hover:scale-105 transition-transform disabled:opacity-50"
            >
              Проверить
            </button>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                Правильный ответ: {currentCalc.answer} {currentCalc.unit}
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
        <div className="text-white/60 text-sm mb-2">📐 Основные формулы:</div>
        <div className="grid grid-cols-2 gap-2 text-xs">
          {FORMULAS.slice(0, 8).map(f => (
            <div key={f.formula} className="flex items-center gap-2 bg-white/5 rounded p-2">
              <span className="font-mono text-yellow-300">{f.formula}</span>
              <span className="text-white/70">{f.name}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
