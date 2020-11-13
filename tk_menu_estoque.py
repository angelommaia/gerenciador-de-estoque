# -*- coding: utf-8 -*-
from tkinter import *
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
		for lin in range(6):
			self.master.rowconfigure(lin, weight=1)    
		for col in range(5):
			self.master.columnconfigure(col, weight=1)
		
		btn_mostrar_banco = Button(master, text = "Mostrar Banco", command = mostrar_banco)
		btn_mostrar_banco.grid(column=1, row=3, sticky="e")
				
		btn_adc_item_ao_banco = Button(master, text = "Adicionar Item", command = adc_item_ao_banco)
		btn_adc_item_ao_banco.grid(column=1, row=1, sticky="e")
		
		btn_remover_item_do_banco = Button(master, text = "Remover Item", command = remover_item_do_banco)
		btn_remover_item_do_banco.grid(column=1, row=2, sticky="e")
		
root = Tk()

#mostar a tela inicial e a deixar centralizada
w=400
h=200	
(x,y)=xy_screen(root,w,h)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconbitmap(resource_path("box.ico"))	
app=Application(master=root)
app.mainloop()