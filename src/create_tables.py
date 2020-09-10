import sqlite3

conn = sqlite3.connect('../db/data.db')
cursor = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, " \
               "password text)"
cursor.execute(create_table)

conn.commit()
conn.close()
