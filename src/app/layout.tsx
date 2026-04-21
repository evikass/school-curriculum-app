import type { Metadata } from "next";
import { Geist, Geist_Mono, Nunito } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import VKBridge from "@/components/VKBridge";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const nunito = Nunito({
  variable: "--font-nunito",
  subsets: ["latin", "cyrillic"],
  weight: ["400", "600", "700", "800", "900"],
});

export const metadata: Metadata = {
  title: "ИНЕТШКОЛА - Полная школьная программа",
  description: "Интерактивная школьная программа для классов 0-11 с уроками и мини-играми по всем предметам.",
  keywords: ["школа", "уроки", "образование", "мини-игры", "учеба", "онлайн обучение", "ИНЕТШКОЛА"],
  authors: [{ name: "ИНЕТШКОЛА" }],
  manifest: "/manifest.json",
  icons: {
    icon: [
      { url: "/favicon.png", sizes: "192x192", type: "image/png" },
      { url: "/icon-192.png", sizes: "192x192", type: "image/png" },
      { url: "/icon-512.png", sizes: "512x512", type: "image/png" },
    ],
    apple: [
      { url: "/icon-192.png", sizes: "192x192", type: "image/png" },
    ],
  },
  openGraph: {
    title: "ИНЕТШКОЛА",
    description: "Полная школьная программа с мини-играми",
    url: "https://evikass.github.io/school-curriculum-app/",
    siteName: "ИНЕТШКОЛА",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "ИНЕТШКОЛА",
    description: "Полная школьная программа с мини-играми",
  },
};

export const viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  themeColor: "#7c3aed",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${nunito.variable} antialiased bg-background text-foreground`}
      >
        {children}
        <Toaster />
        <VKBridge />
      </body>
    </html>
  );
}
