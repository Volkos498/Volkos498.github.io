import sqlite3
conn = sqlite3.connect("users.db",check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY,
               name TEXT, 
               age INTEGER, 
               balance INTEGER)''')

def add_user(user_id, username,age, balance):

    cursor.execute('''INSERT INTO users (user_id, name,age , balance)
    VALUES (?,?,?,?)''', (user_id, username, age, balance))
    conn.commit()

def get_user_all():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
conn.commit()


def get_to_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    return cursor.fetchall






