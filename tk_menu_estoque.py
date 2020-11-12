# -*- coding: utf-8 -*-
from tkinter import *
import subprocess
import os
import time

#funcoes

#funcao necessaria para gerar o executavel. sem ela, ele nao consegue lidar com o path que eh alocado em %temp% quando o progarama roda
def resource_path(relative_path):
    #""" Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#funcao criada para definirmos a forma da janela da GUI
def xy_screen(w=300, h=200):
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) - (w/2) 
	y = (hs/2) - (h/2)	
	return (x,y)
	
#GUI
class Application(Frame):
	
	def __init__(self, master=None):
	
		Frame.__init__(self, master)
		self.grid()
		self.master.title("Gerenciamento de Estoque")

		#geometria da tela
		for lin in range(6):
			self.master.rowconfigure(lin, weight=1)    
		for col in range(5):
			self.master.columnconfigure(col, weight=1)
		
		#funcao para mostrar o banco em nova janela
		def mostrar_banco():
			import sqlite3
			import tkinter as tk
			import tkinter.ttk as ttk
			
			#abrindo nova janela pra mostrar o banco
			newWindow = Toplevel()
			
			headings = ("Nome", "Preço", "Descrição", "Data de Inclusão")
			
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
	
		#botao para mostrar o banco
		btn_mostrar_banco = Button(master, text = "Mostrar Banco", command = mostrar_banco)
		btn_mostrar_banco.grid(column=1, row=3, sticky="e")
		
		
		#funcao para adicionar itens ao banco
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
			
		btn_adc_item_ao_banco = Button(master, text = "Adicionar Item", command = adc_item_ao_banco)
		btn_adc_item_ao_banco.grid(column=1, row=1, sticky="e")
		
		#falta apenas puxar os dados das entrys, em uma nova janela (ou não)
		def remover_item_do_banco():
			import sqlite3
			from business.estoque_business import EstoqueBusiness

			
		btn_remover_item_do_banco = Button(master, text = "Remover Item", command = remover_item_do_banco)
		btn_remover_item_do_banco.grid(column=1, row=2, sticky="e")
		
		
root = Tk()

w=400
h=200	
(x,y)=xy_screen(w,h)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconbitmap(resource_path("box.ico"))	
app=Application(master=root)
app.mainloop()