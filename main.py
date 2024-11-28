import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    position TEXT,
    salary REAL,
    hire_date TEXT,
    department_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT
)
''')

cursor.execute('''
CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    project_name TEXT,
    start_date TEXT,
    end_date TEXT,
    budget REAL
)
''')


cursor.executemany('''
INSERT INTO employees (id, first_name, last_name, position, salary, hire_date, department_id)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    (1, 'Ali', 'Karimov', 'Manager', 3000, '2020-03-15', 1),
    (2, 'Nodira', 'Toirova', 'Developer', 2500, '2021-05-10', 2),
    (3, 'Shoxruh', 'Abdullayev', 'Designer', 2200, '2022-01-22', 3),
    (4, 'Zarina', 'Mamadjonova', 'HR Specialist', 1800, '2019-11-11', 1),
    (5, 'Jasur', 'Jasurov', 'Developer', 2400, '2023-02-01', 2)
])

cursor.executemany('''
INSERT INTO departments (id, department_name)
VALUES (?, ?)
''', [
    (1, 'Administration'),
    (2, 'IT'),
    (3, 'Design')
])

cursor.executemany('''
INSERT INTO projects (id, project_name, start_date, end_date, budget)
VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'New Website', '2023-01-10', '2023-06-30', 50000),
    (2, 'Mobile App', '2022-08-15', '2023-03-20', 30000),
    (3, 'CRM System', '2024-02-01', None, 60000)
])

conn.commit()


cursor.execute('''
SELECT first_name || ' ' || last_name AS "Full Name"
FROM employees
''')
print(cursor.fetchall())


cursor.execute('''
SELECT *
FROM employees
ORDER BY salary DESC
''')
print(cursor.fetchall())


cursor.execute('''
SELECT *
FROM employees
WHERE salary > 2500
''')
print(cursor.fetchall())


cursor.execute('''
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3
''')
print(cursor.fetchall())


cursor.execute('''
SELECT *
FROM employees
WHERE salary IN (2400, 3000)
''')
print(cursor.fetchall())


cursor.execute('''
SELECT *
FROM employees
WHERE salary BETWEEN 2000 AND 3000
''')
print(cursor.fetchall())


cursor.execute('''
SELECT *
FROM employees
WHERE first_name LIKE '%a%'
''')
print(cursor.fetchall())


cursor.execute('''
SELECT *
FROM projects
WHERE end_date IS NULL
''')
print(cursor.fetchall())


cursor.execute('''
SELECT department_id, AVG(salary) AS "Average Salary"
FROM employees
GROUP BY department_id
''')
print(cursor.fetchall())


