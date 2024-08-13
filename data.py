import sqlite3

conn=sqlite3.connect('database.db')

cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    pwd TEXT NOT NULL
); 
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    valor TEXT NOT NULL
);
               ''')

print('\033[32m]'+'Banco de dados Conectado')
