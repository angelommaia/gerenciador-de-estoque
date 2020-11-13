#funcao necessaria para gerar o executavel. sem ela, ele nao consegue lidar com o path que eh alocado em %temp% quando o progarama roda
def resource_path(relative_path):
	import subprocess
	import os
	import time
	#""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join(base_path, relative_path)

#funcao criada para definirmos a forma da janela da GUI
def xy_screen(root, w=300, h=200):
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) - (w/2) 
	y = (hs/2) - (h/2)	
	return (x,y)
