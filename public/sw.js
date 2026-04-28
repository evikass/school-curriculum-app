// Service Worker для ИНЕТШКОЛА — оффлайн-поддержка для мобильного приложения
const CACHE_NAME = 'inetshkola-v3.721';
const STATIC_CACHE = 'inetshkola-static-v3.721';
const DATA_CACHE = 'inetshkola-data-v3.721';

// Ресурсы для предварительного кэширования (критические)
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/favicon.png',
  '/icon-192.png',
  '/icon-512.png',
];

// Установка Service Worker
self.addEventListener('install', (event) => {
  console.log('[SW] Установка Service Worker');
  event.waitUntil(
    caches.open(STATIC_CACHE).then((cache) => {
      console.log('[SW] Предварительное кэширование критических ресурсов');
      return cache.addAll(PRECACHE_URLS).catch((err) => {
        console.warn('[SW] Не все ресурсы удалось закэшировать при установке:', err);
      });
    })
  );
  // Активируем сразу без ожидания
  self.skipWaiting();
});

// Активация Service Worker
self.addEventListener('activate', (event) => {
  console.log('[SW] Активация Service Worker');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== STATIC_CACHE && name !== DATA_CACHE)
          .map((name) => {
            console.log('[SW] Удаление старого кэша:', name);
            return caches.delete(name);
          })
      );
    })
  );
  self.clients.claim();
});

// Стратегия: Network First с fallback на кэш для навигации
// Cache First для статических ресурсов (JS, CSS, шрифты)
// Network First для данных (JSON)

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // Пропускаем non-GET запросы
  if (event.request.method !== 'GET') return;

  // Пропускаем chrome-extension и другие не-http(s) запросы
  if (!url.protocol.startsWith('http')) return;

  // Пропускаем запросы к внешним API (z-ai-web-dev-sdk и прочие)
  if (url.hostname !== self.location.hostname) return;

  // Навигационные запросы (HTML страницы) — Network First
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          const responseClone = response.clone();
          caches.open(STATIC_CACHE).then((cache) => {
            cache.put(event.request, responseClone);
          });
          return response;
        })
        .catch(() => {
          return caches.match(event.request).then((cachedResponse) => {
            return cachedResponse || caches.match('/index.html');
          });
        })
    );
    return;
  }

  // JSON данные (bundle-файлы, предметы) — Network First с кэшем
  if (url.pathname.endsWith('.json')) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          const responseClone = response.clone();
          caches.open(DATA_CACHE).then((cache) => {
            cache.put(event.request, responseClone);
          });
          return response;
        })
        .catch(() => {
          return caches.match(event.request);
        })
    );
    return;
  }

  // Статические ресурсы (JS, CSS, изображения, шрифты) — Cache First
  if (
    url.pathname.match(/\.(js|css|png|jpg|jpeg|gif|svg|ico|webp|woff2?|ttf|eot)$/) ||
    url.pathname.includes('/_next/static/') ||
    url.pathname.includes('/images/') ||
    url.pathname.includes('/data/')
  ) {
    event.respondWith(
      caches.match(event.request).then((cachedResponse) => {
        if (cachedResponse) {
          // Фоновое обновление кэша
          fetch(event.request).then((response) => {
            if (response && response.ok) {
              caches.open(STATIC_CACHE).then((cache) => {
                cache.put(event.request, response);
              });
            }
          }).catch(() => {});
          return cachedResponse;
        }
        return fetch(event.request).then((response) => {
          if (response && response.ok) {
            const responseClone = response.clone();
            caches.open(STATIC_CACHE).then((cache) => {
              cache.put(event.request, responseClone);
            });
          }
          return response;
        });
      })
    );
    return;
  }

  // Всё остальное — Network First
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response && response.ok) {
          const responseClone = response.clone();
          caches.open(STATIC_CACHE).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        return caches.match(event.request);
      })
  );
});
