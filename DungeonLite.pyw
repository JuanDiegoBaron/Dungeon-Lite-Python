from tkinter import *
from io import open
from random import choice,choices
from random import randint
from sqlite3 import *

""" TAREAS
	* (LISTO) MOVIMIENTO PERSONAJE: (el personaje se tiene que poder mover por el mapa, hacia arriba, abajo ,derecha e izquierda) 
	* TERMINAR EL SISTEMA DE RECOMPENZA 
	
	"""


""" CLASE PARTIDA: 

	* Control de los frames y widgets
	* Control de los objetos
	* Control con la BD

	ATRIBUTOS:
	INT id
	PERSONAJE personaje
	ENEMIGO enemigo
	MAPA mapa
	INT dado1
	INT dado2
	BOOL precaucionEnem
	BOOL precaucionRecom
	INT turno
	INT dia
	INT hora
	INT mes
	INT año
	
	METODOS:


	"""

"""
	PERSONAJE:

	NPCS: CADA NPC TIENE UN NOMBRE, APELLIDO, UNA RAZA, EDAD

	ZONAS:

	*PACIVAS: (0% DE BATALLA) REINOS, BOSQUES VERDES, 
	*NEUTRALES: (50% DE BATALLA) BOSQUES PROFUNDOS, PANTANOS, 
	*HOSTILES : (100% DE BATALLA) CEMENTERIOS, BOSQUES OSCUROS, 

	EDIFICIOS: 
	CASAS:TIENEN DE 0 A N NPCS, O FAMILIA.
	CUEVAS:
	CASTILLOS: DONDE VIVEN LOS REYES, TIENDAS/COMERCIOS, """

