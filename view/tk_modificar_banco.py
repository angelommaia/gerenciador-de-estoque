def adc_item_ao_banco(nome_item,preco_item,descricao_item):  #falta apenas puxar os dados das entrys, em uma nova janela (ou não) #falta tbm usar a funcao q o Lucas fez
	
	from modelDTO.item import ItemDTO
	from business.estoque_business import EstoqueBusiness
	
	estoque_business = EstoqueBusiness()
	
	item = ItemDTO(nome_item,preco_item,descricao_item)
	estoque_business.adicionar_item(item)
	

def remover_item_do_banco(nome):
	from modelDTO.item import ItemDTO
	from business.estoque_business import EstoqueBusiness
	
	estoque_business = EstoqueBusiness()
	
	estoque_business.retirar_do_estoque_por_nome(str(nome))