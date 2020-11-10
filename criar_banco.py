import sqlite3

conn = sqlite3.connect('./banco.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE estoque (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco INTEGER NOT NULL,
        descricao VARCHAR(255),
        data_inclusao DATE NOT NULL
);
""")

print('Tabela criada com sucesso.')
conn.close()