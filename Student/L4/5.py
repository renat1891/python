import sqlite3

with sqlite3.connect("mydb.db") as conn:
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS person(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT, 
                   age INTEGER
                   )''')
    # name = "Alex"
    # age = 55
    # cursor.execute("INSERT INTO person (name, age) VALUES (?, ?)", (name, age))
    # data_to_insert = [
    #     ('John', 25),
    #     ('Alice', 30),
    #     ('Bob', 22)
    # ]

    # cursor.executemany("INSERT INTO person (name, age) VALUES (?, ?)", data_to_insert)

    # cursor.execute("SELECT * FROM person WHERE age < ?", (30,))
    # results = cursor.fetchall()
    # for row in results:
    #     print(row)

    # name = "Alex"
    # age = 77
    # cursor.execute("INSERT INTO person (name, age) VALUES (?, ?)", (name, age))

    # cursor.execute("DELETE FROM person WHERE name = ? and age = ?", ("Alex", 77))

    cursor.execute("SELECT name FROM person ORDER BY name")
    results = cursor.fetchall()
    for row in results[-2:]:
        print(row[0])