import sqlite3

connection = sqlite3.connect('itstep_DB.sl3', 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Antoshka');")
cur.execute("INSERT INTO first_table (name) VALUES ('Artemchik');")
cur.execute("INSERT INTO first_table (name) VALUES ('Maximka');")
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()