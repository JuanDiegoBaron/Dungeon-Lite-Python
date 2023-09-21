# COMO CREAR EVENTOS CON EL TECLADO

# from tkinter import Tk, Label

# # Función para manejar el evento de teclado
# def manejar_teclado(evento):
#     tecla_presionada = evento.keysym
#     etiqueta.config(text="Tecla presionada: " + tecla_presionada)
#     print(tecla_presionada)

# # Crear una ventana
# ventana = Tk()

# # Crear una etiqueta para mostrar la tecla presionada
# etiqueta = Label(ventana, text="Presiona una tecla")
# etiqueta.pack()

# # Asociar el evento de teclado a la función de manejo
# ventana.bind("<Key>", manejar_teclado)

# # Mostrar la ventana
# ventana.mainloop()


# from tkinter import *
# from sqlite3 import *

# class persona:

# 	def __init__(self):

# 		self.nombre="pedro"
# 		self.Apellido="gomez"

# 	def comprar(self,objeto):

# 		print(self.nombre, "compro un/a ",objeto.nombre)

# class objeto:

# 	def __init__(self,nombre):

# 		self.nombre=nombre

# p1=persona()
# obj=objeto("motosicleta")
# p1.comprar(obj)


# root= Tk()

# def agregarNombre():
	
# 	conexion = connect("BDprueba.db")
# 	cursor= conexion.cursor()

# 	consulta= "INSERT INTO nombres (id,nombre) VALUES (NULL,?)"

# 	valor= (nombre.get(),)

# 	cursor.execute(consulta,valor)

# 	conexion.commit()

# 	print("se agrego con exito")

# 	conexion.close()

# def cargarNombres():
	
# 	diccionario={"Nombre":"Diego","Apellido":"Baron"}
# 	print(diccionario)
# 	print(str(diccionario))

# 	conexion = connect("BDprueba.db")
# 	cursor= conexion.cursor()

# 	consulta= "SELECT * FROM nombres"

# 	cursor.execute(consulta)

# 	registros = cursor.fetchall()

# 	text.delete(1.0,END)

# 	for registro in registros:

# 		text.insert(END,f"{registro[1]}\n")

# 	conexion.close()

# frame=Frame(root,width=500,height=500).pack()

# nombre=StringVar()

# entryNombre=Entry(frame,textvariable=nombre).pack()
# bt_agregar=Button(frame,text="agregar",command=agregarNombre).pack()
# bt_cargar=Button(frame,text="cargar",command=cargarNombres).pack()

# text=Text(frame,width=20,height=20)
# text.pack()

# root.mainloop()

class Persona:

	def __init__(self):

		self.nombre="Diego"
		self.Apellido="Baron"

		self.jugar()
		self.estado()

	def jugar(self):
	
		self.jugando=True

	def estado(self):

		print(self.jugando)

diego=Persona()

		