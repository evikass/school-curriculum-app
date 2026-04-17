#!/bin/bash
cd /home/z/my-project/school-curriculum-app

echo "=== Starting batch 2 - Grade 5 ==="

# Grade 5 biology (12)
echo "--- Grade 5 biology (12) ---"
node gen-one.mjs 5 biology 6 2>&1
node gen-one.mjs 5 biology 6 2>&1

# Grade 5 music (12)
echo "--- Grade 5 music (12) ---"
node gen-one.mjs 5 music 6 2>&1
node gen-one.mjs 5 music 6 2>&1

# Grade 5 pe (12)
echo "--- Grade 5 pe (12) ---"
node gen-one.mjs 5 pe 6 2>&1
node gen-one.mjs 5 pe 6 2>&1

# Grade 5 crafts (11)
echo "--- Grade 5 crafts (11) ---"
node gen-one.mjs 5 crafts 6 2>&1
node gen-one.mjs 5 crafts 5 2>&1

# Grade 5 digital (10)
echo "--- Grade 5 digital (10) ---"
node gen-one.mjs 5 digital 5 2>&1
node gen-one.mjs 5 digital 5 2>&1

# Grade 5 finance (10)
echo "--- Grade 5 finance (10) ---"
node gen-one.mjs 5 finance 5 2>&1
node gen-one.mjs 5 finance 5 2>&1

# Grade 5 informatics (8)
echo "--- Grade 5 informatics (8) ---"
node gen-one.mjs 5 informatics 4 2>&1
node gen-one.mjs 5 informatics 4 2>&1

# Grade 5 robotics (10)
echo "--- Grade 5 robotics (10) ---"
node gen-one.mjs 5 robotics 5 2>&1
node gen-one.mjs 5 robotics 5 2>&1

echo "=== Batch 2 complete at: $(date) ==="
