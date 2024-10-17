import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('users.db')

cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
age INTEGER NOT NULL
)
''')

cursor.execute('INSERT INTO Users (username, age) VALUES (?, ?)', ('newuser', 28))
cursor.execute('INSERT INTO Users (username, age) VALUES (?, ?)', ('Vasya', 18))
cursor.execute('INSERT INTO Users (username, age) VALUES (?, ?)', ('Petr', 17))
cursor.execute('INSERT INTO Users (username, age) VALUES (?, ?)', ('Ivan', 25))


cursor.execute('SELECT * FROM Users where age > 18')
users = cursor.fetchall()

for user in users:
    print(user)

connection.close()