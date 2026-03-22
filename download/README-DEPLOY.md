# ВАЖНО: Развертывание v3.288

## Текущая проблема
На сайте https://evikass.github.io/school-curriculum-app/ всё ещё версия **v3.286**
Нужна версия **v3.288** с исправлениями VK Bridge

## Как развернуть

### Способ 1: Через Git (если у вас есть доступ)

```bash
cd /path/to/school-curriculum-app

# Скопируйте содержимое архива
tar -xzvf school-curriculum-app-v3.288.tar.gz

# Добавьте изменения
git add -A

# Создайте коммит
git commit -m "v3.288: VK Bridge local package + SVG fixes"

# Отправьте на GitHub
git push origin master
```

### Способ 2: Через GitHub Web Interface

1. Откройте https://github.com/evikass/school-curriculum-app
2. Скачайте архив `school-curriculum-app-v3.288.tar.gz`
3. Распакуйте папку `dist/`
4. Загрузите все файлы из `dist/` в репозиторий (drag & drop)
5. Подтвердите изменения

### Способ 3: Через GitHub CLI (gh)

```bash
gh auth login
cd /path/to/repo
gh repo clone evikass/school-curriculum-app
# скопируйте файлы из dist/
gh repo push
```

## После развертывания

1. Подождите 1-2 минуты пока GitHub Pages обновится
2. Проверьте версию: https://evikass.github.io/school-curriculum-app/
   - Должно показать **v3.288**
3. Очистите кэш в VK: Настройки → Приложения → ИНЕТШКОЛА → Очистить кэш
4. Откройте приложение заново

## Файлы для скачивания

- `/home/z/my-project/download/school-curriculum-app-v3.288.tar.gz` - полный архив
- `/home/z/my-project/download/deploy-v3.288.tar.gz` - только содержимое dist/
