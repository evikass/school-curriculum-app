// Экспорт игр для 9 класса
import { GameLesson } from '../types'

export const ninthGradeGames: GameLesson[] = [
  {
    title: "Причастие",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Причастие — это:", options: ["Глагол", "Существительное", "Прилагательное", "Наречие", "Особая форма глагола"], correctAnswer: "Особая форма глагола", hint: "Причастие = признак по действию" },
      { type: 'quiz', question: "Причастие отвечает на вопрос:", options: ["Что делать?", "Кто?", "Какой?", "Как?", "Сколько?"], correctAnswer: "Какой?", hint: "Какой? — как прилагательное" },
      { type: 'quiz', question: "Признак причастия от глагола:", options: ["Род", "Падеж", "Склонение", "Число", "Время и вид"], correctAnswer: "Время и вид", hint: "Причастие имеет время и вид" },
      { type: 'quiz', question: "Действительное причастие:", options: ["Совершает действие само", "Действие совершается над ним", "Только настоящее время", "Не имеет действия", "Только прошедшее время"], correctAnswer: "Совершает действие само", hint: "Действительное — само совершает" },
      { type: 'quiz', question: "Страдательное причастие:", options: ["Только прошедшее время", "Только настоящее время", "Действие совершается над ним", "Совершает действие само", "Не имеет действия"], correctAnswer: "Действие совершается над ним", hint: "Страдательное — над ним совершают" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Причастие»! 🎉" }
  },
  {
    title: "Деепричастие",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Деепричастие обозначает:", options: ["Признак предмета", "Основное действие", "Добавочное действие", "Место", "Количество"], correctAnswer: "Добавочное действие", hint: "Деепричастие — добавочное действие" },
      { type: 'quiz', question: "Деепричастие отвечает на вопрос:", options: ["Сколько?", "Кто?", "Что делать?", "Что делая? Что сделав?", "Какой?"], correctAnswer: "Что делая? Что сделав?", hint: "Что делая? что сделав?" },
      { type: 'quiz', question: "Деепричастный оборот выделяется:", options: ["Тире", "Не выделяется", "Запятыми", "Скобками", "Двоеточием"], correctAnswer: "Запятыми", hint: "Деепричастный оборот обособляется" },
      { type: 'quiz', question: "Деепричастие — неизменяемая форма:", options: ["По числу", "По падежу", "По лицу", "По роду", "По всем признакам"], correctAnswer: "По всем признакам", hint: "Деепричастие не изменяется" },
      { type: 'quiz', question: "Какое слово — деепричастие?", options: ["Читающий", "Читать", "Читальный", "Прочитанный", "Читая"], correctAnswer: "Читая", hint: "Читая — что делая?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Деепричастие»! 🎉" }
  },
  {
    title: "Синтаксис сложного предложения",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сложносочинённое предложение связывается:", options: ["Сочинительными союзами", "Интонацией", "Подчинительными союзами", "Частицами", "Предлогами"], correctAnswer: "Сочинительными союзами", hint: "И, а, но, или" },
      { type: 'quiz', question: "Сложноподчинённое предложение связывается:", options: ["Интонацией", "Сочинительными союзами", "Частицами", "Предлогами", "Подчинительными союзами"], correctAnswer: "Подчинительными союзами", hint: "Что, чтобы, если, когда" },
      { type: 'quiz', question: "Бессоюзное предложение связывается:", options: ["Местоимениями", "Союзами", "Интонацией", "Предлогами", "Частицами"], correctAnswer: "Интонацией", hint: "Без союзов — по смыслу" },
      { type: 'quiz', question: "Сколько грамматических основ в сложном предложении?", options: ["Пять", "Четыре", "Одна", "Три", "Две или больше"], correctAnswer: "Две или больше", hint: "Сложное = 2+ простых" },
      { type: 'quiz', question: "Какой союз — подчинительный?", options: ["Или", "Что", "Но", "И", "А"], correctAnswer: "Что", hint: "Что — подчинительный союз" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Синтаксис сложного предложения»! 🎉" }
  },
  {
    title: "Достоевский",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Достоевский родился в:", options: ["1825", "1815", "1830", "1821", "1819"], correctAnswer: "1821", hint: "Москва, 1821" },
      { type: 'quiz', question: "Родион Раскольников — герой:", options: ["Идиота", "Преступления и наказания", "Бесов", "Братьев Карамазовых", "Подростка"], correctAnswer: "Преступления и наказания", hint: "Главный герой романа" },
      { type: 'quiz', question: "Теория Раскольникова о:", options: ["Деньгах", "Боге", "Любви", "Тварях дрожащих и Право имеющих", "Свободе"], correctAnswer: "Тварях дрожащих и Право имеющих", hint: "Два типа людей" },
      { type: 'quiz', question: "«Братья Карамазовы» — автор:", options: ["Толстой", "Достоевский", "Чехов", "Тургенев", "Гоголь"], correctAnswer: "Достоевский", hint: "Ф.М. Достоевский" },
      { type: 'quiz', question: "Достоевский — великий:", options: ["Путешественник", "Историк", "Психолог", "Учёный", "Политик"], correctAnswer: "Психолог", hint: "Глубокий психологизм" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Достоевский»! 🎉" }
  },
  {
    title: "Уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "x + 5 = 12, x = ?", options: ["6", "8", "17", "5", "7"], correctAnswer: "7", hint: "x = 12 - 5" },
      { type: 'quiz', question: "3x = 18, x = ?", options: ["9", "7", "6", "4", "5"], correctAnswer: "6", hint: "x = 18 ÷ 3" },
      { type: 'quiz', question: "2x + 4 = 14, x = ?", options: ["6", "7", "10", "5", "4"], correctAnswer: "5", hint: "2x = 10, x = 5" },
      { type: 'quiz', question: "x - 8 = 15, x = ?", options: ["20", "23", "13", "7", "17"], correctAnswer: "23", hint: "x = 15 + 8" },
      { type: 'quiz', question: "x/3 = 9, x = ?", options: ["12", "27", "3", "6", "18"], correctAnswer: "27", hint: "x = 9 × 3" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Уравнения»! 🎉" }
  },
  {
    title: "Неравенства",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "При делении на отрицательное число знак:", options: ["Удваивается", "Не меняется", "Становится =", "Исчезает", "Меняется"], correctAnswer: "Меняется", hint: "Важно: минус меняет знак!" },
      { type: 'quiz', question: "Решить: 2x > 6", options: ["x > 3", "x = 3", "x < 3", "x > 4", "x < 4"], correctAnswer: "x > 3", hint: "x > 6/2" },
      { type: 'quiz', question: "Решить: -x > 5", options: ["x > 5", "x > -5", "x = -5", "x < 5", "x < -5"], correctAnswer: "x < -5", hint: "При делении на -1 знак меняется" },
      { type: 'quiz', question: "Решить: x + 2 > 7", options: ["x > 4", "x > 5", "x > 9", "x < 9", "x < 5"], correctAnswer: "x > 5", hint: "x > 7 - 2" },
      { type: 'quiz', question: "Решить: 3x < 12", options: ["x > 3", "x < 3", "x > 4", "x = 4", "x < 4"], correctAnswer: "x < 4", hint: "x < 12/3" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Неравенства»! 🎉" }
  },
  {
    title: "Степени и корни",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2³ = ?", options: ["8", "12", "6", "9", "4"], correctAnswer: "8", hint: "2 × 2 × 2 = 8" },
      { type: 'quiz', question: "5⁰ = ?", options: ["0", "5", "1", "10", "25"], correctAnswer: "1", hint: "Любое число в степени 0 = 1" },
      { type: 'quiz', question: "√81 = ?", options: ["6", "7", "9", "10", "8"], correctAnswer: "9", hint: "9 × 9 = 81" },
      { type: 'quiz', question: "3² = ?", options: ["8", "3", "6", "12", "9"], correctAnswer: "9", hint: "3 × 3 = 9" },
      { type: 'quiz', question: "√100 = ?", options: ["12", "9", "8", "11", "10"], correctAnswer: "10", hint: "10 × 10 = 100" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Степени и корни»! 🎉" }
  },
  {
    title: "Треугольники",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сумма углов треугольника:", options: ["120°", "360°", "90°", "270°", "180°"], correctAnswer: "180°", hint: "Сумма всегда 180°" },
      { type: 'quiz', question: "Прямоугольный треугольник имеет угол:", options: ["60°", "90°", "180°", "120°", "45°"], correctAnswer: "90°", hint: "Прямой угол = 90°" },
      { type: 'quiz', question: "Равносторонний треугольник имеет углы:", options: ["60°", "45°", "30°", "120°", "90°"], correctAnswer: "60°", hint: "Все углы равны: 180°/3" },
      { type: 'quiz', question: "Гипотенуза — это сторона:", options: ["Напротив прямого угла", "Прилежащая к углу", "Самая короткая", "Медиана", "Любая"], correctAnswer: "Напротив прямого угла", hint: "Гипотенуза — самая длинная" },
      { type: 'quiz', question: "Пифагорова теорема:", options: ["a × b = c", "a + b = c", "2a + 2b = c", "a² + b² = c²", "a² - b² = c²"], correctAnswer: "a² + b² = c²", hint: "Для прямоугольного треугольника" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Треугольники»! 🎉" }
  },
  {
    title: "Окружность",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Вписанный угол равен:", options: ["Половине дуги", "Острым углам", "Центральному углу", "Удвоенной дуге", "Дуге"], correctAnswer: "Половине дуги", hint: "Вписанный = ½ центрального" },
      { type: 'quiz', question: "Длина окружности C = ?", options: ["πr", "2πd", "2πr", "πr²", "4πr"], correctAnswer: "2πr", hint: "C = 2πr" },
      { type: 'quiz', question: "Площадь круга S = ?", options: ["2πr²", "2πr", "πd", "πr", "πr²"], correctAnswer: "πr²", hint: "S = πr²" },
      { type: 'quiz', question: "Угол на диаметр:", options: ["0°", "Тупой", "Развёрнутый", "Прямой (90°)", "Острый"], correctAnswer: "Прямой (90°)", hint: "Всегда 90°" },
      { type: 'quiz', question: "Радиус — это:", options: ["Секущая", "Хорда", "Дуга", "Половина диаметра", "Диаметр"], correctAnswer: "Половина диаметра", hint: "r = d/2" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Окружность»! 🎉" }
  },
  {
    title: "Механика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Единица силы:", options: ["Ватт (Вт)", "Килограмм (кг)", "Джоуль (Дж)", "Ньютон (Н)", "Паскаль (Па)"], correctAnswer: "Ньютон (Н)", hint: "Н = кг·м/с²" },
      { type: 'quiz', question: "F = m × a — это:", options: ["Второй закон Ньютона", "Закон Архимеда", "Закон Гука", "Закон всемирного тяготения", "Закон Ома"], correctAnswer: "Второй закон Ньютона", hint: "Сила = масса × ускорение" },
      { type: 'quiz', question: "Ускорение свободного падения ≈", options: ["10.8 м/с²", "5 м/с²", "15 м/с²", "3.14 м/с²", "9.8 м/с²"], correctAnswer: "9.8 м/с²", hint: "g ≈ 9.8 м/с²" },
      { type: 'quiz', question: "Закон сохранения энергии:", options: ["E уменьшается", "E растёт", "E = const", "E = mc²", "E = 0"], correctAnswer: "E = const", hint: "Энергия не исчезает" },
      { type: 'quiz', question: "Работа измеряется в:", options: ["Паскалях (Па)", "Джоулях (Дж)", "Ньютонах (Н)", "Ваттах (Вт)", "Вольтах (В)"], correctAnswer: "Джоулях (Дж)", hint: "Дж = Н·м" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Механика»! 🎉" }
  },
  {
    title: "Оптика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Угол падения равен:", options: ["180°", "Нулю", "Половине угла отражения", "Углу отражения", "Двойному углу"], correctAnswer: "Углу отражения", hint: "Закон отражения" },
      { type: 'quiz', question: "Линза, собирающая лучи:", options: ["Вогнутая (рассеивающая)", "Плоская", "Сферическая", "Выпуклая (собирающая)", "Цилиндрическая"], correctAnswer: "Выпуклая (собирающая)", hint: "Выпуклая — собирающая" },
      { type: 'quiz', question: "Оптическая сила D = ?", options: ["2F", "1/F", "F²", "F/2", "F"], correctAnswer: "1/F", hint: "Д = 1/f (диоптрии)" },
      { type: 'quiz', question: "Показатель преломления стекла ≈", options: ["1", "1.5", "3", "0.5", "2"], correctAnswer: "1.5", hint: "Стекло преломляет свет" },
      { type: 'quiz', question: "Радуга — это результат:", options: ["Отражения", "Поглощения", "Поляризации", "Рассеяния", "Дисперсии света"], correctAnswer: "Дисперсии света", hint: "Разложение белого света" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Оптика»! 🎉" }
  },
  {
    title: "Основы химии",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Формула воды:", options: ["NaCl", "CO₂", "O₂", "H₂O", "H₂SO₄"], correctAnswer: "H₂O", hint: "Вода = водород + кислород" },
      { type: 'quiz', question: "pH нейтральной среды:", options: ["7", "0", "14", "1", "5"], correctAnswer: "7", hint: "pH 7 = нейтрально" },
      { type: 'quiz', question: "Кислота + основание =", options: ["Соль + вода", "Основание", "Кислота", "Металл", "Оксид"], correctAnswer: "Соль + вода", hint: "Реакция нейтрализации" },
      { type: 'quiz', question: "Формула серной кислоты:", options: ["H₂SO₄", "CH₃COOH", "H₃PO₄", "HCl", "HNO₃"], correctAnswer: "H₂SO₄", hint: "Серная кислота" },
      { type: 'quiz', question: "Типы химических реакций:", options: ["Только соединения", "Соединения, разложения, замещения", "Только разложения", "Только замещения", "Только обмена"], correctAnswer: "Соединения, разложения, замещения", hint: "4 основных типа" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Основы химии»! 🎉" }
  },
  {
    title: "Первая мировая война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда началась Первая мировая?", options: ["1912", "1917", "1905", "1939", "1914"], correctAnswer: "1914", hint: "28 июля 1914 года" },
      { type: 'quiz', question: "Повод к войне:", options: ["Экономический кризис", "Теракт", "Нападение на Польшу", "Убийство эрцгерцога Франца Фердинанда", "Революция"], correctAnswer: "Убийство эрцгерцога Франца Фердинанда", hint: "Сараевское убийство" },
      { type: 'quiz', question: "Когда Россия вышла из войны?", options: ["1917", "1914", "1918", "1916", "1915"], correctAnswer: "1917", hint: "После революции" },
      { type: 'quiz', question: "Страны Антанты:", options: ["Россия, Франция, Англия", "Германия, Австрия", "Италия, Турция", "Германия, Италия", "США, Япония"], correctAnswer: "Россия, Франция, Англия", hint: "Антанта = союз" },
      { type: 'quiz', question: "Война закончилась в:", options: ["1917", "1918", "1916", "1920", "1914"], correctAnswer: "1918", hint: "11 ноября 1918" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Первая мировая война»! 🎉" }
  },
  {
    title: "Революция 1917",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Февральская революция:", options: ["Январь 1917", "Октябрь 1917", "Март 1917", "Ноябрь 1917", "Февраль 1917"], correctAnswer: "Февраль 1917", hint: "Свержение монархии" },
      { type: 'quiz', question: "Последний император:", options: ["Пётр I", "Екатерина II", "Александр II", "Николай II", "Александр III"], correctAnswer: "Николай II", hint: "Николай II отрёкся в 1917" },
      { type: 'quiz', question: "Октябрьскую революцию возглавил:", options: ["Ленин", "Николай II", "Керенский", "Троцкий", "Столыпин"], correctAnswer: "Ленин", hint: "Большевики и Ленин" },
      { type: 'quiz', question: "Что провозгласили большевики?", options: ["Монархию", "Империю", "Демократию", "Власть Советов", "Республику"], correctAnswer: "Власть Советов", hint: "Советская власть" },
      { type: 'quiz', question: "Гражданская война:", options: ["1917-1922", "1910-1915", "1925-1930", "1914-1918", "1920-1925"], correctAnswer: "1917-1922", hint: "После революции" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Революция 1917»! 🎉" }
  },
  {
    title: "Генетика",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Ген — это:", options: ["Клетка", "Орган", "Участок ДНК", "Ткань", "Белок"], correctAnswer: "Участок ДНК", hint: "Ген кодирует признак" },
      { type: 'quiz', question: "Гомозигота — это:", options: ["aB", "Ab", "Aa", "AA или aa", "AB"], correctAnswer: "AA или aa", hint: "Одинаковые аллели" },
      { type: 'quiz', question: "Первый закон Менделя:", options: ["Единообразие гибридов", "Сцепление", "Доминирование", "Расщепление", "Независимое наследование"], correctAnswer: "Единообразие гибридов", hint: "AA × aa → Aa" },
      { type: 'quiz', question: "Расщепление Aa × Aa по фенотипу:", options: ["1:2:1", "2:1", "9:3:3:1", "1:1", "3:1"], correctAnswer: "3:1", hint: "Второй закон Менделя" },
      { type: 'quiz', question: "Гетерозигота:", options: ["Aa", "bb", "AA", "BB", "aa"], correctAnswer: "Aa", hint: "Разные аллели" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Генетика»! 🎉" }
  },
  {
    title: "План и карта",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Что показывает масштаб?", options: ["Высоту", "Степень уменьшения", "Расстояние", "Площадь", "Направление"], correctAnswer: "Степень уменьшения", hint: "Во сколько раз уменьшено" },
      { type: 'quiz', question: "Стороны горизонта:", options: ["Верх, низ", "Тут, там", "Лево, право", "Север, юг, восток, запад", "Близко, далеко"], correctAnswer: "Север, юг, восток, запад", hint: "4 основных направления" },
      { type: 'quiz', question: "Масштаб 1:1000 означает:", options: ["1 см = 1 км", "1 см = 1000 см", "1 см = 100 м", "1 см = 1 м", "1 см = 10 м"], correctAnswer: "1 см = 1000 см", hint: "В 1000 раз больше" },
      { type: 'quiz', question: "Горизонталь на карте показывает:", options: ["Ветер", "Рельеф", "Температуру", "Давление", "Осадки"], correctAnswer: "Рельеф", hint: "Одинаковая высота" },
      { type: 'quiz', question: "Азимут измеряется в:", options: ["Километрах", "Минутах", "Градусах", "Секундах", "Метрах"], correctAnswer: "Градусах", hint: "От 0° до 360°" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «План и карта»! 🎉" }
  },
  {
    title: "Мировой океан",
    subject: "География",
    icon: "Map",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: "Сколько океанов на Земле?", options: ["4", "3", "5", "7", "6"], correctAnswer: "5", hint: "Тихий, Атлантический, Индийский, Сев. Ледовитый, Южный" },
      { type: 'quiz', question: "Самый большой океан:", options: ["Северный Ледовитый", "Индийский", "Южный", "Тихий", "Атлантический"], correctAnswer: "Тихий", hint: "Тихий — самый большой" },
      { type: 'quiz', question: "Самый тёплый океан:", options: ["Южный", "Индийский", "Северный Ледовитый", "Атлантический", "Тихий"], correctAnswer: "Индийский", hint: "Индийский — самый тёплый" },
      { type: 'quiz', question: "Солёность океанской воды:", options: ["50‰", "0‰", "10‰", "100‰", "35‰"], correctAnswer: "35‰", hint: "В среднем 35 промилле" },
      { type: 'quiz', question: "Море — это часть:", options: ["Реки", "Океана", "Пролива", "Залива", "Озера"], correctAnswer: "Океана", hint: "Море принадлежит океану" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Мировой океан»! 🎉" }
  },
  {
    title: "Present Perfect",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I have ___ this book.", options: ["read", "readen", "reading", "reads", "readed"], correctAnswer: "read", hint: "have + V3" },
      { type: 'quiz', question: "She has ___ London.", options: ["visited", "visits", "visit", "visitied", "visiting"], correctAnswer: "visited", hint: "has + V3 (+ed)" },
      { type: 'quiz', question: "Present Perfect для:", options: ["Прошлого времени", "Привычек", "Будущего", "Процесса", "Результата в настоящем"], correctAnswer: "Результата в настоящем", hint: "Результат важен сейчас" },
      { type: 'quiz', question: "Маркер Present Perfect:", options: ["In 2020", "Two days ago", "Yesterday", "Just", "Last week"], correctAnswer: "Just", hint: "Just, already, ever, never" },
      { type: 'quiz', question: "I have ___ known that.", options: ["yesterday", "ago", "last week", "in 2020", "already"], correctAnswer: "already", hint: "Already = уже" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Present Perfect»! 🎉" }
  },
  {
    title: "Modal Verbs",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ swim. (могу)", options: ["may", "can", "would", "should", "must"], correctAnswer: "can", hint: "Can = мочь" },
      { type: 'quiz', question: "You ___ do homework. (должен)", options: ["could", "can", "may", "should", "must"], correctAnswer: "must", hint: "Must = обязан" },
      { type: 'quiz', question: "You ___ see a doctor. (следует)", options: ["must", "will", "may", "should", "can"], correctAnswer: "should", hint: "Should = следует" },
      { type: 'quiz', question: "___ I come in? (Можно?)", options: ["May", "Can", "Will", "Should", "Must"], correctAnswer: "May", hint: "May = можно (разрешение)" },
      { type: 'quiz', question: "___ you help me? (Можешь?)", options: ["Could", "Should", "Will", "Must", "May"], correctAnswer: "Could", hint: "Could = вежливая просьба" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Modal Verbs»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Резины", "Стекла", "Древесины", "Пластика", "Металла"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Лепки", "Рисования", "Шитья", "Клея", "Резания"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Измерения", "Лепки", "Рисования", "Соединения деталей", "Резания"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Ножницы", "Молоток", "Карандаш", "Кисть", "Линейка"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Лепка", "Искусство складывания бумаги", "Шитьё", "Рисование", "Вязание"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Синее", "Красное", "Зелёное", "Жёлтое", "Фиолетовое"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Оранжевый", "Красный", "Фиолетовый", "Коричневый", "Зелёный"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Синяя", "Зелёная", "Красная", "Белая", "Жёлтая"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Синий", "Оранжевый", "Зелёный", "Фиолетовый", "Коричневый"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Жёлтый", "Оранжевый", "Коричневый", "Фиолетовый", "Зелёный"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Скрипка 🎻", "Гитара 🎸", "Пианино 🎹", "Флейта 🎶", "Барабан 🥁"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["5", "12", "6", "7", "8"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Гитара 🎸", "Барабан 🥁", "Скрипка 🎻", "Пианино 🎹", "Труба 🎺"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Флейта 🎶", "Гитара 🎸", "Труба 🎺", "Бубен", "Барабан 🥁"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Цирком", "Оркестром", "Хором", "Кинотеатром", "Театром"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Ракеткой", "Руками", "Без мяча", "Клюшкой", "Ногами и мячом ⚽"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["9", "6", "11", "5", "7"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Не спать", "Сидеть весь день", "Есть конфеты", "Мало двигаться", "Зарядка"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Без мяча", "Клюшкой", "Ракеткой", "Руками и мячом 🏀", "Ногами"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["1", "2", "0", "7", "3-4"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Безопасность",
    subject: "ОБЖ",
    icon: "Shield",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: "При пожаре нужно звонить:", options: ["101", "112", "102", "103", "104"], correctAnswer: "101", hint: "Пожарная служба" },
      { type: 'quiz', question: "Скорая помощь:", options: ["101", "102", "104", "112", "103"], correctAnswer: "103", hint: "Медицинская помощь" },
      { type: 'quiz', question: "Полиция:", options: ["102", "101", "104", "112", "103"], correctAnswer: "102", hint: "Полицейская служба" },
      { type: 'quiz', question: "Единый номер экстренной помощи:", options: ["101", "102", "104", "112", "103"], correctAnswer: "112", hint: "Единый номер" },
      { type: 'quiz', question: "При пожаре НЕЛЬЗЯ:", options: ["Дышать через влажную ткань", "Идти к выходу", "Эвакуироваться", "Звонить 101", "Прятаться"], correctAnswer: "Прятаться", hint: "Нельзя прятаться!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Безопасность»! 🎉" }
  },
]
