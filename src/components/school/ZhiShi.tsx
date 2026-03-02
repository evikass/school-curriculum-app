'use client'
import { useState, useEffect } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { useSound } from '@/hooks/useSound'
import { RefreshCw, Star, BookOpen } from 'lucide-react'

const RULES = [
  {
    rule: 'ЖИ-ШИ',
    pattern: ['ЖИ', 'ШИ'],
    correct: 'И',
    wrong: 'Ы',
    examples: ['ЖИЗНЬ', 'ШИНА', 'ЖИРАФ', 'ШИШКА', 'МАШИНА', 'КНИЖКА', 'УШИ', 'ЛЫЖИ', 'ЕЖИ', 'МЫШИ'],
    wrongExamples: ['ЖЫЗНЬ', 'ШЫНА', 'ЖЫРАФ', 'ШЫШКА']
  },
  {
    rule: 'ЧА-ЩА',
    pattern: ['ЧА', 'ЩА'],
    correct: 'А',
    wrong: 'Я',
    examples: ['ЧАШКА', 'ЩАВЕЛЬ', 'ЧАСЫ', 'ЩУКА', 'ДАЧА', 'ЗАДАЧА', 'РОЩА', 'ТОВАРИЩ', 'ЧАЙ', 'ЧАЩА'],
    wrongExamples: ['ЧЯШКА', 'ЩЯВЕЛЬ', 'ЧЯСЫ', 'РОЩЯ']
  },
  {
    rule: 'ЧУ-ЩУ',
    pattern: ['ЧУ', 'ЩУ'],
    correct: 'У',
    wrong: 'Ю',
    examples: ['ЧУДО', 'ЩУКА', 'ЧУГУН', 'ЧУТЬ', 'ЧУМА', 'ЩУПАЛЬЦЕ', 'ЧУЛОК', 'ЧУТЬЁ', 'ЧУДИЩЕ', 'ПЛАЩУ'],
    wrongExamples: ['ЧЮДО', 'ЩЮКА', 'ЧЮГУН', 'ЩЮПАЛЬЦЕ']
  }
]

type Difficulty = 'easy' | 'medium' | 'hard'
type GameMode = 'fill' | 'find' | 'rule'

