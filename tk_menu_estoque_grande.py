# -*- coding: utf-8 -*-
import sqlite3
from tkinter import *
import tkinter.ttk as ttk
from datetime import date

from telas.tk_mostrar_banco import mostrar_banco
from telas.tk_modificar_banco import adc_item_ao_banco, remover_item_do_banco
from telas.tk_recursos_extras import resource_path, xy_screen	


#GUI
class Application(Frame):
	
	def __init__(self, master=None):
	
		Frame.__init__(self, master)
		self.grid()
		self.master.title("Gerenciamento de Estoque")

		#geometria da tela
		for lin in range(5):
			self.master.rowconfigure(lin, weight=1)    
		for col in range(5):
			self.master.columnconfigure(col, weight=1)
		
		#treeview
		#nao consegui definir uma funcao e dps chamar o delete e add...
		headings = ('Número','Nome','Preço','Descrição','Data de Inclusão')
		
		trvframe = Frame(root)
		trvframe.grid(column=3, row=0,columnspan=3,rowspan=3)
		
		tree = ttk.Treeview(trvframe, show=["headings"])
		tree['columns'] = headings	
		global contador
		contador = 0 		

		with sqlite3.connect('banco.db') as connection:
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM estoque")
			data = (row for row in cursor.fetchall())

		for head in headings:
			tree.heading(head, text=head, anchor=CENTER)
			tree.column(head, anchor=CENTER, width=100)
		for row in data:
			tree.insert('', END, values=row)
			contador=contador+1



		def remover_item_por_nome():
			
			#remover_item_do_banco(vnome.get())
			remover_item_do_banco(str(vnome.get()))
		def atualizar_dados():
			#atualizar db
			adc_item_ao_banco(vnome.get(),vpreco.get(),vdesc.get(),date.today())
			
			#atualizar treeview
			global contador
			contador = contador+1
			tree.insert('', END,values=(contador, vnome.get(),vpreco.get(),vdesc.get(),date.today()))

			
			
		
		#grid
		#adc item
		addItemframe = Frame(root)
		addItemframe.grid(column=0,row=0, columnspan=1, rowspan=4)
		
		lbl_nome = Label(addItemframe,text="Adicionar novo item ao banco").grid(column=0,row=0, columnspan=2)
		
		lbl_nome = Label(addItemframe,text="Nome")
		vnome = Entry(addItemframe, justify = "right", font="tahoma")
		
		lbl_preco = Label(addItemframe,text="Preço")
		vpreco = Entry(addItemframe, justify = "right", font="tahoma")
		
		lbl_desc = Label(addItemframe,text="Descrição")
		vdesc = Entry(addItemframe, justify = "right", font="tahoma")
	
		lbl_nome.grid(column=0, row=1,stick="e")
		vnome.grid(column=1, row=1)
	
		lbl_preco.grid(column=0, row=2, stick="e")
		vpreco.grid(column=1, row=2)
		
		lbl_desc.grid(column=0, row=3, stick="e")
		vdesc.grid(column=1, row=3)
		
		btn_adc_item_ao_banco = Button(addItemframe, text = "Adicionar Item", command = atualizar_dados)
		btn_adc_item_ao_banco.grid(column=1, row=4, stick="e")
		
		
		#btns
		buttonframe = Frame(root)
		buttonframe.grid(column=4,row=3, columnspan=3, rowspan=1)
		
		btn_mostrar_banco = Button(buttonframe, text = "Mostrar Banco", command = mostrar_banco)
		#btn_limpar_banco = Button(buttonframe, text = "Limpar Banco",bg="red", command = limpar_treeview) #chamar limpar banco q sera feita pelo pessoal do backend	
		btn_remover_item_do_banco = Button(buttonframe, text = "Remover item por nome", command = remover_item_por_nome)
		
		btn_mostrar_banco.grid(column=0, row=2, stick="e")
		btn_remover_item_do_banco.grid(column=1, row=2, stick="e")
		#btn_limpar_banco.grid(column=3, row=2, stick="e")
		
		#treeview

		scrolltable = Scrollbar(trvframe, command=tree.yview) 
		tree.configure(yscrollcommand=scrolltable.set)
		scrolltable.grid(column=6, row=0, rowspan=3, stick="ns")
		
		tree.grid(column=3, row=0,columnspan=3,rowspan=3)
		
root = Tk()

#mostar a tela inicial e a deixar centralizada
w=800
h=400	
(x,y)=xy_screen(root,w,h)
#root.state('zoomed')
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconbitmap(resource_path("box.ico"))	
app=Application(master=root)
app.mainloop()