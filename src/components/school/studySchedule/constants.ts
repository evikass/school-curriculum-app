import { ScheduleItem, SubjectInfo } from './types'

export const defaultSchedule: ScheduleItem[] = [
  { id: '1', subject: 'Русский язык', time: '09:00', duration: 30, days: [1, 3, 5], active: true },
  { id: '2', subject: 'Математика', time: '10:00', duration: 30, days: [1, 2, 4], active: true },
  { id: '3', subject: 'Окружающий мир', time: '11:00', duration: 20, days: [2, 4], active: true },
  { id: '4', subject: 'Литература', time: '15:00', duration: 25, days: [1, 3, 5], active: true },
]

export const subjects: SubjectInfo[] = [
  { name: 'Русский язык', icon: '📖', color: 'bg-red-500' },
  { name: 'Математика', icon: '🔢', color: 'bg-blue-500' },
  { name: 'Литература', icon: '📚', color: 'bg-purple-500' },
  { name: 'Окружающий мир', icon: '🌍', color: 'bg-green-500' },
  { name: 'Иностранный язык', icon: '🌐', color: 'bg-pink-500' },
  { name: 'История', icon: '🏛️', color: 'bg-amber-500' },
  { name: 'Биология', icon: '🔬', color: 'bg-emerald-500' },
  { name: 'География', icon: '🗺️', color: 'bg-teal-500' },
]

export const dayNames = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']
export const dayNamesFull = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
