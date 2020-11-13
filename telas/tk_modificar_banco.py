def adc_item_ao_banco():  #falta apenas puxar os dados das entrys, em uma nova janela (ou não) #falta tbm usar a funcao q o Lucas fez
	
	#USAR FUNCAO DO LUCAS DPS
	import sqlite3
	conn = sqlite3.connect('./banco.db')
	cursor = conn.cursor()
	nome_item = 'abroba'
	preco_item = '100'
	descricao_item = 'organica'
	data_inclusao_item = '12-11-2020'
	cursor.execute("""
	INSERT INTO estoque (nome, preco, descricao, data_inclusao)
	VALUES (?, ?, ?,?)
	""",(nome_item, preco_item, descricao_item, data_inclusao_item))
	
	conn.commit()
	conn.close()

def remover_item_do_banco():
	import sqlite3
	from business.estoque_business import EstoqueBusiness
