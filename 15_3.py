import sqlite3  # Импортируем модуль для работы с SQLite

# Создаем соединение с базой данных (если файл базы данных не существует, он будет создан)
conn = sqlite3.connect('olegcode_academy.db')
cursor = conn.cursor()  # Создаем объект курсора для выполнения SQL-запросов


# Функция для создания таблиц
def create_tables():
    # Удаляем старую таблицу Students, если она существует
    cursor.execute('DROP TABLE IF EXISTS Students')
    # Создаем таблицу для хранения данных о студентах
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор студента
            Name TEXT NOT NULL,  -- Имя студента (обязательное поле)
            Age TEXT NOT NULL,  -- Возраст студента (обязательное поле)
            Gender TEXT NOT NULL,  -- Пол студента (М или Ж)
            EnrollmentData TEXT NOT NULL  -- Дата зачисления студента (обязательное поле)
        )
    ''')

    # Удаляем старую таблицу Courses, если она существует
    cursor.execute('DROP TABLE IF EXISTS Courses')
    # Создаем таблицу для хранения данных о курсах
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            CourseID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор курса
            CourseName TEXT NOT NULL,  -- Название курса (обязательное поле)
            DurationWeeks INTEGER NOT NULL,  -- Длительность курса в неделях (обязательное поле)
            StartDate TEXT NOT NULL  -- Дата начала курса (обязательное поле)
        )
    ''')

    # Удаляем старую таблицу Enrollments, если она существует
    cursor.execute('DROP TABLE IF EXISTS Enrollments')
    # Создаем таблицу для записи студентов на курсы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Enrollments (
            EnrollmentsID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор записи
            StudentID INTEGER NOT NULL,  -- Идентификатор студента (внешний ключ)
            CourseID INTEGER NOT NULL,  -- Идентификатор курса (внешний ключ)
            EnrollmentsData TEXT NOT NULL,  -- Дата записи на курс
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),  -- Связь с таблицей Students
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)  -- Связь с таблицей Courses
        )
    ''')
    conn.commit()  # Сохраняем изменения в базе данных


# Функция для добавления тестовых данных в таблицы
def insert_sample_data():
    # Вставляем данные о студентах
    cursor.executemany('''
        INSERT INTO Students (Name, Age, Gender, EnrollmentData)
        VALUES (?, ?, ?, ?)
    ''', [
        ('Сергеев Олег', 30, 'М', '2024-11-15'),  # Студент 1
        ('Петров Саша', 35, 'М', '2024-11-10'),  # Студент 2
        ('Петрова Марина', 35, 'Ж', '2024-11-12'),  # Студент 3
        ('Иванова Светлана', 40, 'Ж', '2024-11-13'),  # Студент 4
    ])

    # Вставляем данные о курсах
    cursor.executemany('''
        INSERT INTO Courses (CourseName, DurationWeeks, StartDate)
        VALUES (?, ?, ?)
    ''', [
        ('Основы Python', 6, '2024-03-01'),  # Курс 1
        ('Веб-разработка на HTML и CSS', 8, '2024-03-15'),  # Курс 2
        ('Разработка игр на Unity', 10, '2024-04-01'),  # Курс 3
    ])

    # Вставляем данные о записи на курсы
    cursor.executemany('''
        INSERT INTO Enrollments (StudentID, CourseID, EnrollmentsData)
        VALUES (?, ?, ?)
    ''', [
        (1, 1, '2024-03-02'),  # Студент 1 записан на Курс 1
        (2, 2, '2024-04-16'),  # Студент 2 записан на Курс 2
        (3, 3, '2024-03-02'),  # Студент 3 записан на Курс 3
        (4, 1, '2024-05-16'),  # Студент 4 записан на Курс 1
        (4, 2, '2024-03-17'),  # Студент 4 записан на Курс 2
    ])
    conn.commit()  # Сохраняем изменения в базе данных


# Функция для вывода данных из базы
def fetch_data():
    # Выводим данные о студентах
    print("=== Студенты ===")
    cursor.execute('SELECT * FROM Students')  # Извлекаем все записи из таблицы Students
    for row in cursor.fetchall():  # Перебираем и выводим каждую запись
        print(row)

    # Выводим данные о курсах
    print("\n=== Курсы ===")
    cursor.execute('SELECT * FROM Courses')  # Извлекаем все записи из таблицы Courses
    for row in cursor.fetchall():  # Перебираем и выводим каждую запись
        print(row)

    # Выводим данные о записях на курсы
    print("\n=== Запись на курсы ===")
    cursor.execute('''
        SELECT Enrollments.EnrollmentsID, Students.Name, Courses.CourseName, Enrollments.EnrollmentsData
        FROM Enrollments
        INNER JOIN Students ON Enrollments.StudentID = Students.StudentID
        INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID
    ''')  # Объединяем таблицы Enrollments, Students и Courses
    for row in cursor.fetchall():  # Перебираем и выводим каждую запись
        print(row)


# Основная программа
if __name__ == "__main__":
    create_tables()  # Создаем таблицы
    insert_sample_data()  # Добавляем тестовые данные
    fetch_data()  # Выводим данные из базы

# Закрываем соединение с базой данных
conn.close()
