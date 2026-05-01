'use client'

import { useState, useMemo, useRef, Suspense, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { X, Atom, FlaskConical, Zap, Globe, Clock, User, MapPin, Lightbulb, Sparkles, Gamepad2 } from 'lucide-react'
import { Canvas, useFrame, useThree } from '@react-three/fiber'
import { OrbitControls, Sphere, Html, Float } from '@react-three/drei'
import * as THREE from 'three'

// Цвета категорий (объявлено до использования в AtomVisualization)
const categoryColors: Record<string, string> = {
  'alkali-metal': 'bg-red-500',
  'alkaline-earth': 'bg-orange-500',
  'transition-metal': 'bg-yellow-500',
  'post-transition': 'bg-green-500',
  'metalloid': 'bg-teal-500',
  'nonmetal': 'bg-blue-500',
  'halogen': 'bg-indigo-500',
  'noble-gas': 'bg-purple-500',
  'lanthanide': 'bg-pink-500',
  'actinide': 'bg-rose-600'
}

// Цвета для Three.js (hex формат)
const categoryHexColors: Record<string, string> = {
  'alkali-metal': '#ef4444',
  'alkaline-earth': '#f97316',
  'transition-metal': '#eab308',
  'post-transition': '#22c55e',
  'metalloid': '#14b8a6',
  'nonmetal': '#3b82f6',
  'halogen': '#6366f1',
  'noble-gas': '#a855f7',
  'lanthanide': '#ec4899',
  'actinide': '#f43f5e'
}

const categoryNames: Record<string, string> = {
  'alkali-metal': 'Щёлочные металлы',
  'alkaline-earth': 'Щёлочноземельные металлы',
  'transition-metal': 'Переходные металлы',
  'post-transition': 'Постпереходные металлы',
  'metalloid': 'Металлоиды',
  'nonmetal': 'Неметаллы',
  'halogen': 'Галогены',
  'noble-gas': 'Благородные газы',
  'lanthanide': 'Лантаноиды',
  'actinide': 'Актиноиды'
}

// Цвета оболочек для электронов
const shellHexColors = [
  '#f87171', // красный
  '#fb923c', // оранжевый
  '#facc15', // жёлтый
  '#4ade80', // зелёный
  '#22d3ee', // голубой
  '#60a5fa', // синий
  '#c084fc'  // фиолетовый
]

// Функция для расчёта электронной конфигурации
function getElectronConfiguration(atomicNumber: number): number[] {
  const maxElectronsPerShell = [2, 8, 18, 32, 32, 18, 8]
  const shells: number[] = []
  let remaining = atomicNumber
  
  for (let i = 0; i < maxElectronsPerShell.length && remaining > 0; i++) {
    const electronsInShell = Math.min(remaining, maxElectronsPerShell[i])
    shells.push(electronsInShell)
    remaining -= electronsInShell
  }
  
  return shells
}

// 3D ядро атома с настоящими сферами
function Nucleus({ atomicNumber, color, symbol }: { atomicNumber: number; color: string; symbol: string }) {
  const groupRef = useRef<THREE.Group>(null)
  
  // Количество протонов и нейтронов для визуализации
  const nucleonCount = Math.min(Math.ceil(atomicNumber / 2), 20)
  
  useFrame((state) => {
    if (groupRef.current) {
      groupRef.current.rotation.y = state.clock.elapsedTime * 0.3
      groupRef.current.rotation.x = Math.sin(state.clock.elapsedTime * 0.2) * 0.1
    }
  })

  return (
    <group ref={groupRef}>
      {/* Основное ядро - светящаяся сфера */}
      <Sphere args={[0.5, 32, 32]}>
        <meshStandardMaterial
          color={color}
          emissive={color}
          emissiveIntensity={0.5}
          metalness={0.3}
          roughness={0.4}
        />
      </Sphere>
      
      {/* Внутренняя светящаяся сфера */}
      <Sphere args={[0.52, 32, 32]}>
        <meshBasicMaterial
          color={color}
          transparent
          opacity={0.3}
        />
      </Sphere>
      
      {/* Протоны и нейтроны внутри ядра */}
      {Array.from({ length: nucleonCount }).map((_, i) => {
        const phi = Math.acos(-1 + (2 * i) / nucleonCount)
        const theta = Math.sqrt(nucleonCount * Math.PI) * phi
        const radius = 0.25 + Math.random() * 0.15
        
        return (
          <mesh
            key={i}
            position={[
              radius * Math.sin(phi) * Math.cos(theta),
              radius * Math.sin(phi) * Math.sin(theta),
              radius * Math.cos(phi)
            ]}
          >
            <sphereGeometry args={[0.06, 16, 16]} />
            <meshStandardMaterial
              color={i % 2 === 0 ? '#ff6b6b' : '#4dabf7'}
              emissive={i % 2 === 0 ? '#ff6b6b' : '#4dabf7'}
              emissiveIntensity={0.3}
            />
          </mesh>
        )
      })}
      
      {/* Символ элемента */}
      <Html center>
        <div className="text-white font-black text-2xl pointer-events-none select-none"
             style={{ textShadow: '0 0 10px rgba(255,255,255,0.5)' }}>
          {symbol}
        </div>
      </Html>
    </group>
  )
}

// 3D электрон на орбите
function Electron({ position, color, orbitRadius, speed, orbitTilt }: { 
  position: [number, number, number]
  color: string
  orbitRadius: number
  speed: number
  orbitTilt: [number, number, number]
}) {
  const meshRef = useRef<THREE.Mesh>(null)
  const groupRef = useRef<THREE.Group>(null)
  
  useFrame((state) => {
    if (meshRef.current && groupRef.current) {
      const time = state.clock.elapsedTime * speed
      meshRef.current.position.x = Math.cos(time) * orbitRadius
      meshRef.current.position.z = Math.sin(time) * orbitRadius
    }
  })

  return (
    <group ref={groupRef} rotation={orbitTilt}>
      {/* Орбитальное кольцо */}
      <mesh rotation={[Math.PI / 2, 0, 0]}>
        <ringGeometry args={[orbitRadius - 0.01, orbitRadius + 0.01, 64]} />
        <meshBasicMaterial color="#ffffff" transparent opacity={0.15} />
      </mesh>
      
      {/* Электрон - светящаяся сфера */}
      <mesh ref={meshRef}>
        <sphereGeometry args={[0.08, 16, 16]} />
        <meshStandardMaterial
          color={color}
          emissive={color}
          emissiveIntensity={0.8}
          metalness={0.5}
          roughness={0.2}
        />
      </mesh>
      
      {/* Свечение электрона */}
      <mesh ref={meshRef}>
        <sphereGeometry args={[0.12, 16, 16]} />
        <meshBasicMaterial
          color={color}
          transparent
          opacity={0.3}
        />
      </mesh>
    </group>
  )
}

// Электронная оболочка
function ElectronShell({ electronCount, shellIndex, baseRadius }: { 
  electronCount: number
  shellIndex: number
  baseRadius: number 
}) {
  const radius = baseRadius + shellIndex * 0.4
  const color = shellHexColors[shellIndex % shellHexColors.length]
  const speed = 1.5 - shellIndex * 0.15
  const tiltX = (shellIndex * 30) * (Math.PI / 180)
  const tiltY = (shellIndex * 45) * (Math.PI / 180)
  const tiltZ = (shellIndex * 15) * (Math.PI / 180)
  
  return (
    <group rotation={[tiltX, tiltY, tiltZ]}>
      {/* Орбитальное кольцо */}
      <mesh rotation={[Math.PI / 2, 0, 0]}>
        <ringGeometry args={[radius - 0.008, radius + 0.008, 64]} />
        <meshBasicMaterial color="#ffffff" transparent opacity={0.2} />
      </mesh>
      
      {/* Электроны на орбите */}
      {Array.from({ length: electronCount }).map((_, i) => {
        const angle = (2 * Math.PI * i) / electronCount
        return (
          <OrbitingElectron
            key={i}
            radius={radius}
            initialAngle={angle}
            speed={speed + i * 0.05}
            color={color}
          />
        )
      })}
    </group>
  )
}

// Электрон на орбите
function OrbitingElectron({ radius, initialAngle, speed, color }: {
  radius: number
  initialAngle: number
  speed: number
  color: string
}) {
  const meshRef = useRef<THREE.Mesh>(null)
  const glowRef = useRef<THREE.Mesh>(null)
  
  useFrame((state) => {
    const angle = initialAngle + state.clock.elapsedTime * speed
    const x = Math.cos(angle) * radius
    const z = Math.sin(angle) * radius
    
    if (meshRef.current) {
      meshRef.current.position.x = x
      meshRef.current.position.z = z
    }
    if (glowRef.current) {
      glowRef.current.position.x = x
      glowRef.current.position.z = z
    }
  })

  return (
    <>
      {/* Электрон */}
      <mesh ref={meshRef}>
        <sphereGeometry args={[0.06, 16, 16]} />
        <meshStandardMaterial
          color={color}
          emissive={color}
          emissiveIntensity={0.8}
        />
      </mesh>
      {/* Свечение */}
      <mesh ref={glowRef}>
        <sphereGeometry args={[0.1, 16, 16]} />
        <meshBasicMaterial
          color={color}
          transparent
          opacity={0.3}
        />
      </mesh>
    </>
  )
}

// Полная 3D сцена атома
function AtomScene({ atomicNumber, category, symbol }: { 
  atomicNumber: number
  category: string
  symbol: string 
}) {
  const shells = useMemo(() => getElectronConfiguration(atomicNumber), [atomicNumber])
  const color = categoryHexColors[category] || '#6b7280'
  
  return (
    <>
      {/* Освещение */}
      <ambientLight intensity={0.4} />
      <pointLight position={[10, 10, 10]} intensity={1} color="#ffffff" />
      <pointLight position={[-10, -10, -10]} intensity={0.5} color={color} />
      <pointLight position={[0, 0, 0]} intensity={2} color={color} distance={3} />
      
      {/* Ядро */}
      <Float speed={2} rotationIntensity={0.2} floatIntensity={0.3}>
        <Nucleus atomicNumber={atomicNumber} color={color} symbol={symbol} />
      </Float>
      
      {/* Электронные оболочки */}
      {shells.map((electronCount, shellIndex) => (
        <ElectronShell
          key={shellIndex}
          electronCount={electronCount}
          shellIndex={shellIndex}
          baseRadius={0.8}
        />
      ))}
      
      {/* Управление камерой */}
      <OrbitControls 
        enablePan={false}
        enableZoom={true}
        minDistance={2}
        maxDistance={8}
        autoRotate
        autoRotateSpeed={1}
      />
    </>
  )
}

// 3D визуализация атома с Canvas
function AtomVisualization({ atomicNumber, category, symbol }: { 
  atomicNumber: number
  category: string
  symbol: string 
}) {
  return (
    <div className="w-full h-32 sm:h-40 md:h-48 mx-auto">
      <Canvas
        camera={{ position: [0, 0, 4], fov: 50 }}
        gl={{ antialias: true, alpha: true }}
        style={{ background: 'transparent' }}
      >
        <Suspense fallback={null}>
          <AtomScene 
            atomicNumber={atomicNumber} 
            category={category} 
            symbol={symbol} 
          />
        </Suspense>
      </Canvas>
    </div>
  )
}

// Отображение электронной конфигурации
function ElectronConfigDisplay({ atomicNumber }: { atomicNumber: number }) {
  const shells = useMemo(() => getElectronConfiguration(atomicNumber), [atomicNumber])
  const shellNames = ['K', 'L', 'M', 'N', 'O', 'P', 'Q']
  const shellColors = [
    'from-red-400 to-red-600',
    'from-orange-400 to-orange-600', 
    'from-yellow-400 to-yellow-600',
    'from-green-400 to-green-600',
    'from-cyan-400 to-cyan-600',
    'from-blue-400 to-blue-600',
    'from-purple-400 to-purple-600'
  ]
  
  return (
    <div className="bg-black/30 rounded-lg p-2 sm:p-3 backdrop-blur-sm border border-white/10">
      <div className="text-[10px] sm:text-xs text-white/60 mb-1.5 text-center font-medium">Электроны по оболочкам</div>
      <div className="space-y-1.5">
        {shells.map((count, idx) => (
          <div key={idx} className="flex items-center gap-2">
            <div className={`w-5 h-5 sm:w-6 sm:h-6 rounded-full bg-gradient-to-br ${shellColors[idx]} flex items-center justify-center text-white text-[10px] sm:text-xs font-bold shadow-lg flex-shrink-0`}>
              {shellNames[idx]}
            </div>
            <div className="flex-1 flex items-center gap-0.5 flex-wrap">
              {Array.from({ length: count }).map((_, i) => (
                <motion.div
                  key={i}
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ delay: idx * 0.05 + i * 0.02, duration: 0.2 }}
                  className={`w-2 h-2 sm:w-2.5 sm:h-2.5 rounded-full bg-gradient-to-br ${shellColors[idx]} shadow-sm`}
                />
              ))}
            </div>
            <div className="text-white font-bold text-xs sm:text-sm w-5 sm:w-6 text-right flex-shrink-0">{count}</div>
          </div>
        ))}
      </div>
      <div className="mt-1.5 pt-1.5 border-t border-white/10 text-center">
        <span className="text-white/80 text-[10px] sm:text-xs">Всего: </span>
        <span className="text-white font-bold text-xs sm:text-sm">{atomicNumber}</span>
        <span className="text-white/60 text-[10px] sm:text-xs"> e⁻</span>
      </div>
    </div>
  )
}

