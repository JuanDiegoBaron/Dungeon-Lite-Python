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
		self.estados=[] # ATURDIDIDO/CEGADO/ENVENENADO/MALDITO/SILENCIADO/FURIOSO/CORRUPTO/DESANGRADO/FORTALEZA/INMUNIDAD/BENDECIDO/INSPIRADO/RAPIDEZ/

		self.celdasAvanzadas=0
		self.movimientos=0

		self.oro=0
		self.inventario=[]
		self.materiales={"Madera":0,"Piedra":0,"Cuero":0,"Tela":0,"Arcilla":0,"Mineral de hierro":0,"Mineral de oro":0,"Hueso":0,"Cristal":0,"Hierro":0,"Oro":0,"Rubi":0,"Zafiro":0,"Esmeralda":0,"Cuero refinado":0,"Tela de calidad":0,"Madera refinada":0,"Piedra refinada":0,"Ladrillo":0,"Alma":0,"Polvo de estrellas":0,"Diamante":0,"Corazon de piedra":0,"Escama de dragon":0,"Flor de fuego":0,"Runa":0}
		self.llaves1=1
		self.llaves2=1
		self.llaves3=1
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

		if(self.exp+XP>self.sigNivel):

			self.exp=(self.exp+XP)-self.sigNivel
			self.sigNivel+=round(self.sigNivel*0.5)

		elif(self.exp+XP==self.sigNivel):
			
			self.exp=0
			self.sigNivel+=round(self.sigNivel*0.5)

		else:
		
			self.exp+=XP	

	def EDUA(self):

		if(partida.objetoEDUA.get()==""):
			return

		if(type(partida.personaje.inventario[int(partida.objetoEDUA.get())])==Arma or type(partida.personaje.inventario[int(partida.objetoEDUA.get())])==Armadura):
			
			partida.personaje.inventario[int(partida.objetoEDUA.get())].equiparDesequipar()
			partida.objetoEDUA.set("")
			partida.crearFrameEstadisticas()
			partida.crearFrameSuperior()