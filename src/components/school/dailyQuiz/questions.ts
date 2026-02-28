export interface QuizQuestion {
  id: number
  question: string
  options: string[]
  correct: number
  subject: string
  difficulty: 1 | 2 | 3
}

export const quizQuestions: QuizQuestion[] = [
  // Математика
  { id: 1, question: "Сколько будет 15 + 27?", options: ["42", "41", "43", "40"], correct: 0, subject: "Математика", difficulty: 1 },
  { id: 2, question: "Какое число идёт после 99?", options: ["100", "101", "98", "110"], correct: 0, subject: "Математика", difficulty: 1 },
  { id: 3, question: "Сколько минут в часе?", options: ["60", "100", "24", "30"], correct: 0, subject: "Математика", difficulty: 1 },
  { id: 4, question: "Чему равно 8 × 7?", options: ["54", "56", "48", "64"], correct: 1, subject: "Математика", difficulty: 2 },
  { id: 5, question: "Какой результат деления 81 на 9?", options: ["8", "10", "9", "7"], correct: 2, subject: "Математика", difficulty: 2 },

  // Русский язык
  { id: 6, question: "Сколько букв в русском алфавите?", options: ["30", "33", "32", "31"], correct: 1, subject: "Русский язык", difficulty: 1 },
  { id: 7, question: "Какая часть речи обозначает действие?", options: ["Существительное", "Прилагательное", "Глагол", "Наречие"], correct: 2, subject: "Русский язык", difficulty: 1 },
  { id: 8, question: "Как пишется: жи-ши?", options: ["С буквой ы", "С буквой и", "Через ъ", "Через ь"], correct: 1, subject: "Русский язык", difficulty: 1 },
  { id: 9, question: "Какой падеж отвечает на вопрос 'кого, чего?'", options: ["Именительный", "Родительный", "Дательный", "Винительный"], correct: 1, subject: "Русский язык", difficulty: 2 },
  { id: 10, question: "Сколько падежей в русском языке?", options: ["5", "6", "7", "8"], correct: 1, subject: "Русский язык", difficulty: 2 },

  // Окружающий мир
  { id: 11, question: "Какое время года идёт после зимы?", options: ["Лето", "Осень", "Весна", "Зима"], correct: 2, subject: "Окружающий мир", difficulty: 1 },
  { id: 12, question: "Сколько планет в Солнечной системе?", options: ["8", "9", "7", "10"], correct: 0, subject: "Окружающий мир", difficulty: 1 },
  { id: 13, question: "Какое животное является символом России?", options: ["Тигр", "Медведь", "Орёл", "Волк"], correct: 1, subject: "Окружающий мир", difficulty: 1 },
  { id: 14, question: "Какой океан самый большой?", options: ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"], correct: 2, subject: "Окружающий мир", difficulty: 2 },
  { id: 15, question: "Сколько материков на Земле?", options: ["5", "6", "7", "8"], correct: 1, subject: "Окружающий мир", difficulty: 2 },

  // История
  { id: 16, question: "В каком году была Куликовская битва?", options: ["988", "1380", "1812", "1147"], correct: 1, subject: "История", difficulty: 3 },
  { id: 17, question: "Кто крестил Русь?", options: ["Пётр I", "Иван Грозный", "Князь Владимир", "Ярослав Мудрый"], correct: 2, subject: "История", difficulty: 2 },
  { id: 18, question: "Как называется древнее государство славян?", options: ["Россия", "Древняя Русь", "СССР", "Московское царство"], correct: 1, subject: "История", difficulty: 2 },

  // Биология
  { id: 19, question: "Какой орган перекачивает кровь?", options: ["Лёгкие", "Желудок", "Сердце", "Печень"], correct: 2, subject: "Биология", difficulty: 1 },
  { id: 20, question: "Что необходимо растениям для фотосинтеза?", options: ["Кислород", "Свет", "Азот", "Водород"], correct: 1, subject: "Биология", difficulty: 2 },

  // География
  { id: 21, question: "Столица России?", options: ["Санкт-Петербург", "Москва", "Казань", "Новосибирск"], correct: 1, subject: "География", difficulty: 1 },
  { id: 22, question: "Самая длинная река в России?", options: ["Волга", "Енисей", "Обь", "Лена"], correct: 3, subject: "География", difficulty: 3 },
  { id: 23, question: "Какое море омывает Россию с юга?", options: ["Баренцево", "Чёрное", "Балтийское", "Охотское"], correct: 1, subject: "География", difficulty: 2 },

  // Литература
  { id: 24, question: "Кто написал 'Сказку о рыбаке и рыбке'?", options: ["Толстой", "Пушкин", "Чехов", "Гоголь"], correct: 1, subject: "Литература", difficulty: 2 },
  { id: 25, question: "Кто автор басни 'Ворона и Лисица'?", options: ["Пушкин", "Крылов", "Есенин", "Тютчев"], correct: 1, subject: "Литература", difficulty: 2 },
]
