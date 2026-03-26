import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
)
""")

conn.commit()


cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM movies")
cursor.execute("DELETE FROM reviews")

cursor.executemany("INSERT INTO users (name) VALUES (?)", [
    ("Диана",),
    ("Асан",),
    ("Бек",),
    ("Айжан",),
    ("Руслан",)
])

cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", [
    ("Интерстеллар", "Sci-Fi"),
    ("Титаник", "Drama"),
    ("Матрица", "Action"),
    ("Джокер", "Crime"),
    ("Аватар", "Fantasy")
])

cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", [
    (1, 1, 9),
    (1, 2, 8),
    (2, 1, 10),
    (2, 3, 7),
    (3, 4, 6),
    (3, 5, 8),
    (4, 2, 9),
    (4, 3, 5),
    (5, 1, 7),
    (5, 5, 10)
])

conn.commit()


print("\n Пользователь |  Фильм |  Оценка")

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row)

print("\n Все фильмы (даже без отзывов)")

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)

print("\n Статистика:")

cursor.execute("SELECT AVG(rating) FROM reviews")
print("Средняя оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MAX(rating) FROM reviews")
print("Максимальная:", cursor.fetchone()[0])

cursor.execute("SELECT MIN(rating) FROM reviews")
print("Минимальная:", cursor.fetchone()[0])

cursor.execute("SELECT * FROM users")
print("Users:", cursor.fetchall())

cursor.execute("SELECT * FROM movies")
print("Movies:", cursor.fetchall())

cursor.execute("SELECT * FROM reviews")
print("Reviews:", cursor.fetchall())

conn.close()
