'use client'

import { SchoolProvider, useSchool } from '@/context/SchoolContext'
import { ErrorBoundary, GradeSelector, SubjectGrid, LessonViewer, KidSubjectGrid, KidLessonViewer, GameSection, Gameplay, KidGameSection, KidGameplay, AchievementsDisplay, AnimatedBackground, KidGradeSelector, LevelProgress, DailyBonus, StreakCalendar, SoundToggle, ThemeSelector, ExtendedQuickQuiz, LearningPath, ChallengeMode, MemoryGame, DailyChallenge, FlashCards, SpeedTest, StatsDashboard, TypingPractice, SpellingGame, NumberPuzzle, WordScramble, MathRacing, TriviaBattle, CrosswordGame, SentenceBuilder, ColorMatch, WordSearch, SequenceGame, EmojiQuiz, GeographyQuiz, HangmanGame, TrueOrFalse, AnagramGame, OddOneOut, SoundQuiz, MathPuzzle, WordChain, QuickMath, AlphabetSort, SynonymAntonym, FlagsQuiz, TimeQuiz, Riddles, Proverbs, PunctuationQuiz, CapitalCities, RomanNumerals, FractionCompare, PercentQuiz, GeometryQuiz, NatureQuiz, HistoryQuiz, ScienceQuiz, MeasurementQuiz, EquationSolver, PartsOfSpeech, WordFormation, Syllables, StressMark, MultiplicationTable, Antonyms, WordCases, DivisionTable, Homonyms, Conjugations, CompareNumbers, Abbreviations, PrimeNumbers, VowelsConsonants, ZhiShi, DaysOfWeek, EvenOdd, ShapesQuiz, SimpleMath, CountingGame, AnimalsGame, ProfessionsGame, PeriodicTableGame, PhysicsFormulas, ChemistryQuiz, BiologyQuiz, AstronomyQuiz, LogicPuzzles, WordProblems, ReadingComprehension, FloatingGameMenu, VerbTenseGame, WordBuilder } from '@/components/school'
import { useState, useEffect } from 'react'
import { Calendar, Gamepad2, Map, Trophy, Settings, X, Heart, Copy, Check } from 'lucide-react'

function getTodayString(): string { return new Date().toISOString().split('T')[0] }
type MiniGameType = 'challenge' | 'memory' | 'daily' | 'flashcards' | 'speedtest' | 'stats' | 'typing' | 'spelling' | 'puzzle' | 'scramble' | 'racing' | 'trivia' | 'crossword' | 'sentence' | 'colormatch' | 'wordsearch' | 'sequence' | 'emoji' | 'geography' | 'hangman' | 'truefalse' | 'anagram' | 'oddoneout' | 'soundquiz' | 'mathpuzzle' | 'wordchain' | 'quickmath' | 'multiply' | 'divide' | 'alphabetsort' | 'synonym' | 'antonyms' | 'homonyms' | 'flags' | 'timequiz' | 'riddles' | 'proverbs' | 'punctuation' | 'capitals' | 'roman' | 'fraction' | 'percent' | 'geometry' | 'nature' | 'history' | 'science' | 'measurement' | 'equation' | 'parts' | 'wordform' | 'syllables' | 'stress' | 'cases' | 'conjugations' | 'compare' | 'abbr' | 'prime' | 'vowels' | 'zhishi' | 'days' | 'evenodd' | 'shapes' | 'simplemath' | 'counting' | 'animals' | 'professions' | 'periodic' | 'physics' | 'chemistry' | 'biology' | 'astronomy' | 'logic' | 'wordprob' | 'reading' | 'verbtense' | 'wordbuilder' | null

