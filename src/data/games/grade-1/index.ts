// Экспорт игр для 1 класса
import { GameLesson } from '../types'

export const firstGradeGames: GameLesson[] = [
  // ========== РУССКИЙ ЯЗЫК ==========
  {
    title: "Алфавит: первые буквы",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какая буква первая в алфавите?", options: ["А", "Б", "В", "Г", "Д"], correctAnswer: "А", hint: "Алфавит начинается с А" },
      { type: 'quiz', question: "Какая буква следует за А?", options: ["В", "Б", "Г", "Д", "Е"], correctAnswer: "Б", hint: "А, Б, ..." },
      { type: 'find', question: "Выбери гласные буквы:", options: ["А", "Б", "О", "М", "У"], correctAnswer: ["А", "О", "У"], hint: "Гласные - их можно петь" },
      { type: 'quiz', question: "Сколько букв в русском алфавите?", options: ["30", "33", "35", "31", "32"], correctAnswer: "33", hint: "В русском алфавите 33 буквы" },
      { type: 'quiz', question: "Какая буква третья в алфавите?", options: ["А", "Б", "В", "Г", "Д"], correctAnswer: "В", hint: "А, Б, ..." },
      { type: 'quiz', question: "Какая буква последняя в алфавите?", options: ["Э", "Ю", "Я", "Щ", "Ш"], correctAnswer: "Я", hint: "Алфавит заканчивается буквой Я" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь алфавит! 🔤" }
  },
  {
    title: "Буква А",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какой звук обозначает буква А?", options: ["Гласный 🔴", "Согласный 🔵", "Звонкий 🔔", "Глухой 🔇", "Твёрдый ⬛"], correctAnswer: "Гласный 🔴", hint: "Этот звук поётся свободно!" },
      { type: 'find', question: "Выбери слова с буквой А:", options: ["МАМА 👩", "ПАПА 👨", "СЫН 👦", "ДОМ 🏠", "АНЯ 👧"], correctAnswer: ["МАМА 👩", "ПАПА 👨", "АНЯ 👧"], hint: "Ищи букву А в словах" },
      { type: 'quiz', question: "С какой буквы начинается слово АРБУЗ?", options: ["О", "А", "У", "Р", "Б"], correctAnswer: "А", hint: "Произнеси слово: [А]рбуз" },
      { type: 'quiz', question: "Сколько звуков [а] в слове БАНАН?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "БА-НАН - послушай внимательно!" },
      { type: 'find', question: "Выбери слова, которые начинаются на букву А:", options: ["Арбуз 🍉", "Банан 🍌", "Аист 🪶", "Кот 🐱", "Апельсин 🍊"], correctAnswer: ["Арбуз 🍉", "Аист 🪶", "Апельсин 🍊"], hint: "Ищи слова, где первая буква — А" },
      { type: 'quiz', question: "Какое слово заканчивается на букву А?", options: ["Мама", "Дом", "Кот", "Лес", "Сон"], correctAnswer: "Мама", hint: "Ма-ма — последний звук [а]" },
      { type: 'quiz', question: "Какая из этих букв гласная?", options: ["Б", "В", "А", "Д", "К"], correctAnswer: "А", hint: "Гласные можно петь!" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь букву А! 🌟" }
  },
  {
    title: "ЖИ-ШИ пиши с И",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: МАШ__НА?", options: ["МАШЫНА", "МАШИНА", "МАШЕНА", "МАШОНА", "МАШЮНА"], correctAnswer: "МАШИНА", hint: "ЖИ-ШИ пиши с И!" },
      { type: 'quiz', question: "Как правильно написать?", options: ["ШЫНА 🛞", "ШИНА 🛞", "ШЕНА 🛞", "ШОНА 🛞", "ШАНА 🛞"], correctAnswer: "ШИНА 🛞", hint: "ШИ всегда пишется с буквой И" },
      { type: 'find', question: "Выбери слова с ЖИ и ШИ:", options: ["ЖИРАФ 🦒", "ШИЛО", "МАМА 👩", "МАШИНА 🚗", "ЖИЗНЬ ✨"], correctAnswer: ["ЖИРАФ 🦒", "ШИЛО", "МАШИНА 🚗", "ЖИЗНЬ ✨"], hint: "Ищи сочетания ЖИ и ШИ" },
      { type: 'fill', question: "Вставь букву: ЛЫЖ__", correctAnswer: "И", hint: "ЖИ - пиши с И!" },
      { type: 'quiz', question: "Как правильно: Ш__ШКА?", options: ["ШЫШКА", "ШИШКА 🌲", "ШЕШКА", "ШАШКА", "ШЮШКА"], correctAnswer: "ШИШКА 🌲", hint: "ШИ пиши с И!" },
      { type: 'quiz', question: "Как правильно: Ж__ВОТ?", options: ["ЖЫВОТ", "ЖИВОТ", "ЖЕВОТ", "ЖОВОТ", "ЖЮВОТ"], correctAnswer: "ЖИВОТ", hint: "ЖИ пиши с И!" },
      { type: 'quiz', question: "В каком слове пишется И: МАШИНА или МАШЫНА?", options: ["МАШИНА", "МАШЫНА", "Оба верно", "Ни одно", "Машына"], correctAnswer: "МАШИНА", hint: "ЖИ-ШИ всегда с И" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь правило! 🏆" }
  },
  {
    title: "Ча-ща пиши с А",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: ТУЧ__?", options: ["ТУЧА ☁️", "ТУЧЯ ☁️", "ТУЧИ ☁️", "ТУЧУ ☁️", "ТУЧО ☁️"], correctAnswer: "ТУЧА ☁️", hint: "ЧА-ЩА пиши с А!" },
      { type: 'find', question: "Выбери слова с ЧА и ЩА:", options: ["ЧАЩА 🌲", "ЧАША 🏆", "МАМА 👩", "ЩУКА 🐟", "ДАЧА 🏡"], correctAnswer: ["ЧАЩА 🌲", "ЧАША 🏆", "ДАЧА 🏡"], hint: "Ищи ЧА и ЩА" },
      { type: 'quiz', question: "В слове РОЩА какая орфограмма?", options: ["ЖИ-ШИ", "ЧА-ЩА", "ЧУ-ЩУ", "ЖЕ-ШЕ", "ЧК-ЧН"], correctAnswer: "ЧА-ЩА", hint: "РОЩА - это ЩА" },
      { type: 'fill', question: "Вставь букву: ЗАДАЧ__", correctAnswer: "А", hint: "ЧА - пиши с А!" },
      { type: 'find', question: "Выбери слова с буквой ЩА:", options: ["ЩАВЕЛЬ 🥬", "ПЛАЩ", "ЩЕНОК 🐶", "ТЩАТЕЛЬНО", "ПОМОЩЬ 💪"], correctAnswer: ["ЩАВЕЛЬ 🥬", "ТЩАТЕЛЬНО"], hint: "Ищи сочетание ЩА" },
      { type: 'quiz', question: "Как правильно: ЧАЙ или ЧАЙ?", options: ["ЧАЙ ☕", "ЧЕЙ ☕", "ЧИЙ ☕", "ЧУЙ ☕", "ЧОЙ ☕"], correctAnswer: "ЧАЙ ☕", hint: "ЧА пиши с А!" },
      { type: 'quiz', question: "Как правильно: ЧУ__ЩИ?", options: ["ЧАЩИ", "ЧОЩИ", "ЧУЩИ 🌲", "ЧИЩИ", "ЧЕЩИ"], correctAnswer: "ЧУЩИ 🌲", hint: "В слове ЧУЩИ две орфограммы: ЧУ и ЩИ" },
      { type: 'quiz', question: "Как правильно: ПРОЩ__НИЕ?", options: ["ПРОЩАНИЕ", "ПРОЩУНИЕ", "ПРОЩИНИЕ", "ПРОЩОНИЕ", "ПРОЩЯНИЕ"], correctAnswer: "ПРОЩАНИЕ", hint: "ЩА пиши с А!" }
    ],
    reward: { stars: 3, message: "Замечательно! Ты знаешь правило ЧА-ЩА! 📝" }
  },
  {
    title: "Большая буква",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "С какой буквы начинаются имена?", options: ["С маленькой", "С большой", "С любой", "С гласной", "С согласной"], correctAnswer: "С большой", hint: "Имена пишутся с большой буквы!" },
      { type: 'find', question: "Выбери правильно написанные имена:", options: ["маша", "Маша", "ПЕТЯ", "Петя", "аня"], correctAnswer: ["Маша", "Петя"], hint: "Имена начинаются с большой буквы" },
      { type: 'quiz', question: "Как написать название города?", options: ["москва", "Москва", "МОСКВА", "мОсква", "МосквА"], correctAnswer: "Москва", hint: "Названия городов - с большой буквы" },
      { type: 'quiz', question: "Что пишется с большой буквы?", options: ["Стол", "Москва", "Бежит", "Река", "Кот"], correctAnswer: "Москва", hint: "Название города!" },
      { type: 'find', question: "Что пишется с большой буквы?", options: ["Москва 🏙️", "Река 🌊", "Маша 👧", "Стол 🪑", "Россия 🇷🇺"], correctAnswer: ["Москва 🏙️", "Маша 👧", "Россия 🇷🇺"], hint: "Имена собственные пишутся с большой буквы" },
      { type: 'quiz', question: "Как правильно написать имя кота: Мурка или мурка?", options: ["Мурка", "мурка", "МУРКА", "мурКа", "МуркА"], correctAnswer: "Мурка", hint: "Клички животных пишутся с большой буквы" },
      { type: 'quiz', question: "Что НЕ пишется с большой буквы?", options: ["Иван", "Москва", "река", "Россия", "Мурка"], correctAnswer: "река", hint: "Названия простых предметов пишутся с маленькой" }
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь про большую букву! 📖" }
  },

  // ========== МАТЕМАТИКА ==========
  {
    title: "Числа 1-5",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько звёзд? ⭐⭐⭐", options: ["2", "3", "4", "5", "1"], correctAnswer: "3", hint: "Посчитай: раз, два, три!" },
      { type: 'quiz', question: "Сколько яблок? 🍎🍎🍎🍎🍎", options: ["4", "5", "6", "3", "7"], correctAnswer: "5", hint: "Посчитай все яблоки!" },
      { type: 'order', question: "Расставь по порядку: 3, 1, 5, 2", options: ["3", "1", "5", "2", "4"], correctAnswer: "1, 2, 3, 5", hint: "От меньшего к большему" },
      { type: 'quiz', question: "Какое число больше: 2 или 4?", options: ["2", "4", "Одинаково", "1", "3"], correctAnswer: "4", hint: "4 идёт позже при счёте" },
      { type: 'quiz', question: "Какое число идёт перед 5?", options: ["3", "6", "4", "2", "7"], correctAnswer: "4", hint: "Считай обратно: 5, 4, 3..." },
      { type: 'quiz', question: "Какое число идёт после 3?", options: ["2", "4", "5", "1", "6"], correctAnswer: "4", hint: "Считай: 1, 2, 3, 4..." }
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь числа! 🔢" }
  },
  {
    title: "Сложение до 10",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "2 + 3 = ?", options: ["4", "5", "6", "3", "7"], correctAnswer: "5", hint: "Два плюс три..." },
      { type: 'quiz', question: "4 + 2 = ?", options: ["5", "6", "7", "4", "8"], correctAnswer: "6", hint: "Четыре и два вместе" },
      { type: 'fill', question: "3 + __ = 7", correctAnswer: "4", hint: "Сколько добавить до семи?" },
      { type: 'quiz', question: "5 + 5 = ?", options: ["9", "10", "11", "8", "12"], correctAnswer: "10", hint: "Это все пальцы на руках!" },
      { type: 'quiz', question: "1 + 6 = ?", options: ["5", "6", "7", "8", "4"], correctAnswer: "7", hint: "Один плюс шесть" },
      { type: 'quiz', question: "3 + 4 = ?", options: ["6", "7", "8", "5", "9"], correctAnswer: "7", hint: "Три плюс четыре" }
    ],
    reward: { stars: 3, message: "Супер! Ты умеешь складывать! ➕" }
  },
  {
    title: "Вычитание",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "5 - 2 = ?", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "Пять минус два..." },
      { type: 'quiz', question: "7 - 3 = ?", options: ["3", "4", "5", "2", "6"], correctAnswer: "4", hint: "Семь убери три" },
      { type: 'fill', question: "10 - __ = 6", correctAnswer: "4", hint: "Что отнять от 10, чтобы получить 6?" },
      { type: 'quiz', question: "8 - 0 = ?", options: ["0", "8", "7", "1", "9"], correctAnswer: "8", hint: "Если ничего не отнять..." },
      { type: 'quiz', question: "9 - 4 = ?", options: ["3", "4", "5", "6", "7"], correctAnswer: "5", hint: "Девять минус четыре" },
      { type: 'quiz', question: "6 - 3 = ?", options: ["2", "3", "4", "1", "5"], correctAnswer: "3", hint: "Шесть минус три" }
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь вычитать! ➖" }
  },
  {
    title: "Геометрические фигуры",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Сколько углов у треугольника?", options: ["2", "3", "4", "5", "6"], correctAnswer: "3", hint: "Треугольник = три угла" },
      { type: 'quiz', question: "Какая фигура круглой формы?", options: ["Квадрат ⬜", "Круг ⭕", "Треугольник 🔺", "Прямоугольник ▭", "Овал 🥚"], correctAnswer: "Круг ⭕", hint: "Круглая как мяч!" },
      { type: 'find', question: "Выбери фигуры с 4 углами:", options: ["Квадрат ⬜", "Треугольник 🔺", "Прямоугольник ▭", "Круг ⭕", "Ромб 🔷"], correctAnswer: ["Квадрат ⬜", "Прямоугольник ▭", "Ромб 🔷"], hint: "4 угла = четырёхугольник" },
      { type: 'quiz', question: "Что похоже на квадрат?", options: ["Мяч ⚽", "Окно 🪟", "Колесо 🛞", "Солнце ☀️", "Яйцо 🥚"], correctAnswer: "Окно 🪟", hint: "У окна 4 равные стороны" },
      { type: 'quiz', question: "Сколько сторон у треугольника?", options: ["2", "3", "4", "5", "6"], correctAnswer: "3", hint: "Три-угольник!" },
      { type: 'quiz', question: "Сколько углов у квадрата?", options: ["2", "3", "4", "5", "6"], correctAnswer: "4", hint: "Квадрат = четыре угла" }
    ],
    reward: { stars: 3, message: "Здорово! Ты знаешь фигуры! 🔷" }
  },

  // ========== ЛИТЕРАТУРНОЕ ЧТЕНИЕ ==========
  {
    title: "Сказки",
    subject: "Литература",
    icon: "BookOpenText",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: "Кто съел Колобка?", options: ["Волк 🐺", "Лиса 🦊", "Медведь 🐻", "Заяц 🐰", "Дедка 👴"], correctAnswer: "Лиса 🦊", hint: "Хитрая рыжая плутовка" },
      { type: 'quiz', question: "Из чего сделан Буратино?", options: ["Из железа", "Из дерева", "Из пластилина", "Из бумаги", "Из глины"], correctAnswer: "Из дерева", hint: "Папа Карло вырезал его" },
      { type: 'find', question: "Кто помогал Красной Шапочке?", options: ["Волк 🐺", "Охотники 🔫", "Бабушка 👵", "Дровосеки 🪓", "Мама 👩"], correctAnswer: ["Охотники 🔫", "Дровосеки 🪓"], hint: "Они спасли бабушку" },
      { type: 'quiz', question: "Кто тянул репку первым?", options: ["Бабка", "Дедка", "Внучка", "Жучка 🐕", "Кошка 🐱"], correctAnswer: "Дедка", hint: "Посадил дед репку..." },
      { type: 'quiz', question: "В какой сказке девочка пошла к бабушке через лес?", options: ["Репка", "Колобок", "Красная Шапочка 🧢", "Теремок", "Маша и медведь"], correctAnswer: "Красная Шапочка 🧢", hint: "Она несла пирожки в корзинке" },
      { type: 'quiz', question: "Кто жил в теремке?", options: ["Только волк", "Многие звери", "Только лиса", "Никто", "Только медведь"], correctAnswer: "Многие звери", hint: "Звери по очереди заселялись в теремок" }
    ],
    reward: { stars: 3, message: "Прекрасно! Ты знаешь сказки! 📚" }
  },

  // ========== ОКРУЖАЮЩИЙ МИР ==========
  {
    title: "Времена года",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое время года после зимы?", options: ["Лето ☀️", "Весна 🌸", "Осень 🍂", "Зима ❄️", "Ранняя весна 🌷"], correctAnswer: "Весна 🌸", hint: "Когда тает снег?" },
      { type: 'find', question: "Что бывает осенью?", options: ["Листопад 🍂", "Снег ❄️", "Дожди 🌧️", "Цветы 🌷", "Грибы 🍄"], correctAnswer: ["Листопад 🍂", "Дожди 🌧️", "Грибы 🍄"], hint: "Осенью прохладно" },
      { type: 'quiz', question: "Когда можно купаться в речке?", options: ["Зимой ❄️", "Летом ☀️", "Осенью 🍂", "Весной 🌸", "Каждый день"], correctAnswer: "Летом ☀️", hint: "Когда тепло и солнечно" },
      { type: 'quiz', question: "Сколько времён года?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "Зима, весна, лето, осень" },
      { type: 'quiz', question: "Какое время года самое холодное?", options: ["Лето ☀️", "Весна 🌸", "Осень 🍂", "Зима ❄️", "Ранняя осень"], correctAnswer: "Зима ❄️", hint: "Когда выпадает снег?" },
      { type: 'quiz', question: "Какое время года идёт перед зимой?", options: ["Весна 🌸", "Лето ☀️", "Осень 🍂", "Зима ❄️", "Ранняя весна"], correctAnswer: "Осень 🍂", hint: "После осени наступает зима" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь времена года! 🌸" }
  },
  {
    title: "Животные",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какое животное говорит «Му»?", options: ["Кошка 🐱", "Корова 🐄", "Собака 🐕", "Лошадь 🐴", "Свинья 🐷"], correctAnswer: "Корова 🐄", hint: "Большое животное на ферме" },
      { type: 'find', question: "Выбери домашних животных:", options: ["Кошка 🐱", "Лиса 🦊", "Собака 🐕", "Волк 🐺", "Корова 🐄"], correctAnswer: ["Кошка 🐱", "Собака 🐕", "Корова 🐄"], hint: "Они живут с людьми" },
      { type: 'quiz', question: "Кто умеет летать?", options: ["Рыба 🐟", "Птица 🐦", "Змея 🐍", "Лягушка 🐸", "Черепаха 🐢"], correctAnswer: "Птица 🐦", hint: "У кого есть крылья?" },
      { type: 'quiz', question: "Где живёт белка?", options: ["В норе 🕳️", "В дупле 🌳", "В воде 🌊", "В берлоге 🐻", "В гнезде 🪺"], correctAnswer: "В дупле 🌳", hint: "Белка живёт на дереве" },
      { type: 'find', question: "Выбери диких животных:", options: ["Кошка 🐱", "Лиса 🦊", "Волк 🐺", "Корова 🐄", "Заяц 🐰"], correctAnswer: ["Лиса 🦊", "Волк 🐺", "Заяц 🐰"], hint: "Дикие животные живут в лесу" },
      { type: 'quiz', question: "Какое животное самое большое?", options: ["Кошка 🐱", "Слон 🐘", "Мышка 🐭", "Заяц 🐰", "Лиса 🦊"], correctAnswer: "Слон 🐘", hint: "Слон — самое большое сухопутное животное" },
      { type: 'quiz', question: "Какое животное живёт в воде?", options: ["Птица 🐦", "Рыба 🐟", "Заяц 🐰", "Белка 🐿️", "Кошка 🐱"], correctAnswer: "Рыба 🐟", hint: "Рыбы плавают в воде" }
    ],
    reward: { stars: 3, message: "Молодец! Ты знаешь животных! 🐾" }
  },

  // ========== АНГЛИЙСКИЙ ==========
  {
    title: "Hello! Привет!",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Как сказать «Привет» по-английски?", options: ["Goodbye 👋", "Hello 👋", "Thanks 🙏", "Sorry 🙏", "Please 🙏"], correctAnswer: "Hello 👋", hint: "Самое популярное приветствие" },
      { type: 'quiz', question: "Что значит Hi?", options: ["Пока", "Привет", "Спасибо", "Извините", "Пожалуйста"], correctAnswer: "Привет", hint: "Hi = Привет" },
      { type: 'find', question: "Выбери приветствия:", options: ["Hello", "Hi", "Goodbye", "Bye", "Thanks"], correctAnswer: ["Hello", "Hi"], hint: "Приветствия по-английски" },
      { type: 'quiz', question: "Как сказать «Пока»?", options: ["Hello", "Bye", "Hi", "Morning", "Night"], correctAnswer: "Bye", hint: "Bye = Пока" },
      { type: 'quiz', question: "Что значит Good morning?", options: ["Спокойной ночи", "Доброе утро ☀️", "До свидания", "Спасибо", "Привет"], correctAnswer: "Доброе утро ☀️", hint: "Morning = утро" },
      { type: 'quiz', question: "Что значит Good night?", options: ["Доброе утро", "Спокойной ночи 🌙", "До свидания", "Спасибо", "Привет"], correctAnswer: "Спокойной ночи 🌙", hint: "Night = ночь" }
    ],
    reward: { stars: 3, message: "Great! Отлично! 👋" }
  },
  {
    title: "Цвета по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Red - это...", options: ["Синий", "Красный", "Зелёный", "Жёлтый", "Белый"], correctAnswer: "Красный", hint: "Red = красный цвет" },
      { type: 'quiz', question: "Как будет «жёлтый»?", options: ["Yellow", "Green", "Blue", "Red", "Pink"], correctAnswer: "Yellow", hint: "Yellow = цвет солнца" },
      { type: 'find', question: "Выбери цвета радуги:", options: ["Red", "Cat", "Blue", "Dog", "Green"], correctAnswer: ["Red", "Blue", "Green"], hint: "Цвета = Colors" },
      { type: 'quiz', question: "Какого цвета трава?", options: ["Red", "Blue", "Green", "Yellow", "Pink"], correctAnswer: "Green", hint: "Green = зелёный" },
      { type: 'quiz', question: "Как будет «чёрный»?", options: ["White", "Brown", "Black", "Orange", "Purple"], correctAnswer: "Black", hint: "Black = чёрный цвет" },
      { type: 'quiz', question: "Blue - это...", options: ["Красный", "Синий", "Зелёный", "Жёлтый", "Белый"], correctAnswer: "Синий", hint: "Blue = синий цвет" }
    ],
    reward: { stars: 3, message: "Wonderful! Замечательно! 🎨" }
  },
  
  // ========== НОВЫЕ ИГРЫ ==========
  {
    title: "Счёт до 20",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Какое число идёт после 15?", options: ["14", "16", "17", "18", "19"], correctAnswer: "16", hint: "Посчитай: 14, 15, ..." },
      { type: 'fill', question: "Какое число между 12 и 14?", correctAnswer: "13", hint: "12, ?, 14" },
      { type: 'quiz', question: "Сколько десятков в числе 17?", options: ["1", "7", "17", "10", "3"], correctAnswer: "1", hint: "17 = 1 десяток и 7 единиц" },
      { type: 'quiz', question: "Какое число больше: 19 или 15?", options: ["19", "15", "Одинаково", "20", "18"], correctAnswer: "19", hint: "19 идёт позже при счёте" },
      { type: 'quiz', question: "Какое число идёт перед 20?", options: ["18", "21", "19", "17", "15"], correctAnswer: "19", hint: "Считай обратно: 20, 19, 18..." },
      { type: 'quiz', question: "Какое число идёт после 10?", options: ["9", "11", "12", "20", "13"], correctAnswer: "11", hint: "После десяти идёт одиннадцать" }
    ],
    reward: { stars: 3, message: "Умница! Ты считаешь до 20! 🔢" }
  },
  {
    title: "Состав числа",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: "5 - это 2 + __", correctAnswer: "3", hint: "2 + 3 = 5" },
      { type: 'quiz', question: "7 - это 4 и сколько?", options: ["2", "3", "4", "5", "1"], correctAnswer: "3", hint: "4 + 3 = 7" },
      { type: 'quiz', question: "Из каких чисел состоит 6?", options: ["3 и 3", "2 и 2", "5 и 2", "1 и 4", "6 и 0"], correctAnswer: "3 и 3", hint: "3 + 3 = 6" },
      { type: 'quiz', question: "10 - это 6 и сколько?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "6 + 4 = 10" },
      { type: 'quiz', question: "8 - это 5 и сколько?", options: ["2", "3", "4", "5", "1"], correctAnswer: "3", hint: "5 + 3 = 8" },
      { type: 'quiz', question: "9 - это 5 и сколько?", options: ["3", "4", "5", "6", "2"], correctAnswer: "4", hint: "5 + 4 = 9" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь состав чисел! 🧮" }
  },
  {
    title: "Чу-щу пиши с У",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Как правильно: Щ__КА?", options: ["ЩУКА 🐟", "ЩАКА", "ЩИКА", "ЩОКА", "ЩЕКА"], correctAnswer: "ЩУКА 🐟", hint: "ЧУ-ЩУ пиши с У!" },
      { type: 'find', question: "Выбери слова с ЧУ и ЩУ:", options: ["ЧУДО ✨", "ЩУКА 🐟", "МАМА 👩", "ЧУГУН", "РОЩА 🌳"], correctAnswer: ["ЧУДО ✨", "ЩУКА 🐟", "ЧУГУН"], hint: "ЧУ-ЩУ с буквой У" },
      { type: 'fill', question: "Вставь букву: Ч__ДО", correctAnswer: "У", hint: "ЧУ - пиши с У!" },
      { type: 'quiz', question: "В слове ЧУМАКА какая орфограмма?", options: ["ЖИ-ШИ", "ЧУ-ЩУ", "ЧА-ЩА", "ЖЕ-ШЕ", "ЧК-ЧН"], correctAnswer: "ЧУ-ЩУ", hint: "ЧУ - пишется с У" },
      { type: 'quiz', question: "Как правильно: Ч__ЖИК?", options: ["ЧОЖИК", "ЧАЖИК", "ЧУЖИК 🐦", "ЧИЖИК", "ЧЕЖИК"], correctAnswer: "ЧУЖИК 🐦", hint: "ЧУ - пиши с буквой У!" },
      { type: 'quiz', question: "Как правильно: Ч__ДЕСА?", options: ["ЧУДЕСА ✨", "ЧАДЕСА", "ЧИДЕСА", "ЧЕДЕСА", "ЧОДЕСА"], correctAnswer: "ЧУДЕСА ✨", hint: "ЧУ пиши с У!" },
      { type: 'quiz', question: "Как правильно: Щ__ПАЛЬЦЕ?", options: ["ЩИПАЛЬЦЕ", "ЩАПАЛЬЦЕ", "ЩУПАЛЬЦЕ 🐙", "ЩОПАЛЬЦЕ", "ЩЕПАЛЬЦЕ"], correctAnswer: "ЩУПАЛЬЦЕ 🐙", hint: "ЩУ пиши с У!" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь правило ЧУ-ЩУ! ✍️" }
  },
  {
    title: "Слова-действия",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Что делает птица? 🐦", options: ["Летит", "Плавает", "Бегает", "Ползает", "Роет"], correctAnswer: "Летит", hint: "Птицы летают!" },
      { type: 'find', question: "Выбери слова-действия:", options: ["Бежит 🏃", "Красивый", "Пишет ✍️", "Стол", "Читает 📖"], correctAnswer: ["Бежит 🏃", "Пишет ✍️", "Читает 📖"], hint: "Слова-действия отвечают на «что делает?»" },
      { type: 'quiz', question: "На какой вопрос отвечает слово «рисует»?", options: ["Что?", "Что делает?", "Какой?", "Где?", "Когда?"], correctAnswer: "Что делает?", hint: "Рисует - это действие" },
      { type: 'quiz', question: "Что делает рыба? 🐟", options: ["Летит", "Плавает", "Бегает", "Прыгает", "Поёт"], correctAnswer: "Плавает", hint: "Рыбы плавают в воде" },
      { type: 'find', question: "Выбери слова, которые НЕ являются действиями:", options: ["Прыгает 🦘", "Красный", "Быстрый", "Поёт 🎤", "Добрый"], correctAnswer: ["Красный", "Быстрый", "Добрый"], hint: "Ищи слова-признаки, а не действия" },
      { type: 'quiz', question: "Что делает собака? 🐕", options: ["Летит", "Плавает", "Гавкает", "Поёт", "Ползает"], correctAnswer: "Гавкает", hint: "Собаки гавкают!" },
      { type: 'quiz', question: "Какое слово является действием?", options: ["Красный", "Быстрый", "Высокий", "Прыгает 🦘", "Добрый"], correctAnswer: "Прыгает 🦘", hint: "Прыгает - отвечает на вопрос «что делает?»" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слова-действия! 📝" }
  },
  {
    title: "Дни недели и месяцы",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Какой день идёт после среды?", options: ["Вторник", "Четверг", "Пятница", "Понедельник", "Суббота"], correctAnswer: "Четверг", hint: "Понедельник, вторник, среда, ..." },
      { type: 'find', question: "Выбери зимние месяцы:", options: ["Декабрь", "Июнь", "Январь", "Июль", "Февраль"], correctAnswer: ["Декабрь", "Январь", "Февраль"], hint: "Зимние месяцы - холодные" },
      { type: 'quiz', question: "Сколько месяцев в году?", options: ["10", "11", "12", "13", "9"], correctAnswer: "12", hint: "В году 12 месяцев" },
      { type: 'quiz', question: "В каком месяце начинается учебный год?", options: ["Август", "Сентябрь", "Октябрь", "Ноябрь", "Июль"], correctAnswer: "Сентябрь", hint: "1 сентября - День знаний" },
      { type: 'quiz', question: "Какой день недели первый?", options: ["Вторник", "Среда", "Понедельник", "Четверг", "Воскресенье"], correctAnswer: "Понедельник", hint: "Неделя начинается с понедельника" },
      { type: 'quiz', question: "Сколько дней в неделе?", options: ["5", "6", "7", "8", "4"], correctAnswer: "7", hint: "Понедельник, вторник, ..., воскресенье" }
    ],
    reward: { stars: 3, message: "Умница! Ты знаешь календарь! 📅" }
  },
  {
    title: "Животные и их детёныши",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Кто детёныш у кошки?", options: ["Щенок", "Котёнок", "Медвежонок", "Телятёнок", "Жеребёнок"], correctAnswer: "Котёнок", hint: "Кошка - котёнок" },
      { type: 'find', question: "Выбери правильные пары:", options: ["Собака - щенок", "Корова - телёнок", "Кошка - щенок", "Лошадь - жеребёнок", "Утка - утёнок"], correctAnswer: ["Собака - щенок", "Корова - телёнок", "Лошадь - жеребёнок", "Утка - утёнок"], hint: "У каждого животного свой детёныш" },
      { type: 'quiz', question: "Кто детёныш у курицы?", options: ["Утёнок", "Цыплёнок", "Гусёнок", "Котёнок", "Щенок"], correctAnswer: "Цыплёнок", hint: "Курица - цыплёнок" },
      { type: 'quiz', question: "Кто детёныш у медведя?", options: ["Медвежонок", "Зайчонок", "Лисёнок", "Волчонок", "Бельчонок"], correctAnswer: "Медвежонок", hint: "Медведь - медвежонок" },
      { type: 'quiz', question: "Кто детёныш у свиньи?", options: ["Щенок", "Жеребёнок", "Поросёнок 🐷", "Котёнок", "Телятёнок"], correctAnswer: "Поросёнок 🐷", hint: "Свинья - поросёнок" },
      { type: 'quiz', question: "Кто детёныш у лошади?", options: ["Щенок", "Котёнок", "Жеребёнок 🐴", "Утёнок", "Цыплёнок"], correctAnswer: "Жеребёнок 🐴", hint: "Лошадь - жеребёнок" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь детёнышей! 🐾" }
  },
  {
    title: "Числа на английском",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "One - это...", options: ["Один", "Два", "Три", "Четыре", "Пять"], correctAnswer: "Один", hint: "One = 1" },
      { type: 'quiz', question: "Как будет «три»?", options: ["Two", "Three", "Four", "Five", "Six"], correctAnswer: "Three", hint: "Three = 3" },
      { type: 'fill', question: "Two + Two = __ (Four)", correctAnswer: "Four", hint: "2 + 2 = 4" },
      { type: 'find', question: "Выбери числа от 1 до 3:", options: ["One", "Four", "Two", "Five", "Three"], correctAnswer: ["One", "Two", "Three"], hint: "1, 2, 3" },
      { type: 'quiz', question: "Five - это...", options: ["3", "4", "5", "6", "2"], correctAnswer: "5", hint: "Five = пять" },
      { type: 'quiz', question: "Two - это...", options: ["Один", "Два", "Три", "Четыре", "Пять"], correctAnswer: "Два", hint: "Two = 2" },
      { type: 'quiz', question: "Как будет «четыре»?", options: ["Two", "Three", "Four", "Five", "Six"], correctAnswer: "Four", hint: "Four = 4" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь числа! 🔢" }
  },

  // ========== НОВЫЕ ИГРЫ v3.41 ==========
  {
    title: "Сравнение чисел",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Что больше: 7 или 5?", options: ["7", "5", "Одинаково", "6", "8"], correctAnswer: "7", hint: "7 идёт позже при счёте" },
      { type: 'quiz', question: "Что меньше: 3 или 6?", options: ["3", "6", "Одинаково", "4", "5"], correctAnswer: "3", hint: "3 идёт раньше при счёте" },
      { type: 'fill', question: "Поставь знак: 4 __ 4 (равно)", correctAnswer: "=", hint: "Числа одинаковые" },
      { type: 'quiz', question: "Сколько яблок больше? 🍎🍎🍎 vs 🍎🍎", options: ["Первых больше на 1", "Вторых больше", "Одинаково", "Первых больше на 2", "Первых больше на 3"], correctAnswer: "Первых больше на 1", hint: "3 > 2" },
      { type: 'quiz', question: "Что больше: 10 или 8?", options: ["10", "8", "Одинаково", "9", "7"], correctAnswer: "10", hint: "10 - это два десятка" },
      { type: 'quiz', question: "Что меньше: 8 или 9?", options: ["8", "9", "Одинаково", "7", "10"], correctAnswer: "8", hint: "8 идёт раньше при счёте" }
    ],
    reward: { stars: 3, message: "Отлично! Ты умеешь сравнивать! ⚖️" }
  },
  {
    title: "Задачи в картинках",
    subject: "Математика",
    icon: "Calculator",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: "Было 3 яблока 🍎🍎🍎, съели 1. Сколько осталось?", options: ["1", "2", "4", "3", "5"], correctAnswer: "2", hint: "3 - 1 = 2" },
      { type: 'quiz', question: "Было 2 птички 🐦🐦, прилетели ещё 2. Сколько стало?", options: ["2", "4", "3", "5", "1"], correctAnswer: "4", hint: "2 + 2 = 4" },
      { type: 'fill', question: "5 конфет 🍬🍬🍬🍬🍬, 2 съели. Осталось __", correctAnswer: "3", hint: "5 - 2 = 3" },
      { type: 'quiz', question: "У Маши 2 куклы 🎎🎎, у Даши 3. Сколько всего?", options: ["4", "5", "6", "3", "7"], correctAnswer: "5", hint: "2 + 3 = 5" },
      { type: 'quiz', question: "На ветке сидели 4 птицы 🐦🐦🐦🐦, 1 улетела. Сколько осталось?", options: ["1", "2", "3", "4", "5"], correctAnswer: "3", hint: "4 - 1 = 3" },
      { type: 'quiz', question: "Было 4 конфеты 🍬, добавили ещё 3. Сколько стало?", options: ["5", "6", "7", "8", "4"], correctAnswer: "7", hint: "4 + 3 = 7" }
    ],
    reward: { stars: 3, message: "Умница! Ты решаешь задачи! 📊" }
  },
  {
    title: "Слоги",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Сколько слогов в слове МА-МА?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "Хлопни два раза: МА-МА" },
      { type: 'quiz', question: "Сколько слогов в слове ШАР?", options: ["1", "2", "3", "4", "5"], correctAnswer: "1", hint: "Хлопни один раз" },
      { type: 'find', question: "Выбери слова из 2 слогов:", options: ["Дом 🏠", "Вода 💧", "Кот 🐱", "Рука ✋", "Сад 🌳"], correctAnswer: ["Вода 💧", "Рука ✋"], hint: "Посчитай хлопки" },
      { type: 'quiz', question: "Какое слово самое длинное?", options: ["Кот", "Машина", "Дом", "Сон", "Нос"], correctAnswer: "Машина", hint: "Посчитай слоги" },
      { type: 'fill', question: "Сколько слогов в слове КА-РАН-ДАШ? __", correctAnswer: "3", hint: "Хлопни три раза: КА-РАН-ДАШ" },
      { type: 'quiz', question: "Сколько слогов в слове СО-БА-КА?", options: ["1", "2", "3", "4", "5"], correctAnswer: "3", hint: "Хлопни три раза: СО-БА-КА" },
      { type: 'quiz', question: "Сколько слогов в слове ЛУНА?", options: ["1", "2", "3", "4", "5"], correctAnswer: "2", hint: "ЛУ-НА — два слога" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь слоги! 📝" }
  },
  {
    title: "Слова-признаки",
    subject: "Русский язык",
    icon: "BookOpen",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: "Какой мяч? ⚽", options: ["Круглый", "Бежит", "Мяч", "Катится", "Прыгает"], correctAnswer: "Круглый", hint: "Признак предмета" },
      { type: 'find', question: "Выбери слова-признаки:", options: ["Большой", "Стол", "Красный", "Дом", "Быстрый"], correctAnswer: ["Большой", "Красный", "Быстрый"], hint: "Слова-признаки описывают предметы" },
      { type: 'quiz', question: "На какой вопрос отвечает слово «красивый»?", options: ["Что?", "Какой?", "Что делает?", "Где?", "Когда?"], correctAnswer: "Какой?", hint: "Какой? - это признак" },
      { type: 'quiz', question: "Какое небо? ☁️", options: ["Синее", "Бежит", "Небо", "Шумит", "Темное"], correctAnswer: "Синее", hint: "Признак неба" },
      { type: 'find', question: "Выбери слова-признаки для яблока 🍎:", options: ["Красное", "Круглое", "Катится", "Сладкое", "Растёт"], correctAnswer: ["Красное", "Круглое", "Сладкое"], hint: "Признаки описывают, какое яблоко" },
      { type: 'quiz', question: "Какой снег? ❄️", options: ["Белый", "Шумит", "Снег", "Тает", "Холодный"], correctAnswer: "Белый", hint: "Снег белый — это признак" },
      { type: 'quiz', question: "Какое слово является признаком?", options: ["Бежит", "Прыгает", "Весёлый 😊", "Читает", "Поёт"], correctAnswer: "Весёлый 😊", hint: "Весёлый отвечает на вопрос «какой?»" }
    ],
    reward: { stars: 3, message: "Супер! Ты знаешь слова-признаки! ✍️" }
  },
  {
    title: "Семья",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: "Мама и папа - это...", options: ["Дети", "Родители", "Бабушка", "Дедушка", "Внуки"], correctAnswer: "Родители", hint: "Родители - это мама и папа" },
      { type: 'find', question: "Выбери членов семьи:", options: ["Мама 👩", "Учитель", "Папа 👨", "Друг", "Бабушка 👵"], correctAnswer: ["Мама 👩", "Папа 👨", "Бабушка 👵"], hint: "Семья - самые близкие люди" },
      { type: 'quiz', question: "Брат мамы - это...", options: ["Дядя", "Дедушка", "Папа", "Двоюродный брат", "Сын"], correctAnswer: "Дядя", hint: "Брат мамы или папы" },
      { type: 'quiz', question: "Дочь мамы - это...", options: ["Тётя", "Сестра", "Бабушка", "Племянница", "Кузина"], correctAnswer: "Сестра", hint: "Дочь моих родителей" },
      { type: 'quiz', question: "Мамин папа - это...", options: ["Брат", "Дядя", "Дедушка 👴", "Папа", "Сын"], correctAnswer: "Дедушка 👴", hint: "Папа мамы = твой дедушка" },
      { type: 'quiz', question: "Сестра мамы - это...", options: ["Мама", "Тётя", "Бабушка", "Сестра", "Двоюродная мама"], correctAnswer: "Тётя", hint: "Сестра мамы или папы = тётя" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь семью! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Транспорт",
    subject: "Окружающий мир",
    icon: "Globe",
    color: "text-indigo-400",
    tasks: [
      { type: 'quiz', question: "Что летает в небе?", options: ["Машина 🚗", "Самолёт ✈️", "Корабль 🚢", "Поезд 🚂", "Велосипед 🚲"], correctAnswer: "Самолёт ✈️", hint: "У самолёта есть крылья" },
      { type: 'find', question: "Выбери транспорт:", options: ["Машина 🚗", "Стол 🪑", "Автобус 🚌", "Дерево 🌳", "Велосипед 🚲"], correctAnswer: ["Машина 🚗", "Автобус 🚌", "Велосипед 🚲"], hint: "Транспорт - это то, на чём ездят" },
      { type: 'quiz', question: "Корабль плавает...", options: ["В небе", "На дороге", "По воде 🌊", "По рельсам", "В космосе"], correctAnswer: "По воде 🌊", hint: "Корабли плавают по морям и рекам" },
      { type: 'quiz', question: "Сколько колёс у велосипеда?", options: ["2", "3", "4", "1", "6"], correctAnswer: "2", hint: "Велосипед = два колеса" },
      { type: 'quiz', question: "Что едет по рельсам?", options: ["Самолёт ✈️", "Корабль 🚢", "Поезд 🚂", "Вертолёт 🚁", "Мяч ⚽"], correctAnswer: "Поезд 🚂", hint: "У поезда есть колёса и рельсы" },
      { type: 'quiz', question: "Что ездит по дороге?", options: ["Самолёт ✈️", "Корабль 🚢", "Машина 🚗", "Птица 🐦", "Рыба 🐟"], correctAnswer: "Машина 🚗", hint: "Машины едут по дорогам" }
    ],
    reward: { stars: 3, message: "Отлично! Ты знаешь транспорт! 🚗" }
  },
  {
    title: "Семья по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Mother - это...", options: ["Папа", "Мама", "Сестра", "Бабушка", "Тётя"], correctAnswer: "Мама", hint: "Mother = мама" },
      { type: 'quiz', question: "Как будет «папа»?", options: ["Mother", "Father", "Sister", "Brother", "Uncle"], correctAnswer: "Father", hint: "Father = папа" },
      { type: 'find', question: "Выбери слова о семье:", options: ["Mother 👩", "Cat 🐱", "Father 👨", "Dog 🐕", "Sister 👧"], correctAnswer: ["Mother 👩", "Father 👨", "Sister 👧"], hint: "Family = семья" },
      { type: 'fill', question: "Brother = __ (брат)", correctAnswer: "брат", hint: "Brother - это брат" },
      { type: 'quiz', question: "Grandmother - это...", options: ["Мама", "Сестра", "Бабушка 👵", "Тётя", "Дочь"], correctAnswer: "Бабушка 👵", hint: "Grandmother = бабушка" },
      { type: 'quiz', question: "Sister - это...", options: ["Брат", "Мама", "Сестра 👧", "Бабушка", "Тётя"], correctAnswer: "Сестра 👧", hint: "Sister = сестра" },
      { type: 'quiz', question: "Uncle - это...", options: ["Папа", "Дядя", "Брат", "Дедушка", "Сын"], correctAnswer: "Дядя", hint: "Uncle = дядя" }
    ],
    reward: { stars: 3, message: "Great! Ты знаешь семью! 👨‍👩‍👧‍👦" }
  },
  {
    title: "Животные по-английски",
    subject: "Английский",
    icon: "Languages",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: "Cat - это...", options: ["Собака", "Кошка", "Птица", "Рыба", "Лягушка"], correctAnswer: "Кошка", hint: "Cat = кошка 🐱" },
      { type: 'quiz', question: "Как будет «собака»?", options: ["Cat", "Dog", "Bird", "Fish", "Cow"], correctAnswer: "Dog", hint: "Dog = собака 🐕" },
      { type: 'fill', question: "Fish = __ (рыба)", correctAnswer: "рыба", hint: "Fish плавает в воде" },
      { type: 'find', question: "Выбери названия животных:", options: ["Cat 🐱", "Red", "Dog 🐕", "Big", "Bird 🐦"], correctAnswer: ["Cat 🐱", "Dog 🐕", "Bird 🐦"], hint: "Animals = животные" },
      { type: 'quiz', question: "Bear - это...", options: ["Зайец 🐰", "Медведь 🐻", "Лиса 🦊", "Волк 🐺", "Ёж 🦔"], correctAnswer: "Медведь 🐻", hint: "Bear = медведь" },
      { type: 'quiz', question: "Bird - это...", options: ["Рыба 🐟", "Птица 🐦", "Собака 🐕", "Кошка 🐱", "Лягушка 🐸"], correctAnswer: "Птица 🐦", hint: "Bird = птица" },
      { type: 'quiz', question: "Cow - это...", options: ["Лошадь 🐴", "Свинья 🐷", "Корова 🐄", "Овца 🐑", "Коза 🐐"], correctAnswer: "Корова 🐄", hint: "Cow = корова" }
    ],
    reward: { stars: 3, message: "Wonderful! Ты знаешь животных! 🐾" }
  }
]
