class Enemigo:

	def __init__(self,tipo,nombre,nivel,dañoMin,dañoMax,dañoMagico,vidaMax,vida,armadura,exp,oro):

		self.id=0
		self.tipo=tipo # Jefe / Subjefe / Esbirro
		self.nombre=nombre
		self.nivel=nivel
		self.dañoMin=dañoMin
		self.dañoMax=dañoMax
		self.dañoMagico=dañoMagico
		self.vidaMax=vidaMax
		self.vida=vida
		self.armadura=armadura
		# self.resistenciaMagica=0
		self.expRecom=exp
		self.oroRecom=oro
		self.estados=""

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