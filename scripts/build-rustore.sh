#!/bin/bash
# Скрипт сборки APK для RuStore
# Использование: ./scripts/build-rustore.sh [debug|release]
#
# Для публикации в RuStore:
# 1. Соберите release: ./scripts/build-rustore.sh release
# 2. Загрузите inetshkola-*-rustore.apk на https://rustore.ru/
# 3. Заполните информацию о приложении (иконки, скриншоты — в public/store-assets/)
#
# Важно: сохраните keystore (inetshkola-keystore.jks) и пароль!
# Без них невозможно обновлять приложение в RuStore.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BUILD_TYPE="${1:-release}"

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

success() { echo -e "${GREEN}✅ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }
info() { echo -e "${YELLOW}ℹ️  $1${NC}"; }

# Проверка JAVA_HOME
if [ -z "$JAVA_HOME" ]; then
    if [ -d "/home/z/jdk-21" ]; then
        export JAVA_HOME=/home/z/jdk-21
    else
        error "JAVA_HOME не установлен. Установите JDK 21."
    fi
fi
export PATH=$JAVA_HOME/bin:$PATH

# Проверка ANDROID_HOME
if [ -z "$ANDROID_HOME" ]; then
    if [ -d "/home/z/android-sdk" ]; then
        export ANDROID_HOME=/home/z/android-sdk
        export ANDROID_SDK_ROOT=/home/z/android-sdk
    else
        error "ANDROID_HOME не установлен. Установите Android SDK."
    fi
fi
export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH

echo "📱 ИНЕТШКОЛА — Сборка APK для RuStore"
echo "======================================"
echo "Тип сборки: $BUILD_TYPE"
echo "Java: $(java -version 2>&1 | head -1)"
echo "Android SDK: $ANDROID_HOME"
echo ""

# Шаг 1: Сборка Next.js (без basePath)
info "Шаг 1/5: Сборка Next.js (Capacitor mode)..."
cd "$PROJECT_ROOT"
npm run build:capacitor

# Шаг 2: Замена манифеста для Capacitor
info "Шаг 2/5: Подготовка манифеста для Capacitor..."
cp out/manifest.json out/manifest-github.json
cp out/manifest-capacitor.json out/manifest.json

# Шаг 3: Синхронизация с Capacitor
info "Шаг 3/5: Синхронизация с Android проектом..."
npx cap sync android

# Шаг 4: Сборка APK
info "Шаг 4/5: Сборка APK ($BUILD_TYPE)..."
cd "$PROJECT_ROOT/android"

if [ "$BUILD_TYPE" = "debug" ]; then
    ./gradlew assembleDebug
    APK_PATH="app/build/outputs/apk/debug/app-debug.apk"
    OUTPUT_NAME="inetshkola-$(node -p "require('$PROJECT_ROOT/package.json').version")-debug.apk"
else
    ./gradlew assembleRelease
    APK_PATH="app/build/outputs/apk/release/app-release-unsigned.apk"

    # Подписание APK
    KEYSTORE="${RUSTORE_KEYSTORE:-$PROJECT_ROOT/../download/inetshkola-keystore.jks}"
    KEY_ALIAS="${RUSTORE_KEY_ALIAS:-inetshkola}"
    KEY_PASS="${RUSTORE_KEY_PASS:-inetshkola2024}"

    if [ -f "$KEYSTORE" ]; then
        info "Подписание APK..."
        jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
            -keystore "$KEYSTORE" \
            -storepass "$KEY_PASS" \
            -keypass "$KEY_PASS" \
            "$APK_PATH" "$KEY_ALIAS"

        # Zipalign
        OUTPUT_NAME="inetshkola-$(node -p "require('$PROJECT_ROOT/package.json').version")-rustore.apk"
        info "Zipalign..."
        $ANDROID_HOME/build-tools/34.0.0/zipalign -v 4 "$APK_PATH" "$PROJECT_ROOT/../download/$OUTPUT_NAME"
    else
        info "Keystore не найден, пропускаем подписание."
        OUTPUT_NAME="inetshkola-$(node -p "require('$PROJECT_ROOT/package.json').version")-release-unsigned.apk"
        cp "$APK_PATH" "$PROJECT_ROOT/../download/$OUTPUT_NAME"
    fi
fi

# Шаг 5: Копирование в download
info "Шаг 5/5: Копирование APK..."
mkdir -p "$PROJECT_ROOT/../download"
if [ "$BUILD_TYPE" = "debug" ]; then
    cp "$APK_PATH" "$PROJECT_ROOT/../download/$OUTPUT_NAME"
fi

success "APK создан: download/$OUTPUT_NAME"
ls -lh "$PROJECT_ROOT/../download/$OUTPUT_NAME"

echo ""
echo "📋 Следующие шаги для публикации в RuStore:"
echo "  1. Перейдите на https://rustore.ru/profile/developer"
echo "  2. Создайте новое приложение"
echo "  3. Загрузите APK файл: download/$OUTPUT_NAME"
echo "  4. Заполните описание (шаблон в app-store-builds/store-assets/descriptions/rustore.txt)"
echo "  5. Загрузите иконки и скриншоты (из public/store-assets/)"
echo "  6. Укажите политику конфиденциальности (public/store-assets/privacy-policy-ru.html)"
echo ""
echo "⚠️  ВАЖНО: Сохраните keystore файл и пароль! Без них нельзя обновлять приложение!"
