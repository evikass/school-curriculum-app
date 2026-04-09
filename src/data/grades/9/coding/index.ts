import { Subject, GameLesson } from '../../../types'

export const lessons: Subject = {
  id: 'coding-9',
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
          tasks: ['Определить сложность алгоритма', 'Сравнить алгоритмы по эффективности', 'Выбрать оптимальный алгоритм для задачи']
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
          tasks: ['Реализовать алгоритм сортировки', 'Сравнить методы сортировки', 'Выбрать сортировку для конкретной задачи']
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
          tasks: ['Реализовать стек', 'Реализовать очередь', 'Решить задачу с использованием стека']
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
          tasks: ['Построить бинарное дерево', 'Реализовать обход графа', 'Решить задачу поиска пути']
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
          tasks: ['Создать класс "Книга"', 'Создать экземпляры класса', 'Добавить методы в класс']
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
          tasks: ['Создать приватные атрибуты', 'Реализовать свойства через @property', 'Добавить валидацию в setter']
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
          tasks: ['Создать иерархию классов "Фигуры"', 'Переопределить метод', 'Использовать super()']
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
          tasks: ['Реализовать полиморфный метод', 'Создать абстрактный класс', 'Использовать полиморфизм на практике']
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
          tasks: ['Прочитать файл целиком', 'Прочитать файл построчно', 'Записать данные в файл']
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
          tasks: ['Сохранить список словарей в JSON', 'Прочитать CSV в список словарей', 'Преобразовать CSV в JSON']
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
          tasks: ['Написать SELECT-запрос с условием', 'Добавить данные в таблицу', 'Обновить запись в таблице']
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
          tasks: ['Создать базу данных', 'Добавить записи в таблицу', 'Выполнить SELECT-запрос']
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
          tasks: ['Создать HTML-страницу', 'Добавить заголовки и абзацы', 'Создать список и таблицу']
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
          tasks: ['Добавить стили к странице', 'Использовать Flexbox', 'Создать адаптивную вёрстку']
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
          tasks: ['Создать Flask-приложение', 'Добавить маршруты', 'Использовать шаблоны']
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
          tasks: ['Создать HTML-форму', 'Обработать отправку формы в Flask', 'Добавить валидацию']
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
          tasks: ['Создать окно приложения', 'Добавить виджеты Label и Button', 'Создать поле ввода']
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
          tasks: ['Создать форму регистрации', 'Обработать данные формы', 'Добавить валидацию']
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
          tasks: ['Привязать функцию к кнопке', 'Обработать нажатие клавиши', 'Создать обработчик клика мыши']
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
          tasks: ['Создать меню с пунктами', 'Показать диалоговое окно', 'Реализовать открытие файла']
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
          tasks: ['Использовать print-отладку', 'Поставить точку останова', 'Пошагово выполнить код']
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
          tasks: ['Написать unit-тест для функции', 'Использовать assertEqual', 'Протестировать исключение']
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
          tasks: ['Добавить docstring к функции', 'Создать README.md', 'Добавить type hints']
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
          tasks: ['Использовать try-except', 'Создать своё исключение', 'Написать контекстный менеджер']
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
          tasks: ['Создать репозиторий', 'Сделать коммит', 'Просмотреть историю']
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
          tasks: ['Создать ветку', 'Слить ветки', 'Разрешить конфликт']
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
          tasks: ['Отправить изменения на GitHub', 'Создать Pull Request', 'Провести Code Review']
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
          tasks: ['Проверить код на PEP 8', 'Настроить линтер', 'Исправить нарушения стиля']
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
          tasks: ['Выбрать тему проекта', 'Составить техническое задание', 'Разбить на подзадачи']
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
          tasks: ['Начать разработку по плану', 'Проводить тестирование', 'Документировать код']
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
          tasks: ['Подготовить презентацию', 'Провести демонстрацию', 'Ответить на вопросы']
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
          tasks: ['Провести ретроспективу', 'Спланировать развитие', 'Подготовить портфолио']
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
      { type: 'quiz', question: 'Менеджер компоновки pack:', options: ['Упаковывает виджеты', 'Удаляет виджеты', 'Создаёт виджеты', 'Красит виджеты'], correctAnswer: 'Упаковывает виджеты', hint: 'Размещение' },
      { type: 'fill', question: 'Entry — виджет для ___ данных.', correctAnswer: 'ввода', hint: 'Одна строка' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с Tkinter! 🖼️" }
  },
  {
    title: "Создание форм",
    subject: "Программирование",
    icon: "TextBox",
    color: "text-blue-300",
    tasks: [
      { type: 'fill', question: 'Entry — поле для ___ строки.', correctAnswer: 'одной', hint: 'Однострочное' },
      { type: 'quiz', question: 'Text — это:', options: ['Многострочное поле', 'Метка', 'Кнопка', 'Список'], correctAnswer: 'Многострочное поле', hint: 'Несколько строк' },
      { type: 'fill', question: 'get() ___ данные из виджета.', correctAnswer: 'получает', hint: 'Извлечение' },
      { type: 'quiz', question: 'Checkbutton — это:', options: ['Флажок', 'Переключатель', 'Кнопка', 'Поле'], correctAnswer: 'Флажок', hint: 'Галочка' },
      { type: 'fill', question: 'Radiobutton — ___ переключатель.', correctAnswer: 'радиокнопка', hint: 'Один из нескольких' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать формы! 📝" }
  },
  {
    title: "Обработка событий",
    subject: "Программирование",
    icon: "MousePointerClick",
    color: "text-emerald-400",
    tasks: [
      { type: 'fill', question: 'command привязывает ___ к кнопке.', correctAnswer: 'функцию', hint: 'Обработчик' },
      { type: 'quiz', question: 'bind() привязывает:', options: ['Событие к виджету', 'Виджет к окну', 'Функцию к переменной', 'Файл к программе'], correctAnswer: 'Событие к виджету', hint: 'Реакция' },
      { type: 'fill', question: '<Button-1> — ___ клик мыши.', correctAnswer: 'левый', hint: 'Основная кнопка' },
      { type: 'quiz', question: '<Key> — событие:', options: ['Нажатие клавиши', 'Клик мыши', 'Движение мыши', 'Закрытие окна'], correctAnswer: 'Нажатие клавиши', hint: 'Клавиатура' },
      { type: 'fill', question: 'lambda позволяет передавать ___ .', correctAnswer: 'аргументы', hint: 'Параметры' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать события! 🖱️" }
  },
  {
    title: "Меню и диалоги",
    subject: "Программирование",
    icon: "Menu",
    color: "text-amber-400",
    tasks: [
      { type: 'fill', question: 'Menu — виджет для создания ___ .', correctAnswer: 'меню', hint: 'Пункты' },
      { type: 'quiz', question: 'add_cascade создаёт:', options: ['Вложенное меню', 'Пункт меню', 'Разделитель', 'Кнопку'], correctAnswer: 'Вложенное меню', hint: 'Подменю' },
      { type: 'fill', question: 'messagebox показывает ___ окна.', correctAnswer: 'диалоговые', hint: 'Сообщения' },
      { type: 'quiz', question: 'askopenfilename открывает:', options: ['Диалог выбора файла', 'Файл для чтения', 'Новое окно', 'Сохранение'], correctAnswer: 'Диалог выбора файла', hint: 'Выбор' },
      { type: 'fill', question: 'showinfo показывает ___ сообщение.', correctAnswer: 'информационное', hint: 'Информация' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать меню и диалоги! 📋" }
  },
  {
    title: "Методы отладки",
    subject: "Программирование",
    icon: "Bug",
    color: "text-red-400",
    tasks: [
      { type: 'fill', question: 'Print-отладка — вывод значений в ___ .', correctAnswer: 'консоль', hint: 'Терминал' },
      { type: 'quiz', question: 'Отладчик позволяет:', options: ['Пошагово выполнять код', 'Удалять код', 'Компилировать', 'Архивировать'], correctAnswer: 'Пошагово выполнять код', hint: 'По шагам' },
      { type: 'fill', question: 'Точка ___ останавливает выполнение.', correctAnswer: 'останова', hint: 'Breakpoint' },
      { type: 'quiz', question: 'pdb — это:', options: ['Отладчик Python', 'Компилятор', 'Интерпретатор', 'Редактор'], correctAnswer: 'Отладчик Python', hint: 'Debug' },
      { type: 'fill', question: 'IDE — интегрированная среда ___ .', correctAnswer: 'разработки', hint: 'Development' }
    ],
    reward: { stars: 3, message: "Ты умеешь отлаживать код! 🐛" }
  },
  {
    title: "Unit-тестирование",
    subject: "Программирование",
    icon: "TestTube",
    color: "text-green-500",
    tasks: [
      { type: 'fill', question: 'Unit-тест проверяет ___ функцию.', correctAnswer: 'отдельную', hint: 'Изолированно' },
      { type: 'quiz', question: 'unittest — это:', options: ['Встроенный фреймворк', 'Внешняя библиотека', 'Язык программирования', 'IDE'], correctAnswer: 'Встроенный фреймворк', hint: 'Модуль Python' },
      { type: 'fill', question: 'assertEqual проверяет ___ значений.', correctAnswer: 'равенство', hint: 'Сравнение' },
      { type: 'quiz', question: 'setUp выполняется:', options: ['Перед каждым тестом', 'После каждого теста', 'Один раз в начале', 'В конце всех тестов'], correctAnswer: 'Перед каждым тестом', hint: 'Подготовка' },
      { type: 'fill', question: 'python -m unittest запускает ___ .', correctAnswer: 'тесты', hint: 'Проверка' }
    ],
    reward: { stars: 3, message: "Ты умеешь писать тесты! 🧪" }
  },
  {
    title: "Документирование кода",
    subject: "Программирование",
    icon: "FileText",
    color: "text-blue-400",
    tasks: [
      { type: 'fill', question: 'Docstring — ___ документации функции.', correctAnswer: 'строка', hint: 'Описание' },
      { type: 'quiz', question: 'README.md — это:', options: ['Описание проекта', 'Код программы', 'Тесты', 'Конфигурация'], correctAnswer: 'Описание проекта', hint: 'Документация' },
      { type: 'fill', question: '# означает ___ комментарий.', correctAnswer: 'однострочный', hint: 'Короткий' },
      { type: 'quiz', question: 'Type hints — это:', options: ['Аннотации типов', 'Комментарии', 'Переменные', 'Функции'], correctAnswer: 'Аннотации типов', hint: 'Указание типов' },
      { type: 'fill', question: 'Документация помогает ___ код.', correctAnswer: 'понимать', hint: 'Чтение' }
    ],
    reward: { stars: 3, message: "Ты умеешь документировать код! 📄" }
  },
  {
    title: "Обработка ошибок",
    subject: "Программирование",
    icon: "AlertTriangle",
    color: "text-yellow-500",
    tasks: [
      { type: 'fill', question: 'try-except ___ исключения.', correctAnswer: 'обрабатывает', hint: 'Ловит ошибки' },
      { type: 'quiz', question: 'finally выполняется:', options: ['Всегда', 'Только при ошибке', 'Только без ошибки', 'Никогда'], correctAnswer: 'Всегда', hint: 'Гарантированно' },
      { type: 'fill', question: 'raise ___ исключение.', correctAnswer: 'генерирует', hint: 'Создаёт' },
      { type: 'quiz', question: 'Собственные исключения наследуются от:', options: ['Exception', 'Error', 'BaseException', 'object'], correctAnswer: 'Exception', hint: 'Базовый класс' },
      { type: 'fill', question: 'with автоматически ___ ресурсы.', correctAnswer: 'управляет', hint: 'Контекст' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать ошибки! ⚠️" }
  },
  {
    title: "Git: контроль версий",
    subject: "Программирование",
    icon: "GitBranch",
    color: "text-orange-500",
    tasks: [
      { type: 'fill', question: 'git init ___ репозиторий.', correctAnswer: 'создаёт', hint: 'Инициализация' },
      { type: 'quiz', question: 'git add:', options: ['Добавляет файлы', 'Коммитит', 'Отправляет', 'Клонирует'], correctAnswer: 'Добавляет файлы', hint: 'Staging' },
      { type: 'fill', question: 'git commit ___ изменения.', correctAnswer: 'фиксирует', hint: 'Сохраняет' },
      { type: 'quiz', question: 'git status показывает:', options: ['Состояние файлов', 'Историю', 'Различия', 'Ветки'], correctAnswer: 'Состояние файлов', hint: 'Текущее' },
      { type: 'fill', question: 'git log показывает ___ коммитов.', correctAnswer: 'историю', hint: 'Прошлое' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы Git! 🔀" }
  },
  {
    title: "Ветвление и слияние",
    subject: "Программирование",
    icon: "GitMerge",
    color: "text-purple-500",
    tasks: [
      { type: 'fill', question: 'Ветка — независимая ___ разработки.', correctAnswer: 'линия', hint: 'Ветвь' },
      { type: 'quiz', question: 'git checkout -b:', options: ['Создаёт и переключает ветку', 'Удаляет ветку', 'Сливает ветки', 'Показывает ветки'], correctAnswer: 'Создаёт и переключает ветку', hint: 'Новая ветка' },
      { type: 'fill', question: 'git merge ___ ветки.', correctAnswer: 'сливает', hint: 'Объединяет' },
      { type: 'quiz', question: 'Конфликт возникает при:', options: ['Несовместимых изменениях', 'Удалении ветки', 'Создании ветки', 'Переключении'], correctAnswer: 'Несовместимых изменениях', hint: 'Проблема' },
      { type: 'fill', question: 'git branch показывает список ___ .', correctAnswer: 'веток', hint: 'Перечень' }
    ],
    reward: { stars: 3, message: "Ты понимаешь ветвление! 🌿" }
  },
  {
    title: "GitHub для совместной работы",
    subject: "Программирование",
    icon: "Github",
    color: "text-gray-500",
    tasks: [
      { type: 'fill', question: 'GitHub — платформа для ___ репозиториев.', correctAnswer: 'хостинга', hint: 'Хранение' },
      { type: 'quiz', question: 'git push:', options: ['Отправляет изменения', 'Получает изменения', 'Создаёт ветку', 'Сливает ветки'], correctAnswer: 'Отправляет изменения', hint: 'Upload' },
      { type: 'fill', question: 'git pull ___ изменения.', correctAnswer: 'получает', hint: 'Download' },
      { type: 'quiz', question: 'Pull Request — это:', options: ['Предложение изменений', 'Запрос на скачивание', 'Команда Git', 'Тип ветки'], correctAnswer: 'Предложение изменений', hint: 'Merge request' },
      { type: 'fill', question: 'Code review — ___ кода.', correctAnswer: 'проверка', hint: 'Review' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с GitHub! 🐙" }
  },
  {
    title: "Стиль кода и соглашения",
    subject: "Программирование",
    icon: "Code2",
    color: "text-cyan-500",
    tasks: [
      { type: 'fill', question: 'PEP 8 — ___ кода Python.', correctAnswer: 'стиль', hint: 'Правила' },
      { type: 'quiz', question: 'Отступ в Python:', options: ['4 пробела', '2 пробела', 'Таб', '8 пробелов'], correctAnswer: '4 пробела', hint: 'Стандарт' },
      { type: 'fill', question: 'Длина строки до ___ символов.', correctAnswer: '79', hint: 'Ограничение' },
      { type: 'quiz', question: 'snake_case используется для:', options: ['Функций и переменных', 'Классов', 'Констант', 'Модулей'], correctAnswer: 'Функций и переменных', hint: 'Именование' },
      { type: 'fill', question: 'pylint — ___ для проверки стиля.', correctAnswer: 'линтер', hint: 'Инструмент' }
    ],
    reward: { stars: 3, message: "Ты следуешь стилю кода! ✨" }
  },
  {
    title: "Выбор и планирование проекта",
    subject: "Программирование",
    icon: "ClipboardList",
    color: "text-indigo-400",
    tasks: [
      { type: 'fill', question: 'MVP — минимальный ___ продукт.', correctAnswer: 'жизнеспособный', hint: 'Базовая версия' },
      { type: 'quiz', question: 'Критерий выбора проекта:', options: ['Интерес', 'Сложность', 'Цена', 'Время года'], correctAnswer: 'Интерес', hint: 'Мотивация' },
      { type: 'fill', question: 'Техническое ___ описывает требования.', correctAnswer: 'задание', hint: 'Документ' },
      { type: 'quiz', question: 'Декомпозиция — это:', options: ['Разбиение на подзадачи', 'Удаление задач', 'Объединение задач', 'Сортировка задач'], correctAnswer: 'Разбиение на подзадачи', hint: 'Деление' },
      { type: 'fill', question: 'Функциональные ___ описывают возможности.', correctAnswer: 'требования', hint: 'Что должно делать' }
    ],
    reward: { stars: 3, message: "Ты умеешь планировать проекты! 📋" }
  },
  {
    title: "Реализация проекта",
    subject: "Программирование",
    icon: "Rocket",
    color: "text-red-500",
    tasks: [
      { type: 'fill', question: 'Итеративная разработка — ___ шаги.', correctAnswer: 'маленькие', hint: 'Постепенно' },
      { type: 'quiz', question: 'Рефакторинг — это:', options: ['Улучшение кода без изменения функций', 'Добавление функций', 'Удаление кода', 'Тестирование'], correctAnswer: 'Улучшение кода без изменения функций', hint: 'Оптимизация' },
      { type: 'fill', question: 'Регулярные ___ сохраняют историю.', correctAnswer: 'коммиты', hint: 'Git' },
      { type: 'quiz', question: 'Тестировать нужно:', options: ['После каждого изменения', 'Один раз в конце', 'Не нужно', 'Раз в неделю'], correctAnswer: 'После каждого изменения', hint: 'Регулярно' },
      { type: 'fill', question: 'Документирование помогает ___ код.', correctAnswer: 'понимать', hint: 'Читаемость' }
    ],
    reward: { stars: 3, message: "Ты умеешь реализовывать проекты! 🚀" }
  },
  {
    title: "Презентация проекта",
    subject: "Программирование",
    icon: "Presentation",
    color: "text-cyan-500",
    tasks: [
      { type: 'fill', question: 'Структура презентации: проблема, решение, ___ .', correctAnswer: 'демонстрация', hint: 'Показ работы' },
      { type: 'quiz', question: 'Демонстрация работы — это:', options: ['Показ проекта', 'Рассказ о планах', 'Чтение документации', 'Обсуждение кода'], correctAnswer: 'Показ проекта', hint: 'В действии' },
      { type: 'fill', question: 'Обратная ___ помогает улучшить проект.', correctAnswer: 'связь', hint: 'Feedback' },
      { type: 'quiz', question: 'Ответы на вопросы:', options: ['Помогают объяснить решения', 'Не нужны', 'Только для экспертов', 'Усложняют презентацию'], correctAnswer: 'Помогают объяснить решения', hint: 'Взаимодействие' },
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
