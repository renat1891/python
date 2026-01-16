import sqlite3

class DB:
    def __init__(self, file_name="mydb2.db"):
        with sqlite3.connect(file_name) as self.conn:
            self.cursor = self.conn.cursor()

            self.cursor.execute('''CREATE TABLE IF NOT EXISTS person(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT, 
                        age INTEGER
                        )''')
            self.conn.commit()
            
    def add_person(self, name:str, age:int)->None:
        """
        Add a new person to the database.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.

        Returns:
            None
        """
        self.cursor.execute("INSERT INTO person (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()
    
    def show_people(self):
        self.cursor.execute("SELECT * FROM person")
        people =self.cursor.fetchall() 
        for row in people:
            print(row)
        if len(people) == 0:
            print("список пустий")

    def delete_people(self):
        self.cursor.execute("DELETE FROM person")
        self.conn.commit()
    
    def delete_person(self, name):
        self.cursor.execute("DELETE FROM person WHERE name = ?", (name,))
        self.conn.commit()
    
    def exit(self):
        self.conn.close()
        exit()