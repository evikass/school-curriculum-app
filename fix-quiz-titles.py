#!/usr/bin/env python3
"""
Fix quiz/game titles in school curriculum app to match lesson titles.

The app's LessonViewer.tsx tries to find a matching game for a lesson by:
1. Stripping "Урок N:" prefix from lesson title
2. Exact match on topic or full title
3. Substring match

This script renames game titles to match lesson titles so the app's matching
logic works correctly. Only game title strings are modified - nothing else.

Usage:
  python3 fix-quiz-titles.py --test --dry-run    # Test on grade 10 biology (no changes)
  python3 fix-quiz-titles.py --dry-run            # Preview all changes (no changes)
  python3 fix-quiz-titles.py                      # Apply all changes
  python3 fix-quiz-titles.py --file=PATH          # Process specific file
"""

import os
import re
import shutil
import difflib
from pathlib import Path
from typing import List, Tuple, Optional, Dict

BASE_DIR = Path("/home/z/my-project/school-curriculum-app/src/data/grades")

# Supplementary game patterns - skip these (they span multiple lessons or are summaries)
SUPPLEMENTARY_PATTERNS = [
    "Итоговый", "Итоговая", "Викторина", "Обзор", "Обобщение",
    "Повторение", "Подготовка к", "Все о", "Все об", "Проверка",
    "Контрольн", "Тест по разделу", "Тест по теме", "Тест по главе",
    "Итоговый тест", "Итоговая работа", "Итоговая контрольная",
    "Обобщающий", "Обобщающая", "Повторительн", "Закреплен",
    "Практикум", "Проект", "Исследован",
]

# Combined game indicator words (Russian conjunctions that join two topics)
COMBINE_WORDS = {'и', 'или', 'а', 'но'}

# Russian stop words to exclude from content word analysis
STOP_WORDS = {'и', 'или', 'а', 'но', 'в', 'на', 'с', 'за', 'по', 'из', 'от', 'к', 'о', 'об',
              'не', 'как', 'что', 'это', 'всё', 'для', 'при', 'про', 'без', 'до', 'из-за',
              'под', 'над', 'из-под', 'кроме', 'между', 'перед', 'через', 'после'}

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA00-\U0001FA6F"  # chess symbols
    "\U0001FA70-\U0001FAFF"  # symbols extended-A
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"
    "\u2600-\u26FF"          # misc symbols
    "\u2700-\u27BF"          # dingbats
    "\uFE00-\uFE0F"          # variation selectors
    "\u200D"                 # zero width joiner
    "]+"
)


# ============================================================
# Title normalization & matching (mimics app's LessonViewer.tsx)
# ============================================================

def strip_lesson_prefix(title: str) -> str:
    """Strip 'Урок N:' prefix from a title."""
    if ':' in title:
        return title.split(':', 1)[1].strip()
    return title.strip()


def normalize(title: str) -> str:
    """Normalize title for comparison: lowercase, strip emoji, strip whitespace."""
    t = title.lower().strip()
    t = EMOJI_PATTERN.sub('', t)
    return t.strip()


def strip_emoji(title: str) -> str:
    """Remove emoji from title."""
    return EMOJI_PATTERN.sub('', title).strip()


def app_match(lesson_title: str, game_title: str) -> bool:
    """
    Check if the app's matching logic would match a game to a lesson.
    Mirrors LessonViewer.tsx startQuiz() logic with normalize() for emoji handling.
    """
    lesson_topic = strip_lesson_prefix(lesson_title)
    lesson_topic_lower = normalize(lesson_topic)
    lesson_title_lower = normalize(lesson_title)
    game_name_lower = normalize(game_title)

    # Step 1: exact match
    if game_name_lower == lesson_topic_lower or game_name_lower == lesson_title_lower:
        return True

    # Step 2: substring match (only if both are long enough to be meaningful)
    if len(game_name_lower) > 3 and len(lesson_topic_lower) > 3:
        if game_name_lower in lesson_topic_lower or lesson_topic_lower in game_name_lower:
            return True

    return False


