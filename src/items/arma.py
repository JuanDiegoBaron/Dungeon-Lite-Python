from items import Item

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

				print("se equipo en la mano derecha:",self.nombre)

			elif(partida.personaje.equipamiento["mano derecha"]==self.nombre):

				partida.personaje.equipamiento["mano derecha"]="vacio"
				partida.personaje.dañoMin-=self.dañoMinimo
				partida.personaje.dañoMax-=self.dañoMaximo
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

				print("se desequipo de la mano derecha:",self.nombre)

			elif(partida.personaje.equipamiento["mano izquierda"]=="vacio"):

				partida.personaje.equipamiento["mano izquierda"]=self.nombre
				partida.personaje.dañoMin+=self.dañoMinimo
				partida.personaje.dañoMax+=self.dañoMaximo
				partida.personaje.fuerza+=self.fuerza
				partida.personaje.aguante+=self.aguante
				partida.personaje.agilidad+=self.agilidad
				partida.personaje.inteligencia+=self.inteligencia
				partida.personaje.magia+=self.magia

				print("se equipo en una mano izquierda:",self.nombre)

			elif(partida.personaje.equipamiento["mano izquierda"]==self.nombre):

				partida.personaje.equipamiento["mano izquierda"]="vacio"
				partida.personaje.dañoMin-=self.dañoMinimo
				partida.personaje.dañoMax-=self.dañoMaximo
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

				print("se desequipo de la mano izquierda",self.nombre)

		elif(self.manos==2):

			if(partida.personaje.equipamiento["mano derecha"]=="vacio" and partida.personaje.equipamiento["mano izquierda"]=="vacio"):

				partida.personaje.equipamiento["mano derecha"]=self.nombre
				partida.personaje.equipamiento["mano izquierda"]=self.nombre
				partida.personaje.dañoMin+=self.dañoMinimo
				partida.personaje.dañoMax+=self.dañoMaximo
				partida.personaje.fuerza+=self.fuerza
				partida.personaje.aguante+=self.aguante
				partida.personaje.agilidad+=self.agilidad
				partida.personaje.inteligencia+=self.inteligencia
				partida.personaje.magia+=self.magia

				print("se equipo en las dos mano:",self.nombre)

			elif(partida.personaje.equipamiento["mano derecha"]==self.nombre and partida.personaje.equipamiento["mano izquierda"]==self.nombre):

				partida.personaje.equipamiento["mano derecha"]="vacio"
				partida.personaje.equipamiento["mano izquierda"]="vacio"
				partida.personaje.dañoMin-=self.dañoMinimo
				partida.personaje.dañoMax-=self.dañoMaximo
				partida.personaje.fuerza-=self.fuerza
				partida.personaje.aguante-=self.aguante
				partida.personaje.agilidad-=self.agilidad
				partida.personaje.inteligencia-=self.inteligencia
				partida.personaje.magia-=self.magia

				print("se desequipo de las dos manos:",self.nombre)

	def ver(self):

		self.carta=Frame(partida.framePrincipal,width=500,height=1000,bg="blue")
		self.carta.place(x=285,y=250)
