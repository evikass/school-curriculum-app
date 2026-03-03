'use client'

<<<<<<< HEAD
import { useState, useEffect } from 'react'
import { Zap, RefreshCw, Trophy, Sparkles, CheckCircle, XCircle } from 'lucide-react'
import { useSound } from '@/lib/sounds'

// Sample quick quiz questions from different subjects
const QUIZ_QUESTIONS = [
  // Math
  { q: "5 + 7 = ?", options: ["11", "12", "13"], answer: "12", subject: "🔢 Математика" },
  { q: "15 - 8 = ?", options: ["6", "7", "8"], answer: "7", subject: "🔢 Математика" },
  { q: "6 × 7 = ?", options: ["42", "43", "44"], answer: "42", subject: "🔢 Математика" },
  { q: "81 ÷ 9 = ?", options: ["8", "9", "10"], answer: "9", subject: "🔢 Математика" },
  // Russian
  { q: "Сколько букв в русском алфавите?", options: ["32", "33", "34"], answer: "33", subject: "📝 Русский язык" },
  { q: "Какая часть речи обозначает действие?", options: ["Существительное", "Глагол", "Прилагательное"], answer: "Глагол", subject: "📝 Русский язык" },
  { q: "Как пишется: 'о_шибка' или 'оши_ка'?", options: ["ошибка", "ошыбка"], answer: "ошибка", subject: "📝 Русский язык" },
  // Science
  { q: "Сколько планет в Солнечной системе?", options: ["7", "8", "9"], answer: "8", subject: "🌍 Окружающий мир" },
  { q: "Какой газ мы вдыхаем?", options: ["Азот", "Кислород", "Углекислый газ"], answer: "Кислород", subject: "🌍 Окружающий мир" },
  { q: "Столица России?", options: ["Санкт-Петербург", "Москва", "Новосибирск"], answer: "Москва", subject: "🏛️ История" },
  // Literature
  { q: "Кто написал 'Руслан и Людмила'?", options: ["Лермонтов", "Пушкин", "Толстой"], answer: "Пушкин", subject: "📚 Литература" },
  { q: "Сколько богатырей в сказке Пушкина?", options: ["31", "32", "33"], answer: "33", subject: "📚 Литература" },
  // English
  { q: "Как будет 'собака' по-английски?", options: ["cat", "dog", "bird"], answer: "dog", subject: "🇬🇧 Английский" },
  { q: "Translate: 'I am a student'", options: ["Я учитель", "Я ученик", "Я студентка"], answer: "Я ученик", subject: "🇬🇧 Английский" },
]

