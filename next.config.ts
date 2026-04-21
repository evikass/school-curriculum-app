import type { NextConfig } from "next";

// Для GitHub Pages: BASE_PATH=/school-curriculum-app npm run build
// Для Capacitor APK: npm run build (без BASE_PATH, по умолчанию '')
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
};

export default nextConfig;
