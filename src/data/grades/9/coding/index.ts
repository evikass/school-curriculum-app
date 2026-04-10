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
      { type: 'quiz', question: 'Какая сложность означает константное время?', options: ['O(1)', 'O(n)', 'O(n²)', 'O(log n)', 'Другой ответ'], correctAnswer: 'O(1)', hint: 'Не зависит от размера данных' },
      { type: 'quiz', question: 'Линейная сложность обозначается как O(___).', options: ['n', 'log n', 'n²', '1', '2n', 'n log n'], correctAnswer: 'n', hint: 'Время растёт пропорционально данным' },
      { type: 'quiz', question: 'Какая сложность у пузырьковой сортировки?', options: ['O(n²)', 'O(n)', 'O(log n)', 'O(1)', 'Другой ответ'], correctAnswer: 'O(n²)', hint: 'Два вложенных цикла' },
      { type: 'quiz', question: 'Сложность O(log n) — ___ сложность.', options: ['логарифмическая', 'линейная', 'квадратичная', 'константная', 'экспоненциальная', 'факториальная'], correctAnswer: 'логарифмическая', hint: 'Бинарный поиск' },
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
      { type: 'quiz', question: 'Упорядочивание элементов — это ___ .', options: ['сортировка', 'фильтрация', 'поиск', 'удаление', 'копирование', 'сравнение'], correctAnswer: 'сортировка', hint: 'Расстановка по порядку' },
      { type: 'quiz', question: 'Какой алгоритм сортировки самый простой?', options: ['Пузырьковый', 'Быстрый', 'Слиянием', 'Пирамидальный', 'Другой ответ'], correctAnswer: 'Пузырьковый', hint: 'Но медленный O(n²)' },
      { type: 'quiz', question: 'Быстрая сортировка работает за O(n log ___).', options: ['n', 'n²', '1', 'log n', 'm', 'k'], correctAnswer: 'n', hint: 'В среднем случае' },
      { type: 'quiz', question: 'Сортировка выбором:', options: ['Находит минимум и ставит в начало', 'Меняет соседние элементы', 'Делит массив пополам', 'Использует пирамиду', 'Другой ответ'], correctAnswer: 'Находит минимум и ставит в начало', hint: 'Постепенно заполняем начало' },
      { type: 'quiz', question: 'Сортировка слиянием — ___ алгоритм.', options: ['стабильный', 'нестабильный', 'простой', 'медленный', 'линейный', 'неэффективный'], correctAnswer: 'стабильный', hint: 'Сохраняет порядок равных' }
    ],
    reward: { stars: 3, message: "Ты понимаешь сортировку! 🔄" }
  },
  {
    title: "Стек и очередь",
    subject: "Программирование",
    icon: "Layers",
    color: "text-purple-400",
    tasks: [
      { type: 'quiz', question: 'LIFO расшифровывается как Last In, First ___ .', options: ['Out', 'In', 'Over', 'On', 'Off', 'Open'], correctAnswer: 'Out', hint: 'Последний пришёл — первый вышел' },
      { type: 'quiz', question: 'Стек работает по принципу:', options: ['LIFO', 'FIFO', 'LILO', 'FILO', 'Другой ответ'], correctAnswer: 'LIFO', hint: 'Стек блюд' },
      { type: 'quiz', question: 'Операция добавления в стек — ___ .', options: ['push', 'pop', 'peek', 'pull', 'add', 'insert'], correctAnswer: 'push', hint: 'Поместить наверх' },
      { type: 'quiz', question: 'Очередь работает по принципу:', options: ['FIFO', 'LIFO', 'LILO', 'FILO', 'Другой ответ'], correctAnswer: 'FIFO', hint: 'Очередь в магазине' },
      { type: 'quiz', question: 'Операция удаления из очереди — ___ .', options: ['dequeue', 'enqueue', 'push', 'pop', 'remove', 'delete'], correctAnswer: 'dequeue', hint: 'Убрать из начала' }
    ],
    reward: { stars: 3, message: "Ты понимаешь стек и очередь! 📚" }
  },
  {
    title: "Деревья и графы",
    subject: "Программирование",
    icon: "GitBranch",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: 'Дерево — ___ структура с корнем и узлами.', options: ['иерархическая', 'линейная', 'плоская', 'циклическая', 'сетевая', 'табличная'], correctAnswer: 'иерархическая', hint: 'Один корень, много ветвей' },
      { type: 'quiz', question: 'Бинарное дерево имеет не более:', options: ['Двух детей у узла', 'Одного ребёнка', 'Трёх детей', 'Любое количество', 'Другой ответ'], correctAnswer: 'Двух детей у узла', hint: 'Бинарное = двоичное' },
      { type: 'quiz', question: 'Граф — набор вершин и ___ .', options: ['рёбер', 'узлов', 'листьев', 'корней', 'путей', 'циклов'], correctAnswer: 'рёбер', hint: 'Связи между вершинами' },
      { type: 'quiz', question: 'BFS — это поиск:', options: ['В ширину', 'В глубину', 'Бинарный', 'Линейный', 'Другой ответ'], correctAnswer: 'В ширину', hint: 'Breadth-First Search' },
      { type: 'quiz', question: 'DFS — поиск в ___ .', options: ['глубину', 'ширину', 'высоту', 'длину', 'объём', 'площадь'], correctAnswer: 'глубину', hint: 'Deep-First Search' }
    ],
    reward: { stars: 3, message: "Ты понимаешь деревья и графы! 🌳" }
  },
  {
    title: "Классы и объекты",
    subject: "Программирование",
    icon: "Box",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: 'Класс — это ___ для создания объектов.', options: ['шаблон', 'объект', 'метод', 'функция', 'переменная', 'тип'], correctAnswer: 'шаблон', hint: 'Чертёж' },
      { type: 'quiz', question: 'Объект — это:', options: ['Экземпляр класса', 'Шаблон класса', 'Метод класса', 'Атрибут класса', 'Другой ответ'], correctAnswer: 'Экземпляр класса', hint: 'Конкретный представитель' },
      { type: 'quiz', question: '___ в Python ссылается на текущий объект.', options: ['self', 'this', 'me', 'obj', 'current', 'instance'], correctAnswer: 'self', hint: 'Ключевое слово' },
      { type: 'quiz', question: 'Конструктор — это метод:', options: ['Для создания объекта', 'Для удаления объекта', 'Для копирования', 'Для сравнения', 'Другой ответ'], correctAnswer: 'Для создания объекта', hint: '__init__ в Python' },
      { type: 'quiz', question: 'Атрибуты — это ___ класса.', options: ['свойства', 'методы', 'функции', 'объекты', 'переменные', 'константы'], correctAnswer: 'свойства', hint: 'Данные объекта' }
    ],
    reward: { stars: 3, message: "Ты понимаешь классы и объекты! 📦" }
  },
  {
    title: "Инкапсуляция",
    subject: "Программирование",
    icon: "Lock",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: 'Инкапсуляция — ___ внутренней реализации.', options: ['скрытие', 'открытие', 'удаление', 'копирование', 'изменение', 'добавление'], correctAnswer: 'скрытие', hint: 'Защита данных' },
      { type: 'quiz', question: 'Приватные атрибуты в Python начинаются с:', options: ['_', '__', '@', '#', 'Другой ответ'], correctAnswer: '_', hint: 'Одно или два подчёркивания' },
      { type: 'quiz', question: '___ контролируют доступ к атрибутам.', options: ['свойства', 'методы', 'функции', 'классы', 'объекты', 'переменные'], correctAnswer: 'свойства', hint: 'property в Python' },
      { type: 'quiz', question: 'Публичные атрибуты:', options: ['Доступны извне', 'Скрыты', 'Только для чтения', 'Удалены', 'Другой ответ'], correctAnswer: 'Доступны извне', hint: 'Без ограничений' },
      { type: 'quiz', question: 'Инкапсуляция защищает данные от ___ изменения.', options: ['некорректного', 'правильного', 'быстрого', 'медленного', 'частого', 'редкого'], correctAnswer: 'некорректного', hint: 'Безопасность' }
    ],
    reward: { stars: 3, message: "Ты понимаешь инкапсуляцию! 🔒" }
  },
  {
    title: "Наследование",
    subject: "Программирование",
    icon: "GitMerge",
    color: "text-orange-400",
    tasks: [
      { type: 'quiz', question: 'Наследование — создание нового класса на основе ___ .', options: ['существующего', 'нового', 'пустого', 'абстрактного', 'базового', 'родительского'], correctAnswer: 'существующего', hint: 'Базовый класс' },
      { type: 'quiz', question: 'Родительский класс также называют:', options: ['Базовым', 'Производным', 'Дочерним', 'Наследником', 'Другой ответ'], correctAnswer: 'Базовым', hint: 'Основа' },
      { type: 'quiz', question: '___ вызывает метод родительского класса.', options: ['super()', 'parent()', 'base()', 'this()', 'self()', 'call()'], correctAnswer: 'super()', hint: 'Функция в Python' },
      { type: 'quiz', question: 'Переопределение методов — это:', options: ['Изменение поведения', 'Удаление метода', 'Добавление метода', 'Копирование метода', 'Другой ответ'], correctAnswer: 'Изменение поведения', hint: 'Новая реализация' },
      { type: 'quiz', question: 'Дочерний класс ___ родительский.', options: ['расширяет', 'удаляет', 'копирует', 'игнорирует', 'заменяет', 'перезаписывает'], correctAnswer: 'расширяет', hint: 'Добавляет функциональность' }
    ],
    reward: { stars: 3, message: "Ты понимаешь наследование! 🔀" }
  },
  {
    title: "Полиморфизм",
    subject: "Программирование",
    icon: "Copy",
    color: "text-cyan-400",
    tasks: [
      { type: 'quiz', question: 'Полиморфизм — единый ___ для разных форм.', options: ['интерфейс', 'класс', 'объект', 'метод', 'атрибут', 'тип'], correctAnswer: 'интерфейс', hint: 'Один метод — разное поведение' },
      { type: 'quiz', question: 'Методы с одинаковым именем в разных классах:', options: ['Работают по-разному', 'Одинаково', 'Не работают', 'Дублируются', 'Другой ответ'], correctAnswer: 'Работают по-разному', hint: 'Суть полиморфизма' },
      { type: 'quiz', question: '___ классы определяют интерфейс без реализации.', options: ['Абстрактные', 'Конкретные', 'Базовые', 'Дочерние', 'Публичные', 'Приватные'], correctAnswer: 'Абстрактные', hint: 'ABC в Python' },
      { type: 'quiz', question: 'Полиморфизм позволяет:', options: ['Работать с разными классами одинаково', 'Создавать классы', 'Удалять методы', 'Копировать объекты', 'Другой ответ'], correctAnswer: 'Работать с разными классами одинаково', hint: 'Гибкость кода' },
      { type: 'quiz', question: 'Полиморфизм ___ код.', options: ['упрощает', 'усложняет', 'удаляет', 'копирует', 'игнорирует', 'перезаписывает'], correctAnswer: 'упрощает', hint: 'Удобство' }
    ],
    reward: { stars: 3, message: "Ты понимаешь полиморфизм! 🎭" }
  },
  {
    title: "Чтение и запись файлов",
    subject: "Программирование",
    icon: "FileText",
    color: "text-yellow-400",
    tasks: [
      { type: 'quiz', question: 'Файлы хранят данные между ___ программы.', options: ['запусками', 'строками', 'функциями', 'классами', 'циклами', 'методами'], correctAnswer: 'запусками', hint: 'Сохранение' },
      { type: 'quiz', question: 'Режим "r" означает:', options: ['Чтение', 'Запись', 'Добавление', 'Удаление', 'Другой ответ'], correctAnswer: 'Чтение', hint: 'Read' },
      { type: 'quiz', question: 'Режим "w" — ___ в файл.', options: ['запись', 'чтение', 'добавление', 'удаление', 'перемещение', 'копирование'], correctAnswer: 'запись', hint: 'Write' },
      { type: 'quiz', question: 'with автоматически:', options: ['Закрывает файл', 'Открывает файл', 'Читает файл', 'Удаляет файл', 'Другой ответ'], correctAnswer: 'Закрывает файл', hint: 'Контекстный менеджер' },
      { type: 'quiz', question: '___ () читает весь файл.', options: ['read', 'write', 'open', 'close', 'delete', 'copy'], correctAnswer: 'read', hint: 'Одним вызовом' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с файлами! 📄" }
  },
  {
    title: "Работа с CSV и JSON",
    subject: "Программирование",
    icon: "FileJson",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: 'CSV — формат ___ данных.', options: ['табличных', 'графических', 'звуковых', 'видео', 'архивных', 'исполняемых'], correctAnswer: 'табличных', hint: 'Разделённые запятыми' },
      { type: 'quiz', question: 'JSON поддерживает:', options: ['Объекты и массивы', 'Только строки', 'Только числа', 'Только булевы', 'Другой ответ'], correctAnswer: 'Объекты и массивы', hint: 'Структурированные данные' },
      { type: 'quiz', question: 'json.___() преобразует объект в строку.', options: ['dumps', 'loads', 'read', 'write', 'parse', 'stringify'], correctAnswer: 'dumps', hint: 'Сериализация' },
      { type: 'quiz', question: 'json.loads() выполняет:', options: ['Десериализацию', 'Сериализацию', 'Удаление', 'Чтение файла', 'Другой ответ'], correctAnswer: 'Десериализацию', hint: 'Строка в объект' },
      { type: 'quiz', question: 'CSV расшифровывается как Comma-Separated ___ .', options: ['Values', 'Variables', 'Vectors', 'Views', 'Versions', 'Volumes'], correctAnswer: 'Values', hint: 'Значения' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с CSV и JSON! 📋" }
  },
  {
    title: "Основы SQL",
    subject: "Программирование",
    icon: "Database",
    color: "text-blue-500",
    tasks: [
      { type: 'quiz', question: 'SQL — язык ___ к базам данных.', options: ['запросов', 'программирования', 'разметки', 'стилей', 'скриптов', 'команд'], correctAnswer: 'запросов', hint: 'Structured Query Language' },
      { type: 'quiz', question: 'SELECT — это:', options: ['Выборка данных', 'Добавление данных', 'Удаление данных', 'Обновление данных', 'Другой ответ'], correctAnswer: 'Выборка данных', hint: 'Чтение из таблицы' },
      { type: 'quiz', question: 'INSERT ___ добавляет данные.', options: ['INTO', 'FROM', 'WHERE', 'SET', 'VALUES', 'TABLE'], correctAnswer: 'INTO', hint: 'Вставить в таблицу' },
      { type: 'quiz', question: 'DELETE удаляет:', options: ['Данные', 'Таблицу', 'Базу', 'Столбец', 'Другой ответ'], correctAnswer: 'Данные', hint: 'С условием WHERE' },
      { type: 'quiz', question: 'WHERE — условие ___ .', options: ['фильтрации', 'сортировки', 'группировки', 'объединения', 'удаления', 'вставки'], correctAnswer: 'фильтрации', hint: 'Отбор записей' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы SQL! 💾" }
  },
  {
    title: "SQLite в Python",
    subject: "Программирование",
    icon: "HardDrive",
    color: "text-slate-400",
    tasks: [
      { type: 'quiz', question: 'SQLite — ___ база данных.', options: ['встроенная', 'внешняя', 'сетевая', 'облачная', 'распределённая', 'иерархическая'], correctAnswer: 'встроенная', hint: 'Не требует сервера' },
      { type: 'quiz', question: 'Модуль для работы с SQLite:', options: ['sqlite3', 'sql', 'database', 'db', 'Другой ответ'], correctAnswer: 'sqlite3', hint: 'Стандартная библиотека' },
      { type: 'quiz', question: 'sqlite3.___() создаёт соединение.', options: ['connect', 'open', 'create', 'start', 'init', 'link'], correctAnswer: 'connect', hint: 'Подключение к БД' },
      { type: 'quiz', question: 'Курсор используется для:', options: ['Выполнения запросов', 'Создания БД', 'Закрытия БД', 'Резервного копирования', 'Другой ответ'], correctAnswer: 'Выполнения запросов', hint: 'cursor.execute()' },
      { type: 'quiz', question: 'fetchall() возвращает все ___ .', options: ['результаты', 'ошибки', 'таблицы', 'столбцы', 'строки', 'запросы'], correctAnswer: 'результаты', hint: 'Список записей' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с SQLite! 🗄️" }
  },
  {
    title: "Основы HTML",
    subject: "Программирование",
    icon: "Code",
    color: "text-orange-500",
    tasks: [
      { type: 'quiz', question: 'HTML — язык ___ веб-страниц.', options: ['разметки', 'программирования', 'стилей', 'скриптов', 'запросов', 'данных'], correctAnswer: 'разметки', hint: 'Структура страницы' },
      { type: 'quiz', question: 'Тег для заголовка:', options: ['<h1>', '<header>', '<heading>', '<title>', 'Другой ответ'], correctAnswer: '<h1>', hint: 'От h1 до h6' },
      { type: 'quiz', question: 'Тег <___> создаёт ссылку.', options: ['a', 'link', 'href', 'url', 'ref', 'src'], correctAnswer: 'a', hint: 'Anchor' },
      { type: 'quiz', question: 'Атрибут для адреса ссылки:', options: ['href', 'src', 'link', 'url', 'Другой ответ'], correctAnswer: 'href', hint: 'Hypertext Reference' },
      { type: 'quiz', question: '<img> — тег для ___ .', options: ['изображения', 'ссылки', 'текста', 'видео', 'аудио', 'таблицы'], correctAnswer: 'изображения', hint: 'Picture' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы HTML! 🌐" }
  },
  {
    title: "CSS для стилизации",
    subject: "Программирование",
    icon: "Palette",
    color: "text-pink-400",
    tasks: [
      { type: 'quiz', question: 'CSS — ___ таблицы стилей.', options: ['каскадные', 'календарные', 'качественные', 'компактные', 'комплексные', 'комбинированные'], correctAnswer: 'каскадные', hint: 'Cascading Style Sheets' },
      { type: 'quiz', question: 'Селектор по классу:', options: ['.class', '#class', 'class', '@class', 'Другой ответ'], correctAnswer: '.class', hint: 'Точка перед именем' },
      { type: 'quiz', question: 'Box model: content, padding, border, ___ .', options: ['margin', 'border', 'padding', 'content', 'width', 'height'], correctAnswer: 'margin', hint: 'Внешний отступ' },
      { type: 'quiz', question: 'Flexbox используется для:', options: ['Вёрстки', 'Анимации', 'Форм', 'Базы данных', 'Другой ответ'], correctAnswer: 'Вёрстки', hint: 'Расположение элементов' },
      { type: 'quiz', question: 'Свойство color изменяет ___ текста.', options: ['цвет', 'размер', 'шрифт', 'позицию', 'выравнивание', 'отступ'], correctAnswer: 'цвет', hint: 'Оформление' }
    ],
    reward: { stars: 3, message: "Ты знаешь CSS! 🎨" }
  },
  {
    title: "Flask: создание веб-приложения",
    subject: "Программирование",
    icon: "Flame",
    color: "text-gray-400",
    tasks: [
      { type: 'quiz', question: 'Flask — ___ для веб-приложений.', options: ['микрофреймворк', 'библиотека', 'язык', 'база данных', 'редактор', 'компилятор'], correctAnswer: 'микрофреймворк', hint: 'Лёгкий фреймворк' },
      { type: 'quiz', question: 'Декоратор для маршрута:', options: ['@app.route', '@route', '@url', '@path', 'Другой ответ'], correctAnswer: '@app.route', hint: 'Связывает URL с функцией' },
      { type: 'quiz', question: 'render___() возвращает HTML-шаблон.', options: ['template', 'html', 'page', 'view', 'file', 'string'], correctAnswer: 'template', hint: 'Рендеринг' },
      { type: 'quiz', question: 'app.run() запускает:', options: ['Сервер', 'Базу данных', 'Тесты', 'Компилятор', 'Другой ответ'], correctAnswer: 'Сервер', hint: 'Локальный сервер' },
      { type: 'quiz', question: 'request содержит ___ запроса.', options: ['данные', 'ошибки', 'функции', 'классы', 'методы', 'переменные'], correctAnswer: 'данные', hint: 'Информация от клиента' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать веб-приложения! 🔥" }
  },
  {
    title: "Формы и обработка данных",
    subject: "Программирование",
    icon: "FileInput",
    color: "text-teal-400",
    tasks: [
      { type: 'quiz', question: 'HTML-формы ___ данные пользователя.', options: ['собирают', 'отправляют', 'удаляют', 'копируют', 'перемещают', 'архивируют'], correctAnswer: 'собирают', hint: 'Ввод информации' },
      { type: 'quiz', question: 'Метод POST:', options: ['Отправляет данные', 'Запрашивает данные', 'Удаляет данные', 'Обновляет данные', 'Другой ответ'], correctAnswer: 'Отправляет данные', hint: 'Передача на сервер' },
      { type: 'quiz', question: '<input> — поле для ___ .', options: ['ввода', 'вывода', 'отображения', 'хранения', 'удаления', 'редактирования'], correctAnswer: 'ввода', hint: 'Текст, число, файл' },
      { type: 'quiz', question: 'Валидация — это:', options: ['Проверка корректности', 'Отправка данных', 'Сохранение данных', 'Удаление данных', 'Другой ответ'], correctAnswer: 'Проверка корректности', hint: 'Правильность данных' },
      { type: 'quiz', question: 'request.___ содержит данные формы.', options: ['form', 'data', 'body', 'input', 'value', 'fields'], correctAnswer: 'form', hint: 'В Flask' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с формами! 📝" }
  },
  {
    title: "Библиотека Tkinter",
    subject: "Программирование",
    icon: "Layout",
    color: "text-violet-400",
    tasks: [
      { type: 'quiz', question: 'Tkinter — библиотека для ___ интерфейса.', options: ['графического', 'текстового', 'командного', 'сетевого', 'базового', 'файлового'], correctAnswer: 'графического', hint: 'GUI' },
      { type: 'quiz', question: 'Виджет Button — это:', options: ['Кнопка', 'Поле ввода', 'Метка', 'Список', 'Другой ответ'], correctAnswer: 'Кнопка', hint: 'Нажимается' },
      { type: 'quiz', question: 'root.___() запускает главный цикл.', options: ['mainloop', 'start', 'run', 'begin', 'init', 'execute'], correctAnswer: 'mainloop', hint: 'Обработка событий' },
      { type: 'quiz', question: 'Менеджер компоновки pack:', options: ['Упаковывает виджеты', 'Удаляет виджеты', 'Создаёт виджеты', 'Красит виджеты', 'Другой ответ'], correctAnswer: 'Упаковывает виджеты', hint: 'Размещение' },
      { type: 'quiz', question: 'Entry — виджет для ___ данных.', options: ['ввода', 'вывода', 'отображения', 'хранения', 'обработки', 'проверки'], correctAnswer: 'ввода', hint: 'Одна строка' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с Tkinter! 🖼️" }
  },
  {
    title: "Создание форм",
    subject: "Программирование",
    icon: "TextBox",
    color: "text-blue-300",
    tasks: [
      { type: 'quiz', question: 'Entry — поле для ___ строки.', options: ['одной', 'двух', 'нескольких', 'многострочной', 'пустой', 'длинной'], correctAnswer: 'одной', hint: 'Однострочное' },
      { type: 'quiz', question: 'Text — это:', options: ['Многострочное поле', 'Метка', 'Кнопка', 'Список', 'Другой ответ'], correctAnswer: 'Многострочное поле', hint: 'Несколько строк' },
      { type: 'quiz', question: 'get() ___ данные из виджета.', options: ['получает', 'устанавливает', 'удаляет', 'копирует', 'перемещает', 'проверяет'], correctAnswer: 'получает', hint: 'Извлечение' },
      { type: 'quiz', question: 'Checkbutton — это:', options: ['Флажок', 'Переключатель', 'Кнопка', 'Поле', 'Другой ответ'], correctAnswer: 'Флажок', hint: 'Галочка' },
      { type: 'quiz', question: 'Radiobutton — ___ переключатель.', options: ['радиокнопка', 'флажок', 'кнопка', 'список', 'меню', 'поле'], correctAnswer: 'радиокнопка', hint: 'Один из нескольких' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать формы! 📝" }
  },
  {
    title: "Обработка событий",
    subject: "Программирование",
    icon: "MousePointerClick",
    color: "text-emerald-400",
    tasks: [
      { type: 'quiz', question: 'command привязывает ___ к кнопке.', options: ['функцию', 'переменную', 'класс', 'объект', 'массив', 'строку'], correctAnswer: 'функцию', hint: 'Обработчик' },
      { type: 'quiz', question: 'bind() привязывает:', options: ['Событие к виджету', 'Виджет к окну', 'Функцию к переменной', 'Файл к программе', 'Другой ответ'], correctAnswer: 'Событие к виджету', hint: 'Реакция' },
      { type: 'quiz', question: '<Button-1> — ___ клик мыши.', options: ['левый', 'правый', 'средний', 'двойной', 'тройной', 'длинный'], correctAnswer: 'левый', hint: 'Основная кнопка' },
      { type: 'quiz', question: '<Key> — событие:', options: ['Нажатие клавиши', 'Клик мыши', 'Движение мыши', 'Закрытие окна', 'Другой ответ'], correctAnswer: 'Нажатие клавиши', hint: 'Клавиатура' },
      { type: 'quiz', question: 'lambda позволяет передавать ___ .', options: ['аргументы', 'функции', 'классы', 'объекты', 'массивы', 'переменные'], correctAnswer: 'аргументы', hint: 'Параметры' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать события! 🖱️" }
  },
  {
    title: "Меню и диалоги",
    subject: "Программирование",
    icon: "Menu",
    color: "text-amber-400",
    tasks: [
      { type: 'quiz', question: 'Menu — виджет для создания ___ .', options: ['меню', 'кнопок', 'полей', 'списков', 'окон', 'диалогов'], correctAnswer: 'меню', hint: 'Пункты' },
      { type: 'quiz', question: 'add_cascade создаёт:', options: ['Вложенное меню', 'Пункт меню', 'Разделитель', 'Кнопку', 'Другой ответ'], correctAnswer: 'Вложенное меню', hint: 'Подменю' },
      { type: 'quiz', question: 'messagebox показывает ___ окна.', options: ['диалоговые', 'главные', 'вспомогательные', 'второстепенные', 'поплавковые', 'модальные'], correctAnswer: 'диалоговые', hint: 'Сообщения' },
      { type: 'quiz', question: 'askopenfilename открывает:', options: ['Диалог выбора файла', 'Файл для чтения', 'Новое окно', 'Сохранение', 'Другой ответ'], correctAnswer: 'Диалог выбора файла', hint: 'Выбор' },
      { type: 'quiz', question: 'showinfo показывает ___ сообщение.', options: ['информационное', 'предупреждение', 'ошибку', 'вопрос', 'подтверждение', 'уведомление'], correctAnswer: 'информационное', hint: 'Информация' }
    ],
    reward: { stars: 3, message: "Ты умеешь создавать меню и диалоги! 📋" }
  },
  {
    title: "Методы отладки",
    subject: "Программирование",
    icon: "Bug",
    color: "text-red-400",
    tasks: [
      { type: 'quiz', question: 'Print-отладка — вывод значений в ___ .', options: ['консоль', 'файл', 'базу', 'окно', 'память', 'буфер'], correctAnswer: 'консоль', hint: 'Терминал' },
      { type: 'quiz', question: 'Отладчик позволяет:', options: ['Пошагово выполнять код', 'Удалять код', 'Компилировать', 'Архивировать', 'Другой ответ'], correctAnswer: 'Пошагово выполнять код', hint: 'По шагам' },
      { type: 'quiz', question: 'Точка ___ останавливает выполнение.', options: ['останова', 'входа', 'выхода', 'возврата', 'перехода', 'останова'], correctAnswer: 'останова', hint: 'Breakpoint' },
      { type: 'quiz', question: 'pdb — это:', options: ['Отладчик Python', 'Компилятор', 'Интерпретатор', 'Редактор', 'Другой ответ'], correctAnswer: 'Отладчик Python', hint: 'Debug' },
      { type: 'quiz', question: 'IDE — интегрированная среда ___ .', options: ['разработки', 'тестирования', 'отладки', 'компиляции', 'интерпретации', 'архивации'], correctAnswer: 'разработки', hint: 'Development' }
    ],
    reward: { stars: 3, message: "Ты умеешь отлаживать код! 🐛" }
  },
  {
    title: "Unit-тестирование",
    subject: "Программирование",
    icon: "TestTube",
    color: "text-green-500",
    tasks: [
      { type: 'quiz', question: 'Unit-тест проверяет ___ функцию.', options: ['отдельную', 'все', 'главную', 'вспомогательную', 'системную', 'интеграционную'], correctAnswer: 'отдельную', hint: 'Изолированно' },
      { type: 'quiz', question: 'unittest — это:', options: ['Встроенный фреймворк', 'Внешняя библиотека', 'Язык программирования', 'IDE', 'Другой ответ'], correctAnswer: 'Встроенный фреймворк', hint: 'Модуль Python' },
      { type: 'quiz', question: 'assertEqual проверяет ___ значений.', options: ['равенство', 'различие', 'больше', 'меньше', 'сумму', 'произведение'], correctAnswer: 'равенство', hint: 'Сравнение' },
      { type: 'quiz', question: 'setUp выполняется:', options: ['Перед каждым тестом', 'После каждого теста', 'Один раз в начале', 'В конце всех тестов', 'Другой ответ'], correctAnswer: 'Перед каждым тестом', hint: 'Подготовка' },
      { type: 'quiz', question: 'python -m unittest запускает ___ .', options: ['тесты', 'программу', 'скрипт', 'компиляцию', 'отладку', 'сервер'], correctAnswer: 'тесты', hint: 'Проверка' }
    ],
    reward: { stars: 3, message: "Ты умеешь писать тесты! 🧪" }
  },
  {
    title: "Документирование кода",
    subject: "Программирование",
    icon: "FileText",
    color: "text-blue-400",
    tasks: [
      { type: 'quiz', question: 'Docstring — ___ документации функции.', options: ['строка', 'блок', 'файл', 'комментарий', 'раздел', 'класс'], correctAnswer: 'строка', hint: 'Описание' },
      { type: 'quiz', question: 'README.md — это:', options: ['Описание проекта', 'Код программы', 'Тесты', 'Конфигурация', 'Другой ответ'], correctAnswer: 'Описание проекта', hint: 'Документация' },
      { type: 'quiz', question: '# означает ___ комментарий.', options: ['однострочный', 'многострочный', 'документирующий', 'блочный', 'встроенный', 'специальный'], correctAnswer: 'однострочный', hint: 'Короткий' },
      { type: 'quiz', question: 'Type hints — это:', options: ['Аннотации типов', 'Комментарии', 'Переменные', 'Функции', 'Другой ответ'], correctAnswer: 'Аннотации типов', hint: 'Указание типов' },
      { type: 'quiz', question: 'Документация помогает ___ код.', options: ['понимать', 'удалять', 'копировать', 'перемещать', 'архивировать', 'шифровать'], correctAnswer: 'понимать', hint: 'Чтение' }
    ],
    reward: { stars: 3, message: "Ты умеешь документировать код! 📄" }
  },
  {
    title: "Обработка ошибок",
    subject: "Программирование",
    icon: "AlertTriangle",
    color: "text-yellow-500",
    tasks: [
      { type: 'quiz', question: 'try-except ___ исключения.', options: ['обрабатывает', 'создаёт', 'удаляет', 'игнорирует', 'передаёт', 'возвращает'], correctAnswer: 'обрабатывает', hint: 'Ловит ошибки' },
      { type: 'quiz', question: 'finally выполняется:', options: ['Всегда', 'Только при ошибке', 'Только без ошибки', 'Никогда', 'Другой ответ'], correctAnswer: 'Всегда', hint: 'Гарантированно' },
      { type: 'quiz', question: 'raise ___ исключение.', options: ['генерирует', 'обрабатывает', 'удаляет', 'игнорирует', 'передаёт', 'возвращает'], correctAnswer: 'генерирует', hint: 'Создаёт' },
      { type: 'quiz', question: 'Собственные исключения наследуются от:', options: ['Exception', 'Error', 'BaseException', 'object', 'Другой ответ'], correctAnswer: 'Exception', hint: 'Базовый класс' },
      { type: 'quiz', question: 'with автоматически ___ ресурсы.', options: ['управляет', 'удаляет', 'создаёт', 'копирует', 'перемещает', 'блокирует'], correctAnswer: 'управляет', hint: 'Контекст' }
    ],
    reward: { stars: 3, message: "Ты умеешь обрабатывать ошибки! ⚠️" }
  },
  {
    title: "Git: контроль версий",
    subject: "Программирование",
    icon: "GitBranch",
    color: "text-orange-500",
    tasks: [
      { type: 'quiz', question: 'git init ___ репозиторий.', options: ['создаёт', 'удаляет', 'копирует', 'перемещает', 'архивирует', 'клонирует'], correctAnswer: 'создаёт', hint: 'Инициализация' },
      { type: 'quiz', question: 'git add:', options: ['Добавляет файлы', 'Коммитит', 'Отправляет', 'Клонирует', 'Другой ответ'], correctAnswer: 'Добавляет файлы', hint: 'Staging' },
      { type: 'quiz', question: 'git commit ___ изменения.', options: ['фиксирует', 'удаляет', 'отправляет', 'получает', 'копирует', 'перемещает'], correctAnswer: 'фиксирует', hint: 'Сохраняет' },
      { type: 'quiz', question: 'git status показывает:', options: ['Состояние файлов', 'Историю', 'Различия', 'Ветки', 'Другой ответ'], correctAnswer: 'Состояние файлов', hint: 'Текущее' },
      { type: 'quiz', question: 'git log показывает ___ коммитов.', options: ['историю', 'список', 'дерево', 'граф', 'таблицу', 'диаграмму'], correctAnswer: 'историю', hint: 'Прошлое' }
    ],
    reward: { stars: 3, message: "Ты знаешь основы Git! 🔀" }
  },
  {
    title: "Ветвление и слияние",
    subject: "Программирование",
    icon: "GitMerge",
    color: "text-purple-500",
    tasks: [
      { type: 'quiz', question: 'Ветка — независимая ___ разработки.', options: ['линия', 'часть', 'ветвь', 'копия', 'версия', 'модуль'], correctAnswer: 'линия', hint: 'Ветвь' },
      { type: 'quiz', question: 'git checkout -b:', options: ['Создаёт и переключает ветку', 'Удаляет ветку', 'Сливает ветки', 'Показывает ветки', 'Другой ответ'], correctAnswer: 'Создаёт и переключает ветку', hint: 'Новая ветка' },
      { type: 'quiz', question: 'git merge ___ ветки.', options: ['сливает', 'удаляет', 'создаёт', 'копирует', 'переименовывает', 'перемещает'], correctAnswer: 'сливает', hint: 'Объединяет' },
      { type: 'quiz', question: 'Конфликт возникает при:', options: ['Несовместимых изменениях', 'Удалении ветки', 'Создании ветки', 'Переключении', 'Другой ответ'], correctAnswer: 'Несовместимых изменениях', hint: 'Проблема' },
      { type: 'quiz', question: 'git branch показывает список ___ .', options: ['веток', 'коммитов', 'файлов', 'папок', 'изменений', 'авторов'], correctAnswer: 'веток', hint: 'Перечень' }
    ],
    reward: { stars: 3, message: "Ты понимаешь ветвление! 🌿" }
  },
  {
    title: "GitHub для совместной работы",
    subject: "Программирование",
    icon: "Github",
    color: "text-gray-500",
    tasks: [
      { type: 'quiz', question: 'GitHub — платформа для ___ репозиториев.', options: ['хостинга', 'создания', 'удаления', 'копирования', 'архивации', 'шифрования'], correctAnswer: 'хостинга', hint: 'Хранение' },
      { type: 'quiz', question: 'git push:', options: ['Отправляет изменения', 'Получает изменения', 'Создаёт ветку', 'Сливает ветки', 'Другой ответ'], correctAnswer: 'Отправляет изменения', hint: 'Upload' },
      { type: 'quiz', question: 'git pull ___ изменения.', options: ['получает', 'отправляет', 'удаляет', 'создаёт', 'копирует', 'перемещает'], correctAnswer: 'получает', hint: 'Download' },
      { type: 'quiz', question: 'Pull Request — это:', options: ['Предложение изменений', 'Запрос на скачивание', 'Команда Git', 'Тип ветки', 'Другой ответ'], correctAnswer: 'Предложение изменений', hint: 'Merge request' },
      { type: 'quiz', question: 'Code review — ___ кода.', options: ['проверка', 'написание', 'удаление', 'копирование', 'форматирование', 'оптимизация'], correctAnswer: 'проверка', hint: 'Review' }
    ],
    reward: { stars: 3, message: "Ты умеешь работать с GitHub! 🐙" }
  },
  {
    title: "Стиль кода и соглашения",
    subject: "Программирование",
    icon: "Code2",
    color: "text-cyan-500",
    tasks: [
      { type: 'quiz', question: 'PEP 8 — ___ кода Python.', options: ['стиль', 'стандарт', 'правило', 'формат', 'шаблон', 'образец'], correctAnswer: 'стиль', hint: 'Правила' },
      { type: 'quiz', question: 'Отступ в Python:', options: ['4 пробела', '2 пробела', 'Таб', '8 пробелов', 'Другой ответ'], correctAnswer: '4 пробела', hint: 'Стандарт' },
      { type: 'quiz', question: 'Длина строки до ___ символов.', options: ['79', '80', '100', '120', '72', '99'], correctAnswer: '79', hint: 'Ограничение' },
      { type: 'quiz', question: 'snake_case используется для:', options: ['Функций и переменных', 'Классов', 'Констант', 'Модулей', 'Другой ответ'], correctAnswer: 'Функций и переменных', hint: 'Именование' },
      { type: 'quiz', question: 'pylint — ___ для проверки стиля.', options: ['линтер', 'компилятор', 'отладчик', 'редактор', 'интерпретатор', 'система'], correctAnswer: 'линтер', hint: 'Инструмент' }
    ],
    reward: { stars: 3, message: "Ты следуешь стилю кода! ✨" }
  },
  {
    title: "Выбор и планирование проекта",
    subject: "Программирование",
    icon: "ClipboardList",
    color: "text-indigo-400",
    tasks: [
      { type: 'quiz', question: 'MVP — минимальный ___ продукт.', options: ['жизнеспособный', 'рабочий', 'функциональный', 'прототип', 'готовый', 'полезный'], correctAnswer: 'жизнеспособный', hint: 'Базовая версия' },
      { type: 'quiz', question: 'Критерий выбора проекта:', options: ['Интерес', 'Сложность', 'Цена', 'Время года', 'Другой ответ'], correctAnswer: 'Интерес', hint: 'Мотивация' },
      { type: 'quiz', question: 'Техническое ___ описывает требования.', options: ['задание', 'описание', 'руководство', 'письмо', 'документ', 'файл'], correctAnswer: 'задание', hint: 'Документ' },
      { type: 'quiz', question: 'Декомпозиция — это:', options: ['Разбиение на подзадачи', 'Удаление задач', 'Объединение задач', 'Сортировка задач', 'Другой ответ'], correctAnswer: 'Разбиение на подзадачи', hint: 'Деление' },
      { type: 'quiz', question: 'Функциональные ___ описывают возможности.', options: ['требования', 'задачи', 'функции', 'методы', 'классы', 'модули'], correctAnswer: 'требования', hint: 'Что должно делать' }
    ],
    reward: { stars: 3, message: "Ты умеешь планировать проекты! 📋" }
  },
  {
    title: "Реализация проекта",
    subject: "Программирование",
    icon: "Rocket",
    color: "text-red-500",
    tasks: [
      { type: 'quiz', question: 'Итеративная разработка — ___ шаги.', options: ['маленькие', 'большие', 'случайные', 'параллельные', 'последовательные', 'обратные'], correctAnswer: 'маленькие', hint: 'Постепенно' },
      { type: 'quiz', question: 'Рефакторинг — это:', options: ['Улучшение кода без изменения функций', 'Добавление функций', 'Удаление кода', 'Тестирование', 'Другой ответ'], correctAnswer: 'Улучшение кода без изменения функций', hint: 'Оптимизация' },
      { type: 'quiz', question: 'Регулярные ___ сохраняют историю.', options: ['коммиты', 'бекапы', 'копии', 'сохранения', 'архивы', 'ветки'], correctAnswer: 'коммиты', hint: 'Git' },
      { type: 'quiz', question: 'Тестировать нужно:', options: ['После каждого изменения', 'Один раз в конце', 'Не нужно', 'Раз в неделю', 'Другой ответ'], correctAnswer: 'После каждого изменения', hint: 'Регулярно' },
      { type: 'quiz', question: 'Документирование помогает ___ код.', options: ['понимать', 'удалять', 'копировать', 'перемещать', 'архивировать', 'шифровать'], correctAnswer: 'понимать', hint: 'Читаемость' }
    ],
    reward: { stars: 3, message: "Ты умеешь реализовывать проекты! 🚀" }
  },
  {
    title: "Презентация проекта",
    subject: "Программирование",
    icon: "Presentation",
    color: "text-cyan-500",
    tasks: [
      { type: 'quiz', question: 'Структура презентации: проблема, решение, ___ .', options: ['демонстрация', 'выводы', 'теория', 'практика', 'обсуждение', 'вопросы'], correctAnswer: 'демонстрация', hint: 'Показ работы' },
      { type: 'quiz', question: 'Демонстрация работы — это:', options: ['Показ проекта', 'Рассказ о планах', 'Чтение документации', 'Обсуждение кода', 'Другой ответ'], correctAnswer: 'Показ проекта', hint: 'В действии' },
      { type: 'quiz', question: 'Обратная ___ помогает улучшить проект.', options: ['связь', 'сторона', 'информация', 'реакция', 'помощь', 'поддержка'], correctAnswer: 'связь', hint: 'Feedback' },
      { type: 'quiz', question: 'Ответы на вопросы:', options: ['Помогают объяснить решения', 'Не нужны', 'Только для экспертов', 'Усложняют презентацию', 'Другой ответ'], correctAnswer: 'Помогают объяснить решения', hint: 'Взаимодействие' },
      { type: 'quiz', question: 'Ответы на вопросы ___ .', options: ['аудитории', 'преподавателя', 'экспертов', 'коллег', 'друзей', 'родителей'], correctAnswer: 'аудитории', hint: 'После презентации' }
    ],
    reward: { stars: 3, message: "Ты презентуешь проекты! 🎤" }
  },
  {
    title: "Анализ и развитие",
    subject: "Программирование",
    icon: "TrendingUp",
    color: "text-green-400",
    tasks: [
      { type: 'quiz', question: 'Ретроспектива — анализ ___ проекта.', options: ['результатов', 'ошибок', 'успехов', 'кода', 'тестов', 'документации'], correctAnswer: 'результатов', hint: 'Что получилось' },
      { type: 'quiz', question: 'Портфолио проектов нужно для:', options: ['Карьеры', 'Учёбы', 'Хобби', 'Друзей', 'Другой ответ'], correctAnswer: 'Карьеры', hint: 'Резюме' },
      { type: 'quiz', question: 'Непрерывное ___ — ключ к успеху.', options: ['обучение', 'тестирование', 'написание', 'чтение', 'программирование', 'документирование'], correctAnswer: 'обучение', hint: 'Развитие' },
      { type: 'quiz', question: 'Планирование развития включает:', options: ['Следующие шаги', 'Только прошлое', 'Только настоящее', 'Удаление проекта', 'Другой ответ'], correctAnswer: 'Следующие шаги', hint: 'Будущее' },
      { type: 'quiz', question: 'Анализ проблем помогает их ___ .', options: ['решить', 'понять', 'описать', 'найти', 'избежать', 'проанализировать'], correctAnswer: 'решить', hint: 'В будущем' }
    ],
    reward: { stars: 3, message: "Ты анализируешь и развиваешься! 📈" }
  }
]
