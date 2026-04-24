import { Subject, GameLesson } from '../../../types'

export const lessons: Subject = {
  title: 'Программирование',
  icon: 'Code',
  color: 'from-emerald-500 to-teal-500',
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
      topic: 'Алгоритмы и структуры данных',
      lessons: [
        {
          title: 'Сложность алгоритмов',
          description: `**Сложность алгоритма** — это функция, показывающая, как растёт время выполнения или память при увеличении входных данных.

**Основные обозначения:**
- **O(1)** — константная сложность, не зависит от размера данных
- **O(log n)** — логарифмическая сложность
- **O(n)** — линейная сложность
- **O(n log n)** — линейно-логарифмическая
- **O(n²)** — квадратичная сложность
- **O(2ⁿ)** — экспоненциальная сложность

**Примеры:**
- Доступ к элементу массива по индексу — O(1)
- Бинарный поиск — O(log n)
- Линейный поиск — O(n)
- Быстрая сортировка — O(n log n)
- Пузырьковая сортировка — O(n²)

**Зачем это нужно?**
Анализ сложности помогает выбрать оптимальный алгоритм для задачи и избежать проблем с производительностью на больших данных.`,
          tasks: ['Определить сложность алгоритма', 'Сравнить алгоритмы по эффективности', 'Выбрать оптимальный алгоритм для задачи'],
          examples: [
            'Доступ к элементу массива по индексу — O(1), бинарный поиск — O(log n)',
            'Пузырьковая сортировка имеет сложность O(n²), быстрая — O(n log n)',
            'Анализ сложности помогает выбрать оптимальный алгоритм для больших данных'
          ],
          keyPoints: [
            "Основные обозначения — O(1) — константная сложность, не зависит от размера данных",
            "O(1) — константная сложность, не зависит от размера данных",
            "O(log n) — логарифмическая сложность"
          ]
        },
        {
          title: 'Сортировка данных',
          description: `**Сортировка** — упорядочивание элементов по возрастанию или убыванию.

**Основные алгоритмы сортировки:**

**Пузырьковая сортировка (Bubble Sort)**
- Сложность: O(n²)
- Принцип: сравниваем соседние элементы и меняем местами, если они в неправильном порядке
- Простой, но медленный

**Сортировка выбором (Selection Sort)**
- Сложность: O(n²)
- Принцип: находим минимум и ставим в начало, затем повторяем для оставшейся части

**Быстрая сортировка (Quick Sort)**
- Сложность: O(n log n) в среднем
- Принцип: выбираем опорный элемент, делим массив на две части, рекурсивно сортируем

**Сортировка слиянием (Merge Sort)**
- Сложность: O(n log n)
- Принцип: делим массив пополам, сортируем каждую часть, сливаем

**Python:** \`sorted(list)\` или \`list.sort()\` используют Timsort — гибридный алгоритм.`,
          tasks: ['Реализовать алгоритм сортировки', 'Сравнить методы сортировки', 'Выбрать сортировку для конкретной задачи'],
          examples: [
            'Пузырьковая сортировка сравнивает соседние элементы — простая, но медленная O(n²)',
            'Быстрая сортировка выбирает опорный элемент и делит массив — O(n log n)',
            'Python sorted() использует Timsort — гибридный алгоритм сортировки'
          ],
          keyPoints: [
            "Основные алгоритмы сортировки — Пузырьковая сортировка (Bubble Sort)",
            "Python: \`sorted(list)\` или \`list.sort()\` используют Timsort — гибридный алгоритм.`,",
            "Ключевое понятие: Сортировка данных"
          ]
        },
        {
          title: 'Стек и очередь',
          description: `**Стек (Stack)** — структура данных LIFO (Last In, First Out)

**Операции:**
- **push(x)** — добавить элемент на вершину
- **pop()** — удалить и вернуть верхний элемент
- **peek()** — посмотреть верхний элемент без удаления
- **isEmpty()** — проверить, пуст ли стек

**Примеры использования:**
- История браузера (кнопка "Назад")
- Отмена действий (Ctrl+Z)
- Вызов функций в программе

---

**Очередь (Queue)** — структура данных FIFO (First In, First Out)

**Операции:**
- **enqueue(x)** — добавить элемент в конец
- **dequeue()** — удалить и вернуть элемент из начала
- **front()** — посмотреть первый элемент
- **isEmpty()** — проверить, пуста ли очередь

**Примеры использования:**
- Очередь печати документов
- Обработка запросов к серверу
- Очередь задач в операционной системе

**Python:**
\`\`\`python
# Стек через список
stack = []
stack.append(1)  # push
stack.pop()      # pop

# Очередь через collections.deque
from collections import deque
queue = deque()
queue.append(1)  # enqueue
queue.popleft()  # dequeue
\`\`\``,
          tasks: ['Реализовать стек', 'Реализовать очередь', 'Решить задачу с использованием стека'],
          examples: [
            'Стек работает по принципу LIFO: push() добавляет, pop() удаляет верхний элемент',
            'Очередь работает по FIFO: enqueue() в конец, dequeue() из начала',
            'Стек используется для отмены действий (Ctrl+Z), очередь — для печати документов'
          ],
          keyPoints: [
            "push(x) — добавить элемент на вершину",
            "pop() — удалить и вернуть верхний элемент",
            "peek() — посмотреть верхний элемент без удаления"
          ]
        },
        {
          title: 'Деревья и графы',
          description: `**Дерево** — иерархическая структура данных с корнем и узлами.

**Основные понятия:**
- **Корень** — верхний узел дерева
- **Узел (Node)** — элемент дерева
- **Лист** — узел без детей
- **Высота** — максимальная глубина дерева

**Бинарное дерево** — каждый узел имеет не более двух детей (левый и правый).

**Обходы дерева:**
- **Прямой (preorder)**: корень → лево → право
- **Симметричный (inorder)**: лево → корень → право
- **Обратный (postorder)**: лево → право → корень

---

**Граф** — набор вершин (узлов) и рёбер (связей).

**Виды графов:**
- Ориентированный / неориентированный
- Взвешенный / невзвешенный
- Связный / несвязный

**Алгоритмы обхода:**
- **BFS (поиск в ширину)** — уровень за уровнем
- **DFS (поиск в глубину)** — углубляемся максимально

**Применение:**
- Навигация и маршруты
- Социальные сети
- Зависимости между задачами`,
          tasks: ['Построить бинарное дерево', 'Реализовать обход графа', 'Решить задачу поиска пути'],
          examples: [
            'Бинарное дерево: каждый узел имеет не более двух детей (левый и правый)',
            'BFS обходит граф в ширину (уровень за уровнем), DFS — в глубину',
            'Деревья применяются в файловых системах, графы — в навигации и соцсетях'
          ],
          keyPoints: [
            "Основные понятия — Корень — верхний узел дерева",
            "Корень — верхний узел дерева",
            "Узел (Node) — элемент дерева"
          ]
        }
      ]
    },
    {
      topic: 'Объектно-ориентированное программирование',
      lessons: [
        {
          title: 'Классы и объекты',
          description: `**Класс** — это шаблон (чертёж) для создания объектов. Класс описывает:
- **Атрибуты** — свойства (данные)
- **Методы** — поведение (функции)

**Объект** — экземпляр класса с конкретными значениями атрибутов.

**Пример на Python:**
\`\`\`python
class Student:
    def __init__(self, name, age):
        self.name = name  # атрибут
        self.age = age    # атрибут
    
    def greet(self):      # метод
        print(f"Привет, я {self.name}!")

# Создание объектов
student1 = Student("Иван", 15)
student2 = Student("Мария", 16)

student1.greet()  # Привет, я Иван!
\`\`\`

**Ключевые понятия:**
- **__init__** — конструктор, вызывается при создании объекта
- **self** — ссылка на текущий объект
- **Атрибуты экземпляра** — уникальны для каждого объекта
- **Атрибуты класса** — общие для всех объектов`,
          tasks: ['Создать класс "Книга"', 'Создать экземпляры класса', 'Добавить методы в класс'],
          examples: [
            'class Student: создаёт шаблон, student1 = Student("Иван", 15) — экземпляр класса',
            '__init__ — конструктор, вызывается при создании объекта, self — ссылка на текущий объект',
            'Атрибуты — свойства объекта (self.name), методы — функции внутри класса'
          ],
          keyPoints: [
            "Атрибуты — свойства (данные)",
            "Методы — поведение (функции)",
            "Объект — экземпляр класса с конкретными значениями атрибутов."
          ]
        },
        {
          title: 'Инкапсуляция',
          description: `**Инкапсуляция** — скрытие внутренней реализации объекта от внешнего вмешательства.

**Уровни доступа в Python:**

**Публичные (public):**
\`\`\`python
self.name = "Иван"  # доступен откуда угодно
\`\`\`

**Защищённые (protected) — соглашение:**
\`\`\`python
self._age = 15  # не рекомендуется использовать извне
\`\`\`

**Приватные (private):**
\`\`\`python
self.__password = "secret"  # недоступен напрямую
\`\`\`

**Свойства (property):**
\`\`\`python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Баланс не может быть отрицательным")
\`\`\`

**Зачем нужна инкапсуляция?**
- Защита данных от некорректного изменения
- Контроль доступа к данным
- Возможность изменить реализацию без изменения интерфейса`,
          tasks: ['Создать приватные атрибуты', 'Реализовать свойства через @property', 'Добавить валидацию в setter'],
          examples: [
            'self._age — защищённый атрибут (соглашение), self.__password — приватный (недоступен напрямую)',
            '@property создаёт геттер, @balance.setter — сеттер с валидацией',
            'Инкапсуляция защищает данные от некорректного изменения'
          ],
          keyPoints: [
            "Уровни доступа в Python — Публичные (public):",
            "Защищённые (protected) — соглашение:",
            "Ключевое понятие: Инкапсуляция"
          ]
        },
        {
          title: 'Наследование',
          description: `**Наследование** — создание нового класса на основе существующего.

**Терминология:**
- **Родительский класс (базовый)** — класс, от которого наследуют
- **Дочерний класс (производный)** — класс, который наследует

**Пример:**
\`\`\`python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}: Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Мяу!"

dog = Dog("Бобик")
cat = Cat("Мурка")

print(dog.speak())  # Бобик: Гав!
print(cat.speak())  # Мурка: Мяу!
\`\`\`

**super()** — вызов метода родительского класса:
\`\`\`python
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # вызов __init__ родителя
        self.grade = grade
\`\`\`

**Переопределение методов** — изменение поведения унаследованного метода.`,
          tasks: ['Создать иерархию классов "Фигуры"', 'Переопределить метод', 'Использовать super()'],
          examples: [
            'class Dog(Animal): наследует атрибуты и методы родительского класса Animal',
            'super().__init__(name) вызывает конструктор родительского класса',
            'Переопределение метода — изменение поведения унаследованного метода в дочернем классе'
          ],
          keyPoints: [
            "Родительский класс (базовый) — класс, от которого наследуют",
            "Дочерний класс (производный) — класс, который наследует",
            "super() — вызов метода родительского класса:"
          ]
        },
        {
          title: 'Полиморфизм',
          description: `**Полиморфизм** — способность объектов разных классов реагировать на одинаковые методы по-разному.

**Пример полиморфизма:**
\`\`\`python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Полиморфизм: один метод — разное поведение
shapes = [Rectangle(5, 3), Circle(4), Rectangle(2, 6)]

for shape in shapes:
    print(f"Площадь: {shape.area()}")
\`\`\`

**Абстрактные классы:**
\`\`\`python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Еду по дороге")
\`\`\`

**Преимущества полиморфизма:**
- Единый интерфейс для разных типов
- Упрощение кода
- Лёгкое расширение функциональности`,
          tasks: ['Реализовать полиморфный метод', 'Создать абстрактный класс', 'Использовать полиморфизм на практике'],
          examples: [
            'Полиморфизм: shapes = [Rectangle(5,3), Circle(4)] — for s in shapes: s.area()',
            'Абстрактный класс (ABC) определяет интерфейс без реализации через @abstractmethod',
            'Полиморфизм позволяет работать с разными классами через единый интерфейс'
          ],
          keyPoints: [
            "Пример полиморфизма — \`\`\`python",
            "Абстрактные классы — \`\`\`python",
            "Преимущества полиморфизма — Единый интерфейс для разных типов"
          ]
        }
      ]
    },
    {
      topic: 'Работа с файлами и базами данных',
      lessons: [
        {
          title: 'Чтение и запись файлов',
          description: `**Файлы** позволяют хранить данные между запусками программы.

**Открытие файла:**
\`\`\`python
file = open("data.txt", "r")  # режим чтения
content = file.read()
file.close()
\`\`\`

**Режимы открытия:**
- **"r"** — чтение (файл должен существовать)
- **"w"** — запись (создаёт новый или перезаписывает)
- **"a"** — добавление в конец файла
- **"x"** — создание (ошибка, если файл существует)
- **"b"** — бинарный режим
- **"+"** — чтение и запись

**Контекстный менеджер (with):**
\`\`\`python
# Автоматически закрывает файл
with open("data.txt", "r") as file:
    content = file.read()
# Файл закрыт автоматически
\`\`\`

**Методы чтения:**
\`\`\`python
file.read()      # читать всё
file.readline()  # читать одну строку
file.readlines() # читать все строки в список
\`\`\`

**Запись в файл:**
\`\`\`python
with open("output.txt", "w") as file:
    file.write("Привет, мир!\\n")
    file.write("Вторая строка")
\`\`\``,
          tasks: ['Прочитать файл целиком', 'Прочитать файл построчно', 'Записать данные в файл'],
          examples: [
            'with open("data.txt", "r") as file: автоматически закрывает файл после использования',
            'Режимы: "r" — чтение, "w" — запись (перезаписывает), "a" — добавление в конец',
            'file.read() читает весь файл, file.readline() — одну строку, file.readlines() — все в список'
          ],
          keyPoints: [
            "Открытие файла — \`\`\`python",
            "Режимы открытия — \"r\" — чтение (файл должен существовать)",
            "\"r\" — чтение (файл должен существовать)"
          ]
        },
        {
          title: 'Работа с CSV и JSON',
          description: `**CSV (Comma-Separated Values)** — формат табличных данных.

**Работа с CSV:**
\`\`\`python
import csv

# Запись в CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Возраст", "Город"])
    writer.writerow(["Иван", 15, "Москва"])
    writer.writerow(["Мария", 16, "Санкт-Петербург"])

# Чтение из CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
\`\`\`

---

**JSON (JavaScript Object Notation)** — формат структурированных данных.

**Типы данных JSON:**
- Объекты (словари)
- Массивы (списки)
- Строки
- Числа
- true/false
- null

**Работа с JSON:**
\`\`\`python
import json

data = {
    "name": "Иван",
    "age": 15,
    "hobbies": ["чтение", "спорт"]
}

# Сериализация в строку
json_string = json.dumps(data, ensure_ascii=False, indent=2)

# Запись в файл
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# Чтение из файла
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
\`\`\``,
          tasks: ['Сохранить список словарей в JSON', 'Прочитать CSV в список словарей', 'Преобразовать CSV в JSON'],
          examples: [
            'CSV: csv.writer(file).writerow(["Имя", "Возраст"]) — запись строки в таблицу',
            'JSON: json.dumps(data, ensure_ascii=False) — сериализация Python-объекта в строку',
            'json.load(file) — десериализация JSON-файла обратно в Python-объект'
          ],
          keyPoints: [
            "Работа с CSV — \`\`\`python",
            "JSON (JavaScript Object Notation) — формат структурированных данных.",
            "Типы данных JSON — Объекты (словари)"
          ]
        },
        {
          title: 'Основы SQL',
          description: `**SQL (Structured Query Language)** — язык запросов к реляционным базам данных.

**Основные команды:**

**SELECT — выборка данных:**
\`\`\`sql
SELECT * FROM students;
SELECT name, age FROM students WHERE age > 15;
SELECT * FROM students ORDER BY name;
\`\`\`

**INSERT — добавление данных:**
\`\`\`sql
INSERT INTO students (name, age, city)
VALUES ('Иван', 15, 'Москва');
\`\`\`

**UPDATE — обновление данных:**
\`\`\`sql
UPDATE students SET age = 16 WHERE name = 'Иван';
\`\`\`

**DELETE — удаление данных:**
\`\`\`sql
DELETE FROM students WHERE age < 10;
\`\`\`

**Условия WHERE:**
\`\`\`sql
WHERE age = 15          -- равно
WHERE age > 15          -- больше
WHERE age >= 15         -- больше или равно
WHERE name LIKE 'И%'    -- начинается с "И"
WHERE city IN ('Москва', 'СПб')  -- в списке
WHERE age BETWEEN 14 AND 16      -- в диапазоне
\`\`\`

**Агрегатные функции:**
\`\`\`sql
SELECT COUNT(*) FROM students;        -- количество
SELECT AVG(age) FROM students;        -- среднее
SELECT MAX(age), MIN(age) FROM students;  -- максимум и минимум
\`\`\``,
          tasks: ['Написать SELECT-запрос с условием', 'Добавить данные в таблицу', 'Обновить запись в таблице'],
          examples: [
            'SELECT name, age FROM students WHERE age > 15 — выборка с условием',
            'INSERT INTO students (name, age) VALUES ("Иван", 15) — добавление записи',
            'Агрегатные функции: COUNT(*), AVG(age), MAX(age), MIN(age) — анализ данных'
          ],
          keyPoints: [
            "Основные команды — SELECT — выборка данных:",
            "SELECT — выборка данных:",
            "INSERT — добавление данных:"
          ]
        },
        {
          title: 'SQLite в Python',
          description: `**SQLite** — встроенная база данных, не требует отдельного сервера. Данные хранятся в одном файле.

**Подключение к базе:**
\`\`\`python
import sqlite3

# Создание соединения (файл создастся автоматически)
conn = sqlite3.connect("school.db")

# Создание курсора
cursor = conn.cursor()
\`\`\`

**Создание таблицы:**
\`\`\`python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
''')
conn.commit()
\`\`\`

**Вставка данных:**
\`\`\`python
cursor.execute(
    "INSERT INTO students (name, age, city) VALUES (?, ?, ?)",
    ("Иван", 15, "Москва")
)
conn.commit()
\`\`\`

**Выборка данных:**
\`\`\`python
cursor.execute("SELECT * FROM students WHERE age > ?", (14,))
rows = cursor.fetchall()  # получить все строки

for row in rows:
    print(row)
\`\`\`

**Важно:**
- Всегда используйте параметризованные запросы (?\`) для защиты от SQL-инъекций
- Не забывайте \`conn.commit()\` для сохранения изменений
- Закрывайте соединение: \`conn.close()\``,
          tasks: ['Создать базу данных', 'Добавить записи в таблицу', 'Выполнить SELECT-запрос'],
          examples: [
            'sqlite3.connect("school.db") — подключение к базе (файл создаётся автоматически)',
            'cursor.execute("INSERT INTO students VALUES (?, ?)", ("Иван", 15)) — параметризованный запрос',
            'Всегда вызывайте conn.commit() для сохранения изменений и conn.close() для закрытия'
          ],
          keyPoints: [
            "Подключение к базе — \`\`\`python",
            "Создание таблицы — \`\`\`python",
            "Вставка данных — \`\`\`python"
          ]
        }
      ]
    },
    {
      topic: 'Веб-разработка',
      lessons: [
        {
          title: 'Основы HTML',
          description: `**HTML (HyperText Markup Language)** — язык разметки веб-страниц.

**Структура HTML-документа:**
\`\`\`html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Моя страница</title>
</head>
<body>
    <h1>Заголовок</h1>
    <p>Параграф текста</p>
</body>
</html>
\`\`\`

**Основные теги:**
- **<h1>...</h6>** — заголовки (h1 — самый большой)
- **<p>** — параграф текста
- **<a href="url">** — ссылка
- **<img src="путь" alt="описание">** — изображение
- **<ul>, <ol>, <li>** — списки
- **<div>** — блок-контейнер
- **<span>** — строчный контейнер

**Семантические теги HTML5:**
- **<header>** — шапка страницы
- **<nav>** — навигация
- **<main>** — основное содержимое
- **<article>** — статья
- **<section>** — секция
- **<footer>** — подвал

**Атрибуты:**
- **id** — уникальный идентификатор
- **class** — класс для стилизации
- **style** — встроенные стили`,
          tasks: ['Создать HTML-страницу', 'Добавить заголовки и абзацы', 'Создать список и таблицу'],
          examples: [
            '<h1> — самый крупный заголовок, <p> — параграф текста, <a href="url"> — ссылка',
            'Семантические теги HTML5: <header>, <nav>, <main>, <article>, <footer>',
            'Каждый HTML-документ начинается с <!DOCTYPE html> и имеет структуру <html>→<head>→<body>'
          ],
          keyPoints: [
            "Структура HTML-документа — \`\`\`html",
            "Основные теги — <p> — параграф текста",
            "<h1>...</h6> — заголовки (h1 — самый большой)"
          ]
        },
        {
          title: 'CSS для стилизации',
          description: `**CSS (Cascading Style Sheets)** — язык описания внешнего вида документа.

**Способы подключения:**
\`\`\`html
<!-- Внешний файл -->
<link rel="stylesheet" href="styles.css">

<!-- Внутри head -->
<style>
    body { background: white; }
</style>

<!-- Встроенный стиль -->
<p style="color: red;">Текст</p>
\`\`\`

**Селекторы:**
\`\`\`css
/* По тегу */
p { color: blue; }

/* По классу */
.highlight { background: yellow; }

/* По id */
#header { font-size: 24px; }

/* Комбинированные */
div.highlight p { color: green; }
\`\`\`

**Box Model (модель коробки):**
\`\`\`css
.box {
    width: 200px;           /* ширина содержимого */
    padding: 20px;          /* внутренний отступ */
    border: 1px solid gray; /* граница */
    margin: 10px;           /* внешний отступ */
}
\`\`\`

**Flexbox для вёрстки:**
\`\`\`css
.container {
    display: flex;
    justify-content: center;  /* по горизонтали */
    align-items: center;      /* по вертикали */
    gap: 10px;               /* отступ между элементами */
}
\`\`\``,
          tasks: ['Добавить стили к странице', 'Использовать Flexbox', 'Создать адаптивную вёрстку'],
          examples: [
            'Селекторы: p { color: blue; } — по тегу, .class {} — по классу, #id {} — по идентификатору',
            'Box Model: width + padding + border + margin определяют размер элемента',
            'Flexbox: display: flex; justify-content: center; align-items: center; — центрирование'
          ],
          keyPoints: [
            "Способы подключения — \`\`\`html",
            "<!- — Внешний файл -->",
            "Box Model (модель коробки) — \`\`\`css"
          ]
        },
        {
          title: 'Flask: создание веб-приложения',
          description: `**Flask** — микрофреймворк для создания веб-приложений на Python.

**Установка:**
\`\`\`bash
pip install flask
\`\`\`

**Простейшее приложение:**
\`\`\`python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Привет, мир!</h1>"

@app.route("/about")
def about():
    return "<h1>О нас</h1>"

if __name__ == "__main__":
    app.run(debug=True)
\`\`\`

**Роутинг (маршрутизация):**
\`\`\`python
@app.route("/user/<name>")
def user(name):
    return f"Привет, {name}!"

@app.route("/post/<int:id>")
def post(id):
    return f"Пост номер {id}"
\`\`\`

**Шаблоны (templates):**
\`\`\`python
from flask import render_template

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)
\`\`\`

**Запуск:**
\`\`\`bash
python app.py
# Сервер запустится на http://127.0.0.1:5000
\`\`\``,
          tasks: ['Создать Flask-приложение', 'Добавить маршруты', 'Использовать шаблоны'],
          examples: [
            '@app.route("/") связывает URL с функцией — декоратор маршрутизации во Flask',
            'render_template("page.html", name="Иван") — рендеринг HTML-шаблона с переменными',
            'app.run(debug=True) запускает сервер на http://127.0.0.1:5000'
          ],
          keyPoints: [
            "Простейшее приложение — \`\`\`python",
            "Роутинг (маршрутизация) — \`\`\`python",
            "Ключевое понятие: Flask: создание веб-приложения"
          ]
        },
        {
          title: 'Формы и обработка данных',
          description: `**HTML-формы** позволяют пользователям вводить и отправлять данные.

**Создание формы:**
\`\`\`html
<form action="/submit" method="POST">
    <label>Имя:</label>
    <input type="text" name="username" required>
    
    <label>Email:</label>
    <input type="email" name="email">
    
    <label>Сообщение:</label>
    <textarea name="message"></textarea>
    
    <button type="submit">Отправить</button>
</form>
\`\`\`

**Типы input:**
- **text** — текстовое поле
- **password** — поле пароля
- **email** — email с валидацией
- **number** — число
- **checkbox** — флажок
- **radio** — переключатель
- **file** — загрузка файла

**Обработка в Flask:**
\`\`\`python
from flask import request

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Валидация
    if not username:
        return "Введите имя!"
    
    return f"Спасибо, {username}!"
\`\`\`

**GET vs POST:**
- **GET** — для получения данных (параметры в URL)
- **POST** — для отправки данных (в теле запроса)`,
          tasks: ['Создать HTML-форму', 'Обработать отправку формы в Flask', 'Добавить валидацию'],
          examples: [
            '<form method="POST" action="/submit"> — форма отправляет данные на сервер',
            'request.form.get("username") — получение данных формы во Flask',
            'GET — запрос данных (параметры в URL), POST — отправка данных (в теле запроса)'
          ],
          keyPoints: [
            "Создание формы — \`\`\`html",
            "text — текстовое поле",
            "password — поле пароля"
          ]
        }
      ]
    },
    {
      topic: 'Графический интерфейс',
      lessons: [
        {
          title: 'Библиотека Tkinter',
          description: `**Tkinter** — стандартная библиотека Python для создания графического интерфейса (GUI).

**Простейшее окно:**
\`\`\`python
import tkinter as tk

root = tk.Tk()
root.title("Моё приложение")
root.geometry("400x300")

# Код виджетов здесь

root.mainloop()  # Запуск главного цикла
\`\`\`

**Основные виджеты:**
- **Label** — текстовая метка
- **Button** — кнопка
- **Entry** — поле ввода (одна строка)
- **Text** — многострочное текстовое поле
- **Checkbutton** — флажок
- **Radiobutton** — переключатель
- **Listbox** — список
- **Scale** — ползунок

**Пример с виджетами:**
\`\`\`python
# Метка
label = tk.Label(root, text="Привет!", font=("Arial", 14))
label.pack()

# Поле ввода
entry = tk.Entry(root, width=30)
entry.pack()

# Кнопка
def on_click():
    print("Клик!")

button = tk.Button(root, text="Нажать", command=on_click)
button.pack()
\`\`\``,
          tasks: ['Создать окно приложения', 'Добавить виджеты Label и Button', 'Создать поле ввода'],
          examples: [
            'root = tk.Tk() создаёт окно, root.title() — заголовок, root.mainloop() — запуск цикла',
            'Label — текстовая метка, Button — кнопка, Entry — поле ввода, Text — многострочное поле',
            'label.pack() размещает виджет в окне автоматически'
          ],
          keyPoints: [
            "Простейшее окно — \`\`\`python",
            "Основные виджеты — Label — текстовая метка",
            "Label — текстовая метка"
          ]
        },
        {
          title: 'Создание форм',
          description: `**Формы в Tkinter** — набор виджетов для ввода данных.

**Entry — поле ввода:**
\`\`\`python
entry = tk.Entry(root, width=30, show="*")  # show для паролей
entry.pack()

# Получить значение
text = entry.get()

# Установить значение
entry.insert(0, "Текст по умолчанию")

# Очистить
entry.delete(0, tk.END)
\`\`\`

**Text — многострочное поле:**
\`\`\`python
text = tk.Text(root, width=40, height=10)
text.pack()

# Получить весь текст
content = text.get("1.0", tk.END)

# Вставить текст
text.insert(tk.END, "Новая строка")
\`\`\`

**Checkbutton — флажок:**
\`\`\`python
var = tk.IntVar()
check = tk.Checkbutton(root, text="Согласен", variable=var)
check.pack()

if var.get() == 1:
    print("Флажок установлен")
\`\`\`

**Radiobutton — переключатель:**
\`\`\`python
choice = tk.StringVar(value="option1")

rb1 = tk.Radiobutton(root, text="Вариант 1", variable=choice, value="option1")
rb2 = tk.Radiobutton(root, text="Вариант 2", variable=choice, value="option2")

selected = choice.get()
\`\`\``,
          tasks: ['Создать форму регистрации', 'Обработать данные формы', 'Добавить валидацию'],
          examples: [
            'entry.get() получает текст из Entry, entry.insert(0, "текст") — устанавливает',
            'Checkbutton — флажок (var.get() == 1), Radiobutton — переключатель из нескольких вариантов',
            'Text widget: content = text.get("1.0", tk.END) — чтение всего многострочного текста'
          ],
          keyPoints: [
            "Entry — поле ввода:",
            "Text — многострочное поле:",
            "Ключевое понятие: Создание форм"
          ]
        },
        {
          title: 'Обработка событий',
          description: `**События** — действия пользователя: клик, нажатие клавиши, движение мыши.

**Обработка клика кнопки:**
\`\`\`python
def on_button_click():
    print("Кнопка нажата!")

button = tk.Button(root, text="Нажать", command=on_button_click)
\`\`\`

**Передача аргументов:**
\`\`\`python
def greet(name):
    print(f"Привет, {name}!")

button = tk.Button(root, text="Привет", 
                   command=lambda: greet("Иван"))
\`\`\`

**Привязка событий через bind:**
\`\`\`python
def on_key_press(event):
    print(f"Нажата клавиша: {event.char}")

entry.bind("<Key>", on_key_press)

def on_click(event):
    print(f"Клик на x={event.x}, y={event.y}")

label.bind("<Button-1>", on_click)  # Левая кнопка мыши
\`\`\`

**Основные события:**
- **<Button-1>** — левый клик мыши
- **<Button-3>** — правый клик мыши
- **<Key>** — нажатие клавиши
- **<Return>** — клавиша Enter
- **<FocusIn>** — получение фокуса
- **<FocusOut>** — потеря фокуса`,
          tasks: ['Привязать функцию к кнопке', 'Обработать нажатие клавиши', 'Создать обработчик клика мыши'],
          examples: [
            'command=lambda: greet("Иван") — передача аргументов в обработчик через lambda',
            'entry.bind("<Key>", on_key_press) — привязка события нажатия клавиши к функции',
            '<Button-1> — левый клик мыши, <Return> — Enter, <FocusIn> — получение фокуса'
          ],
          keyPoints: [
            "Обработка клика кнопки — \`\`\`python",
            "Передача аргументов — \`\`\`python",
            "Привязка событий через bind — \`\`\`python"
          ]
        },
        {
          title: 'Меню и диалоги',
          description: `**Меню** — важный элемент интерфейса для организации команд.

**Создание меню:**
\`\`\`python
menubar = tk.Menu(root)

# Меню "Файл"
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)
menubar.add_cascade(label="Файл", menu=file_menu)

# Меню "Правка"
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Отменить", command=undo)
edit_menu.add_command(label="Повторить", command=redo)
menubar.add_cascade(label="Правка", menu=edit_menu)

root.config(menu=menubar)
\`\`\`

**Диалоговые окна:**
\`\`\`python
from tkinter import messagebox, filedialog

# Информационное сообщение
messagebox.showinfo("Информация", "Операция выполнена!")

# Вопрос (Да/Нет)
result = messagebox.askyesno("Подтверждение", "Вы уверены?")
if result:
    print("Пользователь нажал Да")

# Выбор файла
filename = filedialog.askopenfilename(
    title="Открыть файл",
    filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
)

# Сохранение файла
save_as = filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("Текстовые файлы", "*.txt")]
)
\`\`\``,
          tasks: ['Создать меню с пунктами', 'Показать диалоговое окно', 'Реализовать открытие файла'],
          examples: [
            'tk.Menu(root) создаёт меню, add_cascade() добавляет пункт, add_command() — команду',
            'messagebox.showinfo("Инфо", "Готово!") — информационное диалоговое окно',
            'filedialog.askopenfilename() — диалог выбора файла для открытия'
          ],
          keyPoints: [
            "Создание меню — \`\`\`python",
            "Диалоговые окна — \`\`\`python",
            "Ключевое понятие: Меню и диалоги"
          ]
        }
      ]
    },
    {
      topic: 'Отладка и тестирование',
      lessons: [
        {
          title: 'Методы отладки',
          description: `**Отладка (Debugging)** — процесс поиска и исправления ошибок в программе.

**Print-отладка:**
\`\`\`python
def calculate(a, b):
    print(f"Входные данные: a={a}, b={b}")
    result = a * b + 10
    print(f"Результат: {result}")
    return result
\`\`\`

**Использование отладчика:**

**pdb — отладчик Python:**
\`\`\`python
import pdb

def buggy_function(x):
    pdb.set_trace()  # Точка останова
    result = x / 0   # Ошибка!
    return result
\`\`\`

**Команды pdb:**
- **n (next)** — выполнить следующую строку
- **s (step)** — войти в функцию
- **c (continue)** — продолжить выполнение
- **p переменная** — вывести значение
- **l (list)** — показать код
- **q (quit)** — выйти

**Точки останова в IDE:**
- VS Code: клик слева от номера строки (красная точка)
- PyCharm: клик в серой области слева

**Просмотр переменных:**
- В отладчике можно навести курсор на переменную
- Watch expressions — отслеживание выражений`,
          tasks: ['Использовать print-отладку', 'Поставить точку останова', 'Пошагово выполнить код'],
          examples: [
            'pdb.set_trace() — точка останова в коде, n — следующая строка, c — продолжить',
            'VS Code: клик слева от номера строки — красная точка (breakpoint)',
            'Print-отладка: print(f"Значение x={x}") — простой, но эффективный метод'
          ],
          keyPoints: [
            "Использование отладчика — pdb — отладчик Python:",
            "n (next) — выполнить следующую строку",
            "s (step) — войти в функцию"
          ]
        },
        {
          title: 'Unit-тестирование',
          description: `**Unit-тестирование** — проверка отдельных функций или методов.

**Модуль unittest:**
\`\`\`python
import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_add_strings(self):
        self.assertEqual(add("hello", " world"), "hello world")
    
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
\`\`\`

**Методы проверки:**
- **assertEqual(a, b)** — равенство
- **assertTrue(x)** — истина
- **assertFalse(x)** — ложь
- **assertRaises(Error)** — ожидается исключение
- **assertIn(a, b)** — a содержится в b

**Запуск тестов:**
\`\`\`bash
python -m unittest test_file.py
\`\`\``,
          tasks: ['Написать unit-тест для функции', 'Использовать assertEqual', 'Протестировать исключение'],
          examples: [
            'self.assertEqual(add(2, 3), 5) — проверка равенства двух значений',
            'self.assertRaises(ValueError) — проверка, что функция вызывает исключение',
            'python -m unittest test_file.py — запуск всех тестов из файла'
          ],
          keyPoints: [
            "Методы проверки — assertEqual(a, b) — равенство",
            "assertRaises(Error) — ожидается исключение",
            "assertIn(a, b) — a содержится в b"
          ]
        },
        {
          title: 'Документирование кода',
          description: `**Документация** делает код понятным для других и для себя в будущем.

**Docstring — документация функции:**
\`\`\`python
def calculate_area(width, height):
    """
    Вычисляет площадь прямоугольника.
    
    Args:
        width (float): Ширина прямоугольника
        height (float): Высота прямоугольника
    
    Returns:
        float: Площадь прямоугольника
    
    Raises:
        ValueError: Если ширина или высота отрицательные
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    if width < 0 or height < 0:
        raise ValueError("Размеры должны быть положительными")
    return width * height
\`\`\`

**Комментарии:**
\`\`\`python
# Однострочный комментарий

"""
Многострочный
комментарий
"""

# TODO: добавить обработку ошибок
# FIXME: исправить баг при пустом вводе
# NOTE: важное замечание
\`\`\`

**Type hints (аннотации типов):**
\`\`\`python
def greet(name: str) -> str:
    return f"Привет, {name}!"

def get_items() -> list[int]:
    return [1, 2, 3]
\`\`\`

**README.md:**
- Описание проекта
- Инструкция по установке
- Примеры использования
- Лицензия`,
          tasks: ['Добавить docstring к функции', 'Создать README.md', 'Добавить type hints'],
          examples: [
            'def f(x: int) -> str: — аннотация типов: принимает int, возвращает str',
            'Docstring: """Вычисляет площадь. Args: width (float). Returns: float."""',
            'README.md: описание проекта, установка, примеры использования, лицензия'
          ],
          keyPoints: [
            "Docstring — документация функции:",
            "Type hints (аннотации типов) — \`\`\`python",
            "Ключевое понятие: Документирование кода"
          ]
        },
        {
          title: 'Обработка ошибок',
          description: `**Исключения (Exceptions)** — ошибки, возникающие во время выполнения программы.

**Try-except:**
\`\`\`python
try:
    x = int(input("Введите число: "))
    result = 10 / x
    print(result)
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("Деление на ноль!")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
else:
    print("Всё прошло успешно!")
finally:
    print("Этот блок выполняется всегда")
\`\`\`

**Генерация исключений:**
\`\`\`python
def set_age(age):
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    return age
\`\`\`

**Создание своих исключений:**
\`\`\`python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

raise CustomError("Произошла кастомная ошибка")
\`\`\`

**Контекстные менеджеры:**
\`\`\`python
# with автоматически обрабатывает ресурсы
with open("file.txt") as f:
    content = f.read()
# Файл автоматически закрыт даже при ошибке
\`\`\``,
          tasks: ['Использовать try-except', 'Создать своё исключение', 'Написать контекстный менеджер'],
          examples: [
            'try-except-else-finally: else выполняется при успехе, finally — всегда',
            'raise ValueError("Сообщение") — генерация исключения с описанием',
            'class MyError(Exception): pass — создание собственного типа исключения'
          ],
          keyPoints: [
            "Генерация исключений — \`\`\`python",
            "Создание своих исключений — \`\`\`python",
            "Контекстные менеджеры — \`\`\`python"
          ]
        }
      ]
    },
    {
      topic: 'Командная разработка',
      lessons: [
        {
          title: 'Git: контроль версий',
          description: `**Git** — распределённая система контроля версий для отслеживания изменений в коде.

**Базовые команды:**
\`\`\`bash
# Создание репозитория
git init

# Клонирование существующего
git clone https://github.com/user/repo.git

# Проверка состояния
git status

# Добавление файлов
git add .              # все файлы
git add file.py        # конкретный файл

# Фиксация изменений
git commit -m "Описание изменений"

# История коммитов
git log
git log --oneline      # кратко

# Просмотр изменений
git diff               # незафиксированные
git diff HEAD~1        # с предыдущим коммитом
\`\`\`

**Игнорирование файлов (.gitignore):**
\`\`\`
__pycache__/
*.pyc
.env
venv/
node_modules/
.DS_Store
\`\`\`

**Просмотр истории:**
\`\`\`bash
git log --graph --oneline --all
\`\`\``,
          tasks: ['Создать репозиторий', 'Сделать коммит', 'Просмотреть историю'],
          examples: [
            'git init создаёт новый репозиторий, git clone — копирует существующий',
            'git add . + git commit -m "описание" — фиксация изменений',
            'git log --oneline — краткая история коммитов, git status — состояние'
          ],
          keyPoints: [
            "Базовые команды — \`\`\`bash",
            "Игнорирование файлов (.gitignore) — \`\`\`",
            "Просмотр истории — \`\`\`bash"
          ]
        },
        {
          title: 'Ветвление и слияние',
          description: `**Ветки (Branches)** — независимые линии разработки.

**Работа с ветками:**
\`\`\`bash
# Список веток
git branch

# Создание ветки
git branch feature-login

# Переключение на ветку
git checkout feature-login

# Создание и переключение одной командой
git checkout -b feature-payment

# Слияние ветки в текущую
git merge feature-login

# Удаление ветки
git branch -d feature-login
\`\`\`

**Стратегии ветвления:**
- **main/master** — стабильная версия
- **develop** — ветка разработки
- **feature/*** — новые функции
- **bugfix/*** — исправление багов
- **release/*** — подготовка к релизу

**Разрешение конфликтов:**
\`\`\`bash
# При конфликте Git помечает файл:
<<<<<<< HEAD
текущая версия
=======
версия из сливаемой ветки
>>>>>>> feature-branch

# Нужно вручную выбрать правильный вариант
# Затем:
git add resolved_file.py
git commit
\`\`\``,
          tasks: ['Создать ветку', 'Слить ветки', 'Разрешить конфликт'],
          examples: [
            'git checkout -b feature-login — создание и переключение на новую ветку',
            'git merge feature-login — слияние ветки в текущую, git branch -d — удаление',
            'Конфликт: <<<<<<< HEAD / ======= / >>>>>>> feature — выбрать нужный вариант'
          ],
          keyPoints: [
            "Работа с ветками — \`\`\`bash",
            "Стратегии ветвления — main/master — стабильная версия",
            "main/master — стабильная версия"
          ]
        },
        {
          title: 'GitHub для совместной работы',
          description: `**GitHub** — платформа для хостинга Git-репозиториев и совместной разработки.

**Работа с удалённым репозиторием:**
\`\`\`bash
# Добавление удалённого репозитория
git remote add origin https://github.com/user/repo.git

# Отправка изменений
git push -u origin main
git push

# Получение изменений
git pull origin main

# Клонирование
git clone https://github.com/user/repo.git
\`\`\`

**Pull Request (PR):**
1. Форк репозитория или создание ветки
2. Внесение изменений и коммиты
3. Создание Pull Request
4. Code Review — проверка кода
5. Обсуждение и исправления
6. Merge PR

**README.md для проекта:**
\`\`\`markdown
# Название проекта

## Описание
Краткое описание проекта.

## Установка
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Использование
\`\`\`python
python main.py
\`\`\`

## Лицензия
MIT
\`\`\``,
          tasks: ['Отправить изменения на GitHub', 'Создать Pull Request', 'Провести Code Review'],
          examples: [
            'git push origin main — отправка изменений, git pull origin main — получение',
            'Pull Request: форк → изменения → PR → Code Review → Merge',
            'README.md на GitHub: описание, установка, использование, лицензия проекта'
          ],
          keyPoints: [
            "Работа с удалённым репозиторием — \`\`\`bash",
            "Code Review — проверка кода",
            "README.md для проекта — \`\`\`markdown"
          ]
        },
        {
          title: 'Стиль кода и соглашения',
          description: `**PEP 8** — стиль кода Python.

**Основные правила:**

**Отступы:**
- 4 пробела на уровень
- Не использовать табы

**Длина строки:**
- Максимум 79 символов
- Длинные строки можно разбивать:
\`\`\`python
long_string = (
    "Очень длинная строка, "
    "разбитая на части"
)
\`\`\`

**Именование:**
\`\`\`python
# Переменные и функции: snake_case
user_name = "Иван"
def calculate_total():

# Классы: CamelCase (PascalCase)
class ShoppingCart:

# Константы: UPPER_SNAKE_CASE
MAX_SIZE = 100

# Приватные атрибуты: _leading_underscore
_internal_value = 42
\`\`\`

**Пробелы:**
\`\`\`python
# Правильно
x = 5
result = func(a, b)
if x == 5:

# Неправильно
x=5
result=func(a,b)
if x==5:
\`\`\`

**Линтеры:**
\`\`\`bash
pip install pylint flake8
pylint my_script.py
flake8 my_script.py
\`\`\``,
          tasks: ['Проверить код на PEP 8', 'Настроить линтер', 'Исправить нарушения стиля'],
          examples: [
            'PEP 8: 4 пробела на уровень, snake_case для переменных, CamelCase для классов',
            'pylint my_script.py — проверка стиля, flake8 — лёгкий линтер для Python',
            'Классы: ShoppingCart (CamelCase), функции: calculate_total() (snake_case)'
          ],
          keyPoints: [
            "Основные правила — Отступы:",
            "Длина строки — Максимум 79 символов",
            "Длинные строки можно разбивать — \`\`\`python"
          ]
        }
      ]
    },
    {
      topic: 'Проектная работа',
      lessons: [
        {
          title: 'Выбор и планирование проекта',
          description: `**Выбор темы проекта** — важный первый шаг.

**Критерии выбора:**
- **Интерес** — тема должна быть увлекательной
- **Посильность** — соответствует вашим навыкам
- **Польза** — решает реальную задачу
- **Масштаб** — выполним за отведённое время

**Этапы планирования:**

**1. Определение требований:**
- Что должна делать программа?
- Кто будет пользователем?
- Какие данные нужны?

**2. Техническое задание:**
\`\`\`
Проект: Приложение "Список задач"

Функции:
- Добавление задач
- Отметка выполненных
- Удаление задач
- Сохранение в файл

Технологии: Python, Tkinter, JSON
Срок: 4 недели
\`\`\`

**3. Декомпозиция:**
\`\`\`
Неделя 1: Интерфейс (Tkinter)
Неделя 2: Логика добавления/удаления
Неделя 3: Сохранение в файл
Неделя 4: Тестирование и доработка
\`\`\`

**MVP (Minimum Viable Product):**
Начните с минимальной работающей версии!`,
          tasks: ['Выбрать тему проекта', 'Составить техническое задание', 'Разбить на подзадачи'],
          examples: [
            'Техническое задание: функции программы, технологии, сроки выполнения',
            'MVP (Minimum Viable Product) — начните с минимальной работающей версии',
            'Декомпозиция: разбейте проект на недели — интерфейс → логика → сохранение → тестирование'
          ],
          keyPoints: [
            "Критерии выбора — Интерес — тема должна быть увлекательной",
            "Интерес — тема должна быть увлекательной",
            "Посильность — соответствует вашим навыкам"
          ]
        },
        {
          title: 'Реализация проекта',
          description: `**Итеративная разработка** — создание проекта небольшими шагами.

**Принципы:**

**1. Маленькие шаги:**
\`\`\`bash
git commit -m "Добавлено окно приложения"
git commit -m "Реализовано добавление задачи"
git commit -m "Добавлено сохранение в файл"
\`\`\`

**2. Регулярные коммиты:**
- Коммит после каждой завершённой функции
- Понятные сообщения коммитов
- Не коммитить неработающий код

**3. Тестирование:**
\`\`\`python
# Тестируйте каждую функцию сразу
def add_task(tasks, task):
    """Добавить задачу в список."""
    tasks.append({"text": task, "done": False})
    return tasks

# Тест
assert add_task([], "Купить хлеб") == [{"text": "Купить хлеб", "done": False}]
\`\`\`

**4. Документирование:**
\`\`\`python
def save_tasks(tasks, filename):
    """
    Сохраняет список задач в JSON-файл.
    
    Args:
        tasks: список задач
        filename: путь к файлу
    """
    with open(filename, 'w') as f:
        json.dump(tasks, f)
\`\`\`

**Рефакторинг:**
- Улучшение кода без изменения функциональности
- Выделение повторяющегося кода в функции
- Упрощение сложных участков`,
          tasks: ['Начать разработку по плану', 'Проводить тестирование', 'Документировать код'],
          examples: [
            'Итеративная разработка: маленькие шаги с регулярными коммитами после каждой функции',
            'assert add_task([], "Купить хлеб") == [{"text": "Купить хлеб", "done": False}]',
            'Рефакторинг — улучшение кода без изменения функциональности'
          ],
          keyPoints: [
            "Маленькие шаги — \`\`\`bash",
            "Регулярные коммиты — Коммит после каждой завершённой функции",
            "Ключевое понятие: Реализация проекта"
          ]
        },
        {
          title: 'Презентация проекта',
          description: `**Презентация** — представление результатов работы.

**Структура презентации:**

**1. Введение (1-2 минуты):**
- Кто вы?
- Какая проблема?
- Какое решение?

**2. Демонстрация (3-5 минут):**
- Запуск программы
- Основные функции
- Интересные особенности

**3. Техническая часть (2-3 минуты):**
- Выбранные технологии
- Архитектура проекта
- Сложности и их решения

**4. Заключение (1 минута):**
- Достигнутые результаты
- Возможные улучшения
- Выводы

**Подготовка:**

**Слайды:**
\`\`\`
1. Титульный слайд
2. Проблема и решение
3. Скриншоты программы
4. Технический стек
5. Демонстрация (live)
6. Результаты
7. Планы развития
8. Спасибо за внимание!
\`\`\`

**Советы:**
- Тренируйтесь выступать
- Готовьте запасные скриншоты
- Предусмотрите вопросы аудитории`,
          tasks: ['Подготовить презентацию', 'Провести демонстрацию', 'Ответить на вопросы'],
          examples: [
            'Структура: введение (1-2 мин) → демонстрация (3-5 мин) → техническая часть (2-3 мин)',
            'Готовьте запасные скриншоты на случай технических проблем при демонстрации',
            'Тренируйтесь выступать — ограничьте время, готовьте ответы на возможные вопросы'
          ],
          keyPoints: [
            "Структура презентации — Введение (1-2 минуты):",
            "Введение (1-2 минуты) — Кто вы",
            "Демонстрация (3-5 минут) — Запуск программы"
          ]
        },
        {
          title: 'Анализ и развитие',
          description: `**Ретроспектива** — анализ проделанной работы.

**Вопросы для анализа:**
- Что получилось хорошо?
- Что можно улучшить?
- Какие были сложности?
- Чему научились?

**Шаблон ретроспективы:**
\`\`\`
✅ Что получилось:
- Успешно реализован интерфейс
- Данные сохраняются корректно
- Код хорошо задокументирован

❌ Что не удалось:
- Не успел добавить напоминания
- Интерфейс можно улучшить
- Мало тестов

📚 Чему научился:
- Работать с Tkinter
- Использовать JSON для хранения
- Планировать разработку

💡 Что улучшить:
- Начинать с MVP
- Писать тесты параллельно
- Чаще делать коммиты
\`\`\`

**Развитие проекта:**
\`\`\`
Версия 1.1:
- Добавить напоминания
- Тёмная тема
- Экспорт в CSV

Версия 2.0:
- Синхронизация с облаком
- Мобильное приложение
- Совместный доступ
\`\`\`

**Портфолио:**
- Опубликуйте код на GitHub
- Напишите хорошую документацию
- Добавьте скриншоты в README`,
          tasks: ['Провести ретроспективу', 'Спланировать развитие', 'Подготовить портфолио'],
          examples: [
            'Ретроспектива: что получилось, что не удалось, чему научились, что улучшить',
            'Версии развития: v1.1 — новые функции, v2.0 — масштабные изменения',
            'Портфолио: опубликуйте код на GitHub с описанием и скриншотами в README'
          ],
          keyPoints: [
            "Вопросы для анализа — Что получилось хорошо",
            "Шаблон ретроспективы — \`\`\`",
            "✅ Что получилось — Успешно реализован интерфейс"
          ]
        }
      ]
    }
  ]
}

