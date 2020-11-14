from datetime import datetime
from modelDTO.item import ItemDTO
import sqlite3

class EstoqueRepository:

    def adicionar_item(self, item: ItemDTO) -> bool:
        try:
            conn = sqlite3.connect('./banco.db')
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO estoque (nome, preco, descricao, data_inclusao)
            VALUES (?, ?, ?, ?)
            """, (item.nome, item.preco,item.descricao, item.data_inclusao))
            conn.commit()
            conn.close()
        
        except Exception as err:
            print(err)
            return False

        return True

    def recuperar_itens_por_nome(self, nome: str):
        conn = sqlite3.connect('./banco.db')
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT * 
        FROM estoque
        WHERE nome = '{nome}'
        AND item_excluido IS NULL;
        """)

        resultados_cursor = cursor.fetchall()
        conn.close()
        return resultados_cursor

    def obter_todo_estoque(self):
        conn = sqlite3.connect('./banco.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * 
        FROM estoque
        WHERE item_excluido IS NULL;
        """)

        resultados_cursor = cursor.fetchall()
        conn.close()
        return resultados_cursor
    
    def retirar_do_estoque_por_nome(self, nome: str) -> bool:
        try:
            conn = sqlite3.connect('./banco.db')
            cursor = conn.cursor()
            cursor.execute(f"""
            UPDATE estoque
            SET item_excluido = 1,
            data_exclusao = '{str(datetime.now().replace(microsecond=0))}'
            WHERE id = (
                SELECT id
                FROM estoque 
                WHERE nome='{nome}'
                AND item_excluido IS NULL
                LIMIT 1)
            """)
            conn.commit()
            conn.close()
    
        except Exception as err:
            print(err)
            return False

        return True

    def retirar_do_estoque_por_id(self, _id: int):
        try:
            conn = sqlite3.connect('./banco.db')
            cursor = conn.cursor()
            cursor.execute(f"""
            UPDATE estoque
            SET item_excluido = 1,
            data_exclusao = '{str(datetime.now().replace(microsecond=0))}'
            WHERE id = '{_id}' AND item_excluido IS NULL
            """)
            conn.commit()
            conn.close()
    
        except Exception as err:
            print(err)
            return False

        return True