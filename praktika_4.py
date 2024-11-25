import sqlite3

# Шаг 1. Создайте новую базу данных
# Подключаемся к базе данных (если файла базы данных нет, он будет создан)
connection = sqlite3.connect("SchoolDB.db")
cursor = connection.cursor()

# Шаг 2. Создайте таблицы в базе данных
# Создаем таблицу для студентов
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Создаем таблицу для курсов
cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
)
''')

# Создаем таблицу для записей студентов на курсы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students (id),
    FOREIGN KEY (course_id) REFERENCES Courses (id)
)
''')

# Шаг 3. Заполните таблицы данными
# Вставляем данные в таблицу студентов
cursor.executemany('''
INSERT INTO Students (name, age) VALUES (?, ?)
''', [
    ("Alice", 20),
    ("Bob", 22),
    ("Charlie", 19)
])

# Вставляем данные в таблицу курсов
cursor.executemany('''
INSERT INTO Courses (course_name) VALUES (?)
''', [
    ("Mathematics",),
    ("Physics",),
    ("Computer Science",)
])

# Вставляем данные в таблицу записей на курсы
cursor.executemany('''
INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)
''', [
    (1, 1),  # Alice записана на Mathematics
    (2, 2),  # Bob записан на Physics
    (3, 3),  # Charlie записан на Computer Science
    (1, 3)   # Alice записана на Computer Science
])

# Сохраняем изменения
connection.commit()

# Проверяем данные (опционально)
print("Students:")
for row in cursor.execute("SELECT * FROM Students"):
    print(row)

print("\nCourses:")
for row in cursor.execute("SELECT * FROM Courses"):
    print(row)

print("\nEnrollments:")
for row in cursor.execute("SELECT * FROM Enrollments"):
    print(row)

# Закрываем соединение с базой данных
connection.close()
