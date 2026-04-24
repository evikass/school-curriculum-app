#!/usr/bin/env node
/**
 * Генератор последовательной версии
 * 
 * Читает текущий номер версии из version.txt, увеличивает на 1
 * и записывает в src/data/version.ts и package.json.
 * 
 * v3.676 → v3.677 → v3.678 → ...
 * Запускается перед каждой сборкой (npm run build).
 */
const fs = require('fs');
const path = require('path');

const versionFile = path.join(__dirname, '..', 'version.txt');
const versionTsFile = path.join(__dirname, '..', 'src', 'data', 'version.ts');
const packageFile = path.join(__dirname, '..', 'package.json');

// Читаем текущую версию из version.txt (или создаём с 676 если файла нет)
let currentMinor = 676;
if (fs.existsSync(versionFile)) {
  const content = fs.readFileSync(versionFile, 'utf8').trim();
  const parsed = parseInt(content, 10);
  if (!isNaN(parsed) && parsed > 0) {
    currentMinor = parsed;
  }
}

// Увеличиваем на 1
const newMinor = currentMinor + 1;
const versionString = 'v3.' + newMinor;

// Сохраняем новую версию в version.txt
fs.writeFileSync(versionFile, String(newMinor), 'utf8');

// Записываем version.ts
const versionTs = `// Автогенерируемый файл — НЕ РЕДАКТИРОВАТЬ ВРУЧНУЮ
// Генерируется скриптом scripts/generate-version.cjs
// Запускается перед каждой сборкой (npm run build)

export const APP_VERSION = '${versionString}'
`;

fs.writeFileSync(versionTsFile, versionTs, 'utf8');

// Обновляем package.json version
const pkg = JSON.parse(fs.readFileSync(packageFile, 'utf8'));
const oldVersion = pkg.version;
pkg.version = '3.' + newMinor;
fs.writeFileSync(packageFile, JSON.stringify(pkg, null, 2) + '\n', 'utf8');

console.log('🏷️  Version: v3.' + currentMinor + ' → ' + versionString);
console.log('✅ Updated version.txt, version.ts, package.json');
