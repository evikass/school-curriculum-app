import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "ИНЕТШКОЛА - Полная школьная программа",
  description: "Интерактивная школьная программа для классов 0-11 с уроками и мини-играми по всем предметам.",
  keywords: ["школа", "уроки", "образование", "мини-игры", "учеба", "онлайн обучение", "ИНЕТШКОЛА"],
  authors: [{ name: "ИНЕТШКОЛА" }],
  metadataBase: new URL('https://evikass.github.io/school-curriculum-app/'),
  icons: {
    icon: [
      { url: "/school-curriculum-app/favicon.ico", type: "image/x-icon" },
      { url: "/school-curriculum-app/icon.png", type: "image/png", sizes: "512x512" },
    ],
    apple: "/school-curriculum-app/icon.png",
  },
  openGraph: {
    title: "ИНЕТШКОЛА",
    description: "Полная школьная программа с мини-играми",
    url: "https://evikass.github.io/school-curriculum-app/",
    siteName: "ИНЕТШКОЛА",
    type: "website",
    images: ["/school-curriculum-app/icon.png"],
  },
  twitter: {
    card: "summary_large_image",
    title: "ИНЕТШКОЛА",
    description: "Полная школьная программа с мини-играми",
    images: ["/school-curriculum-app/icon.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-background text-foreground`}
        suppressHydrationWarning
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
