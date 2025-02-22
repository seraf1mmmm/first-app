import sqlite3


connection = sqlite3.connect("Study Java Script/FruitBasket.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Color TEXT NOT NULL
)
""")


fruit_data = [
    ("Яблуко", "Червоне"),
    ("Банан", "Жовтий"),
    ("Апельсин", "Помаранчевий")
]

cursor.executemany("INSERT INTO Fruits (Name, Color) VALUES (?, ?)", fruit_data)
connection.commit()


cursor.execute("UPDATE Fruits SET Color = ? WHERE Name = ?", ("Зелене", "Яблуко"))
connection.commit()


cursor.execute("SELECT * FROM Fruits WHERE Color = ?", ("Жовтий",))
yellow_fruits = cursor.fetchall()
print("Yellow fruits (Жовті фрукти):", yellow_fruits)


cursor.execute("SELECT * FROM Fruits")
all_records = cursor.fetchall()
print("All fruits (Всі фрукти):", all_records)


connection.close()
