#!/bin/bash
cd /home/z/my-project/school-curriculum-app

echo "=== Starting batch test generation ==="
echo "Started at: $(date)"

# Grade 10 coding - need 28 more (already have 4)
echo "--- Grade 10 coding (28 more) ---"
node gen-one.mjs 10 coding 8 2>&1
node gen-one.mjs 10 coding 8 2>&1
node gen-one.mjs 10 coding 8 2>&1
node gen-one.mjs 10 coding 4 2>&1

# Grade 10 economy - need 32
echo "--- Grade 10 economy (32) ---"
node gen-one.mjs 10 economy 8 2>&1
node gen-one.mjs 10 economy 8 2>&1
node gen-one.mjs 10 economy 8 2>&1
node gen-one.mjs 10 economy 8 2>&1

# Grade 10 lab (1) and philosophy (1)
echo "--- Grade 10 lab + philosophy ---"
node gen-one.mjs 10 lab 1 2>&1
node gen-one.mjs 10 philosophy 1 2>&1

# Grade 9 algebra (15)
echo "--- Grade 9 algebra (15) ---"
node gen-one.mjs 9 algebra 8 2>&1
node gen-one.mjs 9 algebra 7 2>&1

# Grade 9 informatics (2)
echo "--- Grade 9 informatics (2) ---"
node gen-one.mjs 9 informatics 2 2>&1

# Grade 11 algebra (13)
echo "--- Grade 11 algebra (13) ---"
node gen-one.mjs 11 algebra 8 2>&1
node gen-one.mjs 11 algebra 5 2>&1

echo "=== Batch 1 complete at: $(date) ==="
