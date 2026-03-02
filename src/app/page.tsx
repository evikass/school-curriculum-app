'use client'

import { SchoolProvider, useSchool } from '@/context/SchoolContext'
import { GradeSelector, SubjectGrid, LessonViewer, KidSubjectGrid, KidLessonViewer, GameSection, Gameplay, AchievementsDisplay, AnimatedBackground, KidGradeSelector, LevelProgress, DailyBonus, KidGameSection, StreakCalendar, SoundToggle, ThemeSelector, ExtendedQuickQuiz, LearningPath, ChallengeMode, MemoryGame, DailyChallenge, FlashCards, SpeedTest, StatsDashboard, TypingPractice, SpellingGame, NumberPuzzle, WordScramble, MathRacing, TriviaBattle, CrosswordGame, SentenceBuilder, ColorMatch, WordSearch, SequenceGame, EmojiQuiz, GeographyQuiz, HangmanGame, TrueOrFalse, AnagramGame, OddOneOut, SoundQuiz, MathPuzzle, WordChain, QuickMath, AlphabetSort, SynonymAntonym, FlagsQuiz, TimeQuiz, Riddles, Proverbs, PunctuationQuiz, CapitalCities, RomanNumerals, FractionCompare, PercentQuiz, GeometryQuiz, NatureQuiz, HistoryQuiz, ScienceQuiz, MeasurementQuiz, EquationSolver, PartsOfSpeech, WordFormation, Syllables, StressMark, MultiplicationTable, Antonyms, WordCases, DivisionTable, Homonyms, Conjugations, CompareNumbers, Abbreviations, PrimeNumbers, VowelsConsonants, ZhiShi, DaysOfWeek, EvenOdd, ShapesQuiz, SimpleMath, CountingGame } from '@/components/school'
import { useState, useEffect } from 'react'
import { Calendar, Gamepad2, Map, Timer, Brain, Gift, Zap, BarChart, Layers, Pen, Calculator, Shuffle, Car, Swords, Grid3X3, MessageSquare, Palette, Search, Hash, Smile, Globe, CheckCircle, RefreshCw, Target, Volume2, Link2, ArrowUpAz, ArrowRightLeft, Flag, Clock, HelpCircle, BookOpen, PenTool, Building2, Languages, Scale, Percent, CircleDot, Leaf, ScrollText, Atom, Ruler, BookOpenCheck, Puzzle, AudioLines, X, Divide, BookCopy, ArrowLeftRight, Abbreviate, Type, SpellCheck, CalendarDays, Hexagon, Plus, Circle } from 'lucide-react'

function getTodayString(): string { return new Date().toISOString().split('T')[0] }
type MiniGameType = 'challenge' | 'memory' | 'daily' | 'flashcards' | 'speedtest' | 'stats' | 'typing' | 'spelling' | 'puzzle' | 'scramble' | 'racing' | 'trivia' | 'crossword' | 'sentence' | 'colormatch' | 'wordsearch' | 'sequence' | 'emoji' | 'geography' | 'hangman' | 'truefalse' | 'anagram' | 'oddoneout' | 'soundquiz' | 'mathpuzzle' | 'wordchain' | 'quickmath' | 'multiply' | 'divide' | 'alphabetsort' | 'synonym' | 'antonyms' | 'homonyms' | 'flags' | 'timequiz' | 'riddles' | 'proverbs' | 'punctuation' | 'capitals' | 'roman' | 'fraction' | 'percent' | 'geometry' | 'nature' | 'history' | 'science' | 'measurement' | 'equation' | 'parts' | 'wordform' | 'syllables' | 'stress' | 'cases' | 'conjugations' | 'compare' | 'abbr' | 'prime' | 'vowels' | 'zhishi' | 'days' | 'evenodd' | 'shapes' | 'simplemath' | 'counting' | null

