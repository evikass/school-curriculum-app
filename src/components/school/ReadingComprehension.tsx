'use client'

import { useState } from 'react'
import { useSchool } from '@/context/SchoolContext'
import { BookOpen, Star, Trophy, RotateCcw, Zap, ChevronRight, FileText } from 'lucide-react'

interface Question {
  question: string
  options: string[]
  correct: number
}

interface ReadingText {
  title: string
  text: string
  difficulty: 'easy' | 'medium' | 'hard'
  questions: Question[]
}

const TEXTS: ReadingText[] = [
  {
    title: 'Бобры — удивительные строители',
    difficulty: 'easy',
    text: 'Бобры — это крупные грызуны, которые живут возле рек и озёр. Они известны своим умением строить плотины из веток и брёвен. Бобры валят деревья, перегрызая их своими мощными зубами. Плотины бобров создают пруды, в которых эти животные строят свои домики-хатки. Вход в хатку находится под водой — так бобры защищаются от хищников. Бобры — отличные пловцы, они могут оставаться под водой до 15 минут!',
    questions: [
      { question: 'Где живут бобры?', options: ['В лесу', 'Возле рек и озёр', 'В горах', 'В пустыне'], correct: 1 },
      { question: 'Что строят бобры?', options: ['Гнёзда', 'Норы', 'Плотины', 'Дупла'], correct: 2 },
      { question: 'Где находится вход в хатку бобра?', options: ['Сверху', 'Под водой', 'На суше', 'На дереве'], correct: 1 },
      { question: 'Сколько минут бобр может оставаться под водой?', options: ['5 минут', '10 минут', '15 минут', '20 минут'], correct: 2 },
    ]
  },
  {
    title: 'Великая Китайская стена',
    difficulty: 'medium',
    text: 'Великая Китайская стена — это одно из самых грандиозных сооружений в истории человечества. Её строительство началось более 2000 лет назад для защиты от вражеских нашествий. Общая длина стены составляет более 21 000 километров! Строительство продолжалось столетиями, и в нём участвовали миллионы рабочих. Многие из них погибли от тяжёлых условий труда. Стена настолько длинная, что её можно увидеть из космоса. Сегодня это популярная туристическая достопримечательность и символ Китая.',
    questions: [
      { question: 'Для чего была построена стена?', options: ['Для красоты', 'Для защиты от врагов', 'Как дорогу', 'Для хранения зерна'], correct: 1 },
      { question: 'Сколько километров составляет длина стены?', options: ['Более 10 000 км', 'Более 21 000 км', 'Более 30 000 км', 'Более 5 000 км'], correct: 1 },
      { question: 'Когда началось строительство?', options: ['100 лет назад', '500 лет назад', 'Более 2000 лет назад', '1000 лет назад'], correct: 2 },
      { question: 'Что случилось со многими рабочими?', options: ['Разбогатели', 'Погибли', 'Уехали', 'Стали знамениты'], correct: 1 },
    ]
  },
  {
    title: 'Как работает сердце',
    difficulty: 'medium',
    text: 'Сердце — это мышечный орган, который непрерывно перекачивает кровь по всему организму. Размер сердца примерно равен размеру кулака человека. За одну минуту сердце совершает около 60-80 ударов, а за всю жизнь — более 2 миллиардов ударов! Кровь переносит кислород и питательные вещества ко всем клеткам тела. Сердце разделено на четыре камеры: два предсердия и два желудочка. Правая сторона сердца получает кровь от органов и направляет её в лёгкие для насыщения кислородом, а левая — перекачивает обогащённую кислородом кровь к органам.',
    questions: [
      { question: 'Какой размер у сердца?', options: ['Размером с монету', 'Размером с кулак', 'Размером с ладонь', 'Размером с яблоко'], correct: 1 },
      { question: 'Сколько ударов делает сердце за минуту?', options: ['20-30', '40-50', '60-80', '100-120'], correct: 2 },
      { question: 'На сколько камер разделено сердце?', options: ['На две', 'На три', 'На четыре', 'На пять'], correct: 2 },
      { question: 'Куда направляет кровь правая сторона сердца?', options: ['К органам', 'В мозг', 'В лёгкие', 'К ногам'], correct: 2 },
    ]
  },
  {
    title: 'Путешествие света',
    difficulty: 'hard',
    text: 'Свет от Солнца до Земли путешествует около 8 минут, хотя расстояние между ними составляет примерно 150 миллионов километров. Скорость света — самая большая скорость во Вселенной: около 300 000 километров в секунду! Интересно, что когда мы смотрим на звёзды, мы видим их не такими, какие они сейчас, а какими они были много лет назад. Например, свет от ближайшей к нам звезды (после Солнца) Проксимы Центавра идёт до нас более 4 лет. Это значит, что если звезда погаснет сегодня, мы узнаем об этом только через 4 года. Астрономы называют это явление «смотреть в прошлое».',
    questions: [
      { question: 'Сколько времени свет идёт от Солнца до Земли?', options: ['1 минуту', '8 минут', '15 минут', '1 час'], correct: 1 },
      { question: 'Какова скорость света?', options: ['100 000 км/с', '200 000 км/с', '300 000 км/с', '500 000 км/с'], correct: 2 },
      { question: 'Что означает «смотреть в прошлое» для астрономов?', options: ['Изучать историю', 'Видеть звёзды какими они были раньше', 'Смотреть старые записи', 'Вспоминать прошлое'], correct: 1 },
      { question: 'Сколько лет идёт свет от Проксимы Центавра?', options: ['1 год', '2 года', 'Более 4 лет', 'Более 10 лет'], correct: 2 },
    ]
  },
  {
    title: 'Муравьи — маленькие труженики',
    difficulty: 'easy',
    text: 'Муравьи — одни из самых удивительных насекомых на Земле. Они живут большими семьями в муравейниках. Каждый муравей имеет свою работу: одни добывают еду, другие охраняют гнездо, третьи ухаживают за личинками. Муравьи могут поднимать предметы, которые в 50 раз тяжелее их собственного веса! Они общаются друг с другом с помощью запахов — феромонов. Если муравей находит еду, он оставляет запах, по которому другие муравьи могут найти путь к ней. Муравьи живут на всех континентах, кроме Антарктиды.',
    questions: [
      { question: 'Где живут муравьи?', options: ['Поодиночке', 'В муравейниках семьями', 'В дуплах', 'Под водой'], correct: 1 },
      { question: 'Во сколько раз муравей может поднять вес больше своего?', options: ['В 10 раз', 'В 25 раз', 'В 50 раз', 'В 100 раз'], correct: 2 },
      { question: 'Как муравьи общаются между собой?', options: ['Звуками', 'Прикосновениями', 'Запахами', 'Взглядами'], correct: 2 },
      { question: 'На каком континенте муравьи НЕ живут?', options: ['Африка', 'Австралия', 'Антарктида', 'Европа'], correct: 2 },
    ]
  },
]

