from repository.estoque_repository import EstoqueRepository
from typing import List

class EstoqueBusiness:
    def __init__(self):
        self.estoque_repository = EstoqueRepository()
    
    def adicionar_item(self, item):
        return self.estoque_repository.adicionar_item(item)

    def obter_todo_estoque(self):
        return self.estoque_repository.obter_todo_estoque()
    
    def recuperar_itens_por_nome(self, nome):
        return self.estoque_repository.recuperar_itens_por_nome(nome)
    
    def retirar_do_estoque_por_nome(self, nome):
        return self.estoque_repository.retirar_do_estoque_por_nome(nome)

    def retirar_do_estoque_por_id(self, _id):
        return self.estoque_repository.retirar_do_estoque_por_id(_id)