const GAME_BUTTONS: { id: MiniGameType; icon: React.ReactNode; label: string; color: string }[] = [
  { id: 'flashcards', icon: <Layers className="w-3 h-3 inline mr-1" />, label: 'Карточки', color: 'teal' },
  { id: 'speedtest', icon: <Zap className="w-3 h-3 inline mr-1" />, label: 'Спид', color: 'yellow' },
  { id: 'typing', icon: <Pen className="w-3 h-3 inline mr-1" />, label: 'Печать', color: 'slate' },
  { id: 'spelling', icon: <Pen className="w-3 h-3 inline mr-1" />, label: 'Орфо', color: 'pink' },
  { id: 'puzzle', icon: <Calculator className="w-3 h-3 inline mr-1" />, label: 'Голов.', color: 'emerald' },
  { id: 'scramble', icon: <Shuffle className="w-3 h-3 inline mr-1" />, label: 'Слова', color: 'teal' },
  { id: 'racing', icon: <Car className="w-3 h-3 inline mr-1" />, label: 'Гонка', color: 'orange' },
  { id: 'trivia', icon: <Swords className="w-3 h-3 inline mr-1" />, label: 'Битва', color: 'indigo' },
  { id: 'crossword', icon: <Grid3X3 className="w-3 h-3 inline mr-1" />, label: 'Кросс', color: 'blue' },
  { id: 'sentence', icon: <MessageSquare className="w-3 h-3 inline mr-1" />, label: 'Предл', color: 'emerald' },
  { id: 'colormatch', icon: <Palette className="w-3 h-3 inline mr-1" />, label: 'Цвета', color: 'pink' },
  { id: 'wordsearch', icon: <Search className="w-3 h-3 inline mr-1" />, label: 'Поиск', color: 'cyan' },
  { id: 'sequence', icon: <Hash className="w-3 h-3 inline mr-1" />, label: 'Ряд', color: 'violet' },
  { id: 'emoji', icon: <Smile className="w-3 h-3 inline mr-1" />, label: 'Эмодзи', color: 'amber' },
  { id: 'geography', icon: <Globe className="w-3 h-3 inline mr-1" />, label: 'Гео', color: 'emerald' },
  { id: 'hangman', icon: <Gamepad2 className="w-3 h-3 inline mr-1" />, label: 'Висел', color: 'slate' },
  { id: 'truefalse', icon: <CheckCircle className="w-3 h-3 inline mr-1" />, label: 'П/Л', color: 'rose' },
  { id: 'anagram', icon: <RefreshCw className="w-3 h-3 inline mr-1" />, label: 'Анагр', color: 'fuchsia' },
  { id: 'oddoneout', icon: <Target className="w-3 h-3 inline mr-1" />, label: 'Лишн', color: 'sky' },
  { id: 'soundquiz', icon: <Volume2 className="w-3 h-3 inline mr-1" />, label: 'Звук', color: 'orange' },
  { id: 'mathpuzzle', icon: <Calculator className="w-3 h-3 inline mr-1" />, label: 'Гол', color: 'indigo' },
  { id: 'wordchain', icon: <Link2 className="w-3 h-3 inline mr-1" />, label: 'Цепь', color: 'green' },
  { id: 'quickmath', icon: <Zap className="w-3 h-3 inline mr-1" />, label: 'Быстр', color: 'amber' },
  { id: 'multiply', icon: <X className="w-3 h-3 inline mr-1" />, label: 'ТабУ', color: 'blue' },
  { id: 'divide', icon: <Divide className="w-3 h-3 inline mr-1" />, label: 'ТабД', color: 'emerald' },
  { id: 'alphabetsort', icon: <ArrowUpAz className="w-3 h-3 inline mr-1" />, label: 'А-Я', color: 'teal' },
  { id: 'synonym', icon: <ArrowRightLeft className="w-3 h-3 inline mr-1" />, label: 'Син', color: 'purple' },
  { id: 'antonyms', icon: <ArrowRightLeft className="w-3 h-3 inline mr-1" />, label: 'Антон', color: 'fuchsia' },
  { id: 'homonyms', icon: <BookCopy className="w-3 h-3 inline mr-1" />, label: 'Омон', color: 'orange' },
  { id: 'flags', icon: <Flag className="w-3 h-3 inline mr-1" />, label: 'Флаг', color: 'blue' },
  { id: 'timequiz', icon: <Clock className="w-3 h-3 inline mr-1" />, label: 'Часы', color: 'amber' },
  { id: 'riddles', icon: <HelpCircle className="w-3 h-3 inline mr-1" />, label: 'Загад', color: 'violet' },
  { id: 'proverbs', icon: <BookOpen className="w-3 h-3 inline mr-1" />, label: 'Посл', color: 'rose' },
  { id: 'punctuation', icon: <PenTool className="w-3 h-3 inline mr-1" />, label: 'Знак', color: 'cyan' },
  { id: 'capitals', icon: <Building2 className="w-3 h-3 inline mr-1" />, label: 'Стол', color: 'emerald' },
  { id: 'roman', icon: <Languages className="w-3 h-3 inline mr-1" />, label: 'Рим', color: 'stone' },
  { id: 'fraction', icon: <Scale className="w-3 h-3 inline mr-1" />, label: 'Дроб', color: 'indigo' },
  { id: 'percent', icon: <Percent className="w-3 h-3 inline mr-1" />, label: '%', color: 'orange' },
  { id: 'geometry', icon: <CircleDot className="w-3 h-3 inline mr-1" />, label: 'Фиг', color: 'lime' },
  { id: 'nature', icon: <Leaf className="w-3 h-3 inline mr-1" />, label: 'Прир', color: 'green' },
  { id: 'history', icon: <ScrollText className="w-3 h-3 inline mr-1" />, label: 'Ист', color: 'amber' },
  { id: 'science', icon: <Atom className="w-3 h-3 inline mr-1" />, label: 'Наук', color: 'violet' },
  { id: 'measurement', icon: <Ruler className="w-3 h-3 inline mr-1" />, label: 'Измер', color: 'teal' },
  { id: 'equation', icon: <Calculator className="w-3 h-3 inline mr-1" />, label: 'Урав', color: 'indigo' },
  { id: 'parts', icon: <BookOpenCheck className="w-3 h-3 inline mr-1" />, label: 'ЧРеч', color: 'rose' },
  { id: 'wordform', icon: <Puzzle className="w-3 h-3 inline mr-1" />, label: 'Сост', color: 'amber' },
  { id: 'syllables', icon: <AudioLines className="w-3 h-3 inline mr-1" />, label: 'Слог', color: 'cyan' },
  { id: 'stress', icon: <Volume2 className="w-3 h-3 inline mr-1" />, label: 'Удар', color: 'red' },
  { id: 'cases', icon: <BookOpen className="w-3 h-3 inline mr-1" />, label: 'Падеж', color: 'violet' },
  { id: 'conjugations', icon: <PenTool className="w-3 h-3 inline mr-1" />, label: 'Спряг', color: 'pink' },
  { id: 'compare', icon: <ArrowLeftRight className="w-3 h-3 inline mr-1" />, label: 'Сравн', color: 'sky' },
  { id: 'abbr', icon: <Abbreviate className="w-3 h-3 inline mr-1" />, label: 'Аббр', color: 'amber' },
  { id: 'prime', icon: <Hash className="w-3 h-3 inline mr-1" />, label: 'Прост', color: 'violet' },
  { id: 'vowels', icon: <Type className="w-3 h-3 inline mr-1" />, label: 'Гл/Сог', color: 'pink' },
  { id: 'zhishi', icon: <SpellCheck className="w-3 h-3 inline mr-1" />, label: 'ЖИ-ШИ', color: 'green' },
  { id: 'days', icon: <CalendarDays className="w-3 h-3 inline mr-1" />, label: 'Дни', color: 'amber' },
  { id: 'evenodd', icon: <Hash className="w-3 h-3 inline mr-1" />, label: 'Чёт', color: 'cyan' },
  { id: 'shapes', icon: <Hexagon className="w-3 h-3 inline mr-1" />, label: 'Фигуры', color: 'rose' },
  { id: 'simplemath', icon: <Plus className="w-3 h-3 inline mr-1" />, label: '+/-', color: 'emerald' },
  { id: 'counting', icon: <Circle className="w-3 h-3 inline mr-1" />, label: 'Счёт', color: 'yellow' },
  { id: 'challenge', icon: <Timer className="w-3 h-3 inline mr-1" />, label: 'Челлендж', color: 'red' },
  { id: 'memory', icon: <Brain className="w-3 h-3 inline mr-1" />, label: 'Память', color: 'purple' },
  { id: 'daily', icon: <Gift className="w-3 h-3 inline mr-1" />, label: 'Ежедн', color: 'amber' },
  { id: 'stats', icon: <BarChart className="w-3 h-3 inline mr-1" />, label: 'Стат', color: 'blue' },
]

