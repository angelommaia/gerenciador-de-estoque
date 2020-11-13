def mostrar_banco():
	import sqlite3
	import tkinter as tk
	import tkinter.ttk as ttk
	
	#abrindo nova janela pra mostrar o banco
	newWindow = tk.Toplevel()
	
	headings = ('Número','Nome','Preço','Descrição','Data de Inclusão')
	#buscando dados no banco
	with sqlite3.connect('banco.db') as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM estoque")
		data = (row for row in cursor.fetchall())

	tree=ttk.Treeview(newWindow) #inicializando uma treeview na nova janela
	tree["columns"]=headings #o nome de cada coluna sera 1 elemento de headings
	
	#adicionando headings na treeview
	for head in headings:
		tree.heading(head, text=head, anchor=tk.CENTER)
		tree.column(head, anchor=tk.CENTER)

	
	#adicionando dados nas linhas
	for row in data:
		tree.insert('', tk.END, values=row)
	
	#colocando uma barra lateral para navegação
	scrolltable = tk.Scrollbar(newWindow, command=tree.yview) 
	tree.configure(yscrollcommand=scrolltable.set)
	scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
	tree.pack(expand=tk.YES, fill=tk.BOTH)