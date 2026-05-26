// Экспорт игр для 8 класса
import { GameLesson } from '../types'

export const eighthGradeGames: GameLesson[] = [
  {
    title: "Причастие",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Причастие — это:", options: ["Существительное", "Прилагательное", "Наречие", "Особая форма глагола", "Глагол"], correctAnswer: "Особая форма глагола", hint: "Причастие = признак по действию" },
      { type: 'quiz', question: "Причастие отвечает на вопрос:", options: ["Сколько?", "Кто?", "Что делать?", "Как?", "Какой?"], correctAnswer: "Какой?", hint: "Какой? — как прилагательное" },
      { type: 'quiz', question: "Признак причастия от глагола:", options: ["Склонение", "Падеж", "Время и вид", "Род", "Число"], correctAnswer: "Время и вид", hint: "Причастие имеет время и вид" },
      { type: 'quiz', question: "Действительное причастие:", options: ["Только настоящее время", "Только прошедшее время", "Не имеет действия", "Действие совершается над ним", "Совершает действие само"], correctAnswer: "Совершает действие само", hint: "Действительное — само совершает" },
      { type: 'quiz', question: "Страдательное причастие:", options: ["Совершает действие само", "Только прошедшее время", "Только настоящее время", "Не имеет действия", "Действие совершается над ним"], correctAnswer: "Действие совершается над ним", hint: "Страдательное — над ним совершают" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Причастие»! 🎉" }
  },
  {
    title: "Деепричастие",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Деепричастие обозначает:", options: ["Признак предмета", "Добавочное действие", "Место", "Основное действие", "Количество"], correctAnswer: "Добавочное действие", hint: "Деепричастие — добавочное действие" },
      { type: 'quiz', question: "Деепричастие отвечает на вопрос:", options: ["Какой?", "Что делая? Что сделав?", "Сколько?", "Кто?", "Что делать?"], correctAnswer: "Что делая? Что сделав?", hint: "Что делая? что сделав?" },
      { type: 'quiz', question: "Деепричастный оборот выделяется:", options: ["Не выделяется", "Запятыми", "Двоеточием", "Скобками", "Тире"], correctAnswer: "Запятыми", hint: "Деепричастный оборот обособляется" },
      { type: 'quiz', question: "Деепричастие — неизменяемая форма:", options: ["По падежу", "По числу", "По роду", "По всем признакам", "По лицу"], correctAnswer: "По всем признакам", hint: "Деепричастие не изменяется" },
      { type: 'quiz', question: "Какое слово — деепричастие?", options: ["Читая", "Читальный", "Читающий", "Прочитанный", "Читать"], correctAnswer: "Читая", hint: "Читая — что делая?" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Деепричастие»! 🎉" }
  },
  {
    title: "Синтаксис сложного предложения",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сложносочинённое предложение связывается:", options: ["Частицами", "Сочинительными союзами", "Предлогами", "Подчинительными союзами", "Интонацией"], correctAnswer: "Сочинительными союзами", hint: "И, а, но, или" },
      { type: 'quiz', question: "Сложноподчинённое предложение связывается:", options: ["Интонацией", "Сочинительными союзами", "Предлогами", "Частицами", "Подчинительными союзами"], correctAnswer: "Подчинительными союзами", hint: "Что, чтобы, если, когда" },
      { type: 'quiz', question: "Бессоюзное предложение связывается:", options: ["Предлогами", "Местоимениями", "Частицами", "Интонацией", "Союзами"], correctAnswer: "Интонацией", hint: "Без союзов — по смыслу" },
      { type: 'quiz', question: "Сколько грамматических основ в сложном предложении?", options: ["Две или больше", "Одна", "Четыре", "Три", "Пять"], correctAnswer: "Две или больше", hint: "Сложное = 2+ простых" },
      { type: 'quiz', question: "Какой союз — подчинительный?", options: ["И", "А", "Что", "Или", "Но"], correctAnswer: "Что", hint: "Что — подчинительный союз" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Синтаксис сложного предложения»! 🎉" }
  },
  {
    title: "Достоевский",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Достоевский родился в:", options: ["1815", "1830", "1819", "1821", "1825"], correctAnswer: "1821", hint: "Москва, 1821" },
      { type: 'quiz', question: "Родион Раскольников — герой:", options: ["Бесов", "Братьев Карамазовых", "Преступления и наказания", "Идиота", "Подростка"], correctAnswer: "Преступления и наказания", hint: "Главный герой романа" },
      { type: 'quiz', question: "Теория Раскольникова о:", options: ["Свободе", "Боге", "Любви", "Тварях дрожащих и Право имеющих", "Деньгах"], correctAnswer: "Тварях дрожащих и Право имеющих", hint: "Два типа людей" },
      { type: 'quiz', question: "«Братья Карамазовы» — автор:", options: ["Гоголь", "Чехов", "Тургенев", "Достоевский", "Толстой"], correctAnswer: "Достоевский", hint: "Ф.М. Достоевский" },
      { type: 'quiz', question: "Достоевский — великий:", options: ["Учёный", "Путешественник", "Историк", "Психолог", "Политик"], correctAnswer: "Психолог", hint: "Глубокий психологизм" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Достоевский»! 🎉" }
  },
  {
    title: "Уравнения",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "x + 5 = 12, x = ?", options: ["8", "17", "7", "5", "6"], correctAnswer: "7", hint: "x = 12 - 5" },
      { type: 'quiz', question: "3x = 18, x = ?", options: ["7", "4", "9", "6", "5"], correctAnswer: "6", hint: "x = 18 ÷ 3" },
      { type: 'quiz', question: "2x + 4 = 14, x = ?", options: ["7", "4", "5", "10", "6"], correctAnswer: "5", hint: "2x = 10, x = 5" },
      { type: 'quiz', question: "x - 8 = 15, x = ?", options: ["20", "23", "17", "13", "7"], correctAnswer: "23", hint: "x = 15 + 8" },
      { type: 'quiz', question: "x/3 = 9, x = ?", options: ["18", "12", "3", "6", "27"], correctAnswer: "27", hint: "x = 9 × 3" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Уравнения»! 🎉" }
  },
  {
    title: "Неравенства",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "При делении на отрицательное число знак:", options: ["Становится =", "Исчезает", "Не меняется", "Меняется", "Удваивается"], correctAnswer: "Меняется", hint: "Важно: минус меняет знак!" },
      { type: 'quiz', question: "Решить: 2x > 6", options: ["x > 3", "x < 3", "x > 4", "x < 4", "x = 3"], correctAnswer: "x > 3", hint: "x > 6/2" },
      { type: 'quiz', question: "Решить: -x > 5", options: ["x > -5", "x = -5", "x > 5", "x < 5", "x < -5"], correctAnswer: "x < -5", hint: "При делении на -1 знак меняется" },
      { type: 'quiz', question: "Решить: x + 2 > 7", options: ["x < 9", "x > 5", "x > 4", "x < 5", "x > 9"], correctAnswer: "x > 5", hint: "x > 7 - 2" },
      { type: 'quiz', question: "Решить: 3x < 12", options: ["x > 4", "x < 3", "x > 3", "x < 4", "x = 4"], correctAnswer: "x < 4", hint: "x < 12/3" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Неравенства»! 🎉" }
  },
  {
    title: "Степени и корни",
    subject: "Алгебра",
    icon: "Sigma",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2³ = ?", options: ["6", "9", "4", "12", "8"], correctAnswer: "8", hint: "2 × 2 × 2 = 8" },
      { type: 'quiz', question: "5⁰ = ?", options: ["25", "1", "0", "5", "10"], correctAnswer: "1", hint: "Любое число в степени 0 = 1" },
      { type: 'quiz', question: "√81 = ?", options: ["10", "6", "8", "9", "7"], correctAnswer: "9", hint: "9 × 9 = 81" },
      { type: 'quiz', question: "3² = ?", options: ["12", "3", "9", "8", "6"], correctAnswer: "9", hint: "3 × 3 = 9" },
      { type: 'quiz', question: "√100 = ?", options: ["11", "8", "10", "12", "9"], correctAnswer: "10", hint: "10 × 10 = 100" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Степени и корни»! 🎉" }
  },
  {
    title: "Треугольники",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Сумма углов треугольника:", options: ["90°", "270°", "360°", "120°", "180°"], correctAnswer: "180°", hint: "Сумма всегда 180°" },
      { type: 'quiz', question: "Прямоугольный треугольник имеет угол:", options: ["45°", "120°", "60°", "90°", "180°"], correctAnswer: "90°", hint: "Прямой угол = 90°" },
      { type: 'quiz', question: "Равносторонний треугольник имеет углы:", options: ["60°", "120°", "90°", "45°", "30°"], correctAnswer: "60°", hint: "Все углы равны: 180°/3" },
      { type: 'quiz', question: "Гипотенуза — это сторона:", options: ["Любая", "Прилежащая к углу", "Медиана", "Самая короткая", "Напротив прямого угла"], correctAnswer: "Напротив прямого угла", hint: "Гипотенуза — самая длинная" },
      { type: 'quiz', question: "Пифагорова теорема:", options: ["a² + b² = c²", "a² - b² = c²", "2a + 2b = c", "a × b = c", "a + b = c"], correctAnswer: "a² + b² = c²", hint: "Для прямоугольного треугольника" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Треугольники»! 🎉" }
  },
  {
    title: "Окружность",
    subject: "Геометрия",
    icon: "Shapes",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Вписанный угол равен:", options: ["Половине дуги", "Центральному углу", "Удвоенной дуге", "Дуге", "Острым углам"], correctAnswer: "Половине дуги", hint: "Вписанный = ½ центрального" },
      { type: 'quiz', question: "Длина окружности C = ?", options: ["πr", "πr²", "2πr", "2πd", "4πr"], correctAnswer: "2πr", hint: "C = 2πr" },
      { type: 'quiz', question: "Площадь круга S = ?", options: ["πr", "πd", "2πr²", "πr²", "2πr"], correctAnswer: "πr²", hint: "S = πr²" },
      { type: 'quiz', question: "Угол на диаметр:", options: ["0°", "Прямой (90°)", "Развёрнутый", "Тупой", "Острый"], correctAnswer: "Прямой (90°)", hint: "Всегда 90°" },
      { type: 'quiz', question: "Радиус — это:", options: ["Дуга", "Диаметр", "Секущая", "Половина диаметра", "Хорда"], correctAnswer: "Половина диаметра", hint: "r = d/2" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Окружность»! 🎉" }
  },
  {
    title: "Механика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Единица силы:", options: ["Джоуль (Дж)", "Килограмм (кг)", "Паскаль (Па)", "Ньютон (Н)", "Ватт (Вт)"], correctAnswer: "Ньютон (Н)", hint: "Н = кг·м/с²" },
      { type: 'quiz', question: "F = m × a — это:", options: ["Закон Гука", "Закон Ома", "Второй закон Ньютона", "Закон всемирного тяготения", "Закон Архимеда"], correctAnswer: "Второй закон Ньютона", hint: "Сила = масса × ускорение" },
      { type: 'quiz', question: "Ускорение свободного падения ≈", options: ["5 м/с²", "3.14 м/с²", "15 м/с²", "9.8 м/с²", "10.8 м/с²"], correctAnswer: "9.8 м/с²", hint: "g ≈ 9.8 м/с²" },
      { type: 'quiz', question: "Закон сохранения энергии:", options: ["E = const", "E растёт", "E уменьшается", "E = 0", "E = mc²"], correctAnswer: "E = const", hint: "Энергия не исчезает" },
      { type: 'quiz', question: "Работа измеряется в:", options: ["Ньютонах (Н)", "Вольтах (В)", "Ваттах (Вт)", "Джоулях (Дж)", "Паскалях (Па)"], correctAnswer: "Джоулях (Дж)", hint: "Дж = Н·м" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Механика»! 🎉" }
  },
  {
    title: "Оптика",
    subject: "Физика",
    icon: "Atom",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: "Угол падения равен:", options: ["Углу отражения", "Нулю", "Двойному углу", "Половине угла отражения", "180°"], correctAnswer: "Углу отражения", hint: "Закон отражения" },
      { type: 'quiz', question: "Линза, собирающая лучи:", options: ["Плоская", "Цилиндрическая", "Вогнутая (рассеивающая)", "Сферическая", "Выпуклая (собирающая)"], correctAnswer: "Выпуклая (собирающая)", hint: "Выпуклая — собирающая" },
      { type: 'quiz', question: "Оптическая сила D = ?", options: ["1/F", "2F", "F/2", "F²", "F"], correctAnswer: "1/F", hint: "Д = 1/f (диоптрии)" },
      { type: 'quiz', question: "Показатель преломления стекла ≈", options: ["1.5", "3", "1", "2", "0.5"], correctAnswer: "1.5", hint: "Стекло преломляет свет" },
      { type: 'quiz', question: "Радуга — это результат:", options: ["Рассеяния", "Поляризации", "Дисперсии света", "Отражения", "Поглощения"], correctAnswer: "Дисперсии света", hint: "Разложение белого света" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Оптика»! 🎉" }
  },
  {
    title: "Основы химии",
    subject: "Химия",
    icon: "FlaskConical",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: "Формула воды:", options: ["H₂SO₄", "NaCl", "O₂", "H₂O", "CO₂"], correctAnswer: "H₂O", hint: "Вода = водород + кислород" },
      { type: 'quiz', question: "pH нейтральной среды:", options: ["7", "1", "5", "14", "0"], correctAnswer: "7", hint: "pH 7 = нейтрально" },
      { type: 'quiz', question: "Кислота + основание =", options: ["Металл", "Кислота", "Основание", "Соль + вода", "Оксид"], correctAnswer: "Соль + вода", hint: "Реакция нейтрализации" },
      { type: 'quiz', question: "Формула серной кислоты:", options: ["H₂SO₄", "HNO₃", "CH₃COOH", "H₃PO₄", "HCl"], correctAnswer: "H₂SO₄", hint: "Серная кислота" },
      { type: 'quiz', question: "Типы химических реакций:", options: ["Только соединения", "Только обмена", "Только замещения", "Соединения, разложения, замещения", "Только разложения"], correctAnswer: "Соединения, разложения, замещения", hint: "4 основных типа" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Основы химии»! 🎉" }
  },
  {
    title: "Первая мировая война",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Когда началась Первая мировая?", options: ["1912", "1917", "1905", "1914", "1939"], correctAnswer: "1914", hint: "28 июля 1914 года" },
      { type: 'quiz', question: "Повод к войне:", options: ["Экономический кризис", "Теракт", "Революция", "Убийство эрцгерцога Франца Фердинанда", "Нападение на Польшу"], correctAnswer: "Убийство эрцгерцога Франца Фердинанда", hint: "Сараевское убийство" },
      { type: 'quiz', question: "Когда Россия вышла из войны?", options: ["1914", "1917", "1916", "1918", "1915"], correctAnswer: "1917", hint: "После революции" },
      { type: 'quiz', question: "Страны Антанты:", options: ["Германия, Австрия", "Италия, Турция", "Россия, Франция, Англия", "Германия, Италия", "США, Япония"], correctAnswer: "Россия, Франция, Англия", hint: "Антанта = союз" },
      { type: 'quiz', question: "Война закончилась в:", options: ["1914", "1918", "1916", "1920", "1917"], correctAnswer: "1918", hint: "11 ноября 1918" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Первая мировая война»! 🎉" }
  },
  {
    title: "Революция 1917",
    subject: "История",
    icon: "Landmark",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Февральская революция:", options: ["Октябрь 1917", "Март 1917", "Январь 1917", "Ноябрь 1917", "Февраль 1917"], correctAnswer: "Февраль 1917", hint: "Свержение монархии" },
      { type: 'quiz', question: "Последний император:", options: ["Александр III", "Александр II", "Пётр I", "Екатерина II", "Николай II"], correctAnswer: "Николай II", hint: "Николай II отрёкся в 1917" },
      { type: 'quiz', question: "Октябрьскую революцию возглавил:", options: ["Ленин", "Столыпин", "Николай II", "Троцкий", "Керенский"], correctAnswer: "Ленин", hint: "Большевики и Ленин" },
      { type: 'quiz', question: "Что провозгласили большевики?", options: ["Монархию", "Республику", "Империю", "Демократию", "Власть Советов"], correctAnswer: "Власть Советов", hint: "Советская власть" },
      { type: 'quiz', question: "Гражданская война:", options: ["1925-1930", "1910-1915", "1920-1925", "1914-1918", "1917-1922"], correctAnswer: "1917-1922", hint: "После революции" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Революция 1917»! 🎉" }
  },
  {
    title: "Генетика",
    subject: "Биология",
    icon: "Leaf",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Ген — это:", options: ["Белок", "Орган", "Ткань", "Участок ДНК", "Клетка"], correctAnswer: "Участок ДНК", hint: "Ген кодирует признак" },
      { type: 'quiz', question: "Гомозигота — это:", options: ["Aa", "AB", "aB", "Ab", "AA или aa"], correctAnswer: "AA или aa", hint: "Одинаковые аллели" },
      { type: 'quiz', question: "Первый закон Менделя:", options: ["Единообразие гибридов", "Расщепление", "Независимое наследование", "Сцепление", "Доминирование"], correctAnswer: "Единообразие гибридов", hint: "AA × aa → Aa" },
      { type: 'quiz', question: "Расщепление Aa × Aa по фенотипу:", options: ["2:1", "1:2:1", "1:1", "3:1", "9:3:3:1"], correctAnswer: "3:1", hint: "Второй закон Менделя" },
      { type: 'quiz', question: "Гетерозигота:", options: ["bb", "BB", "Aa", "aa", "AA"], correctAnswer: "Aa", hint: "Разные аллели" }
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
      { type: 'quiz', question: "Стороны горизонта:", options: ["Тут, там", "Близко, далеко", "Лево, право", "Верх, низ", "Север, юг, восток, запад"], correctAnswer: "Север, юг, восток, запад", hint: "4 основных направления" },
      { type: 'quiz', question: "Масштаб 1:1000 означает:", options: ["1 см = 1000 см", "1 см = 1 м", "1 см = 100 м", "1 см = 1 км", "1 см = 10 м"], correctAnswer: "1 см = 1000 см", hint: "В 1000 раз больше" },
      { type: 'quiz', question: "Горизонталь на карте показывает:", options: ["Осадки", "Давление", "Температуру", "Ветер", "Рельеф"], correctAnswer: "Рельеф", hint: "Одинаковая высота" },
      { type: 'quiz', question: "Азимут измеряется в:", options: ["Секундах", "Километрах", "Градусах", "Минутах", "Метрах"], correctAnswer: "Градусах", hint: "От 0° до 360°" }
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
      { type: 'quiz', question: "Самый большой океан:", options: ["Тихий", "Индийский", "Атлантический", "Южный", "Северный Ледовитый"], correctAnswer: "Тихий", hint: "Тихий — самый большой" },
      { type: 'quiz', question: "Самый тёплый океан:", options: ["Тихий", "Южный", "Индийский", "Атлантический", "Северный Ледовитый"], correctAnswer: "Индийский", hint: "Индийский — самый тёплый" },
      { type: 'quiz', question: "Солёность океанской воды:", options: ["0‰", "100‰", "35‰", "10‰", "50‰"], correctAnswer: "35‰", hint: "В среднем 35 промилле" },
      { type: 'quiz', question: "Море — это часть:", options: ["Залива", "Озера", "Реки", "Пролива", "Океана"], correctAnswer: "Океана", hint: "Море принадлежит океану" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Мировой океан»! 🎉" }
  },
  {
    title: "Present Perfect",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I have ___ this book.", options: ["reads", "reading", "read", "readed", "readen"], correctAnswer: "read", hint: "have + V3" },
      { type: 'quiz', question: "She has ___ London.", options: ["visits", "visited", "visiting", "visitied", "visit"], correctAnswer: "visited", hint: "has + V3 (+ed)" },
      { type: 'quiz', question: "Present Perfect для:", options: ["Будущего", "Результата в настоящем", "Процесса", "Привычек", "Прошлого времени"], correctAnswer: "Результата в настоящем", hint: "Результат важен сейчас" },
      { type: 'quiz', question: "Маркер Present Perfect:", options: ["Just", "Two days ago", "Last week", "In 2020", "Yesterday"], correctAnswer: "Just", hint: "Just, already, ever, never" },
      { type: 'quiz', question: "I have ___ known that.", options: ["ago", "yesterday", "in 2020", "already", "last week"], correctAnswer: "already", hint: "Already = уже" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Present Perfect»! 🎉" }
  },
  {
    title: "Modal Verbs",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "I ___ swim. (могу)", options: ["may", "can", "should", "must", "would"], correctAnswer: "can", hint: "Can = мочь" },
      { type: 'quiz', question: "You ___ do homework. (должен)", options: ["could", "can", "must", "may", "should"], correctAnswer: "must", hint: "Must = обязан" },
      { type: 'quiz', question: "You ___ see a doctor. (следует)", options: ["can", "must", "may", "will", "should"], correctAnswer: "should", hint: "Should = следует" },
      { type: 'quiz', question: "___ I come in? (Можно?)", options: ["Must", "Should", "May", "Can", "Will"], correctAnswer: "May", hint: "May = можно (разрешение)" },
      { type: 'quiz', question: "___ you help me? (Можешь?)", options: ["Must", "Will", "May", "Should", "Could"], correctAnswer: "Could", hint: "Could = вежливая просьба" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Modal Verbs»! 🎉" }
  },
  {
    title: "Технология",
    subject: "Технология",
    icon: "Ruler",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: "Бумага — материал из:", options: ["Резины", "Древесины", "Стекла", "Металла", "Пластика"], correctAnswer: "Древесины", hint: "Целлюлоза из дерева" },
      { type: 'quiz', question: "Ножницы — инструмент для:", options: ["Клея", "Шитья", "Лепки", "Резания", "Рисования"], correctAnswer: "Резания", hint: "Режут бумагу" },
      { type: 'quiz', question: "Клей нужен для:", options: ["Рисования", "Лепки", "Соединения деталей", "Резания", "Измерения"], correctAnswer: "Соединения деталей", hint: "Склеиваем части" },
      { type: 'quiz', question: "Какой инструмент измеряет длину?", options: ["Молоток", "Ножницы", "Карандаш", "Кисть", "Линейка"], correctAnswer: "Линейка", hint: "В сантиметрах" },
      { type: 'quiz', question: "Оригами — это:", options: ["Вязание", "Рисование", "Лепка", "Искусство складывания бумаги", "Шитьё"], correctAnswer: "Искусство складывания бумаги", hint: "Японское искусство" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Технология»! 🎉" }
  },
  {
    title: "Цвета",
    subject: "ИЗО",
    icon: "Palette",
    color: "text-rose-400",
    tasks: [
      { type: 'quiz', question: "Какого цвета солнце? ☀️", options: ["Фиолетовое", "Красное", "Жёлтое", "Синее", "Зелёное"], correctAnswer: "Жёлтое", hint: "Солнце яркое и тёплое" },
      { type: 'quiz', question: "Смешай жёлтый и синий:", options: ["Коричневый", "Оранжевый", "Зелёный", "Фиолетовый", "Красный"], correctAnswer: "Зелёный", hint: "Жёлтый + синий = зелёный" },
      { type: 'quiz', question: "Какого цвета трава? 🌿", options: ["Зелёная", "Синяя", "Жёлтая", "Белая", "Красная"], correctAnswer: "Зелёная", hint: "Трава зелёная" },
      { type: 'quiz', question: "Красный + жёлтый =", options: ["Синий", "Коричневый", "Оранжевый", "Зелёный", "Фиолетовый"], correctAnswer: "Оранжевый", hint: "Тёплый цвет" },
      { type: 'quiz', question: "Красный + синий =", options: ["Зелёный", "Фиолетовый", "Оранжевый", "Жёлтый", "Коричневый"], correctAnswer: "Фиолетовый", hint: "Холодный цвет" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Цвета»! 🎉" }
  },
  {
    title: "Музыкальные инструменты",
    subject: "Музыка",
    icon: "Music",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: "Какой инструмент бьют палочками?", options: ["Гитара 🎸", "Барабан 🥁", "Пианино 🎹", "Флейта 🎶", "Скрипка 🎻"], correctAnswer: "Барабан 🥁", hint: "Бум-бум-бум!" },
      { type: 'quiz', question: "Сколько нот в музыке?", options: ["6", "8", "5", "7", "12"], correctAnswer: "7", hint: "До, ре, ми, фа, соль, ля, си" },
      { type: 'quiz', question: "Чёрно-белый инструмент:", options: ["Гитара 🎸", "Барабан 🥁", "Скрипка 🎻", "Пианино 🎹", "Труба 🎺"], correctAnswer: "Пианино 🎹", hint: "Клавиши чёрные и белые" },
      { type: 'quiz', question: "У какого инструмента струны?", options: ["Труба 🎺", "Гитара 🎸", "Бубен", "Барабан 🥁", "Флейта 🎶"], correctAnswer: "Гитара 🎸", hint: "Дзинь-дзинь!" },
      { type: 'quiz', question: "Дирижёр руководит:", options: ["Цирком", "Хором", "Оркестром", "Кинотеатром", "Театром"], correctAnswer: "Оркестром", hint: "Дирижёр — руководитель" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Музыкальные инструменты»! 🎉" }
  },
  {
    title: "Спорт",
    subject: "Физкультура",
    icon: "Dumbbell",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: "Футбол играют:", options: ["Клюшкой", "Ногами и мячом ⚽", "Ракеткой", "Без мяча", "Руками"], correctAnswer: "Ногами и мячом ⚽", hint: "Футбол — ногами!" },
      { type: 'quiz', question: "Сколько игроков в команде по футболу?", options: ["5", "9", "11", "6", "7"], correctAnswer: "11", hint: "11 на поле" },
      { type: 'quiz', question: "Что полезно для здоровья?", options: ["Мало двигаться", "Есть конфеты", "Сидеть весь день", "Не спать", "Зарядка"], correctAnswer: "Зарядка", hint: "Движение — жизнь!" },
      { type: 'quiz', question: "Баскетбол играют:", options: ["Руками и мячом 🏀", "Ракеткой", "Без мяча", "Клюшкой", "Ногами"], correctAnswer: "Руками и мячом 🏀", hint: "Забрасываем в кольцо" },
      { type: 'quiz', question: "Сколько раз в неделю нужно заниматься спортом?", options: ["2", "1", "3-4", "0", "7"], correctAnswer: "3-4", hint: "Регулярность важна" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Спорт»! 🎉" }
  },
  {
    title: "Безопасность",
    subject: "ОБЖ",
    icon: "Shield",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: "При пожаре нужно звонить:", options: ["103", "104", "101", "102", "112"], correctAnswer: "101", hint: "Пожарная служба" },
      { type: 'quiz', question: "Скорая помощь:", options: ["102", "104", "101", "112", "103"], correctAnswer: "103", hint: "Медицинская помощь" },
      { type: 'quiz', question: "Полиция:", options: ["101", "104", "102", "112", "103"], correctAnswer: "102", hint: "Полицейская служба" },
      { type: 'quiz', question: "Единый номер экстренной помощи:", options: ["104", "112", "103", "101", "102"], correctAnswer: "112", hint: "Единый номер" },
      { type: 'quiz', question: "При пожаре НЕЛЬЗЯ:", options: ["Дышать через влажную ткань", "Эвакуироваться", "Звонить 101", "Идти к выходу", "Прятаться"], correctAnswer: "Прятаться", hint: "Нельзя прятаться!" }
    ],
    reward: { stars: 5, message: "Отлично! Ты знаешь тему «Безопасность»! 🎉" }
  },
]
