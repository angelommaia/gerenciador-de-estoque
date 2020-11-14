# -*- coding: utf-8 -*-
import sqlite3
from tkinter import *
import tkinter.ttk as ttk
from datetime import date

from view.tk_mostrar_banco import mostrar_banco
from view.tk_modificar_banco import adc_item_ao_banco, remover_item_do_banco
from view.tk_recursos_extras import resource_path, xy_screen	

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
		from modelDTO.item import ItemDTO
		from business.estoque_business import EstoqueBusiness
		
		estoque_business = EstoqueBusiness()
		data = estoque_business.obter_todo_estoque()

		for head in headings:
			tree.heading(head, text=head, anchor=CENTER)
			tree.column(head, anchor=CENTER, width=100)
		for row in data:
			tree.insert('', END, values=row)

		def atualizar_dados():
			#atualizar db
			
			#atualizar treeview
			#limpamos a tela
			for i in tree.get_children():
				tree.delete(i)
			#abrimos o banco novamente e pegamos todos os valores
			from modelDTO.item import ItemDTO
			from business.estoque_business import EstoqueBusiness
			
			estoque_business = EstoqueBusiness()
			data = estoque_business.obter_todo_estoque()

			for head in headings:
				tree.heading(head, text=head, anchor=CENTER)
				tree.column(head, anchor=CENTER, width=100)
			for row in data:
				tree.insert('', END, values=row)	

		def remover_item_selecionado():
			#vamos remover o item selecionado no treeview
			ItemAtual = tree.focus()
			lista_ItemAtual = tree.item(ItemAtual)["values"]
			nome_ItemAtual = lista_ItemAtual[1] 
			
			remover_item_do_banco(nome_ItemAtual)
			atualizar_dados()

		def adc_item():
			#jogamos os itens que estao nas entrys no banco
			adc_item_ao_banco(vnome.get(),vpreco.get(),vdesc.get())
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
		
		btn_adc_item_ao_banco = Button(addItemframe, text = "Adicionar Item", command = lambda:[adc_item(), atualizar_dados()])
		btn_adc_item_ao_banco.grid(column=1, row=4, stick="e")
		
		
		#btns
		buttonframe = Frame(root)
		buttonframe.grid(column=4,row=3, columnspan=3, rowspan=1)
		
		btn_mostrar_banco = Button(buttonframe, text = "Mostrar Banco", command = mostrar_banco)
		#btn_limpar_banco = Button(buttonframe, text = "Limpar Banco",bg="red", command = limpar_treeview) #chamar limpar banco q sera feita pelo pessoal do backend	
		btn_remover_item_do_banco = Button(buttonframe, text = "Remover item selecionado", command = remover_item_selecionado)
		
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
root.iconbitmap(resource_path("./assets/box.ico"))	
app=Application(master=root)
app.mainloop()