function AppContent() {
  const { view, isKidMode, goToClass, selectedClass } = useSchool()
  const [showAchievements, setShowAchievements] = useState(false)
  const [showDailyBonus, setShowDailyBonus] = useState(false)
  const [showQuickQuiz, setShowQuickQuiz] = useState(false)
  const [showCalendar, setShowCalendar] = useState(false)
  const [showLearningPath, setShowLearningPath] = useState(false)
  const [activeMiniGame, setActiveMiniGame] = useState<MiniGameType>(null)
  const [showSettings, setShowSettings] = useState(false)
  const [showDonate, setShowDonate] = useState(false)
  const [copied, setCopied] = useState(false)

  useEffect(() => {
    const lastVisit = localStorage.getItem('lastVisitDate'), today = getTodayString()
    if (lastVisit !== today) { const timer = setTimeout(() => setShowDailyBonus(true), 500); localStorage.setItem('lastVisitDate', today); return () => clearTimeout(timer) }
  }, [])

  const gameComponents: Record<Exclude<MiniGameType, null>, React.ReactNode> = {
    flashcards: <FlashCards />, speedtest: <SpeedTest />, typing: <TypingPractice />, spelling: <SpellingGame />, puzzle: <NumberPuzzle />, scramble: <WordScramble />, racing: <MathRacing />, trivia: <TriviaBattle />, crossword: <CrosswordGame />, sentence: <SentenceBuilder />, colormatch: <ColorMatch />, wordsearch: <WordSearch />, sequence: <SequenceGame />, emoji: <EmojiQuiz />, geography: <GeographyQuiz />, hangman: <HangmanGame />, truefalse: <TrueOrFalse />, anagram: <AnagramGame />, oddoneout: <OddOneOut />, soundquiz: <SoundQuiz />, mathpuzzle: <MathPuzzle />, wordchain: <WordChain />, quickmath: <QuickMath />, multiply: <MultiplicationTable />, divide: <DivisionTable />, alphabetsort: <AlphabetSort />, synonym: <SynonymAntonym />, antonyms: <Antonyms />, homonyms: <Homonyms />, flags: <FlagsQuiz />, timequiz: <TimeQuiz />, riddles: <Riddles />, proverbs: <Proverbs />, punctuation: <PunctuationQuiz />, capitals: <CapitalCities />, roman: <RomanNumerals />, fraction: <FractionCompare />, percent: <PercentQuiz />, geometry: <GeometryQuiz />, nature: <NatureQuiz />, history: <HistoryQuiz />, science: <ScienceQuiz />, measurement: <MeasurementQuiz />, equation: <EquationSolver />, parts: <PartsOfSpeech />, wordform: <WordFormation />, syllables: <Syllables />, stress: <StressMark />, cases: <WordCases />, conjugations: <Conjugations />, compare: <CompareNumbers />, abbr: <Abbreviations />, prime: <PrimeNumbers />, vowels: <VowelsConsonants />, zhishi: <ZhiShi />, days: <DaysOfWeek />, evenodd: <EvenOdd />, shapes: <ShapesQuiz />, simplemath: <SimpleMath />, counting: <CountingGame />, animals: <AnimalsGame />, professions: <ProfessionsGame />, periodic: <PeriodicTableGame />, physics: <PhysicsFormulas />, chemistry: <ChemistryQuiz />, biology: <BiologyQuiz />, astronomy: <AstronomyQuiz />, logic: <LogicPuzzles />, wordprob: <WordProblems />, reading: <ReadingComprehension />, challenge: <ChallengeMode />, memory: <MemoryGame />, daily: <DailyChallenge />, stats: <StatsDashboard />, verbtense: <VerbTenseGame />, wordbuilder: <WordBuilder />
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 p-4 md:p-8 relative overflow-hidden" suppressHydrationWarning>
      <AnimatedBackground />
      
      {/* Floating game menu */}
      {view === 'classes' && (
        <FloatingGameMenu 
          activeGame={activeMiniGame} 
          onSelectGame={(id) => setActiveMiniGame(id as MiniGameType)} 
        />
      )}

      <div className="max-w-7xl mx-auto relative z-10">
        {/* Compact header */}
        <header className="text-center mb-6">
          <button onClick={() => goToClass(0)} className="hover:scale-105 transition-transform">
            <h1 className="text-4xl md:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-pink-300 to-purple-300 mb-1">ИНЕТШКОЛА</h1>
          </button>
          <p className="text-lg text-purple-200">Интерактивная школьная программа</p>
          
          {/* Compact button row */}
          <div className="flex justify-center items-center gap-2 mt-3 flex-wrap">
            <span className="text-green-400 text-xs bg-green-400/20 px-2 py-1 rounded-full">v3.9</span>
            
            <button onClick={() => setShowCalendar(!showCalendar)} 
                    className={`text-xs px-2 py-1 rounded-full transition-colors flex items-center gap-1
                               ${showCalendar ? 'bg-orange-400/30 text-orange-300' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}>
              <Calendar className="w-3 h-3" />
            </button>
            
            <button onClick={() => setShowAchievements(!showAchievements)} 
                    className={`text-xs px-2 py-1 rounded-full transition-colors flex items-center gap-1
                               ${showAchievements ? 'bg-yellow-400/30 text-yellow-300' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}>
              <Trophy className="w-3 h-3" />
            </button>
            
            {selectedClass !== null && (
              <button onClick={() => setShowLearningPath(!showLearningPath)} 
                      className={`text-xs px-2 py-1 rounded-full transition-colors flex items-center gap-1
                                 ${showLearningPath ? 'bg-violet-400/30 text-violet-300' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}>
                <Map className="w-3 h-3" />
              </button>
            )}
            
            <button onClick={() => setShowSettings(!showSettings)} 
                    className={`text-xs px-2 py-1 rounded-full transition-colors flex items-center gap-1
                               ${showSettings ? 'bg-purple-400/30 text-purple-300' : 'bg-white/10 text-white/70 hover:bg-white/20'}`}>
              <Settings className="w-3 h-3" />
            </button>
            
            <button onClick={() => setShowDonate(true)} 
                    className="text-xs px-2 py-1 rounded-full transition-colors flex items-center gap-1 bg-gradient-to-r from-pink-500/30 to-red-500/30 text-pink-300 hover:from-pink-500/40 hover:to-red-500/40">
              <Heart className="w-3 h-3" />
            </button>
          </div>

          {/* Settings dropdown */}
          {showSettings && (
            <div className="mt-3 flex justify-center gap-2 p-2 bg-white/5 rounded-xl">
              <ThemeSelector />
              <SoundToggle />
              <button onClick={() => setShowQuickQuiz(!showQuickQuiz)} 
                      className="text-xs px-3 py-1 rounded-full bg-cyan-400/20 text-cyan-400 hover:bg-cyan-400/30">
                <Gamepad2 className="w-3 h-3 inline mr-1" />Тест
              </button>
            </div>
          )}
        </header>

        {/* Modal overlays */}
        {showCalendar && view === 'classes' && !activeMiniGame && (
          <div className="mb-6 animate-slideIn relative">
            <button onClick={() => setShowCalendar(false)} className="absolute -top-2 -right-2 z-10 w-6 h-6 bg-red-500 hover:bg-red-600 rounded-full flex items-center justify-center text-white text-sm">✕</button>
            <StreakCalendar />
          </div>
        )}
        
        {activeMiniGame && (
          <div className="mb-6 animate-slideIn relative">
            <button onClick={() => setActiveMiniGame(null)} className="absolute -top-2 -right-2 z-10 w-8 h-8 bg-red-500 hover:bg-red-600 rounded-full flex items-center justify-center text-white font-bold shadow-lg">✕</button>
            {gameComponents[activeMiniGame]}
          </div>
        )}
        
        {showLearningPath && view === 'subjects' && (
          <div className="mb-6 animate-slideIn relative">
            <button onClick={() => setShowLearningPath(false)} className="absolute -top-2 -right-2 z-10 w-6 h-6 bg-red-500 hover:bg-red-600 rounded-full flex items-center justify-center text-white text-sm">✕</button>
            <LearningPath />
          </div>
        )}
        
        {selectedClass && <LevelProgress />}
        
        {showAchievements && (
          <div className="mb-6 animate-slideIn relative">
            <button onClick={() => setShowAchievements(false)} className="absolute -top-2 -right-2 z-10 w-6 h-6 bg-red-500 hover:bg-red-600 rounded-full flex items-center justify-center text-white text-sm">✕</button>
            <AchievementsDisplay />
          </div>
        )}

        <main>
          {view === 'classes' && (isKidMode ? <KidGradeSelector /> : <GradeSelector />)}
          {view === 'subjects' && (isKidMode ? <KidSubjectGrid /> : <SubjectGrid />)}
          {view === 'lessons' && (isKidMode ? <KidLessonViewer /> : <LessonViewer />)}
          {view === 'games' && (isKidMode ? <KidGameSection /> : <GameSection />)}
          {view === 'gameplay' && (isKidMode ? <KidGameplay /> : <Gameplay />)}
        </main>
      </div>
      {showDailyBonus && <DailyBonus onClose={() => setShowDailyBonus(false)} />}
      
      {/* Donate Modal */}
      {showDonate && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4" onClick={() => setShowDonate(false)}>
          <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-6 max-w-sm w-full shadow-2xl border border-white/10" onClick={e => e.stopPropagation()}>
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-xl font-bold text-white flex items-center gap-2">
                <Heart className="w-5 h-5 text-pink-400 fill-pink-400" />
                Поддержать проект
              </h2>
              <button onClick={() => setShowDonate(false)} className="text-white/50 hover:text-white">
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <div className="bg-white/5 rounded-xl p-4 mb-4">
              <p className="text-purple-200 text-sm mb-3">
                ИНЕТШКОЛА — бесплатный образовательный проект. Ваша поддержка поможет развивать платформу, добавлять новый контент и улучшать функциональность.
              </p>
              <div className="text-xs text-white/50">
                • Разработка новых уроков и игр<br/>
                • Улучшение интерфейса<br/>
                • Оплата хостинга и домена
              </div>
            </div>
            
            <div className="bg-gradient-to-r from-pink-500/20 to-purple-500/20 rounded-xl p-4 border border-pink-500/30">
              <div className="text-xs text-white/50 mb-1">Перевод на номер телефона:</div>
              <div className="flex items-center justify-between bg-black/30 rounded-lg px-3 py-2">
                <span className="text-lg font-mono text-white font-bold">+7 909 132-72-32</span>
                <button 
                  onClick={() => {
                    navigator.clipboard.writeText('+79091327232')
                    setCopied(true)
                    setTimeout(() => setCopied(false), 2000)
                  }}
                  className="p-2 hover:bg-white/10 rounded-lg transition-colors"
                  title="Скопировать"
                >
                  {copied ? (
                    <Check className="w-5 h-5 text-green-400" />
                  ) : (
                    <Copy className="w-5 h-5 text-white/50 hover:text-white" />
                  )}
                </button>
              </div>
              <div className="text-xs text-white/40 mt-2 text-center">
                Любая сумма важна для развития проекта!
              </div>
            </div>
            
            <div className="mt-4 text-center text-xs text-white/30">
              Спасибо за вашу поддержку! 💜
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
export default function Home() { return <SchoolProvider><AppContent /></SchoolProvider> }
