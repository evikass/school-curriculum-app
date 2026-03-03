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
<<<<<<< HEAD
  manifest: "/manifest.json",
  icons: {
    icon: [
      { url: "/favicon.ico", sizes: "48x48" },
      { url: "/icon-192.png", sizes: "192x192", type: "image/png" },
      { url: "/icon-512.png", sizes: "512x512", type: "image/png" },
    ],
    apple: [
      { url: "/icon-192.png", sizes: "192x192", type: "image/png" },
    ],
=======
  metadataBase: new URL('https://evikass.github.io/school-curriculum-app/'),
  icons: {
    icon: [
      { url: "/school-curriculum-app/favicon.ico", type: "image/x-icon" },
      { url: "/school-curriculum-app/icon.png", type: "image/png", sizes: "512x512" },
    ],
    apple: "/school-curriculum-app/icon.png",
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
  },
  openGraph: {
    title: "ИНЕТШКОЛА",
    description: "Полная школьная программа с мини-играми",
    url: "https://evikass.github.io/school-curriculum-app/",
    siteName: "ИНЕТШКОЛА",
    type: "website",
<<<<<<< HEAD
=======
    images: ["/school-curriculum-app/icon.png"],
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
  },
  twitter: {
    card: "summary_large_image",
    title: "ИНЕТШКОЛА",
    description: "Полная школьная программа с мини-играми",
<<<<<<< HEAD
  },
};

export const viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  themeColor: "#7c3aed",
};

=======
    images: ["/school-curriculum-app/icon.png"],
  },
};

>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-background text-foreground`}
<<<<<<< HEAD
=======
        suppressHydrationWarning
>>>>>>> e73dce10ee3b11e1d7702effc925444d9dfee03c
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
