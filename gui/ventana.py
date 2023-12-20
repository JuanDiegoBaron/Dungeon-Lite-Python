from tkinter import Frame
from abc import ABC, abstractmethod

class Ventana(ABC):

	def __init__(self, interfaz, padre, nombre):

		self.interfaz=interfaz
		self.padre = padre
		self.nombre = nombre

		self.ancho = 1366
		self.alto = 768

		self.colorFondo = "Grey"

		self.posicionX = 0
		self.posicionY = 0

		self.frame = Frame(self.padre,width=self.ancho,height=self.alto,bg=self.colorFondo)

		self.widgets = []

	@abstractmethod
	def recibirInformacion(self,informacion):
		pass

	def mostrarVentana(self):

		self.frame.place(x=self.posicionX,y=self.posicionY)

	def ocultarVentana(self):
	
		self.frame.place_forget()




