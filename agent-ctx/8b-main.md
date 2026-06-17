# Task 8b - Replace Auto-Generated Quiz Questions

## Summary
Replaced all 250 auto-generated quiz questions for biology lessons 11-60 with proper, hand-crafted questions based on Пасечник textbook content.

## What was done
1. Analyzed current biology.json structure - found 60 games, first 10 with good questions, 11-60 with terrible auto-generated ones
2. Created Python script `replace_quiz_questions.py` with 250 quiz questions embedded as dictionary
3. Each lesson (11-60) got 5 specific biology questions with:
   - Proper question text (not just "what is true about X")
   - 5 options: 1 correct + 3 wrong but plausible + "Не знаю"
   - correctAnswer matching the correct option exactly
   - Short helpful hint
   - examples and keyPoints from the corresponding lesson
4. Fixed two duplicate-key bugs in the script
5. Ran the script successfully - all 50 games replaced
6. Full validation passed

## Files Modified
- `public/data/grades/10/biology.json` - replaced quiz questions in games[10-59]

## Files Created
- `replace_quiz_questions.py` - script with embedded quiz data (can be deleted after verification)

## Validation Results
- JSON valid ✓
- 60 games, 300 total quiz tasks ✓
- All replaced games: 5 tasks each ✓
- All tasks quiz type ✓
- All tasks have 5 options ✓
- Last option always "Не знаю" ✓
- correctAnswer always in options ✓
- All tasks have examples, keyPoints, hints ✓