export const games = [
  {
    title: "Сложность алгоритмов",
    subject: "Программирование",
    icon: "Activity",
    color: "text-indigo-400",
    tasks: [
      { type: 'quiz', question: 'Какая сложность означает константное время?', options: ['O(1)', 'O(n)', 'O(n²)', 'O(log n)', 'Другой ответ'],
      keyPoints: [
        "Основные обозначения — O(1) — константная сложность, не зависит от размера данных",
        "O(1) — константная сложность, не зависит от размера данных",
        "O(log n) — логарифмическая сложность",
      ],
      examples: [
        "Пузырьковая сортировка сравнивает соседние элементы — простая, но медленная O(n²)",
        "Быстрая сортировка выбирает опорный элемент и делит массив — O(n log n)",
        "Python sorted() использует Timsort — гибридный алгоритм сортировки",
      ], correctAnswer: 'O(1)', hint: 'Не зависит от размера данных' },
      { type: 'quiz', question: 'Линейная сложность обозначается как O(___).', options: ["1", "n log n", "n", "2n", "n²"], correctAnswer: 'n', hint: 'Время растёт пропорционально данным' },
      { type: 'quiz', question: 'Какая сложность у пузырьковой сортировки?', options: ['O(n²)', 'O(n)', 'O(log n)', 'O(1)', 'Другой ответ'], correctAnswer: 'O(n²)', hint: 'Два вложенных цикла' },
      { type: 'quiz', question: 'Сложность O(log n) — ___ сложность.', options: ["константная", "линейная", "квадратичная", "экспоненциальная", "логарифмическая"], correctAnswer: 'логарифмическая', hint: 'Бинарный поиск' },
      { type: 'quiz', question: 'O(n log n) — сложность:', options: ['Быстрой сортировки', 'Пузырьковой', 'Линейного поиска', 'Константная', 'Другой ответ'], correctAnswer: 'Быстрой сортировки', hint: 'Эффективный алгоритм' }
    ],
    reward: { stars: 3, message: "Ты понимаешь сложность алгоритмов! 📊" }
  },
  {
    title: "Сортировка данных",
    subject: "Программирование",
    icon: "ArrowUpDown",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: 'Упорядочивание элементов — это ___ .', options: ["фильтрация", "поиск", "удаление", "копирование", "сортировка"],
      keyPoints: [
        "Основные алгоритмы сортировки — Пузырьковая сортировка (Bubble Sort)",
        "Python: \`sorted(list)\` или \`list.sort()\` используют Timsort — гибридный алгоритм.\`,",
        "Ключевое понятие: Сортировка данных",
      ],
      examples: [
        "Стек работает по принципу LIFO: push() добавляет, pop() удаляет верхний элемент",
        "Очередь работает по FIFO: enqueue() в конец, dequeue() из начала",
        "Стек используется для отмены действий (Ctrl+Z), очередь — для печати документов",
      ], correctAnswer: 'сортировка', hint: 'Расстановка по порядку' },
      { type: 'quiz', question: 'Какой алгоритм сортировки самый простой?', options: ['Пузырьковый', 'Быстрый', 'Слиянием', 'Пирамидальный', 'Другой ответ'], correctAnswer: 'Пузырьковый', hint: 'Но медленный O(n²)' },
      { type: 'quiz', question: 'Быстрая сортировка работает за O(n log ___).', options: ["log n", "n", "k", "n²", "1"], correctAnswer: 'n', hint: 'В среднем случае' },
      { type: 'quiz', question: 'Сортировка выбором:', options: ['Находит минимум и ставит в начало', 'Меняет соседние элементы', 'Делит массив пополам', 'Использует пирамиду', 'Другой ответ'], correctAnswer: 'Находит минимум и ставит в начало', hint: 'Постепенно заполняем начало' },
      { type: 'quiz', question: 'Сортировка слиянием — ___ алгоритм.', options: ["простой", "стабильный", "медленный", "неэффективный", "нестабильный"], correctAnswer: 'стабильный', hint: 'Сохраняет порядок равных' }
    ],
    reward: { stars: 3, message: "Ты понимаешь сортировку! 🔄" }
  },
  {
    title: "Стек и очередь",
    subject: "Программирование",
    icon: "Layers",
    color: "text-purple-400",
    tasks: [
      { type: 'quiz', question: 'LIFO расшифровывается как Last In, First ___ .', options: ["Over", "Off", "Out", "In", "On"],
      keyPoints: [
        "push(x) — добавить элемент на вершину",
        "pop() — удалить и вернуть верхний элемент",
        "peek() — посмотреть верхний элемент без удаления",
      ],
      examples: [
        "Бинарное дерево: каждый узел имеет не более двух детей (левый и правый)",
        "BFS обходит граф в ширину (уровень за уровнем), DFS — в глубину",
        "Деревья применяются в файловых системах, графы — в навигации и соцсетях",
      ], correctAnswer: 'Out', hint: 'Последний пришёл — первый вышел' },
      { type: 'quiz', question: 'Стек работает по принципу:', options: ['LIFO', 'FIFO', 'LILO', 'FILO', 'Другой ответ'], correctAnswer: 'LIFO', hint: 'Стек блюд' },
      { type: 'quiz', question: 'Операция добавления в стек — ___ .', options: ["insert", "add", "pull", "peek", "push"], correctAnswer: 'push', hint: 'Поместить наверх' },
      { type: 'quiz', question: 'Очередь работает по принципу:', options: ['FIFO', 'LIFO', 'LILO', 'FILO', 'Другой ответ'], correctAnswer: 'FIFO', hint: 'Очередь в магазине' },
      { type: 'quiz', question: 'Операция удаления из очереди — ___ .', options: ["remove", "dequeue", "delete", "push", "enqueue"], correctAnswer: 'dequeue', hint: 'Убрать из начала' }
    ],
    reward: { stars: 3, message: "Ты понимаешь стек и очередь! 📚" }
  },
  {
    title: "Деревья и графы",
    subject: "Программирование",
    icon: "GitBranch",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: 'Дерево — ___ структура с корнем и узлами.', options: ["сетевая", "табличная", "плоская", "линейная", "иерархическая"],
      keyPoints: [
        "Основные понятия — Корень — верхний узел дерева",
        "Корень — верхний узел дерева",
        "Узел (Node) — элемент дерева",
      ],
      examples: [
        "Иван",
        "__init__ — конструктор, вызывается при создании объекта, self — ссылка на текущий объект",
        "Атрибуты — свойства объекта (self.name), методы — функции внутри класса",
      ], correctAnswer: 'иерархическая', hint: 'Один корень, много ветвей' },
      { type: 'quiz', question: 'Бинарное дерево имеет не более:', options: ['Двух детей у узла', 'Одного ребёнка', 'Трёх детей', 'Любое количество', 'Другой ответ'], correctAnswer: 'Двух детей у узла', hint: 'Бинарное = двоичное' },
      { type: 'quiz', question: 'Граф — набор вершин и ___ .', options: ["корней", "листьев", "циклов", "узлов", "рёбер"], correctAnswer: 'рёбер', hint: 'Связи между вершинами' },
      { type: 'quiz', question: 'BFS — это поиск:', options: ['В ширину', 'В глубину', 'Бинарный', 'Линейный', 'Другой ответ'], correctAnswer: 'В ширину', hint: 'Breadth-First Search' },
      { type: 'quiz', question: 'DFS — поиск в ___ .', options: ["объём", "длину", "глубину", "площадь", "ширину"], correctAnswer: 'глубину', hint: 'Deep-First Search' }
    ],
    reward: { stars: 3, message: "Ты понимаешь деревья и графы! 🌳" }
  },
  {
    title: "Классы и объекты",
    subject: "Программирование",
    icon: "Box",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: 'Класс — это ___ для создания объектов.', options: ["функция", "тип", "метод", "объект", "шаблон"],
      keyPoints: [
        "Атрибуты — свойства (данные)",
        "Методы — поведение (функции)",
        "Объект — экземпляр класса с конкретными значениями атрибутов.",
      ],
      examples: [
        "self._age — защищённый атрибут (соглашение), self.__password — приватный (недоступен напрямую)",
        "@property создаёт геттер, @balance.setter — сеттер с валидацией",
        "Инкапсуляция защищает данные от некорректного изменения",
      ], correctAnswer: 'шаблон', hint: 'Чертёж' },
      { type: 'quiz', question: 'Объект — это:', options: ['Экземпляр класса', 'Шаблон класса', 'Метод класса', 'Атрибут класса', 'Другой ответ'], correctAnswer: 'Экземпляр класса', hint: 'Конкретный представитель' },
      { type: 'quiz', question: '___ в Python ссылается на текущий объект.', options: ["me", "instance", "current", "obj", "self"], correctAnswer: 'self', hint: 'Ключевое слово' },
      { type: 'quiz', question: 'Конструктор — это метод:', options: ['Для создания объекта', 'Для удаления объекта', 'Для копирования', 'Для сравнения', 'Другой ответ'], correctAnswer: 'Для создания объекта', hint: '__init__ в Python' },
      { type: 'quiz', question: 'Атрибуты — это ___ класса.', options: ["переменные", "функции", "свойства", "объекты", "методы"], correctAnswer: 'свойства', hint: 'Данные объекта' }
    ],
    reward: { stars: 3, message: "Ты понимаешь классы и объекты! 📦" }
  },
  {
    title: "Инкапсуляция",
    subject: "Программирование",
    icon: "Lock",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: 'Инкапсуляция — ___ внутренней реализации.', options: ["скрытие", "копирование", "открытие", "удаление", "изменение"],
      keyPoints: [
        "Уровни доступа в Python — Публичные (public):",
        "Защищённые (protected) — соглашение:",
        "Ключевое понятие: Инкапсуляция",
      ],
      examples: [
        "class Dog(Animal): наследует атрибуты и методы родительского класса Animal",
        "super().__init__(name) вызывает конструктор родительского класса",
        "Переопределение метода — изменение поведения унаследованного метода в дочернем классе",
      ], correctAnswer: 'скрытие', hint: 'Защита данных' },
      { type: 'quiz', question: 'Приватные атрибуты в Python начинаются с:', options: ['_', '__', '@', '#', 'Другой ответ'], correctAnswer: '_', hint: 'Одно или два подчёркивания' },
      { type: 'quiz', question: '___ контролируют доступ к атрибутам.', options: ["функции", "классы", "методы", "переменные", "свойства"], correctAnswer: 'свойства', hint: 'property в Python' },
      { type: 'quiz', question: 'Публичные атрибуты:', options: ['Доступны извне', 'Скрыты', 'Только для чтения', 'Удалены', 'Другой ответ'], correctAnswer: 'Доступны извне', hint: 'Без ограничений' },
      { type: 'quiz', question: 'Инкапсуляция защищает данные от ___ изменения.', options: ["правильного", "быстрого", "некорректного", "частого", "медленного"], correctAnswer: 'некорректного', hint: 'Безопасность' }
    ],
    reward: { stars: 3, message: "Ты понимаешь инкапсуляцию! 🔒" }
  },
  {
    title: "Наследование",
    subject: "Программирование",
    icon: "GitMerge",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: 'Наследование — создание нового класса на основе ___ .', options: ["существующего", "нового", "родительского", "пустого", "абстрактного"],
      keyPoints: [
        "Родительский класс (базовый) — класс, от которого наследуют",
        "Дочерний класс (производный) — класс, который наследует",
        "super() — вызов метода родительского класса:",
      ],
      examples: [
        "Полиморфизм: shapes = [Rectangle(5,3), Circle(4)] — for s in shapes: s.area()",
        "Абстрактный класс (ABC) определяет интерфейс без реализации через @abstractmethod",
        "Полиморфизм позволяет работать с разными классами через единый интерфейс",
      ], correctAnswer: 'существующего', hint: 'Базовый класс' },
      { type: 'quiz', question: 'Родительский класс также называют:', options: ['Базовым', 'Производным', 'Дочерним', 'Наследником', 'Другой ответ'], correctAnswer: 'Базовым', hint: 'Основа' },
      { type: 'quiz', question: '___ вызывает метод родительского класса.', options: ["this()", "parent()", "self()", "call()", "super()"], correctAnswer: 'super()', hint: 'Функция в Python' },
      { type: 'quiz', question: 'Переопределение методов — это:', options: ['Изменение поведения', 'Удаление метода', 'Добавление метода', 'Копирование метода', 'Другой ответ'], correctAnswer: 'Изменение поведения', hint: 'Новая реализация' },
      { type: 'quiz', question: 'Дочерний класс ___ родительский.', options: ["игнорирует", "заменяет", "перезаписывает", "удаляет", "расширяет"], correctAnswer: 'расширяет', hint: 'Добавляет функциональность' }
    ],
    reward: { stars: 3, message: "Ты понимаешь наследование! 🔀" }
  },
  {
    title: "Полиморфизм",
    subject: "Программирование",
    icon: "Copy",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: 'Полиморфизм — единый ___ для разных форм.', options: ["объект", "метод", "интерфейс", "класс", "атрибут"],
      keyPoints: [
        "Пример полиморфизма — \`\`\`python",
        "Абстрактные классы — \`\`\`python",
        "Преимущества полиморфизма — Единый интерфейс для разных типов",
      ],
      examples: [
        "data.txt",
        "r",
        "r",
        "w",
        "a",
        "file.read() читает весь файл, file.readline() — одну строку, file.readlines() — все в список",
      ], correctAnswer: 'интерфейс', hint: 'Один метод — разное поведение' },
      { type: 'quiz', question: 'Методы с одинаковым именем в разных классах:', options: ['Работают по-разному', 'Одинаково', 'Не работают', 'Дублируются', 'Другой ответ'], correctAnswer: 'Работают по-разному', hint: 'Суть полиморфизма' },
      { type: 'quiz', question: '___ классы определяют интерфейс без реализации.', options: ["Базовые", "Приватные", "Абстрактные", "Конкретные", "Дочерние"], correctAnswer: 'Абстрактные', hint: 'ABC в Python' },
      { type: 'quiz', question: 'Полиморфизм позволяет:', options: ['Работать с разными классами одинаково', 'Создавать классы', 'Удалять методы', 'Копировать объекты', 'Другой ответ'], correctAnswer: 'Работать с разными классами одинаково', hint: 'Гибкость кода' },
      { type: 'quiz', question: 'Полиморфизм ___ код.', options: ["перезаписывает", "удаляет", "усложняет", "игнорирует", "упрощает"], correctAnswer: 'упрощает', hint: 'Удобство' }
    ],
    reward: { stars: 3, message: "Ты понимаешь полиморфизм! 🎭" }
  },
  {
    title: "Чтение и запись файлов",
    subject: "Программирование",
    icon: "FileText",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: 'Файлы хранят данные между ___ программы.', options: ["методами", "запусками", "строками", "классами", "функциями"],
      keyPoints: [
        "Открытие файла — \`\`\`python",
        "r",
        "r",
      ],
      examples: [
        "Имя",
        "Возраст",
        "JSON: json.dumps(data, ensure_ascii=False) — сериализация Python-объекта в строку",
        "json.load(file) — десериализация JSON-файла обратно в Python-объект",
      ], correctAnswer: 'запусками', hint: 'Сохранение' },
      { type: 'quiz', question: 'Режим "r" означает:', options: ['Чтение', 'Запись', 'Добавление', 'Удаление', 'Другой ответ'], correctAnswer: 'Чтение', hint: 'Read' },
      { type: 'quiz', question: 'Режим "w" — ___ в файл.', options: ["чтение", "копирование", "удаление", "добавление", "запись"], correctAnswer: 'запись', hint: 'Write' },
      { type: 'quiz', question: 'with автоматически:', options: ['Закрывает файл', 'Открывает файл', 'Читает файл', 'Удаляет файл', 'Другой ответ'], correctAnswer: 'Закрывает файл', hint: 'Контекстный менеджер' },
      { type: 'quiz', question: '___ () читает весь файл.', options: ["write", "read", "open", "copy", "close"], correctAnswer: 'read', hint: 'Одним вызовом' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с файлами! 📄" }
  },
  {
    title: "Работа с CSV и JSON",
    subject: "Программирование",
    icon: "FileJson",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: 'CSV — формат ___ данных.', options: ["табличных", "графических", "архивных", "звуковых", "исполняемых"],
      keyPoints: [
        "Работа с CSV — \`\`\`python",
        "JSON (JavaScript Object Notation) — формат структурированных данных.",
        "Типы данных JSON — Объекты (словари)",
      ],
      examples: [
        "SELECT name, age FROM students WHERE age > 15 — выборка с условием",
        "Иван",
        "Агрегатные функции: COUNT(*), AVG(age), MAX(age), MIN(age) — анализ данных",
      ], correctAnswer: 'табличных', hint: 'Разделённые запятыми' },
      { type: 'quiz', question: 'JSON поддерживает:', options: ['Объекты и массивы', 'Только строки', 'Только числа', 'Только булевы', 'Другой ответ'], correctAnswer: 'Объекты и массивы', hint: 'Структурированные данные' },
      { type: 'quiz', question: 'json.___() преобразует объект в строку.', options: ["dumps", "parse", "write", "loads", "stringify"], correctAnswer: 'dumps', hint: 'Сериализация' },
      { type: 'quiz', question: 'json.loads() выполняет:', options: ['Десериализацию', 'Сериализацию', 'Удаление', 'Чтение файла', 'Другой ответ'], correctAnswer: 'Десериализацию', hint: 'Строка в объект' },
      { type: 'quiz', question: 'CSV расшифровывается как Comma-Separated ___ .', options: ["Versions", "Vectors", "Variables", "Values", "Volumes"], correctAnswer: 'Values', hint: 'Значения' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с CSV и JSON! 📋" }
  },
  {
    title: "Основы SQL",
    subject: "Программирование",
    icon: "Database",
    color: "text-blue-500",
    tasks: [
      { type: 'quiz', question: 'SQL — язык ___ к базам данных.', options: ["запросов", "разметки", "скриптов", "стилей", "программирования"],
      keyPoints: [
        "Основные команды — SELECT — выборка данных:",
        "SELECT — выборка данных:",
        "INSERT — добавление данных:",
      ],
      examples: [
        "school.db",
        "INSERT INTO students VALUES (?, ?)",
        "Иван",
        "Всегда вызывайте conn.commit() для сохранения изменений и conn.close() для закрытия",
      ], correctAnswer: 'запросов', hint: 'Structured Query Language' },
      { type: 'quiz', question: 'SELECT — это:', options: ['Выборка данных', 'Добавление данных', 'Удаление данных', 'Обновление данных', 'Другой ответ'], correctAnswer: 'Выборка данных', hint: 'Чтение из таблицы' },
      { type: 'quiz', question: 'INSERT ___ добавляет данные.', options: ["WHERE", "VALUES", "INTO", "SET", "FROM"], correctAnswer: 'INTO', hint: 'Вставить в таблицу' },
      { type: 'quiz', question: 'DELETE удаляет:', options: ['Данные', 'Таблицу', 'Базу', 'Столбец', 'Другой ответ'], correctAnswer: 'Данные', hint: 'С условием WHERE' },
      { type: 'quiz', question: 'WHERE — условие ___ .', options: ["фильтрации", "удаления", "объединения", "вставки", "сортировки"], correctAnswer: 'фильтрации', hint: 'Отбор записей' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы SQL! 💾" }
  },
  {
    title: "SQLite в Python",
    subject: "Программирование",
    icon: "HardDrive",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: 'SQLite — ___ база данных.', options: ["внешняя", "сетевая", "встроенная", "облачная", "распределённая"],
      keyPoints: [
        "Подключение к базе — \`\`\`python",
        "Создание таблицы — \`\`\`python",
        "Вставка данных — \`\`\`python",
      ],
      examples: [
        "url",
        "Семантические теги HTML5: <header>, <nav>, <main>, <article>, <footer>",
        "Каждый HTML-документ начинается с <!DOCTYPE html> и имеет структуру <html>→<head>→<body>",
      ], correctAnswer: 'встроенная', hint: 'Не требует сервера' },
      { type: 'quiz', question: 'Модуль для работы с SQLite:', options: ['sqlite3', 'sql', 'database', 'db', 'Другой ответ'], correctAnswer: 'sqlite3', hint: 'Стандартная библиотека' },
      { type: 'quiz', question: 'sqlite3.___() создаёт соединение.', options: ["connect", "init", "start", "open", "link"], correctAnswer: 'connect', hint: 'Подключение к БД' },
      { type: 'quiz', question: 'Курсор используется для:', options: ['Выполнения запросов', 'Создания БД', 'Закрытия БД', 'Резервного копирования', 'Другой ответ'], correctAnswer: 'Выполнения запросов', hint: 'cursor.execute()' },
      { type: 'quiz', question: 'fetchall() возвращает все ___ .', options: ["результаты", "строки", "ошибки", "столбцы", "таблицы"], correctAnswer: 'результаты', hint: 'Список записей' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с SQLite! 🗄️" }
  },
  {
    title: "Основы HTML",
    subject: "Программирование",
    icon: "Code",
    color: "text-orange-500",
    tasks: [
      { type: 'quiz', question: 'HTML — язык ___ веб-страниц.', options: ["запросов", "стилей", "программирования", "разметки", "данных"],
      keyPoints: [
        "HTML (HyperText Markup Language) — язык разметки веб-страниц",
        "Основные теги: <html>, <head>, <body>, <h1>-<h6>, <p>, <a>, <img>",
        "Теги обычно открываются <> и закрываются </>",
      ],
      examples: [
        "p { color: blue; } — синий цвет для всех параграфов 🎨",
        "#header { font-size: 24px; } — селектор по id",
        "margin — внешний отступ, padding — внутренний отступ",
      ], correctAnswer: 'разметки', hint: 'Структура страницы' },
      { type: 'quiz', question: 'Тег для заголовка:', options: ['<h1>', '<header>', '<heading>', '<title>', 'Другой ответ'], correctAnswer: '<h1>', hint: 'От h1 до h6' },
      { type: 'quiz', question: 'Тег <___> создаёт ссылку.', options: ["href", "link", "ref", "src", "a"], correctAnswer: 'a', hint: 'Anchor' },
      { type: 'quiz', question: 'Атрибут для адреса ссылки:', options: ['href', 'src', 'link', 'url', 'Другой ответ'], correctAnswer: 'href', hint: 'Hypertext Reference' },
      { type: 'quiz', question: '<img> — тег для ___ .', options: ["аудио", "текста", "ссылки", "таблицы", "изображения"], correctAnswer: 'изображения', hint: 'Picture' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы HTML! 🌐" }
  },
  {
    title: "CSS для стилизации",
    subject: "Программирование",
    icon: "Palette",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: 'CSS — ___ таблицы стилей.', options: ["качественные", "компактные", "календарные", "каскадные", "комбинированные"],
      keyPoints: [
        "Способы подключения — \`\`\`html",
        "<!- — Внешний файл -->",
        "Box Model (модель коробки) — \`\`\`css",
      ],
      examples: [
        "/",
        "page.html",
        "Иван",
        "app.run(debug=True) запускает сервер на http://127.0.0.1:5000",
      ], correctAnswer: 'каскадные', hint: 'Cascading Style Sheets' },
      { type: 'quiz', question: 'Селектор по классу:', options: ['.class', '#class', 'class', '@class', 'Другой ответ'], correctAnswer: '.class', hint: 'Точка перед именем' },
      { type: 'quiz', question: 'Box model: content, padding, border, ___ .', options: ["margin", "content", "padding", "height", "border"], correctAnswer: 'margin', hint: 'Внешний отступ' },
      { type: 'quiz', question: 'Flexbox используется для:', options: ['Вёрстки', 'Анимации', 'Форм', 'Базы данных', 'Другой ответ'], correctAnswer: 'Вёрстки', hint: 'Расположение элементов' },
      { type: 'quiz', question: 'Свойство color изменяет ___ текста.', options: ["цвет", "отступ", "выравнивание", "размер", "шрифт"], correctAnswer: 'цвет', hint: 'Оформление' }
    ],
    reward: { stars: 3, message: "Ты знаешь CSS! 🎨" }
  },
  {
    title: "Flask: создание веб-приложения",
    subject: "Программирование",
    icon: "Flame",
    color: "text-gray-400",
    tasks: [
      { type: 'quiz', question: 'Flask — ___ для веб-приложений.', options: ["микрофреймворк", "язык", "компилятор", "библиотека", "база данных"],
      keyPoints: [
        "Простейшее приложение — \`\`\`python",
        "Роутинг (маршрутизация) — \`\`\`python",
        "Ключевое понятие: Flask: создание веб-приложения",
      ],
      examples: [
        "POST",
        "/submit",
        "username",
        "GET — запрос данных (параметры в URL), POST — отправка данных (в теле запроса)",
      ], correctAnswer: 'микрофреймворк', hint: 'Лёгкий фреймворк' },
      { type: 'quiz', question: 'Декоратор для маршрута:', options: ['@app.route', '@route', '@url', '@path', 'Другой ответ'], correctAnswer: '@app.route', hint: 'Связывает URL с функцией' },
      { type: 'quiz', question: 'render___() возвращает HTML-шаблон.', options: ["template", "html", "page", "file", "view"], correctAnswer: 'template', hint: 'Рендеринг' },
      { type: 'quiz', question: 'app.run() запускает:', options: ['Сервер', 'Базу данных', 'Тесты', 'Компилятор', 'Другой ответ'], correctAnswer: 'Сервер', hint: 'Локальный сервер' },
      { type: 'quiz', question: 'request содержит ___ запроса.', options: ["данные", "функции", "методы", "ошибки", "переменные"], correctAnswer: 'данные', hint: 'Информация от клиента' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать веб-приложения! 🔥" }
  },
  {
    title: "Формы и обработка данных",
    subject: "Программирование",
    icon: "FileInput",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: 'HTML-формы ___ данные пользователя.', options: ["удаляют", "архивируют", "копируют", "перемещают", "собирают"],
      keyPoints: [
        "Создание формы — \`\`\`html",
        "text — текстовое поле",
        "password — поле пароля",
      ],
      examples: [
        "root = tk.Tk() создаёт окно, root.title() — заголовок, root.mainloop() — запуск цикла",
        "Label — текстовая метка, Button — кнопка, Entry — поле ввода, Text — многострочное поле",
        "label.pack() размещает виджет в окне автоматически",
      ], correctAnswer: 'собирают', hint: 'Ввод информации' },
      { type: 'quiz', question: 'Метод POST:', options: ['Отправляет данные', 'Запрашивает данные', 'Удаляет данные', 'Обновляет данные', 'Другой ответ'], correctAnswer: 'Отправляет данные', hint: 'Передача на сервер' },
      { type: 'quiz', question: '<input> — поле для ___ .', options: ["ввода", "вывода", "отображения", "редактирования", "хранения"], correctAnswer: 'ввода', hint: 'Текст, число, файл' },
      { type: 'quiz', question: 'Валидация — это:', options: ['Проверка корректности', 'Отправка данных', 'Сохранение данных', 'Удаление данных', 'Другой ответ'], correctAnswer: 'Проверка корректности', hint: 'Правильность данных' },
      { type: 'quiz', question: 'request.___ содержит данные формы.', options: ["body", "input", "value", "data", "form"], correctAnswer: 'form', hint: 'В Flask' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с формами! 📝" }
  },
  {
    title: "Библиотека Tkinter",
    subject: "Программирование",
    icon: "Layout",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: 'Tkinter — библиотека для ___ интерфейса.', options: ["сетевого", "файлового", "графического", "командного", "текстового"],
      keyPoints: [
        "Простейшее окно — \`\`\`python",
        "Основные виджеты — Label — текстовая метка",
        "Label — текстовая метка",
      ],
      examples: [
        "текст",
        "Checkbutton — флажок (var.get() == 1), Radiobutton — переключатель из нескольких вариантов",
        "1.0",
      ], correctAnswer: 'графического', hint: 'GUI' },
      { type: 'quiz', question: 'Виджет Button — это:', options: ['Кнопка', 'Поле ввода', 'Метка', 'Список', 'Другой ответ'], correctAnswer: 'Кнопка', hint: 'Нажимается' },
      { type: 'quiz', question: 'root.___() запускает главный цикл.', options: ["run", "mainloop", "init", "start", "begin"], correctAnswer: 'mainloop', hint: 'Обработка событий' },
      { type: 'quiz', question: 'Менеджер компоновки pack:', options: ['Упаковывает виджеты', 'Удаляет виджеты', 'Создаёт виджеты', 'Красит виджеты', 'Другой ответ'], correctAnswer: 'Упаковывает виджеты', hint: 'Размещение' },
      { type: 'quiz', question: 'Entry — виджет для ___ данных.', options: ["проверки", "ввода", "вывода", "обработки", "отображения"], correctAnswer: 'ввода', hint: 'Одна строка' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с Tkinter! 🖼️" }
  },
  {
    title: "Создание форм",
    subject: "Программирование",
    icon: "TextBox",
    color: "text-blue-300",
    tasks: [
      { type: 'quiz', question: 'Entry — поле для ___ строки.', options: ["нескольких", "двух", "длинной", "одной", "многострочной"],
      keyPoints: [
        "Entry — поле ввода:",
        "Text — многострочное поле:",
        "Ключевое понятие: Создание форм",
      ],
      examples: [
        "Иван",
        "<Key>",
        "<Button-1> — левый клик мыши, <Return> — Enter, <FocusIn> — получение фокуса",
      ], correctAnswer: 'одной', hint: 'Однострочное' },
      { type: 'quiz', question: 'Text — это:', options: ['Многострочное поле', 'Метка', 'Кнопка', 'Список', 'Другой ответ'], correctAnswer: 'Многострочное поле', hint: 'Несколько строк' },
      { type: 'quiz', question: 'get() ___ данные из виджета.', options: ["получает", "устанавливает", "удаляет", "перемещает", "проверяет"], correctAnswer: 'получает', hint: 'Извлечение' },
      { type: 'quiz', question: 'Checkbutton — это:', options: ['Флажок', 'Переключатель', 'Кнопка', 'Поле', 'Другой ответ'], correctAnswer: 'Флажок', hint: 'Галочка' },
      { type: 'quiz', question: 'Radiobutton — ___ переключатель.', options: ["флажок", "список", "радиокнопка", "кнопка", "меню"], correctAnswer: 'радиокнопка', hint: 'Один из нескольких' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать формы! 📝" }
  },
  {
    title: "Обработка событий",
    subject: "Программирование",
    icon: "MousePointerClick",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: 'command привязывает ___ к кнопке.', options: ["массив", "объект", "функцию", "строку", "переменную"],
      keyPoints: [
        "Обработка клика кнопки — \`\`\`python",
        "Передача аргументов — \`\`\`python",
        "Привязка событий через bind — \`\`\`python",
      ],
      examples: [
        "tk.Menu(root) создаёт меню, add_cascade() добавляет пункт, add_command() — команду",
        "Инфо",
        "Готово!",
        "filedialog.askopenfilename() — диалог выбора файла для открытия",
      ], correctAnswer: 'функцию', hint: 'Обработчик' },
      { type: 'quiz', question: 'bind() привязывает:', options: ['Событие к виджету', 'Виджет к окну', 'Функцию к переменной', 'Файл к программе', 'Другой ответ'], correctAnswer: 'Событие к виджету', hint: 'Реакция' },
      { type: 'quiz', question: '<Button-1> — ___ клик мыши.', options: ["левый", "двойной", "тройной", "правый", "средний"], correctAnswer: 'левый', hint: 'Основная кнопка' },
      { type: 'quiz', question: '<Key> — событие:', options: ['Нажатие клавиши', 'Клик мыши', 'Движение мыши', 'Закрытие окна', 'Другой ответ'], correctAnswer: 'Нажатие клавиши', hint: 'Клавиатура' },
      { type: 'quiz', question: 'lambda позволяет передавать ___ .', options: ["аргументы", "массивы", "переменные", "объекты", "функции"], correctAnswer: 'аргументы', hint: 'Параметры' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать события! 🖱️" }
  },
  {
    title: "Меню и диалоги",
    subject: "Программирование",
    icon: "Menu",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: 'Menu — виджет для создания ___ .', options: ["меню", "диалогов", "окон", "кнопок", "полей"],
      keyPoints: [
        "Создание меню — \`\`\`python",
        "Диалоговые окна — \`\`\`python",
        "Ключевое понятие: Меню и диалоги",
      ],
      examples: [
        "pdb.set_trace() — точка останова в коде, n — следующая строка, c — продолжить",
        "VS Code: клик слева от номера строки — красная точка (breakpoint)",
        "Значение x={x}",
      ], correctAnswer: 'меню', hint: 'Пункты' },
      { type: 'quiz', question: 'add_cascade создаёт:', options: ['Вложенное меню', 'Пункт меню', 'Разделитель', 'Кнопку', 'Другой ответ'], correctAnswer: 'Вложенное меню', hint: 'Подменю' },
      { type: 'quiz', question: 'messagebox показывает ___ окна.', options: ["поплавковые", "вспомогательные", "главные", "диалоговые", "модальные"], correctAnswer: 'диалоговые', hint: 'Сообщения' },
      { type: 'quiz', question: 'askopenfilename открывает:', options: ['Диалог выбора файла', 'Файл для чтения', 'Новое окно', 'Сохранение', 'Другой ответ'], correctAnswer: 'Диалог выбора файла', hint: 'Выбор' },
      { type: 'quiz', question: 'showinfo показывает ___ сообщение.', options: ["ошибку", "информационное", "уведомление", "вопрос", "предупреждение"], correctAnswer: 'информационное', hint: 'Информация' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать меню и диалоги! 📋" }
  },
  {
    title: "Методы отладки",
    subject: "Программирование",
    icon: "Bug",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: 'Print-отладка — вывод значений в ___ .', options: ["буфер", "консоль", "базу", "файл", "окно"],
      keyPoints: [
        "Использование отладчика — pdb — отладчик Python:",
        "n (next) — выполнить следующую строку",
        "s (step) — войти в функцию",
      ],
      examples: [
        "self.assertEqual(add(2, 3), 5) — проверка равенства двух значений",
        "self.assertRaises(ValueError) — проверка, что функция вызывает исключение",
        "python -m unittest test_file.py — запуск всех тестов из файла",
      ], correctAnswer: 'консоль', hint: 'Терминал' },
      { type: 'quiz', question: 'Отладчик позволяет:', options: ['Пошагово выполнять код', 'Удалять код', 'Компилировать', 'Архивировать', 'Другой ответ'], correctAnswer: 'Пошагово выполнять код', hint: 'По шагам' },
      { type: 'quiz', question: 'Точка ___ останавливает выполнение.', options: ["останова", "входа", "выхода", "возврата", "перехода"], correctAnswer: 'останова', hint: 'Breakpoint' },
      { type: 'quiz', question: 'pdb — это:', options: ['Отладчик Python', 'Компилятор', 'Интерпретатор', 'Редактор', 'Другой ответ'], correctAnswer: 'Отладчик Python', hint: 'Debug' },
      { type: 'quiz', question: 'IDE — интегрированная среда ___ .', options: ["тестирования", "интерпретации", "отладки", "архивации", "разработки"], correctAnswer: 'разработки', hint: 'Development' }
    ],
    reward: { stars: 3, message: "Ты умеешь отлаживать код! 🐛" }
  },
  {
    title: "Unit-тестирование",
    subject: "Программирование",
    icon: "TestTube",
    color: "text-green-500",
    tasks: [
      { type: 'quiz', question: 'Unit-тест проверяет ___ функцию.', options: ["отдельную", "главную", "системную", "интеграционную", "все"],
      keyPoints: [
        "Методы проверки — assertEqual(a, b) — равенство",
        "assertRaises(Error) — ожидается исключение",
        "assertIn(a, b) — a содержится в b",
      ],
      examples: [
        "def f(x: int) -> str: — аннотация типов: принимает int, возвращает str",
        "",
        "Вычисляет площадь. Args: width (float). Returns: float.",
        "",
        "README.md: описание проекта, установка, примеры использования, лицензия",
      ], correctAnswer: 'отдельную', hint: 'Изолированно' },
      { type: 'quiz', question: 'unittest — это:', options: ['Встроенный фреймворк', 'Внешняя библиотека', 'Язык программирования', 'IDE', 'Другой ответ'], correctAnswer: 'Встроенный фреймворк', hint: 'Модуль Python' },
      { type: 'quiz', question: 'assertEqual проверяет ___ значений.', options: ["произведение", "сумму", "равенство", "больше", "различие"], correctAnswer: 'равенство', hint: 'Сравнение' },
      { type: 'quiz', question: 'setUp выполняется:', options: ['Перед каждым тестом', 'После каждого теста', 'Один раз в начале', 'В конце всех тестов', 'Другой ответ'], correctAnswer: 'Перед каждым тестом', hint: 'Подготовка' },
      { type: 'quiz', question: 'python -m unittest запускает ___ .', options: ["сервер", "скрипт", "программу", "компиляцию", "тесты"], correctAnswer: 'тесты', hint: 'Проверка' }
    ],
    reward: { stars: 3, message: "Ты умеешь писать тесты! 🧪" }
  },
  {
    title: "Документирование кода",
    subject: "Программирование",
    icon: "FileText",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: 'Docstring — ___ документации функции.', options: ["строка", "файл", "комментарий", "раздел", "блок"],
      keyPoints: [
        "Docstring — документация функции:",
        "Type hints (аннотации типов) — \`\`\`python",
        "Ключевое понятие: Документирование кода",
      ],
      examples: [
        "try-except-else-finally: else выполняется при успехе, finally — всегда",
        "Сообщение",
        "class MyError(Exception): pass — создание собственного типа исключения",
      ], correctAnswer: 'строка', hint: 'Описание' },
      { type: 'quiz', question: 'README.md — это:', options: ['Описание проекта', 'Код программы', 'Тесты', 'Конфигурация', 'Другой ответ'], correctAnswer: 'Описание проекта', hint: 'Документация' },
      { type: 'quiz', question: '# означает ___ комментарий.', options: ["документирующий", "блочный", "многострочный", "однострочный", "специальный"], correctAnswer: 'однострочный', hint: 'Короткий' },
      { type: 'quiz', question: 'Type hints — это:', options: ['Аннотации типов', 'Комментарии', 'Переменные', 'Функции', 'Другой ответ'], correctAnswer: 'Аннотации типов', hint: 'Указание типов' },
      { type: 'quiz', question: 'Документация помогает ___ код.', options: ["шифровать", "копировать", "удалять", "архивировать", "понимать"], correctAnswer: 'понимать', hint: 'Чтение' }
    ],
    reward: { stars: 3, message: "Ты умеешь документировать код! 📄" }
  },
  {
    title: "Обработка ошибок",
    subject: "Программирование",
    icon: "AlertTriangle",
    color: "text-yellow-500",
    tasks: [
      { type: 'quiz', question: 'try-except ___ исключения.', options: ["создаёт", "передаёт", "удаляет", "игнорирует", "обрабатывает"],
      keyPoints: [
        "Генерация исключений — \`\`\`python",
        "Создание своих исключений — \`\`\`python",
        "Контекстные менеджеры — \`\`\`python",
      ],
      examples: [
        "git init создаёт новый репозиторий, git clone — копирует существующий",
        "описание",
        "git log --oneline — краткая история коммитов, git status — состояние",
      ], correctAnswer: 'обрабатывает', hint: 'Ловит ошибки' },
      { type: 'quiz', question: 'finally выполняется:', options: ['Всегда', 'Только при ошибке', 'Только без ошибки', 'Никогда', 'Другой ответ'], correctAnswer: 'Всегда', hint: 'Гарантированно' },
      { type: 'quiz', question: 'raise ___ исключение.', options: ["игнорирует", "удаляет", "передаёт", "генерирует", "обрабатывает"], correctAnswer: 'генерирует', hint: 'Создаёт' },
      { type: 'quiz', question: 'Собственные исключения наследуются от:', options: ['Exception', 'Error', 'BaseException', 'object', 'Другой ответ'], correctAnswer: 'Exception', hint: 'Базовый класс' },
      { type: 'quiz', question: 'with автоматически ___ ресурсы.', options: ["блокирует", "удаляет", "копирует", "перемещает", "управляет"], correctAnswer: 'управляет', hint: 'Контекст' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать ошибки! ⚠️" }
  },
  {
    title: "Git: контроль версий",
    subject: "Программирование",
    icon: "GitBranch",
    color: "text-orange-500",
    tasks: [
      { type: 'quiz', question: 'git init ___ репозиторий.', options: ["создаёт", "копирует", "клонирует", "перемещает", "удаляет"],
      keyPoints: [
        "Базовые команды — \`\`\`bash",
        "Игнорирование файлов (.gitignore) — \`\`\`",
        "Просмотр истории — \`\`\`bash",
      ],
      examples: [
        "git checkout -b feature-login — создание и переключение на новую ветку",
        "git merge feature-login — слияние ветки в текущую, git branch -d — удаление",
        "Конфликт: <<<<<<< HEAD / ======= / >>>>>>> feature — выбрать нужный вариант",
      ], correctAnswer: 'создаёт', hint: 'Инициализация' },
      { type: 'quiz', question: 'git add:', options: ['Добавляет файлы', 'Коммитит', 'Отправляет', 'Клонирует', 'Другой ответ'], correctAnswer: 'Добавляет файлы', hint: 'Staging' },
      { type: 'quiz', question: 'git commit ___ изменения.', options: ["перемещает", "фиксирует", "удаляет", "отправляет", "копирует"], correctAnswer: 'фиксирует', hint: 'Сохраняет' },
      { type: 'quiz', question: 'git status показывает:', options: ['Состояние файлов', 'Историю', 'Различия', 'Ветки', 'Другой ответ'], correctAnswer: 'Состояние файлов', hint: 'Текущее' },
      { type: 'quiz', question: 'git log показывает ___ коммитов.', options: ["список", "граф", "историю", "диаграмму", "дерево"], correctAnswer: 'историю', hint: 'Прошлое' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы Git! 🔀" }
  },
  {
    title: "Ветвление и слияние",
    subject: "Программирование",
    icon: "GitMerge",
    color: "text-purple-500",
    tasks: [
      { type: 'quiz', question: 'Ветка — независимая ___ разработки.', options: ["ветвь", "часть", "модуль", "линия", "копия"],
      keyPoints: [
        "Работа с ветками — \`\`\`bash",
        "Стратегии ветвления — main/master — стабильная версия",
        "main/master — стабильная версия",
      ],
      examples: [
        "git push origin main — отправка изменений, git pull origin main — получение",
        "Pull Request: форк → изменения → PR → Code Review → Merge",
        "README.md на GitHub: описание, установка, использование, лицензия проекта",
      ], correctAnswer: 'линия', hint: 'Ветвь' },
      { type: 'quiz', question: 'git checkout -b:', options: ['Создаёт и переключает ветку', 'Удаляет ветку', 'Сливает ветки', 'Показывает ветки', 'Другой ответ'], correctAnswer: 'Создаёт и переключает ветку', hint: 'Новая ветка' },
      { type: 'quiz', question: 'git merge ___ ветки.', options: ["сливает", "переименовывает", "перемещает", "создаёт", "копирует"], correctAnswer: 'сливает', hint: 'Объединяет' },
      { type: 'quiz', question: 'Конфликт возникает при:', options: ['Несовместимых изменениях', 'Удалении ветки', 'Создании ветки', 'Переключении', 'Другой ответ'], correctAnswer: 'Несовместимых изменениях', hint: 'Проблема' },
      { type: 'quiz', question: 'git branch показывает список ___ .', options: ["изменений", "коммитов", "веток", "файлов", "авторов"], correctAnswer: 'веток', hint: 'Перечень' }
    ],
    reward: { stars: 3, message: "Ты понимаешь ветвление! 🌿" }
  },
  {
    title: "GitHub для совместной работы",
    subject: "Программирование",
    icon: "Github",
    color: "text-gray-500",
    tasks: [
      { type: 'quiz', question: 'GitHub — платформа для ___ репозиториев.', options: ["хостинга", "архивации", "шифрования", "создания", "копирования"],
      keyPoints: [
        "Работа с удалённым репозиторием — \`\`\`bash",
        "Code Review — проверка кода",
        "README.md для проекта — \`\`\`markdown",
      ],
      examples: [
        "PEP 8: 4 пробела на уровень, snake_case для переменных, CamelCase для классов",
        "pylint my_script.py — проверка стиля, flake8 — лёгкий линтер для Python",
        "Классы: ShoppingCart (CamelCase), функции: calculate_total() (snake_case)",
      ], correctAnswer: 'хостинга', hint: 'Хранение' },
      { type: 'quiz', question: 'git push:', options: ['Отправляет изменения', 'Получает изменения', 'Создаёт ветку', 'Сливает ветки', 'Другой ответ'], correctAnswer: 'Отправляет изменения', hint: 'Upload' },
      { type: 'quiz', question: 'git pull ___ изменения.', options: ["перемещает", "копирует", "получает", "создаёт", "отправляет"], correctAnswer: 'получает', hint: 'Download' },
      { type: 'quiz', question: 'Pull Request — это:', options: ['Предложение изменений', 'Запрос на скачивание', 'Команда Git', 'Тип ветки', 'Другой ответ'], correctAnswer: 'Предложение изменений', hint: 'Merge request' },
      { type: 'quiz', question: 'Code review — ___ кода.', options: ["оптимизация", "форматирование", "проверка", "удаление", "написание"], correctAnswer: 'проверка', hint: 'Review' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с GitHub! 🐙" }
  },
  {
    title: "Стиль кода и соглашения",
    subject: "Программирование",
    icon: "Code2",
    color: "text-cyan-500",
    tasks: [
      { type: 'quiz', question: 'PEP 8 — ___ кода Python.', options: ["образец", "правило", "шаблон", "формат", "стиль"],
      keyPoints: [
        "Основные правила — Отступы:",
        "Длина строки — Максимум 79 символов",
        "Длинные строки можно разбивать — \`\`\`python",
      ],
      examples: [
        "Техническое задание: функции программы, технологии, сроки выполнения",
        "MVP (Minimum Viable Product) — начните с минимальной работающей версии",
        "Декомпозиция: разбейте проект на недели — интерфейс → логика → сохранение → тестирование",
      ], correctAnswer: 'стиль', hint: 'Правила' },
      { type: 'quiz', question: 'Отступ в Python:', options: ['4 пробела', '2 пробела', 'Таб', '8 пробелов', 'Другой ответ'], correctAnswer: '4 пробела', hint: 'Стандарт' },
      { type: 'quiz', question: 'Длина строки до ___ символов.', options: ["80", "100", "79", "72", "99"], correctAnswer: '79', hint: 'Ограничение' },
      { type: 'quiz', question: 'snake_case используется для:', options: ['Функций и переменных', 'Классов', 'Констант', 'Модулей', 'Другой ответ'], correctAnswer: 'Функций и переменных', hint: 'Именование' },
      { type: 'quiz', question: 'pylint — ___ для проверки стиля.', options: ["редактор", "интерпретатор", "отладчик", "система", "линтер"], correctAnswer: 'линтер', hint: 'Инструмент' }
    ],
    reward: { stars: 3, message: "Ты следуешь стилю кода! ✨" }
  },
  {
    title: "Выбор и планирование проекта",
    subject: "Программирование",
    icon: "ClipboardList",
    color: "text-indigo-400",
    tasks: [
      { type: 'quiz', question: 'MVP — минимальный ___ продукт.', options: ["полезный", "рабочий", "готовый", "функциональный", "жизнеспособный"],
      keyPoints: [
        "Критерии выбора — Интерес — тема должна быть увлекательной",
        "Интерес — тема должна быть увлекательной",
        "Посильность — соответствует вашим навыкам",
      ],
      examples: [
        "Итеративная разработка: маленькие шаги с регулярными коммитами после каждой функции",
        "Купить хлеб",
        "text",
        "Купить хлеб",
        "done",
        "Рефакторинг — улучшение кода без изменения функциональности",
      ], correctAnswer: 'жизнеспособный', hint: 'Базовая версия' },
      { type: 'quiz', question: 'Критерий выбора проекта:', options: ['Интерес', 'Сложность', 'Цена', 'Время года', 'Другой ответ'], correctAnswer: 'Интерес', hint: 'Мотивация' },
      { type: 'quiz', question: 'Техническое ___ описывает требования.', options: ["документ", "задание", "руководство", "файл", "описание"], correctAnswer: 'задание', hint: 'Документ' },
      { type: 'quiz', question: 'Декомпозиция — это:', options: ['Разбиение на подзадачи', 'Удаление задач', 'Объединение задач', 'Сортировка задач', 'Другой ответ'], correctAnswer: 'Разбиение на подзадачи', hint: 'Деление' },
      { type: 'quiz', question: 'Функциональные ___ описывают возможности.', options: ["классы", "задачи", "функции", "модули", "требования"], correctAnswer: 'требования', hint: 'Что должно делать' }
    ],
    reward: { stars: 3, message: "Ты умеешь планировать проекты! 📋" }
  },
  {
    title: "Реализация проекта",
    subject: "Программирование",
    icon: "Rocket",
    color: "text-red-500",
    tasks: [
      { type: 'quiz', question: 'Итеративная разработка — ___ шаги.', options: ["параллельные", "последовательные", "обратные", "случайные", "маленькие"],
      keyPoints: [
        "Маленькие шаги — \`\`\`bash",
        "Регулярные коммиты — Коммит после каждой завершённой функции",
        "Ключевое понятие: Реализация проекта",
      ],
      examples: [
        "Структура: введение (1-2 мин) → демонстрация (3-5 мин) → техническая часть (2-3 мин)",
        "Готовьте запасные скриншоты на случай технических проблем при демонстрации",
        "Тренируйтесь выступать — ограничьте время, готовьте ответы на возможные вопросы",
      ], correctAnswer: 'маленькие', hint: 'Постепенно' },
      { type: 'quiz', question: 'Рефакторинг — это:', options: ['Улучшение кода без изменения функций', 'Добавление функций', 'Удаление кода', 'Тестирование', 'Другой ответ'], correctAnswer: 'Улучшение кода без изменения функций', hint: 'Оптимизация' },
      { type: 'quiz', question: 'Регулярные ___ сохраняют историю.', options: ["бекапы", "сохранения", "ветки", "архивы", "коммиты"], correctAnswer: 'коммиты', hint: 'Git' },
      { type: 'quiz', question: 'Тестировать нужно:', options: ['После каждого изменения', 'Один раз в конце', 'Не нужно', 'Раз в неделю', 'Другой ответ'], correctAnswer: 'После каждого изменения', hint: 'Регулярно' },
      { type: 'quiz', question: 'Документирование помогает ___ код.', options: ["архивировать", "шифровать", "перемещать", "копировать", "понимать"], correctAnswer: 'понимать', hint: 'Читаемость' }
    ],
    reward: { stars: 3, message: "Ты умеешь реализовывать проекты! 🚀" }
  },
  {
    title: "Презентация проекта",
    subject: "Программирование",
    icon: "Presentation",
    color: "text-cyan-500",
    tasks: [
      { type: 'quiz', question: 'Структура презентации: проблема, решение, ___ .', options: ["обсуждение", "демонстрация", "выводы", "вопросы", "практика"],
      keyPoints: [
        "Структура презентации — Введение (1-2 минуты):",
        "Введение (1-2 минуты) — Кто вы",
        "Демонстрация (3-5 минут) — Запуск программы",
      ],
      examples: [
        "Ретроспектива: что получилось, что не удалось, чему научились, что улучшить",
        "Версии развития: v1.1 — новые функции, v2.0 — масштабные изменения",
        "Портфолио: опубликуйте код на GitHub с описанием и скриншотами в README",
      ], correctAnswer: 'демонстрация', hint: 'Показ работы' },
      { type: 'quiz', question: 'Демонстрация работы — это:', options: ['Показ проекта', 'Рассказ о планах', 'Чтение документации', 'Обсуждение кода', 'Другой ответ'], correctAnswer: 'Показ проекта', hint: 'В действии' },
      { type: 'quiz', question: 'Обратная ___ помогает улучшить проект.', options: ["поддержка", "сторона", "помощь", "связь", "информация"], correctAnswer: 'связь', hint: 'Feedback' },
      { type: 'quiz', question: 'Ответы на вопросы:', options: ['Помогают объяснить решения', 'Не нужны', 'Только для экспертов', 'Усложняют презентацию', 'Другой ответ'], correctAnswer: 'Помогают объяснить решения', hint: 'Взаимодействие' },
      { type: 'quiz', question: 'Ответы на вопросы ___ .', options: ["экспертов", "друзей", "коллег", "преподавателя", "аудитории"], correctAnswer: 'аудитории', hint: 'После презентации' }
    ],
    reward: { stars: 3, message: "Ты презентуешь проекты! 🎤" }
  },
  {
    title: "Анализ и развитие",
    subject: "Программирование",
    icon: "TrendingUp",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: 'Ретроспектива — анализ ___ проекта.', options: ["тестов", "результатов", "документации", "ошибок", "успехов"],
      keyPoints: [
        "Вопросы для анализа — Что получилось хорошо",
        "Шаблон ретроспективы — \`\`\`",
        "✅ Что получилось — Успешно реализован интерфейс",
      ],
      examples: [
        "Сообщение из 150 страниц по 40 строк по 60 символов, алфавит — русский (32 буквы). I = 150 × 40 × 60 × 5 = 1 800 000 бит ≈ 220 Кбайт.",
        "Монета подброшена дважды: N = 4 события, i = log₂4 = 2 бита информации.",
        "Сообщение число делится на 3 уменьшает неопределённость выбора числа от 1 до 9: 3 варианта из 9, i = log₂(9/3) ≈ 1,58 бита.",
      ], correctAnswer: 'результатов', hint: 'Что получилось' },
      { type: 'quiz', question: 'Портфолио проектов нужно для:', options: ['Карьеры', 'Учёбы', 'Хобби', 'Друзей', 'Другой ответ'], correctAnswer: 'Карьеры', hint: 'Резюме' },
      { type: 'quiz', question: 'Непрерывное ___ — ключ к успеху.', options: ["тестирование", "обучение", "чтение", "документирование", "написание"], correctAnswer: 'обучение', hint: 'Развитие' },
      { type: 'quiz', question: 'Планирование развития включает:', options: ['Следующие шаги', 'Только прошлое', 'Только настоящее', 'Удаление проекта', 'Другой ответ'], correctAnswer: 'Следующие шаги', hint: 'Будущее' },
      { type: 'quiz', question: 'Анализ проблем помогает их ___ .', options: ["избежать", "понять", "найти", "описать", "решить"], correctAnswer: 'решить', hint: 'В будущем' }
    ],
    reward: { stars: 3, message: "Ты анализируешь и развиваешься! 📈" }
  }
]

