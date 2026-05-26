// Экспорт игр для 7 класса
import { GameLesson } from '../types'

export const seventhGradeGames: GameLesson[] = [
  {
    title: "Причастие",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Причастие — это:", options: ["Прилагательное", "Глагол", "Особая форма глагола", "Наречие", "Существительное"], correctAnswer: "Особая форма глагола", hint: "Причастие = признак по действию" },
      { type: 'quiz', question: "Причастие отвечает на вопрос:", options: ["Кто?", "Сколько?", "Как?", "Какой?", "Что делать?"], correctAnswer: "Какой?", hint: "Какой? — как прилагательное" },
      { type: 'quiz', question: "Признак причастия от глагола:", options: ["Склонение", "Время и вид", "Число", "Падеж", "Род"], correctAnswer: "Время и вид", hint: "Причастие имеет время и вид" },
      { type: 'quiz', question: "Действительное причастие:", options: ["Только настоящее время", "Совершает действие само", "Действие совершается над ним", "Не имеет действия", "Только прошедшее время"], correctAnswer: "Совершает действие само", hint: "Действительное — само совершает" },
      { type: 'quiz', question: "Страдательное причастие:", options: ["Только прошедшее время", "Не имеет действия", "Совершает действие само", "Только настоящее время", "Действие совершается над ним"], correctAnswer: "Действие совершается над ним", hint: "Страдательное — над ним совершают" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Причастие»! 🎉" }
  },
  {
    title: "Деепричастие",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Деепричастие обозначает:", options: ["Признак предмета", "Количество", "Добавочное действие", "Место", "Основное действие"], correctAnswer: "Добавочное действие", hint: "Деепричастие — добавочное действие" },
      { type: 'quiz', question: "Деепричастие отвечает на вопрос:", options: ["Сколько?", "Какой?", "Кто?", "Что делать?", "Что делая? Что сделав?"], correctAnswer: "Что делая? Что сделав?", hint: "Что делая? что сделав?" },
      { type: 'quiz', question: "Деепричастный оборот выделяется:", options: ["Тире", "Двоеточием", "Запятыми", "Скобками", "Не выделяется"], correctAnswer: "Запятыми", hint: "Деепричастный оборот обособляется" },
      { type: 'quiz', question: "Деепричастие — неизменяемая форма:", options: ["По роду", "По лицу", "По падежу", "По числу", "По всем признакам"], correctAnswer: "По всем признакам", hint: "Деепричастие не изменяется" },
      { type: 'quiz', question: "Какое слово — деепричастие?", options: ["Прочитанный", "Читая", "Читать", "Читающий", "Читальный"], correctAnswer: "Читая", hint: "Читая — что делая?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Деепричастие»! 🎉" }
  },
  {
    title: "Синтаксис сложного предложения",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сложносочинённое предложение связывается:", options: ["Частицами", "Сочинительными союзами", "Подчинительными союзами", "Предлогами", "Интонацией"], correctAnswer: "Сочинительными союзами", hint: "И, а, но, или" },
      { type: 'quiz', question: "Сложноподчинённое предложение связывается:", options: ["Предлогами", "Подчинительными союзами", "Интонацией", "Сочинительными союзами", "Частицами"], correctAnswer: "Подчинительными союзами", hint: "Что, чтобы, если, когда" },
      { type: 'quiz', question: "Бессоюзное предложение связывается:", options: ["Предлогами", "Местоимениями", "Интонацией", "Союзами", "Частицами"], correctAnswer: "Интонацией", hint: "Без союзов — по смыслу" },
      { type: 'quiz', question: "Сколько грамматических основ в сложном предложении?", options: ["Четыре", "Две или больше", "Одна", "Пять", "Три"], correctAnswer: "Две или больше", hint: "Сложное = 2+ простых" },
      { type: 'quiz', question: "Какой союз — подчинительный?", options: ["Или", "А", "Но", "И", "Что"], correctAnswer: "Что", hint: "Что — подчинительный союз" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Синтаксис сложного предложения»! 🎉" }
  },
  {
    title: "Достоевский",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Достоевский родился в:", options: ["1815", "1821", "1819", "1825", "1830"], correctAnswer: "1821", hint: "Москва, 1821" },
      { type: 'quiz', question: "Родион Раскольников — герой:", options: ["Братьев Карамазовых", "Идиота", "Преступления и наказания", "Подростка", "Бесов"], correctAnswer: "Преступления и наказания", hint: "Главный герой романа" },
      { type: 'quiz', question: "Теория Раскольникова о:", options: ["Боге", "Тварях дрожащих и Право имеющих", "Деньгах", "Любви", "Свободе"], correctAnswer: "Тварях дрожащих и Право имеющих", hint: "Два типа людей" },
      { type: 'quiz', question: "«Братья Карамазовы» — автор:", options: ["Тургенев", "Гоголь", "Достоевский", "Чехов", "Толстой"], correctAnswer: "Достоевский", hint: "Ф.М. Достоевский" },
      { type: 'quiz', question: "Достоевский — великий:", options: ["Психолог", "Путешественник", "Историк", "Политик", "Учёный"], correctAnswer: "Психолог", hint: "Глубокий психологизм" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Достоевский»! 🎉" }
  },
  {
    title: "Уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "x + 5 = 12, x = ?", options: ["5", "7", "17", "8", "6"], correctAnswer: "7", hint: "x = 12 - 5" },
      { type: 'quiz', question: "3x = 18, x = ?", options: ["5", "6", "9", "4", "7"], correctAnswer: "6", hint: "x = 18 ÷ 3" },
      { type: 'quiz', question: "2x + 4 = 14, x = ?", options: ["10", "4", "5", "6", "7"], correctAnswer: "5", hint: "2x = 10, x = 5" },
      { type: 'quiz', question: "x - 8 = 15, x = ?", options: ["23", "7", "17", "20", "13"], correctAnswer: "23", hint: "x = 15 + 8" },
      { type: 'quiz', question: "x/3 = 9, x = ?", options: ["27", "6", "12", "3", "18"], correctAnswer: "27", hint: "x = 9 × 3" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Уравнения»! 🎉" }
  },
  {
    title: "Неравенства",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "При делении на отрицательное число знак:", options: ["Удваивается", "Меняется", "Не меняется", "Исчезает", "Становится ="], correctAnswer: "Меняется", hint: "Важно: минус меняет знак!" },
      { type: 'quiz', question: "Решить: 2x > 6", options: ["x = 3", "x > 3", "x > 4", "x < 3", "x < 4"], correctAnswer: "x > 3", hint: "x > 6/2" },
      { type: 'quiz', question: "Решить: -x > 5", options: ["x < 5", "x > -5", "x > 5", "x < -5", "x = -5"], correctAnswer: "x < -5", hint: "При делении на -1 знак меняется" },
      { type: 'quiz', question: "Решить: x + 2 > 7", options: ["x > 9", "x > 5", "x < 9", "x > 4", "x < 5"], correctAnswer: "x > 5", hint: "x > 7 - 2" },
      { type: 'quiz', question: "Решить: 3x < 12", options: ["x < 3", "x > 4", "x < 4", "x = 4", "x > 3"], correctAnswer: "x < 4", hint: "x < 12/3" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Неравенства»! 🎉" }
  },
  {
    title: "Степени и корни",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2³ = ?", options: ["12", "8", "4", "9", "6"], correctAnswer: "8", hint: "2 × 2 × 2 = 8" },
      { type: 'quiz', question: "5⁰ = ?", options: ["5", "0", "1", "25", "10"], correctAnswer: "1", hint: "Любое число в степени 0 = 1" },
      { type: 'quiz', question: "√81 = ?", options: ["9", "7", "8", "10", "6"], correctAnswer: "9", hint: "9 × 9 = 81" },
      { type: 'quiz', question: "3² = ?", options: ["6", "9", "8", "12", "3"], correctAnswer: "9", hint: "3 × 3 = 9" },
      { type: 'quiz', question: "√100 = ?", options: ["8", "12", "11", "10", "9"], correctAnswer: "10", hint: "10 × 10 = 100" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Степени и корни»! 🎉" }
  },
  {
    title: "Треугольники",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сумма углов треугольника:", options: ["360°", "180°", "120°", "90°", "270°"], correctAnswer: "180°", hint: "Сумма всегда 180°" },
      { type: 'quiz', question: "Прямоугольный треугольник имеет угол:", options: ["90°", "45°", "60°", "120°", "180°"], correctAnswer: "90°", hint: "Прямой угол = 90°" },
      { type: 'quiz', question: "Равносторонний треугольник имеет углы:", options: ["45°", "90°", "30°", "120°", "60°"], correctAnswer: "60°", hint: "Все углы равны: 180°/3" },
      { type: 'quiz', question: "Гипотенуза — это сторона:", options: ["Напротив прямого угла", "Любая", "Самая короткая", "Медиана", "Прилежащая к углу"], correctAnswer: "Напротив прямого угла", hint: "Гипотенуза — самая длинная" },
      { type: 'quiz', question: "Пифагорова теорема:", options: ["a + b = c", "a² + b² = c²", "a × b = c", "a² - b² = c²", "2a + 2b = c"], correctAnswer: "a² + b² = c²", hint: "Для прямоугольного треугольника" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Треугольники»! 🎉" }
  },
  {
    title: "Окружность",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Вписанный угол равен:", options: ["Острым углам", "Удвоенной дуге", "Дуге", "Половине дуги", "Центральному углу"], correctAnswer: "Половине дуги", hint: "Вписанный = ½ центрального" },
      { type: 'quiz', question: "Длина окружности C = ?", options: ["πr", "4πr", "2πr", "2πd", "πr²"], correctAnswer: "2πr", hint: "C = 2πr" },
      { type: 'quiz', question: "Площадь круга S = ?", options: ["πr²", "πd", "2πr²", "πr", "2πr"], correctAnswer: "πr²", hint: "S = πr²" },
      { type: 'quiz', question: "Угол на диаметр:", options: ["Прямой (90°)", "0°", "Тупой", "Острый", "Развёрнутый"], correctAnswer: "Прямой (90°)", hint: "Всегда 90°" },
      { type: 'quiz', question: "Радиус — это:", options: ["Секущая", "Диаметр", "Половина диаметра", "Дуга", "Хорда"], correctAnswer: "Половина диаметра", hint: "r = d/2" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Окружность»! 🎉" }
  },
  {
    title: "Механика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Единица силы:", options: ["Килограмм (кг)", "Джоуль (Дж)", "Ньютон (Н)", "Ватт (Вт)", "Паскаль (Па)"], correctAnswer: "Ньютон (Н)", hint: "Н = кг·м/с²" },
      { type: 'quiz', question: "F = m × a — это:", options: ["Закон Ома", "Закон Гука", "Закон Архимеда", "Закон всемирного тяготения", "Второй закон Ньютона"], correctAnswer: "Второй закон Ньютона", hint: "Сила = масса × ускорение" },
      { type: 'quiz', question: "Ускорение свободного падения ≈", options: ["15 м/с²", "3.14 м/с²", "10.8 м/с²", "5 м/с²", "9.8 м/с²"], correctAnswer: "9.8 м/с²", hint: "g ≈ 9.8 м/с²" },
      { type: 'quiz', question: "Закон сохранения энергии:", options: ["E = 0", "E = const", "E уменьшается", "E растёт", "E = mc²"], correctAnswer: "E = const", hint: "Энергия не исчезает" },
      { type: 'quiz', question: "Работа измеряется в:", options: ["Вольтах (В)", "Джоулях (Дж)", "Ньютонах (Н)", "Паскалях (Па)", "Ваттах (Вт)"], correctAnswer: "Джоулях (Дж)", hint: "Дж = Н·м" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Механика»! 🎉" }
  },
  {
    title: "Оптика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Угол падения равен:", options: ["Двойному углу", "180°", "Углу отражения", "Половине угла отражения", "Нулю"], correctAnswer: "Углу отражения", hint: "Закон отражения" },
      { type: 'quiz', question: "Линза, собирающая лучи:", options: ["Вогнутая (рассеивающая)", "Сферическая", "Плоская", "Выпуклая (собирающая)", "Цилиндрическая"], correctAnswer: "Выпуклая (собирающая)", hint: "Выпуклая — собирающая" },
      { type: 'quiz', question: "Оптическая сила D = ?", options: ["F²", "1/F", "F", "F/2", "2F"], correctAnswer: "1/F", hint: "Д = 1/f (диоптрии)" },
      { type: 'quiz', question: "Показатель преломления стекла ≈", options: ["2", "1.5", "0.5", "3", "1"], correctAnswer: "1.5", hint: "Стекло преломляет свет" },
      { type: 'quiz', question: "Радуга — это результат:", options: ["Отражения", "Рассеяния", "Поглощения", "Дисперсии света", "Поляризации"], correctAnswer: "Дисперсии света", hint: "Разложение белого света" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Оптика»! 🎉" }
  },
  {
    title: "Первая мировая война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда началась Первая мировая?", options: ["1905", "1917", "1914", "1912", "1939"], correctAnswer: "1914", hint: "28 июля 1914 года" },
      { type: 'quiz', question: "Повод к войне:", options: ["Экономический кризис", "Нападение на Польшу", "Теракт", "Революция", "Убийство эрцгерцога Франца Фердинанда"], correctAnswer: "Убийство эрцгерцога Франца Фердинанда", hint: "Сараевское убийство" },
      { type: 'quiz', question: "Когда Россия вышла из войны?", options: ["1917", "1914", "1918", "1915", "1916"], correctAnswer: "1917", hint: "После революции" },
      { type: 'quiz', question: "Страны Антанты:", options: ["Германия, Австрия", "Россия, Франция, Англия", "США, Япония", "Италия, Турция", "Германия, Италия"], correctAnswer: "Россия, Франция, Англия", hint: "Антанта = союз" },
      { type: 'quiz', question: "Война закончилась в:", options: ["1917", "1918", "1914", "1920", "1916"], correctAnswer: "1918", hint: "11 ноября 1918" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Первая мировая война»! 🎉" }
  },
  {
    title: "Революция 1917",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Февральская революция:", options: ["Октябрь 1917", "Ноябрь 1917", "Январь 1917", "Февраль 1917", "Март 1917"], correctAnswer: "Февраль 1917", hint: "Свержение монархии" },
      { type: 'quiz', question: "Последний император:", options: ["Екатерина II", "Александр III", "Пётр I", "Николай II", "Александр II"], correctAnswer: "Николай II", hint: "Николай II отрёкся в 1917" },
      { type: 'quiz', question: "Октябрьскую революцию возглавил:", options: ["Столыпин", "Троцкий", "Николай II", "Керенский", "Ленин"], correctAnswer: "Ленин", hint: "Большевики и Ленин" },
      { type: 'quiz', question: "Что провозгласили большевики?", options: ["Демократию", "Власть Советов", "Монархию", "Республику", "Империю"], correctAnswer: "Власть Советов", hint: "Советская власть" },
      { type: 'quiz', question: "Гражданская война:", options: ["1920-1925", "1917-1922", "1914-1918", "1910-1915", "1925-1930"], correctAnswer: "1917-1922", hint: "После революции" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Революция 1917»! 🎉" }
  },
  {
    title: "Генетика",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Ген — это:", options: ["Ткань", "Участок ДНК", "Белок", "Клетка", "Орган"], correctAnswer: "Участок ДНК", hint: "Ген кодирует признак" },
      { type: 'quiz', question: "Гомозигота — это:", options: ["Aa", "aB", "AA или aa", "AB", "Ab"], correctAnswer: "AA или aa", hint: "Одинаковые аллели" },
      { type: 'quiz', question: "Первый закон Менделя:", options: ["Расщепление", "Единообразие гибридов", "Доминирование", "Сцепление", "Независимое наследование"], correctAnswer: "Единообразие гибридов", hint: "AA × aa → Aa" },
      { type: 'quiz', question: "Расщепление Aa × Aa по фенотипу:", options: ["2:1", "9:3:3:1", "1:1", "3:1", "1:2:1"], correctAnswer: "3:1", hint: "Второй закон Менделя" },
      { type: 'quiz', question: "Гетерозигота:", options: ["Aa", "bb", "aa", "BB", "AA"], correctAnswer: "Aa", hint: "Разные аллели" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Генетика»! 🎉" }
  },
  {
    title: "План и карта",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Что показывает масштаб?", options: ["Степень уменьшения", "Направление", "Расстояние", "Площадь", "Высоту"], correctAnswer: "Степень уменьшения", hint: "Во сколько раз уменьшено" },
      { type: 'quiz', question: "Стороны горизонта:", options: ["Тут, там", "Лево, право", "Север, юг, восток, запад", "Верх, низ", "Близко, далеко"], correctAnswer: "Север, юг, восток, запад", hint: "4 основных направления" },
      { type: 'quiz', question: "Масштаб 1:1000 означает:", options: ["1 см = 10 м", "1 см = 1 км", "1 см = 1000 см", "1 см = 100 м", "1 см = 1 м"], correctAnswer: "1 см = 1000 см", hint: "В 1000 раз больше" },
      { type: 'quiz', question: "Горизонталь на карте показывает:", options: ["Осадки", "Ветер", "Рельеф", "Давление", "Температуру"], correctAnswer: "Рельеф", hint: "Одинаковая высота" },
      { type: 'quiz', question: "Азимут измеряется в:", options: ["Метрах", "Градусах", "Километрах", "Минутах", "Секундах"], correctAnswer: "Градусах", hint: "От 0° до 360°" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «План и карта»! 🎉" }
  },
  {
    title: "Мировой океан",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Сколько океанов на Земле?", options: ["6", "4", "3", "5", "7"], correctAnswer: "5", hint: "Тихий, Атлантический, Индийский, Сев. Ледовитый, Южный" },
      { type: 'quiz', question: "Самый большой океан:", options: ["Северный Ледовитый", "Атлантический", "Индийский", "Тихий", "Южный"], correctAnswer: "Тихий", hint: "Тихий — самый большой" },
      { type: 'quiz', question: "Самый тёплый океан:", options: ["Атлантический", "Индийский", "Северный Ледовитый", "Тихий", "Южный"], correctAnswer: "Индийский", hint: "Индийский — самый тёплый" },
      { type: 'quiz', question: "Солёность океанской воды:", options: ["100‰", "0‰", "35‰", "50‰", "10‰"], correctAnswer: "35‰", hint: "В среднем 35 промилле" },
      { type: 'quiz', question: "Море — это часть:", options: ["Пролива", "Озера", "Океана", "Залива", "Реки"], correctAnswer: "Океана", hint: "Море принадлежит океану" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Мировой океан»! 🎉" }
  },
  {
    title: "Present Perfect",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I have ___ this book.", options: ["reading", "reads", "readen", "readed", "read"], correctAnswer: "read", hint: "have + V3" },
      { type: 'quiz', question: "She has ___ London.", options: ["visit", "visits", "visited", "visiting", "visitied"], correctAnswer: "visited", hint: "has + V3 (+ed)" },
      { type: 'quiz', question: "Present Perfect для:", options: ["Будущего", "Привычек", "Результата в настоящем", "Процесса", "Прошлого времени"], correctAnswer: "Результата в настоящем", hint: "Результат важен сейчас" },
      { type: 'quiz', question: "Маркер Present Perfect:", options: ["Yesterday", "Just", "Two days ago", "Last week", "In 2020"], correctAnswer: "Just", hint: "Just, already, ever, never" },
      { type: 'quiz', question: "I have ___ known that.", options: ["already", "ago", "yesterday", "in 2020", "last week"], correctAnswer: "already", hint: "Already = уже" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Present Perfect»! 🎉" }
  },
  {
    title: "Modal Verbs",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ swim. (могу)", options: ["should", "must", "may", "can", "would"], correctAnswer: "can", hint: "Can = мочь" },
      { type: 'quiz', question: "You ___ do homework. (должен)", options: ["can", "could", "should", "may", "must"], correctAnswer: "must", hint: "Must = обязан" },
      { type: 'quiz', question: "You ___ see a doctor. (следует)", options: ["must", "may", "should", "will", "can"], correctAnswer: "should", hint: "Should = следует" },
      { type: 'quiz', question: "___ I come in? (Можно?)", options: ["Must", "May", "Will", "Should", "Can"], correctAnswer: "May", hint: "May = можно (разрешение)" },
      { type: 'quiz', question: "___ you help me? (Можешь?)", options: ["Could", "Must", "May", "Should", "Will"], correctAnswer: "Could", hint: "Could = вежливая просьба" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Modal Verbs»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Пластика", "Металла", "Древесины", "Резины", "Стекла"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Резания", "Клея", "Шитья", "Рисования", "Лепки"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Рисования", "Соединения деталей", "Резания", "Измерения", "Лепки"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Молоток", "Ножницы", "Кисть", "Карандаш", "Линейка"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Рисование", "Лепка", "Шитьё", "Вязание", "Искусство складывания бумаги"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Жёлтое", "Зелёное", "Фиолетовое", "Красное", "Синее"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Оранжевый", "Зелёный", "Красный", "Коричневый", "Фиолетовый"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Синяя", "Зелёная", "Красная", "Жёлтая", "Белая"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Синий", "Зелёный", "Фиолетовый", "Коричневый", "Оранжевый"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Оранжевый", "Зелёный", "Жёлтый", "Коричневый", "Фиолетовый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Флейта 🎶", "Гитара 🎸", "Скрипка 🎻", "Барабан 🥁", "Пианино 🎹"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["8", "12", "7", "6", "5"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Скрипка 🎻", "Гитара 🎸", "Барабан 🥁", "Труба 🎺", "Пианино 🎹"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Бубен", "Труба 🎺", "Гитара 🎸", "Барабан 🥁", "Флейта 🎶"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Цирком", "Оркестром", "Кинотеатром", "Хором", "Театром"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ракеткой", "Руками", "Клюшкой", "Без мяча", "Ногами и мячом ⚽"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["9", "6", "7", "5", "11"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Сидеть весь день", "Есть конфеты", "Зарядка", "Не спать", "Мало двигаться"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Без мяча", "Клюшкой", "Ногами", "Руками и мячом 🏀", "Ракеткой"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["7", "1", "2", "3-4", "0"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Безопасность",
    subject: "ОБЖ",
    icon: "Shield",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: "При пожаре нужно звонить:", options: ["103", "102", "104", "112", "101"], correctAnswer: "101", hint: "Пожарная служба" },
      { type: 'quiz', question: "Скорая помощь:", options: ["104", "101", "103", "112", "102"], correctAnswer: "103", hint: "Медицинская помощь" },
      { type: 'quiz', question: "Полиция:", options: ["104", "103", "102", "112", "101"], correctAnswer: "102", hint: "Полицейская служба" },
      { type: 'quiz', question: "Единый номер экстренной помощи:", options: ["112", "102", "103", "101", "104"], correctAnswer: "112", hint: "Единый номер" },
      { type: 'quiz', question: "При пожаре НЕЛЬЗЯ:", options: ["Прятаться", "Эвакуироваться", "Дышать через влажную ткань", "Идти к выходу", "Звонить 101"], correctAnswer: "Прятаться", hint: "Нельзя прятаться!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Безопасность»! 🎉" }
  },
]
