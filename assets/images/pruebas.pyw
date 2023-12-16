# from tkinter import *

# root = Tk()

# 
		
from random import choice,choices,randint			
from tkinter import *

# Crear la ventana principal
raiz = Tk()
raiz.config(bg="red",width=300,height=300)


celdaMuro=PhotoImage(file="celdaMuro.png")
celdaCamino=PhotoImage(file="celdaCamino.png")

# 7 tipos
celdaLlanura=PhotoImage(file="celdaLlanura.png")
celdaAgua=PhotoImage(file="celdaAgua.png")
celdaCasa=PhotoImage(file="celdaCasa.png")
celdaCueva=PhotoImage(file="celdaCueva.png")
celdaBosque=PhotoImage(file="celdaBosque.png")
celdaMontaña=PhotoImage(file="celdaMontaña.png")
celdaCastillo=PhotoImage(file="celdaCastillo.png")
celdaVacia=PhotoImage(file="celdaVacia.png")

class Mapa():

	def __init__(self):

		self.ancho=225
		self.alto=225
		self.grid=[]
		self.row=9
		self.col=9

		self.tipoCeldas = {   # Y Sus adyasentes
			"Llanura":["Llanura","Bosque","Agua","Montaña","Cueva","Casa","Castillo"],#
			"Bosque":["Llanura","Bosque","Agua","Montaña","Cueva","Casa","Castillo"],
			"Agua":["Llanura","Bosque","Agua"],
			"Montaña":["Llanura","Bosque","Montaña","Cueva","Castillo"],
			"Cueva":["Llanura","Bosque","Montaña"],
			"Casa":["Llanura","Bosque","Agua"],
			"Castillo":["Llanura","Bosque","Montaña","Agua"]
		}

		self.densidades = { 
			"Llanura":70,
			"Bosque":50,
			"Agua":40,
			"Montaña":25,
			"Cueva":5,
			"Casa":10,
			"Castillo":5
		}

		self.x=4 # punto medio (personaje)
		self.y=4	

		self.mapa=Frame(raiz,width=self.ancho,height=self.alto,bg="blue")
		self.mapa.place(x=0,y=0)	

		self.generar()

		self.pj = Frame(self.mapa,width=25,height=25,bg="red").place(x=100,y=100)

	# NO ESTA EN USO
	def celExist(self,x,y):
	
		for i in self.grid:

			if(i.x==x and i.y==y):

				aux=True
			else:
				aux=False

		return aux				

	def verificarTipo(self,tipo):

		if(tipo in self.tipoCeldas):

			return self.tipoCeldas[tipo]	

	def calcularDensidad(self,listaTipos):

		densidades = []

		for i in listaTipos:

			densidades.append(self.densidades[i])

		# print(densidades)
		return densidades	

	# se ejecuta varias veces dentro de generar() pero despues nunca mas
	def calcularTipoCelda(self,x,y):

		# primer fila, solo se busca la celda anterior (ESTO ANDA BIEN)
		if(y==0):

			# busca la celda anterior y la guarda en la variable
			for celda in self.grid:


				if(celda.x == x-1 and celda.y == y):

					# print(f"({celda.x}-{celda.y}), es la celda anterior")
					tipoAnterior = celda.tipo	

			if(tipoAnterior=="Llanura"):

				tipo = self.calcularProbabilidad(["Llanura","Bosque","Agua","Montaña","Cueva","Casa","Castillo"],[40,20,10,10,10,5,5])
				return tipo

			elif(tipoAnterior=="Bosque"):	

				tipo = self.calcularProbabilidad(["Llanura","Bosque","Agua","Montaña","Cueva","Casa","Castillo"],[20,40,10,10,10,5,5])
				return tipo

			elif(tipoAnterior=="Agua"):	

				tipo = self.calcularProbabilidad(["Llanura","Bosque","Agua"],[20,20,60])
				return tipo

			elif(tipoAnterior=="Montaña"):	

				tipo = self.calcularProbabilidad(["Llanura","Bosque","Montaña","Cueva","Castillo"],[15,15,50,10,10])
				return tipo	

			elif(tipoAnterior=="Cueva"):	

				tipo = self.calcularProbabilidad(["Llanura","Bosque","Montaña"],[25,25,50])
				return tipo

			elif(tipoAnterior=="Casa"):	

				tipo = self.calcularProbabilidad(["Llanura","Bosque","Agua"],[65,30,5])
				return tipo

			elif(tipoAnterior=="Castillo"):	

				tipo = self.calcularProbabilidad(["Llanura","Bosque","Montaña","Agua"],[40,40,10,10])
				return tipo			

		# segunda fila y siguientes, se busca la celda superior, superior derecha e izquierda y la izquierda
		elif(y>=1):

			# si esta en la primera columna, no tiene celda a la izquierda
			if(x==0):

				# print("X == 0")

				for celda in self.grid:

					# verifica si la celda es la superior
					if(celda.x == x and celda.y == y-1):

						# print(f"({celda.x}-{celda.y}), es la celda superior")
						tipoSuperior = celda.tipo

					#verifica si la celda es la superior derecha
					if(celda.x == x+1 and celda.y == y-1):
						
						# print(f"({celda.x}-{celda.y}), es la celda superior derecha")
						tipoSuperiorDerecha = celda.tipo

				tipo1 = self.verificarTipo(tipoSuperior)
				tipo2 = self.verificarTipo(tipoSuperiorDerecha)

				tipo = list(set(tipo1).intersection(tipo2))
				dens = self.calcularDensidad(tipo)
			
				tipo = self.calcularProbabilidad(tipo,dens)
				
				return tipo	

			# verificacion casi completa
			elif(x == 8):

				for celda in self.grid:

					# anterior
					if(celda.x == x-1 and celda.y == y):

						tipoAnterior= celda.tipo

					# Superior izquierda
					if(celda.x == x-1 and celda.y == y-1):

						tipoSuperiorIzquierda= celda.tipo

					# superior
					if(celda.x == x and celda.y == y-1):

						tipoSuperior= celda.tipo

				tipo1 = self.verificarTipo(tipoAnterior)
				tipo2 = self.verificarTipo(tipoSuperiorIzquierda)
				tipo3 = self.verificarTipo(tipoSuperior)

				tipo = list(set(tipo1).intersection(tipo2, tipo3))

				dens = self.calcularDensidad(tipo)
			
				# print(tipo, ", ", dens)
				tipo = self.calcularProbabilidad(tipo,dens)
				
				# print(tipo)
				return tipo

			# verificacion completa
			else:

				for celda in self.grid:

					# anterior
					if(celda.x == x-1 and celda.y == y):

						tipoAnterior= celda.tipo

					# Superior izquierda
					if(celda.x == x-1 and celda.y == y-1):

						tipoSuperiorIzquierda= celda.tipo

					# superior
					if(celda.x == x and celda.y == y-1):

						tipoSuperior= celda.tipo
					
					# superior derecha
					if(celda.x == x+1 and celda.y == y-1):

						tipoSuperiorDerecha = celda.tipo
		
	
			
				tipo1 = self.verificarTipo(tipoAnterior)
				tipo2 = self.verificarTipo(tipoSuperiorIzquierda)
				tipo3 = self.verificarTipo(tipoSuperior)
				tipo4 = self.verificarTipo(tipoSuperiorDerecha)
				
				# print()
				# print("______________________________________________________________")
				# print("X: ",x,"  Y: ",y)
				# print()
				# print("tipo anterior: ",tipoAnterior, "     opciones: ",tipo1)
				# print("tipo Superior Izquierda: ",tipoSuperiorIzquierda, "     opciones: ",tipo2)
				# print("Tipo superior: ",tipoSuperior, "     opciones: ",tipo3)
				# print("tipo superior derecha: ",tipoSuperiorDerecha, "     opciones: ",tipo4)		
				tipo = list(set(tipo1).intersection(tipo2, tipo3, tipo4))
				# print("______________________________________________________________")
				# print(tipo)
				dens = self.calcularDensidad(tipo)
			
				tipo = self.calcularProbabilidad(tipo,dens)
				# print(tipo)
				# print("______________________________________________________________")
				# print()
				
				# print(tipo)
				return tipo

	# se ejecuta 1 vez cuando se crea el mapa
	def generar(self):

		# reseteo las celdas guardadas
		self.grid=[]

		for y in range(0,self.row):

			for x in range(0,self.col):

				# verifica si no existen celdas, para crear la primera,
				if(len(self.grid)==0):

					tipo = self.calcularProbabilidad(["Llanura","Bosque","Agua","Montaña","Casa","Castillo","Cueva"],[40,20,15,10,5,5,5])
					# print("primera celda, (",i,",",j,") tipo:",tipo)
				
				else:

					tipo=self.calcularTipoCelda(x,y)
				

				if(tipo=="Llanura"):
					imagen=celdaLlanura
				elif(tipo=="Bosque"):
					imagen=celdaBosque
				elif(tipo=="Agua"):
					imagen=celdaAgua
				elif(tipo=="Montaña"):
					imagen=celdaMontaña
				elif(tipo=="Casa"):
					imagen=celdaCasa
				elif(tipo=="Castillo"):
					imagen=celdaCastillo
				elif(tipo=="Cueva"):
					imagen=celdaCueva				

				nuevaCelda=Celda(x,y,x*25,y*25,tipo,imagen,self.mapa)	

				self.grid.append(nuevaCelda)

	def calcularProbabilidad(self,opciones,probabilidades):

	    total_probabilidad = sum(probabilidades)
	    probabilidad_normalizada = [p / total_probabilidad for p in probabilidades]

	    resultado = choices(opciones, probabilidad_normalizada)[0]
	    return resultado

	def mover(self,direccion):


		# 1° verificar las celdas que no existen

			# 1° verificar la columna o fila segun la direccion

		# if direccion == "Derecha":

		# 	celdasLimite = [
		# 		{"x":self.x+4,"y":self.y+4,"posX":200,"posY":0},
		# 		{"x":self.x+4,"y":self.y+3,"posX":200,"posY":25},
		# 		{"x":self.x+4,"y":self.y+2,"posX":200,"posY":50},
		# 		{"x":self.x+4,"y":self.y+1,"posX":200,"posY":75},
		# 		{"x":self.x+4,"y":self.y,  "posX":200,"posY":100},
		# 		{"x":self.x+4,"y":self.y+1,"posX":200,"posY":125},
		# 		{"x":self.x+4,"y":self.y+2,"posX":200,"posY":150},
		# 		{"x":self.x+4,"y":self.y+3,"posX":200,"posY":175},
		# 		{"x":self.x+4,"y":self.y+4,"posX":200,"posY":200}]

		# elif direccion == "Izquierda":
		
		# 	celdasLimite = [
		# 		{"x":self.x-4,"y":self.y+4,"posX":0,"posY":0},
		# 		{"x":self.x-4,"y":self.y+3,"posX":0,"posY":25},
		# 		{"x":self.x-4,"y":self.y+2,"posX":0,"posY":50},
		# 		{"x":self.x-4,"y":self.y+1,"posX":0,"posY":75},
		# 		{"x":self.x-4,"y":self.y,  "posX":0,"posY":100},
		# 		{"x":self.x-4,"y":self.y+1,"posX":0,"posY":125},
		# 		{"x":self.x-4,"y":self.y+2,"posX":0,"posY":150},
		# 		{"x":self.x-4,"y":self.y+3,"posX":0,"posY":175},
		# 		{"x":self.x-4,"y":self.y+4,"posX":0,"posY":200}]

		# elif direccion == "Arriba":

		# 	celdasLimite = [
		# 		{"x":self.x+4,"y":self.y+4,"posX":0,"posY":0},
		# 		{"x":self.x+3,"y":self.y+4,"posX":25,"posY":0},
		# 		{"x":self.x+2,"y":self.y+4,"posX":50,"posY":0},
		# 		{"x":self.x+1,"y":self.y+4,"posX":75,"posY":0},
		# 		{"x":self.x,  "y":self.y+4,"posX":100,"posY":0},
		# 		{"x":self.x-1,"y":self.y+4,"posX":125,"posY":0},
		# 		{"x":self.x-2,"y":self.y+4,"posX":150,"posY":0},
		# 		{"x":self.x-3,"y":self.y+4,"posX":175,"posY":0},
		# 		{"x":self.x-4,"y":self.y+4,"posX":200,"posY":0}]

		# elif direccion == "Abajo":

		# 	celdasLimite = [
		# 		{"x":self.x+4,"y":self.y-4,"posX":0,"posY":200},
		# 		{"x":self.x+3,"y":self.y-4,"posX":25,"posY":200},
		# 		{"x":self.x+2,"y":self.y-4,"posX":50,"posY":200},
		# 		{"x":self.x+1,"y":self.y-4,"posX":75,"posY":200},
		# 		{"x":self.x,  "y":self.y-4,"posX":100,"posY":200},
		# 		{"x":self.x-1,"y":self.y-4,"posX":125,"posY":200},
		# 		{"x":self.x-2,"y":self.y-4,"posX":150,"posY":200},
		# 		{"x":self.x-3,"y":self.y-4,"posX":175,"posY":200},
		# 		{"x":self.x-4,"y":self.y-4,"posX":200,"posY":200}]


		# mueve TODAS LAS CELDAS
		for i in self.grid:

			i.mover(direccion)

		

			# 2° segun la columna o fila, buscar las celdas adyasentes

		# 2° crear las celdas que no existen

		# 3° mover todas las celdas, ocultar las que no se ven



	