export default function QuickQuiz() {
  const [question, setQuestion] = useState<typeof QUIZ_QUESTIONS[0] | null>(null)
  const [selected, setSelected] = useState<string | null>(null)
  const [answered, setAnswered] = useState(false)
  const [score, setScore] = useState(0)
  const [total, setTotal] = useState(0)
  const { playCorrect, playWrong, playAchievement } = useSound()

  useEffect(() => {
    nextQuestion()
  }, [])

  const nextQuestion = () => {
    const randomIndex = Math.floor(Math.random() * QUIZ_QUESTIONS.length)
    setQuestion(QUIZ_QUESTIONS[randomIndex])
    setSelected(null)
    setAnswered(false)
  }

  const handleAnswer = (option: string) => {
    if (answered || !question) return
    
    setSelected(option)
    setAnswered(true)
    setTotal(t => t + 1)
    
    if (option === question.answer) {
      playCorrect()
      setScore(s => s + 1)
    } else {
      playWrong()
    }
  }

  if (!question) return null

  return (
    <div className="w-full max-w-md mx-auto p-6 rounded-3xl bg-gradient-to-br from-cyan-500/20 to-blue-500/20 
      border-2 border-cyan-400/30 backdrop-blur-sm">
      
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Zap className="w-6 h-6 text-cyan-400" />
          <span className="font-bold text-cyan-300">Быстрый тест</span>
        </div>
        <div className="text-sm text-white/60">
          {score}/{total} ✅
        </div>
      </div>

      {/* Subject badge */}
      <div className="inline-block px-3 py-1 rounded-full bg-white/10 text-sm text-white/80 mb-4">
        {question.subject}
      </div>

      {/* Question */}
      <h3 className="text-xl font-bold text-white mb-6">{question.q}</h3>

      {/* Options */}
      <div className="space-y-3 mb-4">
        {question.options.map((option, index) => {
          const isSelected = selected === option
          const isCorrect = option === question.answer
          const showCorrect = answered && isCorrect
          const showIncorrect = answered && isSelected && !isCorrect
          
          return (
            <button
              key={index}
              onClick={() => handleAnswer(option)}
              disabled={answered}
              className={`w-full p-4 rounded-2xl text-left font-medium transition-all flex items-center gap-3
                ${showCorrect ? 'bg-gradient-to-r from-green-500 to-emerald-500 text-white' :
                  showIncorrect ? 'bg-gradient-to-r from-red-500 to-rose-500 text-white' :
                  isSelected ? 'bg-gradient-to-r from-cyan-500 to-blue-500 text-white' :
                  'bg-white/10 text-white hover:bg-white/20'}`}
            >
              <span className="w-8 h-8 flex items-center justify-center rounded-full bg-white/20 text-sm font-bold">
                {String.fromCharCode(65 + index)}
              </span>
              {option}
              {showCorrect && <CheckCircle className="w-5 h-5 ml-auto" />}
              {showIncorrect && <XCircle className="w-5 h-5 ml-auto" />}
            </button>
          )
        })}
      </div>

      {/* Result */}
      {answered && (
        <div className={`p-4 rounded-2xl mb-4 ${
          selected === question.answer 
            ? 'bg-green-500/20 text-green-300' 
            : 'bg-red-500/20 text-red-300'
        }`}>
          {selected === question.answer ? (
            <div className="flex items-center gap-2">
              <Trophy className="w-5 h-5" />
              <span className="font-bold">Правильно! Молодец! 🎉</span>
            </div>
          ) : (
            <span>Правильный ответ: <strong>{question.answer}</strong></span>
          )}
        </div>
      )}

      {/* Next button */}
      {answered && (
        <button
          onClick={nextQuestion}
          className="w-full py-4 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-2xl 
            font-bold text-lg hover:scale-[1.02] transition-transform flex items-center justify-center gap-2"
        >
          <RefreshCw className="w-5 h-5" />
          Следующий вопрос
          <Sparkles className="w-5 h-5" />
        </button>
      )}
=======
import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { HelpCircle, ChevronRight } from 'lucide-react'

const QUESTIONS = [
  { q: '2 + 2 = ?', options: ['3', '4', '5'], correct: 1 },
  { q: 'Столица России?', options: ['Москва', 'Париж', 'Лондон'], correct: 0 },
  { q: 'Сколько дней в неделе?', options: ['5', '6', '7'], correct: 2 },
]

export default function QuickQuiz() {
  const { addXP } = useSchool()
  const [index, setIndex] = useState(0)
  const [score, setScore] = useState(0)

  const q = QUESTIONS[index]

  const answer = (idx: number) => {
    if (idx === q.correct) {
      addXP(10)
      setScore(s => s + 1)
    }
    setIndex(i => (i + 1) % QUESTIONS.length)
  }

  return (
    <div className="p-6 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-teal-500/20 border-2 border-cyan-500/30">
      <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <HelpCircle className="w-5 h-5" /> Быстрый квиз
      </h3>
      <p className="text-lg text-white mb-4">{q.q}</p>
      <div className="space-y-2">
        {q.options.map((opt, i) => (
          <button
            key={i}
            onClick={() => answer(i)}
            className="w-full p-4 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold flex items-center justify-between"
          >
            {opt} <ChevronRight className="w-5 h-5" />
          </button>
        ))}
      </div>
      <p className="text-center text-purple-300 mt-4">Счёт: {score}</p>
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
    </div>
  )
}
