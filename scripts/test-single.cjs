const {execSync} = require("child_process");
const fs = require("fs");

// Test grade 1/art
const tsPath = "src/data/grades/1/art/index.ts";
let content = fs.readFileSync(tsPath, "utf-8");
content = content.replace(/from\s*["']@\/data\/types["']/g, 'from "/tmp/types.ts"');
fs.writeFileSync("/tmp/test1art.ts", content);
fs.writeFileSync("/tmp/types.ts", "export const SubjectData={};export const GameLesson={};");

const entry = 'import * as d from "/tmp/test1art.ts";console.log(JSON.stringify({l:!!d.lessons,g:!!d.games}));';
fs.writeFileSync("/tmp/entry1art.mjs", entry);

try {
  execSync("npx esbuild /tmp/entry1art.mjs --bundle --outfile=/tmp/bundle1art.mjs --format=esm --platform=node --log-level=error", {timeout: 30000});
  console.log("esbuild OK, bundle size:", fs.statSync("/tmp/bundle1art.mjs").size);
  const output = execSync("node /tmp/bundle1art.mjs", {encoding: "utf-8", timeout: 10000, maxBuffer: 10*1024*1024});
  console.log("Result:", output.substring(0, 80));
} catch(e) {
  const err = (e.stderr || e.message || "").substring(0, 500);
  console.log("Error:", err);
}
