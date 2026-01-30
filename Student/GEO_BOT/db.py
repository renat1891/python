import sqlite3
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "countries.json")

class DB():
    def __init__(self, db_name='quiz.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                tg_id INTEGER UNIQUE,
                score INTEGER DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS countries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country TEXT UNIQUE,
                capital TEXT
            )
        ''')
        self.connection.commit()

        self.cursor.execute("SELECT COUNT(*) FROM countries")
        if self.cursor.fetchone()[0] == 0:
            self.populate_countries_from_json()

    def populate_countries_from_json(self):
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                countries = json.load(f)
            for country, capital in countries.items():
                self.cursor.execute('''
                    INSERT OR IGNORE INTO countries (country, capital) VALUES (?, ?)
                ''', (country, capital))
            self.connection.commit()

    def add_user(self, name, tg_id):
        self.cursor.execute('''
            INSERT OR IGNORE INTO users (name, tg_id) VALUES (?, ?)
        ''', (name, tg_id))
        self.connection.commit()

    def add_score(self, tg_id, points):
        self.cursor.execute('''
            UPDATE users SET score = score + ? WHERE tg_id = ?
        ''', (points, tg_id))
        self.connection.commit()

    def get_score(self, tg_id):
        self.cursor.execute('''
            SELECT score FROM users WHERE tg_id = ?
        ''', (tg_id,))
        row = self.cursor.fetchone()
        return row[0] if row else 0

    def get_countries_data(self):
        self.cursor.execute('''
            SELECT country, capital FROM countries
        ''')
        rows = self.cursor.fetchall()
        return {row[0]: row[1] for row in rows}

    def close(self):
        self.connection.close()
