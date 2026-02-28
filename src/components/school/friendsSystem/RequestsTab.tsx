'use client'

export function RequestsTab() {
  const requests = [
    { name: 'Иван', avatar: '👦', grade: '5 класс', xp: '450 XP' },
    { name: 'Елена', avatar: '👧', grade: '3 класс', xp: '820 XP' }
  ]

  return (
    <div className="space-y-3">
      {requests.map((req, idx) => (
        <div key={idx} className="bg-white/5 rounded-xl p-3 flex items-center gap-3">
          <span className="text-2xl">{req.avatar}</span>
          <div className="flex-1">
            <p className="text-white">{req.name} хочет дружить</p>
            <p className="text-white/50 text-sm">{req.grade} • {req.xp}</p>
          </div>
          <div className="flex gap-2">
            <button className="px-3 py-1.5 bg-green-500 hover:bg-green-600 text-white rounded-lg text-sm">
              Принять
            </button>
            <button className="px-3 py-1.5 bg-white/10 hover:bg-white/20 text-white rounded-lg text-sm">
              ✕
            </button>
          </div>
        </div>
      ))}
    </div>
  )
}
