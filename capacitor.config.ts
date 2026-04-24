import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'ru.evika.inetshkola',
  appName: 'ИНЕТШКОЛА',
  webDir: 'out',
  server: {
    // Локальный сервер для обслуживания статики из assets
    androidScheme: 'https',
    cleartext: true,
  },
  plugins: {
    SplashScreen: {
      launchShowDuration: 2000,
      launchAutoHide: true,
      backgroundColor: '#1e1b4b',
      showSpinner: true,
      spinnerColor: '#7c3aed',
    },
  },
  android: {
    allowMixedContent: true,
  },
};

export default config;
