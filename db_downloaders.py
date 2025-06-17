import sqlite3
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS downloads(
count INT DEFAULT 0)''')

cursor.execute("INSERT INTO downloads (count) VALUES(0)")
conn.commit()

def counter():
    cursor.execute("UPDATE downloads SET count = count + 1")
    conn.commit()
    return cursor.fetchone()