#_______________________ CLASES _________________________________
class Partida:

	def __init__(self,personaje):

		self.id=0
		
		self.personaje=personaje

		self.enemigo=Enemigo()

		self.mapa=Mapa()

		self.dado1=0
		self.dado2=0

		self.precaucionEnem=False
		self.precaucionRecom=False

		self.turno=0

		self.dia=0
		self.mes=1
		self.año=347
		self.hora=12

	def comenzarPartida(self):

		self.framePrincipal=Frame(root,width=1366,height=768,bg="#33373A")
		self.framePrincipal.place(x=0,y=0)

		# frame superiora
		self.frameSuperior=Frame(self.framePrincipal,width=1320,height=40,bg="#2A2A2A")
		self.frameSuperior.place(x=5,y=5)

		#LABEL DE INVENTARIO
		Label(self.framePrincipal,text="Inventario",font=("Arial",10),fg="white",bg="#33373A").place(x=5,y=40)
		Label(self.framePrincipal,text="Consola",font=("Arial",10),fg="white",bg="#33373A").place(x=280,y=40)

		self.crearFrameSuperior()

		#frame estadisticas
		self.frameEstadisticas=Frame(self.framePrincipal,width=400,height=140,bg="#2A2A2A")
		self.frameEstadisticas.place(x=30,y=605)

		self.crearFrameEstadisticas()

		# Enemigo
		self.frameEnemigo=Frame(self.framePrincipal,width=500,height=140,bg="red")
		self.frameEnemigo.place(x=610,y=60)

		self.crearFrameEnemigo()


		bt_Salir = Button(self.framePrincipal,text="X",fg="white",bg="#390606",bd="0",width="3",height="1",command=self.salir).place(x="1336",y="1")

		# inventario
		self.txt_Inventario = Text(self.framePrincipal,width=34,height=10,bd=0,bg="#961010",fg="white")
		self.txt_Inventario.place(x=5,y=60)

		self.objetoEDUA=StringVar()

		# entry Equipar/Desequipar/Usar/Activar
		et_edua = Entry(self.framePrincipal,textvariable=self.objetoEDUA,width=3,justify="center",font=("Arial",15),bd=0)
		et_edua.place(x=5,y=220)
		bt_edua = Button(self.framePrincipal,text="Equip/Deseq/Usar/Activar",bg="#390606",width=25,command=self.personaje.EDUA,height=1,bd=0,fg="white")
		bt_edua.place(x=45,y=223)
		bt_infoItem=Button(self.framePrincipal,text="info",bg="#390606",width=5,height=1,bd=0,fg="white")
		bt_infoItem.place(x=230,y=223)

		# Consola
		self.consola=StringVar()

		txt_Consola = Text(self.framePrincipal,width=40,height=10,bd=0,bg="#961010",fg="white")
		txt_Consola.place(x=280,y=60)
		et_consola=Entry(self.framePrincipal,width=40,textvariable=self.consola).place(x=280,y=225)
		bt_consola=Button(self.framePrincipal,text="ejecutar",width=8,bd=0,command=self.ejecutarComando).place(x=535,y=225)

		# Tirar dados
		bt_TirarDados = Button(self.framePrincipal,text="Tirar dados",bg="#390606",width=10,height=2,bd=0,font=("Arial",15),fg="white",command=self.tirarDados).place(x=1115,y=230)

		self.lb_celdasDisponibles=Label(self.framePrincipal,text=f"",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1130,y=290)



		# Cofres / Recompenzas

		self.frameRecompenza=Frame(self.framePrincipal,width=260,height=160,bg="green")
		self.frameRecompenza.place(x=1120,y=60)

		self.lb_recom=Label(self.frameRecompenza,text="",fg="white",bg="green").place(x=20,y=5)
		self.imagenCofre=Label(self.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)
		self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)

		bt_abrir_cofre = Button(self.frameRecompenza,text="Abrir",bg="#40E74F",width=8,height=1,bd=0,font=("Arial",15),fg="white",command=self.abrirCofre).place(x=140,y=100)

		#mapa 

		self.frameMapa=Frame(self.framePrincipal,width=220,height=220)
		self.frameMapa.place(x=1125,y=325)
		self.mapa.dibujarMapa(self.frameMapa)

		bt_moverArriba=Button(self.framePrincipal,width=5,text="⇧",command=lambda:self.mapa.moverArriba(self)).place(x=1218,y=550)
		bt_moverAbajo=Button(self.framePrincipal,width=5,text="⇩",command=lambda:self.mapa.moverAbajo(self)).place(x=1218,y=585)
		bt_moverDerecha=Button(self.framePrincipal,width=5,text="⇨",command=lambda:self.mapa.moverDerecha(self)).place(x=1285,y=550)
		bt_moverIzquierda=Button(self.framePrincipal,width=5,text="⇦",command=lambda:self.mapa.moverIzquierda(self)).place(x=1150,y=550)

	def registrarPartida(self):	
		
		conexion=connect("DungeonLiteDB.db")

		cursor=conexion.cursor()

		consulta="INSERT INTO PARTIDAS (idPartida,idPersonaje,idMapa,idEnemigo,turno) VALUES (NULL,?,?,?,?)"

		valores=(self.personaje.id,self.mapa.id,self.enemigo.id,self.turno)

		cursor.execute(consulta,valores)

		print("partida guardada con exito")

		conexion.commit()

		conexion.close()

	def crearFrameEnemigo(self):

		self.frameEnemigo.destroy()

		self.frameEnemigo=Frame(self.framePrincipal,width=500,height=160,bg="red")
		self.frameEnemigo.place(x=610,y=60)

		lb_fila1Enemigo=Label(self.frameEnemigo,text=f"{self.enemigo.nombre}",bg="red",font=("Arial",15),fg="white").place(x=130,y=5)
		lb_fila1=Label(self.frameEnemigo,text=f"Lvl:{self.enemigo.nivel} exp{self.enemigo.expRecom}",bg="red",font=("Arial",15),fg="white").place(x=330,y=5)
		lb_vidaEnemigo=Label(self.frameEnemigo,text=f"Vida:{self.enemigo.vida}",bg="red",font=("Arial",15),fg="white").place(x=130,y=30)
		lb_dañoEnemigo=Label(self.frameEnemigo,text=f"Daño: {self.enemigo.dañoMin}/{self.enemigo.dañoMax}",bg="red",font=("Arial",15),fg="white").place(x=240,y=30)
		lb_fila3Enemigo=Label(self.frameEnemigo,text=f"Armadura:{self.enemigo.armadura}   Resistencia Magica: {self.enemigo.resistenciaMagica}",bg="red",font=("Arial",15),fg="white").place(x=130,y=55)
		

		bt_luchar=Button(self.frameEnemigo,text="Luchar",bg="#961010",width=20,height=1,bd=0,font=("Arial",12),fg="white").place(x=10,y=120)
		bt_huir=Button(self.frameEnemigo,text="Huir",bg="#961010",width=10,height=1,bd=0,font=("Arial",12),fg="white").place(x=1145,y=150)

		lb_imgCuadroblanco=Label(self.frameEnemigo,image=imagenCuadradoBlanco).place(x=5,y=5)
		lb_imgE0=Label(self.frameEnemigo,image=e0).place(x=100,y=5)

	def crearFrameSuperior(self):
	
		self.frameSuperior.destroy()

		self.frameSuperior=Frame(self.framePrincipal,width=1320,height=40,bg="#2A2A2A")
		self.frameSuperior.place(x=5,y=5)

		# label vida
		Label(self.frameSuperior,image=imagenCorazon,bg="#2A2A2A").place(x=0,y=2)
		Label(self.frameSuperior,text=f"{self.personaje.vida}/{self.personaje.vidaMax}  ",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=50,y=10)
		# label daño
		Label(self.frameSuperior,image=imagenEspada,bg="#2A2A2A").place(x=140,y=2)
		Label(self.frameSuperior,text=f"{self.personaje.dañoMin} - {self.personaje.dañoMax}  ",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=180,y=10)
		# label mana
		Label(self.frameSuperior,image=imagenMana,bg="#2A2A2A").place(x=240,y=2)
		Label(self.frameSuperior,text=f"{self.personaje.mana}/{self.personaje.manaMax}  ",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=280,y=10)
		# label barrera
		Label(self.frameSuperior,image=imagenBarrera,bg="#2A2A2A").place(x=355,y=2)
		Label(self.frameSuperior,text=f"{self.personaje.barrera}",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=395,y=10)
		# label armadura
		Label(self.frameSuperior,image=imagenArmadura,bg="#2A2A2A").place(x=435,y=2)
		Label(self.frameSuperior,text=f"{self.personaje.armadura}",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=475,y=10)
		# oro
		Label(self.frameSuperior,image=imagenOro,bg="#2A2A2A").place(x=520,y=2)
		Label(self.frameSuperior,text=self.personaje.oro,font=("Arial",15),bg="#2A2A2A",fg="white",bd=0).place(x=560,y=10)
		# nombre PJ
		Label(self.frameSuperior,text=self.personaje.nombre,font=("Arial",15),bg="#2A2A2A",fg="white",bd=0).place(x=620,y=10)
		# nivel
		Label(self.frameSuperior,text=f"Nivel {self.personaje.nivel}",font=("Arial",15),bg="#2A2A2A",fg="white",bd=0).place(x=830,y=10)
		# exp
		Label(self.frameSuperior,text=f"{self.personaje.exp} / {self.personaje.sigNivel} XP",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=940,y=10)
		# turno
		Label(self.frameSuperior,text=f"Turno {self.turno}",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=1090,y=10)
		# celda
		Label(self.frameSuperior,text=f"Celdas:{self.personaje.celdasAvanzadas}",font=("Arial",15),bg="#2A2A2A",bd=0,fg="white").place(x=1210,y=10)		
		
	def crearFrameEstadisticas(self):
	
		# estadisticas
		self.frameEstadisticas.destroy()

		self.frameEstadisticas=Frame(self.framePrincipal,width=275,height=500,bg="#2A2A2A")
		self.frameEstadisticas.place(x=5,y=250)

		Label(self.frameEstadisticas,text=f"Fuerza:{self.personaje.fuerza}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=10)
		Label(self.frameEstadisticas,text=f"Aguante:{self.personaje.aguante}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=35)
		Label(self.frameEstadisticas,text=f"Agilidad:{self.personaje.agilidad}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=60)
		Label(self.frameEstadisticas,text=f"Inteligencia:{self.personaje.inteligencia}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=85)
		Label(self.frameEstadisticas,text=f"Magia:{self.personaje.magia}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=110)

		Label(self.frameEstadisticas,text=f"Probabilidad critico: {self.personaje.probabilidadCritico}%   ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=150)
		Label(self.frameEstadisticas,text=f"Daño critico: +{self.personaje.dañoCritico}%   ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=175)
		Label(self.frameEstadisticas,text=f"Daño Magico: {self.personaje.dañoMagico}    ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=200)
		Label(self.frameEstadisticas,text=f"probabilidad evadir: {self.personaje.esquivar}%   ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=225)

		Label(self.frameEstadisticas,text=f"Equipamiento:",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=275)
		cabeza=self.personaje.equipamiento["cabeza"]
		Label(self.frameEstadisticas,text=f"Cabeza: {self.personaje.equipamiento['cabeza']}",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=325)
		pecho=self.personaje.equipamiento["pecho"]
		Label(self.frameEstadisticas,text=f"Pecho: {self.personaje.equipamiento['pecho']}",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=350)
		piernas=self.personaje.equipamiento["piernas"]
		Label(self.frameEstadisticas,text=f"Piernas: {self.personaje.equipamiento['piernas']}",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=375)
		pies=self.personaje.equipamiento["pies"]
		Label(self.frameEstadisticas,text=f"Pies: {self.personaje.equipamiento['pies']}",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=400)
		manoD=self.personaje.equipamiento["mano derecha"]
		Label(self.frameEstadisticas,text=f"Mano Derecha: {self.personaje.equipamiento['mano derecha']}",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=425)
		manoI=self.personaje.equipamiento["mano izquierda"]
		Label(self.frameEstadisticas,text=f"Mano Izquierda: {self.personaje.equipamiento['mano izquierda']}",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=450)

	def aumentarHora(self,horas):

		if(self.hora+horas>=24):
			self.hora=(self.hora+horas)%24
			self.dia+=1
		else:
			self.hora+=horas	

	def tirarDados(self):
	

		if(self.precaucionEnem or self.precaucionRecom or self.personaje.movimientos>0):
			return	
		else:	
			
			self.dado1=choice([1,2,3,4,5,6])

			if(self.dado1==1):
				Label(self.framePrincipal,image=IMG_DADO1).place(x=1240,y=230)
			elif(self.dado1==2):
				Label(self.framePrincipal,image=IMG_DADO2).place(x=1240,y=230)	
			elif(self.dado1==3):
				Label(self.framePrincipal,image=IMG_DADO3).place(x=1240,y=230)
			elif(self.dado1==4):
				Label(self.framePrincipal,image=IMG_DADO4).place(x=1240,y=230)
			elif(self.dado1==5):
				Label(self.framePrincipal,image=IMG_DADO5).place(x=1240,y=230)
			elif(self.dado1==6):
				Label(self.framePrincipal,image=IMG_DADO6).place(x=1240,y=230)

			self.dado2=choice([1,2,3,4,5,6])

			if(self.dado2==1):
				Label(self.framePrincipal,image=IMG_DADO1).place(x=1310,y=230)
			elif(self.dado2==2):
				Label(self.framePrincipal,image=IMG_DADO2).place(x=1310,y=230)	
			elif(self.dado2==3):
				Label(self.framePrincipal,image=IMG_DADO3).place(x=1310,y=230)
			elif(self.dado2==4):
				Label(self.framePrincipal,image=IMG_DADO4).place(x=1310,y=230)
			elif(self.dado2==5):
				Label(self.framePrincipal,image=IMG_DADO5).place(x=1310,y=230)
			elif(self.dado2==6):
				Label(self.framePrincipal,image=IMG_DADO6).place(x=1310,y=230)

			
			self.personaje.movimientos=self.dado1+self.dado2
	
			Label(self.framePrincipal,text=f"{self.personaje.movimientos} celdas disponibles",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1130,y=290)

			self.turno+=1

			self.crearFrameSuperior()

	def calcularProbabilidad(self,opciones,probabilidades):

	    total_probabilidad = sum(probabilidades)
	    probabilidad_normalizada = [p / total_probabilidad for p in probabilidades]

	    resultado = choices(opciones, probabilidad_normalizada)[0]
	    return resultado

	def generarMaterialEspecifico(self,material,cantidad):

		self.personaje.materiales["material"]+=cantidad

	def generarMaterialAleatorio(self,calidad,cantidadMin,cantidadMax):

		global materialesEpicos
		global materialesRaros
		global materialesComunes

		if(calidad=="comun"):

			mat=choice(materialesComunes)
			cant=randint(cantidadMin,cantidadMax)

		elif(calidad=="raro"):

			mat=choice(materialesRaros)
			cant=randint(cantidadMin,cantidadMax)
		else:
			mat=choice(materialesEpicos)
			cant=randint(cantidadMin,cantidadMax)
		
		self.personaje.materiales[mat]+=cant
		print(cant," ",mat," calidad ",calidad)

	def refrescarInventario(self):

		self.txt_Inventario.delete(1.0,END)
		for i in range(0,len(self.personaje.inventario)):
			self.txt_Inventario.insert(1.0,f"{i}) {self.personaje.inventario[i].nombre} (nivel {self.personaje.inventario[i].nivel})\n")

	def generarTesoro(self):
	
		global rareza
		global materialesComunes
		global materialesRaros
		global materialesEpicos

		lvlPj=self.personaje.nivel
		
		# segun el tipo de recompenza se crea un objeto de cada tipo
		tipo=choice(["arma"])#,"armadura","consumible","objeto"])
	
		print("___________________________________________________")

		if(rareza==1):

			# VERIFICA LOS PRIMEROS NIVELES
			if(lvlPj==1):
				nivelItem=1
			elif(lvlPj==2):
				nivelItem=choice([1,2])
			elif(lvlPj==3):
				nivelItem=choice([1,2,3])
			elif(lvlPj==4):
				nivelItem=choice([1,2,3,4])
			else:				
				nivelItem=choice([lvlPj-2,lvlPj-3,lvlPj-4])


			# PROBABILIDAD DE APARICION DE MATERIAL 10%
			probabilidadMaterial=choice([0,0,0,0,0,0,0,0,0,1])
			if(probabilidadMaterial==1):

				# PROBABILIDAD CALIDADES
				calidad=self.calcularProbabilidad(["comun","raro","epico"],[70,25,5])

				if(calidad=="comun"):

					self.generarMaterialAleatorio("comun",1,10)

				elif(calidad=="raro"):
					
					self.generarMaterialAleatorio("raro",1,6)

				else:

					self.generarMaterialAleatorio("epico",1,3)
			
			# PROBABILIDAD DE APARICION DE LLAVE 10%
			probabilidadLlave=choice([0,0,0,0,0,0,0,0,0,1])
			if(probabilidadLlave==1):
				llave=self.calcularProbabilidad([1,2,3],[75,20,5])
				if(llave==1):
					self.personaje.llaves1+=1
					print("conseguiste una llave 1")
				elif(llave==2):
					self.personaje.llaves2+=1
					print("conseguiste una llave 2")
				else:
					self.personaje.llaves3+=1
					print("conseguiste una llave 1")		

			# PROBABILIDAD DE APARICION DE ORO 75% 
			probabilidadOro=choice([0,1,1,1])
			if(probabilidadOro==1):
				oro=randint(0,lvlPj)
				self.personaje.oro+=oro
				print("conseguiste ",oro," de oro")


		elif(rareza==2):
		
			if(lvlPj==1):
				nivelItem=1
			else:
				nivelItem=choice([lvlPj-1,lvlPj,lvlPj+1])

			# PROBABILIDAD DE APARICION DE MATERIAL 25%
			probabilidadMaterial=choice([0,0,0,1])
			if(probabilidadMaterial==1):

				# PROBABILIDAD CALIDADES
				calidad=self.calcularProbabilidad(["comun","raro","epico"],[60,30,10])

				if(calidad=="comun"):

					self.generarMaterialAleatorio("comun",1,15)

				elif(calidad=="raro"):
					
					self.generarMaterialAleatorio("raro",1,9)

				else:

					self.generarMaterialAleatorio("epico",1,5)

			# PROBABILIDAD DE APARICION DE LLAVE 25%
			probabilidadLlave=choice([0,0,0,1])
			if(probabilidadLlave==1):
				llave=self.calcularProbabilidad([1,2,3],[65,25,10])
				if(llave==1):
					self.personaje.llaves1+=1
					print("conseguiste una llave 1")
				elif(llave==2):
					self.personaje.llaves2+=1
					print("conseguiste una llave 2")
				else:
					self.personaje.llaves3+=1
					print("conseguiste una llave 3")

			# PROBABILIDAD DE APARICION DE ORO 25% 
			probabilidadOro=choice([0,0,0,1])
			if(probabilidadOro==1):
				oro=randint(0,lvlPj*2)
				self.personaje.oro+=oro
				print("conseguiste ",oro," de oro")

		elif(rareza==3):
	
			nivelItem=choice([lvlPj+2,lvlPj+3,lvlPj+4])	

			# PROBABILIDAD DE APARICION DE MATERIAL 50%
			probabilidadMaterial=choice([0,1])
			if(probabilidadMaterial==1):

				# PROBABILIDAD CALIDADES
				calidad=self.calcularProbabilidad(["comun","raro","epico"],[50,35,15])

				if(calidad=="comun"):

					self.generarMaterialAleatorio("comun",1,20)

				elif(calidad=="raro"):
					
					self.generarMaterialAleatorio("raro",1,12)

				else:

					self.generarMaterialAleatorio("epico",1,9)

			# PROBABILIDAD DE APARICION DE LLAVE 33%
			probabilidadLlave=choice([0,0,1])
			if(probabilidadLlave==1):
				llave=self.calcularProbabilidad([1,2,3],[50,35,15])
				if(llave==1):
					self.personaje.llaves1+=1
					print("conseguiste una llave 1")
				elif(llave==2):
					self.personaje.llaves2+=1
					print("conseguiste una llave 2")
				else:
					self.personaje.llaves3+=1
					print("conseguiste una llave 3")

			# PROBABILIDAD DE APARICION DE ORO 10% 
			probabilidadOro=choice([0,0,0,0,0,0,0,0,0,1])
			if(probabilidadOro==1):
				oro=randint(0,lvlPj*3)
				self.personaje.oro+=oro
				print("conseguiste ",oro," de oro")

		if(tipo=="arma"):

			#nombre del arma
			prefijos = choice(["Espada", "Hacha", "Daga", "Arco", "Vara", "Martillo", "Lanza", "Cetro","Cimitarra","Latigo","Mazo","Baston"])
			sufijo = choice([" de Guerrero"," de Mago"," de guerra", " oxidada", " del mal"," del bien"," real"," del dragon", " de la oscuridad"," de la luz", " de fuego", " impecable"," de la victoria", " de la codicia", " de la locura", " de la esperanza", " del miedo", " con daños", " del cielo", " infernal"," invernal", " gelido/a"," del amor", " del odio", " del rey", " divino/a"])

			nombre=prefijos+sufijo

			#nivel
			nivelItem

			#daño
			dañoMin=randint(1,nivelItem)
			dañoMax=randint(dañoMin+1,nivelItem*2)

			#manos
			if(prefijos=="Daga" or prefijos=="Vara" or prefijos=="Cetro" or prefijos=="Cimitarra" or prefijos=="Latigo"):

				manos=1
			elif(prefijos=="Lanza" or prefijos=="Arco" or prefijos=="Baston"):

				manos=2
			else:
			
				manos=choice([1,2])	

			#estadisticas
			f=0
			agi=0
			agu=0
			m=0
			intl=0

			aux=randint(1,nivelItem)
			for i in range(0,aux):
				
				stat=choice([1,2,3,4,5])
				if(stat==1):
					f+=1
				elif(stat==2):					
					agu+=1
				elif(stat==3):
					agi+=1
				elif(stat==4):					
					intl+=1
				elif(stat==5):	
					m+=1

			valor=aux*2+manos*10+(dañoMax+dañoMin)

			self.personaje.inventario.append(Arma(nombre,valor,nivelItem,manos,dañoMin,dañoMax,f,agu,agi,intl,m))
			self.refrescarInventario()
			print(nombre,", nivel ",nivelItem," | ",dañoMin,"-",dañoMax," | ",f,"-",agu,"-",agi,"-",intl,"-",m," | $",valor)

		print("___________________________________________________")	

	def abrirCofre(self):

		global rareza

		
		# VEFIRICA SI SE ENCONTRO CON UN COFRE
		if(self.precaucionRecom):

			# VERIFICA SI EL JUGADOR TIENE LLAVES
			if(rareza==1):

				# NO REQUIERE LLAVE
				self.generarTesoro()
				self.precaucionRecom=False

				# reseteo de imagenes
				self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
				self.imagenCofre=Label(self.frameRecompenza,image=imagenCofreAbierto).place(x=20,y=30)
				self.lb_recom=Label(self.frameRecompenza,text="                           ",fg="white",bg="green").place(x=20,y=5)
			
			elif(rareza==2):

				if(self.personaje.llaves1>0):

					self.generarTesoro()
					self.precaucionRecom=False

					# reseteo de imagenes
					self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
					self.imagenCofre=Label(self.frameRecompenza,image=imagenCofreAbierto).place(x=20,y=30)
					self.lb_recom=Label(self.frameRecompenza,text="                           ",fg="white",bg="green").place(x=20,y=5)
				else:

					self.precaucionRecom=False

					# reseteo de imagenes
					self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
					self.imagenCofre=Label(self.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)
					self.lb_recom=Label(self.frameRecompenza,text="                           ",fg="white",bg="green").place(x=20,y=5)

					print("no tienes llaves 1")

			else:

				if(self.personaje.llaves2>0):

					self.generarTesoro()
					self.precaucionRecom=False

					# reseteo de imagenes
					self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
					self.imagenCofre=Label(self.frameRecompenza,image=imagenCofreAbierto).place(x=20,y=30)
					self.lb_recom=Label(self.frameRecompenza,text="                           ",fg="white",bg="green").place(x=20,y=5)
					
				else:
				
					self.precaucionRecom=False

					# reseteo de imagenes
					self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
					self.imagenCofre=Label(self.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)
					self.lb_recom=Label(self.frameRecompenza,text="                           ",fg="white",bg="green").place(x=20,y=5)
	
					print("no tienes llave 2")

		else:
		
			print("no hay cofre")				

	def probabilidadTesoro(self):

		# Probabilidad de aparicion de un cofre
		p=choice([0,1])

		if(p==1):

			# imagen cofre
			self.imagenCofre=Label(self.frameRecompenza,image=imagenCofre).place(x=20,y=30)

			# probabilidad de que sea un cofre * , ** o ***
			global rareza 
			rareza=choice([1,1,1,1,1,1,2,2,2,3])

			if(rareza==1):
				self.lb_recom=Label(self.frameRecompenza,text="no requiere llave",fg="white",bg="green").place(x=20,y=5)
				self.nivelCofre=Label(self.frameRecompenza,image=e1).place(x=110,y=30)
				print("Encontraste un cofre nivel 1")
			elif(rareza==2):
			
				self.lb_recom=Label(self.frameRecompenza,text="requiere llave nivel 1",fg="white",bg="green").place(x=20,y=5)
				self.nivelCofre=Label(self.frameRecompenza,image=e2).place(x=110,y=30)	
				print("Encontraste un cofre nivel 2")
			else:
				self.lb_recom=Label(self.frameRecompenza,text="requiere llave nivel 2",fg="white",bg="green").place(x=20,y=5)
				self.nivelCofre=Label(self.frameRecompenza,image=e3).place(x=110,y=30)
				print("Encontraste un cofre nivel 3")	

			self.precaucionRecom=True

	def probabilidadEnemigo(self):

		aux=choice([1,0,0,0,0,0,0,0,0,0])

		if(aux==1):
			self.precaucionEnem=True
			self.enemigo.generar()
		else:
			self.precaucionEnem=False

	def salir(self):

		self.framePrincipal.destroy()	

	def generarMision(self,tipo):
	
		mision=Mision()

	def ejecutarComando(self):

		print(self.consola.get())

class Personaje:

	def __init__(self,nombre,raza,clase,vida,mana,fuerza,aguante,inteligencia,magia,agilidad,percepcion):

		self.id=0
		self.nombre=nombre
		self.raza=raza
		# self.clase=clase
		self.clase=clase

		self.nivel=1
		self.exp=0
		self.sigNivel=50

		if(self.clase=="Guerrero"):
			self.habilidades=[{"habilidad":"Alzar escudo","coste":10},{"habilidad":"Furia Berserk","coste":40},{"habilidad":"Golpear suelo","coste":25}]
		elif(self.clase=="Mago"):
			self.habilidades=[{"habilidad":"Bola de fuego","coste":10},{"habilidad":"Meteoro","coste":40},{"habilidad":"Escudo de hielo","coste":20}]
		elif(self.clase=="Picaro"):
			self.habilidades=[{"habilidad":"apuñalar","coste":10},{"habilidad":"Robar","coste":20},{"habilidad":"Vueltereta","coste":30}]

		self.vidaMax=vida
		self.vida=vida
		self.manaMax=mana
		self.mana=mana
		self.dañoMin=1
		self.dañoMax=2
		self.barrera=0

		self.puntosDisponibles=0
		self.fuerza=fuerza # cada 4 puntos de fuerza agrega 1 al daño maximo 
		self.inteligencia=inteligencia #cada punto de inteligencia agrega 1 al dañoMagico
		self.magia=magia # 1 de magia = 5 de manaMax
		# self.percepcion=percepcion # Ayuda a persivir emboscadas entre otras
		self.agilidad=agilidad # cada punto de agilidad agrega 1 al esquivar y a probabilidadCritico
		self.aguante=aguante # cada punto de aguante agrega 5 puntos de vida,

		# self.resisMagia=0
		# self.resisToxina=0
		# self.resisFrio=0
		# self.resisFuego=0

		self.armadura=0
		self.probabilidadCritico=agilidad
		self.dañoCritico=100
		self.esquivar=agilidad
		self.dañoMagico=5+inteligencia
		self.estados=[]

		self.celdasAvanzadas=0
		self.movimientos=0

		self.oro=0
		self.inventario=[]
		self.materiales={"Madera":0,"Piedra":0,"Cuero":0,"Tela":0,"Arcilla":0,"Mineral de hierro":0,"Mineral de oro":0,"Hueso":0,"Cristal":0,"Hierro":0,"Oro":0,"Rubi":0,"Zafiro":0,"Esmeralda":0,"Cuero refinado":0,"Tela de calidad":0,"Madera refinada":0,"Piedra refinada":0,"Ladrillo":0,"Alma":0,"Polvo de estrellas":0,"Diamante":0,"Corazon de piedra":0,"Escama de dragon":0,"Flor de fuego":0,"Runa":0}
		self.llaves1=10
		self.llaves2=10
		self.llaves3=10
		self.equipamiento={"cabeza":"vacio","pecho":"vacio","piernas":"vacio","pies":"vacio","mano derecha":"vacio","mano izquierda":"vacio"}

	def registrarPersonaje(self):

		return

		conexion=connect("DungeonLiteDB.db")

		cursor=conexion.cursor()

		consulta="INSERT INTO PERSONAJES (idPersonaje,nombre,raza,clase,nivel,exp,sigNivel,habilidades,vidaMax,vida,manaMax,mana,dañoMin,dañoMax,barrera,puntosDisponibles,fuerza,inteligencia,magia,percepcion,agilidad,aguante,resistenciaMagica,resistenciaToxina,resistenciaFrio,resistenciaFuego,armadura,probabilidadCritico,dañoCritico,esquivar,dañoMagico,inventario,equipamiento,celda,estados,oro,movimientos) VALUES (null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

		valores=(self.nombre,self.raza,self.clase,self.nivel,self.exp,self.sigNivel,str(self.habilidades),self.vidaMax,self.vida,self.manaMax,self.mana,self.dañoMin,self.dañoMax,self.barrera,self.puntosDisponibles,self.fuerza,self.inteligencia,self.magia,self.percepcion,self.agilidad,self.aguante,self.resisMagia,self.resisToxina,self.resisFrio,self.resisFuego,self.armadura,self.probabilidadCritico,self.dañoCritico,self.esquivar,self.dañoMagico,str(self.inventario),str(self.equipamiento),str(self.estados),self.oro)

		cursor.execute(consulta,valores)

		print("PERSONAJE GUARDADO CON EXITO")

		consulta="SELECT idPersonaje FROM Personajes ORDER BY idPersonaje DESC LIMIT 1"
		cursor.execute(consulta)

		ultimoId=cursor.fetchone()

		self.id=ultimoId[0]
		print("personaje ultimoId: ", ultimoId[0])

		conexion.commit()
		conexion.close()

	def aumentarXP(self,XP):

		self.exp+=XP

	def calcSiguienteNivel(self):

		self.sigNivel+=sigNivel*0.5

	def EDUA(self):

		if(type(partida.personaje.inventario[int(partida.objetoEDUA.get())])==Arma):
			
			partida.personaje.inventario[int(partida.objetoEDUA.get())].equiparDesequipar()
			partida.crearFrameEstadisticas()

class Mapa:

	def __init__(self):

		self.id=0
		self.x=0
		self.y=0

		# IMAGENES MAPA
		self.imagenMapa=PhotoImage(file="imagenes/mapaDungeonLite.png")
		self.imagenFondoMapa=PhotoImage(file="imagenes/fondoMapa.png")
		self.pj=PhotoImage(file="imagenes/pj.png")

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

	# moverArriba mueve el personaje si cumple con las condiciones
	# que no coliciona, que no haya un enemigo y que tenga movimientos disponibles
	def moverArriba(self,partida):

		if(self.coliciona(self.x,self.y,"arriba") or partida.precaucionEnem or partida.precaucionRecom or partida.personaje.movimientos==0):
			return
		else:	

			#reseteo de las imagenes de recompenza
			partida.nivelCofre=Label(partida.frameRecompenza,image=e0).place(x=110,y=30)
			partida.imagenCofre=Label(partida.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)


			partida.personaje.movimientos-=1
			partida.personaje.celdasAvanzadas+=1

			Label(partida.framePrincipal,text=f"{partida.personaje.movimientos} celdas disponibles",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1130,y=290)
			self.y+=20

			partida.probabilidadTesoro()
			
			Label(partida.frameMapa,image=self.imagenFondoMapa).place(x=0,y=0)
			Label(partida.frameMapa,image=self.imagenMapa).place(x=self.x,y=self.y)
			Label(partida.frameMapa,image=self.pj).place(x=100,y=100)

	# moverArriba mueve el personaje si cumple con las condiciones
	# que no coliciona, que no haya un enemigo y que tenga movimientos disponibles
	def moverAbajo(self,partida):


		if(self.coliciona(self.x,self.y,"abajo") or partida.precaucionEnem or partida.precaucionRecom or partida.personaje.movimientos==0):
			return
		else:

			#reseteo de las imagenes de recompenza
			partida.nivelCofre=Label(partida.frameRecompenza,image=e0).place(x=110,y=30)
			partida.imagenCofre=Label(partida.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)

			partida.personaje.movimientos-=1
			partida.personaje.celdasAvanzadas+=1

			Label(partida.framePrincipal,text=f"{partida.personaje.movimientos} celdas disponibles",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1130,y=290)

			self.y-=20

			partida.probabilidadTesoro()

			Label(partida.frameMapa,image=self.imagenFondoMapa).place(x=0,y=0)
			Label(partida.frameMapa,image=self.imagenMapa).place(x=self.x,y=self.y)
			Label(partida.frameMapa,image=self.pj).place(x=100,y=100)

	# moverArriba mueve el personaje si cumple con las condiciones
	# que no coliciona, que no haya un enemigo y que tenga movimientos disponibles
	def moverDerecha(self,partida):

		if(self.coliciona(self.x,self.y,"derecha") or partida.precaucionEnem or partida.precaucionRecom or partida.personaje.movimientos==0):
			return
		else:

			#reseteo de las imagenes de recompenza
			partida.nivelCofre=Label(partida.frameRecompenza,image=e0).place(x=110,y=30)
			partida.imagenCofre=Label(partida.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)

			partida.personaje.movimientos-=1
			partida.personaje.celdasAvanzadas+=1

			Label(partida.framePrincipal,text=f"{partida.personaje.movimientos} celdas disponibles",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1130,y=290)

			self.x-=20

			partida.probabilidadTesoro()
			
			Label(partida.frameMapa,image=self.imagenFondoMapa).place(x=0,y=0)
			Label(partida.frameMapa,image=self.imagenMapa).place(x=self.x,y=self.y)
			Label(partida.frameMapa,image=self.pj).place(x=100,y=100)

	# moverArriba mueve el personaje si cumple con las condiciones
	# que no coliciona, que no haya un enemigo y que tenga movimientos disponibles
	def moverIzquierda(self,partida):

		if(self.coliciona(self.x,self.y,"izquierda") or partida.precaucionEnem or partida.precaucionRecom or partida.personaje.movimientos==0):
			return
		else:

			#reseteo de las imagenes de recompenza
			partida.nivelCofre=Label(partida.frameRecompenza,image=e0).place(x=110,y=30)
			partida.imagenCofre=Label(partida.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)

			partida.personaje.movimientos-=1
			partida.personaje.celdasAvanzadas+=1

			Label(partida.framePrincipal,text=f"{partida.personaje.movimientos} celdas disponibles",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1130,y=290)

			self.x+=20

			partida.probabilidadTesoro()

			Label(partida.frameMapa,image=self.imagenFondoMapa).place(x=0,y=0)
			Label(partida.frameMapa,image=self.imagenMapa).place(x=self.x,y=self.y)
			Label(partida.frameMapa,image=self.pj).place(x=100,y=100)

class Enemigo:

	def __init__(self):

		self.id=0
		self.tipo="" # Jefe / Subjefe / Esbirro
		self.nombre="El rey exanime"
		self.nivel=100
		self.dañoMin=0
		self.dañoMax=0
		self.dañoMagico=0
		self.vidaMax=0
		self.vida=0
		self.armadura=0
		self.resistenciaMagica=0
		self.expRecom=100
		self.oroRecom=0
		self.estados=""

	def generar(self):

		aux=choice([1,1,1,1,1,2,2,2,3,3])

		if(aux==1):

			Label(partida.frame,image=enem2).place(x=785,y=80)


		


	def registrarEnemigo(self):
	
		conexion=connect("DungeonLiteDB.db")

		cursor=conexion.cursor()

		consulta="INSERT INTO Enemigos (idEnemigo,nombre,nivel,dañoMin,dañoMax,vidaMax,vida,armadura,resistenciaMagica,estados) VALUES (NULL,?,?,?,?,?,?,?,?,?)"

		valores=(self.nombre,self.nivel,self.dañoMin,self.dañoMax,self.vidaMax,self.vida,self.armadura,self.resistenciaMagica,self.estados)

		cursor.execute(consulta,valores)

		print("se registro el enemigo con exito")

		conexion.commit()

		consulta="SELECT idEnemigo FROM Enemigos ORDER BY idEnemigo DESC LIMIT 1"
		cursor.execute(consulta)

		ultimoId=cursor.fetchone()

		self.id=ultimoId[0]

		conexion.close()

class NPC:

	def __init(self):

		self.nombre
		self.apellido
		self.apodo
		self.nombreCompleto
		self.genero # HOMBRE / MUJER
		self.raza
		self.x
		self.y

	def generarNPC():

		pass
		# NO SE TIENEN QUE HABER NPC CON NOMBRES IGUALES

class Mision:

	def __init__(self,tipo):

		self.id
		self.tipo=tipo # PRINCIPAL / SECUNDARIA
		self.destinos # []
		self.objetios # []
		self.dialogos # [""]
		self.npc #  obj NPC (npc que entrega la mision)
		self.recompenza 
		self.recompenzaOro # entre 10 y 50 oro
		self.estado # EN PROGRESO / RECOMPENZA /TERMINADA

class Edificio:

	def __init__(self):

		self.nombre
		self.tipo # CASA / TIENDA / HERRERIA / IGLESIA / CASTILLO / MAZMORRA / CUEVA
		self.x
		self.y

class Item:

	def __init__(self,nombre,valor,nivel,):

		# PARAMETRO TIPO: se puede poner un tipo en especifico o si se pone "aleatorio" elige un ojeto al azar

		self.id=0
		self.nombre=nombre
		self.valor=valor
		self.nivel=nivel
		self.coleccionItems=[
			{"armadura":
				[
					{"nombre":"Casco de cuero","valor":10,"armadura":5,"set":1,"fuerza":0,"aguante":2,"agilidad":2,"Inteligencia":0,"magia":0,"parte":"cabeza"},
					{"nombre":"Armadura de cuero","valor":25,"armadura":10,"set":1,"fuerza":0,"aguante":4,"agilidad":4,"Inteligencia":0,"magia":0,"parte":"pecho"},
					{"nombre":"Pantalones de cuero","valor":20,"armadura":8,"set":1,"fuerza":0,"aguante":4,"agilidad":4,"Inteligencia":0,"magia":0,"parte":"piernas"},
					{"nombre":"Botas de cuero","valor":10,"armadura":5,"set":1,"fuerza":0,"aguante":2,"agilidad":2,"Inteligencia":0,"magia":0,"parte":"pies"},
					{"nombre":"Casco de hierro","valor":20,"armadura":8,"set":2,"fuerza":0,"aguante":4,"agilidad":0,"Inteligencia":0,"magia":0,"parte":"cabeza"},
					{"nombre":"Armadura de hierro","valor":50,"armadura":20,"set":2,"fuerza":0,"aguante":8,"agilidad":0,"Inteligencia":0,"magia":0,"parte":"pecho"},
					{"nombre":"Pantalones de hierro","valor":40,"armadura":10,"set":2,"fuerza":0,"aguante":8,"agilidad":0,"Inteligencia":0,"magia":0,"parte":"piernas"},
					{"nombre":"Botas de hierro","valor":20,"armadura":8,"set":2,"fuerza":0,"aguante":4,"agilidad":0,"Inteligencia":0,"magia":0,"parte":"pies"},
					{"nombre":"Gorro de mago","valor":10,"armadura":5,"set":3,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":2,"magia":2,"parte":"cabeza"},
					{"nombre":"Tunica de mago","valor":20,"armadura":5,"set":3,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":6,"magia":6,"parte":"pecho"},
					{"nombre":"Pantalones de mago","valor":10,"armadura":5,"set":3,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":3,"magia":3,"parte":"piernas"},
					{"nombre":"Botas de mago","valor":10,"armadura":5,"set":3,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":3,"magia":3,"parte":"pies"},
					{"nombre":"Capucha","valor":10,"armadura":5,"set":4,"fuerza":0,"aguante":0,"agilidad":4,"Inteligencia":0,"magia":0,"parte":"cabeza"},
					{"nombre":"Botas de picaro","valor":10,"armadura":5,"set":4,"fuerza":0,"aguante":0,"agilidad":4,"Inteligencia":0,"magia":0,"parte":"pies"},
					{"nombre":"Escudo de madera","valor":10,"armadura":8,"set":4,"fuerza":2,"aguante":2,"agilidad":0,"Inteligencia":0,"magia":0,"parte":"mano izquierda"},
					{"nombre":"Escudo de hierro","valor":30,"armadura":15,"set":4,"fuerza":2,"aguante":4,"agilidad":0,"Inteligencia":0,"magia":0,"parte":"mano izquierda"}
				]
			},
			{"consumible":
				[
					{"nombre":"Pocion de vida","tipo":"consumible","valor":10,"buf":{"vida":10,"mana":0,"barrera":0}},
					{"nombre":"Pocion de mana","tipo":"consumible","valor":10,"buf":{"vida":0,"mana":10,"barrera":0}},
					{"nombre":"Pocion de barrera","tipo":"consumible","valor":10,"buf":{"vida":0,"mana":0,"barrera":10}}
				]
			},
			{"llave":
				[
					{"nombre":"llave","nivel":1,"valor":25},
					{"nombre":"llave","nivel":2,"valor":50},
					{"nombre":"llave","nivel":3,"valor":100}
				]
			},
		]	

class Arma(Item):

	def __init__(self,nombre,valor,nivel,manos,dañoMinimo,dañoMaximo,fuerza,aguante,agilidad,inteligencia,magia):

		super().__init__(nombre,valor,nivel)
					
		self.manos=manos
		self.dañoMinimo=dañoMinimo
		self.dañoMaximo=dañoMaximo
		self.fuerza=fuerza
		self.aguante=aguante
		self.agilidad=agilidad
		self.inteligencia=inteligencia
		self.magia=magia

	def equiparDesequipar(self):

		if(self.manos==1):

			if(partida.personaje.equipamiento["mano derecha"]=="vacio"):

				partida.personaje.equipamiento["mano derecha"]=self.nombre
				partida.personaje.dañoMin+=self.dañoMinimo
				partida.personaje.dañoMax+=self.dañoMaximo
				partida.personaje.fuerza+=self.fuerza
				partida.personaje.aguante+=self.aguante
				partida.personaje.agilidad+=self.agilidad
				partida.personaje.inteligencia+=self.inteligencia
				partida.personaje.magia+=self.magia

				print("se equipo ",self.nombre)

			if(partida.personaje.equipamiento["mano derecha"]==self.nombre):

				partida.personaje.equipamiento["mano derecha"]="vacio"
				partida.personaje.dañoMin-=self.dañoMinimo
				partida.personaje.dañoMax-=self.dañoMaximo
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

				print("se desequipo ",self.nombre)

class Armadura(Item):

	pass

class Consumible(Item):

	pass

class Objeto(Item):

	pass

class Material(Item):

	def __init__(self):

		self.id
		self.material # Nombre del material
		self.cantidad	

#________________________ Ventana ____________________________

root = Tk()  # Creacion de la pantalla 
root.attributes("-fullscreen",True)
root.title("DUNGEON LITE") # Establece un titulo a la ventana
root.resizable(0,0) # Permite agrandar/redimencionar la pantalla 
root.config(bg="blue")

#__________________________  FRAME MENU _______________________________

def crearFrameNuevaPartida():

	def crearPartida():

		global partidas

		#creacion del objeto del personaje
		if(nombre.get()=="" or razaSeleccionada.get()=="" or claseSeleccionada.get()==""):

			return

		vidaAux=100+int(aguante.get())*5
		manaAux=100+int(inteligencia.get())*5
		personaje=Personaje(nombre.get(),razaSeleccionada.get(),claseSeleccionada.get(),vidaAux,manaAux,int(fuerza.get()),int(aguante.get()),int(inteligencia.get()),int(magia.get()),int(agilidad.get()),int(percepcion.get()))
		# personaje.registrarPersonaje()
		
		# enemigo=Enemigo()
		# enemigo.registrarEnemigo()
		# creacion del objeto de la partida 
		partida=Partida(personaje)

		partida.comenzarPartida()

		# agrego la partida a la coleccion
		# partida.registrarPartida()

		salirNuevaPartida()

	def salirNuevaPartida():

		frameNuevaPartida.destroy()

	# ESTADISTICAS JUGADOR
	
	def subirFuerza():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			fuerza.set(int(fuerza.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarFuerza():
		global puntosDisponibles

		if(int(fuerza.get())==0):
			return
		else:
			puntosDisponibles+=1
			fuerza.set(int(fuerza.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirAguante():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			aguante.set(int(aguante.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarAguante():
		global puntosDisponibles

		if(int(aguante.get())==0):
			return
		else:
			puntosDisponibles+=1
			aguante.set(int(aguante.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirInteligencia():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			inteligencia.set(int(inteligencia.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarInteligencia():
		global puntosDisponibles

		if(int(inteligencia.get())==0):
			return
		else:
			puntosDisponibles+=1
			inteligencia.set(int(inteligencia.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirMagia():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			magia.set(int(magia.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)
			
	def bajarMagia():

		global puntosDisponibles

		if(int(magia.get())==0):
			return
		else:
			puntosDisponibles+=1
			magia.set(int(magia.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirAgilidad():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			agilidad.set(int(agilidad.get())+1)
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def bajarAgilidad():
		global puntosDisponibles

		if(int(agilidad.get())==0):
			return
		else:
			puntosDisponibles+=1
			agilidad.set(int(agilidad.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	def subirPercepcion():
		global puntosDisponibles
			
		if(puntosDisponibles-1<0):
			return
		else:	
			puntosDisponibles-=1
			percepcion.set(int(percepcion.get())+1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)			

	def bajarPercepcion():

		global puntosDisponibles

		if(int(percepcion.get())==0):
			return
		else:
			puntosDisponibles+=1
			percepcion.set(int(percepcion.get())-1)	
			Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

	# Radio-Buttons CLASE

	def seleccionarGuerrero():

		global puntosDisponibles
		puntosDisponibles=5
		Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

		fuerza.set(2)
		aguante.set(2)
		inteligencia.set(0)
		magia.set(0)
		agilidad.set(0)
		percepcion.set(0)

		claseSeleccionada.set("Guerrero")

	def seleccionarMago():	

		global puntosDisponibles
		puntosDisponibles=5
		Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

		fuerza.set(0)
		aguante.set(0)
		inteligencia.set(2)
		magia.set(2)
		agilidad.set(0)
		percepcion.set(0)

		claseSeleccionada.set("Mago")

	def seleccionarPicaro():

		global puntosDisponibles
		puntosDisponibles=5
		Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)

		fuerza.set(0)
		aguante.set(0)
		inteligencia.set(0)
		magia.set(0)
		agilidad.set(2)
		percepcion.set(2)

		claseSeleccionada.set("Picaro")	

	# Radio-Buttons RAZA
	


	nombre=StringVar()
	razaSeleccionada=StringVar()
	claseSeleccionada=StringVar()

	frameNuevaPartida=Frame(root,width=1366,height=768)
	frameNuevaPartida.place(x=0,y=0)

	fondo=Label(frameNuevaPartida,image=fondoMenu)
	fondo.place(x=-5,y=-50)

	bt_SalirFrameNuevaPartida=Button(frameNuevaPartida,text="X",command=salirNuevaPartida).place(x=1350,y=0)
	
	Label(frameNuevaPartida,text="Personaje",font=("Calibri",30)).place(x=100,y=100)
	
	Label(frameNuevaPartida,text="nombre:",font=("Arial",12)).place(x=100,y=200)
	et_nombre=Entry(frameNuevaPartida,width=10,textvariable=nombre).place(x=180,y=200)

	Label(frameNuevaPartida,text="Elija una raza ([1] Humano, [2] Enano, [3] Elfo, [4] Orco)").place(x=100,y=350)
	et_raza=Entry(frameNuevaPartida,width=10,textvariable=razaSeleccionada).place(x=100,y=400)


	Label(frameNuevaPartida,text="Elija una clase (Guerrero,Mago,Picaro)").place(x=100,y=250)
	rb_Guerrero=Radiobutton(frameNuevaPartida,text="Guerrero",variable="claseSeleccionada",value="Guerrero",command=seleccionarGuerrero).place(x=100,y=280)
	rb_Mago=Radiobutton(frameNuevaPartida,text="Mago",variable="claseSeleccionada",value="Mago",command=seleccionarMago).place(x=180,y=280)
	rb_Picaro=Radiobutton(frameNuevaPartida,text="Picaro",variable="claseSeleccionada",value="Picaro",command=seleccionarPicaro).place(x=250,y=280)
	# et_clase=Entry(frameNuevaPartida,width=10,textvariable=clase).place(x=100,y=280)
	# bt_selec=Button(frameNuevaPartida,text="seleccionar",command=selecClass).place(x=230,y=280)

	frameEstadisticas=Frame(frameNuevaPartida,width=200,height=300)
	frameEstadisticas.place(x=100,y=500)

	global puntosDisponibles
	puntosDisponibles=5

	Label(frameEstadisticas,text=f"pts disponibles: {puntosDisponibles}").place(x=5,y=5)
	
	fuerza=StringVar()
	fuerza.set(0)
	aguante=StringVar()
	aguante.set(0)
	inteligencia=StringVar()
	inteligencia.set(0)
	magia=StringVar()
	magia.set(0)
	agilidad=StringVar()
	agilidad.set(0)
	percepcion=StringVar()
	percepcion.set(0)

	et_fuerza=Entry(frameEstadisticas,textvariable=fuerza,width=3,font=("Arial",15))
	et_fuerza.place(x=30,y=30)
	Label(frameEstadisticas,text="Fuerza",font=("Arial",15),fg="black").place(x=60,y=30)
	bt_SubirFuerza=Button(frameEstadisticas,text="+",command=subirFuerza).place(x=10,y=30)
	bt_BajarFuerza=Button(frameEstadisticas,text="-",command=bajarFuerza).place(x=0,y=30)

	et_aguante=Entry(frameEstadisticas,textvariable=aguante,width=3,font=("Arial",15))
	et_aguante.place(x=30,y=60)
	Label(frameEstadisticas,text="Aguante",font=("Arial",15),fg="black").place(x=60,y=60)
	bt_aguante=Button(frameEstadisticas,text="+",command=subirAguante).place(x=10,y=60)
	bt_BajarAguante=Button(frameEstadisticas,text="-",command=bajarAguante).place(x=0,y=60)

	et_inteligencia=Entry(frameEstadisticas,textvariable=inteligencia,width=3,font=("Arial",15))
	et_inteligencia.place(x=30,y=90)
	Label(frameEstadisticas,text="Inteligencia",font=("Arial",15),fg="black").place(x=60,y=90)
	bt_inteligencia=Button(frameEstadisticas,text="+",command=subirInteligencia).place(x=10,y=90)
	bt_BajarInteligencia=Button(frameEstadisticas,text="-",command=bajarInteligencia).place(x=0,y=90)

	et_Magia=Entry(frameEstadisticas,textvariable=magia,width=3,font=("Arial",15))
	et_Magia.place(x=30,y=120)
	Label(frameEstadisticas,text="magia",font=("Arial",15),fg="black").place(x=60,y=120)
	bt_magia=Button(frameEstadisticas,text="+",command=subirMagia).place(x=10,y=120)
	bt_BajarMagia=Button(frameEstadisticas,text="-",command=bajarMagia).place(x=0,y=120)

	et_agilidad=Entry(frameEstadisticas,textvariable=agilidad,width=3,font=("Arial",15))
	et_agilidad.place(x=30,y=150)
	Label(frameEstadisticas,text="Agilidad",font=("Arial",15),fg="black").place(x=60,y=150)
	bt_agilidad=Button(frameEstadisticas,text="+",command=subirAgilidad).place(x=10,y=150)
	bt_BajarAgilidad=Button(frameEstadisticas,text="-",command=bajarAgilidad).place(x=0,y=150)

	et_percepcion=Entry(frameEstadisticas,textvariable=percepcion,width=3,font=("Arial",15))
	et_percepcion.place(x=30,y=180)
	Label(frameEstadisticas,text="Percepcion",font=("Arial",15),fg="black").place(x=60,y=180)
	bt_percepcion=Button(frameEstadisticas,text="+",command=subirPercepcion).place(x=10,y=180)
	bt_BajarPercepcion=Button(frameEstadisticas,text="-",command=bajarPercepcion).place(x=0,y=180)


	bt_CrearPartida=Button(frameNuevaPartida,width=10,text="Crear Personaje",font=("Arial",15),command=crearPartida).place(x=500,y=100)
	

 # CREACION DEL FRAME DEL MENU

def salir():

	frameMenu.destroy()
	root.destroy()

frameMenu=Frame(root,width=1366,height=768,bg="red")
frameMenu.place(x=0,y=0)

fondoMenu=PhotoImage(file="imagenes/fondo.png")
fondo=Label(frameMenu,image=fondoMenu)
fondo.place(x=-5,y=-50)

bt_SalirMenu=Button(frameMenu,text="X",command=salir).place(x=1350,y=0)

bt_NuevaPartida=Button(frameMenu,text="Nueva Partida",font=("Arial",20),fg="black",border=0,bg="#EACB95",command=crearFrameNuevaPartida)
bt_NuevaPartida.place(x=600,y=400)

#____________________________________ VARIABLES GLOBALES______________________________

# SI SE AGREGA UN NUEVO MATERIAL, SE TIENE QUE AGREGAR A LA LISTA DE MATERIALES DEL PERSONAJE personaje.materiales={aqui}
materialesComunes=["Madera","Piedra","Cuero","Tela","Arcilla","Mineral de hierro","Mineral de oro","Hueso","Cristal"]
materialesRaros=["Hierro","Oro","Rubi","Zafiro","Esmeralda","Cuero refinado","Tela de calidad","Madera refinada","Piedra refinada","Ladrillo"]
materialesEpicos=["Alma","Polvo de estrellas","Diamante","Corazon de piedra","Escama de dragon","Flor de fuego","Runa"]


# coleccionArmas=[
# 		{"nombre":"Espada corta","manos":1,"valor":10,"dañoMinimo":1,"dañoMaximo":3,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":0,"magia":0},
# 		{"nombre":"Espada","manos":1,"valor":25,"dañoMinimo":2,"dañoMaximo":4,"fuerza":0,"aguante":1,"agilidad":0,"Inteligencia":0,"magia":0},
# 		{"nombre":"Espada Larga","manos":2,"valor":30,"dañoMinimo":2,"dañoMaximo":6,"fuerza":0,"aguante":2,"agilidad":0,"Inteligencia":0,"magia":0},
# 		{"nombre":"Daga","manos":1,"valor":10,"dañoMinimo":1,"dañoMaximo":4,"fuerza":0,"aguante":0,"agilidad":1,"Inteligencia":0,"magia":0},
# 		{"nombre":"Martillo","manos":1,"valor":10,"dañoMinimo":2,"dañoMaximo":4,"fuerza":1,"aguante":1,"agilidad":0,"Inteligencia":0,"magia":0},
# 		{"nombre":"Martillo de batalla","manos":2,"valor":25,"dañoMinimo":1,"dañoMaximo":6,"fuerza":2,"aguante":1,"agilidad":0,"Inteligencia":0,"magia":0},
# 		{"nombre":"Cimitarra","manos":1,"valor":25,"dañoMinimo":2,"dañoMaximo":4,"fuerza":0,"aguante":0,"agilidad":2,"Inteligencia":0,"magia":0},
# 		{"nombre":"Hacha","manos":1,"valor":20,"dañoMinimo":2,"dañoMaximo":4,"fuerza":1,"aguante":0,"agilidad":0,"Inteligencia":0,"magia":0},
# 		{"nombre":"Hacha de batalla","manos":2,"valor":30,"dañoMinimo":3,"dañoMaximo":6,"fuerza":3,"aguante":0,"agilidad":0,"Inteligencia":0,"magia":0},
# 		{"nombre":"vara","manos":1,"valor":30,"dañoMinimo":1,"dañoMaximo":2,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":1,"magia":2},
# 		{"nombre":"vara arcana","manos":1,"valor":50,"dañoMinimo":2,"dañoMaximo":3,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":3,"magia":2},
# 		{"nombre":"Baston","manos":2,"valor":50,"dañoMinimo":2,"dañoMaximo":4,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":3,"magia":3},
# 		{"nombre":"Libro de hechizos","manos":1,"valor":50,"dañoMinimo":0,"dañoMaximo":0,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":0,"magia":2},
# 		{"nombre":"Esfera de energia","manos":1,"valor":50,"dañoMinimo":0,"dañoMaximo":0,"fuerza":0,"aguante":0,"agilidad":0,"Inteligencia":2,"magia":2}]



# _____________________________________________ IMAGENES ___________________________________________________

imagenOro=PhotoImage(file="imagenes/oro.png")
imagenCofre=PhotoImage(file="imagenes/cofre.png")
imagenCofreAbierto=PhotoImage(file="imagenes/cofreAbierto.png")
imagenCuadradoBlanco=PhotoImage(file="imagenes/noEmenRecom.png")

IMG_DADO1= PhotoImage(file="imagenes/dado1.png")
IMG_DADO2= PhotoImage(file="imagenes/dado2.png")
IMG_DADO3= PhotoImage(file="imagenes/dado3.png")
IMG_DADO4= PhotoImage(file="imagenes/dado4.png")
IMG_DADO5= PhotoImage(file="imagenes/dado5.png")
IMG_DADO6= PhotoImage(file="imagenes/dado6.png")

# iconos estadisticas
imagenCorazon = PhotoImage(file="imagenes/cora.png")
imagenEspada = PhotoImage(file="imagenes/espada.png")
imagenBarrera = PhotoImage(file="imagenes/barrera.png")
imagenArmadura = PhotoImage(file="imagenes/armadura.png")
imagenMana = PhotoImage(file="imagenes/mana.png")

# Estrellas
e0=PhotoImage(file="imagenes/noEstrellas.png")
e1=PhotoImage(file="imagenes/1s.png")
e2=PhotoImage(file="imagenes/2s.png")
e3=PhotoImage(file="imagenes/3s.png")

# Enemigos
enem2=PhotoImage(file="imagenes/esqueleto.png")


# COLECCIONES_________________________________

# COMO GENERAR ITEMS?
# Desde la coleccion base, se toma el nivel del cofre.
# cofre nivel 1: nivel del item entre nivel del jugador-1 hasta -4
# cofre nivel 2: nivel del item entre nivel del jugador-1 hasta +1
# cofre nivel 3: nivel del item entre nivel del jugador+1 hasta +4
# jugador nivel 10: Rangos de item cofre1(8,7,6),cofre2(9,10,11), cofre3(12,13,14)

# __________________MAIN__________________

personaje=Personaje("Kriger","humano","Guerrero",100,100,5,5,5,5,5,5)
		 
partida=Partida(personaje)

partida.comenzarPartida()

root.mainloop()

