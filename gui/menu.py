from tkinter import *
from .ventana import Ventana

class Menu(Ventana):

	def __init__(self,interfaz,padre,nombre):

		super().__init__(interfaz, padre, nombre)

		self.img_fondo=PhotoImage(file="assets/images/fondo.png")
		self.fondo=Label(self.frame,image=self.img_fondo)
		self.fondo.place(x=-5,y=-50)


		self.bt_NuevaPartida=Button(self.frame,text="Nueva Partida",font=("Arial",20),fg="black",border=0,bg="#EACB95",command=self.crearVentanaCreacionPersonaje)
		self.bt_NuevaPartida.place(x=600,y=400)

	def recibirInformacion(self,informacion):
		pass

	def crearVentanaCreacionPersonaje(self):

		self.interfaz.cambiarVentana("Creacion Personaje")

	
