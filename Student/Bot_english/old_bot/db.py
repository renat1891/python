import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER UNIQUE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_word (
        user_id INTEGER,
        word TEXT,
        status INTEGER DEFAULT 0,
        PRIMARY KEY (user_id, word)
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
