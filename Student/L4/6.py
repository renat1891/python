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
        self.cursor.execute("SELECT * FROM person")
        people =self.cursor.fetchall() 
        for row in people:
            print(row)
        if len(people) == 0:
            print("список пустий")

    def delete_people(self):
        self.cursor.execute("DELETE FROM person")
    
    def delete_person(self, name):
        self.cursor.execute("DELETE FROM person WHERE name = ?", (name,))
    
    


new_db = DB()
while True:
    print("1. Додати")
    print("2. Показати")
    print("3. Видалити всіх")
    print("4. Видалити особу")
    print("5. Вийти")
    cmd = int(input("Введіть команду: "))
    if cmd == 1:
        name = input("Введіть імя")
        age = int(input("Введіть вік"))
        new_db.add_person(name, age)
    elif cmd == 2:
        new_db.show_people()
    elif cmd == 3:
        new_db.delete_people()
    elif cmd == 4:
        name = input("Введіть імя")
        new_db.delete_person(name)
    elif cmd == 5:
        exit()    
    else:
        print("Невідома команда")
    
