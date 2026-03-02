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
  icons: {
    icon: "/school-curriculum-app/logo.svg",
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

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-background text-foreground`}
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
