'use client'

import { SchoolProvider, useSchool } from '@/context/SchoolContext'
import { ErrorBoundary, GradeSelector, SubjectGrid, LessonViewer, KidSubjectGrid, KidLessonViewer, GameSection, Gameplay, KidGameSection, KidGameplay, AchievementsDisplay, AnimatedBackground, KidGradeSelector, LevelProgress, DailyBonus, StreakCalendar, SoundToggle, ThemeSelector, ExtendedQuickQuiz, LearningPath, ChallengeMode, MemoryGame, DailyChallenge, FlashCards, SpeedTest, StatsDashboard, TypingPractice, SpellingGame, NumberPuzzle, WordScramble, MathRacing, TriviaBattle, CrosswordGame, SentenceBuilder, ColorMatch, WordSearch, SequenceGame, EmojiQuiz, GeographyQuiz, HangmanGame, TrueOrFalse, AnagramGame, OddOneOut, SoundQuiz, MathPuzzle, WordChain, QuickMath, AlphabetSort, SynonymAntonym, FlagsQuiz, TimeQuiz, Riddles, Proverbs, PunctuationQuiz, CapitalCities, RomanNumerals, FractionCompare, PercentQuiz, GeometryQuiz, NatureQuiz, HistoryQuiz, ScienceQuiz, MeasurementQuiz, EquationSolver, PartsOfSpeech, WordFormation, Syllables, StressMark, MultiplicationTable, Antonyms, WordCases, DivisionTable, Homonyms, Conjugations, CompareNumbers, Abbreviations, PrimeNumbers, VowelsConsonants, ZhiShi, DaysOfWeek, EvenOdd, ShapesQuiz, SimpleMath, CountingGame, AnimalsGame, ProfessionsGame, PeriodicTableGame, PhysicsFormulas, ChemistryQuiz, BiologyQuiz, AstronomyQuiz, LogicPuzzles, WordProblems, ReadingComprehension, FloatingGameMenu, VerbTenseGame, WordBuilder } from '@/components/school'
import { useState, useEffect } from 'react'
import { Calendar, Gamepad2, Map, Trophy, Settings, X, Heart, ExternalLink, Smartphone } from 'lucide-react'
import { QRCodeSVG } from 'qrcode.react'

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
            <span className="text-green-400 text-xs bg-green-400/20 px-2 py-1 rounded-full">v3.10</span>
            
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
        <div className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4" onClick={() => setShowDonate(false)}>
          <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-6 max-w-md w-full shadow-2xl border border-white/10" onClick={e => e.stopPropagation()}>
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-xl font-bold text-white flex items-center gap-2">
                <Heart className="w-5 h-5 text-pink-400 fill-pink-400" />
                Поддержать проект
              </h2>
              <button onClick={() => setShowDonate(false)} className="text-white/50 hover:text-white transition-colors">
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <p className="text-purple-200 text-sm mb-4">
              ИНЕТШКОЛА — бесплатный образовательный проект. Любая поддержка поможет развивать платформу!
            </p>
            
            {/* QR Code Section */}
            <div className="flex flex-col items-center mb-4">
              <div className="bg-white rounded-xl p-3 shadow-lg">
                <QRCodeSVG 
                  value="00020101021230800016com.nspk.ru0111790913272325204549953036435405802RU6007Moscow6304A1F8"
                  size={180}
                  level="M"
                  bgColor="#ffffff"
                  fgColor="#1e1b4b"
                />
              </div>
              <p className="text-xs text-white/60 mt-2 flex items-center gap-1">
                <Smartphone className="w-3 h-3" />
                Отсканируйте в приложении банка
              </p>
            </div>
            
            {/* Quick Payment Buttons */}
            <div className="space-y-2 mb-4">
              <p className="text-xs text-white/50 text-center mb-2">Быстрый перевод через:</p>
              <div className="grid grid-cols-3 gap-2">
                <a 
                  href="https://www.sberbank.ru/ru/transfer/phone"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex flex-col items-center gap-1 p-2 bg-green-500/20 hover:bg-green-500/30 rounded-xl transition-colors"
                >
                  <div className="w-8 h-8 bg-green-500 rounded-lg flex items-center justify-center text-white font-bold text-xs">С</div>
                  <span className="text-xs text-green-300">Сбер</span>
                </a>
                <a 
                  href="https://www.tinkoff.ru/transfer/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex flex-col items-center gap-1 p-2 bg-yellow-500/20 hover:bg-yellow-500/30 rounded-xl transition-colors"
                >
                  <div className="w-8 h-8 bg-yellow-500 rounded-lg flex items-center justify-center text-white font-bold text-xs">Т</div>
                  <span className="text-xs text-yellow-300">Тинькофф</span>
                </a>
                <a 
                  href="https://www.raiffeisen.ru/retail/p2r/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex flex-col items-center gap-1 p-2 bg-yellow-400/20 hover:bg-yellow-400/30 rounded-xl transition-colors"
                >
                  <div className="w-8 h-8 bg-yellow-400 rounded-lg flex items-center justify-center text-black font-bold text-xs">Р</div>
                  <span className="text-xs text-yellow-200">Райф</span>
                </a>
              </div>
            </div>
            
            {/* Info */}
            <div className="bg-white/5 rounded-lg p-3 text-xs text-white/50 space-y-1">
              <div className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 bg-pink-400 rounded-full"></div>
                <span>Разработка новых уроков и игр</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 bg-purple-400 rounded-full"></div>
                <span>Улучшение интерфейса</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 bg-blue-400 rounded-full"></div>
                <span>Оплата хостинга</span>
              </div>
            </div>
            
            <div className="mt-4 text-center text-xs text-pink-300/70">
              Спасибо за вашу поддержку! 💜
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
export default function Home() { return <SchoolProvider><AppContent /></SchoolProvider> }
