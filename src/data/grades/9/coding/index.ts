import { Subject, SubjectData, GameLesson } from '../../../types'

const lessons: SubjectData = {
  id: 'coding',
  title: 'Программирование',
  icon: 'Code',
  color: '#10B981',
  topics: [
    'Алгоритмы и структуры данных',
    'Объектно-ориентированное программирование',
    'Работа с файлами и базами данных',
    'Веб-разработка',
    'Графический интерфейс',
    'Отладка и тестирование',
    'Командная разработка',
    'Проектная работа'
  ],
  detailedTopics: [
    {
      title: 'Алгоритмы и структуры данных',
      lessons: [
        {
          title: 'Сложность алгоритмов',
          content: 'Сложность алгоритма показывает, как быстро растёт время выполнения с ростом входных данных. O(1) — константная сложность, не зависит от размера данных. O(n) — линейная сложность, растёт пропорционально. O(n²) — квадратичная сложность. O(log n) — логарифмическая сложность. Анализ сложности важен для оптимизации программ.',
          practice: 'Определите сложность алгоритма поиска элемента в неотсортированном списке.'
        },
        {
          title: 'Сортировка данных',
          content: 'Сортировка — упорядочивание элементов. Пузырьковая сортировка: простой, но медленный алгоритм O(n²). Сортировка выбором: находим минимум и ставим в начало. Быстрая сортировка: рекурсивный алгоритм O(n log n). Сортировка слиянием: стабильная, гарантированная сложность. Встроенные функции сортировки обычно оптимизированы.',
          practice: 'Реализуйте один из алгоритмов сортировки на Python.'
        },
        {
          title: 'Стек и очередь',
          content: 'Стек — структура LIFO (Last In, First Out). Операции: push (добавить), pop (удалить последний). Пример: история браузера, отмена действий. Очередь — структура FIFO (First In, First Out). Операции: enqueue (добавить в конец), dequeue (удалить из начала). Пример: очередь печати, обработка запросов.',
          practice: 'Реализуйте стек с помощью списка и проверьте его работу.'
        },
        {
          title: 'Деревья и графы',
          content: 'Дерево — иерархическая структура с корнем и узлами. Бинарное дерево: каждый узел имеет не более двух детей. Обход дерева: прямой, симметричный, обратный. Граф — набор вершин и рёбер. Поиск в ширину (BFS) и в глубину (DFS). Графы применяются для моделирования сетей, маршрутов.',
          practice: 'Нарисуйте бинарное дерево и опишите порядок обхода.'
        }
      ]
    },
    {
      title: 'Объектно-ориентированное программирование',
      lessons: [
        {
          title: 'Классы и объекты',
          content: 'Класс — это шаблон для создания объектов. Класс описывает свойства (атрибуты) и поведение (методы). Объект — экземпляр класса с конкретными значениями атрибутов. Конструктор — метод для создания объекта. self в Python ссылается на текущий объект.',
          practice: 'Создайте класс Student с атрибутами имя, возраст, класс.'
        },
        {
          title: 'Инкапсуляция',
          content: 'Инкапсуляция — скрытие внутренней реализации объекта. Публичные атрибуты доступны извне. Приватные атрибуты (с _) доступны только внутри класса. Свойства (property) контролируют доступ к атрибутам. Инкапсуляция защищает данные от некорректного изменения.',
          practice: 'Добавьте приватный атрибут и свойство для контролируемого доступа.'
        },
        {
          title: 'Наследование',
          content: 'Наследование — создание нового класса на основе существующего. Родительский класс (базовый) передаёт свойства и методы. Дочерний класс (производный) наследует и расширяет. Переопределение методов — изменение поведения. super() вызывает метод родительского класса.',
          practice: 'Создайте класс HighSchoolStudent, наследующий от Student.'
        },
        {
          title: 'Полиморфизм',
          content: 'Полиморфизм — единый интерфейс для разных форм. Методы с одинаковым именем работают по-разному в разных классах. Полиморфизм позволяет работать с объектами разных классов одинаково. Абстрактные классы определяют интерфейс без реализации. Полиморфизм упрощает код и повышает гибкость.',
          practice: 'Создайте метод info() в разных классах с разной реализацией.'
        }
      ]
    },
    {
      title: 'Работа с файлами и базами данных',
      lessons: [
        {
          title: 'Чтение и запись файлов',
          content: 'Файлы хранят данные между запусками программы. Открытие файла: open(имя, режим). Режимы: "r" — чтение, "w" — запись, "a" — добавление. with автоматически закрывает файл. read() читает весь файл, readline() — одну строку. write() записывает строку в файл.',
          practice: 'Напишите программу, которая сохраняет список задач в файл и читает его.'
        },
        {
          title: 'Работа с CSV и JSON',
          content: 'CSV — формат табличных данных, разделённых запятыми. Модуль csv упрощает работу с CSV-файлами. JSON — формат для хранения структурированных данных. JSON поддерживает: объекты, массивы, строки, числа, булевы значения. json.dumps() и json.loads() для преобразования.',
          practice: 'Сохраните словарь с данными о книгах в формате JSON.'
        },
        {
          title: 'Основы SQL',
          content: 'SQL — язык запросов к базам данных. SELECT — выборка данных: SELECT * FROM table. INSERT — добавление: INSERT INTO table VALUES (...). UPDATE — обновление: UPDATE table SET column = value. DELETE — удаление: DELETE FROM table WHERE condition. WHERE — условие фильтрации.',
          practice: 'Напишите SQL-запрос для выборки учеников старше 15 лет.'
        },
        {
          title: 'SQLite в Python',
          content: 'SQLite — встроенная база данных, не требует сервера. Модуль sqlite3 входит в стандартную библиотеку Python. Соединение: sqlite3.connect("file.db"). Курсор — объект для выполнения запросов. cursor.execute() выполняет SQL-запрос. fetchall() возвращает все результаты.',
          practice: 'Создайте базу данных с таблицей учеников и выполните запрос.'
        }
      ]
    },
    {
      title: 'Веб-разработка',
      lessons: [
        {
          title: 'Основы HTML',
          content: 'HTML — язык разметки веб-страниц. Структура: <!DOCTYPE html>, <html>, <head>, <body>. Теги: <h1>-<h6> — заголовки, <p> — абзац, <a> — ссылка, <img> — изображение. Атрибуты: href, src, class, id. Семантические теги: <header>, <nav>, <main>, <footer>.',
          practice: 'Создайте HTML-страницу с заголовком, абзацами и списком.'
        },
        {
          title: 'CSS для стилизации',
          content: 'CSS — каскадные таблицы стилей. Селекторы: по тегу, классу, id. Свойства: color, background, font-size, margin, padding. Box model: content, padding, border, margin. Flexbox и Grid — современные способы вёрстки. Стили подключаются через тег <link>.',
          practice: 'Добавьте стили к вашей HTML-странице: цвета, отступы, шрифты.'
        },
        {
          title: 'Flask: создание веб-приложения',
          content: 'Flask — микрофреймворк для веб-приложений на Python. @app.route("/") определяет обработчик URL. render_template() возвращает HTML-шаблон. request содержит данные запроса. app.run() запускает сервер. Flask подходит для небольших и средних проектов.',
          practice: 'Создайте простое веб-приложение с одной страницей.'
        },
        {
          title: 'Формы и обработка данных',
          content: 'HTML-формы собирают данные пользователя. <form action="..." method="post">. Элементы: <input>, <textarea>, <select>, <button>. Flask: request.form содержит данные формы. Валидация — проверка корректности данных. POST-запросы отправляют данные, GET — запрашивают.',
          practice: 'Создайте форму регистрации и обработайте данные на сервере.'
        }
      ]
    },
    {
      title: 'Графический интерфейс',
      lessons: [
        {
          title: 'Библиотека Tkinter',
          content: 'Tkinter — стандартная библиотека GUI для Python. Виджеты: Label, Button, Entry, Text, Listbox. Главный цикл: root.mainloop(). Менеджеры компоновки: pack, grid, place. События — действия пользователя: клик, ввод текста. Обработчики событий — функции, вызываемые при событии.',
          practice: 'Создайте окно с кнопкой, которая выводит сообщение.'
        },
        {
          title: 'Создание форм',
          content: 'Entry — поле для ввода одной строки. Text — многострочное поле. Label — текстовая метка. Checkbutton — флажок. Radiobutton — переключатель. get() получает данные из виджета. insert() добавляет текст в виджет. delete() удаляет содержимое.',
          practice: 'Создайте форму калькулятора с полями ввода и кнопками операций.'
        },
        {
          title: 'Обработка событий',
          content: 'command — привязка функции к кнопке. bind() — привязка события к виджету. События: <Button-1> — клик, <Key> — нажатие клавиши. event — объект с информацией о событии. Лямбда-функции для передачи аргументов.',
          practice: 'Добавьте обработку клавиши Enter для отправки формы.'
        },
        {
          title: 'Меню и диалоги',
          content: 'Menu — создание меню. add_cascade — вложенное меню. add_command — пункт меню. messagebox — диалоговые окна: showinfo, askquestion. filedialog — диалог выбора файла. askopenfilename — открыть файл, asksaveasfilename — сохранить.',
          practice: 'Добавьте меню с пунктами "Файл" и "Справка" в ваше приложение.'
        }
      ]
    },
    {
      title: 'Отладка и тестирование',
      lessons: [
        {
          title: 'Методы отладки',
          content: 'Print-отладка — вывод значений в консоль. Отладчик (debugger) — пошаговое выполнение. Точки останова (breakpoints) — пауза в выполнении. Просмотр значений переменных. pdb — отладчик Python в командной строке. IDE (PyCharm, VS Code) имеют встроенные отладчики.',
          practice: 'Используйте отладчик для поиска ошибки в программе.'
        },
        {
          title: 'Unit-тестирование',
          content: 'Unit-тест — проверка отдельной функции или метода. Модуль unittest — встроенный фреймворк. TestCase — класс для создания тестов. assertEqual, assertTrue, assertRaises — проверки. setUp и tearDown — подготовка и очистка. Запуск тестов: python -m unittest.',
          practice: 'Напишите unit-тесты для функции сортировки списка.'
        },
        {
          title: 'Документирование кода',
          content: 'Docstring — строка документации функции. Комментарии (#) объясняют сложные места. README.md — описание проекта. Типизация (type hints) — указание типов аргументов и возвращаемого значения. Документация помогает другим (и себе) понимать код.',
          practice: 'Добавьте docstring к вашим функциям с описанием параметров.'
        },
        {
          title: 'Обработка ошибок',
          content: 'try-except — обработка исключений. finally — блок, выполняемый всегда. raise — генерация исключения. Собственные исключения — наследование от Exception. Контекстные менеджеры (with) автоматически управляют ресурсами. Правильная обработка ошибок делает программу надёжной.',
          practice: 'Добавьте обработку исключений при работе с файлами.'
        }
      ]
    },
    {
      title: 'Командная разработка',
      lessons: [
        {
          title: 'Git: контроль версий',
          content: 'Git — система контроля версий. git init — создание репозитория. git add — добавление файлов. git commit — фиксация изменений. git log — история коммитов. git diff — различия между версиями. git checkout — переключение между версиями.',
          practice: 'Инициализируйте репозиторий и сделайте первый коммит.'
        },
        {
          title: 'Ветвление и слияние',
          content: 'Ветка (branch) — независимая линия разработки. git branch — список веток. git checkout -b — создание и переключение. git merge — слияние веток. Конфликты — несовместимые изменения. Разрешение конфликтов — ручное редактирование.',
          practice: 'Создайте ветку для новой функции, внесите изменения и слейте с main.'
        },
        {
          title: 'GitHub для совместной работы',
          content: 'GitHub — платформа для хостинга Git-репозиториев. git remote add — привязка удалённого репозитория. git push — отправка изменений. git pull — получение изменений. Pull request — предложение изменений. Code review — проверка кода другими разработчиками.',
          practice: 'Опубликуйте ваш проект на GitHub.'
        },
        {
          title: 'Стиль кода и соглашения',
          content: 'PEP 8 — стиль кода Python. Отступы: 4 пробела. Длина строки: до 79 символов. Имена: snake_case для функций, CamelCase для классов. Документация и комментарии. Линтеры (pylint, flake8) проверяют стиль. Единый стиль упрощает чтение кода команды.',
          practice: 'Проверьте ваш код на соответствие PEP 8 и исправьте нарушения.'
        }
      ]
    },
    {
      title: 'Проектная работа',
      lessons: [
        {
          title: 'Выбор и планирование проекта',
          content: 'Критерии выбора: интерес, посильность, польза. Определение функциональных требований. Составление технического задания. Декомпозиция на подзадачи. Оценка времени на каждую задачу. Приоритизация: MVP (минимальный жизнеспособный продукт).',
          practice: 'Выберите проект и составьте план его реализации.'
        },
        {
          title: 'Реализация проекта',
          content: 'Итеративная разработка: маленькие шаги. Регулярные коммиты в Git. Тестирование после каждого изменения. Документирование по ходу работы. Рефакторинг — улучшение кода без изменения функциональности. Управление временем и приоритетами.',
          practice: 'Начните реализацию вашего проекта с первой задачи.'
        },
        {
          title: 'Презентация проекта',
          content: 'Структура презентации: проблема, решение, демонстрация. Подготовка демонстрации работы. Объяснение технических решений. Ответы на вопросы аудитории. Получение обратной связи. Итерации улучшения на основе отзывов.',
          practice: 'Подготовьте презентацию вашего проекта.'
        },
        {
          title: 'Анализ и развитие',
          content: 'Ретроспектива: что получилось, что можно улучшить. Анализ возникших проблем и их решений. Планирование следующих шагов развития. Возможности расширения функциональности. Портфолио проектов для будущей карьеры. Непрерывное обучение — ключ к успеху.',
          practice: 'Напишите отчёт о проекте: что узнали, с чем столкнулись, что улучшите.'
        }
      ]
    }
  ]
}

