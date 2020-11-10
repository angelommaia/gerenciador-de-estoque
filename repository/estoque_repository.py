from model.item import Item
from typing import List
import sqlite3

class EstoqueRepository:
    def __init__(self):
        pass

    def adicionar_item(self, item: Item) -> bool:
        pass

    def remover_item(self, item: Item) -> bool:
        pass

    def recuperar_itens_por_nome(self, nome: str) -> List[Item]:
        pass

    def obter_todo_estoque(self):
        conn = sqlite3.connect('./banco.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM estoque;
        """)

        resultados_cursor = cursor.fetchall()
        for registro in resultados_cursor:
            print(registro)

        conn.close()
        return resultados_cursor
    