// Все 118 элементов с подробной информацией
const elements: {
  atomicNumber: number
  symbol: string
  name: string
  nameRu: string
  atomicMass: string
  category: string
  block: string
  period: number
  group: number
  discoveredBy?: string
  yearDiscovered?: string
  placeDiscovered?: string
  applications?: string[]
  facts?: string[]
}[] = [
  // Период 1
  {
    atomicNumber: 1, symbol: 'H', name: 'Hydrogen', nameRu: 'Водород', atomicMass: '1.008',
    category: 'nonmetal', block: 's', period: 1, group: 1,
    discoveredBy: 'Генри Кавендиш', yearDiscovered: '1766', placeDiscovered: 'Англия',
    applications: ['Топливо для ракет', 'Производство аммиака', 'Сварка металлов', 'Заполнение дирижаблей'],
    facts: ['Самый лёгкий элемент', 'Составляет 75% массы Вселенной', 'Водородная бомба - самое мощное оружие', 'Вода состоит из водорода и кислорода']
  },
  {
    atomicNumber: 2, symbol: 'He', name: 'Helium', nameRu: 'Гелий', atomicMass: '4.003',
    category: 'noble-gas', block: 's', period: 1, group: 18,
    discoveredBy: 'Пьер Жансен, Норман Локьер', yearDiscovered: '1868', placeDiscovered: 'Солнце (спектральный анализ)',
    applications: ['Заполнение воздушных шаров', 'Охлаждение магнитов МРТ', 'Глубоководное дайвинг', 'Лазеры'],
    facts: ['Второй самый лёгкий элемент', 'Открыт на Солнце раньше чем на Земле', 'Не замерзает даже при абсолютном нуле', 'Назван в честь греческого бога Солнца Гелиоса']
  },

  // Период 2
  {
    atomicNumber: 3, symbol: 'Li', name: 'Lithium', nameRu: 'Литий', atomicMass: '6.941',
    category: 'alkali-metal', block: 's', period: 2, group: 1,
    discoveredBy: 'Йохан Август Арфведсон', yearDiscovered: '1817', placeDiscovered: 'Швеция',
    applications: ['Литиевые батарейки', 'Лекарства от депрессии', 'Керамика и стекло', 'Сплавы для авиации'],
    facts: ['Легчайший металл', 'Плавает на воде', 'Используется в электромобилях Tesla', 'Назван от греческого "литос" - камень']
  },
  {
    atomicNumber: 4, symbol: 'Be', name: 'Beryllium', nameRu: 'Бериллий', atomicMass: '9.012',
    category: 'alkaline-earth', block: 's', period: 2, group: 2,
    discoveredBy: 'Луи Николя Воклен', yearDiscovered: '1798', placeDiscovered: 'Франция',
    applications: ['Аэрокосмические материалы', 'Рентгеновские окна', 'Ядерные реакторы', 'Динамики'],
    facts: ['Очень токсичен', 'В 6 раз прочнее стали', 'Прозрачен для рентгена', 'Назван по минералу бериллу']
  },
  {
    atomicNumber: 5, symbol: 'B', name: 'Boron', nameRu: 'Бор', atomicMass: '10.81',
    category: 'metalloid', block: 'p', period: 2, group: 13,
    discoveredBy: 'Жозеф Луи Гей-Люссак, Луи Жак Тенар', yearDiscovered: '1808', placeDiscovered: 'Франция',
    applications: ['Стекловолокно', 'Детекторы нейтронов', 'Удобрения', 'Борная кислота'],
    facts: ['Незаменим для растений', 'Образует самые твёрдые соединения', 'Используется в броне', 'Полупроводник']
  },
  {
    atomicNumber: 6, symbol: 'C', name: 'Carbon', nameRu: 'Углерод', atomicMass: '12.01',
    category: 'nonmetal', block: 'p', period: 2, group: 14,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Алмазы', 'Графит', 'Пластмассы', 'Топливо', 'Нанотехнологии'],
    facts: ['Основа всей жизни на Земле', 'Может образовывать нанотрубки', 'Графен - тончайший материал', '4 формы: алмаз, графит, фуллерен, карбин']
  },
  {
    atomicNumber: 7, symbol: 'N', name: 'Nitrogen', nameRu: 'Азот', atomicMass: '14.01',
    category: 'nonmetal', block: 'p', period: 2, group: 15,
    discoveredBy: 'Дэниел Резерфорд', yearDiscovered: '1772', placeDiscovered: 'Шотландия',
    applications: ['Удобрения', 'Взрывчатые вещества', 'Хранение продуктов', 'Азотные ледяные ванны'],
    facts: ['78% атмосферы Земли', 'Жидкий азот: -196°C', 'Необходим для белков', 'Назван от греческого "нитрон" - селитра']
  },
  {
    atomicNumber: 8, symbol: 'O', name: 'Oxygen', nameRu: 'Кислород', atomicMass: '16.00',
    category: 'nonmetal', block: 'p', period: 2, group: 16,
    discoveredBy: 'Карл Шееле, Джозеф Пристли', yearDiscovered: '1774', placeDiscovered: 'Швеция, Англия',
    applications: ['Дыхание', 'Медицина', 'Сварка', 'Ракетное топливо', 'Производство стали'],
    facts: ['21% атмосферы Земли', 'Без него не было бы огня', 'Открыт независимо двумя учёными', 'Жидкий кислород - голубой']
  },
  {
    atomicNumber: 9, symbol: 'F', name: 'Fluorine', nameRu: 'Фтор', atomicMass: '19.00',
    category: 'halogen', block: 'p', period: 2, group: 17,
    discoveredBy: 'Анри Муассан', yearDiscovered: '1886', placeDiscovered: 'Франция',
    applications: ['Фторопласт (тефлон)', 'Зубная паста', 'Холодильники', 'Электроника'],
    facts: ['Самый реакционноспособный элемент', 'Очень ядовит', 'Свечи на тефлоне не горят', 'Назван от латинского "флуор" - течь']
  },
  {
    atomicNumber: 10, symbol: 'Ne', name: 'Neon', nameRu: 'Неон', atomicMass: '20.18',
    category: 'noble-gas', block: 'p', period: 2, group: 18,
    discoveredBy: 'Уильям Рамзай, Моррис Траверс', yearDiscovered: '1898', placeDiscovered: 'Англия',
    applications: ['Неоновые вывески', 'Лазеры', 'Телевизионные трубки', 'Индикаторы'],
    facts: ['Даёт красно-оранжевое свечение', 'Редкий газ в атмосфере', 'Назван от греческого "неос" - новый', 'Жидкий неон - криогенный хладагент']
  },

  // Период 3
  {
    atomicNumber: 11, symbol: 'Na', name: 'Sodium', nameRu: 'Натрий', atomicMass: '22.99',
    category: 'alkali-metal', block: 's', period: 3, group: 1,
    discoveredBy: 'Гемфри Дэви', yearDiscovered: '1807', placeDiscovered: 'Англия',
    applications: ['Пищевая соль', 'Уличные фонари', 'Производство бумаги', 'Металлургия'],
    facts: ['Взрывается в воде', 'Необходим для нервов', 'Символ Na от латинского "натрий"', 'Мягкий металл, режется ножом']
  },
  {
    atomicNumber: 12, symbol: 'Mg', name: 'Magnesium', nameRu: 'Магний', atomicMass: '24.31',
    category: 'alkaline-earth', block: 's', period: 3, group: 2,
    discoveredBy: 'Джозеф Блэк', yearDiscovered: '1755', placeDiscovered: 'Шотландия',
    applications: ['Лёгкие сплавы', 'Фейерверки', 'Медицина (магнезия)', 'Автомобильные детали'],
    facts: ['Горит ослепительно ярким пламенем', 'Третий по распространённости в морской воде', 'Необходим для фотосинтеза', 'Назван по региону Магнезия в Греции']
  },
  {
    atomicNumber: 13, symbol: 'Al', name: 'Aluminium', nameRu: 'Алюминий', atomicMass: '26.98',
    category: 'post-transition', block: 'p', period: 3, group: 13,
    discoveredBy: 'Ганс Кристиан Эрстед', yearDiscovered: '1825', placeDiscovered: 'Дания',
    applications: ['Банки для напитков', 'Фольга', 'Самолёты', 'Оконные рамы', 'Электропровода'],
    facts: ['Самый распространённый металл в земной коре', 'В 19 веке был дороже золота', 'Не ржавеет', 'Легче стали в 3 раза']
  },
  {
    atomicNumber: 14, symbol: 'Si', name: 'Silicon', nameRu: 'Кремний', atomicMass: '28.09',
    category: 'metalloid', block: 'p', period: 3, group: 14,
    discoveredBy: 'Йёнс Якоб Берцелиус', yearDiscovered: '1824', placeDiscovered: 'Швеция',
    applications: ['Компьютерные чипы', 'Солнечные батареи', 'Стекло', 'Силиконовые импланты'],
    facts: ['Второй по распространённости в земной коре', 'Основа всей электроники', 'Кремниевая долина названа в честь него', 'Полупроводник']
  },
  {
    atomicNumber: 15, symbol: 'P', name: 'Phosphorus', nameRu: 'Фосфор', atomicMass: '30.97',
    category: 'nonmetal', block: 'p', period: 3, group: 15,
    discoveredBy: 'Хенниг Бранд', yearDiscovered: '1669', placeDiscovered: 'Германия',
    applications: ['Спички', 'Удобрения', 'Пищевая добавка', 'Зубные пасты'],
    facts: ['Открыт из мочи!', 'Светится в темноте', 'Назван от греческого "фосфорос" - светоносец', 'Белый фосфор очень ядовит']
  },
  {
    atomicNumber: 16, symbol: 'S', name: 'Sulfur', nameRu: 'Сера', atomicMass: '32.07',
    category: 'nonmetal', block: 'p', period: 3, group: 16,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Серная кислота', 'Резина (вулканизация)', 'Фейерверки', 'Медицина'],
    facts: ['Имеет характерный запах тухлых яиц', 'Вулканические газы содержат серу', 'Жёлтый цвет - от серы', 'Используется в виноделии']
  },
  {
    atomicNumber: 17, symbol: 'Cl', name: 'Chlorine', nameRu: 'Хлор', atomicMass: '35.45',
    category: 'halogen', block: 'p', period: 3, group: 17,
    discoveredBy: 'Карл Шееле', yearDiscovered: '1774', placeDiscovered: 'Швеция',
    applications: ['Дезинфекция воды', 'ПВХ трубы', 'Отбеливание', 'Производство пластмасс'],
    facts: ['Был первым боевым отравляющим газом', 'Убивает бактерии в бассейнах', 'Желтовато-зелёный газ', 'Название означает "зелёный"']
  },
  {
    atomicNumber: 18, symbol: 'Ar', name: 'Argon', nameRu: 'Аргон', atomicMass: '39.95',
    category: 'noble-gas', block: 'p', period: 3, group: 18,
    discoveredBy: 'Лорд Рэлей, Уильям Рамзай', yearDiscovered: '1894', placeDiscovered: 'Англия',
    applications: ['Лампы накаливания', 'Сварка', 'Лазеры', 'Сохранение документов'],
    facts: ['Третий по распространённости газ в атмосфере', 'Не образует соединений', 'Назван от греческого "аргос" - ленивый', 'Используется в виноделии']
  },

  // Период 4
  {
    atomicNumber: 19, symbol: 'K', name: 'Potassium', nameRu: 'Калий', atomicMass: '39.10',
    category: 'alkali-metal', block: 's', period: 4, group: 1,
    discoveredBy: 'Гемфри Дэви', yearDiscovered: '1807', placeDiscovered: 'Англия',
    applications: ['Удобрения', 'Мыло', 'Пищевая соль (заменители)', 'Стекло'],
    facts: ['Символ K от латинского "калий"', 'Необходим для сердца', 'Бананы богаты калием', 'Очень активен с водой']
  },
  {
    atomicNumber: 20, symbol: 'Ca', name: 'Calcium', nameRu: 'Кальций', atomicMass: '40.08',
    category: 'alkaline-earth', block: 's', period: 4, group: 2,
    discoveredBy: 'Гемфри Дэви', yearDiscovered: '1808', placeDiscovered: 'Англия',
    applications: ['Строительство (цемент)', 'Мел', 'Молочные продукты', 'Добавки для костей'],
    facts: ['Пятый по распространённости в земной коре', 'Основной компонент костей', 'Мрамор - это карбонат кальция', 'Кораллы состоят из кальция']
  },
  {
    atomicNumber: 21, symbol: 'Sc', name: 'Scandium', nameRu: 'Скандий', atomicMass: '44.96',
    category: 'transition-metal', block: 'd', period: 4, group: 3,
    discoveredBy: 'Ларс Фредрик Нильсон', yearDiscovered: '1879', placeDiscovered: 'Швеция',
    applications: ['Аэрокосмические сплавы', 'Спортивное оборудование', 'Лампы высокого давления'],
    facts: ['Предсказан Менделеевым как "эка-бор"', 'Назван по Скандинавии', 'Редкий элемент', 'Улучшает свойства алюминия']
  },
  {
    atomicNumber: 22, symbol: 'Ti', name: 'Titanium', nameRu: 'Титан', atomicMass: '47.87',
    category: 'transition-metal', block: 'd', period: 4, group: 4,
    discoveredBy: 'Уильям Грегор', yearDiscovered: '1791', placeDiscovered: 'Англия',
    applications: ['Авиадвигатели', 'Медицинские импланты', 'Ювелирные изделия', 'Спортивные товары'],
    facts: ['Прочнее стали, но легче на 45%', 'Назван в честь титанов из мифологии', 'Гипоаллергенный', 'Не корродирует в морской воде']
  },
  {
    atomicNumber: 23, symbol: 'V', name: 'Vanadium', nameRu: 'Ванадий', atomicMass: '50.94',
    category: 'transition-metal', block: 'd', period: 4, group: 5,
    discoveredBy: 'Андрес Мануэль дель Рио', yearDiscovered: '1801', placeDiscovered: 'Мексика',
    applications: ['Инструментальные стали', 'Пружины', 'Реактивные двигатели', 'Велосипедные рамы'],
    facts: ['Назван в честь скандинавской богини Ванадис', 'Придаёт стали особую прочность', 'Соли имеют красивые цвета', 'Обнаружен в мексиканской свинцовой руде']
  },
  {
    atomicNumber: 24, symbol: 'Cr', name: 'Chromium', nameRu: 'Хром', atomicMass: '52.00',
    category: 'transition-metal', block: 'd', period: 4, group: 6,
    discoveredBy: 'Луи Николя Воклен', yearDiscovered: '1797', placeDiscovered: 'Франция',
    applications: ['Хромирование', 'Нержавеющая сталь', 'Краски', 'Кожевенное производство'],
    facts: ['Назван от греческого "хрома" - цвет', 'Даёт рубину красный цвет', 'Изумруд зелёный из-за хрома', 'Блестящий и устойчивый к коррозии']
  },
  {
    atomicNumber: 25, symbol: 'Mn', name: 'Manganese', nameRu: 'Марганец', atomicMass: '54.94',
    category: 'transition-metal', block: 'd', period: 4, group: 7,
    discoveredBy: 'Карл Шееле, Йохан Ган', yearDiscovered: '1774', placeDiscovered: 'Швеция',
    applications: ['Сталелитейная промышленность', 'Батарейки', 'Стекло (обесцвечивание)', 'Удобрения'],
    facts: ['Необходим для костей', 'Был открыт в пиролюзите', 'Древние использовали как стекло', 'Название от региона Магнезия']
  },
  {
    atomicNumber: 26, symbol: 'Fe', name: 'Iron', nameRu: 'Железо', atomicMass: '55.85',
    category: 'transition-metal', block: 'd', period: 4, group: 8,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Строительство', 'Транспорт', 'Инструменты', 'Медицина (железо в крови)'],
    facts: ['Самый распространённый металл на Земле', 'Ядро Земли состоит из железа', 'Гемоглобин содержит железо', 'Железный век длился 1000 лет']
  },
  {
    atomicNumber: 27, symbol: 'Co', name: 'Cobalt', nameRu: 'Кобальт', atomicMass: '58.93',
    category: 'transition-metal', block: 'd', period: 4, group: 9,
    discoveredBy: 'Георг Брандт', yearDiscovered: '1735', placeDiscovered: 'Швеция',
    applications: ['Литий-ионные батареи', 'Синие пигменты', 'Сплавы', 'Катализаторы'],
    facts: ['Назван от немецкого "кобольд" - гном', 'Даёт синий цвет стеклу и керамике', 'Витамин B12 содержит кобальт', 'Первый открытый древний металл']
  },
  {
    atomicNumber: 28, symbol: 'Ni', name: 'Nickel', nameRu: 'Никель', atomicMass: '58.69',
    category: 'transition-metal', block: 'd', period: 4, group: 10,
    discoveredBy: 'Аксель Кронштедт', yearDiscovered: '1751', placeDiscovered: 'Швеция',
    applications: ['Монеты', 'Нержавеющая сталь', 'Батарейки', 'Гитарные струны'],
    facts: ['Назван от немецкого "купферникель" - чертова медь', 'Монеты США содержат никель', 'Метеориты часто содержат никель', 'Аллергия на никель распространена']
  },
  {
    atomicNumber: 29, symbol: 'Cu', name: 'Copper', nameRu: 'Медь', atomicMass: '63.55',
    category: 'transition-metal', block: 'd', period: 4, group: 11,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Электропровода', 'Трубы', 'Монеты', 'Крыши зданий', 'Бронза'],
    facts: ['Лучший проводник электричества', 'Статуя Свободы сделана из меди', 'Окисляется до зелёного цвета', 'Бронзовый век длился 2000 лет']
  },
  {
    atomicNumber: 30, symbol: 'Zn', name: 'Zinc', nameRu: 'Цинк', atomicMass: '65.38',
    category: 'transition-metal', block: 'd', period: 4, group: 12,
    discoveredBy: 'Андреас Сигизмунд Маргграф', yearDiscovered: '1746', placeDiscovered: 'Германия',
    applications: ['Оцинкованная сталь', 'Батарейки', 'Солнцезащитные кремы', 'Латунь'],
    facts: ['Входит в состав 300 ферментов', 'Необходим для иммунитета', 'Предотвращает ржавчину', 'Индийские металлурги знали его в 12 веке']
  },
  {
    atomicNumber: 31, symbol: 'Ga', name: 'Gallium', nameRu: 'Галлий', atomicMass: '69.72',
    category: 'post-transition', block: 'p', period: 4, group: 13,
    discoveredBy: 'Поль Эмиль Лекок де Буабодран', yearDiscovered: '1875', placeDiscovered: 'Франция',
    applications: ['Полупроводники', 'Светодиоды', 'Термометры', 'Солнечные панели'],
    facts: ['Тает в руке (температура плавления 29.76°C)', 'Предсказан Менделеевым', 'Назван по латинскому названию Франции', 'Расширяется при застывании']
  },
  {
    atomicNumber: 32, symbol: 'Ge', name: 'Germanium', nameRu: 'Германий', atomicMass: '72.63',
    category: 'metalloid', block: 'p', period: 4, group: 14,
    discoveredBy: 'Клеменс Винклер', yearDiscovered: '1886', placeDiscovered: 'Германия',
    applications: ['Полупроводники', 'Инфракрасная оптика', 'Солнечные батареи', 'Катализаторы'],
    facts: ['Предсказан Менделеевым как "эка-кремний"', 'Назван в честь Германии', 'Первый транзистор был из германия', 'Редкий элемент']
  },
  {
    atomicNumber: 33, symbol: 'As', name: 'Arsenic', nameRu: 'Мышьяк', atomicMass: '74.92',
    category: 'metalloid', block: 'p', period: 4, group: 15,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Полупроводники', 'Консервант древесины', 'Красители', 'Пестициды'],
    facts: ['Знаменитый яд средневековья', 'Наполеон возможно был отравлен мышьяком', 'В малых дозах полезен', 'Название от греческого "арсеникон"']
  },
  {
    atomicNumber: 34, symbol: 'Se', name: 'Selenium', nameRu: 'Селен', atomicMass: '78.97',
    category: 'nonmetal', block: 'p', period: 4, group: 16,
    discoveredBy: 'Йёнс Якоб Берцелиус', yearDiscovered: '1817', placeDiscovered: 'Швеция',
    applications: ['Стекло', 'Фотокопировальные аппараты', 'Полупроводники', 'Шампуни'],
    facts: ['Назван от греческого "селена" - Луна', 'Необходим в малых дозах', 'Ядовит в больших дозах', 'Проводимость зависит от света']
  },
  {
    atomicNumber: 35, symbol: 'Br', name: 'Bromine', nameRu: 'Бром', atomicMass: '79.90',
    category: 'halogen', block: 'p', period: 4, group: 17,
    discoveredBy: 'Антуан Жером Балар', yearDiscovered: '1826', placeDiscovered: 'Франция',
    applications: ['Антипирены', 'Фотография', 'Медицина', 'Пестициды'],
    facts: ['Единственный жидкий неметалл при комнатной температуре', 'Очень ядовит', 'Назван от греческого "бромос" - зловоние', 'Красно-коричневая жидкость']
  },
  {
    atomicNumber: 36, symbol: 'Kr', name: 'Krypton', nameRu: 'Криптон', atomicMass: '83.80',
    category: 'noble-gas', block: 'p', period: 4, group: 18,
    discoveredBy: 'Уильям Рамзай, Моррис Траверс', yearDiscovered: '1898', placeDiscovered: 'Англия',
    applications: ['Лампы', 'Лазеры', 'Изоляция окон', 'Метр (изотоп Kr-86)'],
    facts: ['Назван от греческого "криптос" - скрытый', 'Супермен с планеты Криптон', 'Дал зелёный спектр', 'Очень редкий газ']
  },

  // Период 5
  {
    atomicNumber: 37, symbol: 'Rb', name: 'Rubidium', nameRu: 'Рубидий', atomicMass: '85.47',
    category: 'alkali-metal', block: 's', period: 5, group: 1,
    discoveredBy: 'Роберт Бунзен, Густав Кирхгоф', yearDiscovered: '1861', placeDiscovered: 'Германия',
    applications: ['Атомные часы', 'Фейерверки', 'Медицина', 'Глубоководные погружения'],
    facts: ['Назван по красному цвету спектра', 'Открыт методом спектроскопии', 'Мягче свинца', 'Самопроизвольно воспламеняется']
  },
  {
    atomicNumber: 38, symbol: 'Sr', name: 'Strontium', nameRu: 'Стронций', atomicMass: '87.62',
    category: 'alkaline-earth', block: 's', period: 5, group: 2,
    discoveredBy: 'Уильям Крюикшенк', yearDiscovered: '1790', placeDiscovered: 'Шотландия',
    applications: ['Фейерверки (красный цвет)', 'Электронно-лучевые трубки', 'Магниты', 'Зубная паста'],
    facts: ['Назван по шотландской деревне Стронтиан', 'Радиоактивный Sr-90 опасен', 'Даёт красное пламя', 'Входит в состав костей']
  },
  {
    atomicNumber: 39, symbol: 'Y', name: 'Yttrium', nameRu: 'Иттрий', atomicMass: '88.91',
    category: 'transition-metal', block: 'd', period: 5, group: 3,
    discoveredBy: 'Йохан Гадолин', yearDiscovered: '1794', placeDiscovered: 'Финляндия',
    applications: ['Светодиоды', 'Лазеры', 'Сверхпроводники', 'Радары'],
    facts: ['Назван по шведской деревне Иттербю', 'Иттрий даёт красный цвет в телевизорах', 'Редкоземельный элемент', 'Не радиоактивен']
  },
  {
    atomicNumber: 40, symbol: 'Zr', name: 'Zirconium', nameRu: 'Цирконий', atomicMass: '91.22',
    category: 'transition-metal', block: 'd', period: 5, group: 4,
    discoveredBy: 'Мартин Клапрот', yearDiscovered: '1789', placeDiscovered: 'Германия',
    applications: ['Ядерные реакторы', 'Ювелирные изделия', 'Керамика', 'Зубные импланты'],
    facts: ['Назван от персидского "заргун" - золотой', 'Циркон - драгоценный камень', 'Устойчив к коррозии', 'Поглощает мало нейтронов']
  },
  {
    atomicNumber: 41, symbol: 'Nb', name: 'Niobium', nameRu: 'Ниобий', atomicMass: '92.91',
    category: 'transition-metal', block: 'd', period: 5, group: 5,
    discoveredBy: 'Чарльз Хатчетт', yearDiscovered: '1801', placeDiscovered: 'Англия',
    applications: ['Сверхпроводники', 'Ювелирные изделия', 'Аэрокосмическая промышленность', 'МРТ'],
    facts: ['Назван в честь Ниобы из греческой мифологии', 'Используется в монетах', 'Сверхпроводник при низких температурах', 'Ранее назывался колумбий']
  },
  {
    atomicNumber: 42, symbol: 'Mo', name: 'Molybdenum', nameRu: 'Молибден', atomicMass: '95.95',
    category: 'transition-metal', block: 'd', period: 5, group: 6,
    discoveredBy: 'Карл Шееле', yearDiscovered: '1781', placeDiscovered: 'Швеция',
    applications: ['Сплавы стали', 'Электроды', 'Смазки', 'Катализаторы'],
    facts: ['Название означает "свинец" по-гречески', 'Очень высокая температура плавления', 'Необходим для растений', 'Устойчив к коррозии']
  },
  {
    atomicNumber: 43, symbol: 'Tc', name: 'Technetium', nameRu: 'Технеций', atomicMass: '[98]',
    category: 'transition-metal', block: 'd', period: 5, group: 7,
    discoveredBy: 'Карло Перрье, Эмилио Сегре', yearDiscovered: '1937', placeDiscovered: 'Италия',
    applications: ['Медицинская диагностика', 'Калибровка инструментов', 'Сверхпроводники'],
    facts: ['Первый искусственно созданный элемент', 'Название означает "искусственный"', 'Все изотопы радиоактивны', 'Обнаружен в звёздных спектрах']
  },
  {
    atomicNumber: 44, symbol: 'Ru', name: 'Ruthenium', nameRu: 'Рутений', atomicMass: '101.1',
    category: 'transition-metal', block: 'd', period: 5, group: 8,
    discoveredBy: 'Карл Клаус', yearDiscovered: '1844', placeDiscovered: 'Россия',
    applications: ['Электроника', 'Катализаторы', 'Ювелирные изделия', 'Солнечные панели'],
    facts: ['Назван в честь России', 'Открыт в Казанском университете', 'Платиновая группа металлов', 'Очень твёрдый']
  },
  {
    atomicNumber: 45, symbol: 'Rh', name: 'Rhodium', nameRu: 'Родий', atomicMass: '102.9',
    category: 'transition-metal', block: 'd', period: 5, group: 9,
    discoveredBy: 'Уильям Волластон', yearDiscovered: '1803', placeDiscovered: 'Англия',
    applications: ['Автомобильные катализаторы', 'Ювелирные изделия', 'Зеркала', 'Электрические контакты'],
    facts: ['Самый дорогой драгоценный металл', 'Назван по розовому цвету солей', 'Блестящий и устойчивый', 'Редкий элемент']
  },
  {
    atomicNumber: 46, symbol: 'Pd', name: 'Palladium', nameRu: 'Палладий', atomicMass: '106.4',
    category: 'transition-metal', block: 'd', period: 5, group: 10,
    discoveredBy: 'Уильям Волластон', yearDiscovered: '1803', placeDiscovered: 'Англия',
    applications: ['Автомобильные катализаторы', 'Ювелирные изделия', 'Электроника', 'Стоматология'],
    facts: ['Назван в честь астероида Паллада', 'Поглощает водород', 'Используется в белом золоте', 'Драгоценный металл']
  },
  {
    atomicNumber: 47, symbol: 'Ag', name: 'Silver', nameRu: 'Серебро', atomicMass: '107.9',
    category: 'transition-metal', block: 'd', period: 5, group: 11,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Ювелирные изделия', 'Фотография', 'Электроника', 'Зеркала', 'Медицина'],
    facts: ['Лучший проводник тепла и электричества', 'Бактерицидные свойства', 'Символ Ag от латинского "аргентум"', 'Аргентина названа в честь серебра']
  },
  {
    atomicNumber: 48, symbol: 'Cd', name: 'Cadmium', nameRu: 'Кадмий', atomicMass: '112.4',
    category: 'transition-metal', block: 'd', period: 5, group: 12,
    discoveredBy: 'Карл Штромейер', yearDiscovered: '1817', placeDiscovered: 'Германия',
    applications: ['Батарейки', 'Пигменты', 'Покрытия', 'Ядерные реакторы'],
    facts: ['Очень токсичен', 'Назван от греческого "кадмея"', 'Вызывает болезнь "итай-итай"', 'Флюоресцентные лампы']
  },
  {
    atomicNumber: 49, symbol: 'In', name: 'Indium', nameRu: 'Индий', atomicMass: '114.8',
    category: 'post-transition', block: 'p', period: 5, group: 13,
    discoveredBy: 'Фердинанд Райх, Иероним Рихтер', yearDiscovered: '1863', placeDiscovered: 'Германия',
    applications: ['Жидкокристаллические дисплеи', 'Полупроводники', 'Низкоплавкие сплавы', 'Покрытия зеркал'],
    facts: ['Назван по индиго-синей линии спектра', 'Очень мягкий металл', 'Редкий элемент', 'Используется в сенсорных экранах']
  },
  {
    atomicNumber: 50, symbol: 'Sn', name: 'Tin', nameRu: 'Олово', atomicMass: '118.7',
    category: 'post-transition', block: 'p', period: 5, group: 14,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Бронза', 'Припой', 'Консервные банки', 'Покрытия'],
    facts: ['Бронзовый век назван по сплаву олова', 'Символ Sn от латинского "станнум"', 'При низких температурах рассыпается', 'Устойчиво к коррозии']
  },
  {
    atomicNumber: 51, symbol: 'Sb', name: 'Antimony', nameRu: 'Сурьма', atomicMass: '121.8',
    category: 'metalloid', block: 'p', period: 5, group: 15,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Пуляки', 'Батареи', 'Огнеупоры', 'Косметика'],
    facts: ['Символ Sb от латинского "стибиум"', 'Использовалась в Древнем Египте как тушь', 'Токсичен', 'Раньше использовался в медицине']
  },
  {
    atomicNumber: 52, symbol: 'Te', name: 'Tellurium', nameRu: 'Теллур', atomicMass: '127.6',
    category: 'metalloid', block: 'p', period: 5, group: 16,
    discoveredBy: 'Франц Йозеф Мюллер', yearDiscovered: '1782', placeDiscovered: 'Австрия',
    applications: ['Солнечные батареи', 'Термопары', 'Сплавы', 'Стекло'],
    facts: ['Назван от латинского "теллус" - Земля', 'Редкий элемент', 'Токсичен', 'Полупроводник']
  },
  {
    atomicNumber: 53, symbol: 'I', name: 'Iodine', nameRu: 'Йод', atomicMass: '126.9',
    category: 'halogen', block: 'p', period: 5, group: 17,
    discoveredBy: 'Бернар Куртуа', yearDiscovered: '1811', placeDiscovered: 'Франция',
    applications: ['Антисептики', 'Соль (йодированная)', 'Рентгеноконтрастные вещества', 'Фотография'],
    facts: ['Открыт при производстве селитры', 'Необходим для щитовидной железы', 'Фиолетовые пары', 'Назван от греческого "иодес" - фиолетовый']
  },
  {
    atomicNumber: 54, symbol: 'Xe', name: 'Xenon', nameRu: 'Ксенон', atomicMass: '131.3',
    category: 'noble-gas', block: 'p', period: 5, group: 18,
    discoveredBy: 'Уильям Рамзай, Моррис Траверс', yearDiscovered: '1898', placeDiscovered: 'Англия',
    applications: ['Лампы', 'Анестезия', 'Ионные двигатели', 'МРТ'],
    facts: ['Назван от греческого "ксенос" - чужой', 'Может образовывать соединения', 'Используется в автомобильных фарах', 'Очень редкий газ']
  },

  // Период 6
  {
    atomicNumber: 55, symbol: 'Cs', name: 'Cesium', nameRu: 'Цезий', atomicMass: '132.9',
    category: 'alkali-metal', block: 's', period: 6, group: 1,
    discoveredBy: 'Роберт Бунзен, Густав Кирхгоф', yearDiscovered: '1860', placeDiscovered: 'Германия',
    applications: ['Атомные часы', 'Бурение', 'Фотоэлементы', 'Медицина'],
    facts: ['Назван по небесно-голубой линии спектра', 'Почти жидкий при комнатной температуре', 'Взрывается в воде', 'Точка плавления 28.5°C']
  },
  {
    atomicNumber: 56, symbol: 'Ba', name: 'Barium', nameRu: 'Барий', atomicMass: '137.3',
    category: 'alkaline-earth', block: 's', period: 6, group: 2,
    discoveredBy: 'Карл Шееле', yearDiscovered: '1772', placeDiscovered: 'Швеция',
    applications: ['Рентген (бариевая кашица)', 'Фейерверки', 'Стекло', 'Керамика'],
    facts: ['Назван от греческого "барис" - тяжёлый', 'Даёт зелёный цвет фейерверкам', 'Барий растворим и ядовит', 'Барит - тяжёлый минерал']
  },
  {
    atomicNumber: 57, symbol: 'La', name: 'Lanthanum', nameRu: 'Лантан', atomicMass: '138.9',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Карл Мосандер', yearDiscovered: '1839', placeDiscovered: 'Швеция',
    applications: ['Линзы', 'Катализаторы', 'Зажигалки', 'Аккумуляторы'],
    facts: ['Назван от греческого "лантанеин" - скрываться', 'Первый лантаноид', 'Редкоземельный элемент', 'Мягкий и пластичный']
  },
  {
    atomicNumber: 58, symbol: 'Ce', name: 'Cerium', nameRu: 'Церий', atomicMass: '140.1',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Йёнс Якоб Берцелиус', yearDiscovered: '1803', placeDiscovered: 'Швеция',
    applications: ['Катализаторы', 'Стекло', 'Зажигалки', 'Полировка'],
    facts: ['Назван в честь астероида Церера', 'Самый распространённый лантаноид', 'Используется в пирофорных сплавах', 'Дешёвле других редкоземельных']
  },
  {
    atomicNumber: 59, symbol: 'Pr', name: 'Praseodymium', nameRu: 'Празеодим', atomicMass: '140.9',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Карл Ауэр фон Вельсбах', yearDiscovered: '1885', placeDiscovered: 'Австрия',
    applications: ['Магниты', 'Стекло', 'Сварочные маски', 'Катализаторы'],
    facts: ['Назван от греческого "прасиос" - луково-зелёный', 'Даёт зелёный цвет стеклу', 'Ранее считался одним элементом с неодимом', 'Используется в авиадвигателях']
  },
  {
    atomicNumber: 60, symbol: 'Nd', name: 'Neodymium', nameRu: 'Неодим', atomicMass: '144.2',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Карл Ауэр фон Вельсбах', yearDiscovered: '1885', placeDiscovered: 'Австрия',
    applications: ['Сильные магниты', 'Лазеры', 'Наушники', 'Жёсткие диски'],
    facts: ['Назван от греческого "неос дидимос" - новый близнец', 'Самые сильные постоянные магниты', 'Фиолетовый цвет стеклу', 'Используется в ветрогенераторах']
  },
  {
    atomicNumber: 61, symbol: 'Pm', name: 'Promethium', nameRu: 'Прометий', atomicMass: '[145]',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Чин Шиен-Сиан', yearDiscovered: '1945', placeDiscovered: 'США',
    applications: ['Ядерные батареи', 'Светящиеся краски', 'Толщиномеры'],
    facts: ['Назван в честь Прометея из мифологии', 'Все изотопы радиоактивны', 'Нет стабильных изотопов', 'Редчайший лантаноид']
  },
  {
    atomicNumber: 62, symbol: 'Sm', name: 'Samarium', nameRu: 'Самарий', atomicMass: '150.4',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Поль Эмиль Лекок де Буабодран', yearDiscovered: '1879', placeDiscovered: 'Франция',
    applications: ['Магниты', 'Лазеры', 'Ядерные реакторы', 'Медицина'],
    facts: ['Назван в честь русского инженера Самарского', 'Используется в лечении рака', 'Магниты из самария и кобальта', 'Твёрдый и хрупкий']
  },
  {
    atomicNumber: 63, symbol: 'Eu', name: 'Europium', nameRu: 'Европий', atomicMass: '152.0',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Эжен Демарсе', yearDiscovered: '1901', placeDiscovered: 'Франция',
    applications: ['Телевизоры', 'Евро-банкноты', 'Светящиеся материалы', 'Лазеры'],
    facts: ['Назван в честь Европы', 'Самый реакционный лантаноид', 'Используется для защиты валют', 'Даёт красный и синий цвет в ТВ']
  },
  {
    atomicNumber: 64, symbol: 'Gd', name: 'Gadolinium', nameRu: 'Гадолиний', atomicMass: '157.3',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Жан Шарль Галиссар де Мариньяк', yearDiscovered: '1880', placeDiscovered: 'Швейцария',
    applications: ['МРТ-контраст', 'Магниты', 'Ядерные реакторы', 'Лазеры'],
    facts: ['Назван в честь минералога Гадолина', 'Парамагнитен', 'Лучший поглотитель нейтронов', 'Используется в медицине']
  },
  {
    atomicNumber: 65, symbol: 'Tb', name: 'Terbium', nameRu: 'Тербий', atomicMass: '158.9',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Карл Мосандер', yearDiscovered: '1843', placeDiscovered: 'Швеция',
    applications: ['Телевизоры', 'Лампы', 'Магниты', 'Светящиеся материалы'],
    facts: ['Назван по шведской деревне Иттербю', 'Зелёный люминофор', 'Редкий лантаноид', 'Используется в долларах']
  },
  {
    atomicNumber: 66, symbol: 'Dy', name: 'Dysprosium', nameRu: 'Диспрозий', atomicMass: '162.5',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Поль Эмиль Лекок де Буабодран', yearDiscovered: '1886', placeDiscovered: 'Франция',
    applications: ['Магниты', 'Лазеры', 'Ядерные реакторы', 'Жёсткие диски'],
    facts: ['Назван от греческого "диспрозитос" - труднодоступный', 'Используется в электромобилях', 'Магнитные свойства', 'Мягкий металл']
  },
  {
    atomicNumber: 67, symbol: 'Ho', name: 'Holmium', nameRu: 'Гольмий', atomicMass: '164.9',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Марк Делафонтен, Жак-Луи Соре', yearDiscovered: '1878', placeDiscovered: 'Швейцария',
    applications: ['Магниты', 'Лазеры', 'Ядерные реакторы'],
    facts: ['Назван по латинскому названию Стокгольма', 'Самые сильные искусственные магниты', 'Используется в медицине', 'Редкий элемент']
  },
  {
    atomicNumber: 68, symbol: 'Er', name: 'Erbium', nameRu: 'Эрбий', atomicMass: '167.3',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Карл Мосандер', yearDiscovered: '1843', placeDiscovered: 'Швеция',
    applications: ['Оптоволокно', 'Лазеры', 'Стекло', 'Металлургия'],
    facts: ['Назван по шведской деревне Иттербю', 'Розовое стекло', 'Лазеры для стоматологии', 'Интернет-кабели']
  },
  {
    atomicNumber: 69, symbol: 'Tm', name: 'Thulium', nameRu: 'Тулий', atomicMass: '168.9',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Пер Теодор Клеве', yearDiscovered: '1879', placeDiscovered: 'Швеция',
    applications: ['Лазеры', 'Рентген', 'Сверхпроводники'],
    facts: ['Назван по древнему названию Скандинавии - Туле', 'Редчайший лантаноид', 'Используется в медицине', 'Мягкий металл']
  },
  {
    atomicNumber: 70, symbol: 'Yb', name: 'Ytterbium', nameRu: 'Иттербий', atomicMass: '173.0',
    category: 'lanthanide', block: 'f', period: 6, group: 3,
    discoveredBy: 'Жан Шарль Галиссар де Мариньяк', yearDiscovered: '1878', placeDiscovered: 'Швейцария',
    applications: ['Лазеры', 'Стали', 'Атомные часы', 'Пластиковые пакеты'],
    facts: ['Назван по шведской деревне Иттербю', '4 элемента названы по этой деревне', 'Мягкий металл', 'Используется в сейсмологии']
  },
  {
    atomicNumber: 71, symbol: 'Lu', name: 'Lutetium', nameRu: 'Лютеций', atomicMass: '175.0',
    category: 'lanthanide', block: 'd', period: 6, group: 3,
    discoveredBy: 'Жорж Урбен', yearDiscovered: '1907', placeDiscovered: 'Франция',
    applications: ['Катализаторы', 'ПЭТ-сканеры', 'Светодиоды'],
    facts: ['Назван по латинскому названию Парижа', 'Последний лантаноид', 'Самый тяжёлый лантаноид', 'Редкий и дорогой']
  },
  {
    atomicNumber: 72, symbol: 'Hf', name: 'Hafnium', nameRu: 'Гафний', atomicMass: '178.5',
    category: 'transition-metal', block: 'd', period: 6, group: 4,
    discoveredBy: 'Дирк Костер, Дьёрдь Хевеши', yearDiscovered: '1923', placeDiscovered: 'Дания',
    applications: ['Процессоры', 'Ядерные реакторы', 'Сплавы', 'Микросхемы'],
    facts: ['Назван по латинскому названию Копенгагена', 'Похож на цирконий', 'Поглощает нейтроны', 'Используется в Intel']
  },
  {
    atomicNumber: 73, symbol: 'Ta', name: 'Tantalum', nameRu: 'Тантал', atomicMass: '180.9',
    category: 'transition-metal', block: 'd', period: 6, group: 5,
    discoveredBy: 'Андерс Густав Экеберг', yearDiscovered: '1802', placeDiscovered: 'Швеция',
    applications: ['Конденсаторы', 'Хирургические инструменты', 'Ювелирные изделия', 'Мобильные телефоны'],
    facts: ['Назван в честь мифологического Тантала', 'Очень устойчив к коррозии', 'Конфликтный минерал', 'В каждом смартфоне']
  },
  {
    atomicNumber: 74, symbol: 'W', name: 'Tungsten', nameRu: 'Вольфрам', atomicMass: '183.8',
    category: 'transition-metal', block: 'd', period: 6, group: 6,
    discoveredBy: 'Карл Шееле', yearDiscovered: '1781', placeDiscovered: 'Швеция',
    applications: ['Лампы накаливания', 'Сплавы', 'Инструменты', 'Броня'],
    facts: ['Самая высокая температура плавления (3422°C)', 'Символ W от немецкого "вольфрам"', 'Нить в лампочках', 'Очень твёрдый']
  },
  {
    atomicNumber: 75, symbol: 'Re', name: 'Rhenium', nameRu: 'Рений', atomicMass: '186.2',
    category: 'transition-metal', block: 'd', period: 6, group: 7,
    discoveredBy: 'Масатака Огава, Вальтер Ноддак', yearDiscovered: '1925', placeDiscovered: 'Германия',
    applications: ['Авиадвигатели', 'Катализаторы', 'Термопары', 'Сплавы'],
    facts: ['Назван по латинскому названию Рейна', 'Один из редчайших элементов', 'Очень высокая температура плавления', 'Открыт последним из стабильных']
  },
  {
    atomicNumber: 76, symbol: 'Os', name: 'Osmium', nameRu: 'Осмий', atomicMass: '190.2',
    category: 'transition-metal', block: 'd', period: 6, group: 8,
    discoveredBy: 'Смитсон Теннант', yearDiscovered: '1803', placeDiscovered: 'Англия',
    applications: ['Перья ручек', 'Импланты', 'Катализаторы', 'Отпечатки пальцев'],
    facts: ['Самый плотный элемент', 'Назван от греческого "осме" - запах', 'Токсичный оксид', 'Платиновая группа']
  },
  {
    atomicNumber: 77, symbol: 'Ir', name: 'Iridium', nameRu: 'Иридий', atomicMass: '192.2',
    category: 'transition-metal', block: 'd', period: 6, group: 9,
    discoveredBy: 'Смитсон Теннант', yearDiscovered: '1803', placeDiscovered: 'Англия',
    applications: ['Свечи зажигания', 'Контакты', 'Тигли', 'Стандарт килограмма'],
    facts: ['Назван от греческого "ирис" - радуга', 'Самый устойчивый к коррозии', 'Найден в метеоритах', 'Вымерание динозавров']
  },
  {
    atomicNumber: 78, symbol: 'Pt', name: 'Platinum', nameRu: 'Платина', atomicMass: '195.1',
    category: 'transition-metal', block: 'd', period: 6, group: 10,
    discoveredBy: 'Антонио де Ульоа', yearDiscovered: '1735', placeDiscovered: 'Южная Америка',
    applications: ['Ювелирные изделия', 'Катализаторы', 'Медицина', 'Электроды'],
    facts: ['Название означает "маленькое серебро"', 'Драгоценный металл', 'Устойчив к коррозии', 'Платиновая карточка']
  },
  {
    atomicNumber: 79, symbol: 'Au', name: 'Gold', nameRu: 'Золото', atomicMass: '197.0',
    category: 'transition-metal', block: 'd', period: 6, group: 11,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Ювелирные изделия', 'Электроника', 'Зубы', 'Космонавтика', 'Инвестиции'],
    facts: ['Не ржавеет', 'Можно расплющить до тончайшей фольги', 'Символ Au от латинского "аурум"', 'Золото было в маске Тутанхамона']
  },
  {
    atomicNumber: 80, symbol: 'Hg', name: 'Mercury', nameRu: 'Ртуть', atomicMass: '200.6',
    category: 'transition-metal', block: 'd', period: 6, group: 12,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Термометры', 'Лампы', 'Зубные пломбы', 'Золотоискательство'],
    facts: ['Единственный жидкий металл', 'Символ Hg от латинского "гидрагирум"', 'Очень токсична', 'Шляпники сходили с ума от ртути']
  },
  {
    atomicNumber: 81, symbol: 'Tl', name: 'Thallium', nameRu: 'Таллий', atomicMass: '204.4',
    category: 'post-transition', block: 'p', period: 6, group: 13,
    discoveredBy: 'Уильям Кукс', yearDiscovered: '1861', placeDiscovered: 'Англия',
    applications: ['Оптика', 'Электроника', 'Медицина', 'Стекло'],
    facts: ['Назван по зелёной линии спектра', 'Очень ядовит', 'Использовался как яд', "Знаменитый отравитель Грэм Янг"]
  },
  {
    atomicNumber: 82, symbol: 'Pb', name: 'Lead', nameRu: 'Свинец', atomicMass: '207.2',
    category: 'post-transition', block: 'p', period: 6, group: 14,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Батареи', 'Радиация защита', 'Пули', 'Припой'],
    facts: ['Очень токсичен', 'Символ Pb от латинского "плюмбум"', 'Римляне использовали в трубах', 'Бензин раньше содержал свинец']
  },
  {
    atomicNumber: 83, symbol: 'Bi', name: 'Bismuth', nameRu: 'Висмут', atomicMass: '209.0',
    category: 'post-transition', block: 'p', period: 6, group: 15,
    discoveredBy: 'Известен с древности', yearDiscovered: 'До нашей эры', placeDiscovered: 'Везде',
    applications: ['Медицина', 'Косметика', 'Сплавы', 'Пуляки'],
    facts: ['Радужные кристаллы', 'Мало токсичен', 'Пепто-бисмол содержит висмут', 'Диамагнитен']
  },
  {
    atomicNumber: 84, symbol: 'Po', name: 'Polonium', nameRu: 'Полоний', atomicMass: '[209]',
    category: 'metalloid', block: 'p', period: 6, group: 16,
    discoveredBy: 'Мария и Пьер Кюри', yearDiscovered: '1898', placeDiscovered: 'Франция',
    applications: ['Антистатика', 'Источники тепла', 'Источники альфа-излучения'],
    facts: ['Назван в честь Польши', 'Открыт Кюри', 'Очень радиоактивен', 'Использован для убийства Литвиненко']
  },
  {
    atomicNumber: 85, symbol: 'At', name: 'Astatine', nameRu: 'Астат', atomicMass: '[210]',
    category: 'halogen', block: 'p', period: 6, group: 17,
    discoveredBy: 'Дейл Корсон, Кеннет Маккензи, Эмилио Сегре', yearDiscovered: '1940', placeDiscovered: 'США',
    applications: ['Медицина (исследования)', 'Научные исследования'],
    facts: ['Назван от греческого "астатос" - неустойчивый', 'Самый редкий элемент на Земле', 'Все изотопы радиоактивны', 'Меньше 1 грамма на Земле']
  },
  {
    atomicNumber: 86, symbol: 'Rn', name: 'Radon', nameRu: 'Радон', atomicMass: '[222]',
    category: 'noble-gas', block: 'p', period: 6, group: 18,
    discoveredBy: 'Фридрих Дорн', yearDiscovered: '1900', placeDiscovered: 'Германия',
    applications: ['Медицина', 'Обнаружение разломов', 'Научные исследования'],
    facts: ['Радиоактивный газ', 'Скапливается в подвалах', 'Вторая причина рака лёгких', 'Назван от радия']
  },

  // Период 7
  {
    atomicNumber: 87, symbol: 'Fr', name: 'Francium', nameRu: 'Франций', atomicMass: '[223]',
    category: 'alkali-metal', block: 's', period: 7, group: 1,
    discoveredBy: 'Маргерит Перей', yearDiscovered: '1939', placeDiscovered: 'Франция',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Франции', 'Самый нестабильный природный элемент', 'Открыт женщиной', 'Всего 20-30 грамм в земной коре']
  },
  {
    atomicNumber: 88, symbol: 'Ra', name: 'Radium', nameRu: 'Радий', atomicMass: '[226]',
    category: 'alkaline-earth', block: 's', period: 7, group: 2,
    discoveredBy: 'Мария и Пьер Кюри', yearDiscovered: '1898', placeDiscovered: 'Франция',
    applications: ['Медицина (исторически)', 'Светящиеся краски', 'Нейтронный источник'],
    facts: ['Светится в темноте', 'Радиоактивен', 'Кюри умерли от радиации', 'Раньше был в часах']
  },
  {
    atomicNumber: 89, symbol: 'Ac', name: 'Actinium', nameRu: 'Актиний', atomicMass: '[227]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Фридрих Оскар Гизель', yearDiscovered: '1899', placeDiscovered: 'Германия',
    applications: ['Нейтронный источник', 'Научные исследования'],
    facts: ['Назван от греческого "актис" - луч', 'В 150 раз радиоактивнее радия', 'Первый актинид', 'Светится в темноте']
  },
  {
    atomicNumber: 90, symbol: 'Th', name: 'Thorium', nameRu: 'Торий', atomicMass: '232.0',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Йёнс Якоб Берцелиус', yearDiscovered: '1829', placeDiscovered: 'Швеция',
    applications: ['Газовые лампы', 'Ядерное топливо', 'Сварка', 'Стекло'],
    facts: ['Назван в честь бога Тора', 'В 3 раза распространённее урана', 'Возможно топливо будущего', 'Слабо радиоактивен']
  },
  {
    atomicNumber: 91, symbol: 'Pa', name: 'Protactinium', nameRu: 'Протактиний', atomicMass: '231.0',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Касимир Фаянс, Отто Геринг', yearDiscovered: '1913', placeDiscovered: 'Германия',
    applications: ['Научные исследования'],
    facts: ['Назван как "родитель актиния"', 'Очень редкий', 'Радиоактивен', 'Токсичен']
  },
  {
    atomicNumber: 92, symbol: 'U', name: 'Uranium', nameRu: 'Уран', atomicMass: '238.0',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Мартин Клапрот', yearDiscovered: '1789', placeDiscovered: 'Германия',
    applications: ['Ядерные реакторы', 'Ядерное оружие', 'Броня', 'Краски'],
    facts: ['Назван в честь планеты Уран', 'Радиоактивен', 'Используется в АЭС', 'Энрико Ферми создал первый реактор']
  },
  {
    atomicNumber: 93, symbol: 'Np', name: 'Neptunium', nameRu: 'Нептуний', atomicMass: '[237]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Эдвин Макмиллан, Филип Абельсон', yearDiscovered: '1940', placeDiscovered: 'США',
    applications: ['Детекторы нейтронов', 'Научные исследования'],
    facts: ['Назван в честь планеты Нептун', 'Первый трансурановый элемент', 'Радиоактивен', 'Образуется в реакторах']
  },
  {
    atomicNumber: 94, symbol: 'Pu', name: 'Plutonium', nameRu: 'Плутоний', atomicMass: '[244]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Гленн Сиборг', yearDiscovered: '1940', placeDiscovered: 'США',
    applications: ['Ядерное оружие', 'Ядерные реакторы', 'Космические аппараты'],
    facts: ['Назван в честь планеты Плутон', 'Использован в бомбе над Нагасаки', 'Самый токсичный элемент', 'Вояджер работает на плутонии']
  },
  {
    atomicNumber: 95, symbol: 'Am', name: 'Americium', nameRu: 'Америций', atomicMass: '[243]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Гленн Сиборг', yearDiscovered: '1944', placeDiscovered: 'США',
    applications: ['Дымовые датчики', 'Нейтронный источник', 'Медицина'],
    facts: ['Назван в честь Америки', 'В каждом датчике дыма', 'Радиоактивен', 'Искусственный элемент']
  },
  {
    atomicNumber: 96, symbol: 'Cm', name: 'Curium', nameRu: 'Кюрий', atomicMass: '[247]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Гленн Сиборг', yearDiscovered: '1944', placeDiscovered: 'США',
    applications: ['Альфа-источник', 'Космические аппараты'],
    facts: ['Назван в честь Кюри', 'Свечением напоминает звезду', 'Радиоактивен', 'Очень мощный источник']
  },
  {
    atomicNumber: 97, symbol: 'Bk', name: 'Berkelium', nameRu: 'Берклий', atomicMass: '[247]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Гленн Сиборг', yearDiscovered: '1949', placeDiscovered: 'США',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Беркли', 'Синтезирован в Калифорнии', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 98, symbol: 'Cf', name: 'Californium', nameRu: 'Калифорний', atomicMass: '[251]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Гленн Сиборг', yearDiscovered: '1950', placeDiscovered: 'США',
    applications: ['Обнаружение золота', 'Обнаружение нефти', 'Медицина', 'Скважины'],
    facts: ['Назван в честь Калифорнии', 'Дороже золота в миллионы раз', 'Мощный нейтронный источник', 'Мало производится']
  },
  {
    atomicNumber: 99, symbol: 'Es', name: 'Einsteinium', nameRu: 'Эйнштейний', atomicMass: '[252]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Альберт Гиорсо', yearDiscovered: '1952', placeDiscovered: 'США',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Эйнштейна', 'Обнаружен в водородной бомбе', 'Радиоактивен', 'Очень редкий']
  },
  {
    atomicNumber: 100, symbol: 'Fm', name: 'Fermium', nameRu: 'Фермий', atomicMass: '[257]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Альберт Гиорсо', yearDiscovered: '1952', placeDiscovered: 'США',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Ферми', 'Обнаружен в водородной бомбе', 'Нет стабильных изотопов', 'Мало изучен']
  },
  {
    atomicNumber: 101, symbol: 'Md', name: 'Mendelevium', nameRu: 'Менделевий', atomicMass: '[258]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Альберт Гиорсо', yearDiscovered: '1955', placeDiscovered: 'США',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Менделеева', 'Первый элемент названный при жизни учёного', 'Радиоактивен', 'Мало производится']
  },
  {
    atomicNumber: 102, symbol: 'No', name: 'Nobelium', nameRu: 'Нобелий', atomicMass: '[259]',
    category: 'actinide', block: 'f', period: 7, group: 3,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '1966', placeDiscovered: 'СССР',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Нобеля', 'Спор об открытии СССР/США', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 103, symbol: 'Lr', name: 'Lawrencium', nameRu: 'Лоуренсий', atomicMass: '[262]',
    category: 'actinide', block: 'd', period: 7, group: 3,
    discoveredBy: 'Альберт Гиорсо', yearDiscovered: '1961', placeDiscovered: 'США',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Эрнеста Лоуренса', 'Последний актинид', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 104, symbol: 'Rf', name: 'Rutherfordium', nameRu: 'Резерфордий', atomicMass: '[267]',
    category: 'transition-metal', block: 'd', period: 7, group: 4,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '1964', placeDiscovered: 'СССР',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Резерфорда', 'Спор об открытии СССР/США', 'Радиоактивен', 'Несколько атомов']
  },
  {
    atomicNumber: 105, symbol: 'Db', name: 'Dubnium', nameRu: 'Дубний', atomicMass: '[268]',
    category: 'transition-metal', block: 'd', period: 7, group: 5,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '1970', placeDiscovered: 'СССР',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Дубны', 'Советский город науки', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 106, symbol: 'Sg', name: 'Seaborgium', nameRu: 'Сиборгий', atomicMass: '[269]',
    category: 'transition-metal', block: 'd', period: 7, group: 6,
    discoveredBy: 'Альберт Гиорсо', yearDiscovered: '1974', placeDiscovered: 'США',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Гленна Сиборга', 'Прижизненное название', 'Радиоактивен', 'Первый названный при жизни']
  },
  {
    atomicNumber: 107, symbol: 'Bh', name: 'Bohrium', nameRu: 'Борий', atomicMass: '[270]',
    category: 'transition-metal', block: 'd', period: 7, group: 7,
    discoveredBy: 'Gesellschaft für Schwerionenforschung', yearDiscovered: '1981', placeDiscovered: 'Германия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Нильса Бора', 'Радиоактивен', 'Мало изучен', 'Синтезирован в Дармштадте']
  },
  {
    atomicNumber: 108, symbol: 'Hs', name: 'Hassium', nameRu: 'Хассий', atomicMass: '[269]',
    category: 'transition-metal', block: 'd', period: 7, group: 8,
    discoveredBy: 'Gesellschaft für Schwerionenforschung', yearDiscovered: '1984', placeDiscovered: 'Германия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Гессена', 'Германская земля', 'Радиоактивен', 'Синтезирован в Дармштадте']
  },
  {
    atomicNumber: 109, symbol: 'Mt', name: 'Meitnerium', nameRu: 'Мейтнерий', atomicMass: '[278]',
    category: 'transition-metal', block: 'd', period: 7, group: 9,
    discoveredBy: 'Gesellschaft für Schwerionenforschung', yearDiscovered: '1982', placeDiscovered: 'Германия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Лизы Мейтнер', 'Женщина-физик', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 110, symbol: 'Ds', name: 'Darmstadtium', nameRu: 'Дармштадтий', atomicMass: '[281]',
    category: 'transition-metal', block: 'd', period: 7, group: 10,
    discoveredBy: 'Gesellschaft für Schwerionenforschung', yearDiscovered: '1994', placeDiscovered: 'Германия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Дармштадта', 'Город в Германии', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 111, symbol: 'Rg', name: 'Roentgenium', nameRu: 'Рентгений', atomicMass: '[282]',
    category: 'transition-metal', block: 'd', period: 7, group: 11,
    discoveredBy: 'Gesellschaft für Schwerionenforschung', yearDiscovered: '1994', placeDiscovered: 'Германия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Рентгена', 'Открыватель рентгеновских лучей', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 112, symbol: 'Cn', name: 'Copernicium', nameRu: 'Коперниций', atomicMass: '[285]',
    category: 'transition-metal', block: 'd', period: 7, group: 12,
    discoveredBy: 'Gesellschaft für Schwerionenforschung', yearDiscovered: '1996', placeDiscovered: 'Германия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Коперника', 'Возможно газ при комнатной температуре', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 113, symbol: 'Nh', name: 'Nihonium', nameRu: 'Нихоний', atomicMass: '[286]',
    category: 'post-transition', block: 'p', period: 7, group: 13,
    discoveredBy: 'RIKEN', yearDiscovered: '2004', placeDiscovered: 'Япония',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Японии (нихон)', 'Первый японский элемент', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 114, symbol: 'Fl', name: 'Flerovium', nameRu: 'Флеровий', atomicMass: '[289]',
    category: 'post-transition', block: 'p', period: 7, group: 14,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '1998', placeDiscovered: 'Россия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Флёрова', 'Советский физик', 'Радиоактивен', 'Возможно инертный газ']
  },
  {
    atomicNumber: 115, symbol: 'Mc', name: 'Moscovium', nameRu: 'Московий', atomicMass: '[290]',
    category: 'post-transition', block: 'p', period: 7, group: 15,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '2003', placeDiscovered: 'Россия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Москвы', 'Российская столица', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 116, symbol: 'Lv', name: 'Livermorium', nameRu: 'Ливерморий', atomicMass: '[293]',
    category: 'post-transition', block: 'p', period: 7, group: 16,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '2000', placeDiscovered: 'Россия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Ливермора', 'Город в Калифорнии', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 117, symbol: 'Ts', name: 'Tennessine', nameRu: 'Теннессин', atomicMass: '[294]',
    category: 'halogen', block: 'p', period: 7, group: 17,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '2010', placeDiscovered: 'Россия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Теннесси', 'Штат США', 'Радиоактивен', 'Мало изучен']
  },
  {
    atomicNumber: 118, symbol: 'Og', name: 'Oganesson', nameRu: 'Оганесон', atomicMass: '[294]',
    category: 'noble-gas', block: 'p', period: 7, group: 18,
    discoveredBy: 'Объединённый институт ядерных исследований', yearDiscovered: '2002', placeDiscovered: 'Россия',
    applications: ['Научные исследования'],
    facts: ['Назван в честь Оганесяна', 'Армянский физик', 'Самый тяжёлый элемент', 'Радиоактивен']
  }
]

