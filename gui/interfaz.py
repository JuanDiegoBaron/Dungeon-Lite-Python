from tkinter import *
from .partida import Partida
from .menu import Menu
from .ventana import Ventana
from .creacionPersonaje import CreacionPersonaje

class Interfaz:

	def __init__(self, root):

		self.root = root

		self.ventanas = {
			"Menu Principal": Menu(self,self.root,"Menu Principal"),
			"Creacion Personaje": CreacionPersonaje(self,self.root,"Creacion Personaje"),
			"Partida": Partida(self,self.root,"Partida")
			}

		self.ventanaActual = self.ventanas["Menu Principal"]

		self.ventanaActual.mostrarVentana()

		bt_salirApp = Button(root,text="X",command=self.salirApp).place(relx=1.0 ,anchor="ne")

		
	
		
	def enviarInformacion(self,ventana,informacion):

		self.ventanas[ventana].recibirInformacion(informacion)

	def cambiarVentana(self,nuevaVentana):

		self.ventanaActual.ocultarVentana()

		self.ventanaActual = self.ventanas[nuevaVentana]

		self.ventanaActual.mostrarVentana()

	def mostrarVentana(self, ventana):
		
		self.ventanas[ventana].mostrarVentana()

	def ocultarVentana(self, ventana):

		self.ventanas[ventana].cerrarVentana()

	def salirApp(self):
	
		self.root.destroy()		


# root = Tk()  # Creacion de la pantalla 
# root.attributes("-fullscreen",True)
# root.title("DUNGEON LITE") # Establece un titulo a la ventana
# root.resizable(0,0) # Permite agrandar/redimencionar la pantalla 
# root.config(bg="Black")

# interfaz = Interfaz(root)

# interfaz.root.mainloop()


