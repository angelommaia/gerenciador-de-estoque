from datetime import date

class Item:
    def __init__(self, nome: str, preco: int, descricao: str):
        self.nome = nome
        self.preco = str(preco)
        self.descricao = descricao
        self.data_inclusao = str(date.today())
        self.item_excluido = 0