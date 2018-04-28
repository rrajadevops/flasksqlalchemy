import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'raja', 'raajaa')

insert_table = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_table, user)

users = [
(2, 'raja', 'raajaa'),
(3, 'raj', 'raajaa'),
(4, 'raji', 'raajaa')
]

cursor.executemany(insert_table, users)

select_query = "SELECT id FROM users"

for rows in cursor.execute(select_query):
    print (rows)

connection.commit()
connection.close()