// ==================== ИГРА: УГАДАЙ ЭЛЕМЕНТ ====================
interface Question {
  atomicNumber: number
  symbol: string
  name: string
  properties: string[]
  options: { atomicNumber: number; symbol: string; name: string }[]
  fact: string
}

// Компактное отображение электронов для игры
function GameElectronDisplay({ atomicNumber }: { atomicNumber: number }) {
  const shells = getElectronConfiguration(atomicNumber)
  const shellNames = ['K', 'L', 'M', 'N', 'O', 'P', 'Q']
  const shellColors = ['text-red-400', 'text-orange-400', 'text-yellow-400', 'text-green-400', 'text-cyan-400', 'text-blue-400', 'text-purple-400']
  
  return (
    <div className="flex flex-wrap justify-center gap-1 sm:gap-2 text-[10px] sm:text-xs">
      {shells.map((count, idx) => (
        <div key={idx} className="flex items-center gap-0.5 sm:gap-1 bg-white/5 px-1.5 sm:px-2 py-0.5 sm:py-1 rounded-full">
          <span className={shellColors[idx]}>{shellNames[idx]}:</span>
          <span className="text-white font-bold">{count}</span>
        </div>
      ))}
    </div>
  )
}

const questionsPool: Question[] = [
  {
    atomicNumber: 1, symbol: 'H', name: 'Водород',
    properties: [
      "Самый лёгкий элемент во Вселенной",
      "Атомный номер 1",
      "Период 1, группа 1",
      "Основной компонент звёзд и Солнца"
    ],
    options: [
      { atomicNumber: 1, symbol: 'H', name: 'Водород' },
      { atomicNumber: 2, symbol: 'He', name: 'Гелий' },
      { atomicNumber: 6, symbol: 'C', name: 'Углерод' },
      { atomicNumber: 8, symbol: 'O', name: 'Кислород' }
    ],
    fact: "Водород — самый распространённый элемент во Вселенной (около 75% массы)!"
  },
  {
    atomicNumber: 6, symbol: 'C', name: 'Углерод',
    properties: [
      "Основа всех органических веществ и жизни",
      "Встречается в виде алмаза и графита",
      "Атомный номер 6",
      "Период 2, группа 14"
    ],
    options: [
      { atomicNumber: 6, symbol: 'C', name: 'Углерод' },
      { atomicNumber: 8, symbol: 'O', name: 'Кислород' },
      { atomicNumber: 14, symbol: 'Si', name: 'Кремний' },
      { atomicNumber: 7, symbol: 'N', name: 'Азот' }
    ],
    fact: "Углерод — основа всей органической химии и жизни на Земле!"
  },
  {
    atomicNumber: 8, symbol: 'O', name: 'Кислород',
    properties: [
      "Составляет 21% атмосферы Земли",
      "Необходим для дыхания всех животных",
      "Атомный номер 8",
      "Самый распространённый элемент в земной коре"
    ],
    options: [
      { atomicNumber: 8, symbol: 'O', name: 'Кислород' },
      { atomicNumber: 7, symbol: 'N', name: 'Азот' },
      { atomicNumber: 1, symbol: 'H', name: 'Водород' },
      { atomicNumber: 16, symbol: 'S', name: 'Сера' }
    ],
    fact: "Кислород — самый важный элемент для жизни!"
  },
  {
    atomicNumber: 26, symbol: 'Fe', name: 'Железо',
    properties: [
      "Входит в состав гемоглобина крови",
      "Самый распространённый металл в ядре Земли",
      "Атомный номер 26",
      "Используется в производстве стали"
    ],
    options: [
      { atomicNumber: 26, symbol: 'Fe', name: 'Железо' },
      { atomicNumber: 29, symbol: 'Cu', name: 'Медь' },
      { atomicNumber: 79, symbol: 'Au', name: 'Золото' },
      { atomicNumber: 13, symbol: 'Al', name: 'Алюминий' }
    ],
    fact: "Железо — самый важный металл цивилизации!"
  },
  {
    atomicNumber: 79, symbol: 'Au', name: 'Золото',
    properties: [
      "Благородный металл жёлтого цвета",
      "Один из самых ковких металлов",
      "Атомный номер 79",
      "Не окисляется на воздухе"
    ],
    options: [
      { atomicNumber: 79, symbol: 'Au', name: 'Золото' },
      { atomicNumber: 47, symbol: 'Ag', name: 'Серебро' },
      { atomicNumber: 78, symbol: 'Pt', name: 'Платина' },
      { atomicNumber: 80, symbol: 'Hg', name: 'Ртуть' }
    ],
    fact: "Золото — один из самых древних металлов, известных человеку!"
  },
  {
    atomicNumber: 11, symbol: 'Na', name: 'Натрий',
    properties: ["Взрывается в воде", "Входит в состав поваренной соли", "Атомный номер 11", "Щелочной металл"],
    options: [
      { atomicNumber: 11, symbol: 'Na', name: 'Натрий' },
      { atomicNumber: 19, symbol: 'K', name: 'Калий' },
      { atomicNumber: 3, symbol: 'Li', name: 'Литий' },
      { atomicNumber: 37, symbol: 'Rb', name: 'Рубидий' }
    ],
    fact: "Натрий + хлор = обычная поваренная соль!"
  },
  {
    atomicNumber: 92, symbol: 'U', name: 'Уран',
    properties: ["Используется как ядерное топливо", "Самый тяжёлый природный элемент", "Атомный номер 92", "Радиоактивен"],
    options: [
      { atomicNumber: 92, symbol: 'U', name: 'Уран' },
      { atomicNumber: 94, symbol: 'Pu', name: 'Плутоний' },
      { atomicNumber: 90, symbol: 'Th', name: 'Торий' },
      { atomicNumber: 88, symbol: 'Ra', name: 'Радий' }
    ],
    fact: "Уран — основа атомной энергетики!"
  },
  {
    atomicNumber: 13, symbol: 'Al', name: 'Алюминий', 
    properties: ["Самый распространённый металл в земной коре", "Лёгкий и прочный", "Атомный номер 13", "Используется в самолётах"], 
    options: [{ atomicNumber: 13, symbol: 'Al', name: 'Алюминий' }, { atomicNumber: 26, symbol: 'Fe', name: 'Железо' }, { atomicNumber: 29, symbol: 'Cu', name: 'Медь' }, { atomicNumber: 30, symbol: 'Zn', name: 'Цинк' }], 
    fact: "Алюминий — металл будущего!"
  },
  {
    atomicNumber: 17, symbol: 'Cl', name: 'Хлор', 
    properties: ["Зелёно-жёлтый газ с резким запахом", "Используется для обеззараживания воды", "Атомный номер 17", "Галоген"], 
    options: [{ atomicNumber: 17, symbol: 'Cl', name: 'Хлор' }, { atomicNumber: 9, symbol: 'F', name: 'Фтор' }, { atomicNumber: 35, symbol: 'Br', name: 'Бром' }, { atomicNumber: 53, symbol: 'I', name: 'Йод' }], 
    fact: "Хлор спасает миллионы жизней в воде!"
  },
  {
    atomicNumber: 47, symbol: 'Ag', name: 'Серебро', 
    properties: ["Лучший проводник электричества", "Используется в зеркалах и фото", "Атомный номер 47", "Благородный металл"], 
    options: [{ atomicNumber: 47, symbol: 'Ag', name: 'Серебро' }, { atomicNumber: 79, symbol: 'Au', name: 'Золото' }, { atomicNumber: 29, symbol: 'Cu', name: 'Медь' }, { atomicNumber: 78, symbol: 'Pt', name: 'Платина' }], 
    fact: "Серебро убивает бактерии!"
  },
  {
    atomicNumber: 74, symbol: 'W', name: 'Вольфрам', 
    properties: ["Самая высокая температура плавления", "В нитях лампочек", "Атомный номер 74", "Тугоплавкий металл"], 
    options: [{ atomicNumber: 74, symbol: 'W', name: 'Вольфрам' }, { atomicNumber: 42, symbol: 'Mo', name: 'Молибден' }, { atomicNumber: 73, symbol: 'Ta', name: 'Тантал' }, { atomicNumber: 41, symbol: 'Nb', name: 'Ниобий' }], 
    fact: "Вольфрам — чемпион по жаростойкости!"
  },
  {
    atomicNumber: 82, symbol: 'Pb', name: 'Свинец', 
    properties: ["Очень тяжёлый металл", "Защищает от радиации", "Атомный номер 82", "Используется в аккумуляторах"], 
    options: [{ atomicNumber: 82, symbol: 'Pb', name: 'Свинец' }, { atomicNumber: 50, symbol: 'Sn', name: 'Олово' }, { atomicNumber: 83, symbol: 'Bi', name: 'Висмут' }, { atomicNumber: 81, symbol: 'Tl', name: 'Таллий' }], 
    fact: "Свинец — защита от радиации!"
  }
]

