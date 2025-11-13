import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute(
    '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
'''
)

users_data = [
    ('Ayobami', 'ayobami@gmail.com'),
    ('Jane', 'jane@gmail.com'),
    ('David', 'david@gmail.com')
]

cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users_data)

conn.commit()
conn.close()

print("Database and table created successfully with sample data!");