from tkinter import *
from ventana import *
from widget import *

class Interfaz:

	def __init__(self, root):

		self.root = root

		self.ventanas = {}

		self.agregarVentana("Menu Principal", 1360, 768, "Blue", 0, 0)
		self.agregarVentana("Creacion Personaje", 1360, 768, "Red", 0, 0)

		bt_salirApp = Button(root,text="X",command=salir).place(x=1350,y=0) 
		
	def agregarVentana(self, nombre, ancho, alto, colorFondo, posicionX, posicion Y):

		self.ventanas.update({nombre}:Ventana(self.root,nombre, ancho, alto, colorFondo, posicionX, posicionY))


	def mostrarVentana(self, ventana):

		pass
		# ventana.place(x = ventana.x,  y = ventana.y)

	def ocultarVentana(self, ventana):

		pass

	def salirApp(self):
	
		self.root.destroy()		