// Простой SVG атом для игры
function GameAtomModel({ atomicNumber, symbol, color = '#8b5cf6' }: { atomicNumber: number; symbol: string; color?: string }) {
  const electrons = Math.min(Math.max(atomicNumber, 1), 20)
  const shells = Math.ceil(Math.sqrt(electrons))

  return (
    <div className="relative w-32 h-32 sm:w-40 sm:h-40 mx-auto">
      <svg width="100%" height="100%" viewBox="0 0 120 120" className="drop-shadow-2xl">
        <circle cx="60" cy="60" r="14" fill="#1e2937" />
        <text x="60" y="65" textAnchor="middle" fill="white" fontSize="11" fontWeight="bold">{symbol}</text>
        {Array.from({ length: shells }, (_, i) => {
          const radius = 24 + i * 14
          return (
            <g key={i}>
              <circle cx="60" cy="60" r={radius} fill="none" stroke="#94a3b8" strokeWidth="2" strokeDasharray="6 3" />
              {Array.from({ length: Math.min(electrons - i * 4, 8) }, (_, j) => {
                const angle = (j * 360) / Math.min(electrons - i * 4, 8) + i * 30
                const x = 60 + radius * Math.cos((angle * Math.PI) / 180)
                const y = 60 + radius * Math.sin((angle * Math.PI) / 180)
                return (
                  <circle key={j} cx={x} cy={y} r="4" fill={color} className="animate-pulse" />
                )
              })}
            </g>
          )
        })}
      </svg>
    </div>
  )
}