# ============================================================
# Supplementary / combined game detection
# ============================================================

def is_supplementary(title: str) -> bool:
    """Check if a game title is supplementary (shouldn't be renamed)."""
    title_lower = title.lower()
    for pattern in SUPPLEMENTARY_PATTERNS:
        if pattern.lower() in title_lower:
            return True
    return False


def is_combined_game(game_title: str, lesson_titles: List[str]) -> bool:
    """
    Detect if a game spans multiple lessons (e.g., "Причастие и деепричастие").
    Such games should not be renamed to a single lesson's title.
    """
    game_topic = strip_lesson_prefix(game_title)
    game_clean = strip_emoji(game_topic).lower().strip()
    game_words = set(game_clean.split()) - STOP_WORDS

    if not game_words:
        return False

    # Count how many distinct lessons each content word appears in
    word_lesson_map: Dict[str, set] = {}
    for word in game_words:
        for lt in lesson_titles:
            lt_topic = strip_lesson_prefix(lt)
            lt_clean = strip_emoji(lt_topic).lower().strip()
            if word in lt_clean.split():
                word_lesson_map.setdefault(word, set()).add(lt)

    # If key content words appear in different lessons (2+ words each in
    # different unique lesson sets), this is likely a combined game
    if len(word_lesson_map) >= 2:
        unique_lessons = set()
        for lesson_set in word_lesson_map.values():
            unique_lessons.update(lesson_set)
        if len(unique_lessons) >= 2 and len(word_lesson_map) >= 2:
            return True

    return False


# ============================================================
# Fuzzy matching
# ============================================================

