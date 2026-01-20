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
            user_id INTEGER UNIQUE,
            nickname TEXT,
            balance REAL,
            deposit REAL,
            deposit_start REAL
        )
        """)
        self.conn.commit()

    def register(self, user_id, nickname=""):
        try:
            self.cursor.execute(
                """
                INSERT INTO users (user_id, nickname, balance, deposit, deposit_start)
                VALUES (?, ?, ?, ?, ?)
                """,
                (user_id, nickname, 100.0, 0.0, 0.0)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass

    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        return self.cursor.fetchone()

    def get_balance(self, user_id):
        self.cursor.execute("SELECT balance FROM users WHERE user_id=?", (user_id,))
        return self.cursor.fetchone()[0]

    def get_deposit_info(self, user_id):
        self.cursor.execute(
            "SELECT deposit, deposit_start FROM users WHERE user_id=?",
            (user_id,)
        )
        return self.cursor.fetchone()

    def calculate_profit(self, user_id):
        deposit, start = self.get_deposit_info(user_id)

        if deposit <= 0 or start == 0:
            return 0

        minutes_passed = int((time.time() - start) // 60)
        profit = math.floor(deposit * 0.01 * minutes_passed)
        return profit

    def get_deposit_status(self, user_id):
        deposit, start = self.get_deposit_info(user_id)

        if deposit <= 0:
            return "У вас немає активного депозиту"

        minutes = int((time.time() - start) // 60)
        profit = self.calculate_profit(user_id)

        return (
            f"Депозит: {deposit}\n"
            f"Хвилин пройшло: {minutes}\n"
            f"Нараховані відсотки: {profit}\n"
            f"Разом при знятті: {deposit + profit}"
        )

    def add_to_deposit(self, user_id, amount):
        self.cursor.execute("SELECT balance FROM users WHERE user_id=?", (user_id,))
        balance = self.cursor.fetchone()[0]

        if balance < amount:
            return "Недостатньо коштів"

        profit = self.calculate_profit(user_id)
        if profit > 0:
            self.cursor.execute(
                "UPDATE users SET deposit=deposit+? WHERE user_id=?",
                (profit, user_id)
            )

        self.cursor.execute(
            """
            UPDATE users
            SET balance=balance-?,
                deposit=deposit+?,
                deposit_start=?
            WHERE user_id=?
            """,
            (amount, amount, time.time(), user_id)
        )
        self.conn.commit()

        return "Депозит поповнено"

    def withdraw_deposit(self, user_id):
        deposit, start = self.get_deposit_info(user_id)

        if deposit <= 0:
            return "Депозит відсутній"

        profit = self.calculate_profit(user_id)
        total = deposit + profit

        self.cursor.execute(
            """
            UPDATE users
            SET balance=balance+?,
                deposit=0,
                deposit_start=0
            WHERE user_id=?
            """,
            (total, user_id)
        )
        self.conn.commit()

        return f"Депозит знято. Отримано: {total} (відсотки: {profit})"

    def transfer_to_user(self, from_user_id, to_user_id, amount):
        self.cursor.execute("SELECT balance FROM users WHERE user_id=?", (from_user_id,))
        sender = self.cursor.fetchone()

        if not sender or sender[0] < amount:
            return "Недостатньо коштів"

        self.cursor.execute("SELECT user_id FROM users WHERE user_id=?", (to_user_id,))
        if not self.cursor.fetchone():
            return "Користувача не знайдено"

        self.cursor.execute(
            "UPDATE users SET balance=balance-? WHERE user_id=?",
            (amount, from_user_id)
        )
        self.cursor.execute(
            "UPDATE users SET balance=balance+? WHERE user_id=?",
            (amount, to_user_id)
        )
        self.conn.commit()

        return "Переказ виконано"


# Мови(англ, німецька)
# спорт
# 

