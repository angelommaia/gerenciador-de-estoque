#
#	 os dados daqui vem direto do banco. é uma forma de conferir se o que aparece na treeview da janela principal esta de acordo
#


def mostrar_banco():
	import sqlite3
	import tkinter as tk
	import tkinter.ttk as ttk
	
	from modelDTO.item import ItemDTO
	from business.estoque_business import EstoqueBusiness
	estoque_business = EstoqueBusiness()

	#abrindo nova janela pra mostrar o banco
	newWindow = tk.Toplevel()
	
	headings = ('Número','Nome','Preço','Descrição','Data de Inclusão')
	#buscando dados no banco
	data = estoque_business.obter_todo_estoque()

	tree=ttk.Treeview(newWindow,show=["headings"]) #inicializando uma treeview na nova janela
	tree["columns"]=headings #o nome de cada coluna sera 1 elemento de headings
	
	#adicionando headings na treeview
	for head in headings:
		tree.heading(head, text=head, anchor=tk.CENTER)
		tree.column(head, anchor=tk.CENTER,width=100)

	
	#adicionando dados nas linhas
	for row in data:
		tree.insert('', tk.END, values=row)
	
	#colocando uma barra lateral para navegação
	scrolltable = tk.Scrollbar(newWindow, command=tree.yview) 
	tree.configure(yscrollcommand=scrolltable.set)
	scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
	tree.pack(expand=tk.YES, fill=tk.BOTH)