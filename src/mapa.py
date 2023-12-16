from tkinter import PhotoImage

class Mapa:

	def __init__(self):

		self.id=0
		self.x=0
		self.y=0
		self.zona="Amistosa" # zonas: Amistosa(0% aparicion enemigo),Neutral(25% aparicion enemigo),Hostil(50% aparicion enemigo)

		# IMAGENES MAPA
		self.imagenMapa=PhotoImage(file="assets/images/mapaDungeonLite.png")
		self.imagenFondoMapa=PhotoImage(file="assets/images/fondoMapa.png")
		self.pj=PhotoImage(file="assets/images/pj.png")

	def calcularZona(self):

		if(self.x < 100 and self.x > -220 and self.y < 100 and self.y > -200):

			print("Zona verde")
			self.zona="Amistosa"
			Label(partida.frameMapa,text="verde").place(x=0,y=100)

		#ZONAS HOSTILES
		elif(self.x < -380 and self.x > -680 and self.y < -60 and self.y > -300
			or self.x < -720 and self.x > -860 and self.y < 100 and self.y > 20
			or self.x < -860 and self.x > -1080 and self.y < 100 and self.y > 20
			or self.x < -1000 and self.x > -1080 and self.y < -80 and self.y > -160
			or self.x < -960 and self.x > -1080 and self.y < -200 and self.y > -400
			or self.x < -700 and self.x > -840 and self.y < -80 and self.y > -260
			or self.x < -380 and self.x > -500 and self.y < -440 and self.y > -560
			or self.x < -260 and self.x > -500 and self.y < -660 and self.y > -700
			or self.x < -360 and self.x > -520 and self.y < -420 and self.y > -580 
			or self.x < -800 and self.x > -920 and self.y < -600 and self.y > -720):

			print("Zona roja")
			self.zona="Hostil"
			Label(partida.frameMapa,text="Roja").place(x=0,y=100)

		else:

			print("Zona amarilla")
			self.zona="Neutral"
			Label(partida.frameMapa,text="amarilla").place(x=0,y=100)		

	def dibujarMapa(self,framePrincipal):

		Label(framePrincipal,image=self.imagenFondoMapa).place(x=0,y=0)
		Label(framePrincipal,image=self.imagenMapa).place(x=self.x,y=self.y)
		Label(framePrincipal,image=self.pj).place(x=100,y=100)

	def registrarMapa(self):

		conexion=connect("DungeonLiteDB.db")

		cursor=conexion.cursor()

		consulta="INSERT INTO Mapas (idMapa,x,y) VALUES (NULL,?,?)"

		valores=(self.x,self.y)

		cursor.execute(consulta,valores)

		print("se registro el mapa con exito")

		conexion.commit()

		consulta="SELECT idMapa FROM Mapas ORDER BY idMapa DESC LIMIT 1"
		cursor.execute(consulta)

		ultimoId=cursor.fetchone()

		self.id=ultimoId[0]

		conexion.close()

	# VERIFICA SI EL SIGUIENTE MOVIMIENTO COLICIONA, 
	# return bool
	def coliciona(self,x,y,direccion):
		
		#BORRAR PARA QUE HAYAN COLICIONES
		return False

		if(direccion=="arriba"):
			y+=20
		elif(direccion=="abajo"):
			y-=20
		elif(direccion=="derecha"):
			x-=20
		else:
			if(direccion=="izquierda"):
				x+=20			

		#coliciones borde del mapa
		if(y>100 or x>100 or y<-1080 or x<-1080 ):
			return True	

		# Coliciones dentro del mapa (Individuales)
		if(x==80 and y==-200):
			return True

		# Coliciones dentro del mapa (rangos)
		
		# coliciones castillo 
		if(y==100 and x<=100 and x>=-220):
			return True
		elif(x==100 and y<=80 and y>=-200):
			return True
		elif(y==-200 and x<=40 and x>=-220):
			return True
		elif(x==-220 and y>=-180 and y<=-60):
			return True
		elif(x==-220 and y>=-20 and y<=80):
			return True
		elif(x==-140 and y<=80 and y>=-120):
			return True
		elif(y==-120 and x>=-120 and x<=20):
			return True
		elif(y==20 and x>=-120 and x<=40):
			return True
		elif(x==40 and y<=0 and y>=-60):
			return True
		elif(y==-40 and x<=20 and x>=-80):
			return True									
		
		# Lago chieko
		if(x==-380 and y==100):
			return True
		if(x==-400 and y==80):
			return True 
		if(x==-400 and y==60):
			return True 
		if(x==-420 and y==40):
			return True 
		if(x==-440 and y==40):
			return True
		if(y==20 and x<=-460 and x>=-540):
			return True		
		if(x==-720 and y==20):
			return True	
		if(x==-740 and y==40):
			return True	
		if(x==-740 and y==60):
			return True	
		if(y==0 and x>=-860 and x<=-560):
			return True	
		if(x==-720 and y==80):
			return True
		if(x==-700 and y==100):
			return True	

	def mover(self,direccion,partida):


		if(self.coliciona(self.x,self.y,direccion) or partida.precaucionEnem or partida.precaucionRecom or partida.personaje.movimientos==0):
			return
		else:

			if(direccion=="arriba"):

				self.y+=20

			elif(direccion=="abajo"):

				self.y-=20

			elif(direccion=="derecha"):
			
				self.x-=20

			elif(direccion=="izquierda"):
			
				self.x+=20		

			#reseteo de las imagenes de recompenza
			partida.nivelCofre=Label(partida.frameRecompenza,image=e0).place(x=110,y=30)
			partida.imagenCofre=Label(partida.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)

			partida.aumentarHora(1)

			# self.calcularZona()

			partida.personaje.movimientos-=1
			partida.personaje.celdasAvanzadas+=1
			partida.crearFrameSuperior()

			Label(partida.framePrincipal,text=f"{partida.personaje.movimientos} celdas \ndisponibles",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1260,y=430)

			partida.probabilidadTesoro()
			
			Label(partida.frameMapa,image=self.imagenFondoMapa).place(x=0,y=0)
			Label(partida.frameMapa,image=self.imagenMapa).place(x=self.x,y=self.y)
			Label(partida.frameMapa,image=self.pj).place(x=100,y=100)
			Label(partida.framePrincipal,text=f"{self.x}    ",font=("Arial",15),bg="#2A2A2A",fg="white").place(x=1170,y=730)
			Label(partida.framePrincipal,text=f"{self.y}    ",font=("Arial",15),bg="#2A2A2A",fg="white").place(x=1270,y=730)

