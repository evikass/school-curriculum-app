'use client'

import { useMemo, useRef, Suspense } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'
import { OrbitControls, Sphere, Html, Float } from '@react-three/drei'
import * as THREE from 'three'

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
export default function AtomVisualization({ atomicNumber, category, symbol }: { 
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
