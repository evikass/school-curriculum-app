#!/bin/bash
cd /home/z/my-project/school-curriculum-app

echo "=== Starting batch 3 - Grades 6, 3, 8, 2 ==="

# Grade 6 chemistry (10)
echo "--- Grade 6 chemistry (10) ---"
node gen-one.mjs 6 chemistry 5 2>&1
node gen-one.mjs 6 chemistry 5 2>&1

# Grade 6 crafts (10)
echo "--- Grade 6 crafts (10) ---"
node gen-one.mjs 6 crafts 5 2>&1
node gen-one.mjs 6 crafts 5 2>&1

# Grade 6 ecology (9)
echo "--- Grade 6 ecology (9) ---"
node gen-one.mjs 6 ecology 5 2>&1
node gen-one.mjs 6 ecology 4 2>&1

# Grade 6 informatics (9)
echo "--- Grade 6 informatics (9) ---"
node gen-one.mjs 6 informatics 5 2>&1
node gen-one.mjs 6 informatics 4 2>&1

# Grade 6 physics (9)
echo "--- Grade 6 physics (9) ---"
node gen-one.mjs 6 physics 5 2>&1
node gen-one.mjs 6 physics 4 2>&1

# Grade 6 robotics (9)
echo "--- Grade 6 robotics (9) ---"
node gen-one.mjs 6 robotics 5 2>&1
node gen-one.mjs 6 robotics 4 2>&1

# Grade 6 social (9)
echo "--- Grade 6 social (9) ---"
node gen-one.mjs 6 social 5 2>&1
node gen-one.mjs 6 social 4 2>&1

# Grade 6 math (4)
echo "--- Grade 6 math (4) ---"
node gen-one.mjs 6 math 4 2>&1

# Grade 3 art (7)
echo "--- Grade 3 art (7) ---"
node gen-one.mjs 3 art 4 2>&1
node gen-one.mjs 3 art 3 2>&1

# Grade 3 informatics (8)
echo "--- Grade 3 informatics (8) ---"
node gen-one.mjs 3 informatics 4 2>&1
node gen-one.mjs 3 informatics 4 2>&1

# Grade 3 pe (8)
echo "--- Grade 3 pe (8) ---"
node gen-one.mjs 3 pe 4 2>&1
node gen-one.mjs 3 pe 4 2>&1

# Grade 3 safety (7)
echo "--- Grade 3 safety (7) ---"
node gen-one.mjs 3 safety 4 2>&1
node gen-one.mjs 3 safety 3 2>&1

# Grade 3 music (4)
echo "--- Grade 3 music (4) ---"
node gen-one.mjs 3 music 4 2>&1

# Grade 3 tech (4)
echo "--- Grade 3 tech (4) ---"
node gen-one.mjs 3 tech 4 2>&1

# Grade 8 coding (6)
echo "--- Grade 8 coding (6) ---"
node gen-one.mjs 8 coding 3 2>&1
node gen-one.mjs 8 coding 3 2>&1

# Grade 8 russian (3)
echo "--- Grade 8 russian (3) ---"
node gen-one.mjs 8 russian 3 2>&1

# Grade 2 english (3)
echo "--- Grade 2 english (3) ---"
node gen-one.mjs 2 english 3 2>&1

# Grade 2 projects (5)
echo "--- Grade 2 projects (5) ---"
node gen-one.mjs 2 projects 5 2>&1

echo "=== Batch 3 complete at: $(date) ==="
