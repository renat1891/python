import sqlite3
import time
import math

class BankDB:
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT UNIQUE,
            balance REAL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS deposits(
            user_id INTEGER,
            amount REAL,
            start_time REAL
        )
        """)
        self.conn.commit()

    def register(self, nickname):
        try:
            self.cursor.execute(
                "INSERT INTO users (nickname, balance) VALUES (?, ?)",
                (nickname, 100.0)
            )
            self.conn.commit()
            print("Користувач зареєстрований")
        except sqlite3.IntegrityError:
            print("Такий нік вже існує")

    def get_user(self, value):
        if value.isdigit():
            self.cursor.execute("SELECT * FROM users WHERE id=?", (value,))
        else:
            self.cursor.execute("SELECT * FROM users WHERE nickname=?", (value,))
        return self.cursor.fetchone()

    def show_balance(self, user_id):
        self.cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
        print(self.cursor.fetchone()[0])

    def transfer(self, from_id, to_value, amount):
        to_user = self.get_user(to_value)
        if not to_user:
            print("Користувача не знайдено")
            return

        self.cursor.execute("SELECT balance FROM users WHERE id=?", (from_id,))
        if self.cursor.fetchone()[0] < amount:
            print("Недостатньо коштів")
            return

        self.cursor.execute("UPDATE users SET balance=balance-? WHERE id=?", (amount, from_id))
        self.cursor.execute("UPDATE users SET balance=balance+? WHERE id=?", (amount, to_user[0]))
        self.conn.commit()
        print("Переказ виконано")

    def add_deposit(self, user_id, amount):
        self.cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
        if self.cursor.fetchone()[0] < amount:
            print("Недостатньо коштів")
            return

        self.cursor.execute("SELECT * FROM deposits WHERE user_id=?", (user_id,))
        if self.cursor.fetchone():
            print("Депозит вже існує")
            return

        self.cursor.execute("UPDATE users SET balance=balance-? WHERE id=?", (amount, user_id))
        self.cursor.execute(
            "INSERT INTO deposits VALUES (?, ?, ?)",
            (user_id, amount, time.time())
        )
        self.conn.commit()
        print("Депозит відкрито")

    def _calc_deposit(self, amount, start_time):
        seconds = time.time() - start_time
        periods = int(seconds // 15)
        total = amount * (1.1 ** periods)
        return math.ceil(total * 100) / 100, periods

    def show_deposit(self, user_id):
        self.cursor.execute("SELECT * FROM deposits WHERE user_id=?", (user_id,))
        dep = self.cursor.fetchone()
        if not dep:
            print("Депозит відсутній")
            return

        total, periods = self._calc_deposit(dep[1], dep[2])
        print(dep[1], "періодів:", periods, "сума:", total)

    def withdraw_deposit(self, user_id):
        self.cursor.execute("SELECT * FROM deposits WHERE user_id=?", (user_id,))
        dep = self.cursor.fetchone()
        if not dep:
            print("Депозиту немає")
            return

        total, _ = self._calc_deposit(dep[1], dep[2])

        self.cursor.execute("DELETE FROM deposits WHERE user_id=?", (user_id,))
        self.cursor.execute("UPDATE users SET balance=balance+? WHERE id=?", (total, user_id))
        self.conn.commit()
        print(total)

db = BankDB()
user = None

while True:
    cmd = input("1-регестрація 2-вхід 3-баланс 4-переказ 5-депозит 6-показати депозит 7-зняти 8-вихід: ")

    if cmd == "1":
        db.register(input("Нік: "))

    elif cmd == "2":
        user = db.get_user(input("ID або нік: "))

    elif cmd == "3" and user:
        db.show_balance(user[0])

    elif cmd == "4" and user:
        db.transfer(user[0], input("Кому: "), float(input("Сума: ")))

    elif cmd == "5" and user:
        db.add_deposit(user[0], float(input("Сума: ")))

    elif cmd == "6" and user:
        db.show_deposit(user[0])

    elif cmd == "7" and user:
        db.withdraw_deposit(user[0])

    elif cmd == "8":
        break

    else:
        print("Помилка")



# коли ми поповнюємо депозит, вирішити куди перекидати відстко чи в депозит чи на баланс

# коли ми знімаємо депозит, гроші з депозита на баланс + відсотки

# 1 година це 1%
# заокруглювати в меншу сторону

# перекинути іншому користувачеві, лише треба знати його id 