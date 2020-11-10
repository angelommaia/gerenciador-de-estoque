from datetime import date

class ItemDTO:
    def __init__(self, nome: str, preco: str, descricao: str, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade
        self.data_inclusao = date.today()