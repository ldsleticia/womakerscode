import sqlite3

conexao = sqlite3.connect('banco')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE jantinha(id INT PRIMARY KEY, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')

conexao.commit()
conexao.close()
