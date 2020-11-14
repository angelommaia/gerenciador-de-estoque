from datetime import datetime

class ItemDTO:
    def __init__(self, nome: str, preco: float, descricao: str):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.data_inclusao = datetime.now().replace(microsecond=0)
