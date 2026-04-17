#!/bin/bash
cd /home/z/my-project/school-curriculum-app
G="node gen-one.mjs"

echo "=== $(date) Starting ==="

# Helper function
run() {
  for i in $(seq 1 $2); do
    $G $1 1 >/dev/null 2>&1 || true
  done
  echo "  $1: $2 tests done"
}

echo "--- Grade 10 coding (32) ---"
for i in $(seq 1 32); do $G 10 coding 1 >/dev/null 2>&1; done
echo "  coding: 32 done"

echo "--- Grade 10 economy (32) ---"
for i in $(seq 1 32); do $G 10 economy 1 >/dev/null 2>&1; done
echo "  economy: 32 done"

echo "--- Grade 10 lab (1) + philosophy (1) ---"
$G 10 lab 1 >/dev/null 2>&1
$G 10 philosophy 1 >/dev/null 2>&1
echo "  lab+philosophy: done"

echo "--- Grade 9 algebra (15) ---"
for i in $(seq 1 15); do $G 9 algebra 1 >/dev/null 2>&1; done
echo "  algebra: 15 done"

echo "--- Grade 9 informatics (2) ---"
$G 9 informatics 1 >/dev/null 2>&1
$G 9 informatics 1 >/dev/null 2>&1
echo "  informatics: 2 done"

echo "--- Grade 11 algebra (13) ---"
for i in $(seq 1 13); do $G 11 algebra 1 >/dev/null 2>&1; done
echo "  algebra: 13 done"

echo "--- Grade 5 biology (12) ---"
for i in $(seq 1 12); do $G 5 biology 1 >/dev/null 2>&1; done
echo "  biology: 12 done"

echo "--- Grade 5 music (12) ---"
for i in $(seq 1 12); do $G 5 music 1 >/dev/null 2>&1; done
echo "  music: 12 done"

echo "--- Grade 5 pe (12) ---"
for i in $(seq 1 12); do $G 5 pe 1 >/dev/null 2>&1; done
echo "  pe: 12 done"

echo "--- Grade 5 crafts (11) ---"
for i in $(seq 1 11); do $G 5 crafts 1 >/dev/null 2>&1; done
echo "  crafts: 11 done"

echo "--- Grade 5 digital (10) ---"
for i in $(seq 1 10); do $G 5 digital 1 >/dev/null 2>&1; done
echo "  digital: 10 done"

echo "--- Grade 5 finance (10) ---"
for i in $(seq 1 10); do $G 5 finance 1 >/dev/null 2>&1; done
echo "  finance: 10 done"

echo "--- Grade 5 informatics (8) ---"
for i in $(seq 1 8); do $G 5 informatics 1 >/dev/null 2>&1; done
echo "  informatics: 8 done"

echo "--- Grade 5 robotics (10) ---"
for i in $(seq 1 10); do $G 5 robotics 1 >/dev/null 2>&1; done
echo "  robotics: 10 done"

echo "--- Grade 6 chemistry (10) ---"
for i in $(seq 1 10); do $G 6 chemistry 1 >/dev/null 2>&1; done
echo "  chemistry: 10 done"

echo "--- Grade 6 crafts (10) ---"
for i in $(seq 1 10); do $G 6 crafts 1 >/dev/null 2>&1; done
echo "  crafts: 10 done"

echo "--- Grade 6 ecology (9) ---"
for i in $(seq 1 9); do $G 6 ecology 1 >/dev/null 2>&1; done
echo "  ecology: 9 done"

echo "--- Grade 6 informatics (9) ---"
for i in $(seq 1 9); do $G 6 informatics 1 >/dev/null 2>&1; done
echo "  informatics: 9 done"

echo "--- Grade 6 physics (9) ---"
for i in $(seq 1 9); do $G 6 physics 1 >/dev/null 2>&1; done
echo "  physics: 9 done"

echo "--- Grade 6 robotics (9) ---"
for i in $(seq 1 9); do $G 6 robotics 1 >/dev/null 2>&1; done
echo "  robotics: 9 done"

echo "--- Grade 6 social (9) ---"
for i in $(seq 1 9); do $G 6 social 1 >/dev/null 2>&1; done
echo "  social: 9 done"

echo "--- Grade 6 math (4) ---"
for i in $(seq 1 4); do $G 6 math 1 >/dev/null 2>&1; done
echo "  math: 4 done"

echo "--- Grade 3 art (7) ---"
for i in $(seq 1 7); do $G 3 art 1 >/dev/null 2>&1; done
echo "  art: 7 done"

echo "--- Grade 3 informatics (8) ---"
for i in $(seq 1 8); do $G 3 informatics 1 >/dev/null 2>&1; done
echo "  informatics: 8 done"

echo "--- Grade 3 pe (8) ---"
for i in $(seq 1 8); do $G 3 pe 1 >/dev/null 2>&1; done
echo "  pe: 8 done"

echo "--- Grade 3 safety (7) ---"
for i in $(seq 1 7); do $G 3 safety 1 >/dev/null 2>&1; done
echo "  safety: 7 done"

echo "--- Grade 3 music (4) ---"
for i in $(seq 1 4); do $G 3 music 1 >/dev/null 2>&1; done
echo "  music: 4 done"

echo "--- Grade 3 tech (4) ---"
for i in $(seq 1 4); do $G 3 tech 1 >/dev/null 2>&1; done
echo "  tech: 4 done"

echo "--- Grade 8 coding (6) ---"
for i in $(seq 1 6); do $G 8 coding 1 >/dev/null 2>&1; done
echo "  coding: 6 done"

echo "--- Grade 8 russian (3) ---"
for i in $(seq 1 3); do $G 8 russian 1 >/dev/null 2>&1; done
echo "  russian: 3 done"

echo "--- Grade 2 english (3) ---"
for i in $(seq 1 3); do $G 2 english 1 >/dev/null 2>&1; done
echo "  english: 3 done"

echo "--- Grade 2 projects (5) ---"
for i in $(seq 1 5); do $G 2 projects 1 >/dev/null 2>&1; done
echo "  projects: 5 done"

echo "=== $(date) ALL DONE ==="
