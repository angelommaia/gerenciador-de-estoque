from repository.estoque_repository import EstoqueRepository
from typing import List

class EstoqueBusiness:
    def __init__(self):
        self.estoque_repository = EstoqueRepository()
    
    def adicionar_item(self, item):
        self.estoque_repository.adicionar_item(item)

    def obter_todo_estoque(self):
        return self.estoque_repository.obter_todo_estoque()