// Компонент игры
function PeriodicTableGame({ onClose }: { onClose: () => void }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [wrongCount, setWrongCount] = useState(0)
  const [gameOver, setGameOver] = useState(false)
  const [showCorrectElement, setShowCorrectElement] = useState(false)
  const [displayedElement, setDisplayedElement] = useState<typeof elements[0] | null>(null)

  const [questions] = useState<Question[]>(() => 
    [...questionsPool].sort(() => Math.random() - 0.5).slice(0, 10)
  )

  const current = questions[currentIndex]
  const progress = Math.round(((currentIndex + 1) / questions.length) * 100)
  
  // Перемешиваем варианты для текущего вопроса
  const shuffledOptions = useMemo(() => {
    if (!current) return []
    return [...current.options].sort(() => Math.random() - 0.5)
  }, [current])

  const handleAnswer = (chosenAtomic: number) => {
    const isCorrect = chosenAtomic === current.atomicNumber
    
    if (isCorrect) {
      setScore(s => s + 1)
      // Находим элемент и сохраняем его для показа
      const element = elements.find(el => el.atomicNumber === current.atomicNumber)
      if (element) {
        setDisplayedElement(element)
        setShowCorrectElement(true)
        // Не переходим автоматически - ждём нажатия кнопки
      }
    } else {
      setWrongCount(w => w + 1)
      // При неправильном ответе сразу переходим
      if (currentIndex < questions.length - 1) {
        setCurrentIndex(i => i + 1)
      } else {
        setGameOver(true)
      }
    }
  }

  const handleNextQuestion = () => {
    setShowCorrectElement(false)
    setDisplayedElement(null)
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(i => i + 1)
    } else {
      setGameOver(true)
    }
  }

  const restart = () => {
    setCurrentIndex(0)
    setScore(0)
    setWrongCount(0)
    setGameOver(false)
    setShowCorrectElement(false)
    setDisplayedElement(null)
  }

  if (gameOver) {
    const passed = score >= 6
    const stars = score >= 9 ? 3 : score >= 7 ? 2 : score >= 6 ? 1 : 0
    
    return (
      <div className="text-center py-8 sm:py-12 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl border border-white/10">
        <div className="text-6xl sm:text-8xl mb-4">{passed ? '🧪' : '📚'}</div>
        <h2 className={`text-2xl sm:text-4xl font-bold ${passed ? 'text-amber-400' : 'text-red-400'}`}>
          {passed ? 'Отлично!' : 'Попробуй ещё!'}
        </h2>
        
        {/* Статистика */}
        <div className="mt-6 flex justify-center gap-4 sm:gap-8">
          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-xl px-4 sm:px-6 py-3 sm:py-4">
            <div className="text-3xl sm:text-4xl font-bold text-emerald-400">{score}</div>
            <div className="text-xs sm:text-sm text-emerald-300/70">Правильно</div>
          </div>
          <div className="bg-red-500/10 border border-red-500/30 rounded-xl px-4 sm:px-6 py-3 sm:py-4">
            <div className="text-3xl sm:text-4xl font-bold text-red-400">{wrongCount}</div>
            <div className="text-xs sm:text-sm text-red-300/70">Ошибок</div>
          </div>
        </div>
        
        {/* Звёзды */}
        {passed && (
          <div className="flex justify-center gap-4 sm:gap-6 text-5xl sm:text-7xl my-6 sm:my-8">
            {Array.from({ length: 3 }, (_, i) => (
              <span key={i} className={i < stars ? 'text-yellow-400' : 'text-white/20'}>⭐</span>
            ))}
          </div>
        )}
        
        <p className="text-sm sm:text-base text-white/60 mt-4">
          {passed 
            ? `Результат: ${score} из ${questions.length}` 
            : `Нужно минимум 6 правильных ответов`}
        </p>

        <div className="flex flex-col sm:flex-row gap-3 justify-center px-4 mt-6">
          <button
            onClick={restart}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white text-lg sm:text-xl font-bold rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Играть снова
          </button>
          <button
            onClick={onClose}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-white/10 hover:bg-white/20 text-white text-lg sm:text-xl rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Закрыть
          </button>
        </div>
      </div>
    )
  }

  // Показ правильного элемента при правильном ответе
  if (showCorrectElement && displayedElement) {
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="p-4 sm:p-8 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl sm:rounded-3xl border border-white/10 text-center"
      >
        <div className="text-emerald-400 text-lg sm:text-xl font-bold mb-4 flex items-center justify-center gap-2">
          <span>✓</span> Правильно!
        </div>
        
        {/* Карточка элемента */}
        <div className={`inline-block p-4 sm:p-6 rounded-2xl ${categoryColors[displayedElement.category]} shadow-2xl`}>
          <div className="text-xs opacity-70">#{displayedElement.atomicNumber}</div>
          <div className="text-5xl sm:text-7xl font-black text-white my-2">{displayedElement.symbol}</div>
          <div className="text-lg sm:text-xl font-bold text-white">{displayedElement.nameRu}</div>
          <div className="text-sm opacity-80">{displayedElement.atomicMass}</div>
        </div>
        
        {/* Мини-визуализация атома */}
        <div className="mt-4 flex justify-center">
          <div className="w-24 h-24 sm:w-32 sm:h-32">
            <AtomVisualization 
              atomicNumber={displayedElement.atomicNumber}
              category={displayedElement.category}
              symbol={displayedElement.symbol}
            />
          </div>
        </div>
        
        {/* Электронная конфигурация */}
        <div className="mt-4 max-w-xs mx-auto">
          <ElectronConfigDisplay atomicNumber={displayedElement.atomicNumber} />
        </div>
        
        <button
          onClick={handleNextQuestion}
          className="mt-6 px-8 py-3 bg-white/10 hover:bg-white/20 text-white font-bold rounded-full transition-all active:scale-95"
        >
          Следующий вопрос
        </button>
      </motion.div>
    )
  }

  return (
    <div className="p-3 sm:p-6 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl sm:rounded-3xl border border-white/10">
      {/* Close button - centered at top */}
      <div className="flex justify-center mb-4">
        <button onClick={onClose} className="px-4 py-1.5 bg-white/10 hover:bg-white/20 rounded-full transition-colors flex items-center gap-2 text-white text-sm font-medium">
          <X className="w-4 h-4" />
          <span>Закрыть</span>
        </button>
      </div>
      
      <div className="flex justify-center items-center mb-4 sm:mb-6 flex-wrap gap-2">
        <h2 className="text-lg sm:text-2xl font-bold text-white">🔍 Угадай элемент</h2>
        <div className="text-xl sm:text-2xl font-mono font-bold text-amber-400">⭐ {score}</div>
      </div>

      {/* Прогресс */}
      <div className="h-2 bg-white/10 rounded-full mb-4 sm:mb-6 overflow-hidden">
        <div className="h-full bg-gradient-to-r from-amber-500 to-orange-500 transition-all" style={{ width: `${progress}%` }} />
      </div>

      {/* Вопрос */}
      <div className="bg-white/5 border border-white/10 rounded-xl sm:rounded-2xl p-3 sm:p-5 mb-4 sm:mb-6">
        <div className="uppercase text-[10px] sm:text-xs text-amber-400 tracking-widest mb-2 sm:mb-3">ЧТО ЗА ЭЛЕМЕНТ?</div>
        <ul className="space-y-1.5 sm:space-y-3 text-sm sm:text-lg text-white/90">
          {current.properties.map((prop, i) => (
            <li key={i} className="flex gap-2 sm:gap-3">
              <span className="text-amber-400">•</span> {prop}
            </li>
          ))}
        </ul>
      </div>

      {/* Варианты */}
      <div className="grid grid-cols-2 gap-2 sm:gap-4">
        {shuffledOptions.map((opt, idx) => (
          <button
            key={idx}
            onClick={() => handleAnswer(opt.atomicNumber)}
            className="group relative flex flex-col items-center justify-center border-2 border-white/20 hover:border-amber-400 hover:bg-white/5 rounded-xl sm:rounded-2xl py-3 sm:py-6 transition-all active:scale-95"
          >
            <div className="text-3xl sm:text-5xl font-black mb-1 text-white group-hover:text-amber-400 transition-colors">
              {opt.symbol}
            </div>
            <div className="text-xs sm:text-base font-medium text-white/80 text-center">{opt.name}</div>
          </button>
        ))}
      </div>

      <div className="mt-4 sm:mt-6 text-center text-[10px] sm:text-xs text-white/40">
        10 вопросов • Минимум 6 правильных для победы!
      </div>
    </div>
  )
}

