import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")
conn.commit()


def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()
    print("Товар добавлен!")


def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nСписок товаров:")
    for product in products:
        print(product)


def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    conn.commit()
    print("Цена обновлена!")


def delete_product(id):
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    print("Товар удалён!")


create_product("Кирпич", 50, 100)
create_product("Цемент", 300, 50)

read_products()

update_product(1, 60)

read_products()

delete_product(2)

read_products()


conn.close()