'use client'

import { Component, ReactNode } from 'react'

interface Props {
  children: ReactNode
  fallback?: ReactNode
}

interface State {
  hasError: boolean
  error: Error | null
  errorInfo: React.ErrorInfo | null
}

export default class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props)
    this.state = { hasError: false, error: null, errorInfo: null }
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error, errorInfo: null }
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('ErrorBoundary caught:', error, errorInfo)
    this.setState({ errorInfo })
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div className="p-6 bg-red-500/20 border-2 border-red-500 rounded-2xl text-white">
          <h2 className="text-2xl font-bold mb-4">Что-то пошло не так 😔</h2>
          <p className="mb-2 text-red-300">{this.state.error?.message}</p>
          <pre className="text-xs bg-black/30 p-2 rounded overflow-auto max-h-40">
            {this.state.errorInfo?.componentStack}
          </pre>
          <button 
            onClick={() => this.setState({ hasError: false, error: null, errorInfo: null })}
            className="mt-4 px-4 py-2 bg-white/20 rounded-xl hover:bg-white/30"
          >
            Попробовать снова
          </button>
        </div>
      )
    }

    return this.props.children
  }
}