function AppContent() {
  const { view, isKidMode, goToClass, selectedClass } = useSchool()
  const [showAchievements, setShowAchievements] = useState(false)
  const [showDailyBonus, setShowDailyBonus] = useState(false)
  const [showQuickQuiz, setShowQuickQuiz] = useState(false)
  const [showCalendar, setShowCalendar] = useState(false)
  const [showLearningPath, setShowLearningPath] = useState(false)
  const [activeMiniGame, setActiveMiniGame] = useState<MiniGameType>(null)

  useEffect(() => {
    const lastVisit = localStorage.getItem('lastVisitDate'), today = getTodayString()
    if (lastVisit !== today) { const timer = setTimeout(() => setShowDailyBonus(true), 500); localStorage.setItem('lastVisitDate', today); return () => clearTimeout(timer) }
  }, [])

  const gameComponents: Record<Exclude<MiniGameType, null>, React.ReactNode> = {
    flashcards: <FlashCards />, speedtest: <SpeedTest />, typing: <TypingPractice />, spelling: <SpellingGame />, puzzle: <NumberPuzzle />, scramble: <WordScramble />, racing: <MathRacing />, trivia: <TriviaBattle />, crossword: <CrosswordGame />, sentence: <SentenceBuilder />, colormatch: <ColorMatch />, wordsearch: <WordSearch />, sequence: <SequenceGame />, emoji: <EmojiQuiz />, geography: <GeographyQuiz />, hangman: <HangmanGame />, truefalse: <TrueOrFalse />, anagram: <AnagramGame />, oddoneout: <OddOneOut />, soundquiz: <SoundQuiz />, mathpuzzle: <MathPuzzle />, wordchain: <WordChain />, quickmath: <QuickMath />, multiply: <MultiplicationTable />, divide: <DivisionTable />, alphabetsort: <AlphabetSort />, synonym: <SynonymAntonym />, antonyms: <Antonyms />, homonyms: <Homonyms />, flags: <FlagsQuiz />, timequiz: <TimeQuiz />, riddles: <Riddles />, proverbs: <Proverbs />, punctuation: <PunctuationQuiz />, capitals: <CapitalCities />, roman: <RomanNumerals />, fraction: <FractionCompare />, percent: <PercentQuiz />, geometry: <GeometryQuiz />, nature: <NatureQuiz />, history: <HistoryQuiz />, science: <ScienceQuiz />, measurement: <MeasurementQuiz />, equation: <EquationSolver />, parts: <PartsOfSpeech />, wordform: <WordFormation />, syllables: <Syllables />, stress: <StressMark />, cases: <WordCases />, conjugations: <Conjugations />, compare: <CompareNumbers />, abbr: <Abbreviations />, prime: <PrimeNumbers />, vowels: <VowelsConsonants />, zhishi: <ZhiShi />, days: <DaysOfWeek />, evenodd: <EvenOdd />, shapes: <ShapesQuiz />, simplemath: <SimpleMath />, counting: <CountingGame />, challenge: <ChallengeMode />, memory: <MemoryGame />, daily: <DailyChallenge />, stats: <StatsDashboard />
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 p-4 md:p-8 relative overflow-hidden">
      <AnimatedBackground />
      <div className="max-w-7xl mx-auto relative z-10">
        <header className="text-center mb-6">
          <button onClick={() => goToClass(0)} className="hover:scale-105 transition-transform">
            <h1 className="text-4xl md:text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-2">ИНЕТШКОЛА</h1>
          </button>
          <p className="text-xl text-purple-200">Интерактивная школьная программа</p>
          <div className="flex justify-center gap-2 mt-3 flex-wrap">
            <span className="text-green-400 text-xs bg-green-400/20 px-3 py-1 rounded-full">v2.56</span>
            <button onClick={() => setShowQuickQuiz(!showQuickQuiz)} className={`text-xs px-3 py-1 rounded-full transition-colors ${showQuickQuiz ? 'bg-cyan-400/30 text-cyan-300' : 'bg-cyan-400/20 text-cyan-400 hover:bg-cyan-400/30'}`}><Gamepad2 className="w-3 h-3 inline mr-1" />Тест</button>
            <button onClick={() => setShowCalendar(!showCalendar)} className={`text-xs px-3 py-1 rounded-full transition-colors ${showCalendar ? 'bg-orange-400/30 text-orange-300' : 'bg-orange-400/20 text-orange-400 hover:bg-orange-400/30'}`}><Calendar className="w-3 h-3 inline mr-1" />Календарь</button>
            {selectedClass !== null && <button onClick={() => setShowLearningPath(!showLearningPath)} className={`text-xs px-3 py-1 rounded-full transition-colors ${showLearningPath ? 'bg-violet-400/30 text-violet-300' : 'bg-violet-400/20 text-violet-400 hover:bg-violet-400/30'}`}><Map className="w-3 h-3 inline mr-1" />Путь</button>}
            <button onClick={() => setShowAchievements(!showAchievements)} className="text-yellow-400 text-xs bg-yellow-400/20 px-3 py-1 rounded-full hover:bg-yellow-400/30">🏆 Достижения</button>
            <ThemeSelector /><SoundToggle />
          </div>
          {view === 'classes' && (
            <div className="flex justify-center gap-2 mt-2 flex-wrap">
              {GAME_BUTTONS.map((game) => (
                <button key={game.id} onClick={() => setActiveMiniGame(activeMiniGame === game.id ? null : game.id)} className={`text-xs px-3 py-1 rounded-full transition-colors bg-${game.color}-400/20 text-${game.color}-400 hover:bg-${game.color}-400/30 ${activeMiniGame === game.id ? `bg-${game.color}-400/30 text-${game.color}-300` : ''}`}>{game.icon}{game.label}</button>
              ))}
            </div>
          )}
        </header>

        {showQuickQuiz && view === 'classes' && !activeMiniGame && <div className="mb-8 animate-slideIn"><ExtendedQuickQuiz /></div>}
        {showCalendar && view === 'classes' && !activeMiniGame && <div className="mb-8 animate-slideIn"><StreakCalendar /></div>}
        {activeMiniGame && <div className="mb-8 animate-slideIn">{gameComponents[activeMiniGame]}</div>}
        {showLearningPath && view === 'subjects' && <div className="mb-8 animate-slideIn"><LearningPath /></div>}
        {selectedClass && <LevelProgress />}
        {showAchievements && <div className="mb-8 animate-slideIn"><AchievementsDisplay /></div>}

        <main>
          {view === 'classes' && (isKidMode ? <KidGradeSelector /> : <GradeSelector />)}
          {view === 'subjects' && (isKidMode ? <KidSubjectGrid /> : <SubjectGrid />)}
          {view === 'lessons' && (isKidMode ? <KidLessonViewer /> : <LessonViewer />)}
          {view === 'games' && (isKidMode ? <KidGameSection /> : <GameSection />)}
          {view === 'gameplay' && <Gameplay />}
        </main>
      </div>
      {showDailyBonus && <DailyBonus onClose={() => setShowDailyBonus(false)} />}
    </div>
  )
}
export default function Home() { return <SchoolProvider><AppContent /></SchoolProvider> }