def has_contradictory_content(game_title: str, lesson_title: str) -> bool:
    """
    Check if game and lesson titles have contradictory content.
    E.g., 'Числа 1-5' vs 'Числа 6-10', 'Зарубежные сказки' vs 'Русские сказки',
    'Аппликации из бумаги' vs 'Аппликация из листьев'.
    """
    game_topic = strip_emoji(strip_lesson_prefix(game_title)).lower().strip()
    lesson_topic = strip_emoji(strip_lesson_prefix(lesson_title)).lower().strip()

    game_words = set(game_topic.split()) - STOP_WORDS
    lesson_words = set(lesson_topic.split()) - STOP_WORDS

    # Check for contradictory number ranges (e.g., "1-5" vs "6-10")
    game_nums = set(re.findall(r'\d+', game_topic))
    lesson_nums = set(re.findall(r'\d+', lesson_topic))
    if game_nums and lesson_nums and game_nums != lesson_nums:
        # Both have numbers but they differ
        return True

    # Check for contradictory adjectives/modifiers
    # Words that are in one title but not the other and could change meaning
    game_only = game_words - lesson_words
    lesson_only = lesson_words - game_words

    # Known contradictory pairs (both present across the two titles)
    # These are words that, when they differ across game/lesson titles,
    # indicate genuinely different topics despite sharing a common root word
    contradiction_pairs = [
        # Different types/variants of the same general category
        ('зарубежные', 'русские'),
        ('русские', 'зарубежные'),
        ('бумаги', 'листьев'),
        ('листьев', 'бумаги'),
        ('бумаги', 'ткани'),
        ('ткани', 'бумаги'),
        ('камешков', 'шишек'),
        ('шишек', 'камешков'),
        ('камешков', 'жлудей'),
        ('жлудей', 'камешков'),
        ('желудей', 'шишек'),
        ('шишек', 'желудей'),
        # Math operations - clearly different topics
        ('сложение', 'вычитание'),
        ('вычитание', 'сложение'),
        ('сложение', 'умножение'),
        ('умножение', 'сложение'),
        ('сложение', 'сравнение'),
        ('сравнение', 'сложение'),
        ('сложение', 'деление'),
        ('деление', 'сложение'),
        ('вычитание', 'сравнение'),
        ('сравнение', 'вычитание'),
        ('вычитание', 'умножение'),
        ('умножение', 'вычитание'),
        ('деление', 'умножение'),
        ('умножение', 'деление'),
        ('деление', 'сравнение'),
        ('сравнение', 'деление'),
        # Grammar/literature
        ('гласные', 'согласные'),
        ('согласные', 'гласные'),
        ('действительные', 'страдательные'),
        ('страдательные', 'действительные'),
        ('настоящее', 'прошедшее'),
        ('прошедшее', 'настоящее'),
        ('вежливые', 'волшебные'),
        ('волшебные', 'вежливые'),
        ('писатели', 'поэты'),
        ('поэты', 'писатели'),
        ('сложные', 'вводные'),
        ('вводные', 'сложные'),
        # Biology
        ('беспозвоночные', 'позвоночные'),
        ('позвоночные', 'беспозвоночные'),
        ('пластический', 'энергетический'),
        ('энергетический', 'пластический'),
        ('одноклеточные', 'многоклеточные'),
        ('многоклеточные', 'одноклеточные'),
        ('прямое', 'непрямое'),
        ('непрямое', 'прямое'),
        ('бесполое', 'половое'),
        ('половое', 'бесполое'),
        ('клетки', 'растений'),
        ('растений', 'клетки'),
        # Safety - different types
        ('дорогах', 'водой'),
        ('водой', 'дорогах'),
        ('дорогах', 'газом'),
        ('газом', 'дорогах'),
        ('дорогах', 'велосипедиста'),
        ('велосипедиста', 'дорогах'),
        ('быт', 'газом'),
        ('газом', 'быт'),
        ('быт', 'водой'),
        ('водой', 'быт'),
        ('быт', 'велосипедиста'),
        ('велосипедиста', 'быт'),
        ('газом', 'водой'),
        ('водой', 'газом'),
        # Units of measurement
        ('измерения', 'длины'),
        ('длины', 'измерения'),
        ('измерения', 'времени'),
        ('времени', 'измерения'),
        ('измерения', 'массы'),
        ('массы', 'измерения'),
        ('длины', 'времени'),
        ('времени', 'длины'),
        # Music
        ('музыкальные', 'инструментальные'),
        ('инструментальные', 'музыкальные'),
        # Programming
        ('функции', 'python'),
        ('алгоритмы', 'повторения'),
        ('повторения', 'алгоритмы'),
        # History
        ('нашествие', 'завоевание'),
        ('завоевание', 'нашествие'),
        # Other
        ('знакомство', 'прощание'),
        ('прощание', 'знакомство'),
        ('организм', 'строение'),
        ('строение', 'организм'),
        ('развитие', 'звуки'),
        ('звуки', 'развитие'),
        ('предметов', 'пределах'),
        ('пределах', 'предметов'),
        ('камешков', 'желудей'),
        ('желудей', 'камешков'),
        ('быт', 'велосипедиста'),
        ('велосипедиста', 'быт'),
        ('быту', 'газом'),
        ('газом', 'быту'),
        ('быту', 'водой'),
        ('водой', 'быту'),
        ('быту', 'велосипедиста'),
        ('велосипедиста', 'быту'),
        ('быт', 'газом'),
        ('газом', 'быт'),
        ('быт', 'водой'),
        ('водой', 'быт'),
        ('сложные', 'однородные'),
        ('однородные', 'сложные'),
        ('сложные', 'обособленные'),
        ('обособленные', 'сложные'),
        ('предметов', 'до'),
        ('до', 'предметов'),
    ]

    for g_word in game_only:
        for l_word in lesson_only:
            if (g_word, l_word) in contradiction_pairs:
                return True

    # If both titles have differentiating words (words only in one),
    # and those words are substantial (not stop words), be more cautious
    # If >60% of game content words are NOT in the lesson, it's likely a different topic
    if game_words:
        missing_ratio = len(game_only) / len(game_words)
        if missing_ratio > 0.6:
            return True

    return False


