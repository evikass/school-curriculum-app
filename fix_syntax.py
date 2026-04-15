#!/usr/bin/env python3
"""
Comprehensive fix script for TypeScript syntax errors in school-curriculum-app.

Fixes:
1. psychology/index.ts: Replace `        examples: [\n` with `        [\n` 
   (8-space-indented `examples: [` inside createLesson calls)
2. psychology/index.ts: Fix missing commas and indentation in example strings
3. physics/index.ts: Fix missing commas between example strings, fix indentation
4. russian/index.ts: Fix missing commas between example strings, fix indentation
5. art/index.ts (grade 8): Fix missing opening quote on line 659
6. career/index.ts: Fix missing newline before `export const games`
7. economy/index.ts: Remove orphaned example arrays in games section
"""

import re
import os

BASE = "/home/z/my-project/school-curriculum-app/src/data/grades"

def fix_missing_commas_and_indentation(filepath):
    """Fix missing commas between adjacent string lines and normalize indentation."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = []
    result = []
    for i in range(len(lines)):
        line = lines[i]
        stripped = line.rstrip()
        
        # Check if this line ends with " (a string closing quote at end of line,
        # after stripping whitespace) and the NEXT line starts with " (a new string)
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            next_stripped = next_line.lstrip()
            next_stripped_content = next_stripped
            
            # Current line ends with a string literal (ending ")
            # Check for patterns like: some text"  or  some text",
            # We want: if line ends with " and next line starts with "
            # But we need to handle the case where current line already has a comma
            
            # Check if current line's stripped version ends with " (possibly followed by nothing or whitespace)
            # and doesn't already end with ",
            current_trimmed = stripped.rstrip()
            
            if (current_trimmed.endswith('"') and 
                not current_trimmed.endswith('",') and
                next_stripped_content.startswith('"')):
                # Add comma
                new_line = stripped + ',\n'
                result.append(new_line)
                changes.append(f"  Line {i+1}: Added missing comma")
                continue
            
            # Also handle lines ending with '"` (backtick string closing)
            if (current_trimmed.endswith('"`') and 
                not current_trimmed.endswith('",`') and
                next_stripped_content.startswith('"')):
                new_line = stripped + ',\n'
                result.append(new_line)
                changes.append(f"  Line {i+1}: Added missing comma (backtick)")
                continue
        
        result.append(line)
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(result)
        print(f"  Fixed {len(changes)} missing commas in {filepath}")
    
    return changes


def fix_indentation(filepath, target_indent=12):
    """Fix over-indented example string lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = []
    result = []
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        
        # Only fix lines that are string literals (start with ") and are over-indented
        if stripped.startswith('"') and len(line) - len(stripped) > target_indent:
            # Only fix if it's inside an array context (the line starts with spaces and then ")
            leading_spaces = len(line) - len(stripped)
            if leading_spaces > target_indent:
                new_line = ' ' * target_indent + stripped
                result.append(new_line)
                changes.append(f"  Line {i+1}: Fixed indentation ({leading_spaces} -> {target_indent} spaces)")
                continue
        
        result.append(line)
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(result)
        print(f"  Fixed {len(changes)} indentation issues in {filepath}")
    
    return changes


def fix_psychology(filepath):
    """Fix psychology/index.ts: replace `        examples: [` with `        [`."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    # Replace '        examples: [\n' with '        [\n' (8 spaces)
    old = '        examples: [\n'
    new = '        [\n'
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        changes.append(f"  Replaced {count} occurrences of '        examples: [\\n' with '        [\\n'")
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Psychology fixes in {filepath}:")
        for c in changes:
            print(c)
    
    return changes


def fix_art_grade8(filepath):
    """Fix art/index.ts (grade 8): add missing opening quote on the task line."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = []
    for i, line in enumerate(lines):
        if 'Кто автор скульптуры «Давид»?"' in line and '"Кто автор скульптуры' not in line:
            lines[i] = line.replace('Кто автор скульптуры «Давид»?"', '"Кто автор скульптуры «Давид»?"')
            changes.append(f"  Line {i+1}: Added missing opening quote")
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"  Art grade 8 fixes in {filepath}:")
        for c in changes:
            print(c)
    
    return changes


