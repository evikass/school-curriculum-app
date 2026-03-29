'use client';

import { useEffect, useState } from 'react';

declare global {
  interface Window {
    vkBridge?: {
      send: (method: string, params?: Record<string, unknown>) => Promise<unknown>;
      subscribe: (listener: (event: { detail: { type: string; data: unknown } }) => void) => void;
      unsubscribe: (listener: (event: { detail: { type: string; data: unknown } }) => void) => void;
    };
  }
}

export default function VKBridge() {
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isVK, setIsVK] = useState(false);
  const [retryCount, setRetryCount] = useState(0);
  const [skipped, setSkipped] = useState(false);

  useEffect(() => {
    if (typeof window === 'undefined') return;

    // Detect VK environment - be more conservative
    // Only consider it VK if we have explicit VK indicators
    const checkVK = () => {
      const hasVKParam = new URLSearchParams(window.location.search).has('vk_platform');
      const hasVKAppId = new URLSearchParams(window.location.search).has('vk_app_id');
      const isVKDomain = window.location.hostname.includes('vk.com');
      const isVKReferrer = document.referrer.includes('vk.com');

      // Only return true if we have clear VK indicators
      return hasVKParam || hasVKAppId || isVKDomain || isVKReferrer;
    };

    const vkDetected = checkVK();
    setIsVK(vkDetected);

    if (!vkDetected) {
      setIsLoading(false);
      return;
    }

    // Reduced timeout - 5 seconds instead of 15
    const timeout = setTimeout(() => {
      if (isLoading) {
        setError('Таймаут: не удалось подключиться к VK. Нажмите "Пропустить" для продолжения.');
        setIsLoading(false);
      }
    }, 5000);

    // Load VK Bridge script
    const script = document.createElement('script');
    script.src = 'https://unpkg.com/@vkontakte/vk-bridge/dist/browser.min.js';
    script.async = true;

    script.onload = () => {
      initBridge();
    };

    script.onerror = () => {
      clearTimeout(timeout);
      setError('Не удалось загрузить VK Bridge. Проверьте интернет-соединение.');
      setIsLoading(false);
    };

    document.head.appendChild(script);

    function initBridge() {
      const bridge = window.vkBridge;
      if (!bridge) {
        clearTimeout(timeout);
        setError('VK Bridge не найден');
        setIsLoading(false);
        return;
      }

      // Initialize VK Mini App
      bridge.send('VKWebAppInit')
        .then(() => {
          clearTimeout(timeout);
          console.log('VK Mini App initialized');
          setIsLoading(false);

          // Configure appearance
          bridge.send('VKWebAppSetViewSettings', {
            status_bar_style: 'light',
            action_bar_color: '#1e1b4b',
            navigation_bar_color: '#1e1b4b',
          }).catch(() => {})

          // Get user info
          bridge.send('VKWebAppGetUserInfo')
            .then((user) => {
              console.log('VK User:', user);
            })
            .catch(() => {})

          // Enable swipe back
          bridge.send('VKWebAppEnableSwipeBackHistory')
            .catch(() => {})
        })
        .catch((err) => {
          clearTimeout(timeout);
          console.error('VK Init error:', err);
          setError('Ошибка инициализации VK. Попробуйте обновить страницу.');
          setIsLoading(false);
        });
    }

    return () => {
      clearTimeout(timeout);
    };
  }, [retryCount]);

  const handleRetry = () => {
    setIsLoading(true);
    setError(null);
    setRetryCount(prev => prev + 1);
  };

  const handleSkip = () => {
    setSkipped(true);
    setIsLoading(false);
    setError(null);
  };

  // Don't render anything if not in VK or if skipped
  if (!isVK || skipped) {
    return null;
  }

  // Show loading screen in VK
  if (isLoading) {
    return (
      <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900">
        <div className="text-center p-8">
          <div className="w-16 h-16 border-4 border-white/30 border-t-white rounded-full animate-spin mx-auto mb-4"></div>
          <h2 className="text-2xl font-bold text-white mb-2">ИНЕТШКОЛА</h2>
          <p className="text-purple-200 mb-4">Загрузка VK Mini App...</p>
          <button
            onClick={handleSkip}
            className="px-4 py-2 bg-white/10 hover:bg-white/20 text-white/70 hover:text-white rounded-lg text-sm transition-colors"
          >
            Пропустить
          </button>
        </div>
      </div>
    );
  }

  // Show error screen in VK
  if (error) {
    return (
      <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900">
        <div className="text-center p-8 max-w-md">
          <div className="text-6xl mb-4">😕</div>
          <h2 className="text-xl font-bold text-white mb-2">Ошибка соединения</h2>
          <p className="text-purple-200 mb-4">{error}</p>
          <div className="flex gap-3 justify-center flex-wrap">
            <button
              onClick={handleRetry}
              className="px-6 py-3 bg-purple-500 hover:bg-purple-400 text-white rounded-xl font-semibold transition-colors"
            >
              Попробовать снова
            </button>
            <button
              onClick={handleSkip}
              className="px-6 py-3 bg-white/10 hover:bg-white/20 text-white rounded-xl font-semibold transition-colors"
            >
              Пропустить
            </button>
          </div>
          <p className="text-purple-300/50 text-sm mt-4">
            Если проблема повторяется, проверьте интернет-соединение
          </p>
        </div>
      </div>
    );
  }

  return null;
}
