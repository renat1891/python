import sqlite3

with sqlite3.connect("mydb.db") as conn:
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS person(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT, 
                   age INTEGER
                   )''')

# CRUD
# ----------------------------Insert----------------------------
    # id = 7
    # name = "Alex"
    # age = 55
    
    # cursor.execute("INSERT INTO person VALUES (?, ?, ?)", (id, name, age))
# -----------------------------
    # name = "Alex"
    # age = 55
    
    # cursor.execute("INSERT INTO person (name, age) VALUES (?, ?)", (name, age))
# -----------------------------
    # data_to_insert = [
    #     ('John', 25),
    #     ('Alice', 30),
    #     ('Bob', 22)
    # ]

    # cursor.executemany("INSERT INTO person (name, age) VALUES (?, ?)", data_to_insert)

# ----------------------------Select----------------------------
    # cursor.execute("SELECT name, age FROM person")
    # for row in cursor.fetchall():
    #     print(row)
    # print(cursor.fetchall())
# -----------------------------
    # DESC / ASC
    # cursor.execute("SELECT * FROM person ORDER BY id DESC LIMIT 2")

    # print(cursor.fetchall())

# --------------------------------------Select where
    # fetchall / fetch
    # cursor.execute("SELECT * FROM person WHERE name = 'Alex' and age < 30")

    # for row in cursor.fetchall():
    #     print(row)

# --------------------------------------Delete
        
    # cursor.execute("DELETE FROM person WHERE name = 'Alex' and age < 30")

    
# --------------------------------------UPDATE
    
    # cursor.execute("UPDATE person SET age = 30 WHERE name = 'Alex' and age > 30")