export const games: GameLesson[] = [
  {
    title: "Сложность алгоритмов",
    subject: "Программирование",
    icon: "Activity",
    color: "text-indigo-400",
    tasks: [
      { type: 'quiz', question: 'Какая сложность означает константное время?', options: ['O(1)', 'O(n)', 'O(n²)', 'O(log n)'], correctAnswer: 'O(1)', hint: 'Не зависит от размера данных' },
      { type: 'fill', question: 'Линейная сложность обозначается как O(___).', correctAnswer: 'n', hint: 'Время растёт пропорционально данным' },
      { type: 'quiz', question: 'Какая сложность у пузырьковой сортировки?', options: ['O(n²)', 'O(n)', 'O(log n)', 'O(1)'], correctAnswer: 'O(n²)', hint: 'Два вложенных цикла' },
      { type: 'fill', question: 'Сложность O(log n) — ___ сложность.', correctAnswer: 'логарифмическая', hint: 'Бинарный поиск' },
      { type: 'quiz', question: 'O(n log n) — сложность:', options: ['Быстрой сортировки', 'Пузырьковой', 'Линейного поиска', 'Константная'], correctAnswer: 'Быстрой сортировки', hint: 'Эффективный алгоритм' }
    ],
    reward: { stars: 3, message: "Ты понимаешь сложность алгоритмов! 📊" }
  },
  {
    title: "Сортировка данных",
    subject: "Программирование",
    icon: "ArrowUpDown",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: 'Упорядочивание элементов — это ___ .', correctAnswer: 'сортировка', hint: 'Расстановка по порядку' },
      { type: 'quiz', question: 'Какой алгоритм сортировки самый простой?', options: ['Пузырьковый', 'Быстрый', 'Слиянием', 'Пирамидальный'], correctAnswer: 'Пузырьковый', hint: 'Но медленный O(n²)' },
      { type: 'fill', question: 'Быстрая сортировка работает за O(n log ___).', correctAnswer: 'n', hint: 'В среднем случае' },
      { type: 'quiz', question: 'Сортировка выбором:', options: ['Находит минимум и ставит в начало', 'Меняет соседние элементы', 'Делит массив пополам', 'Использует пирамиду'], correctAnswer: 'Находит минимум и ставит в начало', hint: 'Постепенно заполняем начало' },
      { type: 'fill', question: 'Сортировка слиянием — ___ алгоритм.', correctAnswer: 'стабильный', hint: 'Сохраняет порядок равных' }
    ],
    reward: { stars: 3, message: "Ты понимаешь сортировку! 🔄" }
  },
  {
    title: "Стек и очередь",
    subject: "Программирование",
    icon: "Layers",
    color: "text-purple-400",
    tasks: [
      { type: 'fill', question: 'LIFO расшифровывается как Last In, First ___ .', correctAnswer: 'Out', hint: 'Последний пришёл — первый вышел' },
      { type: 'quiz', question: 'Стек работает по принципу:', options: ['LIFO', 'FIFO', 'LILO', 'FILO'], correctAnswer: 'LIFO', hint: 'Стек блюд' },
      { type: 'fill', question: 'Операция добавления в стек — ___ .', correctAnswer: 'push', hint: 'Поместить наверх' },
      { type: 'quiz', question: 'Очередь работает по принципу:', options: ['FIFO', 'LIFO', 'LILO', 'FILO'], correctAnswer: 'FIFO', hint: 'Очередь в магазине' },
      { type: 'fill', question: 'Операция удаления из очереди — ___ .', correctAnswer: 'dequeue', hint: 'Убрать из начала' }
    ],
    reward: { stars: 3, message: "Ты понимаешь стек и очередь! 📚" }
  },
  {
    title: "Деревья и графы",
    subject: "Программирование",
    icon: "GitBranch",
    color: "text-green-400",
    tasks: [
      { type: 'fill', question: 'Дерево — ___ структура с корнем и узлами.', correctAnswer: 'иерархическая', hint: 'Один корень, много ветвей' },
      { type: 'quiz', question: 'Бинарное дерево имеет не более:', options: ['Двух детей у узла', 'Одного ребёнка', 'Трёх детей', 'Любое количество'], correctAnswer: 'Двух детей у узла', hint: 'Бинарное = двоичное' },
      { type: 'fill', question: 'Граф — набор вершин и ___ .', correctAnswer: 'рёбер', hint: 'Связи между вершинами' },
      { type: 'quiz', question: 'BFS — это поиск:', options: ['В ширину', 'В глубину', 'Бинарный', 'Линейный'], correctAnswer: 'В ширину', hint: 'Breadth-First Search' },
      { type: 'fill', question: 'DFS — поиск в ___ .', correctAnswer: 'глубину', hint: 'Deep-First Search' }
    ],
    reward: { stars: 3, message: "Ты понимаешь деревья и графы! 🌳" }
  },
  {
    title: "Классы и объекты",
    subject: "Программирование",
    icon: "Box",
    color: "text-emerald-400",
    tasks: [
      { type: 'fill', question: 'Класс — это ___ для создания объектов.', correctAnswer: 'шаблон', hint: 'Чертёж' },
      { type: 'quiz', question: 'Объект — это:', options: ['Экземпляр класса', 'Шаблон класса', 'Метод класса', 'Атрибут класса'], correctAnswer: 'Экземпляр класса', hint: 'Конкретный представитель' },
      { type: 'fill', question: '___ в Python ссылается на текущий объект.', correctAnswer: 'self', hint: 'Ключевое слово' },
      { type: 'quiz', question: 'Конструктор — это метод:', options: ['Для создания объекта', 'Для удаления объекта', 'Для копирования', 'Для сравнения'], correctAnswer: 'Для создания объекта', hint: '__init__ в Python' },
      { type: 'fill', question: 'Атрибуты — это ___ класса.', correctAnswer: 'свойства', hint: 'Данные объекта' }
    ],
    reward: { stars: 3, message: "Ты понимаешь классы и объекты! 📦" }
  },
  {
    title: "Инкапсуляция",
    subject: "Программирование",
    icon: "Lock",
    color: "text-red-400",
    tasks: [
      { type: 'fill', question: 'Инкапсуляция — ___ внутренней реализации.', correctAnswer: 'скрытие', hint: 'Защита данных' },
      { type: 'quiz', question: 'Приватные атрибуты в Python начинаются с:', options: ['_', '__', '@', '#'], correctAnswer: '_', hint: 'Одно или два подчёркивания' },
      { type: 'fill', question: '___ контролируют доступ к атрибутам.', correctAnswer: 'свойства', hint: 'property в Python' },
      { type: 'quiz', question: 'Публичные атрибуты:', options: ['Доступны извне', 'Скрыты', 'Только для чтения', 'Удалены'], correctAnswer: 'Доступны извне', hint: 'Без ограничений' },
      { type: 'fill', question: 'Инкапсуляция защищает данные от ___ изменения.', correctAnswer: 'некорректного', hint: 'Безопасность' }
    ],
    reward: { stars: 3, message: "Ты понимаешь инкапсуляцию! 🔒" }
  },
  {
    title: "Наследование",
    subject: "Программирование",
    icon: "GitMerge",
    color: "text-orange-400",
    tasks: [
      { type: 'fill', question: 'Наследование — создание нового класса на основе ___ .', correctAnswer: 'существующего', hint: 'Базовый класс' },
      { type: 'quiz', question: 'Родительский класс также называют:', options: ['Базовым', 'Производным', 'Дочерним', 'Наследником'], correctAnswer: 'Базовым', hint: 'Основа' },
      { type: 'fill', question: '___ вызывает метод родительского класса.', correctAnswer: 'super()', hint: 'Функция в Python' },
      { type: 'quiz', question: 'Переопределение методов — это:', options: ['Изменение поведения', 'Удаление метода', 'Добавление метода', 'Копирование метода'], correctAnswer: 'Изменение поведения', hint: 'Новая реализация' },
      { type: 'fill', question: 'Дочерний класс ___ родительский.', correctAnswer: 'расширяет', hint: 'Добавляет функциональность' }
    ],
    reward: { stars: 3, message: "Ты понимаешь наследование! 🔀" }
  },
  {
    title: "Полиморфизм",
    subject: "Программирование",
    icon: "Copy",
    color: "text-cyan-400",
    tasks: [
      { type: 'fill', question: 'Полиморфизм — единый ___ для разных форм.', correctAnswer: 'интерфейс', hint: 'Один метод — разное поведение' },
      { type: 'quiz', question: 'Методы с одинаковым именем в разных классах:', options: ['Работают по-разному', 'Одинаково', 'Не работают', 'Дублируются'], correctAnswer: 'Работают по-разному', hint: 'Суть полиморфизма' },
      { type: 'fill', question: '___ классы определяют интерфейс без реализации.', correctAnswer: 'Абстрактные', hint: 'ABC в Python' },
      { type: 'quiz', question: 'Полиморфизм позволяет:', options: ['Работать с разными классами одинаково', 'Создавать классы', 'Удалять методы', 'Копировать объекты'], correctAnswer: 'Работать с разными классами одинаково', hint: 'Гибкость кода' },
      { type: 'fill', question: 'Полиморфизм ___ код.', correctAnswer: 'упрощает', hint: 'Удобство' }
    ],
    reward: { stars: 3, message: "Ты понимаешь полиморфизм! 🎭" }
  },
  {
    title: "Чтение и запись файлов",
    subject: "Программирование",
    icon: "FileText",
    color: "text-yellow-400",
    tasks: [
      { type: 'fill', question: 'Файлы хранят данные между ___ программы.', correctAnswer: 'запусками', hint: 'Сохранение' },
      { type: 'quiz', question: 'Режим "r" означает:', options: ['Чтение', 'Запись', 'Добавление', 'Удаление'], correctAnswer: 'Чтение', hint: 'Read' },
      { type: 'fill', question: 'Режим "w" — ___ в файл.', correctAnswer: 'запись', hint: 'Write' },
      { type: 'quiz', question: 'with автоматически:', options: ['Закрывает файл', 'Открывает файл', 'Читает файл', 'Удаляет файл'], correctAnswer: 'Закрывает файл', hint: 'Контекстный менеджер' },
      { type: 'fill', question: '___ () читает весь файл.', correctAnswer: 'read', hint: 'Одним вызовом' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с файлами! 📄" }
  },
  {
    title: "Работа с CSV и JSON",
    subject: "Программирование",
    icon: "FileJson",
    color: "text-amber-400",
    tasks: [
      { type: 'fill', question: 'CSV — формат ___ данных.', correctAnswer: 'табличных', hint: 'Разделённые запятыми' },
      { type: 'quiz', question: 'JSON поддерживает:', options: ['Объекты и массивы', 'Только строки', 'Только числа', 'Только булевы'], correctAnswer: 'Объекты и массивы', hint: 'Структурированные данные' },
      { type: 'fill', question: 'json.___() преобразует объект в строку.', correctAnswer: 'dumps', hint: 'Сериализация' },
      { type: 'quiz', question: 'json.loads() выполняет:', options: ['Десериализацию', 'Сериализацию', 'Удаление', 'Чтение файла'], correctAnswer: 'Десериализацию', hint: 'Строка в объект' },
      { type: 'fill', question: 'CSV расшифровывается как Comma-Separated ___ .', correctAnswer: 'Values', hint: 'Значения' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с CSV и JSON! 📋" }
  },
  {
    title: "Основы SQL",
    subject: "Программирование",
    icon: "Database",
    color: "text-blue-500",
    tasks: [
      { type: 'fill', question: 'SQL — язык ___ к базам данных.', correctAnswer: 'запросов', hint: 'Structured Query Language' },
      { type: 'quiz', question: 'SELECT — это:', options: ['Выборка данных', 'Добавление данных', 'Удаление данных', 'Обновление данных'], correctAnswer: 'Выборка данных', hint: 'Чтение из таблицы' },
      { type: 'fill', question: 'INSERT ___ добавляет данные.', correctAnswer: 'INTO', hint: 'Вставить в таблицу' },
      { type: 'quiz', question: 'DELETE удаляет:', options: ['Данные', 'Таблицу', 'Базу', 'Столбец'], correctAnswer: 'Данные', hint: 'С условием WHERE' },
      { type: 'fill', question: 'WHERE — условие ___ .', correctAnswer: 'фильтрации', hint: 'Отбор записей' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы SQL! 💾" }
  },
  {
    title: "SQLite в Python",
    subject: "Программирование",
    icon: "HardDrive",
    color: "text-slate-400",
    tasks: [
      { type: 'fill', question: 'SQLite — ___ база данных.', correctAnswer: 'встроенная', hint: 'Не требует сервера' },
      { type: 'quiz', question: 'Модуль для работы с SQLite:', options: ['sqlite3', 'sql', 'database', 'db'], correctAnswer: 'sqlite3', hint: 'Стандартная библиотека' },
      { type: 'fill', question: 'sqlite3.___() создаёт соединение.', correctAnswer: 'connect', hint: 'Подключение к БД' },
      { type: 'quiz', question: 'Курсор используется для:', options: ['Выполнения запросов', 'Создания БД', 'Закрытия БД', 'Резервного копирования'], correctAnswer: 'Выполнения запросов', hint: 'cursor.execute()' },
      { type: 'fill', question: 'fetchall() возвращает все ___ .', correctAnswer: 'результаты', hint: 'Список записей' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с SQLite! 🗄️" }
  },
  {
    title: "Основы HTML",
    subject: "Программирование",
    icon: "Code",
    color: "text-orange-500",
    tasks: [
      { type: 'fill', question: 'HTML — язык ___ веб-страниц.', correctAnswer: 'разметки', hint: 'Структура страницы' },
      { type: 'quiz', question: 'Тег для заголовка:', options: ['<h1>', '<header>', '<heading>', '<title>'], correctAnswer: '<h1>', hint: 'От h1 до h6' },
      { type: 'fill', question: 'Тег <___> создаёт ссылку.', correctAnswer: 'a', hint: 'Anchor' },
      { type: 'quiz', question: 'Атрибут для адреса ссылки:', options: ['href', 'src', 'link', 'url'], correctAnswer: 'href', hint: 'Hypertext Reference' },
      { type: 'fill', question: '<img> — тег для ___ .', correctAnswer: 'изображения', hint: 'Picture' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы HTML! 🌐" }
  },
  {
    title: "CSS для стилизации",
    subject: "Программирование",
    icon: "Palette",
    color: "text-pink-400",
    tasks: [
      { type: 'fill', question: 'CSS — ___ таблицы стилей.', correctAnswer: 'каскадные', hint: 'Cascading Style Sheets' },
      { type: 'quiz', question: 'Селектор по классу:', options: ['.class', '#class', 'class', '@class'], correctAnswer: '.class', hint: 'Точка перед именем' },
      { type: 'fill', question: 'Box model: content, padding, border, ___ .', correctAnswer: 'margin', hint: 'Внешний отступ' },
      { type: 'quiz', question: 'Flexbox используется для:', options: ['Вёрстки', 'Анимации', 'Форм', 'Базы данных'], correctAnswer: 'Вёрстки', hint: 'Расположение элементов' },
      { type: 'fill', question: 'Свойство color изменяет ___ текста.', correctAnswer: 'цвет', hint: 'Оформление' }
    ],
    reward: { stars: 3, message: "Ты знаешь CSS! 🎨" }
  },
  {
    title: "Flask: создание веб-приложения",
    subject: "Программирование",
    icon: "Flame",
    color: "text-gray-400",
    tasks: [
      { type: 'fill', question: 'Flask — ___ для веб-приложений.', correctAnswer: 'микрофреймворк', hint: 'Лёгкий фреймворк' },
      { type: 'quiz', question: 'Декоратор для маршрута:', options: ['@app.route', '@route', '@url', '@path'], correctAnswer: '@app.route', hint: 'Связывает URL с функцией' },
      { type: 'fill', question: 'render___() возвращает HTML-шаблон.', correctAnswer: 'template', hint: 'Рендеринг' },
      { type: 'quiz', question: 'app.run() запускает:', options: ['Сервер', 'Базу данных', 'Тесты', 'Компилятор'], correctAnswer: 'Сервер', hint: 'Локальный сервер' },
      { type: 'fill', question: 'request содержит ___ запроса.', correctAnswer: 'данные', hint: 'Информация от клиента' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать веб-приложения! 🔥" }
  },
  {
    title: "Формы и обработка данных",
    subject: "Программирование",
    icon: "FileInput",
    color: "text-teal-400",
    tasks: [
      { type: 'fill', question: 'HTML-формы ___ данные пользователя.', correctAnswer: 'собирают', hint: 'Ввод информации' },
      { type: 'quiz', question: 'Метод POST:', options: ['Отправляет данные', 'Запрашивает данные', 'Удаляет данные', 'Обновляет данные'], correctAnswer: 'Отправляет данные', hint: 'Передача на сервер' },
      { type: 'fill', question: '<input> — поле для ___ .', correctAnswer: 'ввода', hint: 'Текст, число, файл' },
      { type: 'quiz', question: 'Валидация — это:', options: ['Проверка корректности', 'Отправка данных', 'Сохранение данных', 'Удаление данных'], correctAnswer: 'Проверка корректности', hint: 'Правильность данных' },
      { type: 'fill', question: 'request.___ содержит данные формы.', correctAnswer: 'form', hint: 'В Flask' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с формами! 📝" }
  },
  {
    title: "Библиотека Tkinter",
    subject: "Программирование",
    icon: "Layout",
    color: "text-violet-400",
    tasks: [
      { type: 'fill', question: 'Tkinter — библиотека для ___ интерфейса.', correctAnswer: 'графического', hint: 'GUI' },
      { type: 'quiz', question: 'Виджет Button — это:', options: ['Кнопка', 'Поле ввода', 'Метка', 'Список'], correctAnswer: 'Кнопка', hint: 'Нажимается' },
      { type: 'fill', question: 'root.___() запускает главный цикл.', correctAnswer: 'mainloop', hint: 'Обработка событий' },
      { type: 'quiz', question: 'Менеджер компоновки pack:', options: ['Упаковывает виджеты', 'Удаляет виджеты', 'Создаёт виджеты', 'Копирует виджеты'], correctAnswer: 'Упаковывает виджеты', hint: 'Размещение в окне' },
      { type: 'fill', question: 'События — действия ___ .', correctAnswer: 'пользователя', hint: 'Клик, ввод' }
    ],
    reward: { stars: 3, message: "Ты знаешь Tkinter! 🖼️" }
  },
  {
    title: "Создание форм",
    subject: "Программирование",
    icon: "FormInput",
    color: "text-lime-400",
    tasks: [
      { type: 'fill', question: 'Entry — поле для ввода ___ строки.', correctAnswer: 'одной', hint: 'Одиночный ввод' },
      { type: 'quiz', question: 'Text — это:', options: ['Многострочное поле', 'Однострочное поле', 'Кнопка', 'Метка'], correctAnswer: 'Многострочное поле', hint: 'Несколько строк' },
      { type: 'fill', question: '___ () получает данные из виджета.', correctAnswer: 'get', hint: 'Извлечение' },
      { type: 'quiz', question: 'Checkbutton — это:', options: ['Флажок', 'Переключатель', 'Кнопка', 'Поле'], correctAnswer: 'Флажок', hint: 'Галочка' },
      { type: 'fill', question: 'insert() ___ текст в виджет.', correctAnswer: 'добавляет', hint: 'Вставка' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать формы! 📊" }
  },
  {
    title: "Обработка событий",
    subject: "Программирование",
    icon: "MousePointer",
    color: "text-fuchsia-400",
    tasks: [
      { type: 'fill', question: 'command — привязка функции к ___ .', correctAnswer: 'кнопке', hint: 'При нажатии' },
      { type: 'quiz', question: 'bind() привязывает:', options: ['Событие к виджету', 'Виджет к окну', 'Функцию к классу', 'Переменную к значению'], correctAnswer: 'Событие к виджету', hint: 'Обработка действий' },
      { type: 'fill', question: '<Button-1> — событие ___ .', correctAnswer: 'клика', hint: 'Нажатие кнопки мыши' },
      { type: 'quiz', question: '<Key> — это событие:', options: ['Нажатия клавиши', 'Клика мышью', 'Движения мыши', 'Закрытия окна'], correctAnswer: 'Нажатия клавиши', hint: 'Клавиатура' },
      { type: 'fill', question: '___ -функции для передачи аргументов.', correctAnswer: 'лямбда', hint: 'lambda' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать события! 🖱️" }
  },
  {
    title: "Меню и диалоги",
    subject: "Программирование",
    icon: "Menu",
    color: "text-rose-400",
    tasks: [
      { type: 'fill', question: 'Menu — создание ___ .', correctAnswer: 'меню', hint: 'Панель с пунктами' },
      { type: 'quiz', question: 'add_cascade создаёт:', options: ['Вложенное меню', 'Пункт меню', 'Разделитель', 'Кнопку'], correctAnswer: 'Вложенное меню', hint: 'Подменю' },
      { type: 'fill', question: 'messagebox — ___ окна.', correctAnswer: 'диалоговые', hint: 'Сообщения' },
      { type: 'quiz', question: 'showinfo показывает:', options: ['Информационное сообщение', 'Вопрос', 'Ошибку', 'Файл'], correctAnswer: 'Информационное сообщение', hint: 'Уведомление' },
      { type: 'fill', question: 'filedialog — диалог выбора ___ .', correctAnswer: 'файла', hint: 'Открыть/сохранить' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать меню! 📋" }
  },
  {
    title: "Методы отладки",
    subject: "Программирование",
    icon: "Bug",
    color: "text-red-500",
    tasks: [
      { type: 'fill', question: 'Print-отладка — вывод значений в ___ .', correctAnswer: 'консоль', hint: 'Терминал' },
      { type: 'quiz', question: 'Отладчик выполняет:', options: ['Пошаговое выполнение', 'Компиляцию', 'Интерпретацию', 'Деплой'], correctAnswer: 'Пошаговое выполнение', hint: 'Debug' },
      { type: 'fill', question: 'Точки останова — ___ в выполнении.', correctAnswer: 'пауза', hint: 'Breakpoints' },
      { type: 'quiz', question: 'pdb — это:', options: ['Отладчик Python', 'Компилятор', 'Интерпретатор', 'Редактор'], correctAnswer: 'Отладчик Python', hint: 'В командной строке' },
      { type: 'fill', question: 'IDE имеют ___ отладчики.', correctAnswer: 'встроенные', hint: 'PyCharm, VS Code' }
    ],
    reward: { stars: 3, message: "Ты умеешь отлаживать код! 🐛" }
  },
  {
    title: "Unit-тестирование",
    subject: "Программирование",
    icon: "CheckCircle",
    color: "text-green-500",
    tasks: [
      { type: 'fill', question: 'Unit-тест проверяет отдельную ___ .', correctAnswer: 'функцию', hint: 'Или метод' },
      { type: 'quiz', question: 'Модуль для тестирования в Python:', options: ['unittest', 'test', 'testing', 'pytest'], correctAnswer: 'unittest', hint: 'Стандартный модуль' },
      { type: 'fill', question: '___ — класс для создания тестов.', correctAnswer: 'TestCase', hint: 'Наследование' },
      { type: 'quiz', question: 'assertEqual проверяет:', options: ['Равенство', 'Истинность', 'Исключение', 'Тип'], correctAnswer: 'Равенство', hint: 'Сравнение значений' },
      { type: 'fill', question: 'setUp — ___ к тесту.', correctAnswer: 'подготовка', hint: 'Выполняется до' }
    ],
    reward: { stars: 3, message: "Ты умеешь писать тесты! ✅" }
  },
  {
    title: "Документирование кода",
    subject: "Программирование",
    icon: "BookOpen",
    color: "text-amber-500",
    tasks: [
      { type: 'fill', question: 'Docstring — строка ___ функции.', correctAnswer: 'документации', hint: 'Описание' },
      { type: 'quiz', question: 'Комментарии в Python начинаются с:', options: ['#', '//', '--', '/*'], correctAnswer: '#', hint: 'Решётка' },
      { type: 'fill', question: 'README.md — описание ___ .', correctAnswer: 'проекта', hint: 'Главная страница' },
      { type: 'quiz', question: 'Type hints — это:', options: ['Указание типов', 'Комментарии', 'Переменные', 'Функции'], correctAnswer: 'Указание типов', hint: 'Аннотации' },
      { type: 'fill', question: 'Документация помогает ___ код.', correctAnswer: 'понимать', hint: 'Читаемость' }
    ],
    reward: { stars: 3, message: "Ты документируешь код! 📖" }
  },
  {
    title: "Обработка ошибок",
    subject: "Программирование",
    icon: "AlertTriangle",
    color: "text-yellow-500",
    tasks: [
      { type: 'fill', question: 'try-except — обработка ___ .', correctAnswer: 'исключений', hint: 'Ошибки' },
      { type: 'quiz', question: 'finally выполняется:', options: ['Всегда', 'Только при ошибке', 'Только при успехе', 'Никогда'], correctAnswer: 'Всегда', hint: 'В конце' },
      { type: 'fill', question: 'raise — ___ исключение.', correctAnswer: 'генерирует', hint: 'Создание ошибки' },
      { type: 'quiz', question: 'with автоматически управляет:', options: ['Ресурсами', 'Переменными', 'Функциями', 'Классами'], correctAnswer: 'Ресурсами', hint: 'Контекстный менеджер' },
      { type: 'fill', question: 'Собственные исключения наследуют от ___ .', correctAnswer: 'Exception', hint: 'Базовый класс' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать ошибки! ⚠️" }
  },
  {
    title: "Git: контроль версий",
    subject: "Программирование",
    icon: "GitBranch",
    color: "text-orange-600",
    tasks: [
      { type: 'fill', question: 'Git — система контроля ___ .', correctAnswer: 'версий', hint: 'История изменений' },
      { type: 'quiz', question: 'git init создаёт:', options: ['Репозиторий', 'Файл', 'Ветку', 'Коммит'], correctAnswer: 'Репозиторий', hint: 'Новый проект' },
      { type: 'fill', question: 'git ___ добавляет файлы.', correctAnswer: 'add', hint: 'В индекс' },
      { type: 'quiz', question: 'git commit:', options: ['Фиксирует изменения', 'Добавляет файлы', 'Удаляет файлы', 'Отправляет на сервер'], correctAnswer: 'Фиксирует изменения', hint: 'Сохранение' },
      { type: 'fill', question: 'git log показывает ___ коммитов.', correctAnswer: 'историю', hint: 'Список' }
    ],
    reward: { stars: 3, message: "Ты знаешь Git! 🔀" }
  },
  {
    title: "Ветвление и слияние",
    subject: "Программирование",
    icon: "GitMerge",
    color: "text-purple-500",
    tasks: [
      { type: 'fill', question: 'Ветка — независимая линия ___ .', correctAnswer: 'разработки', hint: 'Branch' },
      { type: 'quiz', question: 'git branch показывает:', options: ['Список веток', 'Историю', 'Файлы', 'Изменения'], correctAnswer: 'Список веток', hint: 'Все ветки' },
      { type: 'fill', question: 'git ___ сливает ветки.', correctAnswer: 'merge', hint: 'Объединение' },
      { type: 'quiz', question: 'Конфликты возникают при:', options: ['Несовместимых изменениях', 'Создании ветки', 'Удалении ветки', 'Переключении ветки'], correctAnswer: 'Несовместимых изменениях', hint: 'Одни и те же строки' },
      { type: 'fill', question: 'git checkout -b создаёт и ___ ветку.', correctAnswer: 'переключает', hint: 'На новую ветку' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с ветками! 🌿" }
  },
  {
    title: "GitHub для совместной работы",
    subject: "Программирование",
    icon: "Github",
    color: "text-gray-500",
    tasks: [
      { type: 'fill', question: 'GitHub — платформа для ___ репозиториев.', correctAnswer: 'хостинга', hint: 'Облако' },
      { type: 'quiz', question: 'git push отправляет:', options: ['Изменения на сервер', 'Изменения с сервера', 'Файлы', 'Ветки'], correctAnswer: 'Изменения на сервер', hint: 'Загрузка' },
      { type: 'fill', question: 'git ___ получает изменения.', correctAnswer: 'pull', hint: 'С сервера' },
      { type: 'quiz', question: 'Pull request — это:', options: ['Предложение изменений', 'Запрос на скачивание', 'Удаление ветки', 'Создание репозитория'], correctAnswer: 'Предложение изменений', hint: 'PR' },
      { type: 'fill', question: 'Code review — ___ кода.', correctAnswer: 'проверка', hint: 'Другими разработчиками' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с GitHub! 🐙" }
  },
  {
    title: "Стиль кода и соглашения",
    subject: "Программирование",
    icon: "Ruler",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: 'PEP 8 — стиль кода ___ .', correctAnswer: 'Python', hint: 'Правила' },
      { type: 'quiz', question: 'Отступы в Python:', options: ['4 пробела', '2 пробела', '1 таб', '3 пробела'], correctAnswer: '4 пробела', hint: 'Стандарт' },
      { type: 'fill', question: 'Длина строки: до ___ символов.', correctAnswer: '79', hint: 'Ограничение' },
      { type: 'quiz', question: 'snake_case используется для:', options: ['Функций', 'Классов', 'Констант', 'Всех'], correctAnswer: 'Функций', hint: 'Нижние подчёркивания' },
      { type: 'fill', question: 'Линтеры проверяют ___ кода.', correctAnswer: 'стиль', hint: 'pylint, flake8' }
    ],
    reward: { stars: 3, message: "Ты пишешь чистый код! 📏" }
  },
  {
    title: "Выбор и планирование проекта",
    subject: "Программирование",
    icon: "ClipboardList",
    color: "text-indigo-500",
    tasks: [
      { type: 'fill', question: 'MVP — минимальный ___ продукт.', correctAnswer: 'жизнеспособный', hint: 'Minimum Viable Product' },
      { type: 'quiz', question: 'Декомпозиция — это:', options: ['Разбиение на подзадачи', 'Объединение задач', 'Удаление задач', 'Сортировка задач'], correctAnswer: 'Разбиение на подзадачи', hint: 'Деление' },
      { type: 'fill', question: 'Техническое ___ описывает требования.', correctAnswer: 'задание', hint: 'ТЗ' },
      { type: 'quiz', question: 'Критерий выбора проекта:', options: ['Интерес', 'Сложность', 'Время', 'Язык'], correctAnswer: 'Интерес', hint: 'Мотивация' },
      { type: 'fill', question: 'Приоритизация — расстановка ___ .', correctAnswer: 'приоритетов', hint: 'Важность' }
    ],
    reward: { stars: 3, message: "Ты умеешь планировать проекты! 📋" }
  },
  {
    title: "Реализация проекта",
    subject: "Программирование",
    icon: "Rocket",
    color: "text-red-400",
    tasks: [
      { type: 'fill', question: 'Итеративная разработка — маленькими ___ .', correctAnswer: 'шагами', hint: 'Постепенно' },
      { type: 'quiz', question: 'Рефакторинг — это:', options: ['Улучшение кода', 'Добавление функций', 'Удаление кода', 'Копирование кода'], correctAnswer: 'Улучшение кода', hint: 'Без изменения функциональности' },
      { type: 'fill', question: 'Регулярные ___ сохраняют прогресс.', correctAnswer: 'коммиты', hint: 'В Git' },
      { type: 'quiz', question: 'Тестирование после каждого изменения:', options: ['Повышает качество', 'Замедляет работу', 'Не нужно', 'Усложняет код'], correctAnswer: 'Повышает качество', hint: 'Проверка' },
      { type: 'fill', question: 'Документирование ведётся по ___ работы.', correctAnswer: 'ходу', hint: 'В процессе' }
    ],
    reward: { stars: 3, message: "Ты реализуешь проекты! 🚀" }
  },
  {
    title: "Презентация проекта",
    subject: "Программирование",
    icon: "Presentation",
    color: "text-cyan-500",
    tasks: [
      { type: 'fill', question: 'Структура презентации: проблема, решение, ___ .', correctAnswer: 'демонстрация', hint: 'Показ работы' },
      { type: 'quiz', question: 'Code review — это:', options: ['Проверка кода', 'Написание кода', 'Удаление кода', 'Тестирование'], correctAnswer: 'Проверка кода', hint: 'Другими людьми' },
      { type: 'fill', question: 'Обратная ___ помогает улучшить проект.', correctAnswer: 'связь', hint: 'Feedback' },
      { type: 'quiz', question: 'Демонстрация работы — это:', options: ['Показ проекта', 'Рассказ о планах', 'Чтение документации', 'Обсуждение кода'], correctAnswer: 'Показ проекта', hint: 'В действии' },
      { type: 'fill', question: 'Ответы на вопросы ___ .', correctAnswer: 'аудитории', hint: 'После презентации' }
    ],
    reward: { stars: 3, message: "Ты презентуешь проекты! 🎤" }
  },
  {
    title: "Анализ и развитие",
    subject: "Программирование",
    icon: "TrendingUp",
    color: "text-green-400",
    tasks: [
      { type: 'fill', question: 'Ретроспектива — анализ ___ проекта.', correctAnswer: 'результатов', hint: 'Что получилось' },
      { type: 'quiz', question: 'Портфолио проектов нужно для:', options: ['Карьеры', 'Учёбы', 'Хобби', 'Друзей'], correctAnswer: 'Карьеры', hint: 'Резюме' },
      { type: 'fill', question: 'Непрерывное ___ — ключ к успеху.', correctAnswer: 'обучение', hint: 'Развитие' },
      { type: 'quiz', question: 'Планирование развития включает:', options: ['Следующие шаги', 'Только прошлое', 'Только настоящее', 'Удаление проекта'], correctAnswer: 'Следующие шаги', hint: 'Будущее' },
      { type: 'fill', question: 'Анализ проблем помогает их ___ .', correctAnswer: 'решить', hint: 'В будущем' }
    ],
    reward: { stars: 3, message: "Ты анализируешь и развиваешься! 📈" }
  }
]

export { lessons, games }
