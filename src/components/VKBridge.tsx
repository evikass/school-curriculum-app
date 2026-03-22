'use client';

import { useEffect } from 'react';
import bridge from '@vkontakte/vk-bridge';

export default function VKBridge() {
  useEffect(() => {
    if (typeof window === 'undefined') return;

    // Check if running inside VK
    const isVK = window.location !== window.parent.location ||
                 window.location.href.includes('vk.com') ||
                 navigator.userAgent.includes('VKApp') ||
                 new URLSearchParams(window.location.search).has('vk_platform');

    if (!isVK) return;

    async function initBridge() {
      try {
        // Initialize VK Mini App
        await bridge.send('VKWebAppInit');
        console.log('VK Bridge initialized');

        // Set appearance
        await bridge.send('VKWebAppSetViewSettings', {
          status_bar_style: 'light',
          action_bar_color: '#1e1b4b',
          navigation_bar_color: '#1e1b4b',
        }).catch(() => {});

        // Get user info
        const user = await bridge.send('VKWebAppGetUserInfo').catch(() => null);
        if (user) {
          console.log('VK user:', user);
        }
      } catch (error) {
        console.error('VK Bridge error:', error);
      }
    }

    initBridge();

    // Subscribe to VK events
    const unsubscribe = bridge.subscribe((event) => {
      console.log('VK event:', event.detail.type, event.detail.data);
    });

    return () => {
      unsubscribe?.();
    };
  }, []);

  return null;
}
