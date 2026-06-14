/**
 * Добавляет basePath к путям изображений.
 * Next.js автоматически добавляет basePath только к <Link> и <Image>,
 * но не к обычным <img> тегам. Этот хелпер исправляет это.
 */

const BASE_PATH = '/school-curriculum-app';

export function getImagePath(path: string | undefined): string | undefined {
  if (!path) return undefined;
  // Если путь уже содержит basePath, не добавляем повторно
  if (path.startsWith(BASE_PATH)) return path;
  // Добавляем basePath к абсолютным путям
  if (path.startsWith('/')) return `${BASE_PATH}${path}`;
  // Относительные пути возвращаем как есть
  return path;
}