def fix_career(filepath):
    """Fix career/index.ts: add missing newline before 'export const games'."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    old = '}export const games'
    new = '}\n\nexport const games'
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        changes.append(f"  Fixed {count} missing newline before 'export const games'")
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Career fixes in {filepath}:")
        for c in changes:
            print(c)
    
    return changes


def fix_economy_games(filepath):
    """Fix economy/index.ts: remove orphaned example arrays from games section.
    
    These are blocks of 3 example strings followed by '],' that appear after
    the tasks array closing ']' but before 'reward:' in game objects.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Strategy: find blocks in the games section that are orphaned example arrays.
    # These blocks appear between `],` (closing tasks) and `reward:` 
    # They consist of lines starting with many spaces + `"some text"` (or ending with `],`)
    # Pattern: lines that start with `          "` (10 spaces + quote) as string content,
    # NOT inside a proper array/object structure.
    
    # Actually, let's be more precise. Looking at the file:
    # After the tasks array closes with `],`, the orphaned blocks look like:
    #     ],
    #           "string1"
    #           "string2"
    #           "string3"
    #           ],
    #     reward: ...
    
    # The orphaned lines start with 10 spaces + " and the closing ], also starts with 10 spaces
    
    # Let me parse line by line and remove these orphaned blocks
    changes = []
    result = []
    i = 0
    in_games = False
    removed_blocks = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Track when we enter the games section
        if 'export const games' in stripped:
            in_games = True
        
        # Check for orphaned block pattern in games section
        # An orphaned block starts with a line that has 10 spaces + " (a string) 
        # after a `],` that closed the tasks array
        if in_games and line.startswith('          "') and i > 0:
            # Check if the previous line (in result) was `],` closing tasks
            # or another orphaned block closing
            prev_in_result = result[-1].rstrip() if result else ""
            if prev_in_result.endswith('],') or prev_in_result.endswith(']'):
                # This looks like the start of an orphaned block
                # Collect all lines until we find `],` 
                orphan_lines = [line]
                j = i + 1
                while j < len(lines):
                    if lines[j].strip() == '],' or lines[j].strip() == '],':
                        orphan_lines.append(lines[j])
                        j += 1
                        break
                    elif lines[j].startswith('          "'):
                        orphan_lines.append(lines[j])
                        j += 1
                    else:
                        # Not part of orphaned block
                        break
                
                # Check if the block ends with ],
                if orphan_lines[-1].strip() == '],':
                    # Verify: all lines in the block should be string content or ],
                    all_orphan = all(
                        l.startswith('          "') or l.strip() == '],'
                        for l in orphan_lines
                    )
                    if all_orphan and len(orphan_lines) >= 2:
                        # Remove this block
                        for ol in orphan_lines:
                            changes.append(f"  Removed: {ol.rstrip()}")
                        removed_blocks += 1
                        i = j
                        continue
        
        result.append(line)
        i += 1
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(result)
        print(f"  Economy games fixes in {filepath}:")
        print(f"  Removed {removed_blocks} orphaned example blocks ({len(changes)} lines)")
        for c in changes[:10]:  # Show first 10
            print(c)
        if len(changes) > 10:
            print(f"  ... and {len(changes) - 10} more lines")
    
    return changes


def main():
    print("=" * 60)
    print("Fixing TypeScript syntax errors")
    print("=" * 60)
    
    # 1. Fix psychology/index.ts
    print("\n[1] Fixing psychology/index.ts...")
    psych_file = os.path.join(BASE, "9/psychology/index.ts")
    fix_psychology(psych_file)
    fix_missing_commas_and_indentation(psych_file)
    fix_indentation(psych_file, target_indent=12)
    
    # 2. Fix physics/index.ts
    print("\n[2] Fixing physics/index.ts...")
    phys_file = os.path.join(BASE, "9/physics/index.ts")
    fix_missing_commas_and_indentation(phys_file)
    fix_indentation(phys_file, target_indent=12)
    
    # 3. Fix russian/index.ts
    print("\n[3] Fixing russian/index.ts...")
    rus_file = os.path.join(BASE, "9/russian/index.ts")
    fix_missing_commas_and_indentation(rus_file)
    fix_indentation(rus_file, target_indent=12)
    
    # 4. Fix art/index.ts (grade 8)
    print("\n[4] Fixing art/index.ts (grade 8)...")
    art_file = os.path.join(BASE, "8/art/index.ts")
    fix_art_grade8(art_file)
    
    # 5. Fix career/index.ts
    print("\n[5] Fixing career/index.ts...")
    career_file = os.path.join(BASE, "9/career/index.ts")
    fix_career(career_file)
    
    # 6. Fix economy/index.ts
    print("\n[6] Fixing economy/index.ts...")
    econ_file = os.path.join(BASE, "9/economy/index.ts")
    fix_economy_games(econ_file)
    
    print("\n" + "=" * 60)
    print("All fixes applied!")
    print("=" * 60)


if __name__ == '__main__':
    main()
