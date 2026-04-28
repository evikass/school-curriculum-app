import type { NextConfig } from "next";

// Для GitHub Pages: BASE_PATH=/school-curriculum-app npm run build
// Для Capacitor APK: npm run build:capacitor (без BASE_PATH, по умолчанию '')
const basePath = process.env.BASE_PATH || '';

const nextConfig: NextConfig = {
  output: 'export',
  trailingSlash: true,
  basePath: basePath || undefined,
  images: {
    unoptimized: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
  // Service Worker и Capacitor-манифест — статические файлы из public/
  // Они копируются как есть в выходную директорию
  headers: async () => [
    {
      source: '/sw.js',
      headers: [
        {
          key: 'Cache-Control',
          value: 'no-cache, no-store, must-revalidate',
        },
        {
          key: 'Service-Worker-Allowed',
          value: '/',
        },
      ],
    },
  ],
};

export default nextConfig;
