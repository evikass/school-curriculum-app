# Правила деплоя и работы с ветками

## Структура веток

| Ветка | Назначение | Содержимое |
|-------|------------|------------|
| `main` | Исходный код проекта | TypeScript, React компоненты, конфиги |
| `gh-pages` | Готовый сайт для публикации | Статический билд (HTML, CSS, JS) |

## Workflow

### 1. Разработка (в ветке `main`)
```bash
git checkout main
# Внесение изменений в исходный код
git add .
git commit -m "feat: описание изменений"
git push origin main
```

### 2. Деплой (публикация на gh-pages)
```bash
# 1. Переключиться на main и убедиться, что всё закоммичено
git checkout main

# 2. Собрать проект
npm install
npm run build

# 3. Экспортировать статические файлы (если настроено)
# или скопировать из out/ или dist/ в корень gh-pages

# 4. Пуш в gh-pages
# Вариант A: через git subtree (если out/ папка со статикой)
git subtree push --prefix out origin gh-pages

# Вариант B: вручную переключиться и скопировать
git checkout gh-pages
git checkout main -- out/ .
git add .
git commit -m "deploy: версия X.X.X"
git push origin gh-pages
git checkout main
```

## Правила

1. **Исходный код всегда правим в `main`**
2. **В `gh-pages` только пушим готовый билд** — не редактируем файлы напрямую
3. **Версию обновляем в `package.json` в ветке `main`**
4. **После изменений в `main` → собрать и задеплоить в `gh-pages`**

## Скрипт для автоматического деплоя

Добавить в `package.json`:
```json
{
  "scripts": {
    "deploy": "npm run build && git subtree push --prefix out origin gh-pages"
  }
}
```

Примечание: требует настройки `output: 'export'` в `next.config.ts` для генерации папки `out/`.
