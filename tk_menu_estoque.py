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
		
		def mostrar_banco():
			import sqlite3
			my_conn = sqlite3.connect('./banco.db')
			r_set = my_conn.execute('''SELECT * from estoque LIMIT 0,20''');
			newWindow = Toplevel()
			i = 0
			for estoque in r_set: 
				for j in range(len(estoque)):
					e = Entry(newWindow, width=15, fg='blue') 
					e.grid(row=i, column=j) 
					e.insert(END, estoque[j])
				i=i+1
		btn_mostrar_banco = Button(master, text = "Mostrar Banco", command = mostrar_banco)
		btn_mostrar_banco.grid(column=1, row=3, sticky="e")
		
		#falta apenas puxar os dados das entrys, em uma nova janela (ou não)
		def adc_item_ao_banco():
			import sqlite3
			from business.estoque_business import EstoqueBusiness
			estoque_business = EstoqueBusiness()
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
		btn_adc_item_ao_banco.grid(column=1, row=2, sticky="e")
root = Tk()

w=400
h=200	
(x,y)=xy_screen(w,h)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconbitmap(resource_path("box.ico"))	
app=Application(master=root)
app.mainloop()