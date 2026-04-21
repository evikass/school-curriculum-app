// Асинхронная загрузка данных из JSON-файлов
import { Subject, SubjectData, GameLesson, GradeCurriculum, gradeNames } from './types'

// Кэш загруженных данных
const subjectsCache = new Map<number, SubjectData[]>()
const gamesCache = new Map<number, GameLesson[]>()

// Маппинг предметов для каждого класса (из manifest)
const gradeSubjectKeys: Record<number, string[]> = {
  0: ["art", "craft", "math", "music", "pe", "reading", "russian", "world"],
  1: ["art", "english", "literature", "math", "music", "pe", "reading", "russian", "tech", "world"],
  2: ["art", "english", "literature", "math", "music", "pe", "projects", "russian", "tech", "world"],
  3: ["art", "english", "ethics", "informatics", "literature", "math", "music", "pe", "robotics", "russian", "safety", "tech", "world"],
  4: ["art", "english", "geography", "history", "informatics", "literature", "math", "music", "nature", "pe", "projects", "religion", "russian", "tech", "world"],
  5: ["art", "biology", "crafts", "digital", "english", "finance", "geography", "history", "informatics", "literature", "math", "music", "pe", "robotics", "russian", "safety", "tech"],
  6: ["art", "biology", "chemistry", "coding", "crafts", "ecology", "english", "geography", "history", "informatics", "literature", "math", "music", "pe", "physics", "robotics", "russian", "safety", "social", "tech"],
  7: ["algebra", "art", "biology", "chemistry", "coding", "ecology", "english", "geography", "geometry", "history", "informatics", "literature", "music", "pe", "physics", "robotics", "russian", "safety", "social", "tech"],
  8: ["algebra", "art", "biology", "chemistry", "coding", "economy", "english", "geography", "geometry", "history", "informatics", "law", "literature", "music", "pe", "physics", "robotics", "russian", "safety", "social", "tech"],
  9: ["algebra", "art", "biology", "career", "chemistry", "coding", "economy", "english", "geography", "geometry", "history", "informatics", "literature", "music", "oge", "pe", "physics", "psychology", "russian", "safety", "social", "tech"],
  10: ["algebra", "art", "astronomy", "biology", "business", "career", "chemistry", "coding", "economy", "ege", "english", "geography", "geometry", "history", "informatics", "lab", "literature", "pe", "philosophy", "physics", "projects", "russian", "safety", "social", "tech"],
  11: ["algebra", "biology", "chemistry", "coding", "economy", "english", "geography", "geometry", "history", "informatics", "literature", "pe", "physics", "russian", "safety", "social"],
}

// Предметы по классам для быстрого доступа (без загрузки данных)
export function getSubjectKeysForGrade(grade: number): string[] {
  return gradeSubjectKeys[grade] || []
}

// Базовый путь для загрузки данных (соответствует basePath в next.config.ts)
const BASE_PATH = '/school-curriculum-app'

// Асинхронная загрузка данных предмета из JSON
async function loadSubjectData(grade: number, subject: string): Promise<{ lessons?: SubjectData; games?: GameLesson[] }> {
  try {
    const response = await fetch(`${BASE_PATH}/data/grades/${grade}/${subject}.json`)
    if (!response.ok) {
      console.warn(`Failed to load ${grade}/${subject}: ${response.status}`)
      return {}
    }
    return await response.json()
  } catch (e) {
    console.warn(`Error loading ${grade}/${subject}:`, e)
    return {}
  }
}

// Загрузка всех предметов для класса
export async function getSubjectsForGrade(grade: number): Promise<Subject[]> {
  // Проверяем кэш
  const cached = subjectsCache.get(grade)
  if (cached) return cached

  const keys = gradeSubjectKeys[grade] || []
  const results = await Promise.all(keys.map(key => loadSubjectData(grade, key)))

  const subjects = results
    .map(r => r.lessons)
    .filter((s): s is SubjectData => !!s)

  // Кэшируем
  subjectsCache.set(grade, subjects)
  return subjects
}

// Загрузка всех игр для класса
export async function getGamesForGrade(grade: number): Promise<GameLesson[]> {
  // Проверяем кэш
  const cached = gamesCache.get(grade)
  if (cached) return cached

  const keys = gradeSubjectKeys[grade] || []
  const results = await Promise.all(keys.map(key => loadSubjectData(grade, key)))

  const games = results
    .flatMap(r => r.games || [])

  // Кэшируем
  gamesCache.set(grade, games)
  return games
}

// Curriculum данные (синхронные - только структура)
export const gradeCurriculum: GradeCurriculum[] = Array.from({ length: 12 }, (_, i) => ({
  grade: i,
  title: gradeNames[i],
  subjects: [] // Предметы загружаются асинхронно
}))

// Экспорт типов для обратной совместимости
export type { Subject, SubjectData, GameLesson, GradeCurriculum }
