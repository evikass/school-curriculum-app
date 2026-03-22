# ИНЕТШКОЛА v3.287 - Заметки к релизу

## Исправленные проблемы

### 1. SVG-изображения для уроков чтения (1 класс)
- **Проблема**: SVG-файлы не отображались на GitHub Pages из-за неправильного пути
- **Решение**: Добавлен basePath `/school-curriculum-app` ко всем путям изображений (20 файлов)
- Все 20 анимированных SVG теперь доступны по правильным URL:
  - `/school-curriculum-app/images/lessons/grade1/reading/lesson1-tongue-exercises.svg`
  - `/school-curriculum-app/images/lessons/grade1/reading/lesson2-lip-exercises.svg`
  - ... и так далее

### 2. Файлы для развертывания
- Скопированы все SVG-файлы в `dist/images/lessons/grade1/reading/`
- Создан архив для развертывания: `deploy-v3.287.tar.gz`

## Известные проблемы с VK Mini Apps

Если приложение не работает в VK Mini Apps ("нет соединения"):

1. **Проверьте URL приложения**
   - Убедитесь, что URL в настройках VK приложения: `https://evikass.github.io/school-curriculum-app/`
   - URL должен заканчиваться слешем

2. **Проверьте HTTPS**
   - VK Mini Apps требует HTTPS
   - GitHub Pages автоматически предоставляет HTTPS

3. **Очистите кэш**
   - В приложении VK: Настройки -> Приложения -> ИНЕТШКОЛА -> Очистить кэш
   - Или переустановите приложение

4. **Проверьте сетевое подключение**
   - VK может блокировать некоторые запросы в определенных регионах
   - Попробуйте использовать VPN

## Как развернуть обновление

### Вариант 1: Через GitHub (рекомендуется)
```bash
git pull origin master
npm run build
# Скопируйте содержимое dist/ в репозиторий
git add .
git commit -m "Update to v3.287"
git push
```

### Вариант 2: Прямое развертывание
1. Скачайте `deploy-v3.287.tar.gz`
2. Распакуйте в корневую директорию GitHub Pages репозитория
3. Запушьте изменения

## Структура файлов для развертывания

```
school-curriculum-app/
├── index.html
├── manifest.json
├── _next/
│   └── static/
│       ├── chunks/
│       └── media/
├── images/
│   └── lessons/
│       └── grade1/
│           └── reading/
│               ├── lesson1-tongue-exercises.svg
│               ├── lesson2-lip-exercises.svg
│               └── ... (20 SVG файлов)
├── store-assets/
└── ... другие файлы
```

## Версия
- **Текущая**: v3.287
- **Предыдущая**: v3.286
- **Дата**: 2025-03-23
