import re
import json

# Read the TS file
with open('/home/z/my-project/school-curriculum-app/src/data/grades/10/history-russia/index.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the lessons object using a different approach - use Node.js to evaluate
# Actually, let's just extract the structured data using regex on the L() calls

# The file has a pattern like:
# L("title", "description", [...], "image", "content", [...], [...], [...])

# This is complex to parse with regex. Let me use a different approach.
# Let's use Node.js ts-node to directly import and export

import subprocess

# Create a minimal JS wrapper that exports just the data
wrapper = """
const ts = require('typescript');
const fs = require('fs');

const sourceCode = fs.readFileSync('src/data/grades/10/history-russia/index.ts', 'utf-8');

// Create a program
const code = sourceCode.replace(/import.*from.*;/g, '');

// Simple approach: evaluate the code
// Replace L() function definition and export statements
let modified = sourceCode
  .replace(/import\s*\{[^}]*\}\s*from\s*['"][^'"]*['"]\s*;?/g, '')
  .replace(/export\s+const\s+lessons\s*:\s*SubjectData\s*=\s*/, 'const lessons = ')
  .replace(/export\s+const\s+games\s*:\s*GameLesson\[\]\s*=\s*/, 'const games = ');

// Write as a JS file
fs.writeFileSync('/tmp/hr_eval.js', modified);
console.log('Written to /tmp/hr_eval.js');
"""

with open('/tmp/wrapper.cjs', 'w') as f:
    f.write(wrapper)

subprocess.run(['node', '/tmp/wrapper.cjs'], cwd='/home/z/my-project/school-curriculum-app', capture_output=True)
print("Step 1 done")

