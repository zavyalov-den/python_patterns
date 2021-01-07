import sqlite3

DB_NAME = 'data.db'

con = sqlite3.connect(DB_NAME)
cur = con.cursor()
with open('create_db.sql', 'r') as f:
    text = f.read()
cur.executescript(text)
cur.close()
con.close()
