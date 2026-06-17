import { writeFileSync } from 'fs';

// We'll use sucrase to transpile TS to JS
import { transform } from 'sucrase';

const code = `
import { SubjectData, GameLesson } from '@/data/types'
const L = (title, description, tasks, image, content, examples, facts, keyPoints) => ({ title, description, tasks, image, content, examples, facts, keyPoints })
`;

const tsCode = code + `
export const lessons = ${JSON.stringify(null)}; // placeholder
`;

// Read the actual file
import { readFileSync } from 'fs';
const sourceCode = readFileSync('/home/z/my-project/school-curriculum-app/src/data/grades/10/history-russia/index.ts', 'utf-8');

// Transform TS to JS
const result = transform(sourceCode, { transforms: ['typescript', 'imports'] });

// Write to temp file
writeFileSync('/tmp/history-russia.mjs', result.code);
console.log("Transformed successfully");