def fuzzy_match_score(lesson_title: str, game_title: str) -> float:
    """
    Compute fuzzy match score between a lesson and a game title.

    Uses the topic part (after "Урок N:") of both titles, strips emoji,
    then uses SequenceMatcher + word overlap for similarity.
    Returns 0.0 if contradictory content is detected.
    """
    lesson_topic = strip_lesson_prefix(lesson_title)
    game_topic = strip_lesson_prefix(game_title)

    lesson_clean = strip_emoji(lesson_topic).lower().strip()
    game_clean = strip_emoji(game_topic).lower().strip()

    if not lesson_clean or not game_clean:
        return 0.0

    # Check for contradictions first
    if has_contradictory_content(game_title, lesson_title):
        return 0.0

    # Direct sequence matcher score
    score = difflib.SequenceMatcher(None, lesson_clean, game_clean).ratio()

    # Also check word overlap
    lesson_words = set(lesson_clean.split()) - STOP_WORDS
    game_words = set(game_clean.split()) - STOP_WORDS

    if lesson_words and game_words:
        common = lesson_words & game_words
        if common:
            # Overlap coefficient: fraction of game words found in lesson
            # Weight this by how much of the game's content is covered
            game_coverage = len(common) / len(game_words) if game_words else 0
            lesson_coverage = len(common) / len(lesson_words) if lesson_words else 0
            # Use harmonic mean for balanced coverage
            if game_coverage + lesson_coverage > 0:
                word_overlap = 2 * game_coverage * lesson_coverage / (game_coverage + lesson_coverage)
            else:
                word_overlap = 0
            score = max(score, word_overlap)

    return score


def find_best_lesson_match(game_title: str, lesson_titles: List[str]) -> Optional[Tuple[str, float]]:
    """
    Find the best matching lesson for a game title.
    Returns (lesson_title, score) or None if no good match found.
    Only returns matches where the game is clearly about the same topic as the lesson.
    """
    best_match = None
    best_score = 0.0

    game_topic = strip_lesson_prefix(game_title)
    game_clean = strip_emoji(game_topic).lower().strip()

    for lesson_title in lesson_titles:
        score = fuzzy_match_score(lesson_title, game_title)

        # Skip if contradictory (score will be 0.0)
        if score == 0.0:
            continue

        # Bonus: if the game topic is a substring of the lesson topic (or vice versa)
        lesson_topic = strip_lesson_prefix(lesson_title)
        lesson_clean = strip_emoji(lesson_topic).lower().strip()

        if game_clean and lesson_clean:
            if game_clean in lesson_clean or lesson_clean in game_clean:
                score = max(score, 0.7)

        # Additional check: require that most of the game's key words appear in the lesson
        game_words = set(game_clean.split()) - STOP_WORDS
        lesson_words = set(lesson_clean.split()) - STOP_WORDS
        if game_words:
            common = game_words & lesson_words
            coverage = len(common) / len(game_words)
            # If less than 50% of game's content words are in the lesson,
            # this is likely a different topic - penalize heavily
            if coverage < 0.5:
                score *= 0.3

        if score > best_score:
            best_score = score
            best_match = lesson_title

    return (best_match, best_score) if best_match else None


# ============================================================
# Title generation
# ============================================================

def get_desired_game_title(lesson_title: str) -> str:
    """
    Get the desired game title from a lesson title.
    - If lesson has "Урок N:" prefix, use the topic part (after colon).
    - If lesson has emoji prefix (e.g., "🔢 Урок 1: ..."), strip emoji from prefix
      but keep the topic part clean.
    - If lesson has no "Урок N:" prefix, use the full lesson title (without emoji).
    - Preserve emoji only if the lesson title itself has emoji in the topic part.
    """
    # First strip any leading emoji
    cleaned = strip_emoji(lesson_title)

    if ':' in cleaned:
        # Has "Урок N:" prefix - use topic part
        return cleaned.split(':', 1)[1].strip()
    return cleaned


# ============================================================
# File parsing
# ============================================================

