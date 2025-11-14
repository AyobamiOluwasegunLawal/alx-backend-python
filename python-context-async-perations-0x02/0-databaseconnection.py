import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__ (self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self, type, value, tracback):
        if self.conn:
            self.conn.close()
        return False

users_data = [
    ('Ayobami', 'ayobami@gmail.com'),
    ('Jane', 'jane@gmail.com'),
    ('David', 'david@gmail.com')
]  

with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
                   )''')
    cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users_data)
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    print(results)



    
    