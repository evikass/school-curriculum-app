# Правила деплоя и работы с ветками

## Структура веток

| Ветка | Назначение | Содержимое |
|-------|------------|------------|
| `main` | Исходный код проекта | TypeScript, React компоненты, конфиги |
| `gh-pages` | Готовый сайт для публикации | Статический билд (HTML, CSS, JS) |

---

## ⚠️ Версия проекта — ОБЯЗАТЕЛЬНО менять при ЛЮБЫХ изменениях!

### Где менять версию (2 места):

| Файл | Строка | Пример |
|------|--------|--------|
| `package.json` | 3 | `"version": "3.373"` |
| `src/app/page.tsx` | 136 | `v3.373` |

### Правило:
```
При КАЖДОМ изменении кода → увеличить версию на +0.001
Пример: 3.372 → 3.373 → 3.374 → 3.375 ...
```

### Быстрый поиск версии в коде:
```bash
grep -n "version" package.json | head -1
grep -n "v3\." src/app/page.tsx
```

---

## Workflow (пошагово)

### Шаг 1: Разработка
```bash
git checkout main

# Внесение изменений в код...

# ⚠️ ОБНОВИТЬ ВЕРСИЮ в двух файлах:
# - package.json (строка 3)
# - src/app/page.tsx (строка 136)

git add .
git commit -m "feat: описание изменений"
git push origin main
```

### Шаг 2: Деплой на gh-pages
```bash
# 1. Собрать проект
npm run build

# 2. Переключиться на gh-pages
git checkout gh-pages

# 3. Очистить всё КРОМЕ .git
find . -maxdepth 1 -not -name '.git' -not -name '.' -delete

# 4. Скопировать билд из out/
cp -r out/* .

# 5. Удалить папку out
rm -rf out

# 6. Закоммитить и запушить
git add -A
git commit -m "deploy: vX.XXX - краткое описание"
git push origin gh-pages

# 7. Вернуться на main
git checkout main
```

---

## Правила (чеклист)

1. ✅ **Исходный код всегда правим в `main`**
2. ✅ **В `gh-pages` только пушим готовый билд** — не редактируем файлы напрямую
3. ✅ **Версию обновляем в ДВУХ местах** при каждом изменении:
   - `package.json`
   - `src/app/page.tsx`
4. ✅ **После изменений в `main` → собрать и задеплоить в `gh-pages`**
5. ✅ **Версия увеличивается на +0.001** (3.372 → 3.373)

---

## Пример полного цикла изменений

```bash
# === НАЧАЛО ===
git checkout main

# Редактируем код...
# Например: исправили ошибку в src/data/grades/11/economy/index.ts

# ⚠️ ОБНОВЛЯЕМ ВЕРСИЮ:
# package.json: "version": "3.372" → "version": "3.373"
# src/app/page.tsx: v3.372 → v3.373

# Коммитим в main
git add .
git commit -m "fix: 11th grade economy topics"
git push origin main

# === ДЕПЛОЙ ===
npm run build

git checkout gh-pages
find . -maxdepth 1 -not -name '.git' -not -name '.' -delete
cp -r out/* .
rm -rf out
git add -A
git commit -m "deploy: v3.373 - fix 11th grade economy topics"
git push origin gh-pages

git checkout main
# === КОНЕЦ ===
```

---

## Автоматизация (опционально)

Добавить в `package.json` скрипт для деплоя:
```json
{
  "scripts": {
    "deploy": "npm run build && git checkout gh-pages && find . -maxdepth 1 -not -name '.git' -not -name '.' -delete && cp -r out/* . && rm -rf out && git add -A && git commit -m 'deploy: new version' && git push origin gh-pages && git checkout main"
  }
}
```

Примечание: версия всё равно обновляется вручную перед запуском `npm run deploy`.
