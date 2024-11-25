import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect("SchoolDB.db")
cursor = connection.cursor()

# Шаг 1. Соединение таблиц
print("Студенты и курсы, на которые они записаны:")
query_join = '''
SELECT Students.name AS student_name, Courses.course_name 
FROM Students
JOIN Enrollments ON Students.id = Enrollments.student_id
JOIN Courses ON Enrollments.course_id = Courses.id
'''
joined_data = cursor.execute(query_join).fetchall()
for record in joined_data:
    print(record)

# Шаг 2. Группировка данных
print("\nКоличество студентов на каждом курсе:")
query_group_by = '''
SELECT Courses.course_name, COUNT(Enrollments.student_id) AS student_count
FROM Enrollments
JOIN Courses ON Enrollments.course_id = Courses.id
GROUP BY Courses.course_name
'''
grouped_data = cursor.execute(query_group_by).fetchall()
for course, count in grouped_data:
    print(f"{course}: {count} студент(ов)")

# Шаг 3. Агрегатные функции
print("\nСредний возраст студентов на каждом курсе:")
query_aggregate = '''
SELECT Courses.course_name, AVG(Students.age) AS average_age
FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.id
JOIN Courses ON Enrollments.course_id = Courses.id
GROUP BY Courses.course_name
'''
aggregated_data = cursor.execute(query_aggregate).fetchall()
for course, avg_age in aggregated_data:
    print(f"{course}: средний возраст студентов - {avg_age:.2f}")

# Закрываем соединение с базой данных
connection.close()