export default function ZhiShi() {
  const { addXP } = useSchool()
  const { playCorrect, playWrong } = useSound()
  const [mode, setMode] = useState<GameMode>('fill')
  const [difficulty, setDifficulty] = useState<Difficulty>('easy')
  const [score, setScore] = useState(0)
  const [streak, setStreak] = useState(0)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  
  const [currentWord, setCurrentWord] = useState<{ word: string; rule: typeof RULES[0]; blankIndex: number } | null>(null)
  const [options, setOptions] = useState<string[]>([])
  const [ruleToShow, setRuleToShow] = useState<typeof RULES[0] | null>(null)
  const [wrongWord, setWrongWord] = useState<{ wrong: string; correct: string } | null>(null)

  const getAllWords = () => RULES.flatMap(r => r.examples.map(w => ({ word: w, rule: r })))

  const generateFillQuestion = () => {
    const allWords = getAllWords()
    const { word, rule } = allWords[Math.floor(Math.random() * allWords.length)]
    
    let blankIndex = -1
    for (let i = 0; i < word.length - 1; i++) {
      const twoLetters = word.slice(i, i + 2)
      if (rule.pattern.includes(twoLetters)) {
        blankIndex = i + 1
        break
      }
    }
    
    setCurrentWord({ word, rule, blankIndex })
    setOptions([rule.correct, rule.wrong].sort(() => Math.random() - 0.5))
  }

  const generateFindQuestion = () => {
    const useWrong = Math.random() > 0.5
    const rule = RULES[Math.floor(Math.random() * RULES.length)]
    
    if (useWrong) {
      const wrong = rule.wrongExamples[Math.floor(Math.random() * rule.wrongExamples.length)]
      const correct = rule.examples.find(e => 
        e.slice(0, -2) === wrong.slice(0, -2) || 
        e.replace(rule.wrong, rule.correct) === wrong.replace(rule.wrong, rule.correct)
      ) || rule.examples[0]
      setWrongWord({ wrong, correct })
    } else {
      const correct = rule.examples[Math.floor(Math.random() * rule.examples.length)]
      setWrongWord({ wrong: correct, correct })
    }
  }

  const generateRuleQuestion = () => {
    setRuleToShow(RULES[Math.floor(Math.random() * RULES.length)])
  }

  useEffect(() => {
    if (mode === 'fill') generateFillQuestion()
    else if (mode === 'find') generateFindQuestion()
    else generateRuleQuestion()
  }, [mode])

  const handleFillAnswer = (answer: string) => {
    if (!currentWord) return
    const correct = answer === currentWord.rule.correct
    
    if (correct) {
      playCorrect()
      const points = difficulty === 'easy' ? 10 : difficulty === 'medium' ? 15 : 20
      setScore(s => s + points)
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
      generateFillQuestion()
    }, 1000)
  }

  const handleFindAnswer = (isCorrect: boolean) => {
    if (!wrongWord) return
    const wordIsCorrect = !wrongWord.wrong.includes(wrongWord.correct)
    const answeredCorrect = isCorrect === wordIsCorrect
    
    if (answeredCorrect) {
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
      generateFindQuestion()
    }, 1000)
  }

  const handleRuleAnswer = (ruleName: string) => {
    if (!ruleToShow) return
    const correct = ruleName === ruleToShow.rule
    
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
      generateRuleQuestion()
    }, 1000)
  }

  const reset = () => {
    setScore(0)
    setStreak(0)
    if (mode === 'fill') generateFillQuestion()
    else if (mode === 'find') generateFindQuestion()
    else generateRuleQuestion()
  }

  return (
    <div className="bg-gradient-to-br from-green-500/20 to-teal-500/20 rounded-2xl p-6 backdrop-blur-sm">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <span className="text-3xl">📝</span> ЖИ-ШИ, ЧА-ЩА, ЧУ-ЩУ
        </h2>
        <div className="flex items-center gap-4">
          <span className="text-yellow-400 font-bold">⭐ {score}</span>
          {streak > 2 && <span className="text-orange-400 text-sm">🔥 {streak}</span>}
        </div>
      </div>

      <div className="flex gap-2 mb-3">
        {(['fill', 'find', 'rule'] as GameMode[]).map(m => (
          <button
            key={m}
            onClick={() => { setMode(m); reset() }}
            className={`flex-1 py-2 rounded-lg text-sm font-medium transition-all ${mode === m ? 'bg-green-500 text-white' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}
          >
            {m === 'fill' ? '✏️ Вставь букву' : m === 'find' ? '🔍 Найди ошибку' : '📖 Выбери правило'}
          </button>
        ))}
      </div>

      <div className="flex gap-2 mb-4">
        {(['easy', 'medium', 'hard'] as Difficulty[]).map(d => (
          <button
            key={d}
            onClick={() => { setDifficulty(d); reset() }}
            className={`flex-1 py-1 rounded-lg text-xs font-medium transition-all ${difficulty === d ? 'bg-teal-500 text-white' : 'bg-white/10 text-white/50 hover:bg-white/20'}`}
          >
            {d === 'easy' ? 'Легко' : d === 'medium' ? 'Средне' : 'Сложно'}
          </button>
        ))}
      </div>

      <div className={`transition-all duration-200 ${feedback === 'correct' ? 'scale-105' : feedback === 'wrong' ? 'scale-95' : ''}`}>
        {mode === 'fill' && currentWord && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Вставь пропущенную букву:</div>
            <div className="text-5xl font-black text-white mb-6 flex justify-center items-center gap-1">
              {currentWord.word.split('').map((letter, i) => (
                <span
                  key={i}
                  className={`${i === currentWord.blankIndex ? 'w-12 h-14 border-b-4 border-yellow-400 text-yellow-400' : ''} ${feedback === 'correct' && i === currentWord.blankIndex ? 'text-green-400' : ''}`}
                >
                  {i === currentWord.blankIndex ? (feedback ? currentWord.rule.correct : '_') : letter}
                </span>
              ))}
            </div>
            <div className="flex justify-center gap-4">
              {options.map(opt => (
                <button
                  key={opt}
                  onClick={() => handleFillAnswer(opt)}
                  className="w-20 h-20 rounded-xl bg-gradient-to-br from-green-400 to-teal-500 text-white text-4xl font-bold hover:scale-110 transition-transform shadow-lg"
                >
                  {opt}
                </button>
              ))}
            </div>
          </div>
        )}

        {mode === 'find' && wrongWord && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Правильно ли написано слово?</div>
            <div className={`text-5xl font-black mb-6 ${feedback === 'correct' ? 'text-green-400' : feedback === 'wrong' ? 'text-red-400' : 'text-white'}`}>
              {wrongWord.wrong}
            </div>
            <div className="flex justify-center gap-4">
              <button
                onClick={() => handleFindAnswer(true)}
                className="px-8 py-4 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
              >
                ✅ Правильно
              </button>
              <button
                onClick={() => handleFindAnswer(false)}
                className="px-8 py-4 bg-gradient-to-r from-red-500 to-pink-500 rounded-xl text-white font-bold text-xl hover:scale-105 transition-transform shadow-lg"
              >
                ❌ Ошибка
              </button>
            </div>
            {feedback === 'wrong' && (
              <div className="mt-4 text-yellow-300">
                Правильно: {wrongWord.correct}
              </div>
            )}
          </div>
        )}

        {mode === 'rule' && ruleToShow && (
          <div className="text-center">
            <div className="mb-4 text-white/60">Какое правило здесь применяется?</div>
            <div className="text-3xl font-black text-white mb-6">
              {ruleToShow.examples.slice(0, 3).join(', ')}
            </div>
            <div className="flex justify-center gap-3 flex-wrap">
              {RULES.map(r => (
                <button
                  key={r.rule}
                  onClick={() => handleRuleAnswer(r.rule)}
                  className="px-6 py-3 bg-gradient-to-r from-green-400 to-teal-500 rounded-xl text-white font-bold hover:scale-105 transition-transform shadow-lg"
                >
                  {r.rule}
                </button>
              ))}
            </div>
            {feedback && (
              <div className={`mt-4 p-3 rounded-lg ${feedback === 'correct' ? 'bg-green-500/20 text-green-300' : 'bg-red-500/20 text-red-300'}`}>
                Правило: пиши <strong>{ruleToShow.pattern.join(' и ')}</strong> с буквой <strong>{ruleToShow.correct}</strong>
              </div>
            )}
          </div>
        )}
      </div>

      <div className="flex justify-center mt-4 gap-4">
        <button onClick={reset} className="text-white/50 hover:text-white transition-colors flex items-center gap-1">
          <RefreshCw className="w-4 h-4" /> Заново
        </button>
      </div>

      <div className="mt-4 p-3 bg-white/5 rounded-lg">
        <div className="text-white/60 text-sm mb-2">📖 Запомни правила:</div>
        <div className="grid grid-cols-3 gap-2 text-sm">
          <div className="text-center p-2 bg-pink-500/20 rounded-lg">
            <div className="font-bold text-pink-300">ЖИ-ШИ</div>
            <div className="text-white/70">пиши с И</div>
          </div>
          <div className="text-center p-2 bg-yellow-500/20 rounded-lg">
            <div className="font-bold text-yellow-300">ЧА-ЩА</div>
            <div className="text-white/70">пиши с А</div>
          </div>
          <div className="text-center p-2 bg-blue-500/20 rounded-lg">
            <div className="font-bold text-blue-300">ЧУ-ЩУ</div>
            <div className="text-white/70">пиши с У</div>
          </div>
        </div>
      </div>
    </div>
  )
}
