# from mapa import Mapa
# from personaje import Personaje
from tkinter import Frame

class Partida:

	def __init__(self, personaje, mapa):

		self.id=0
		
		self.personaje=personaje

		# self.enemigo=Enemigo()

		self.mapa = mapa

		self.dado1=0
		self.dado2=0

		self.precaucionEnem=False
		self.precaucionRecom=False

		self.turno=0

		self.dia=1
		self.mes=1
		self.año=347
		self.hora=12

		#control frames
		self.estat_expand=True

	def comenzarPartida(self):

		self.framePrincipal=Frame(root,width=1366,height=768,bg="#33373A")
		self.framePrincipal.place(x=0,y=0)

		# frame superiora
		self.frameSuperior=Frame(self.framePrincipal,width=1320,height=40,bg="#2A2A2A")
		self.frameSuperior.place(x=5,y=5)

		self.crearFrameSuperior()

		# frame menu Util
		self.frameMenuUtil=Frame(self.framePrincipal,width=750,height=40,bg="#2A2A2A")
		self.frameMenuUtil.place(x=610,y=60)

		self.crearMenuUtil()

		self.lb_horario=Label(self.frameMenuUtil,text=f"{self.dia}/{self.mes}/{self.año}, {self.hora} hs   ",font=("Arial",15),fg="white",bg="#33373A").place(x=580,y=8)

		#LABEL DE INVENTARIO
		Label(self.framePrincipal,text="Inventario",font=("Arial",10),fg="white",bg="#33373A").place(x=5,y=40)
		Label(self.framePrincipal,text="Consola",font=("Arial",10),fg="white",bg="#33373A").place(x=280,y=40)

		

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
		bt_infoItem=Button(self.framePrincipal,text="info",bg="#390606",width=5,height=1,bd=0,fg="white",command=lambda:self.infoItem(self.objetoEDUA.get()))
		bt_infoItem.place(x=230,y=223)

		# Consola
		self.consola=StringVar()

		self.txt_Consola = Text(self.framePrincipal,width=40,height=10,bd=0,bg="#961010",fg="white")
		self.txt_Consola.place(x=280,y=60)
		et_consola=Entry(self.framePrincipal,width=40,textvariable=self.consola).place(x=280,y=225)
		bt_consola=Button(self.framePrincipal,text="ejecutar",width=8,bd=0,command=self.ejecutarComando).place(x=535,y=225)

		# Tirar dados
		self.bt_TirarDados = Button(self.framePrincipal,text="Tirar dados",bg="#390606",width=10,height=2,bd=0,font=("Arial",15),fg="white",command=self.tirarDados)
		# self.bt_TirarDados.place(x=2015,y=230)

		self.lb_celdasDisponibles=Label(self.framePrincipal,text=f"",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1130,y=290)



		# Cofres / Recompenzas

		self.frameRecompenza=Frame(self.framePrincipal,width=260,height=160,bg="green")
		self.frameRecompenza.place(x=1120,y=100)

		self.lb_recom=Label(self.frameRecompenza,text="",fg="white",bg="green").place(x=20,y=5)
		self.imagenCofre=Label(self.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)
		self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
		

		self.bt_abrir_cofre = Button(self.frameRecompenza,text="Abrir",bg="#40E74F",width=8,height=1,bd=0,font=("Arial",15),fg="white",command=self.abrirCofre)
		self.bt_abrir_cofre.place(x=140,y=100)

		#mapa 

		self.frameMapa=Frame(self.framePrincipal,width=220,height=220)
		self.frameMapa.place(x=1140,y=500)
		self.mapa.dibujarMapa(self.frameMapa)

		# PEQUEÑO FRAME PARA LAS COORDENADAS (se crea una sola vez)
		Frame(self.framePrincipal,width=220,height=40,bg="#2A2A2A").place(x=1140,y=725)
		Label(self.framePrincipal,text="X",fg="white",bg="#2A2A2A").place(x=1150,y=735)
		Label(self.framePrincipal,text="Y",fg="white",bg="#2A2A2A").place(x=1250,y=735)
		

		self.bt_moverArriba=Button(self.framePrincipal,width=5,text="⇧",command=lambda:self.mapa.mover("arriba",self))
		# self.bt_moverArriba.place(x=1218,y=550)
		self.bt_moverAbajo=Button(self.framePrincipal,width=5,text="⇩",command=lambda:self.mapa.mover("abajo",self))
		# self.bt_moverAbajo.place(x=1218,y=585)
		self.bt_moverDerecha=Button(self.framePrincipal,width=5,text="⇨",command=lambda:self.mapa.mover("derecha",self))
		# self.bt_moverDerecha.place(x=1285,y=550)
		self.bt_moverIzquierda=Button(self.framePrincipal,width=5,text="⇦",command=lambda:self.mapa.mover("izquierda",self))
		# self.bt_moverIzquierda.place(x=1150,y=550)

		root.bind("<KeyPress>", self.alPresionaTecla)

	def registrarPartida(self):	
		
		conexion=connect("DungeonLiteDB.db")

		cursor=conexion.cursor()

		consulta="INSERT INTO PARTIDAS (idPartida,idPersonaje,idMapa,idEnemigo,turno) VALUES (NULL,?,?,?,?)"

		valores=(self.personaje.id,self.mapa.id,self.enemigo.id,self.turno)

		cursor.execute(consulta,valores)

		print("partida guardada con exito")

		conexion.commit()

		conexion.close()

	def crearMenuUtil(self):

		self.frameMenuUtil.destroy()

		self.frameMenuUtil=Frame(self.framePrincipal,width=750,height=40,bg="#2A2A2A")
		self.frameMenuUtil.place(x=610,y=60)

		# BOTON MATERIALES, muestra un menu donde se ven todos los materiales y las cantidades
		self.bt_materiales=Button(self.frameMenuUtil,text="Materiales",bg="#2A2A2A",bd=0,fg="white")
		self.bt_materiales.place(x=5,y=8)

		# BOTON CONSTRUIR, muestra un menu de los planos de edificios que pueden crear y los materiales necesarios
		self.bt_construir=Button(self.frameMenuUtil,text="Construir",bg="#2A2A2A",bd=0,fg="white")
		self.bt_construir.place(x=70,y=8)

		# BOTON ELABORAR, muestra un menu con los items que puedas crear y sus materiales.
		self.bt_elaborar=Button(self.frameMenuUtil,text="Elaborar",bg="#2A2A2A",bd=0,fg="white")
		self.bt_elaborar.place(x=135,y=8)

		# BOTON MISIONES, muestra en menu con las misiones, principales y secundarias, el objetivo, y toda la informacion
		self.bt_misiones=Button(self.frameMenuUtil,text="Misiones",bg="#2A2A2A",bd=0,fg="white")
		self.bt_misiones.place(x=190,y=8)

		# BOTON LUGARES, muestra una lista de todos los lugares o edificios visitados y sus coordenadas
		self.bt_lugares=Button(self.frameMenuUtil,text="Lugares",bg="#2A2A2A",bd=0,fg="white")
		self.bt_lugares.place(x=250,y=8)

		# BOTON HABILIDADES
		self.bt_habilidades=Button(self.frameMenuUtil,text="Habilidades",bg="#2A2A2A",bd=0,fg="white")
		self.bt_habilidades.place(x=300,y=8)

		self.lb_horario=Label(self.frameMenuUtil,text=f"{self.dia}/{self.mes}/{self.año}, {self.hora} hs   ",font=("Arial",15),fg="white",bg="#2A2A2A").place(x=580,y=8)


		# 

		# self.bt_=Button(self.frameMenuUtil,text="",bg="#2A2A2A",bd=0,fg="white")
		# self.bt_.place(x=135,y=8)

	def crearFrameEnemigo(self):

		self.frameEnemigo.destroy()

		self.frameEnemigo=Frame(self.framePrincipal,width=500,height=140,bg="red")
		self.frameEnemigo.place(x=610,y=110)

		# lb_fila1Enemigo=Label(self.frameEnemigo,text=f"{self.enemigo.nombre}",bg="red",font=("Arial",15),fg="white").place(x=130,y=5)
		# lb_fila1=Label(self.frameEnemigo,text=f"Lvl:{self.enemigo.nivel} exp{self.enemigo.expRecom}",bg="red",font=("Arial",15),fg="white").place(x=330,y=5)
		# lb_vidaEnemigo=Label(self.frameEnemigo,text=f"Vida:{self.enemigo.vida}",bg="red",font=("Arial",15),fg="white").place(x=130,y=30)
		# lb_dañoEnemigo=Label(self.frameEnemigo,text=f"Daño: {self.enemigo.dañoMin}/{self.enemigo.dañoMax}",bg="red",font=("Arial",15),fg="white").place(x=240,y=30)
		# lb_fila3Enemigo=Label(self.frameEnemigo,text=f"Armadura:{self.enemigo.armadura}   Resistencia Magica: {self.enemigo.resistenciaMagica}",bg="red",font=("Arial",15),fg="white").place(x=130,y=55)
		

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

		self.frameEstadisticas.destroy()

		self.estat_expand=False

		self.frameEstadisticas=Frame(self.framePrincipal,width=100,height=170,bg="#2A2A2A")
		self.frameEstadisticas.place(x=5,y=250)

		self.bt_expan_stats=Button(self.frameEstadisticas,text="˃",command=self.crearFrameEstadisticasExpandido,font=("Arial",15),bd=0,fg="white",bg="#2A2A2A")
		self.bt_expan_stats.place(x=70,y=5)

		Label(self.frameEstadisticas,text="Stats",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=10)

		Label(self.frameEstadisticas,text=f"Fue:{self.personaje.fuerza}",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=20,y=40)
		Label(self.frameEstadisticas,text=f"Agu:{self.personaje.aguante}",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=20,y=65)
		Label(self.frameEstadisticas,text=f"Agi:{self.personaje.agilidad}",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=20,y=90)
		Label(self.frameEstadisticas,text=f"Int:{self.personaje.inteligencia}",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=20,y=115)
		Label(self.frameEstadisticas,text=f"Mag:{self.personaje.magia}",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=20,y=140)

	def crearFrameEstadisticasExpandido(self):
	
		# estadisticas
		self.frameEstadisticas.destroy()

		self.estat_expand=True

		self.frameEstadisticas=Frame(self.framePrincipal,width=275,height=500,bg="#2A2A2A")
		self.frameEstadisticas.place(x=5,y=250)

		self.bt_expan_stats=Button(self.frameEstadisticas,text="˅",command=self.crearFrameEstadisticas,font=("Arial",15),bd=0,fg="white",bg="#2A2A2A")
		self.bt_expan_stats.place(x=250,y=5)

		Label(self.frameEstadisticas,text="Estadisticas",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=10)

		Label(self.frameEstadisticas,text=f"Fuerza:{self.personaje.fuerza}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=40)
		Label(self.frameEstadisticas,text=f"Aguante:{self.personaje.aguante}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=65)
		Label(self.frameEstadisticas,text=f"Agilidad:{self.personaje.agilidad}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=90)
		Label(self.frameEstadisticas,text=f"Inteligencia:{self.personaje.inteligencia}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=115)
		Label(self.frameEstadisticas,text=f"Magia:{self.personaje.magia}",font=("Arial",12),bg="#33373A",bd=0,fg="white").place(x=20,y=140)

		Label(self.frameEstadisticas,text=f"Probabilidad critico: {self.personaje.probabilidadCritico}%   ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=180)
		Label(self.frameEstadisticas,text=f"Daño critico: +{self.personaje.dañoCritico}%   ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=205)
		Label(self.frameEstadisticas,text=f"Daño Magico: {self.personaje.dañoMagico}    ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=230)
		Label(self.frameEstadisticas,text=f"probabilidad evadir: {self.personaje.esquivar}%   ",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=255)

		Label(self.frameEstadisticas,text=f"Equipamiento:",font=("Arial",12),bd=0,bg="#33373A",fg="white").place(x=10,y=305)
		cabeza=self.personaje.equipamiento["cabeza"]
		Label(self.frameEstadisticas,text=f"Cabeza: {self.personaje.equipamiento['cabeza']}",font=("Arial",10),bd=0,bg="#33373A",fg="white").place(x=10,y=355)
		pecho=self.personaje.equipamiento["pecho"]
		Label(self.frameEstadisticas,text=f"Pecho: {self.personaje.equipamiento['pecho']}",font=("Arial",10),bd=0,bg="#33373A",fg="white").place(x=10,y=380)
		piernas=self.personaje.equipamiento["piernas"]
		Label(self.frameEstadisticas,text=f"Piernas: {self.personaje.equipamiento['piernas']}",font=("Arial",10),bd=0,bg="#33373A",fg="white").place(x=10,y=405)
		pies=self.personaje.equipamiento["pies"]
		Label(self.frameEstadisticas,text=f"Pies: {self.personaje.equipamiento['pies']}",font=("Arial",10),bd=0,bg="#33373A",fg="white").place(x=10,y=430)
		manoD=self.personaje.equipamiento["mano derecha"]
		Label(self.frameEstadisticas,text=f"ManoD: {self.personaje.equipamiento['mano derecha']}",font=("Arial",10),bd=0,bg="#33373A",fg="white").place(x=10,y=455)
		manoI=self.personaje.equipamiento["mano izquierda"]
		Label(self.frameEstadisticas,text=f"ManoI: {self.personaje.equipamiento['mano izquierda']}",font=("Arial",10),bd=0,bg="#33373A",fg="white").place(x=10,y=480)

	def alPresionaTecla(self,event):

		tecla=event.keysym
		
		# print(tecla)

		if(tecla == "Up"):

			self.bt_moverArriba.invoke()

		elif(tecla == "Down"):

			self.bt_moverAbajo.invoke()

		elif(tecla == "Left"):
		
			self.bt_moverIzquierda.invoke()

		elif(tecla == "Right"):
		
			self.bt_moverDerecha.invoke()

		elif(tecla=="r"):
		
			self.bt_TirarDados.invoke()	

		elif(tecla=="Return"):

			self.bt_abrir_cofre.invoke()

	def aumentarHora(self,horas):

		ultimoDia=0

		if(self.mes==1 or self.mes==3 or self.mes==5 or self.mes==7 or self.mes==8 or self.mes==10 or self.mes==12):
			ultimoDia=31
		elif(self.mes==4 or self.mes==6 or self.mes==9 or self.mes==11):
			ultimoDia=30
		else:
			ultimoDia=28		

		if(self.hora+horas>=24):
			self.hora=(self.hora+horas)%24
			self.dia+=1

			if(self.dia>ultimoDia):
				self.mes+=1
				self.dia=1
				if(self.mes>12):
					self.año+=1
					self.mes=1
		else:
			self.hora+=horas	

		self.lb_horario=Label(self.frameMenuUtil,text=f"{self.dia}/{self.mes}/{self.año}, {self.hora} hs   ",font=("Arial",15),fg="white",bg="#2A2A2A").place(x=580,y=8)

	def tirarDados(self):
	

		if(self.precaucionEnem or self.precaucionRecom or self.personaje.movimientos>0):
			return	
		else:	
			
			self.dado1=choice([1,2,3,4,5,6])

			if(self.dado1==1):
				Label(self.framePrincipal,image=IMG_DADO1).place(x=1140,y=430)
			elif(self.dado1==2):
				Label(self.framePrincipal,image=IMG_DADO2).place(x=1140,y=430)	
			elif(self.dado1==3):
				Label(self.framePrincipal,image=IMG_DADO3).place(x=1140,y=430)
			elif(self.dado1==4):
				Label(self.framePrincipal,image=IMG_DADO4).place(x=1140,y=430)
			elif(self.dado1==5):
				Label(self.framePrincipal,image=IMG_DADO5).place(x=1140,y=430)
			elif(self.dado1==6):
				Label(self.framePrincipal,image=IMG_DADO6).place(x=1140,y=430)

			self.dado2=choice([1,2,3,4,5,6])

			if(self.dado2==1):
				Label(self.framePrincipal,image=IMG_DADO1).place(x=1200,y=430)
			elif(self.dado2==2):
				Label(self.framePrincipal,image=IMG_DADO2).place(x=1200,y=430)	
			elif(self.dado2==3):
				Label(self.framePrincipal,image=IMG_DADO3).place(x=1200,y=430)
			elif(self.dado2==4):
				Label(self.framePrincipal,image=IMG_DADO4).place(x=1200,y=430)
			elif(self.dado2==5):
				Label(self.framePrincipal,image=IMG_DADO5).place(x=1200,y=430)
			elif(self.dado2==6):
				Label(self.framePrincipal,image=IMG_DADO6).place(x=1200,y=430)

			
			self.personaje.movimientos=self.dado1+self.dado2
	
			Label(self.framePrincipal,text=f"{self.personaje.movimientos} celdas \ndisponibles",font=("Arial",15),bg="#33373A",bd=0,fg="white").place(x=1260,y=430)

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
		self.txt_Consola.insert(1.0,f"{self.turno}) +{cant} {mat}\n")

	def refrescarInventario(self):

		self.txt_Inventario.delete(1.0,END)
		for i in range(0,len(self.personaje.inventario)):
			self.txt_Inventario.insert(1.0,f"{i}) {self.personaje.inventario[i].nombre} ({self.personaje.inventario[i].nivel})\n")

	def generarTesoro(self):
	
		global rareza
		global materialesComunes
		global materialesRaros
		global materialesEpicos

		lvlPj=self.personaje.nivel#randint(1,100)
		
		# segun el tipo de recompenza se crea un objeto de cada tipo
		tipo=choice(["arma","armadura"])#,"consumible","objeto"])
	
		print("___________________________________________________")

		# MATERIALES; LLAVES Y OBJETOS

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
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 1 ({self.personaje.llaves1})\n")
				elif(llave==2):
					self.personaje.llaves2+=1
					print("conseguiste una llave 2")
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 2 ({self.personaje.llaves2})\n")
				else:
					self.personaje.llaves3+=1
					print("conseguiste una llave 1")
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 3 ({self.personaje.llaves3})\n")		

			# PROBABILIDAD DE APARICION DE ORO 75% 
			probabilidadOro=choice([0,1,1,1])
			if(probabilidadOro==1):
				oro=randint(0,lvlPj+3)
				if(oro>0):
					self.personaje.oro+=oro
					print("conseguiste ",oro," de oro")
					self.txt_Consola.insert(1.0,f"{self.turno}) +{oro} de oro ({self.personaje.oro})\n")

			# PROBABILIDAD DE APARICION DE OBJETO
			probabilidadObjeto=choice([0,0,0,0,0,0,0,0,0,1])

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
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 1 ({self.personaje.llaves1})\n")
				elif(llave==2):
					self.personaje.llaves2+=1
					print("conseguiste una llave 2")
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 2 ({self.personaje.llaves2})\n")
				else:
					self.personaje.llaves3+=1
					print("conseguiste una llave 1")
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 3 ({self.personaje.llaves3})\n")

			# PROBABILIDAD DE APARICION DE ORO 25% 
			probabilidadOro=choice([0,0,0,1])
			if(probabilidadOro==1):
				oro=randint(0,lvlPj*2)
				if(oro>0):
					self.personaje.oro+=oro
					print("conseguiste ",oro," de oro")
					self.txt_Consola.insert(1.0,f"{self.turno}) +{oro} de oro ({self.personaje.oro})\n")

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
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 1 ({self.personaje.llaves1})\n")
				elif(llave==2):
					self.personaje.llaves2+=1
					print("conseguiste una llave 2")
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 2 ({self.personaje.llaves2})\n")
				else:
					self.personaje.llaves3+=1
					print("conseguiste una llave 1")
					self.txt_Consola.insert(1.0,f"{self.turno}) conseguiste una llave 3 ({self.personaje.llaves3})\n")

			# PROBABILIDAD DE APARICION DE ORO 10% 
			probabilidadOro=choice([0,0,0,0,0,0,0,0,0,1])
			if(probabilidadOro==1):
				oro=randint(0,lvlPj*3)
				if(oro>0):
					self.personaje.oro+=oro
					print("conseguiste ",oro," de oro")
					self.txt_Consola.insert(1.0,f"{self.turno}) +{oro} de oro ({self.personaje.oro})\n")


		if(tipo=="arma"):

			#nombre del arma
			prefijos = choice(["Espada", "Hacha", "Daga", "Arco","Ballesta","Porra","Vara", "Martillo", "Lanza", "Cetro","Cimitarra","Latigo","Mazo","Baston","Tridente","Mandoble","Espadon","Katana","Baculo","Gladius","Pica","Sable","Alfange","Claymore","Jian","Xiphos","Libro","Orbe","Pergamino","Puñal","Tanto Dori","Waizashi","Pico"])
			
			if(prefijos=="Espada"):
				prefijos+=choice([" corta",""," larga"," bastarda"," ancha"," elfica"," vikinga"])
			elif(prefijos=="Hacha"):
				prefijos+=choice([" doble",""," vikinga"])	
			elif(prefijos=="Lanza"):
				prefijos+=choice([" larga",""," corta"])	
				 
			# sufijos	
			sufijos=["","","",""]

			if(prefijos=="Espada" or prefijos=="Espada corta" or prefijos=="Espada larga" or prefijos=="Martillo" or prefijos=="Espada ancha" or prefijos=="Hacha" or prefijos=="Hacha doble" or prefijos=="Mazo" or prefijos=="Lanza" or prefijos=="Daga"):
				sufijos+=[" de acero"," de hierro"," oxidado/a"]

			if(rareza==1):

				sufijos+=[" con daños"," de plebeyo"," de guerrero"," de mago"," de picaro"," de lacayo"]
			
			elif(rareza==2):

				sufijos+=[" del amor"," del odio"," de escarcha"," de fuego"," de toxina"," electrico"," con daños"," del mal"," del bien"," invernal"," de calor"," venenoza/o"," de rayo"," de calidad"," de la luz"," de la oscuridad"," infernal"," celestial"," real"," de la victoria"," de la codicia"," del miedo"," de la locura"," de la esperanza"]

			elif(rareza==3):
		
				sufijos+=[" bendecida/o"," del amor"," del odio"," de escarcha"," de fuego"," de toxina"," electrico"," con daños"," del mal"," del bien"," invernal"," de calor"," venenoza/o"," de rayo"," de calidad"," de la luz"," de la oscuridad"," infernal"," celestial"," real"," de la victoria"," gelido/a"," de ceniza"," de llamas"," letal"," de la tormenta"," impecable"," profano"," del rey", " divino/a"," del cielo"," del infierno"," del dragon"," de la codicia"," del miedo"," de la locura"," de la esperanza"]

			sufijo=choice(sufijos)



			# EFECTOS SEGUN SUFIJO
			## COMPLETAR

			nombre=prefijos+sufijo

			#nivel
			#nivelItem

			#daño
			dañoMin=randint(1,nivelItem)
			dañoMax=randint(dañoMin+1,nivelItem*2)

			#manos
			if(prefijos=="Daga" or prefijos=="Vara" or prefijos=="Cetro" or prefijos=="Cimitarra" or prefijos=="Latigo" or prefijos=="Gladius"or prefijos=="Sable"or prefijos=="Alfange"or prefijos=="Jian"or prefijos=="Xiphos"or prefijos=="Libro"or prefijos=="Orbe"or prefijos=="Puñal"or prefijos=="Tanto dori"or prefijos=="Wakizashi"):

				manos=1
			elif(prefijos=="Lanza" or prefijos=="Arco" or prefijos=="Baston" or prefijos=="Ballesta" or prefijos=="Tridente" or prefijos=="Mandoble" or prefijos=="Espadon" or prefijos=="Katana" or prefijos=="Pica" or prefijos=="Claymore" or prefijos=="Pico"):

				manos=2
				dañoMax+=(dañoMax*50)/100
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
			print(nombre,", nivel ",nivelItem," ",manos," mano/s | ",dañoMin,"-",dañoMax," | ",f,"-",agu,"-",agi,"-",intl,"-",m," | $",valor)

		elif(tipo=="armadura"):

			# TIPO
			tipo=choice(["cabeza","pecho","piernas","pies"])
			
			# NOMRBE
			if(tipo=="cabeza"):

				prefijos=["Casco","Gorro","Capucha","Yelmo","Almete","Sallet",]
				prefijo=choice(prefijos)

				if(prefijo=="Casco"):
					prefijo+=choice([" de hierro"," de acero"," de guerrero"])
				elif(prefijo=="Gorro"):
					prefijo+=choice([" de cuero"," de mago"])				

			elif(tipo=="pecho"):

				prefijos=["Armadura","Pechera","Coraza","Poncho","Camiza","Chaleco","Tunica","Cota de malla","Chaqueta de cuero",]
				prefijo=choice(prefijos)

				if(prefijo=="Armadura"):
					prefijo+=choice([""," de acero"," de hierro"," de cuero"])
				elif(prefijo=="Pechera"):
					prefijo+=choice([""," de acero"," de hierro"," de cuero"])
				elif(prefijo=="Chaleco"):
					prefijo+=choice([""," de cuero"," de tela"])	

			elif(tipo=="piernas"):

				prefijo="Pantalones"

			elif(tipo=="pies"):
			
				prefijos=["Botas","Botas de cuero","Botas de hierro","Botas de acero","Zapatos"]	
				prefijo=choice(prefijos)

			# sufijos	
			sufijos=[""," de la codicia"," del miedo"," de la locura"," de la esperanza", " bendecida/o"," de plebeyo"," de guerrero"," de mago"," de picaro"," de lacayo"," del amor"," del odio"]

			if(rareza==1):

				sufijos+=[" de escarcha"," de fuego"," de toxina"," electrico"," con daños"," del mal"," del bien"]
			
			elif(rareza==2):

				sufijos+=[" de escarcha"," de fuego"," de toxina"," electrico"," con daños"," del mal"," del bien"," invernal"," de calor"," venenoza/o"," de rayo"," de calidad"," de la luz"," de la oscuridad"," infernal"," celestial"," real"," de la victoria"]

			elif(rareza==3):
		
				sufijos+=[" de escarcha"," de fuego"," de toxina"," electrico"," con daños"," del mal"," del bien"," invernal"," de calor"," venenoza/o"," de rayo"," de calidad"," de la luz"," de la oscuridad"," infernal"," celestial"," real"," de la victoria"," gelido/a"," de ceniza"," de llamas"," letal"," de la tormenta"," impecable"," profano"," del rey", " divino/a"," del cielo"," del infierno"," del dragon"]

			sufijo=choice(sufijos)

			nombre=prefijo+sufijo

			# ARMADURA
			arm=nivelItem*2

			#la armadura aumenta depende de el tipo
			if(tipo=="piernas"):
				arm+=round((arm*20)/100)
			elif(tipo=="pecho"):	
				arm+=round((arm*40)/100)

			# valor
			valor=arm+nivelItem*2

			#estadisticas
			f=0
			agi=0
			agu=0
			m=0
			intl=0

			aux=randint(1,nivelItem)
			for i in range(0,aux):
				
				stat=choice([1,2,3,4,5,6])
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

			self.personaje.inventario.append(Armadura(nombre,valor,nivelItem,tipo,arm,f,agu,agi,intl,m))	
			self.refrescarInventario()	
			print(nombre," (nivel ",nivelItem,")| arm",arm," $",valor, " | ",f," - ",agu," - ",agi," - ",intl," - ",m)

		self.crearFrameSuperior()
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
				self.lb_recom=Label(self.frameRecompenza,text="                                  ",fg="white",bg="green").place(x=20,y=5)
			
			elif(rareza==2):

				if(self.personaje.llaves1>0):

					self.generarTesoro()
					self.precaucionRecom=False

					# reseteo de imagenes
					self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
					self.imagenCofre=Label(self.frameRecompenza,image=imagenCofreAbierto).place(x=20,y=30)
					self.lb_recom=Label(self.frameRecompenza,text="                                 ",fg="white",bg="green").place(x=20,y=5)
				else:

					self.precaucionRecom=False

					# reseteo de imagenes
					self.nivelCofre=Label(self.frameRecompenza,image=e0).place(x=110,y=30)
					self.imagenCofre=Label(self.frameRecompenza,image=imagenCuadradoBlanco).place(x=20,y=30)
					self.lb_recom=Label(self.frameRecompenza,text="                                 ",fg="white",bg="green").place(x=20,y=5)

					self.txt_Consola.insert(1.5,f"{self.turno}) no tienes llaves 1\n")

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
	
					self.txt_Consola.insert(1.5,f"{self.turno}) no tienes llaves 2\n")

		else:
		
			print("no hay cofre")				

	def infoItem(self,idItem):

		if(idItem==""):
			return

		if(type(self.personaje.inventario[int(idItem)])==Arma or type(self.personaje.inventario[int(idItem)])==Armadura):
			
			self.personaje.inventario[int(idItem)].ver()
			# self.objetoEDUA.set("")
			# self.crearFrameEstadisticas()
			# self.crearFrameSuperior()Expandido

	def probabilidadTesoro(self):

		# borrar para que hayan recompenzas
		# return

		# Probabilidad de aparicion de un cofre
		p=choice([0,0,0,0,0,0,0,1])

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
		self.aumentarHora(int(self.consola.get()))