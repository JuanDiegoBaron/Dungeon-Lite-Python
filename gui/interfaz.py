from tkinter import *

class Interfaz:

	def __init__(self, root):

		self.root = root

		self.ventanas = {}

		self.bt_salirApp = Button(root,text="X",command=self.salirApp)
		self.bt_salirApp.place(relx=1.0 ,anchor="ne")

	def agregarVentanas(self,ventanas):

		self.ventanas = ventanas	
	
	def setVentanaActual(self,ventana):

		self.ventanaActual = self.ventanas[ventana]
		self.ventanaActual.mostrarVentana()

	# String Ventana
	# Dic informacion	
	def enviarInformacion(self,ventana,informacion):

		# la clave de la ventada destinataria, llama al metodo recibir informacion
		# la informacion debe tener una clave llamada "Mensaje"
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


