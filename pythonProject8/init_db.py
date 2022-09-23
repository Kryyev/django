import sqlite3

connection = sqlite3.connect('example.sqlite3')
with open('schema.sql', 'rt') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()