class Celda():

	def __init__(self,x,y,posX,posY,tipo,imagen,mapa):

		self.x = x
		self.y = y
		self.posX = posX
		self.posY = posY
		self.par = f"({self.x},{self.y})"
		# self.imagen = imagen
		self.tipo = tipo
		self.mapa = mapa

		self.celda=Label(self.mapa,image=imagen)
		self.celda.place(x=posX,y=posY )
	
	def mover(self,direccion):

		# oculta la imagen
		self.celda.place_forget()

		if direccion == "Derecha":
	
			self.posX-=25	

		elif direccion == "Izquierda":
		
			self.posX+=25

		elif direccion == "Arriba":

			self.posY+=25

		elif direccion == "Abajo":

			self.posY-=25

		self.celda.place(x=self.posX,y=self.posY )

		if(self.posY >= 225 or self.posY < 0 or self.posX >= 225 or self.posX < 0):

			self.celda.place_forget()

	def retornarAdyacentes(self,direccion,grid):

		pass


map=Mapa()

bt_izquierda=Button(raiz,text="<--",command=lambda:map.mover("Izquierda")).place(x=220,y=220)
bt_derecha=Button(raiz,text="->>",command=lambda:map.mover("Derecha")).place(x=220,y=240)
bt_arriba=Button(raiz,text="^",command=lambda:map.mover("Arriba")).place(x=200,y=240)
bt_abajo=Button(raiz,text="abajo",command=lambda:map.mover("Abajo")).place(x=200,y=260)

# Iniciar el bucle de eventos
raiz.mainloop()

