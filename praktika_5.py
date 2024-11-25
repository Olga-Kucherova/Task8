import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect("SchoolDB.db")
cursor = connection.cursor()

# Шаг 1. Извлеките данные из таблицы
print("Все студенты:")
students = cursor.execute("SELECT * FROM Students").fetchall()
for student in students:
    print(student)

# Шаг 2. Фильтрация данных
print("\nСтуденты, которым 20 лет:")
filtered_students = cursor.execute("SELECT * FROM Students WHERE age = 20").fetchall()
for student in filtered_students:
    print(student)

# Шаг 3. Обновление данных
print("\nОбновляем имя студента с id = 1 на 'Alice Johnson'...")
cursor.execute("UPDATE Students SET name = ? WHERE id = ?", ("Alice Johnson", 1))
connection.commit()

# Проверяем обновление
updated_student = cursor.execute("SELECT * FROM Students WHERE id = 1").fetchone()
print("Обновленные данные:", updated_student)

# Удаление данных
print("\nУдаляем студента с id = 3...")
cursor.execute("DELETE FROM Students WHERE id = ?", (3,))
connection.commit()

# Проверяем удаление
print("Студенты после удаления:")
students_after_deletion = cursor.execute("SELECT * FROM Students").fetchall()
for student in students_after_deletion:
    print(student)

# Закрываем соединение с базой данных
connection.close()