// ==================== ИГРА 2: MEMORY — ПАРЫ ЭЛЕМЕНТОВ ====================
type MemoryCard = {
  id: number
  atomicNumber: number
  type: 'symbol' | 'name'
  content: string
  color: string
}

function PeriodicTableMemoryGame({ onClose }: { onClose: () => void }) {
  const [cards, setCards] = useState<MemoryCard[]>([])
  const [flipped, setFlipped] = useState<number[]>([])
  const [matched, setMatched] = useState<number[]>([])
  const [moves, setMoves] = useState(0)
  const [showFact, setShowFact] = useState<{ atomicNumber: number; symbol: string; name: string; category: string } | null>(null)
  const [gameOver, setGameOver] = useState(false)

  const totalPairs = 8 // 16 карт для мобильной версии

  // Генерируем игру при старте
  useEffect(() => {
    initGame()
  }, [])

  const initGame = () => {
    // Выбираем случайные элементы
    const shuffled = [...elements]
      .filter(el => el.atomicNumber <= 86)
      .sort(() => Math.random() - 0.5)
      .slice(0, totalPairs)

    const newCards: MemoryCard[] = []

    shuffled.forEach((el, index) => {
      const color = categoryHexColors[el.category] || '#6b7280'
      
      newCards.push({
        id: index * 2,
        atomicNumber: el.atomicNumber,
        type: 'symbol',
        content: el.symbol,
        color
      })
      newCards.push({
        id: index * 2 + 1,
        atomicNumber: el.atomicNumber,
        type: 'name',
        content: el.nameRu,
        color
      })
    })

    const shuffledCards = [...newCards].sort(() => Math.random() - 0.5)
    setCards(shuffledCards)
    setFlipped([])
    setMatched([])
    setMoves(0)
    setGameOver(false)
    setShowFact(null)
  }

  const handleCardClick = (index: number) => {
    if (flipped.length === 2 || flipped.includes(index) || matched.includes(cards[index].atomicNumber)) return

    const newFlipped = [...flipped, index]
    setFlipped(newFlipped)

    if (newFlipped.length === 2) {
      setMoves(moves + 1)

      const [first, second] = newFlipped
      const card1 = cards[first]
      const card2 = cards[second]

      if (card1.atomicNumber === card2.atomicNumber) {
        setMatched(prev => [...prev, card1.atomicNumber])

        const element = elements.find(el => el.atomicNumber === card1.atomicNumber)
        if (element) {
          setShowFact({
            atomicNumber: card1.atomicNumber,
            symbol: element.symbol,
            name: element.nameRu,
            category: element.category
          })
        }

        // Не скрываем автоматически - ждём нажатия кнопки
        setFlipped([])
      } else {
        setTimeout(() => setFlipped([]), 800)
      }
    }
  }

  const restart = () => initGame()

  const matchedCount = matched.length
  const progress = Math.round((matchedCount / totalPairs) * 100)

  if (gameOver) {
    const stars = moves <= 12 ? 3 : moves <= 18 ? 2 : 1
    return (
      <div className="text-center py-8 sm:py-12 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl border border-white/10">
        <div className="text-6xl sm:text-8xl mb-4">🧠</div>
        <h2 className="text-2xl sm:text-4xl font-bold text-violet-400">Память на высоте!</h2>
        <p className="text-lg sm:text-xl mt-2 text-white/80">Ходов: {moves}</p>
        
        <div className="flex justify-center gap-4 sm:gap-6 text-5xl sm:text-7xl my-6 sm:my-8">
          {Array.from({ length: 3 }, (_, i) => (
            <span key={i} className={i < stars ? 'text-yellow-400' : 'text-white/20'}>⭐</span>
          ))}
        </div>

        <div className="flex flex-col sm:flex-row gap-3 justify-center px-4 mt-6">
          <button
            onClick={restart}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-gradient-to-r from-violet-500 to-purple-500 hover:from-violet-600 hover:to-purple-600 text-white text-lg sm:text-xl font-bold rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Играть снова
          </button>
          <button
            onClick={onClose}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-white/10 hover:bg-white/20 text-white text-lg sm:text-xl rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Закрыть
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="p-3 sm:p-6 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl sm:rounded-3xl border border-white/10">
      {/* Close button - centered at top */}
      <div className="flex justify-center mb-4">
        <button onClick={onClose} className="px-4 py-1.5 bg-white/10 hover:bg-white/20 rounded-full transition-colors flex items-center gap-2 text-white text-sm font-medium">
          <X className="w-4 h-4" />
          <span>Закрыть</span>
        </button>
      </div>
      
      <div className="flex justify-center items-center mb-4 sm:mb-6 flex-wrap gap-2">
        <h2 className="text-lg sm:text-2xl font-bold text-white">🧠 Мемори: Пары</h2>
        <div className="text-xl sm:text-2xl font-mono font-bold text-violet-400">🃏 {matchedCount}/{totalPairs}</div>
      </div>

      {/* Прогресс */}
      <div className="h-2 bg-white/10 rounded-full mb-4 sm:mb-6 overflow-hidden">
        <div className="h-full bg-gradient-to-r from-violet-500 to-purple-500 transition-all" style={{ width: `${progress}%` }} />
      </div>

      {/* Игровое поле */}
      <div className="grid grid-cols-4 gap-2 sm:gap-3">
        {cards.map((card, index) => {
          const isFlipped = flipped.includes(index) || matched.includes(card.atomicNumber)
          return (
            <button
              key={card.id}
              onClick={() => handleCardClick(index)}
              className={`relative w-full aspect-[4/3] cursor-pointer transition-all duration-500 rounded-xl sm:rounded-2xl overflow-hidden ${
                isFlipped ? '' : 'hover:scale-105'
              }`}
            >
              {isFlipped ? (
                <div 
                  className={`absolute inset-0 flex flex-col items-center justify-center border-2 ${
                    matched.includes(card.atomicNumber) 
                      ? 'bg-emerald-500/20 border-emerald-500/50' 
                      : 'bg-white/10 border-white/30'
                  }`}
                  style={{ backgroundColor: matched.includes(card.atomicNumber) ? undefined : `${card.color}20` }}
                >
                  {card.type === 'symbol' ? (
                    <>
                      <div className="text-2xl sm:text-4xl font-black" style={{ color: card.color }}>
                        {card.content}
                      </div>
                      <div className="text-[10px] sm:text-xs text-white/50">№ {card.atomicNumber}</div>
                    </>
                  ) : (
                    <>
                      <div className="text-xs sm:text-sm font-semibold text-center px-1" style={{ color: card.color }}>
                        {card.content}
                      </div>
                      <div className="text-[10px] text-white/40 mt-1">название</div>
                    </>
                  )}
                </div>
              ) : (
                <div className="absolute inset-0 bg-gradient-to-br from-slate-700 to-slate-900 flex items-center justify-center border-2 border-slate-600">
                  <div className="text-2xl sm:text-3xl opacity-30">⚗️</div>
                </div>
              )}
            </button>
          )
        })}
      </div>

      {/* Модальное окно с фактом */}
      {showFact && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4"
        >
          <motion.div
            initial={{ scale: 0.9 }}
            animate={{ scale: 1 }}
            className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl max-w-sm w-full p-6 text-center border border-white/10"
          >
            {/* 3D модель атома */}
            <div className="w-32 h-32 sm:w-40 sm:h-40 mx-auto">
              <AtomVisualization
                atomicNumber={showFact.atomicNumber}
                category={showFact.category}
                symbol={showFact.symbol}
              />
            </div>
            <div className="mt-4 text-2xl font-bold text-white">{showFact.name}</div>
            <div className="text-violet-400">№ {showFact.atomicNumber}</div>
            <p className="mt-4 text-emerald-400 font-medium">✓ Пара найдена!</p>
            
            <button
              onClick={() => {
                setShowFact(null)
                // Проверка победы
                if (matched.length === totalPairs) {
                  setTimeout(() => setGameOver(true), 300)
                }
              }}
              className="mt-6 px-8 py-3 bg-white/10 hover:bg-white/20 text-white font-bold rounded-full transition-all active:scale-95"
            >
              Продолжить
            </button>
          </motion.div>
        </motion.div>
      )}

      <div className="mt-4 sm:mt-6 text-center text-[10px] sm:text-xs text-white/40">
        8 пар • Меньше 13 ходов = 3 звезды!
      </div>
    </div>
  )
}

