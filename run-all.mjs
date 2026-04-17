#!/usr/bin/env node
// Batch runner - generates all missing tests, 1 per AI call
import { execSync } from 'child_process';

// All subjects needing tests: [grade, dir, needed]
const JOBS = [
  // Grade 10 coding - 32 needed (have 9 after previous runs, actually recount later)
  ...Array(32).fill([10, 'coding']),
  // Grade 10 economy - 32
  ...Array(32).fill([10, 'economy']),
  // Grade 10 lab - 1
  ...Array(1).fill([10, 'lab']),
  // Grade 10 philosophy - 1
  ...Array(1).fill([10, 'philosophy']),
  // Grade 9 algebra - 15
  ...Array(15).fill([9, 'algebra']),
  // Grade 9 informatics - 2
  ...Array(2).fill([9, 'informatics']),
  // Grade 11 algebra - 13
  ...Array(13).fill([11, 'algebra']),
  // Grade 5
  ...Array(12).fill([5, 'biology']),
  ...Array(12).fill([5, 'music']),
  ...Array(12).fill([5, 'pe']),
  ...Array(11).fill([5, 'crafts']),
  ...Array(10).fill([5, 'digital']),
  ...Array(10).fill([5, 'finance']),
  ...Array(8).fill([5, 'informatics']),
  ...Array(10).fill([5, 'robotics']),
  // Grade 6
  ...Array(10).fill([6, 'chemistry']),
  ...Array(10).fill([6, 'crafts']),
  ...Array(9).fill([6, 'ecology']),
  ...Array(9).fill([6, 'informatics']),
  ...Array(9).fill([6, 'physics']),
  ...Array(9).fill([6, 'robotics']),
  ...Array(9).fill([6, 'social']),
  ...Array(4).fill([6, 'math']),
  // Grade 3
  ...Array(7).fill([3, 'art']),
  ...Array(8).fill([3, 'informatics']),
  ...Array(8).fill([3, 'pe']),
  ...Array(7).fill([3, 'safety']),
  ...Array(4).fill([3, 'music']),
  ...Array(4).fill([3, 'tech']),
  // Grade 8
  ...Array(6).fill([8, 'coding']),
  ...Array(3).fill([8, 'russian']),
  // Grade 2
  ...Array(3).fill([2, 'english']),
  ...Array(5).fill([2, 'projects']),
];

console.log(`Total jobs: ${JOBS.length}`);

let ok = 0, fail = 0, skip = 0;
const startIdx = parseInt(process.argv[2]) || 0;

for (let i = startIdx; i < JOBS.length; i++) {
  const [grade, dir] = JOBS[i];
  process.stdout.write(`[${i+1}/${JOBS.length}] ${grade}/${dir} ... `);
  try {
    const out = execSync(`node gen-one.mjs ${grade} ${dir} 1`, {
      cwd: '/home/z/my-project/school-curriculum-app',
      timeout: 60000,
      stdio: ['pipe', 'pipe', 'pipe']
    }).toString();
    
    if (out.includes('Done!')) {
      console.log('OK');
      ok++;
    } else if (out.includes('No lessons need')) {
      console.log('SKIP (no lessons)');
      skip++;
    } else {
      console.log('WARN:', out.trim().split('\n').pop());
      ok++;
    }
  } catch (e) {
    const err = e.stderr?.toString() || e.message;
    if (err.includes('No lessons need')) {
      console.log('SKIP');
      skip++;
    } else {
      console.log('FAIL');
      fail++;
    }
  }
}

console.log(`\nResults: OK=${ok}, FAIL=${fail}, SKIP=${skip}, Total=${JOBS.length}`);