def extract_lesson_titles(content: str) -> List[str]:
    """
    Extract lesson titles from the lessons export section ONLY.
    Skips subject-level title (the first title: property).
    Handles both:
    - L("title", ...) (helper function)
    - title: "..." or title: `...` (direct property)
    """
    titles = []

    # Find the lessons section (with or without export)
    lessons_match = re.search(r'(?:export\s+)?const\s+lessons\s*[:=]\s*', content)
    if not lessons_match:
        return titles

    lessons_start = lessons_match.end()

    # Find where the games export starts (or end of file)
    games_match = re.search(r'export\s+const\s+games\s*[:=]\s*', content)
    lessons_end = games_match.start() if games_match else len(content)

    lessons_content = content[lessons_start:lessons_end]

    # Pattern 1: L("title", ...) helper function
    l_pattern = re.compile(r'L\(\s*["`]([^"`]+)["`]')
    for match in l_pattern.finditer(lessons_content):
        titles.append(match.group(1))

    # Pattern 1b: createLesson("title", ...) helper function
    cl_pattern = re.compile(r'createLesson\(\s*"([^"]+)"')
    for match in cl_pattern.finditer(lessons_content):
        titles.append(match.group(1))

    # Pattern 2: title: "..." or title: `...` within lesson objects
    title_pattern = re.compile(r'^\s*title:\s*["`]([^"`]+)["`]', re.MULTILINE)
    first_title = True
    for match in title_pattern.finditer(lessons_content):
        title = match.group(1)
        if first_title:
            # Skip the first title: which is the subject name
            first_title = False
            continue
        if title not in titles:  # Avoid duplicates from L() pattern
            titles.append(title)

    return titles


def extract_game_entries(content: str) -> List[Tuple[str, int, int, str]]:
    """
    Extract game titles from the games export section ONLY.
    Returns list of (title, start_pos, end_pos, quote_char) for replacement.
    """
    results = []

    # Find the games section (with or without export)
    games_match = re.search(r'(?:export\s+)?const\s+games\s*[:=]\s*', content)
    if not games_match:
        return results

    games_start = games_match.end()
    games_content = content[games_start:]

    # Match title: "..." or title: `...` within game objects
    title_pattern = re.compile(r'title:\s*(["`])([^"`]+?)\1')

    for match in title_pattern.finditer(games_content):
        title = match.group(2)
        quote = match.group(1)
        abs_start = games_start + match.start(2)
        abs_end = games_start + match.end(2)
        results.append((title, abs_start, abs_end, quote))

    return results


# ============================================================
# Main processing
# ============================================================

def process_file(filepath: Path, dry_run: bool = False) -> List[dict]:
    """
    Process a single subject file.
    Returns list of changes made (or proposed in dry-run mode).
    """
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ERROR reading {filepath}: {e}")
        return changes

    # Extract lesson titles from the lessons section
    lesson_titles = extract_lesson_titles(content)

    if not lesson_titles:
        return changes

    # Extract game titles with positions from the games section
    game_entries = extract_game_entries(content)

    if not game_entries:
        return changes

    # Collect all existing game titles for duplicate detection
    existing_game_titles = [gt for gt, _, _, _ in game_entries]
    # Track new titles that will be assigned (to prevent duplicates from renames)
    pending_new_titles = set()

    # Process each game
    replacements = []  # (start, end, old_title, new_title)

    for game_title, start_pos, end_pos, quote in game_entries:
        # Check if already matches any lesson using app's matching logic
        already_matches = any(app_match(lt, game_title) for lt in lesson_titles)

        if already_matches:
            continue

        # Skip supplementary games
        if is_supplementary(game_title):
            continue

        # Skip combined games (spanning multiple lessons)
        if is_combined_game(game_title, lesson_titles):
            continue

        # Try fuzzy matching to find the best lesson
        match_result = find_best_lesson_match(game_title, lesson_titles)

        if match_result is None:
            continue

        best_lesson, score = match_result

        if score < 0.62:
            continue

        # Determine new title
        new_title = get_desired_game_title(best_lesson)

        # Don't rename if the new title would be the same as current (after normalization)
        if normalize(new_title) == normalize(game_title):
            continue

        # Don't rename if the new title would be empty
        if not new_title.strip():
            continue

        # Sanity check: the new title should actually match the lesson via app_match
        if not app_match(best_lesson, new_title):
            # The new title wouldn't match even after our fix - skip
            continue

        # Don't rename if it would create a duplicate game title
        normalized_new = normalize(new_title)
        if any(normalize(gt) == normalized_new for gt in existing_game_titles if gt != game_title):
            continue
        if normalized_new in pending_new_titles:
            continue

        pending_new_titles.add(normalized_new)
        replacements.append((start_pos, end_pos, game_title, new_title))
        changes.append({
            'old_title': game_title,
            'new_title': new_title,
            'matched_lesson': best_lesson,
            'score': round(score, 3),
        })

    if replacements and not dry_run:
        # Apply replacements in reverse order (to preserve positions)
        replacements.sort(key=lambda x: x[0], reverse=True)

        new_content = content
        for start_pos, end_pos, old_title, new_title in replacements:
            new_content = new_content[:start_pos] + new_title + new_content[end_pos:]

        # Backup
        backup_path = filepath.with_suffix('.ts.bak')
        shutil.copy2(filepath, backup_path)

        # Write
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changes


