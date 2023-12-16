from Tkinter import Frame

class Ventana():

	def __init__(self, padre, nombre, ancho, alto, colorFondo, posicionX, posicion Y):

		self.padre = padre
		self.nombre = nombre

		self.alto = alto
		self.ancho = ancho

		self.colorFondo = colorFondo

		self.posicionX = posicionX
		self.posicionY = posicionY

		self.frame = Frame(self.padre,width=ancho,height=alto)

		self.widgets = []

	def cerrarVentana(self):
	
		self.frame.forgetplace()	


