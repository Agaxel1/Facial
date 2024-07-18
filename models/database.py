import sqlite3

def init_db():
    conn = sqlite3.connect('myapp.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name):
    conn = sqlite3.connect('myapp.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect('myapp.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users
