// ============================================================================
// Star rating helper — unified percentage-based formula.
//
//   100%+ correct  → 5 ⭐
//    80%+ correct  → 4 ⭐
//    50%+ correct  → 3 ⭐
//    30%+ correct  → 2 ⭐
//    <30% correct  → 1 ⭐
//
// A player who answers zero questions correctly still gets 1 star (no 0-star
// outcomes — matches the previous UX where stars never fell below 1).
// ============================================================================

export const MAX_STARS = 5

export function calculateStars(score: number, total: number): number {
  if (total <= 0) return 1
  const percent = (score / total) * 100
  if (percent >= 100) return 5
  if (percent >= 80) return 4
  if (percent >= 50) return 3
  if (percent >= 30) return 2
  return 1
}

// Optional: human-readable label for the star tier — used on results screens.
export function starLabel(stars: number): string {
  switch (stars) {
    case 5: return '🏆 Идеально!'
    case 4: return '🎉 Отлично!'
    case 3: return '👍 Хорошо!'
    case 2: return '📖 Почти получилось!'
    default: return '💪 Попробуй ещё!'
  }
}
