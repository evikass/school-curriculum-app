#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
  echo "$(date) - Trying lesson $i"
  node gen-lesson.mjs $i 2>&1
  if [ $? -eq 0 ]; then
    echo "$(date) - Lesson $i SUCCESS"
  else
    echo "$(date) - Lesson $i FAILED"
  fi
  sleep 3
done
echo "$(date) - ALL DONE"
