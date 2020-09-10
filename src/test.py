import sqlite3

conn = sqlite3.connect('../db/data.db')

cursor = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jaewoo', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'test', 'asdf'),
    (3, 'test2', 'asdf')
]

cursor.executemany(insert_query, users)

select_query = "select * from users"

for row in cursor.execute(select_query):
    print(row)

conn.commit()

conn.close()