def find_subject_files() -> List[Path]:
    """Find all subject index.ts files across grades 0-11."""
    files = []
    for grade_dir in sorted(BASE_DIR.iterdir()):
        if not grade_dir.is_dir():
            continue
        try:
            grade_num = int(grade_dir.name)
            if 0 <= grade_num <= 11:
                for subject_dir in sorted(grade_dir.iterdir()):
                    if subject_dir.is_dir():
                        index_file = subject_dir / "index.ts"
                        if index_file.exists():
                            files.append(index_file)
        except ValueError:
            continue
    return files


def main():
    import sys

    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    test_mode = '--test' in sys.argv
    specific_file = None

    for arg in sys.argv[1:]:
        if arg.startswith('--file='):
            specific_file = Path(arg[7:])

    print("=" * 70)
    print("Fix Quiz Titles - School Curriculum App")
    print("=" * 70)
    print()

    if dry_run:
        print("DRY RUN MODE - no files will be modified")
        print()

    if test_mode:
        # Test on grade 10 biology
        test_file = BASE_DIR / "10" / "biology" / "index.ts"
        if test_file.exists():
            print(f"TEST MODE - Processing: {test_file}")
            print()
            changes = process_file(test_file, dry_run=dry_run)
            if changes:
                print(f"Found {len(changes)} changes:")
                for c in changes:
                    print(f"  '{c['old_title']}'")
                    print(f"  -> '{c['new_title']}'")
                    print(f"     (matched lesson: '{c['matched_lesson']}', score: {c['score']})")
            else:
                print("No changes needed - all games already match lessons.")
        else:
            print(f"Test file not found: {test_file}")
        return

    if specific_file:
        files = [specific_file] if specific_file.exists() else []
    else:
        files = find_subject_files()

    total_changes = 0
    files_modified = 0
    total_games = 0
    total_matched = 0
    total_unmatched = 0

    for filepath in files:
        rel_path = filepath.relative_to(BASE_DIR.parent.parent.parent.parent)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        lesson_titles = extract_lesson_titles(content)
        game_entries = extract_game_entries(content)
        total_games += len(game_entries)

        # Count how many already match
        for game_title, _, _, _ in game_entries:
            if any(app_match(lt, game_title) for lt in lesson_titles):
                total_matched += 1
            else:
                total_unmatched += 1

        changes = process_file(filepath, dry_run=dry_run)

        if changes:
            files_modified += 1
            total_changes += len(changes)
            print(f"\n{rel_path}")
            for c in changes:
                print(f"  '{c['old_title']}'")
                print(f"  -> '{c['new_title']}'")
                print(f"     (matched: '{c['matched_lesson']}', score: {c['score']})")

    print()
    print("=" * 70)
    print(f"Total games: {total_games}")
    print(f"Already matching: {total_matched}")
    print(f"Unmatched before fix: {total_unmatched}")
    print(f"Changes proposed/applied: {total_changes} across {files_modified} files")
    if dry_run:
        print("(DRY RUN - no files were modified)")
    print("=" * 70)


if __name__ == '__main__':
    main()
