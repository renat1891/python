import sqlite3
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "A0.json")

class DB():
    def __init__(self, db_name='english_bot.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                tg_id INTEGER UNIQUE
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_word (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                word TEXT,
                status INTEGER DEFAULT 0
            )
        ''')
        self.connection.commit()
    def add_user(self, name, tg_id):
        self.cursor.execute('''
            INSERT OR IGNORE INTO user (name, tg_id) VALUES (?, ?)
        ''', (name, tg_id))
        self.connection.commit()
    def add_words_for_user(self, user_id): 
        with open(json_path, 'r', encoding='utf-8') as f:
            words = json.load(f)
        for word in words:
            self.cursor.execute('''
                INSERT INTO user_word (user_id, word) VALUES (?, ?)
            ''', (user_id, word))
        self.connection.commit()
    def get_user(self, tg_id):
        self.cursor.execute('''
            SELECT * FROM user WHERE tg_id=?
        ''', (tg_id,))
        return self.cursor.fetchone()
    def get_random_word(self, user_id):
        self.cursor.execute('''
            SELECT id, word, status FROM user_word 
            WHERE user_id=? AND status=0 
            ORDER BY RANDOM() LIMIT 1
        ''', (user_id,))
        return self.cursor.fetchone()
    def update_word_status(self, user_id, word_id, status):
        self.cursor.execute('''
            UPDATE user_word SET status=? 
            WHERE id=? AND user_id=?
        ''', (status, word_id, user_id))
        self.connection.commit()





    def close(self):
        self.connection.close()

