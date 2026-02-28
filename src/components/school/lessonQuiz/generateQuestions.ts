import { QuestionItem } from './types'

export function generateQuestions(title: string, description: string): QuestionItem[] {
  const questions: QuestionItem[] = []

  // Question 1: Key term from title
  const keyTerms = title.match(/([А-ЯЁ][а-яё]+(?:\s+[а-яё]+)?)/g) || []
  if (keyTerms.length > 0) {
    questions.push({
      type: 'understanding',
      question: `Что означает термин "${keyTerms[0]}" в контексте данного урока?`,
      options: [description.slice(0, 50) + '...', 'Научное понятие из учебника', 'Непонятное слово', 'Простое выражение'],
      correct: 0,
      hint: 'Внимательно прочитай описание урока'
    })
  }

  // Question 2: Comprehension
  questions.push({
    type: 'comprehension',
    question: `Какое утверждение правильно описывает тему "${title}"?`,
    options: [description.slice(0, 60) + '...', 'Это сложная тема для взрослых', 'Это не важно для изучения', 'Это просто теория без практики'],
    correct: 0,
    hint: 'Ответ находится в описании урока'
  })

  // Question 3: Application
  questions.push({
    type: 'application',
    question: 'Для чего нужно изучать эту тему?',
    options: ['Чтобы лучше понимать мир вокруг', 'Это не нужно в жизни', 'Только для сдачи экзамена', 'Чтобы получить хорошую оценку'],
    correct: 0,
    hint: 'Знания помогают нам развиваться'
  })

  // Question 4: True/False
  questions.push({
    type: 'truefalse',
    question: `Верно ли, что "${title}" является важной темой для изучения?`,
    options: ['Верно', 'Неверно'],
    correct: 0,
    hint: 'Все темы в учебнике важны'
  })

  return questions
}
