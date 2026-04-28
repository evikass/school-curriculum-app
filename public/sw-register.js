// Регистрация Service Worker для мобильного приложения
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').then((registration) => {
      console.log('[App] Service Worker зарегистрирован, scope:', registration.scope);

      // Проверяем обновления каждые 30 минут
      setInterval(() => {
        registration.update().catch(() => {});
      }, 30 * 60 * 1000);
    }).catch((error) => {
      console.warn('[App] Не удалось зарегистрировать Service Worker:', error);
    });
  });
}