// ==================== ИГРА 3: СОБЕРИ ТАБЛИЦУ ПО ГРУППАМ ====================
function PeriodicTableBuildGame({ onClose }: { onClose: () => void }) {
  const [placed, setPlaced] = useState<Record<number, boolean>>({})
  const [activeElement, setActiveElement] = useState<typeof elements[0] | null>(null)
  const [mistakes, setMistakes] = useState(0)
  const [gameOver, setGameOver] = useState(false)
  const [showFact, setShowFact] = useState<{ el: typeof elements[0]; message: string } | null>(null)
  const [level, setLevel] = useState(1)
  const [highlightedSlots, setHighlightedSlots] = useState<Set<string>>(new Set())

  // Уровни сложности: сколько ячеек подсвечивать
  const getHintsCount = (lvl: number) => {
    const hints = [2, 3, 5, 7, 10, 15, 20]
    return hints[Math.min(lvl - 1, hints.length - 1)]
  }

  // Фильтруем только основную таблицу (без лантаноидов и актиноидов)
  const mainElements = useMemo(() => {
    return elements.filter(
      el => !(el.atomicNumber >= 58 && el.atomicNumber <= 71) && !(el.atomicNumber >= 90 && el.atomicNumber <= 103)
    )
  }, [])

  const total = mainElements.length
  const placedCount = Object.keys(placed).length
  const progress = Math.round((placedCount / total) * 100)

  // Перемешанные элементы для нижней панели
  const [remaining, setRemaining] = useState<typeof elements>([])

  useEffect(() => {
    setRemaining([...mainElements].sort(() => Math.random() - 0.5))
  }, [mainElements])

  // Создаём карту: позиция `${period}-${group}` → элемент
  const positionMap = useMemo(() => {
    const map: Record<string, typeof elements[0]> = {}
    mainElements.forEach(el => {
      const key = `${el.period}-${el.group}`
      map[key] = el
    })
    return map
  }, [mainElements])

  // Все валидные позиции в таблице
  const validPositions = useMemo(() => {
    return Object.keys(positionMap)
  }, [positionMap])

  // Обновляем уровень при прогрессе
  useEffect(() => {
    const newLevel = Math.floor(placedCount / 15) + 1
    if (newLevel !== level && newLevel <= 7) {
      setLevel(newLevel)
    }
  }, [placedCount, level])

  const handleSlotClick = (period: number, group: number) => {
    if (!activeElement) return

    const key = `${period}-${group}`
    const targetElement = positionMap[key]

    if (targetElement && targetElement.atomicNumber === activeElement.atomicNumber) {
      // Правильно!
      setPlaced(prev => ({ ...prev, [activeElement.atomicNumber]: true }))

      // Убираем из remaining
      setRemaining(prev => prev.filter(el => el.atomicNumber !== activeElement.atomicNumber))

      // Показываем красивый факт + атом
      const facts = [
        "Отлично! Этот элемент в правильной группе.",
        "Супер! Ты знаешь таблицу!",
        "Круто! Теперь он на своём месте.",
        "Молодец! Химия — это просто.",
      ]
      setShowFact({
        el: activeElement,
        message: facts[Math.floor(Math.random() * facts.length)]
      })

      setActiveElement(null)
      setHighlightedSlots(new Set())

      // Проверка победы
      if (placedCount + 1 === total) {
        setTimeout(() => {
          setGameOver(true)
        }, 800)
      }
    } else if (targetElement && highlightedSlots.has(key)) {
      // Неправильно (клик по подсвеченной ячейке)
      setMistakes(prev => prev + 1)
    }
  }

  const handleElementClick = (el: typeof elements[0]) => {
    if (activeElement?.atomicNumber === el.atomicNumber) {
      setActiveElement(null)
      setHighlightedSlots(new Set())
    } else {
      setActiveElement(el)
      
      // Генерируем подсвеченные ячейки: правильная + случайные неправильные
      const hintsCount = getHintsCount(level)
      const correctKey = `${el.period}-${el.group}`
      const slots = new Set<string>([correctKey])
      
      // Добавляем случайные неправильные позиции
      const emptyPositions = validPositions.filter(pos => {
        const targetEl = positionMap[pos]
        return !placed[targetEl.atomicNumber] && pos !== correctKey
      })
      
      const shuffled = emptyPositions.sort(() => Math.random() - 0.5)
      shuffled.slice(0, hintsCount - 1).forEach(pos => slots.add(pos))
      
      setHighlightedSlots(slots)
    }
  }

  const restart = () => {
    setPlaced({})
    setActiveElement(null)
    setMistakes(0)
    setGameOver(false)
    setShowFact(null)
    setLevel(1)
    setHighlightedSlots(new Set())
    setRemaining([...mainElements].sort(() => Math.random() - 0.5))
  }

  if (gameOver) {
    const stars = mistakes === 0 ? 3 : mistakes <= 5 ? 2 : 1
    return (
      <div className="text-center py-8 sm:py-12 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl border border-white/10">
        <div className="text-6xl sm:text-8xl mb-4">🧩</div>
        <h2 className="text-2xl sm:text-4xl font-bold text-emerald-400">Таблица собрана!</h2>
        <p className="text-lg sm:text-xl mt-2 text-white/80">Ошибок: {mistakes}</p>

        <div className="flex justify-center gap-4 sm:gap-6 text-5xl sm:text-7xl my-6 sm:my-8">
          {Array.from({ length: 3 }, (_, i) => (
            <span key={i} className={i < stars ? 'text-yellow-400' : 'text-white/20'}>⭐</span>
          ))}
        </div>

        <div className="flex flex-col sm:flex-row gap-3 justify-center px-4 mt-6">
          <button
            onClick={restart}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-gradient-to-r from-emerald-500 to-green-500 hover:from-emerald-600 hover:to-green-600 text-white text-lg sm:text-xl font-bold rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Собрать заново
          </button>
          <button
            onClick={onClose}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-white/10 hover:bg-white/20 text-white text-lg sm:text-xl rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Закрыть
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="p-3 sm:p-6 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl sm:rounded-3xl border border-white/10">
      {/* Close button - centered at top */}
      <div className="flex justify-center mb-4">
        <button onClick={onClose} className="px-4 py-1.5 bg-white/10 hover:bg-white/20 rounded-full transition-colors flex items-center gap-2 text-white text-sm font-medium">
          <X className="w-4 h-4" />
          <span>Закрыть</span>
        </button>
      </div>
      
      <div className="flex justify-center items-center mb-4 sm:mb-6 flex-wrap gap-2">
        <h2 className="text-lg sm:text-2xl font-bold text-white">🧩 Собери таблицу</h2>
        <div className="text-xl sm:text-2xl font-mono font-bold text-emerald-400">⭐ {placedCount}/{total}</div>
        <div className="text-xs sm:text-sm bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">Уровень {level}</div>
        <div className="text-xs sm:text-sm text-red-400">Ошибки: {mistakes}</div>
      </div>

      {/* Прогресс */}
      <div className="h-2 bg-white/10 rounded-full mb-4 sm:mb-6 overflow-hidden">
        <div
          className="h-full bg-gradient-to-r from-emerald-500 to-green-500 transition-all duration-700"
          style={{ width: `${progress}%` }}
        />
      </div>

      {/* ТАБЛИЦА (пустые ячейки кликабельны) */}
      <div className="relative overflow-x-auto mb-4 sm:mb-6 -mx-2 px-2">
        <div
          className="grid gap-0.5 sm:gap-1 text-center min-w-[600px] sm:min-w-[800px]"
          style={{ gridTemplateColumns: 'repeat(18, minmax(32px, 1fr))', gridTemplateRows: 'repeat(7, 40px)' }}
        >
          {Array.from({ length: 7 }, (_, p) => {
            const period = p + 1
            return Array.from({ length: 18 }, (_, g) => {
              const group = g + 1
              const key = `${period}-${group}`
              const target = positionMap[key]
              const isPlaced = target && placed[target.atomicNumber]
              const isHighlighted = highlightedSlots.has(key)

              return (
                <div
                  key={key}
                  id={`slot-${period}-${group}`}
                  onClick={() => handleSlotClick(period, group)}
                  className={`flex flex-col items-center justify-center border rounded-md transition-all cursor-pointer select-none
                    ${isPlaced
                      ? `${categoryColors[target.category]} text-white border-transparent shadow-inner`
                      : isHighlighted
                        ? 'border-2 border-amber-400 bg-amber-500/20 hover:bg-amber-500/30 animate-pulse'
                        : target
                          ? 'border-dashed border-white/30 hover:border-white/50 hover:bg-white/5'
                          : 'opacity-20 pointer-events-none border-transparent'}
                    `}
                >
                  {isPlaced && target ? (
                    <>
                      <div className="text-[8px] opacity-70">{target.atomicNumber}</div>
                      <div className="text-sm sm:text-lg font-black text-white">{target.symbol}</div>
                    </>
                  ) : isHighlighted ? (
                    <div className="text-lg sm:text-xl text-amber-400 font-light">?</div>
                  ) : target ? (
                    <div className="text-lg sm:text-xl text-white/30 font-light">+</div>
                  ) : null}
                </div>
              )
            })
          })}
        </div>
      </div>

      {/* ПАНЕЛЬ ОСТАВШИХСЯ ЭЛЕМЕНТОВ */}
      <div className="bg-white/5 rounded-xl sm:rounded-2xl p-3 sm:p-4 border border-white/10">
        <div className="uppercase text-[10px] sm:text-xs tracking-widest text-white/40 mb-3 text-center">
          Выбери элемент и поставь на место ↓
        </div>
        <div className="grid grid-cols-6 sm:grid-cols-8 md:grid-cols-10 lg:grid-cols-12 gap-1.5 sm:gap-2">
          {remaining.map(el => {
            const isActive = activeElement?.atomicNumber === el.atomicNumber
            return (
              <div
                key={el.atomicNumber}
                onClick={() => handleElementClick(el)}
                className={`group flex flex-col items-center justify-center border-2 rounded-lg py-1.5 sm:py-2 cursor-pointer transition-all active:scale-95
                  ${isActive
                    ? `${categoryColors[el.category]} border-transparent ring-2 ring-white/50`
                    : 'border-white/20 hover:border-white/40 hover:bg-white/5'}`}
              >
                <div className="text-[8px] sm:text-[10px] text-white/50">{el.atomicNumber}</div>
                <div className="text-lg sm:text-2xl font-bold text-white group-hover:scale-110 transition-transform">
                  {el.symbol}
                </div>
              </div>
            )
          })}
        </div>
      </div>

      {/* МОДАЛЬНОЕ ОКНО С ФАКТОМ И АТОМОМ */}
      {showFact && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4"
          onClick={() => setShowFact(null)}
        >
          <motion.div
            initial={{ scale: 0.9 }}
            animate={{ scale: 1 }}
            onClick={e => e.stopPropagation()}
            className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl max-w-sm w-full p-6 text-center border border-white/10"
          >
            <div className="w-24 h-24 mx-auto">
              <AtomVisualization
                atomicNumber={showFact.el.atomicNumber}
                category={showFact.el.category}
                symbol={showFact.el.symbol}
              />
            </div>
            <div className="mt-4 text-xl sm:text-2xl font-bold text-white">{showFact.el.nameRu}</div>
            <div className="text-emerald-400">№ {showFact.el.atomicNumber} • {showFact.el.atomicMass}</div>
            <p className="mt-4 text-base sm:text-lg text-white/80">{showFact.message}</p>

            <button
              onClick={() => setShowFact(null)}
              className="mt-6 px-8 py-2 bg-white/10 hover:bg-white/20 text-white rounded-xl transition-all"
            >
              Продолжить
            </button>
          </motion.div>
        </motion.div>
      )}

      <div className="mt-4 sm:mt-6 text-center text-[10px] sm:text-xs text-white/40">
        98 элементов • Без ошибок = 3 звезды!
      </div>
    </div>
  )
}

// ==================== ИГРА 4: ДЕТЕКТИВ ПЕРИОДИЧЕСКОЙ ТАБЛИЦЫ ====================
interface DetectiveQuestion {
  hint: string
  correct: number
  fact: string
}

const detectiveQuestions: DetectiveQuestion[] = [
  { hint: "Самый лёгкий элемент во Вселенной", correct: 1, fact: "Водород — основа всех звёзд и 90% массы Вселенной!" },
  { hint: "Благородный газ, которым надувают воздушные шары", correct: 2, fact: "Гелий — легче воздуха и не горит" },
  { hint: "Элемент, из которого состоят алмазы и графит", correct: 6, fact: "Углерод — основа всей органической жизни" },
  { hint: "Газ, которым мы дышим (21% атмосферы)", correct: 8, fact: "Кислород — самый важный для дыхания" },
  { hint: "Элемент с символом Fe, в крови и стали", correct: 26, fact: "Железо — самый распространённый элемент в ядре Земли" },
  { hint: "Щелочной металл, который взрывается в воде", correct: 11, fact: "Натрий — входит в состав поваренной соли" },
  { hint: "Драгоценный металл жёлтого цвета", correct: 79, fact: "Золото — один из самых ковких металлов" },
  { hint: "Элемент, используемый как топливо в АЭС", correct: 92, fact: "Уран — самый тяжёлый природный элемент" },
  { hint: "Благородный газ в третьем периоде", correct: 18, fact: "Аргон — используется в лампах накаливания" },
  { hint: "Металл с самой высокой температурой плавления", correct: 74, fact: "Вольфрам — в нитях обычных лампочек" },
]

function PeriodicTableDetectiveGame({ onClose }: { onClose: () => void }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [score, setScore] = useState(0)
  const [wrongCount, setWrongCount] = useState(0)
  const [gameOver, setGameOver] = useState(false)
  const [feedback, setFeedback] = useState<'correct' | 'wrong' | null>(null)
  const [selected, setSelected] = useState<number | null>(null)
  const [showCorrectModal, setShowCorrectModal] = useState(false)

  const [questions] = useState<DetectiveQuestion[]>(() => 
    [...detectiveQuestions].sort(() => Math.random() - 0.5)
  )

  const current = questions[currentIndex]
  const progress = Math.round(((currentIndex) / questions.length) * 100)

  const currentElement = elements.find(el => el.atomicNumber === current.correct)

  // Фильтруем только основную таблицу (без лантаноидов и актиноидов)
  const mainElements = useMemo(() => {
    return elements.filter(
      el => !(el.atomicNumber >= 58 && el.atomicNumber <= 71) && !(el.atomicNumber >= 90 && el.atomicNumber <= 103)
    )
  }, [])

  const handleElementClick = (atomicNumber: number) => {
    if (feedback) return // Уже есть обратная связь
    
    setSelected(atomicNumber)

    if (atomicNumber === current.correct) {
      setFeedback('correct')
      setScore(s => s + 1)
      setShowCorrectModal(true)
      // Не переходим автоматически - ждём нажатия кнопки
    } else {
      setFeedback('wrong')
      setWrongCount(w => w + 1)
      setTimeout(() => {
        setFeedback(null)
        setSelected(null)
      }, 600)
    }
  }

  const handleNextQuestion = () => {
    setShowCorrectModal(false)
    setFeedback(null)
    setSelected(null)
    
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(i => i + 1)
    } else {
      setGameOver(true)
    }
  }

  const restart = () => {
    setCurrentIndex(0)
    setScore(0)
    setWrongCount(0)
    setGameOver(false)
    setFeedback(null)
    setSelected(null)
    setShowCorrectModal(false)
  }

  if (gameOver) {
    const passed = score >= 6
    const stars = score >= 9 ? 3 : score >= 7 ? 2 : score >= 6 ? 1 : 0
    
    return (
      <div className="text-center py-8 sm:py-12 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl border border-white/10">
        <div className="text-6xl sm:text-8xl mb-4">{passed ? '🏆' : '📚'}</div>
        <h2 className={`text-2xl sm:text-4xl font-bold ${passed ? 'text-cyan-400' : 'text-red-400'}`}>
          {passed ? 'Миссия выполнена!' : 'Попробуй ещё!'}
        </h2>
        
        <div className="mt-6 flex justify-center gap-4 sm:gap-8">
          <div className="bg-cyan-500/10 border border-cyan-500/30 rounded-xl px-4 sm:px-6 py-3 sm:py-4">
            <div className="text-3xl sm:text-4xl font-bold text-cyan-400">{score}</div>
            <div className="text-xs sm:text-sm text-cyan-300/70">Правильно</div>
          </div>
          <div className="bg-red-500/10 border border-red-500/30 rounded-xl px-4 sm:px-6 py-3 sm:py-4">
            <div className="text-3xl sm:text-4xl font-bold text-red-400">{wrongCount}</div>
            <div className="text-xs sm:text-sm text-red-300/70">Ошибок</div>
          </div>
        </div>
        
        {passed && (
          <div className="flex justify-center gap-4 sm:gap-6 text-5xl sm:text-7xl my-6 sm:my-8">
            {Array.from({ length: 3 }, (_, i) => (
              <span key={i} className={i < stars ? 'text-yellow-400' : 'text-white/20'}>⭐</span>
            ))}
          </div>
        )}
        
        <p className="text-sm sm:text-base text-white/60 mt-4">
          {passed ? `Результат: ${score} из ${questions.length}` : `Нужно минимум 6 правильных ответов`}
        </p>

        <div className="flex flex-col sm:flex-row gap-3 justify-center px-4 mt-6">
          <button
            onClick={restart}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white text-lg sm:text-xl font-bold rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Играть снова
          </button>
          <button
            onClick={onClose}
            className="px-8 sm:px-12 py-3 sm:py-4 bg-white/10 hover:bg-white/20 text-white text-lg sm:text-xl rounded-xl sm:rounded-2xl transition-all active:scale-95"
          >
            Закрыть
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="p-3 sm:p-4 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl border border-white/10">
      {/* Close button */}
      <div className="flex justify-center mb-4">
        <button onClick={onClose} className="px-4 py-1.5 bg-white/10 hover:bg-white/20 rounded-full transition-colors flex items-center gap-2 text-white text-sm font-medium">
          <X className="w-4 h-4" />
          <span>Закрыть</span>
        </button>
      </div>

      {/* Header */}
      <div className="flex justify-center items-center mb-4 flex-wrap gap-2">
        <h2 className="text-lg sm:text-2xl font-bold text-white">🕵️ Детектив</h2>
        <div className="text-xl sm:text-2xl font-mono font-bold text-cyan-400">⭐ {score}</div>
        <div className="text-xs sm:text-sm text-red-400">Ошибки: {wrongCount}</div>
      </div>

      {/* Progress */}
      <div className="h-2 bg-white/10 rounded-full mb-4 overflow-hidden">
        <div className="h-full bg-gradient-to-r from-cyan-500 to-blue-500 transition-all" style={{ width: `${progress}%` }} />
      </div>

      {/* Hint */}
      <div className="bg-gradient-to-r from-cyan-500/10 to-blue-500/10 border border-cyan-500/30 rounded-xl p-4 mb-4 text-center">
        <div className="uppercase text-[10px] tracking-widest text-cyan-400 mb-2">ПОДСКАЗКА</div>
        <div className="text-lg sm:text-xl font-medium text-white">{current.hint}</div>
      </div>

      {/* Periodic Table Grid */}
      <div className="relative overflow-x-auto -mx-2 px-2">
        <div
          className="grid gap-0.5 sm:gap-1 text-center min-w-[600px] sm:min-w-[700px]"
          style={{ gridTemplateColumns: 'repeat(18, minmax(28px, 1fr))', gridTemplateRows: 'repeat(7, 36px)' }}
        >
          {mainElements.map(el => {
            const isSelected = selected === el.atomicNumber
            const isCorrect = feedback === 'correct' && el.atomicNumber === current.correct
            const isWrong = feedback === 'wrong' && isSelected

            return (
              <div
                key={el.atomicNumber}
                onClick={() => handleElementClick(el.atomicNumber)}
                style={{ gridColumn: el.group, gridRow: el.period }}
                className={`group flex flex-col items-center justify-center border rounded-md cursor-pointer transition-all
                  ${isCorrect ? 'ring-2 ring-emerald-400 bg-emerald-500/30 scale-110 z-10' : ''}
                  ${isWrong ? 'ring-2 ring-red-400 bg-red-500/30' : ''}
                  ${isSelected && !isCorrect && !isWrong ? 'ring-2 ring-cyan-400 bg-cyan-500/20' : ''}
                  ${!feedback ? 'hover:bg-white/10 border-white/20' : 'border-white/10'}
                  ${categoryColors[el.category]}`}
              >
                <div className="text-[8px] opacity-70">{el.atomicNumber}</div>
                <div className="text-xs sm:text-sm font-bold text-white">{el.symbol}</div>
              </div>
            )
          })}
        </div>
      </div>

      <div className="mt-4 text-center text-[10px] sm:text-xs text-white/40">
        Найди элемент в таблице! • {currentIndex + 1} из {questions.length}
      </div>

      {/* Modal for correct answer */}
      {showCorrectModal && currentElement && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4"
        >
          <motion.div
            initial={{ scale: 0.9 }}
            animate={{ scale: 1 }}
            className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl max-w-sm w-full p-6 text-center border border-white/10"
          >
            {/* 3D модель атома */}
            <div className="w-28 h-28 sm:w-32 sm:h-32 mx-auto">
              <AtomVisualization
                atomicNumber={currentElement.atomicNumber}
                category={currentElement.category}
                symbol={currentElement.symbol}
              />
            </div>
            <div className="mt-4 text-xl sm:text-2xl font-bold text-white">{currentElement.nameRu}</div>
            <div className="text-cyan-400">№ {currentElement.atomicNumber} • {currentElement.atomicMass}</div>
            <p className="mt-4 text-base sm:text-lg text-white/80">{current.fact}</p>
            <p className="mt-2 text-emerald-400 font-medium">✓ Правильно!</p>
            
            <button
              onClick={handleNextQuestion}
              className="mt-6 px-8 py-3 bg-white/10 hover:bg-white/20 text-white font-bold rounded-full transition-all active:scale-95"
            >
              {currentIndex < questions.length - 1 ? 'Следующий вопрос' : 'Результаты'}
            </button>
          </motion.div>
        </motion.div>
      )}
    </div>
  )
}

