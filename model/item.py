from datetime import date

class Item:
    def __init__(self, nome: str, preco: str, descricao: str):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.data_inclusao = str(date.today())