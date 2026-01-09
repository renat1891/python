import sqlite3

class DB:
    def __init__(self, file_name="mydb2.db"):
        with sqlite3.connect(file_name) as conn:
            self.cursor = conn.cursor()

            self.cursor.execute('''CREATE TABLE IF NOT EXISTS person(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT, 
                        age INTEGER
                        )''')
            
    def add_person(self, name, age):
        self.cursor.execute("INSERT INTO person (name, age) VALUES (?, ?)", (name, age))
    
    def show_people(self):
        self.cursor.execute("")


new_db = DB()
new_db.add_person("Charlie", 28)
new_db.add_person("Diana", 34)
new_db.add_person("Eve", 29)
