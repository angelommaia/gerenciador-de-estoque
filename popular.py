import sqlite3

conn = sqlite3.connect('./banco.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao)
VALUES ('Celular', '3500', 'celular brabo','10-10-2010')
""")

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao)
VALUES ('Cabide', '30', 'cabide','10-10-2010')
""")

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao)
VALUES ('Carro', '100000', 'barrin','10-10-2010')
""")

cursor.execute("""
INSERT INTO estoque (nome, preco, descricao, data_inclusao)
VALUES ('Batata', '2', 'batatinha','10-10-2010')
""")


conn.commit()

conn.close()