const DIFFICULTY_CONFIG = {
  easy: { xp: 15, color: 'from-green-500/20 to-emerald-500/20', border: 'border-green-500/30', badge: 'bg-green-500/20 text-green-300', label: 'Лёгкий' },
  medium: { xp: 20, color: 'from-blue-500/20 to-cyan-500/20', border: 'border-blue-500/30', badge: 'bg-blue-500/20 text-blue-300', label: 'Средний' },
  hard: { xp: 30, color: 'from-purple-500/20 to-pink-500/20', border: 'border-purple-500/30', badge: 'bg-purple-500/20 text-purple-300', label: 'Сложный' },
}

export default function ReadingComprehension() {
  const { addPoints } = useSchool()
  const [selectedText, setSelectedText] = useState<ReadingText | null>(null)
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [answered, setAnswered] = useState(false)
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null)
  const [gameOver, setGameOver] = useState(false)
  const [showText, setShowText] = useState(true)

  const currentQuestion = selectedText?.questions[currentQuestionIndex]

  const selectText = (text: ReadingText) => {
    setSelectedText(text)
    setCurrentQuestionIndex(0)
    setScore(0)
    setGameOver(false)
    setAnswered(false)
    setSelectedAnswer(null)
    setShowText(true)
  }

  const handleAnswer = (idx: number) => {
    if (answered || !currentQuestion) return
    setAnswered(true)
    setSelectedAnswer(idx)
    
    if (idx === currentQuestion.correct) {
      const xp = DIFFICULTY_CONFIG[selectedText!.difficulty].xp
      addPoints(xp)
      setScore(s => s + 1)
    }
  }

  const nextQuestion = () => {
    if (!selectedText) return
    if (currentQuestionIndex < selectedText.questions.length - 1) {
      setCurrentQuestionIndex(i => i + 1)
      setAnswered(false)
      setSelectedAnswer(null)
      setShowText(false) // После первого вопроса текст скрыт
    } else {
      setGameOver(true)
    }
  }

  const resetGame = () => {
    setSelectedText(null)
    setCurrentQuestionIndex(0)
    setScore(0)
    setGameOver(false)
    setAnswered(false)
    setSelectedAnswer(null)
    setShowText(true)
  }

  // Выбор текста
  if (!selectedText) {
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-violet-500/20 border-2 border-indigo-500/30">
        <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
          <BookOpen className="w-6 h-6 text-indigo-400" />
          Чтение с пониманием
        </h3>
        <p className="text-indigo-200 mb-6">Выберите текст для чтения:</p>
        <div className="space-y-3">
          {TEXTS.map((text, i) => (
            <button
              key={i}
              onClick={() => selectText(text)}
              className={`w-full p-4 rounded-xl bg-gradient-to-r ${DIFFICULTY_CONFIG[text.difficulty].color} border-2 ${DIFFICULTY_CONFIG[text.difficulty].border} hover:scale-[1.01] transition-all text-left`}
            >
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white font-bold">{text.title}</p>
                  <p className="text-indigo-300 text-sm">{text.questions.length} вопроса</p>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`px-3 py-1 rounded-full text-sm ${DIFFICULTY_CONFIG[text.difficulty].badge}`}>
                    {DIFFICULTY_CONFIG[text.difficulty].label}
                  </span>
                  <span className="text-indigo-300 text-sm flex items-center gap-1">
                    <Zap className="w-3 h-3" /> +{DIFFICULTY_CONFIG[text.difficulty].xp} XP
                  </span>
                </div>
              </div>
            </button>
          ))}
        </div>
      </div>
    )
  }

  // Результаты
  if (gameOver) {
    const percentage = Math.round((score / selectedText.questions.length) * 100)
    return (
      <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-violet-500/20 border-2 border-indigo-500/30 text-center">
        <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
        <h3 className="text-2xl font-bold text-white mb-2">Результат</h3>
        <p className="text-indigo-200 mb-2">Текст: {selectedText.title}</p>
        <p className="text-4xl font-bold text-indigo-300 mb-2">{score} / {selectedText.questions.length}</p>
        <p className="text-lg text-indigo-200 mb-4">
          {percentage >= 80 ? 'Отличное понимание! 📖' : percentage >= 60 ? 'Хорошо! 👍' : 'Попробуй прочитать внимательнее 📚'}
        </p>
        <p className="text-indigo-300 mb-4">Заработано XP: {score * DIFFICULTY_CONFIG[selectedText.difficulty].xp}</p>
        <div className="flex gap-3 justify-center">
          <button
            onClick={() => selectText(selectedText)}
            className="px-6 py-3 bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white font-bold transition-colors flex items-center gap-2"
          >
            <RotateCcw className="w-4 h-4" /> Прочитать снова
          </button>
          <button
            onClick={resetGame}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 rounded-xl text-white font-bold transition-colors"
          >
            Другой текст
          </button>
        </div>
      </div>
    )
  }

  if (!currentQuestion) return null

  const config = DIFFICULTY_CONFIG[selectedText.difficulty]

  return (
    <div className={`p-6 rounded-2xl bg-gradient-to-br ${config.color} border-2 ${config.border}`}>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-bold text-white flex items-center gap-2">
          <FileText className="w-5 h-5 text-indigo-400" />
          {selectedText.title}
        </h3>
        <div className="flex items-center gap-2">
          <span className={`px-3 py-1 rounded-full text-sm ${config.badge}`}>
            {config.label}
          </span>
          <span className="text-indigo-300 text-sm">
            Вопрос {currentQuestionIndex + 1}/{selectedText.questions.length}
          </span>
        </div>
      </div>

      {showText && (
        <div className="bg-white/5 rounded-xl p-4 mb-4 border border-white/10">
          <p className="text-white/90 text-sm leading-relaxed whitespace-pre-line">{selectedText.text}</p>
        </div>
      )}

      {!showText && (
        <button
          onClick={() => setShowText(true)}
          className="mb-4 w-full p-2 bg-white/5 hover:bg-white/10 rounded-lg text-indigo-300 text-sm flex items-center justify-center gap-2"
        >
          <BookOpen className="w-4 h-4" /> Показать текст
        </button>
      )}

      <div className="bg-white/10 rounded-xl p-4 mb-4">
        <p className="text-white font-medium">{currentQuestion.question}</p>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {currentQuestion.options.map((opt, i) => {
          const isCorrect = i === currentQuestion.correct
          const isSelected = i === selectedAnswer
          
          let buttonClass = 'p-3 rounded-xl text-white font-medium transition-all '
          
          if (!answered) {
            buttonClass += 'bg-white/10 hover:bg-white/20 hover:scale-[1.02]'
          } else if (isCorrect) {
            buttonClass += 'bg-indigo-500/50 border-2 border-indigo-400'
          } else if (isSelected && !isCorrect) {
            buttonClass += 'bg-red-500/50 border-2 border-red-400'
          } else {
            buttonClass += 'bg-white/5 opacity-50'
          }
          
          return (
            <button
              key={i}
              onClick={() => handleAnswer(i)}
              disabled={answered}
              className={buttonClass}
            >
              <span className="flex items-center justify-center gap-2">
                {opt}
                {answered && isCorrect && <Star className="w-4 h-4 text-yellow-300" />}
              </span>
            </button>
          )
        })}
      </div>

      {answered && (
        <button
          onClick={nextQuestion}
          className="mt-4 w-full p-3 bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white font-bold transition-colors flex items-center justify-center gap-2"
        >
          {currentQuestionIndex < selectedText.questions.length - 1 ? (
            <>Следующий вопрос <ChevronRight className="w-4 h-4" /></>
          ) : (
            'Показать результат'
          )}
        </button>
      )}

      <div className="flex items-center justify-between mt-4 text-indigo-300 text-sm">
        <span className="flex items-center gap-1"><Star className="w-4 h-4" /> Счёт: {score}</span>
        <span className="flex items-center gap-1"><Zap className="w-4 h-4" /> XP: {score * config.xp}</span>
      </div>
    </div>
  )
}