interface Props {
  onClose?: () => void
}

export default function PeriodicTable({ onClose }: Props) {
  const [selectedElement, setSelectedElement] = useState<typeof elements[0] | null>(null)
  const [showGame, setShowGame] = useState(false)
  const [showMemoryGame, setShowMemoryGame] = useState(false)
  const [showBuildGame, setShowBuildGame] = useState(false)
  const [showDetectiveGame, setShowDetectiveGame] = useState(false)

  // Позиции элементов в сетке
  const getElementPosition = (el: typeof elements[0]) => {
    const group = el.group
    const period = el.period

    // Лантаноиды (57-71) идут под таблицей
    if (el.atomicNumber >= 57 && el.atomicNumber <= 71) {
      return { row: 9, col: el.atomicNumber - 54 }
    }
    // Актиноиды (89-103) идут под таблицей
    if (el.atomicNumber >= 89 && el.atomicNumber <= 103) {
      return { row: 10, col: el.atomicNumber - 86 }
    }

    return { row: period, col: group }
  }

  return (
    <div className="relative w-full">
      {/* Close button - centered at top */}
      {onClose && (
        <div className="flex justify-center mb-4">
          <button
            onClick={onClose}
            className="px-6 py-2 bg-white/10 hover:bg-white/20 rounded-full transition-colors flex items-center gap-2 text-white font-medium"
          >
            <X className="w-5 h-5" />
            <span>Закрыть</span>
          </button>
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-center mb-4 flex-wrap gap-2 sm:gap-3">
        <div className="flex items-center gap-2 sm:gap-3">
          <div className="p-2 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-xl">
            <Atom className="w-5 h-5 sm:w-6 sm:h-6 text-white" />
          </div>
          <h2 className="text-xl sm:text-2xl font-black text-white">Таблица Менделеева</h2>
        </div>
        {/* Кнопки игр */}
        <button
          onClick={() => setShowGame(true)}
          className="flex items-center gap-1 px-2 sm:px-3 py-1 sm:py-1.5 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white text-xs sm:text-sm font-bold rounded-lg sm:rounded-xl transition-all shadow-lg hover:shadow-xl"
        >
          <Gamepad2 className="w-4 h-4" />
          <span className="hidden sm:inline">Угадай</span>
        </button>
        <button
          onClick={() => setShowMemoryGame(true)}
          className="flex items-center gap-1 px-2 sm:px-3 py-1 sm:py-1.5 bg-gradient-to-r from-violet-500 to-purple-500 hover:from-violet-600 hover:to-purple-600 text-white text-xs sm:text-sm font-bold rounded-lg sm:rounded-xl transition-all shadow-lg hover:shadow-xl"
        >
          <span>🧠</span>
          <span className="hidden sm:inline">Мемори</span>
        </button>
        <button
          onClick={() => setShowBuildGame(true)}
          className="flex items-center gap-1 px-2 sm:px-3 py-1 sm:py-1.5 bg-gradient-to-r from-emerald-500 to-green-500 hover:from-emerald-600 hover:to-green-600 text-white text-xs sm:text-sm font-bold rounded-lg sm:rounded-xl transition-all shadow-lg hover:shadow-xl"
        >
          <span>🧩</span>
          <span className="hidden sm:inline">Собери</span>
        </button>
        <button
          onClick={() => setShowDetectiveGame(true)}
          className="flex items-center gap-1 px-2 sm:px-3 py-1 sm:py-1.5 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white text-xs sm:text-sm font-bold rounded-lg sm:rounded-xl transition-all shadow-lg hover:shadow-xl"
        >
          <span>🕵️</span>
          <span className="hidden sm:inline">Детектив</span>
        </button>
      </div>

      {/* Legend */}
      <div className="flex flex-wrap gap-2 mb-4 p-3 bg-white/5 rounded-xl">
        {Object.entries(categoryColors).map(([key, color]) => (
          <div key={key} className="flex items-center gap-1 text-xs">
            <div className={`w-4 h-4 rounded ${color}`} />
            <span className="text-gray-300">{categoryNames[key]}</span>
          </div>
        ))}
      </div>

      {/* Periodic Table Grid */}
      <div className="overflow-x-auto pb-4">
        <div className="grid gap-0.5 min-w-[1200px]" style={{ gridTemplateColumns: 'repeat(18, minmax(48px, 1fr))', gridTemplateRows: 'repeat(10, auto)' }}>
          {elements.map((el) => {
            const pos = getElementPosition(el)
            return (
              <motion.button
                key={el.atomicNumber}
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: el.atomicNumber * 0.003 }}
                onClick={() => setSelectedElement(el)}
                className={`
                  relative p-1 rounded-md transition-all hover:scale-110 hover:z-10 hover:shadow-lg
                  ${categoryColors[el.category]} text-white text-center cursor-pointer
                `}
                style={{
                  gridRow: pos.row,
                  gridColumn: pos.col
                }}
              >
                <div className="text-[8px] opacity-70">{el.atomicNumber}</div>
                <div className="font-bold text-sm">{el.symbol}</div>
                <div className="text-[7px] truncate">{el.nameRu}</div>
              </motion.button>
            )
          })}
        </div>
      </div>

      {/* Element Detail Modal */}
      <AnimatePresence>
        {selectedElement && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-start justify-center bg-black/70 backdrop-blur-sm overflow-y-auto"
            onClick={() => setSelectedElement(null)}
            style={{ paddingTop: 'env(safe-area-inset-top, 10px)', paddingBottom: 'env(safe-area-inset-bottom, 10px)' }}
          >
            <motion.div
              initial={{ scale: 0.9, y: 20 }}
              animate={{ scale: 1, y: 0 }}
              exit={{ scale: 0.9, y: 20 }}
              onClick={(e) => e.stopPropagation()}
              className={`
                w-[95vw] max-w-lg my-2 rounded-2xl shadow-2xl overflow-hidden
                bg-gradient-to-br from-gray-900 to-gray-800 border-2
                ${categoryColors[selectedElement.category].replace('bg-', 'border-')}
              `}
            >
              {/* Header with close button inside */}
              <div className={`relative p-3 sm:p-4 ${categoryColors[selectedElement.category]}`}>
                {/* Close button - centered at top inside header */}
                <div className="flex justify-center -mt-1 mb-2">
                  <button
                    onClick={() => setSelectedElement(null)}
                    className="px-4 py-1.5 bg-black/30 hover:bg-black/50 backdrop-blur-sm border border-white/10 rounded-full transition-colors flex items-center gap-2 text-white text-sm font-medium"
                  >
                    <X className="w-4 h-4" />
                    <span>Закрыть</span>
                  </button>
                </div>
                
                <div className="flex items-center gap-3">
                  <div className="flex-1">
                    <div className="text-xs opacity-80">#{selectedElement.atomicNumber}</div>
                    <h3 className="text-3xl sm:text-4xl font-black">{selectedElement.symbol}</h3>
                    <div className="text-lg sm:text-xl font-bold">{selectedElement.nameRu}</div>
                    <div className="text-xs sm:text-sm opacity-80">{selectedElement.name}</div>
                  </div>
                  <div className="text-right">
                    <div className="text-base sm:text-lg font-bold">{selectedElement.atomicMass}</div>
                    <div className="text-xs sm:text-sm opacity-80">{categoryNames[selectedElement.category]}</div>
                  </div>
                </div>

                {/* 3D Atom Visualization - centered */}
                <div className="mt-2">
                  <AtomVisualization 
                    atomicNumber={selectedElement.atomicNumber}
                    category={selectedElement.category}
                    symbol={selectedElement.symbol}
                  />
                </div>
                
                {/* Electron Configuration - below 3D model */}
                <div className="mt-2">
                  <ElectronConfigDisplay atomicNumber={selectedElement.atomicNumber} />
                </div>
              </div>

              {/* Content */}
              <div className="p-3 sm:p-4 space-y-3 max-h-[50vh] overflow-y-auto">
                {/* Discovery */}
                {selectedElement.discoveredBy && (
                  <div className="bg-white/5 rounded-lg p-2 sm:p-3 border border-white/10">
                    <div className="flex items-center gap-2 text-cyan-400 mb-2 text-sm">
                      <Clock className="w-5 h-5" />
                      <span className="font-medium">Открытие</span>
                    </div>
                    <div className="space-y-2 text-gray-300">
                      <div className="flex items-center gap-2">
                        <User className="w-4 h-4 text-gray-500" />
                        <span>{selectedElement.discoveredBy}</span>
                      </div>
                      {selectedElement.yearDiscovered && (
                        <div className="flex items-center gap-2">
                          <Clock className="w-4 h-4 text-gray-500" />
                          <span>{selectedElement.yearDiscovered}</span>
                        </div>
                      )}
                      {selectedElement.placeDiscovered && (
                        <div className="flex items-center gap-2">
                          <MapPin className="w-4 h-4 text-gray-500" />
                          <span>{selectedElement.placeDiscovered}</span>
                        </div>
                      )}
                    </div>
                  </div>
                )}

                {/* Applications */}
                {selectedElement.applications && selectedElement.applications.length > 0 && (
                  <div className="bg-white/5 rounded-lg p-2 sm:p-3 border border-white/10">
                    <div className="flex items-center gap-2 text-green-400 mb-2 text-sm">
                      <FlaskConical className="w-5 h-5" />
                      <span className="font-medium">Применение</span>
                    </div>
                    <div className="flex flex-wrap gap-2">
                      {selectedElement.applications.map((app, idx) => (
                        <span
                          key={idx}
                          className="px-2 py-0.5 bg-green-500/20 text-green-300 rounded-full text-xs"
                        >
                          {app}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {/* Interesting Facts */}
                {selectedElement.facts && selectedElement.facts.length > 0 && (
                  <div className="bg-white/5 rounded-lg p-2 sm:p-3 border border-white/10">
                    <div className="flex items-center gap-2 text-yellow-400 mb-2 text-sm">
                      <Lightbulb className="w-5 h-5" />
                      <span className="font-medium">Интересные факты</span>
                    </div>
                    <ul className="space-y-2">
                      {selectedElement.facts.map((fact, idx) => (
                        <li key={idx} className="flex items-start gap-2 text-gray-300">
                          <Sparkles className="w-4 h-4 text-yellow-400 mt-0.5 flex-shrink-0" />
                          <span>{fact}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Game Modal */}
      <AnimatePresence>
        {showGame && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 overflow-y-auto bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900"
            onClick={() => setShowGame(false)}
          >
            {/* Animated Background */}
            <div className="fixed inset-0 pointer-events-none overflow-hidden">
              <div className="absolute top-0 left-1/4 w-[500px] h-[500px] bg-purple-500/20 rounded-full blur-[128px] animate-pulse" />
              <div className="absolute bottom-0 right-1/4 w-[400px] h-[400px] bg-pink-500/20 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }} />
              {/* Stars */}
              {Array.from({ length: 50 }, (_, i) => (
                <div
                  key={i}
                  className="absolute rounded-full bg-white animate-sparkle"
                  style={{
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                    width: `${1 + Math.random() * 3}px`,
                    height: `${1 + Math.random() * 3}px`,
                    opacity: 0.2 + Math.random() * 0.5,
                    animationDuration: `${2 + Math.random() * 3}s`,
                    animationDelay: `${Math.random() * 3}s`
                  }}
                />
              ))}
            </div>
            <motion.div
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.95, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
              className="relative z-10 w-full max-w-2xl mx-auto p-4 py-8"
            >
              <PeriodicTableGame onClose={() => setShowGame(false)} />
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Memory Game Modal */}
      <AnimatePresence>
        {showMemoryGame && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 overflow-y-auto bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900"
            onClick={() => setShowMemoryGame(false)}
          >
            {/* Animated Background */}
            <div className="fixed inset-0 pointer-events-none overflow-hidden">
              <div className="absolute top-0 left-1/4 w-[500px] h-[500px] bg-purple-500/20 rounded-full blur-[128px] animate-pulse" />
              <div className="absolute bottom-0 right-1/4 w-[400px] h-[400px] bg-pink-500/20 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }} />
              {/* Stars */}
              {Array.from({ length: 50 }, (_, i) => (
                <div
                  key={i}
                  className="absolute rounded-full bg-white animate-sparkle"
                  style={{
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                    width: `${1 + Math.random() * 3}px`,
                    height: `${1 + Math.random() * 3}px`,
                    opacity: 0.2 + Math.random() * 0.5,
                    animationDuration: `${2 + Math.random() * 3}s`,
                    animationDelay: `${Math.random() * 3}s`
                  }}
                />
              ))}
            </div>
            <motion.div
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.95, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
              className="relative z-10 w-full max-w-lg mx-auto p-4 py-8"
            >
              <PeriodicTableMemoryGame onClose={() => setShowMemoryGame(false)} />
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Build Game Modal */}
      <AnimatePresence>
        {showBuildGame && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 overflow-y-auto bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900"
            onClick={() => setShowBuildGame(false)}
          >
            {/* Animated Background */}
            <div className="fixed inset-0 pointer-events-none overflow-hidden">
              <div className="absolute top-0 left-1/4 w-[500px] h-[500px] bg-purple-500/20 rounded-full blur-[128px] animate-pulse" />
              <div className="absolute bottom-0 right-1/4 w-[400px] h-[400px] bg-pink-500/20 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }} />
              {/* Stars */}
              {Array.from({ length: 50 }, (_, i) => (
                <div
                  key={i}
                  className="absolute rounded-full bg-white animate-sparkle"
                  style={{
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                    width: `${1 + Math.random() * 3}px`,
                    height: `${1 + Math.random() * 3}px`,
                    opacity: 0.2 + Math.random() * 0.5,
                    animationDuration: `${2 + Math.random() * 3}s`,
                    animationDelay: `${Math.random() * 3}s`
                  }}
                />
              ))}
            </div>
            <motion.div
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.95, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
              className="relative z-10 w-full max-w-4xl mx-auto p-4 py-8"
            >
              <PeriodicTableBuildGame onClose={() => setShowBuildGame(false)} />
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Detective Game Modal */}
      <AnimatePresence>
        {showDetectiveGame && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 overflow-y-auto bg-gradient-to-br from-indigo-900 via-cyan-900 to-blue-900"
            onClick={() => setShowDetectiveGame(false)}
          >
            {/* Animated Background */}
            <div className="fixed inset-0 pointer-events-none overflow-hidden">
              <div className="absolute top-0 left-1/4 w-[500px] h-[500px] bg-cyan-500/20 rounded-full blur-[128px] animate-pulse" />
              <div className="absolute bottom-0 right-1/4 w-[400px] h-[400px] bg-blue-500/20 rounded-full blur-[100px] animate-pulse" style={{ animationDelay: '1s' }} />
              {/* Stars */}
              {Array.from({ length: 50 }, (_, i) => (
                <div
                  key={i}
                  className="absolute rounded-full bg-white animate-sparkle"
                  style={{
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                    width: `${1 + Math.random() * 3}px`,
                    height: `${1 + Math.random() * 3}px`,
                    opacity: 0.2 + Math.random() * 0.5,
                    animationDuration: `${2 + Math.random() * 3}s`,
                    animationDelay: `${Math.random() * 3}s`
                  }}
                />
              ))}
            </div>
            <motion.div
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.95, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
              className="relative z-10 w-full max-w-4xl mx-auto p-4 py-8"
            >
              <PeriodicTableDetectiveGame onClose={() => setShowDetectiveGame(false)} />
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}
